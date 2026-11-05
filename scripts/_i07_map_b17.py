"""Installment 07 (British and American Romantic, c. 1789-1832), batch b17.

MAP_B17 maps each exact work title authored in
``data/works/installment_07_works_batch17.json`` to the tuple
``([authors], [genres], [themes], [movements])`` used by the loader.
Author names are the exact ``full_name`` strings of this installment's
Romantic minor-canonical poets, and every taxonomy name is copied verbatim
from ``scripts/_i07_taxonomy_names.txt``.
"""

MAP_B17 = {
    "Dramatic Scenes, and Other Poems": (
        ["Bryan Waller Procter"],
        ["Lyrical Ballad and Popular Stanza", "Romantic Sonnet Revival"],
        [
            "Sensibility, feeling, and its critics",
            "Idealized love and the lost beloved",
            "Poetic solitude and the conversation with nature"
        ],
        ["Regency Popular Verse and the Annual Public"]),
    "English Songs, and Other Small Poems": (
        ["Bryan Waller Procter"],
        ["Lyrical Ballad and Popular Stanza"],
        [
            "Idealized love and the lost beloved",
            "Sensibility, feeling, and its critics"
        ],
        ["Regency Popular Verse and the Annual Public"]),
    "The World before the Flood: A Poem, in Ten Cantos": (
        ["James Montgomery"],
        ["Religious Narrative Poetry", "National Epic and Didactic Poem"],
        [
            "Creation and cosmology",
            "Judgment Day and eschatology",
            "Rebellion, guilt, and the outcast hero"
        ],
        []),
    "Greenland, and Other Poems": (
        ["James Montgomery"],
        ["Topographical and Descriptive Poetry", "Nature Lyric and Meditation"],
        [
            "The transience of earthly glory (ubi sunt)",
            "Exile, travel, and the southern sojourn",
            "Nature, landscape, and the shaping mind"
        ],
        []),
    "The Descent of Liberty: A Mask": (
        ["Leigh Hunt"],
        ["Political and Revolutionary Verse", "Metrical Tale and Romance in Verse"],
        [
            "Revolutionary hope and its disappointment",
            "Tyranny and the abuse of power",
            "Liberty of conscience and religious toleration"
        ],
        ["Shelley and Radical Romanticism"]),
    "Foliage; or, Poems Original and Translated": (
        ["Leigh Hunt"],
        ["Lyrical Ballad and Popular Stanza", "Romantic Sonnet Revival"],
        [
            "Sensibility, feeling, and its critics",
            "Poetic solitude and the conversation with nature"
        ],
        ["Regency Popular Verse and the Annual Public"]),
    "The Fancy: A Selection from the Poetical Remains of the Late Peter Corcoran, Esq., of Gray's Inn, Student at Law": (
        ["John Hamilton Reynolds"],
        ["Fairy Tale and Romantic Legend", "Lyrical Ballad and Popular Stanza"],
        [
            "Dream, intoxication, and the divided mind",
            "Imagination as a way of knowing",
            "Sensibility, feeling, and its critics"
        ],
        ["Keats and the Sensuous Ode"]),
    "The Feast of the Poets; with Notes, and Other Pieces in Verse": (
        ["Leigh Hunt"],
        ["Mock-Heroic and Verse Satire", "Critical Review and Periodical Essay"],
        [
            "Poverty, dependence, and the professional writer",
            "Taste, decorum, and the rules of art",
            "Patronage and the literary marketplace"
        ],
        ["Romantic Essay, Criticism and the Review"]),
}
