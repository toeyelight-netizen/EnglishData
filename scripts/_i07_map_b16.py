# -*- coding: utf-8 -*-
"""Installment-07 relationship map, batch 16.

Mechanical taxonomy assignment: title -> ([authors], [genres], [themes], [movements]).
Author strings are the exact ``authors.full_name`` values of the under-represented
installment-07 author records; genre/theme/movement strings are copied verbatim from
scripts/_i07_taxonomy_names.txt (installment-07 vocabulary where it fits, otherwise the
established database vocabulary recorded in that file).
"""

# --- permitted authors (b16) ---
HUNT = ["Leigh Hunt"]
REYNOLDS = ["John Hamilton Reynolds"]
PROCTER = ["Bryan Waller Procter"]
MONTGOMERY = ["James Montgomery"]
BARLOW = ["Joel Barlow"]
MACAULAY = ["Thomas Babington Macaulay"]
BELL = ["Andrew Bell"]

MAP_B16 = {
    # --- Leigh Hunt ---
    "The Story of Rimini: A Poem": (
        HUNT,
        ["Metrical Tale and Romance in Verse"],
        ["Idealized love and the lost beloved",
         "Sensibility, feeling, and its critics"],
        ["Regency Popular Verse and the Annual Public"]),
    "The Indicator": (
        HUNT,
        ["Critical Review and Periodical Essay",
         "Familiar Essay and Character Sketch",
         "Periodical Essay and Spectator Paper"],
        ["Familiar prose and the essayist's persona",
         "The public sphere, print, and the periodical",
         "Poverty, dependence, and the professional writer"],
        ["Romantic Essay, Criticism and the Review",
         "The Spectator and Periodical Journalism"]),
    "Lord Byron and Some of His Contemporaries": (
        HUNT,
        ["Prose Biography",
         "Memoir and Autobiographical Prose",
         "Critical Review and Periodical Essay"],
        ["Exile, travel, and the southern sojourn",
         "Poverty, dependence, and the professional writer",
         "Familiar prose and the essayist's persona"],
        ["Romantic Essay, Criticism and the Review",
         "Byron and the Byronic Revolt"]),
    # --- John Hamilton Reynolds ---
    "Peter Bell. A Lyrical Ballad": (
        REYNOLDS,
        ["Mock-Heroic and Verse Satire", "Lyrical Ballad and Popular Stanza"],
        ["Wit, ridicule, and the war against dullness",
         "Poverty, dependence, and the professional writer"],
        ["Regency Popular Verse and the Annual Public"]),
    "The Garden of Florence; and Other Poems": (
        REYNOLDS,
        ["Metrical Tale and Romance in Verse", "Romantic Sonnet Revival"],
        ["Idealized love and the lost beloved",
         "Sensibility, feeling, and its critics",
         "Memory and the growth of the poet's mind"],
        ["Regency Popular Verse and the Annual Public",
         "Keats and the Sensuous Ode"]),
    "Odes and Addresses to Great People": (
        ["John Hamilton Reynolds", "Thomas Hood"],
        ["Mock-Heroic and Verse Satire", "Pindaric Ode", "Romantic Ode"],
        ["Wit, ridicule, and the war against dullness",
         "The public sphere, print, and the periodical",
         "Patronage and the literary marketplace"],
        ["Regency Popular Verse and the Annual Public"]),
}
