"""Detect probable duplicate records without deleting anything.

Groups authors by normalized full name and works by title + authorship status
+ composition start. Prints any group with more than one row for manual review.

Usage:
    python scripts/check_duplicates.py
"""

import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models import Author, Work, get_session  # noqa: E402


def normalize(value):
    return " ".join(str(value).lower().split())


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
    finally:
        session.close()

    print(f"\n{duplicates} potential duplicate group(s) found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
