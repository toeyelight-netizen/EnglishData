"""Regression tests for the medium classifier in scripts/content_enrich.py.

``family(form, genres)`` decides whether a work is verse, drama, prose fiction
or non-fiction, and so which label, metre and structure text the enrichment
gives it. Each case below was once classified wrongly.
"""

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import content_enrich as ce  # noqa: E402

LCS = "Local-Colour Sketch and the Regional Portrait"
SI = "Social Inquiry and the Documented Survey"
WAR = "War Narrative of the Common Soldier"
REVIEW = "Review Essay and Quarterly Argument"
NONSENSE = "Nonsense Verse and the Parody of Rule"

CASES = {
    "nonfiction": [
        ("Prose (regimental memoir)", [WAR, SI]),
        ("Prose (history of morals)", [LCS, REVIEW]),
        ("Prose (garden diary)", [LCS, REVIEW]),
        ("Memoir / sketches", [LCS, SI]),
        ("Impressions of the South Wiltshire Downs", [LCS, SI]),
        ("Prose narrative and essay sequence", [REVIEW]),
        ("Collected periodical sketches in two series", [REVIEW]),
        ("Comic travel narrative", [NONSENSE]),
        ("Slave narrative", []),
        ("Historical narrative (nine volumes)", []),
    ],
    "fiction": [
        ("Collection of Dakota legends", [LCS, "Idyll and Domestic Narrative Poem"]),
        ("Impressions", [LCS, "Pastoral Elegy and the Mourning Sequence"]),
        ("Novel (first of 'The Epic of the Wheat')", []),
        ("Comic narrative", [NONSENSE]),
        ("Book", ["Detective Novel and the Golden Age Mystery"]),
        ("Collection of stories", ["Dialect Poem and Vernacular Performance"]),
    ],
    "verse": [
        ("Satire", [NONSENSE]),
        ("Allegorical poem", []),
        ("Collection of allegorical prose poems", []),
        ("Novel in verse", []),
        ("Dramatic monologue", []),
        ("Prose poems", []),
        ("Monodrama (poetic monologue) with lyrics", []),
        ("Epistolary verse novelette in hexameters", []),
        ("Collection of translations from French poetry", []),
        ("Nonsense verses, stories and alphabets", []),
    ],
    "drama": [
        ("Verse drama", []),
    ],
}


class FamilyTests(unittest.TestCase):
    def test_regression_cases(self):
        for expected, cases in CASES.items():
            for form, genres in cases:
                with self.subTest(form=form, genres=genres):
                    self.assertEqual(ce.family(form, genres), expected)


class ComposeTests(unittest.TestCase):
    def test_verse_structure_default_follows_the_form(self):
        single = ce.compose_structure({"form": "Narrative poem in blank verse", "genres": []})
        self.assertIn("single continuous narrative poem", single)
        lyric = ce.compose_structure({"form": "Lyric poem", "genres": []})
        self.assertIn("single poem", lyric)
        collection = ce.compose_structure({"form": "Poetry collection", "genres": []})
        self.assertIn("collection of separate poems", collection)

    def test_metre_uses_a_genre_of_the_works_own_medium(self):
        # "narrative" is a weak prose word, so the war-narrative register suits
        # a memoir; the survey register of the second genre must not win.
        meter = ce.compose_meter({"form": "Prose (regimental memoir)", "genres": [WAR, SI]}, None)
        self.assertTrue(meter.startswith("Prose."))
        self.assertNotIn("survey", meter.split(".")[1])
        # A comic novel tagged Nonsense Verse must not get verse metre text.
        novel = ce.compose_meter({"form": "Novel", "genres": [NONSENSE]}, None)
        self.assertTrue(novel.startswith("Prose."))

    def test_label_keeps_genre_capitals(self):
        label = ce.compose_description_extra(
            {"form": "Novel", "genres": ["Provincial Novel and the British Rural Chronicle"],
             "author": "A. Writer", "pub": "1932"}, None)
        self.assertIn("Provincial Novel and the British Rural Chronicle", label)
        self.assertTrue(label.startswith("It is a prose fiction work of 1932 by A. Writer"))


if __name__ == "__main__":
    unittest.main()
