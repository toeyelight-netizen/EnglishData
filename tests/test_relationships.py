"""Tests for many-to-many relationships and referential links."""

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from models import get_session  # noqa: E402


def query(session, sql, **params):
    return session.execute(text(sql), params).fetchall()


class TestRelationships(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = get_session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_beowulf_is_linked_to_old_english_period(self):
        rows = query(self.session,
            "SELECT COUNT(*) FROM work_periods wp "
            "JOIN works w ON w.work_id = wp.work_id "
            "JOIN periods p ON p.period_id = wp.period_id "
            "WHERE w.title = 'Beowulf' AND p.name LIKE 'Old English%'")
        self.assertEqual(rows[0][0], 1)

    def test_cynewulf_is_linked_to_elene(self):
        rows = query(self.session,
            "SELECT wa.contribution_type FROM work_authors wa "
            "JOIN works w ON w.work_id = wa.work_id "
            "JOIN authors a ON a.author_id = wa.author_id "
            "WHERE w.title = 'Elene' AND a.full_name = 'Cynewulf'")
        self.assertEqual(len(rows), 1)

    def test_anonymous_works_have_no_author_links(self):
        rows = query(self.session,
            "SELECT COUNT(*) FROM works w JOIN work_authors wa ON wa.work_id = w.work_id "
            "WHERE w.authorship_status = 'anonymous'")
        self.assertEqual(rows[0][0], 0)

    def test_every_work_has_genre_theme_period(self):
        rows = query(self.session,
            "SELECT w.title FROM works w "
            "WHERE NOT EXISTS (SELECT 1 FROM work_genres wg WHERE wg.work_id = w.work_id) "
            "OR NOT EXISTS (SELECT 1 FROM work_themes wt WHERE wt.work_id = w.work_id) "
            "OR NOT EXISTS (SELECT 1 FROM work_periods wp WHERE wp.work_id = w.work_id)")
        self.assertEqual(rows, [])

    def test_author_influence_links_are_valid(self):
        rows = query(self.session,
            "SELECT ai.author_id, ai.influenced_by_author_id FROM author_influences ai "
            "WHERE ai.author_id = ai.influenced_by_author_id")
        self.assertEqual(rows, [])

    def test_works_use_known_genres(self):
        rows = query(self.session,
            "SELECT COUNT(*) FROM work_genres wg "
            "WHERE wg.genre_id NOT IN (SELECT genre_id FROM genres)")
        self.assertEqual(rows[0][0], 0)

    def test_work_editions_reference_existing_works(self):
        rows = query(self.session,
            "SELECT COUNT(*) FROM work_editions we "
            "WHERE we.work_id NOT IN (SELECT work_id FROM works)")
        self.assertEqual(rows[0][0], 0)


if __name__ == "__main__":
    unittest.main()
