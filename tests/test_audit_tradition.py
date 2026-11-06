"""The installment 10 audit counts British, American and other traditions with
tradition(); these cases pin the classification of the recorded convention
"Nationality; description" and of ancestry clauses that name another country."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from audit_installment_10 import tradition  # noqa: E402


class TraditionTest(unittest.TestCase):
    def test_leading_nationality_decides(self):
        self.assertEqual(tradition("English; British poet, novelist and librarian"), "British")
        self.assertEqual(tradition("American; African American novelist"), "American")
        self.assertEqual(tradition("Irish; novelist and playwright"), "Irish")
        self.assertEqual(tradition("Nigerian; Yoruba (Egba) novelist writing in English"), "Other English-language")
        self.assertEqual(tradition("Barbadian; Caribbean novelist, in England from 1950"), "Other English-language")

    def test_ancestry_clause_does_not_change_tradition(self):
        # A Trinidadian writer of partly Scottish descent is not a British author.
        self.assertEqual(tradition("Trinidadian, of Indian and Scottish-Indian descent; Caribbean novelist"),
                         "Other English-language")
        # The descent clause is removed only as a phrase; the nationality before it still counts.
        self.assertEqual(tradition("Scottish, of Irish descent; poet"), "British")


if __name__ == "__main__":
    unittest.main()
