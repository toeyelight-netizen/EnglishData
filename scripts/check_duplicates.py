"""Detect probable duplicate records without deleting anything.

Groups authors by normalized full name and works by title + authorship status
+ composition start. Prints any group with more than one row for manual review.

Also lists stale rows: database rows that no installment file defines. The
importer upserts works by title + authorship status + composition start and
never deletes, so an edit that changes one of those values (a corrected
composition date, say) leaves the old row beside its replacement, and the
grouping cannot see it because the two keys differ. Rebuilding the database
from the JSON (alembic upgrade head + import_data.py on an empty file) removes
such rows.

Usage:
    python scripts/check_duplicates.py
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models import Author, Work, get_session  # noqa: E402


def normalize(value):
    return " ".join(str(value).lower().split())


def json_keys(root=PROJECT_ROOT):
    """The importer's upsert keys for every record an installment file defines:
    works by (title, authorship status, composition start), authors by name."""
    works, authors = set(), set()
    for path in sorted((root / "data" / "works").glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for rec in payload if isinstance(payload, list) else []:
            start = rec.get("composition_date_start")
            works.add((rec["title"], rec.get("authorship_status", "single"),
                       None if start is None else str(start)))
    for path in sorted((root / "data" / "authors").glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for rec in payload if isinstance(payload, list) else []:
            authors.add(rec["full_name"])
    return works, authors


def stale_rows(work_rows, author_names, keys=None):
    """Rows that no installment file defines.

    work_rows yields (work_id, title, authorship_status, composition start);
    returns ([(work_id, title, start)], [author name]).
    """
    work_keys, json_authors = keys or json_keys()
    works = [(wid, title, start) for wid, title, status, start in work_rows
             if (title, status, None if start is None else str(start)) not in work_keys]
    return works, sorted(n for n in author_names if n not in json_authors)


def main() -> int:
    session = get_session()
    duplicates = 0
    try:
        authors = defaultdict(list)
        for author in session.query(Author).all():
            authors[normalize(author.full_name)].append(author)
        for name, group in sorted(authors.items()):
            if len(group) > 1:
                duplicates += 1
                print(f"AUTHOR duplicate '{group[0].full_name}': ids "
                      f"{[a.author_id for a in group]}")

        works = defaultdict(list)
        for work in session.query(Work).all():
            key = (normalize(work.title), work.authorship_status,
                   work.composition_date_start)
            works[key].append(work)
        for key, group in sorted(works.items()):
            if len(group) > 1:
                duplicates += 1
                print(f"WORK duplicate '{group[0].title}' "
                      f"(status={group[0].authorship_status}, "
                      f"start={group[0].composition_date_start}): ids "
                      f"{[w.work_id for w in group]}")
        stale_works, stale_authors = stale_rows(
            ((w.work_id, w.title, w.authorship_status, w.composition_date_start)
             for w in session.query(Work).all()),
            [a.full_name for a in session.query(Author).all()])
        for wid, title, start in stale_works:
            print(f"STALE work row, defined by no installment file: '{title}' "
                  f"(start={start}): id {wid}")
        for name in stale_authors:
            print(f"STALE author row, defined by no installment file: '{name}'")
    finally:
        session.close()

    print(f"\n{duplicates} potential duplicate group(s) found.")
    stale = len(stale_works) + len(stale_authors)
    print(f"{stale} stale row(s) defined by no installment file"
          + ("; rebuild the database from the JSON to remove them." if stale else "."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
