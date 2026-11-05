"""Read-only completeness sweep: expected titles of the period against the corpus.

An absent title is a question for the researcher, not automatically an error: some
entries belong to a neighbouring installment and some are poems that never had a
separate title page. It prints what the corpus does not carry.

Usage: python scripts/_i07_canonical_sweep.py 07
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from installment_toolkit import corpus_titles, works_for

BRITISH = [
    "Lyrical Ballads",
    "Rime of the Ancient Mariner",
    "Kubla Khan",
    "Christabel",
    "Biographia Literaria",
    "The Excursion",
    "The Prelude",
    "Aids to Reflection",
    "Childe Harold's Pilgrimage",
    "Don Juan",
    "Manfred",
    "The Corsair",
    "Prometheus Unbound",
    "Adonais",
    "The Revolt of Islam",
    "Ode to the West Wind",
    "A Defence of Poetry",
    "Frankenstein; or, The Modern Prometheus",
    "The Last Man",
    "Endymion",
    "Lamia, Isabella, The Eve of St. Agnes, and Other Poems",
    "Hyperion",
    "Songs of Innocence",
    "Songs of Experience",
    "The Marriage of Heaven and Hell",
    "Milton: a Poem",
    "Jerusalem",
    "Poems, Chiefly in the Scottish Dialect",
    "Scots Musical Museum",
    "Elegiac Sonnets",
    "Emmeline",
    "The Old Manor House",
    "Beachy Head",
    "Sappho and Phaon",
    "Walsingham",
    "The Romance of the Forest",
    "The Mysteries of Udolpho",
    "The Italian",
    "Zofloya",
    "Melmoth the Wanderer",
    "Self-Control",
    "Discipline",
    "Adeline Mowbray",
    "Glenarvon",
    "Letters from France",
    "Memoirs of Modern Philosophers",
    "Marriage",
    "The Inheritance",
    "Belinda",
    "Plays on the Passions",
    "The De Monfort",
    "The Examiner",
    "The Indicator",
    "The Liberal",
    "Blackwood's Edinburgh Magazine",
    "The Edinburgh Review",
    "The Quarterly Review",
    "The Friend",
    "Vindiciae Gallicae",
    "An Enquiry Concerning Political Justice",
    "Essay on the Principle of Population",
    "Rural Rides",
    "The Rights of Man",
    "The Lay of the Last Minstrel",
    "Waverley",
    "Guy Mannering",
    "The Antiquary",
    "Rob Roy",
    "The Heart of Midlothian",
    "Lalla Rookh",
    "The Bride of Abydos",
    "Beppo",
    "English Bards and Scotch Reviewers",
    "The Task",
    "Night Thoughts",
    "The Deserted Village",
]

AMERICAN = [
    "The Sketch Book",
    "Bracebridge Hall",
    "A Tour on the Prairies",
    "The Spy",
    "The Pioneers",
    "The Last of the Mohicans",
    "The Prairie",
    "The Deerslayer",
    "Edgar Huntly",
    "Arthur Mervyn",
    "Ormond",
    "The Coquette",
    "The Power of Sympathy",
    "The Columbiad",
    "The Vision of Columbus",
    "An Appeal in Favor of That Class of Americans Called Africans",
    "Hobomok",
    "A New-England Tale",
    "The Bravo",
    "The Journal of Major John André",
    "Poems (Sigourney)",
    "Moral Pieces",
    "The Frontier",
    "Modern Chivalry",
    "The Revenge",
    "Androborus",
    "The Battle of Blenheim",
    "Nature: An Essay",
    "The American Universal Geography",
    "Annals of the American Revolution",
    "An American Dictionary of the English Language",
    "Letters from the Federal Farmer",
    "The Rights of All",
    "Walker's Appeal",
    "The History of Mary Prince",
    "Narrative of a Five Years' Expedition",
    "Freedom's Journal",
    "The Genius of Universal Emancipation",
]


def main(installment):
    have = [t.lower() for t in (list(corpus_titles()) +
                                [w["title"] for w in works_for(installment)])]
    joined = " | " + " | ".join(have) + " | "
    for label, checklist in (("BRITISH", BRITISH), ("AMERICAN", AMERICAN)):
        print("== %s ==" % label)
        for title in checklist:
            if title.lower() not in joined:
                print("   absent: %s" % title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "07"))
