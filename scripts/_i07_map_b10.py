# -*- coding: utf-8 -*-
"""Installment-07 relationship map, batch 10 (abolition, annuals, early-American reform).

Mechanical taxonomy assignment: title -> ([authors], [genres], [themes], [movements]).
Author strings follow the permitted b10 list; genre/theme/movement strings are taken
verbatim from scripts/_i07_taxonomy_names.txt. Where a periodical/annual has no single
named editor the author list is left empty rather than guessed.
"""

# --- permitted authors (b10) ---
WALKER = ["David Walker"]
GARRISON = ["William Lloyd Garrison"]
HEYRICK = ["Elizabeth Heyrick"]
BARKER = ["James Nelson Barker"]
CLARKSON = ["Thomas Clarkson"]
VSMITH = ["Venture Smith"]
MPRINCE = ["Mary Prince"]
STEDMAN = ["John Gabriel Stedman"]
STEWART = ["Maria W. Stewart"]
CHILD = ["Lydia Maria Child"]
LUNDY = ["Benjamin Lundy"]
NONE = []

# --- movements (exact names from _i07_taxonomy_names.txt) ---
ABOL = ["Abolitionist and Anti-Slavery Writing"]
REP = ["The Early American Republic and Its Letters"]
SCOTT = ["Scott, the Ballad Revival and the Historical Novel"]
STAGE = ["The Regency Stage and Popular Drama"]
COOPER = ["Cooper and the American Romance of Forest and Sea"]
EVANG = ["The Evangelical Revival and Hymn Writing"]
ANNUAL = ["Regency Popular Verse and the Annual Public"]

