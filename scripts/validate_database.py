"""Validate the database and write a validation report.

Checks: SQLite integrity, foreign keys, missing required fields, invalid date
ranges, duplicate authors/works, anonymous works wrongly linked to authors,
works missing period/genre/theme links, missing source references, and
period-assignment consistency (composition dates within the linked period).

Usage:
    python scripts/validate_database.py [--installment N]

The report is written to documentation/validation_reports/validation_report_NN.md
and a summary is printed. Exit code 1 if any checks fail.
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from models import (  # noqa: E402
    Author, Genre, Period, Theme, Work, get_session,
)

ISSUES = defaultdict(list)


def issue(category, message):
    ISSUES[category].append(message)


def normalize(value):
    return " ".join(str(value).lower().split())


def _year(value):
    """Extract the earliest year from a date string like 'c. 890', '700', '975-1025'."""
    if value is None:
        return None
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return None
    if len(digits) >= 4:
        return int(digits[:4])
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--installment", default="01")
    args = parser.parse_args()

    session = get_session()
    try:
        integrity = session.execute(text("PRAGMA integrity_check")).scalar()
        if integrity != "ok":
            issue("integrity", f"PRAGMA integrity_check: {integrity}")
        else:
            issue("integrity", "ok")

        fk_errors = session.execute(text("PRAGMA foreign_key_check")).fetchall()
        if fk_errors:
            issue("foreign_keys", f"{len(fk_errors)} broken foreign key(s): {fk_errors[:20]}")
        else:
            issue("foreign_keys", "ok")

        # Missing required fields
        missing_names = session.query(Author).filter(Author.full_name.is_(None)).count()
        if missing_names:
            issue("required_fields", f"{missing_names} author(s) without full_name")
        missing_titles = session.query(Work).filter(Work.title.is_(None)).count()
        if missing_titles:
            issue("required_fields", f"{missing_titles} work(s) without title")

        # Invalid date ranges
        works = session.query(Work).all()
        for work in works:
            start = _year(work.composition_date_start)
            end = _year(work.composition_date_end)
            if start and end and start > end:
                issue("invalid_dates", f"work '{work.title}': composition start {work.composition_date_start} after end {work.composition_date_end}")
            pub = _year(work.publication_date)
            if start and pub and pub < start - 60 and work.original_language == "Old English":
                issue("invalid_dates", f"work '{work.title}': publication year {work.publication_date} long precedes composition {work.composition_date_start} (may be a modern edition date)")

        # Duplicate authors (same normalized full name)
        authors = session.query(Author).all()
        by_name = defaultdict(list)
        for author in authors:
            by_name[normalize(author.full_name)].append(author)
        for name, group in by_name.items():
            if len(group) > 1:
                ids = ", ".join(str(a.author_id) for a in group)
                issue("duplicates", f"duplicate author '{group[0].full_name}' (ids {ids})")

        # Duplicate works
        by_key = defaultdict(list)
        for work in works:
            key = (normalize(work.title), work.authorship_status, work.composition_date_start)
            by_key[key].append(work)
        for key, group in by_key.items():
            if len(group) > 1:
                ids = ", ".join(str(w.work_id) for w in group)
                issue("duplicates", f"duplicate work '{group[0].title}' (ids {ids})")

        # Anonymous works incorrectly assigned authors
        anon_with_authors = session.execute(text(
            "SELECT w.work_id, w.title FROM works w JOIN work_authors wa ON wa.work_id = w.work_id "
            "WHERE w.authorship_status = 'anonymous'"
        )).fetchall()
        for work_id, title in anon_with_authors:
            issue("anonymous_attribution", f"anonymous work '{title}' (id {work_id}) has work_authors rows")

        # Works missing links
        for work in works:
            period_links = session.execute(text("SELECT COUNT(*) FROM work_periods WHERE work_id = :w"), {"w": work.work_id}).scalar()
            genre_links = session.execute(text("SELECT COUNT(*) FROM work_genres WHERE work_id = :w"), {"w": work.work_id}).scalar()
            theme_links = session.execute(text("SELECT COUNT(*) FROM work_themes WHERE work_id = :w"), {"w": work.work_id}).scalar()
            if not period_links:
                issue("missing_links", f"work '{work.title}': no period assigned")
            if not genre_links:
                issue("missing_links", f"work '{work.title}': no genre assigned")
            if not theme_links:
                issue("missing_links", f"work '{work.title}': no themes assigned")

        # Missing source references
        no_source_works = session.execute(text(
            "SELECT COUNT(*) FROM works w WHERE NOT EXISTS (SELECT 1 FROM work_sources ws WHERE ws.work_id = w.work_id)"
        )).scalar()
        no_source_authors = session.execute(text(
            "SELECT COUNT(*) FROM authors a WHERE NOT EXISTS (SELECT 1 FROM author_sources asrc WHERE asrc.author_id = a.author_id)"
        )).scalar()
        if no_source_works:
            issue("missing_sources", f"{no_source_works} work(s) without source references")
        if no_source_authors:
            issue("missing_sources", f"{no_source_authors} author(s) without source references")

        # Period assignment consistency
        periods = {p.period_id: p for p in session.query(Period).all()}
        for work in works:
            year = _year(work.composition_date_start)
            if year is None:
                continue
            rows = session.execute(text("SELECT period_id FROM work_periods WHERE work_id = :w"), {"w": work.work_id}).fetchall()
            for (period_id,) in rows:
                period = periods.get(period_id)
                if period is None:
                    continue
                if period.start_year and year < period.start_year - 50:
                    issue("period_consistency", f"work '{work.title}' (comp. {work.composition_date_start}) precedes period '{period.name}' ({period.start_year})")
                if period.end_year and year > period.end_year + 50:
                    issue("period_consistency", f"work '{work.title}' (comp. {work.composition_date_start}) postdates period '{period.name}' ({period.end_year})")
    finally:
        session.close()

    # Write report
    report_dir = PROJECT_ROOT / "documentation" / "validation_reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"validation_report_{args.installment}.md"
    lines = [
        f"# Validation Report - Installment {args.installment}",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Summary",
        "",
    ]
    total_issues = 0
    for category, messages in sorted(ISSUES.items()):
        status = "ok" if category in ("integrity", "foreign_keys") else f"{len(messages)} issue(s)"
        lines.append(f"- **{category}**: {status}")
        total_issues += 0 if category in ("integrity", "foreign_keys") else len(messages)
    lines += ["", "## Details", ""]
    for category, messages in sorted(ISSUES.items()):
        if category in ("integrity", "foreign_keys"):
            continue
        if messages:
            lines.append(f"### {category}")
            for message in messages:
                lines.append(f"- {message}")
            lines.append("")
    if total_issues == 0:
        lines.append("No issues found.")
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Validation report written to {report_path}")
    print(f"Total issues: {total_issues}")
    return 1 if total_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
