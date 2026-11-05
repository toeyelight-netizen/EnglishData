"""Installment 07 (British and American Romantic, c. 1789-1832), batch b8.

MAP_B8 maps each exact work title authored in
``data/works/installment_07_works_batch8.json`` to the tuple
``([authors], [genres], [themes], [movements])`` used by the loader.
Author names are limited to the authors owned by this batch plus
Joanna Baillie, whose author record is written in batch b3, and every
taxonomy name is copied verbatim from ``scripts/_i07_taxonomy_names.txt``.
"""

MAP_B8 = {
    "Helpstone": (
        ["John Clare"],
        ["Topographical and Descriptive Poetry", "Nature Lyric and Meditation"],
        [
         "Industry, enclosure, and the changed countryside",
         "Rural labour, depopulation, and the deserted village",
         "Poverty, dependence, and the professional writer"
        ],
        ["Labouring-Class and Village Poetry"]),
    "The Village Minstrel, and Other Poems": (
        ["John Clare"],
        [
         "Metrical Tale and Romance in Verse",
         "Lyrical Ballad and Popular Stanza"
        ],
        [
         "Industry, enclosure, and the changed countryside",
         "Poverty, dependence, and the professional writer",
         "Memory and the growth of the poet's mind"
        ],
        ["Labouring-Class and Village Poetry"]),
    "The Shepherd's Calendar; with Village Stories, and Other Poems": (
        ["John Clare"],
        ["Pastoral Poetry", "Topographical and Descriptive Poetry"],
        [
         "Industry, enclosure, and the changed countryside",
         "Rural labour, depopulation, and the deserted village",
         "Natural history, science, and the poetic eye"
        ],
        ["Labouring-Class and Village Poetry"]),
    "The Rural Muse": (
        ["John Clare"],
        ["Nature Lyric and Meditation", "Romantic Sonnet Revival"],
        [
         "Poetic solitude and the conversation with nature",
         "Nature, landscape, and the shaping mind",
         "Poverty, dependence, and the professional writer"
        ],
        ["Labouring-Class and Village Poetry"]),
    "The Farmer's Boy": (
        ["Robert Bloomfield"],
        ["Topographical and Descriptive Poetry", "Pastoral Poetry"],
        [
         "Rural labour, depopulation, and the deserted village",
         "Industry, enclosure, and the changed countryside",
         "Patronage and the literary marketplace"
        ],
        ["Labouring-Class and Village Poetry"]),
    "Whims and Oddities": (
        ["Thomas Hood"],
        ["Mock-Heroic and Verse Satire", "The Sketch and Character Tale"],
        [
         "Wit, ridicule, and the war against dullness",
         "Poverty, dependence, and the professional writer",
         "The annual, the keepsake, and the gift-book economy"
        ],
        ["Regency Popular Verse and the Annual Public"]),
    "National Tales": (
        ["Thomas Hood"],
        ["Prose Fiction and the Early Novel", "The Sketch and Character Tale"],
        [
         "Revenge and justice",
         "Blood-feud, vengeance, and kinship",
         "Love, constancy, and betrayal"
        ],
        ["Regency Popular Verse and the Annual Public"]),
    "The Plea of the Midsummer Fairies": (
        ["Thomas Hood"],
        [
         "Metrical Tale and Romance in Verse",
         "Literary Annual and Keepsake Verse"
        ],
        [
         "Imagination as a way of knowing",
         "Idealized love and the lost beloved",
         "The supernatural ballad and willed belief"
        ],
        ["Regency Popular Verse and the Annual Public"]),
    "The Dream of Eugene Aram": (
        ["Thomas Hood"],
        [
         "Metrical Tale and Romance in Verse",
         "Lyrical Ballad and Popular Stanza"
        ],
        [
         "Penance, confession, and sin",
         "Rebellion, guilt, and the outcast hero",
         "Death, mourning, and the graveyard meditation"
        ],
        ["Regency Popular Verse and the Annual Public"]),
    "The Sorrows of Rosalie: A Tale, with Other Poems": (
        ["Caroline Norton"],
        [
         "Metrical Tale and Romance in Verse",
         "Literary Annual and Keepsake Verse"
        ],
        [
         "Seduction and the betrayed heroine",
         "Women's experience and the feminine voice",
         "Female authorship and the woman writer"
        ],
        [
         "Byron and the Byronic Revolt",
         "Regency Popular Verse and the Annual Public"
        ]),
    "The Undying One, and Other Poems": (
        ["Caroline Norton"],
        [
         "Literary Annual and Keepsake Verse",
         "Metrical Tale and Romance in Verse"
        ],
        [
         "Exile and homelessness",
         "Rebellion, guilt, and the outcast hero",
         "The annual, the keepsake, and the gift-book economy"
        ],
        [
         "Byron and the Byronic Revolt",
         "Regency Popular Verse and the Annual Public"
        ]),
    "Count Basil: A Tragedy": (
        ["Joanna Baillie"],
        ["Closet Drama", "Tragedy"],
        [
         "Heroism and the heroic code",
         "Love, constancy, and betrayal",
         "Warfare and battle"
        ],
        []),
    "The Tryal: A Comedy": (
        ["Joanna Baillie"],
        ["Comedy", "Closet Drama"],
        [
         "Revenge and justice",
         "Conscience and moral self-examination",
         "Sensibility, feeling, and its critics"
        ],
        []),
    "The Family Legend: A Tragedy": (
        ["Joanna Baillie"],
        ["Closet Drama", "Tragedy"],
        [
         "Blood-feud, vengeance, and kinship",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Marriage and women's conduct"
        ],
        ["Scott, the Ballad Revival and the Historical Novel"]),
    "Metrical Legends of Exalted Characters": (
        ["Joanna Baillie"],
        [
         "Metrical Tale and Romance in Verse",
         "Topographical and Descriptive Poetry"
        ],
        [
         "Heroism and the heroic code",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Colonial enterprise and the New World",
         "The transience of earthly glory (ubi sunt)"
        ],
        ["Scott, the Ballad Revival and the Historical Novel"]),
    "The Bride's Tragedy": (
        ["Thomas Lovell Beddoes"],
        ["Closet Drama", "Tragedy"],
        [
         "Revenge and justice",
         "Love, constancy, and betrayal",
         "Death, the soul, and the afterlife"
        ],
        []),
    "Death's Jest-Book; or, The Fool's Tragedy": (
        ["Thomas Lovell Beddoes"],
        ["Closet Drama", "Tragedy"],
        [
         "Death, the soul, and the afterlife",
         "Revenge and justice",
         "Dream, intoxication, and the divided mind",
         "Judgment Day and eschatology"
        ],
        ["Gothic and the Literature of Terror"]),
    "Graham Hamilton": (
        ["Lady Caroline Lamb"],
        ["Historical Novel and Romance"],
        [
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Religious persecution and martyrdom",
         "Love, constancy, and betrayal"
        ],
        ["Scott, the Ballad Revival and the Historical Novel"]),
    "Ada Reis; a Tale": (
        ["Lady Caroline Lamb"],
        ["Gothic Novel and Romance of Terror"],
        [
         "Rebellion, guilt, and the outcast hero",
         "Gothic confinement and the pursued heroine",
         "Female authorship and the woman writer"
        ],
        ["Gothic and the Literature of Terror", "Byron and the Byronic Revolt"]),
    "The Forging of the Anchor": (
        ["Samuel Ferguson"],
        ["Ballad and Popular Song", "Lyrical Ballad and Popular Stanza"],
        [
         "Industry, enclosure, and the changed countryside",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Love, constancy, and betrayal"
        ],
        ["Scott, the Ballad Revival and the Historical Novel"]),
    "The Fairy Thorn": (
        ["Samuel Ferguson"],
        ["Ballad and Popular Song", "Fairy Tale and Romantic Legend"],
        [
         "The supernatural ballad and willed belief",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Monsters and the marvellous"
        ],
        ["Scott, the Ballad Revival and the Historical Novel"]),
    "Poems (1833)": (
        ["Hartley Coleridge"],
        [
         "Romantic Sonnet Revival",
         "Nature Lyric and Meditation",
         "Metrical Tale and Romance in Verse"
        ],
        [
         "Melancholy and self-analysis",
         "Idealized love and the lost beloved",
         "Death, mourning, and the graveyard meditation",
         "Colonial enterprise and the New World"
        ],
        ["Lyrical Ballads and the Lake Poets"]),
    "Researches in the South of Ireland": (
        ["Thomas Crofton Croker"],
        ["Local Guide and Topographical Prose", "Travel and Wonders Literature"],
        [
         "The literature of the nations: Scotland, Ireland, and Wales",
         "The supernatural ballad and willed belief",
         "Primitive genius and national poetry"
        ],
        ["Scott, the Ballad Revival and the Historical Novel"]),
    "The Fairy Legends and Traditions of the South of Ireland": (
        ["Thomas Crofton Croker"],
        ["Fairy Tale and Romantic Legend", "Ballad and Popular Song"],
        [
         "The supernatural ballad and willed belief",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Monsters and the marvellous",
         "Primitive genius and national poetry"
        ],
        ["Scott, the Ballad Revival and the Historical Novel"]),
    "Damon and Pythias": (
        ["John Banim"],
        ["Tragedy"],
        [
         "Loyalty and the comitatus bond",
         "Heroism and the heroic code",
         "Tyranny and the abuse of power"
        ],
        ["The Regency Stage and Popular Drama"]),
    "Revelations of the Dead-Alive": (
        ["John Banim"],
        ["Gothic Novel and Romance of Terror"],
        [
         "Death, the soul, and the afterlife",
         "Fortune and mutability",
         "Conscience and moral self-examination"
        ],
        ["Gothic and the Literature of Terror"]),
    "The Tales of the O'Hara Family, First Series": (
        ["John Banim", "Michael Banim"],
        ["The Sketch and Character Tale", "Prose Fiction and the Early Novel"],
        [
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Rural labour, depopulation, and the deserted village",
         "The supernatural ballad and willed belief"
        ],
        ["The Regency Stage and Popular Drama"]),
}
