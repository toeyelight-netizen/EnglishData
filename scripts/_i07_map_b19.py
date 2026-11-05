# -*- coding: utf-8 -*-
"""Installment-07 relationship map, batch 19 (Charlotte Smith and Mary Robinson).

Mechanical taxonomy assignment: title -> ([authors], [genres], [themes], [movements]).
Author strings are the full_names written in
data/authors/installment_07_authors_b19.json; genre, theme and movement strings are
taken verbatim from scripts/_i07_taxonomy_names.txt (or from the controlled vocabularies
already established in the database for the same period).
"""

# --- permitted authors (b19) ---
CSMITH = ["Charlotte Smith"]
MROBINSON = ["Mary Robinson"]

# --- movements (exact names from _i07_taxonomy_names.txt / established vocabulary) ---
GRAVEYARD = ["The Graveyard School and Preromantic Meditation"]
GODWIN = ["Philosophical Fiction and the Godwin Circle"]
RISEN = ["The Rise of the English Novel"]
TOPO = ["Topographical and Estate Poetry"]
BLUE = ["The Bluestockings and Women's Letters"]
SENT = ["Sentimentalism and the Culture of Feeling"]
GOTHIC = ["Gothic and the Literature of Terror"]
LAKE = ["Lyrical Ballads and the Lake Poets"]
MANNERS = ["Austen and the Novel of Manners"]

