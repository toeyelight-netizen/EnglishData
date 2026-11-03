"""Export database tables to JSON files.

Usage:
    python scripts/export_data.py [--out data/exports]

Writes one JSON file per entity type (plus relationships) into the output
directory. Dates and timestamps are serialized as ISO strings.
"""

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from models import get_session  # noqa: E402

TABLE_LIST = [
    "periods", "movements", "genres", "themes", "sources",
    "authors", "works", "work_authors", "work_editions",
    "author_themes", "work_themes", "author_movements", "work_movements",
    "author_genres", "work_genres", "work_periods",
    "author_sources", "work_sources", "movement_sources",
    "period_movements", "author_influences",
]


def json_default(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return str(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(PROJECT_ROOT / "data" / "exports"))
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    session = get_session()
    try:
        for table in TABLE_LIST:
            rows = session.execute(text(f"SELECT * FROM {table}")).mappings().all()
            payload = [dict(row) for row in rows]
            path = out_dir / f"{table}.json"
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, ensure_ascii=False, indent=2, default=json_default)
            print(f"Exported {table}: {len(payload)} rows -> {path}")
    finally:
        session.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
