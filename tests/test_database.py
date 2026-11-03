"""Tests for database structure and integrity."""

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import inspect, text  # noqa: E402

from models import DATABASE_PATH, engine  # noqa: E402

EXPECTED_TABLES = {
    "authors", "works", "work_authors", "periods", "movements", "genres",
    "themes", "sources", "author_themes", "work_themes", "author_movements",
    "work_movements", "author_genres", "work_genres", "work_periods",
    "work_editions", "author_sources", "work_sources", "movement_sources",
    "period_movements", "author_influences",
}


class TestDatabase(unittest.TestCase):

    def test_database_file_exists(self):
        self.assertTrue(DATABASE_PATH.exists(), "master database file missing")

    def test_required_tables_exist(self):
        inspector = inspect(engine)
        tables = set(inspector.get_table_names())
        missing = EXPECTED_TABLES - tables
        self.assertFalse(missing, f"missing tables: {missing}")

    def test_integrity_check(self):
        with engine.connect() as connection:
            result = connection.execute(text("PRAGMA integrity_check")).scalar()
        self.assertEqual(result, "ok")

    def test_foreign_key_check(self):
        with engine.connect() as connection:
            rows = connection.execute(text("PRAGMA foreign_key_check")).fetchall()
        self.assertEqual(rows, [], f"broken foreign keys: {rows}")

    def test_fts5_tables_present(self):
        with engine.connect() as connection:
            try:
                count = connection.execute(text(
                    "SELECT COUNT(*) FROM sqlite_master "
                    "WHERE type = 'table' AND name IN ('works_fts', 'authors_fts')"
                )).scalar()
            except Exception:
                self.skipTest("FTS5 unavailable")
        self.assertEqual(count, 2)

    def test_fts_search_returns_rows(self):
        with engine.connect() as connection:
            try:
                rows = connection.execute(text(
                    "SELECT title FROM works_fts WHERE works_fts MATCH 'Beowulf'"
                )).fetchall()
            except Exception:
                self.skipTest("FTS5 unavailable")
        self.assertTrue(rows, "FTS search for 'Beowulf' returned no rows")


if __name__ == "__main__":
    unittest.main()