MAP_B19 = {
    "Elegiac Sonnets, and Other Poems": (
        CSMITH,
        ["Romantic Sonnet Revival", "Sonnet Sequence", "Elegy"],
        ["Death, mourning, and the graveyard meditation", "Melancholy and self-analysis",
         "Poverty, dependence, and the professional writer", "Idealized love and the lost beloved",
         "Nature, landscape, and the shaping mind", "Time, death, and immortality through verse",
         "Female authorship and the woman writer"],
        GRAVEYARD + SENT),
    "Celestina": (
        CSMITH,
        ["Sentimental and Domestic Novel", "Novel of Manners and Fashion",
         "Prose Fiction and the Early Novel"],
        ["The marriage market and the limited estate", "Sensibility, feeling, and its critics",
         "Tyranny and the abuse of power", "Marriage and women's conduct",
         "Female authorship and the woman writer", "Revolutionary hope and its disappointment"],
        RISEN),
    "Desmond": (
        CSMITH,
        ["Epistolary Fiction", "Prose Fiction and the Early Novel",
         "Sentimental and Domestic Novel"],
        ["Revolutionary hope and its disappointment", "Marriage and women's conduct",
         "Tyranny and the abuse of power", "Poverty, dependence, and the professional writer",
         "Sensibility, feeling, and its critics"],
        GODWIN + RISEN),
    "The Emigrants, A Poem, in Two Books": (
        CSMITH,
        ["Nature Lyric and Meditation", "Meditative Blank Verse",
         "Topographical and Descriptive Poetry"],
        ["Exile, travel, and the southern sojourn", "Revolutionary hope and its disappointment",
         "Nature, landscape, and the shaping mind",
         "Poverty, dependence, and the professional writer",
         "Industry, enclosure, and the changed countryside"],
        TOPO),
    "The Old Manor House": (
        CSMITH,
        ["Prose Fiction and the Early Novel", "Sentimental and Domestic Novel",
         "Novel of Manners and Fashion"],
        ["The marriage market and the limited estate", "Tyranny and the abuse of power",
         "Industry, enclosure, and the changed countryside", "Marriage and women's conduct",
         "Poverty, dependence, and the professional writer", "Fortune and mutability"],
        RISEN + GODWIN),
    "The Banished Man": (
        CSMITH,
        ["Prose Fiction and the Early Novel", "Gothic Novel and Romance of Terror",
         "Historical Novel and Romance"],
        ["Exile, travel, and the southern sojourn", "Revolutionary hope and its disappointment",
         "Tyranny and the abuse of power", "Gothic confinement and the pursued heroine",
         "Sensibility, feeling, and its critics"],
        GOTHIC + RISEN),
    "Rural Walks: In Dialogues": (
        CSMITH,
        ["Juvenile, School and Educational Book", "Conduct, Education, and Domestic Prose"],
        ["Childhood, innocence, and education", "Women's education and intellectual friendship",
         "Nature, landscape, and the shaping mind",
         "Sympathy, benevolence, and the moral sense"],
        BLUE),
    "Marchmont": (
        CSMITH,
        ["Prose Fiction and the Early Novel", "Gothic Novel and Romance of Terror",
         "Sentimental and Domestic Novel"],
        ["Tyranny and the abuse of power", "The marriage market and the limited estate",
         "Gothic confinement and the pursued heroine", "Marriage and women's conduct",
         "Female authorship and the woman writer"],
        GOTHIC + RISEN),
    "A Narrative of the Loss of the Catharine, Venus, and Piedmont Transports": (
        CSMITH,
        ["Prose", "Polemic, Pamphlet, and Open Letter"],
        ["Sea voyage and seafaring", "Sympathy, benevolence, and the moral sense",
         "Poverty, dependence, and the professional writer",
         "Female authorship and the woman writer"],
        []),
    "The Young Philosopher": (
        CSMITH,
        ["Prose Fiction and the Early Novel", "Sentimental and Domestic Novel",
         "Novel of Manners and Fashion"],
        ["Revolutionary hope and its disappointment",
         "Poverty, dependence, and the professional writer",
         "Idealized love and the lost beloved", "Marriage and women's conduct",
         "Exile, travel, and the southern sojourn"],
        GODWIN + RISEN),
    "Conversations, Introducing Poetry to the Young": (
        CSMITH,
        ["Juvenile, School and Educational Book", "Conduct, Education, and Domestic Prose"],
        ["Childhood, innocence, and education", "Women's education and intellectual friendship",
         "Memory and the growth of the poet's mind"],
        BLUE),
    "Beachy Head, and Other Poems": (
        CSMITH,
        ["Topographical and Descriptive Poetry", "Nature Lyric and Meditation",
         "Romantic Sonnet Revival"],
        ["Nature, landscape, and the shaping mind", "The sublime, terror, and the ruin",
         "Natural history, science, and the poetic eye",
         "Poverty, dependence, and the professional writer",
         "Death, mourning, and the graveyard meditation",
         "Memory and the growth of the poet's mind"],
        TOPO),
    "Poems. By Mrs. M. Robinson. In Two Volumes": (
        MROBINSON,
        ["Lyric", "Romantic Sonnet Revival", "Elegy"],
        ["Idealized love and the lost beloved", "Melancholy and self-analysis",
         "Female authorship and the woman writer", "Patronage and the literary marketplace",
         "Fortune and mutability"],
        SENT),
    "Vancenza; or, The Dangers of Credulity": (
        MROBINSON,
        ["Gothic Novel and Romance of Terror", "Epistolary Fiction"],
        ["Enthusiasm and the disease of the imagination",
         "Gothic confinement and the pursued heroine", "Seduction and the betrayed heroine",
         "Women's education and intellectual friendship"],
        GOTHIC + RISEN),
    "Monody to the Memory of the Late Queen of France": (
        MROBINSON,
        ["Elegy", "Political and Revolutionary Verse", "Lyric"],
        ["Revolutionary hope and its disappointment", "Tyranny and the abuse of power",
         "Death, mourning, and the graveyard meditation",
         "Time, death, and immortality through verse", "Consolation and endurance"],
        []),
    "Sappho and Phaon. In a Series of Legitimate Sonnets, with Other Poems, and a Ballad": (
        MROBINSON,
        ["Romantic Sonnet Revival", "Sonnet Sequence", "Lyric"],
        ["Petrarchan desire and the sonnet mistress", "Idealized love and the lost beloved",
         "Melancholy and self-analysis", "Women's experience and the feminine voice",
         "Female authorship and the woman writer"],
        SENT),
    "Walsingham; or, The Pupil of Nature. A Domestic Story": (
        MROBINSON,
        ["Prose Fiction and the Early Novel", "Gothic Novel and Romance of Terror",
         "Novel of Manners and Fashion"],
        ["Seduction and the betrayed heroine", "Gothic confinement and the pursued heroine",
         "Patronage and the literary marketplace", "Female authorship and the woman writer",
         "Enthusiasm and the disease of the imagination"],
        GOTHIC + RISEN),
    "A Letter to the Women of England, on the Injustice of Mental Subordination": (
        MROBINSON,
        ["Polemic, Pamphlet, and Open Letter", "Conduct, Education, and Domestic Prose"],
        ["Women's education and intellectual friendship", "Marriage and women's conduct",
         "Female authorship and the woman writer",
         "Politeness, fashion, and the codes of conduct"],
        BLUE),
    "The Natural Daughter; with Portraits of the Leadenhead Family": (
        MROBINSON,
        ["Novel of Manners and Fashion", "Prose Fiction and the Early Novel",
         "Sentimental and Domestic Novel"],
        ["Marriage and women's conduct", "The marriage market and the limited estate",
         "Female authorship and the woman writer", "Patronage and the literary marketplace",
         "Appearance, dissembling, and self-fashioning",
         "Politeness, fashion, and the codes of conduct"],
        MANNERS + RISEN),
    "Lyrical Tales": (
        MROBINSON,
        ["Lyrical Ballad and Popular Stanza", "Metrical Tale and Romance in Verse", "Lyric"],
        ["Seduction and the betrayed heroine", "Poverty, dependence, and the professional writer",
         "Exile, travel, and the southern sojourn", "Memory and the growth of the poet's mind",
         "Melancholy and self-analysis"],
        LAKE + GOTHIC),
    "Memoirs of the Late Mrs. Robinson, Written by Herself": (
        MROBINSON,
        ["Memoir and Autobiographical Prose"],
        ["Women's experience and the feminine voice",
         "Appearance, dissembling, and self-fashioning",
         "Patronage and the literary marketplace", "Female authorship and the woman writer",
         "Seduction and the betrayed heroine"],
        []),
}
