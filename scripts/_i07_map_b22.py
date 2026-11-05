# -*- coding: utf-8 -*-
"""Installment-07 relationship map, batch 22 (Burns in period, Barlow, Sigourney).

Mechanical taxonomy assignment: title -> ([authors], [genres], [themes], [movements]).
Genre/theme/movement strings are copied verbatim from scripts/_i07_taxonomy_names.txt.
Robert Burns already holds an author record in the database; Joel Barlow and Lydia
Howard Sigourney are claimed by this installment's own author file
(data/authors/installment_07_authors_b5x.json). Song anthologies to which Burns
contributed, and collections with an editor or publisher other than the named poet,
claim only the author this installment can honestly assert; the nuance sits in each
record's attribution_notes.
"""

# --- permitted authors (b22) ---
BURNS = ["Robert Burns"]
BARLOW = ["Joel Barlow"]
SIGOURNEY = ["Lydia Howard Sigourney"]

# --- movements (exact names from _i07_taxonomy_names.txt) ---
SCOTT = ["Scott, the Ballad Revival and the Historical Novel"]
LABOUR = ["Labouring-Class and Village Poetry"]
REPUBLIC = ["The Early American Republic and Its Letters"]
ANNUAL = ["Regency Popular Verse and the Annual Public"]

MAP_B22 = {
    "The Scots Musical Museum": (
        BURNS,
        ["Anthology, Reliques, and Editorial Collection", "Ballad and Popular Song"],
        ["Border, ballad, and national memory",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Primitive genius and national poetry"],
        SCOTT),

    "A Select Collection of Original Scottish Airs for the Voice": (
        BURNS,
        ["Anthology, Reliques, and Editorial Collection", "Ballad and Popular Song"],
        ["Border, ballad, and national memory",
         "The literature of the nations: Scotland, Ireland, and Wales",
         "Patronage and the literary marketplace",
         "Idealized love and the lost beloved"],
        SCOTT),

    "The Columbiad": (
        BARLOW,
        ["National Epic and Didactic Poem"],
        ["Republican nationhood and the claim to a national literature",
         "Colonial enterprise and the New World",
         "Progress, decay, and the philosophy of history",
         "Slavery, empire, and the Atlantic world"],
        REPUBLIC),

    "The Hasty-Pudding": (
        BARLOW,
        ["Mock-Heroic and Verse Satire"],
        ["Republican nationhood and the claim to a national literature",
         "Transatlantic exchange and cultural dependence"],
        REPUBLIC),
}
