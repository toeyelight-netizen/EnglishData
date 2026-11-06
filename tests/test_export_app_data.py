"""The app export must carry each record's own links, not ids looked up in the wrong table.

Until 2026-11-06 the exporter took the first column of each link table, which
is the owner's own id: works and authors were exported with whatever genre,
theme, movement or source happened to share that id (or with none), and every
author as influenced by himself.
"""

import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from sqlalchemy import text  # noqa: E402

from export_app_data import APP_ASSET, linked_ids  # noqa: E402
from models import author_influences, engine, get_session, work_genres, work_movements  # noqa: E402


def work_id(title):
    with engine.connect() as connection:
        return connection.execute(text("select work_id from works where title = :t"), {"t": title}).scalar()


def names(table, column, key, ids):
    with engine.connect() as connection:
        return sorted(connection.execute(
            text("select %s from %s where %s in (%s)" % (column, table, key, ",".join(map(str, ids) or ["0"])))
        ).scalars())


class LinkedIdsTest(unittest.TestCase):
    def setUp(self):
        self.session = get_session()

    def tearDown(self):
        self.session.close()

    def test_returns_the_target_column(self):
        pearl = work_id("Pearl")
        genres = linked_ids(self.session, work_genres, "work_id", pearl)
        self.assertNotIn(pearl, genres)
        self.assertEqual(names("genres", "name", "genre_id", genres), ["Dream Vision", "Elegy"])
        movements = linked_ids(self.session, work_movements, "work_id", pearl)
        self.assertEqual(names("movements", "name", "movement_id", movements), ["The Alliterative Revival"])

    def test_influences_name_another_author(self):
        with engine.connect() as connection:
            author = connection.execute(text("select author_id from author_influences limit 1")).scalar()
        influences = linked_ids(self.session, author_influences, "author_id", author)
        self.assertTrue(influences)
        self.assertNotIn(author, influences)


class AssetTest(unittest.TestCase):
    """The committed asset agrees with the database for a sample of records."""

    @classmethod
    def setUpClass(cls):
        cls.asset = json.loads(APP_ASSET.read_text(encoding="utf-8"))

    def test_pearl_is_exported_with_its_own_links(self):
        pearl = [w for w in self.asset["works"] if w["title"] == "Pearl"][0]
        self.assertEqual(pearl["genres"], ["Dream Vision", "Elegy"])
        self.assertEqual(pearl["movements"], ["The Alliterative Revival"])

    def test_no_author_is_influenced_by_himself(self):
        self.assertEqual([a["name"] for a in self.asset["authors"] if a["name"] in a["influencedBy"]], [])

    def test_every_work_has_a_genre(self):
        self.assertEqual([w["title"] for w in self.asset["works"] if not w["genres"]], [])


if __name__ == "__main__":
    unittest.main()
