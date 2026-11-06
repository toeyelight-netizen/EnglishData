"""The installment 8-9 check queue flags character lists that name no one (the
signature of the fabricated "Picture of Mortimer and Ray" record) and does not
flag lists containing any capitalised word. These tests pin both behaviours,
including the known blind spots."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

from i08_i09_check_queue import nameless_characters  # noqa: E402


class NamelessCharactersTest(unittest.TestCase):
    def test_generic_descriptors_are_flagged(self):
        # The character list of the removed fabricated record.
        self.assertTrue(nameless_characters("the two young men; the lecturers; the reviewers; the literary circle"))
        self.assertTrue(nameless_characters("the old farmer; the son; the neighbour"))

    def test_a_proper_name_anywhere_clears_the_flag(self):
        self.assertFalse(nameless_characters("Edward Westray; Lord Blandamer; Sharnall"))
        self.assertFalse(nameless_characters("the narrator; Boris, a Russian waiter; Paddy, an Irish tramp"))
        # Known limitation: any capitalised word clears the flag, so the old
        # Winter in Moscow list ("the Moscow scene") was not flagged.
        self.assertFalse(nameless_characters("the visitors; the guides; the hotels; the Moscow scene"))
        # The invented plots listed (invented) proper names and are not flagged either.
        self.assertFalse(nameless_characters("John Easter; Lord Blandamer; the Bishop; Jolliffe"))

    def test_empty_lists_are_not_flagged(self):
        self.assertFalse(nameless_characters(None))
        self.assertFalse(nameless_characters(""))
        self.assertFalse(nameless_characters(" ; "))


if __name__ == "__main__":
    unittest.main()
