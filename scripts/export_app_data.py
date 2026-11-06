"""Export the master database into the Android app's bundled JSON asset.

Reads the cumulative SQLite database and writes a single JSON file consumed
by the Android app (android/app/src/main/assets/data/english_literature.json).
The master database remains the single source of truth; re-run this script
after any installment to refresh the app data.
"""

import datetime
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models import (  # noqa: E402
    Author,
    Genre,
    Movement,
    Period,
    Source,
    Theme,
    Work,
    WorkAuthor,
    WorkEdition,
    author_genres,
    author_influences,
    author_movements,
    author_sources,
    author_themes,
    movement_sources,
    period_movements,
    work_genres,
    work_movements,
    work_periods,
    work_sources,
    work_themes,
    get_session,
)

APP_ASSET = (
    PROJECT_ROOT / "android" / "app" / "src" / "main" / "assets" / "data" /
    "english_literature.json"
)

JSON_LIST_FIELDS = (
    "alternative_names", "pseudonyms", "major_influences",
    "alternative_titles", "editions", "modern_translations",
    "related_works", "manuscript_locations",
)


def parse_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, list) else []
    except (json.JSONDecodeError, TypeError):
        return []


def fold(value):
    text = unicodedata.normalize("NFD", str(value or "").lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return text.replace("\u00fe", "th").replace("\u00f0", "th").strip()


def installment_range():
    """Span of the installments whose works are present, e.g. "1-9"."""
    nums = sorted({int(m.group(1)) for p in (PROJECT_ROOT / "data" / "works").glob("installment_*")
                   for m in [re.match(r"installment_(\d+)_", p.name)] if m})
    if not nums:
        return ""
    return str(nums[0]) if nums[0] == nums[-1] else "%d-%d" % (nums[0], nums[-1])


def generated_date():
    """Build date; honours SOURCE_DATE_EPOCH for reproducible output."""
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc).date().isoformat()
    return datetime.date.today().isoformat()


def author_dates(record):
    parts = []
    for field in ("birth_date", "death_date"):
        value = record.get(field)
        if value:
            parts.append(str(value))
    return " \u2013 ".join(parts) if parts else ""


def work_dates(record):
    start = record.get("composition_date_start")
    end = record.get("composition_date_end")
    if start and end and start != end:
        return f"{start} \u2013 {end}"
    return str(start or end or "")


def linked_ids(session, table, id_column, id_value):
    """Ids linked to one owner through a two-column link table.

    Every link table holds the owner (``work_id`` or ``author_id``) and the
    target (``genre_id``, ``influenced_by_author_id`` ...); this returns the
    target column. Until 2026-11-06 the export took the first column, which is
    the owner's own id, so each work and author was exported with whatever
    genre, theme, movement or source happened to share its id (or with none),
    and every author as influenced by himself.
    """
    (target,) = [c for c in table.c if c.name != id_column]
    return [r[0] for r in session.execute(
        table.select().with_only_columns(target).where(table.c[id_column] == id_value)
    ).fetchall()]