MAP_B10 = {
    "Walker's Appeal, in Four Articles; Together with a Preamble, to the Coloured Citizens of the World, but in Particular, and Very Expressly, to Those of the United States of America": (
        WALKER,
        ["Polemic, Pamphlet, and Open Letter", "Prose"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "Tyranny and the abuse of power", "Religious persecution and martyrdom"],
        ABOL + REP),

    "The Liberator": (
        GARRISON,
        ["Periodical Essay and Spectator Paper", "Critical Review and Periodical Essay"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "The public sphere, print, and the periodical", "Liberty, corruption, and the decline of nations"],
        ABOL + REP),

    "Immediate, Not Gradual Abolition; or, An Inquiry into the Shortest, Safest and Most Effectual Means of Getting Rid of West Indian Slavery": (
        HEYRICK,
        ["Polemic, Pamphlet, and Open Letter", "Political Treatise"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "Commerce, luxury, and commercial society", "Female authorship and the woman writer"],
        ABOL),

    "The Indian Princess; or, La Belle Sauvage": (
        BARKER,
        ["Melodrama and Nautical Drama", "Comic Opera and Burletta"],
        ["The wilderness, settlement, and Indian removal", "Colonial enterprise and the New World",
         "Sensibility, feeling, and its critics"],
        STAGE + COOPER),

    "The Keepsake": (
        NONE,
        ["Literary Annual and Keepsake Verse", "Anthology, Reliques, and Editorial Collection"],
        ["The annual, the keepsake, and the gift-book economy", "Patronage and the literary marketplace",
         "Idealized love and the lost beloved", "Familiar prose and the essayist's persona"],
        ANNUAL),

    "The History of the Rise, Progress, and Accomplishment of the Abolition of the African Slave-Trade, by the British Parliament": (
        CLARKSON,
        ["Philosophical and National History", "History and Chronicle"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "Commerce, luxury, and commercial society", "Sympathy, benevolence, and the moral sense"],
        ABOL + EVANG),

    "A Narrative of the Life and Adventures of Venture, a Native of Africa: But resident above sixty years in the United States of America. Related by Himself": (
        VSMITH,
        ["Slave Narrative and Abolitionist Testimony", "Memoir and Autobiographical Prose"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "Colonial enterprise and the New World", "Exile and homelessness"],
        ABOL),

    "The History of Mary Prince, a West Indian Slave. Related by Herself. With a Supplement by the Editor. To which is added, the Narrative of Asa-Asa, a Crowing Negro": (
        MPRINCE,
        ["Slave Narrative and Abolitionist Testimony", "Memoir and Autobiographical Prose"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "Women's experience and the feminine voice", "Seduction and the betrayed heroine"],
        ABOL),

    "Narrative of a Five Years' Expedition, against the Revolted Negroes of Surinam, in Guiana, on the Wild Coast of South America; from the Year 1772 to 1777": (
        STEDMAN,
        ["Travel and Wonders Literature", "Memoir and Autobiographical Prose"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "Colonial enterprise and the New World", "Love, constancy, and betrayal"],
        ABOL + EVANG),

    "Freedom's Journal": (
        ["Samuel Cornish", "John Brown Russwurm"],
        ["Periodical Essay and Spectator Paper", "Critical Review and Periodical Essay"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "The public sphere, print, and the periodical", "Republican nationhood and the claim to a national literature"],
        ABOL + REP),

    "The Genius of Universal Emancipation": (
        LUNDY,
        ["Periodical Essay and Spectator Paper", "Critical Review and Periodical Essay"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "The public sphere, print, and the periodical", "Commerce, luxury, and commercial society"],
        ABOL + REP),

    "The Forget-Me-Not": (
        NONE,
        ["Literary Annual and Keepsake Verse", "Anthology, Reliques, and Editorial Collection"],
        ["The annual, the keepsake, and the gift-book economy", "Idealized love and the lost beloved",
         "Memory and the growth of the poet's mind", "Poetic solitude and the conversation with nature"],
        ANNUAL),

    "The Bijou: An Annual Remembrancer of Literature and the Fine Arts": (
        NONE,
        ["Literary Annual and Keepsake Verse", "Anthology, Reliques, and Editorial Collection"],
        ["The annual, the keepsake, and the gift-book economy", "Patronage and the literary marketplace",
         "Idealized love and the lost beloved", "Memory and the growth of the poet's mind"],
        ANNUAL),

    "Religion and the Pure Principles of Morality, the Sure Foundation on Which We Must Build": (
        STEWART,
        ["Polemic, Pamphlet, and Open Letter", "Homily (Sermon)"],
        ["The slave trade and abolition", "Women's experience and the feminine voice",
         "Religious persecution and martyrdom", "Faith, grace, and the pilgrim's journey"],
        ABOL + EVANG),

    "The Rebels; or, Boston before the Revolution": (
        CHILD,
        ["Historical Novel and Romance", "Sentimental and Domestic Novel"],
        ["Republican nationhood and the claim to a national literature", "Warfare and battle",
         "Tyranny and the abuse of power", "Marriage and women's conduct"],
        REP + SCOTT),

    "The Juvenile Miscellany": (
        CHILD,
        ["Juvenile, School and Educational Book", "Periodical Essay and Spectator Paper"],
        ["Childhood, innocence, and education", "The education of princes and magistrates",
         "The slave trade and abolition", "Women's education and intellectual friendship"],
        REP),

    "The Literary Souvenir": (
        NONE,
        ["Literary Annual and Keepsake Verse", "Critical Review and Periodical Essay"],
        ["The annual, the keepsake, and the gift-book economy", "Patronage and the literary marketplace",
         "Familiar prose and the essayist's persona", "Poverty, dependence, and the professional writer"],
        ANNUAL),

    "The First Settlers of New-England; or, Conquest of the Pequods, Narragansets, and Pokanokets, as Related by a Father to His Children": (
        CHILD,
        ["Juvenile, School and Educational Book", "History and Chronicle"],
        ["The wilderness, settlement, and Indian removal", "Colonial enterprise and the New World",
         "Childhood, innocence, and education", "Republican nationhood and the claim to a national literature"],
        REP + SCOTT),
}
