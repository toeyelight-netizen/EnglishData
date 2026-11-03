"""Tests for idempotent imports: importing twice must not duplicate records."""

import subprocess
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from models import get_session  # noqa: E402


def count(session, table):
    return session.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()


class TestImports(unittest.TestCase):

    def test_import_is_idempotent(self):
        session = get_session()
        try:
            before = {
                "authors": count(session, "authors"),
                "works": count(session, "works"),
                "work_authors": count(session, "work_authors"),
                "work_genres": count(session, "work_genres"),
            }
        finally:
            session.close()

        result = subprocess.run(
            [sys.executable, "scripts/import_data.py"],
            cwd=PROJECT_ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, f"re-import failed: {result.stderr}")

        session = get_session()
        try:
            after = {
                "authors": count(session, "authors"),
                "works": count(session, "works"),
                "work_authors": count(session, "work_authors"),
                "work_genres": count(session, "work_genres"),
            }
        finally:
            session.close()

        self.assertEqual(before, after,
                         "re-import changed record counts (import not idempotent)")


if __name__ == "__main__":
    unittest.main()