def main() -> int:
    session = get_session()
    try:
        periods = [
            {
                "id": p.period_id,
                "name": p.name,
                "start": p.start_year,
                "end": p.end_year,
            }
            for p in session.query(Period).order_by(Period.start_year).all()
        ]
        genres = [g.name for g in session.query(Genre).order_by(Genre.name).all()]
        themes = [t.name for t in session.query(Theme).order_by(Theme.name).all()]
        movements = [m.name for m in session.query(Movement).order_by(Movement.name).all()]
        sources = [s.title for s in session.query(Source).order_by(Source.title).all()]

        genre_of = {g.genre_id: g.name for g in session.query(Genre).all()}
        theme_of = {t.theme_id: t.name for t in session.query(Theme).all()}
        movement_of = {m.movement_id: m.name for m in session.query(Movement).all()}
        period_of = {p.period_id: p.name for p in session.query(Period).all()}
        source_of = {s.source_id: s.title for s in session.query(Source).all()}

        authors = session.query(Author).all()
        works = session.query(Work).all()

        def names(rows, index):
            return sorted({index[r] for r in rows if r in index})

        def link_rows(table, id_column, id_value):
            return linked_ids(session, table, id_column, id_value)

        # work -> linked author rows
        work_authors = session.query(WorkAuthor).all()
        author_ids_by_work = {}
        for wa in work_authors:
            author_ids_by_work.setdefault(wa.work_id, []).append(wa.author_id)
        work_ids_by_author = {}
        for wa in work_authors:
            work_ids_by_author.setdefault(wa.author_id, []).append(wa.work_id)

        period_by_work = {
            r[0]: r[1] for r in session.execute(
                work_periods.select().with_only_columns(
                    work_periods.c.work_id, work_periods.c.period_id
                )
            ).fetchall()
        }

        work_payloads = []
        for work in works:
            record = {c.name: getattr(work, c.name) for c in work.__table__.columns}
            linked_authors = sorted(
                {a.full_name for a in authors if a.author_id in author_ids_by_work.get(work.work_id, [])}
            )
            work_payloads.append({
                "id": work.work_id,
                "title": work.title,
                "altTitles": parse_list(record.get("alternative_titles")),
                "authorship": work.authorship_status,
                "authors": linked_authors,
                "authorIds": sorted(author_ids_by_work.get(work.work_id, [])),
                "compositionStart": work.composition_date_start or "",
                "compositionEnd": work.composition_date_end or "",
                "compositionCirca": bool(record.get("composition_date_circa")),
                "dates": work_dates(record),
                "publicationDate": work.publication_date or "",
                "manuscriptDate": work.manuscript_date or "",
                "language": work.original_language or "",
                "form": work.literary_form or "",
                "period": period_of.get(period_by_work.get(work.work_id), ""),
                "description": work.description or "",
                "summary": record.get("summary") or "",
                "plot": work.plot_or_argument or "",
                "significance": record.get("significance") or work.literary_significance or "",
                "meter": work.meter_and_prosody or "",
                "context": work.historical_context or "",
                "characters": work.principal_characters or "",
                "structure": work.narrative_structure or "",
                "attributionNotes": work.attribution_notes or "",
                "canonicalStatus": record.get("canonical_status") or "",
                "genres": names(
                    link_rows(work_genres, "work_id", work.work_id), genre_of
                ),
                "themes": names(
                    link_rows(work_themes, "work_id", work.work_id), theme_of
                ),
                "movements": names(
                    link_rows(work_movements, "work_id", work.work_id), movement_of
                ),
                "editions": [
                    {
                        "title": e.edition_title or "",
                        "editor": e.editor or "",
                        "publisher": e.publisher or "",
                        "year": str(e.publication_year) if e.publication_year else "",
                    }
                    for e in sorted(
                        session.query(WorkEdition).filter_by(work_id=work.work_id).all(),
                        key=lambda e: (e.publication_year is None, e.publication_year or 0),
                    )
                ],
                "sources": names(
                    link_rows(work_sources, "work_id", work.work_id), source_of
                ),
            })

        author_payloads = []
        for author in authors:
            record = {c.name: getattr(author, c.name) for c in author.__table__.columns}
            linked_works = [
                w for w in works
                if w.work_id in work_ids_by_author.get(author.author_id, [])
            ]
            author_payloads.append({
                "id": author.author_id,
                "name": author.full_name,
                "altNames": parse_list(record.get("alternative_names")),
                "dates": author_dates(record),
                "birthplace": author.birthplace or "",
                "nationality": author.nationality_or_literary_tradition or "",
                "identity": author.literary_identity or "",
                "biography": author.biography or "",
                "profile": author.literary_profile or "",
                "style": author.stylistic_characteristics or "",
                "concerns": author.intellectual_concerns or "",
                "significance": author.historical_significance or "",
                "tier": author.significance_tier or "",
                "uncertainty": author.biographical_uncertainty or "",
                "genres": names(
                    link_rows(author_genres, "author_id", author.author_id), genre_of
                ),
                "movements": names(
                    link_rows(author_movements, "author_id", author.author_id), movement_of
                ),
                "themes": names(
                    link_rows(author_themes, "author_id", author.author_id), theme_of
                ),
                "influencedBy": names(
                    link_rows(author_influences, "author_id", author.author_id),
                    {a.author_id: a.full_name for a in authors},
                ),
                "works": sorted(
                    ({"id": w.work_id, "title": w.title} for w in linked_works),
                    key=lambda item: fold(item["title"]),
                ),
                "sources": names(
                    link_rows(author_sources, "author_id", author.author_id), source_of
                ),
            })

        author_payloads.sort(key=lambda a: fold(a["name"]))
        work_payloads.sort(key=lambda w: fold(w["title"]))

        payload = {
            "generated": generated_date(),
            "installments": installment_range(),
            "counts": {
                "authors": len(author_payloads),
                "works": len(work_payloads),
            },
            "periods": periods,
            "genres": genres,
            "themes": themes,
            "movements": movements,
            "sources": sources,
            "authors": author_payloads,
            "works": work_payloads,
        }
    finally:
        session.close()

    APP_ASSET.parent.mkdir(parents=True, exist_ok=True)
    APP_ASSET.write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    size_kb = APP_ASSET.stat().st_size / 1024
    print(f"App data written: {APP_ASSET} ({size_kb:.0f} KB)")
    print(f"  authors={len(author_payloads)} works={len(work_payloads)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
