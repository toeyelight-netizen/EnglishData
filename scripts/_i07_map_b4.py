"""Installment 7 batch b4: Rogers, Campbell, Moore, Hemans and Landon.

Written centrally because the batch agent failed before producing its map.
The movement "Regency Popular Verse and the Annual Public" is the 11th British
row in data/movements/installment_07_movements_british.json.
"""

ROGERS = ["Samuel Rogers"]
CAMPBELL = ["Thomas Campbell"]
MOORE = ["Thomas Moore"]
HEMANS = ["Felicia Hemans"]
LANDON = ["Letitia Elizabeth Landon"]

ANNUAL = ["Regency Popular Verse and the Annual Public"]
CRIT = ["Romantic Essay, Criticism and the Review"]

MAP_B4 = {
    "Poems (1827)": (
        ROGERS, ["Poetry", "Lyric"],
        ["Taste, decorum, and the rules of art",
         "Patronage and the literary marketplace"], ANNUAL),
    "Human Life": (
        ROGERS, ["Meditative Blank Verse"],
        ["Self-knowledge and the philosophy of the mind",
         "Reason, faith, and the limits of understanding"], ANNUAL),
    "Italy": (
        ROGERS, ["Verse Epistle"],
        ["Exile, travel, and the southern sojourn",
         "The transience of earthly glory (ubi sunt)"], ANNUAL),

    "The Pleasures of Hope": (
        CAMPBELL, ["Meditative Blank Verse", "Political Verse"],
        ["Progress, decay, and the philosophy of history",
         "Liberty, corruption, and the decline of nations"], ANNUAL),
    "Gertrude of Wyoming": (
        CAMPBELL, ["Metrical Tale and Romance in Verse"],
        ["The wilderness, settlement, and Indian removal",
         "Transatlantic exchange and cultural dependence",
         "Warfare and battle"], ANNUAL),
    "Specimens of the British Poets": (
        CAMPBELL, ["Anthology, Reliques, and Editorial Collection",
                   "Critical Treatise and Dissertation"],
        ["Taste, decorum, and the rules of art",
         "Primitive genius and national poetry"], ANNUAL + CRIT),

    "Irish Melodies": (
        MOORE, ["Lyrical Ballad and Popular Stanza", "Ballad and Popular Song"],
        ["Border, ballad, and national memory",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Liberty, corruption, and the decline of nations"], ANNUAL),
    "Intercepted Letters; or, the Two-Penny Post-Bag": (
        MOORE, ["Mock-Heroic and Verse Satire", "Verse Epistle"],
        ["Wit, ridicule, and the war against dullness",
         "The public sphere, print, and the periodical"], ANNUAL),
    "The Fudge Family in Paris": (
        MOORE, ["Mock-Heroic and Verse Satire", "Verse Epistle"],
        ["Transatlantic exchange and cultural dependence",
         "Exile, travel, and the southern sojourn",
         "Social satire and estates criticism"], ANNUAL),
    "Lalla Rookh": (
        MOORE, ["Metrical Tale and Romance in Verse",
                "Philosophical Tale and Oriental Fiction"],
        ["Exile, travel, and the southern sojourn",
         "Idealized love and the lost beloved",
         "Monsters and the marvellous"], ANNUAL),
    "The Loves of the Angels": (
        MOORE, ["Metrical Tale and Romance in Verse"],
        ["Divine love and holy desire",
         "Enthusiasm and the disease of the imagination",
         "Reason, faith, and the limits of understanding"], ANNUAL),
    "Letters and Journals of Lord Byron": (
        MOORE, ["Letters", "Literary Biography and Prefatory Commentary"],
        ["Patronage and the literary marketplace",
         "Appearance, dissembling, and self-fashioning",
         "Transatlantic exchange and cultural dependence"], ANNUAL + CRIT),

    "The Domestic Affections, and Other Poems": (
        HEMANS, ["Lyric", "Poetry"],
        ["Sensibility, feeling, and its critics",
         "Marriage and women's conduct"], ANNUAL),
    "The Forest Sanctuary": (
        HEMANS, ["Metrical Tale and Romance in Verse"],
        ["Exile and homelessness", "Gothic confinement and the pursued heroine",
         "Women's experience and the feminine voice"], ANNUAL),
    "Records of Woman": (
        HEMANS, ["Lyric", "Sonnet Sequence"],
        ["Women's experience and the feminine voice",
         "Female authorship and the woman writer",
         "Marriage and women's conduct"], ANNUAL),
    "Songs of the Affections, with Other Poems": (
        HEMANS, ["Lyric", "Hymn and Devotional Song"],
        ["Sensibility, feeling, and its critics", "Consolation and endurance",
         "Early death and the mourning of poets"], ANNUAL),

    "The Fate of Adelaide": (
        LANDON, ["Metrical Tale and Romance in Verse"],
        ["Gothic confinement and the pursued heroine",
         "Love, constancy, and betrayal"], ANNUAL),
    "The Improvisatrice": (
        LANDON, ["Metrical Tale and Romance in Verse"],
        ["Female authorship and the woman writer",
         "Idealized love and the lost beloved",
         "The annual, the keepsake, and the gift-book economy",
         "Poverty, dependence, and the professional writer"], ANNUAL),
    "The Golden Violet": (
        LANDON, ["Metrical Tale and Romance in Verse",
                 "Fairy Tale and Romantic Legend"],
        ["The annual, the keepsake, and the gift-book economy",
         "Chivalry and knighthood", "Fortune and mutability"], ANNUAL),
    "The Venetian Bracelet": (
        LANDON, ["Lyric", "English Sonnet"],
        ["The annual, the keepsake, and the gift-book economy",
         "Idealized love and the lost beloved",
         "Women's experience and the feminine voice"], ANNUAL),
}
