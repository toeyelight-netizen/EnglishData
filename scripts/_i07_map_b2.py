"""Installment 7 batch b2: Byron, Shelley, Keats and the younger generation.

Written centrally because the batch agent failed before producing its map.
Keys must match data/works/installment_07_works_batch2.json exactly; taxonomy
names are taken from scripts/_i07_taxonomy_names.txt (installment-7 rows plus
the pre-existing database rows).
"""

BYRON = ["George Gordon Byron, Sixth Baron Byron"]
SHELLEY = ["Percy Bysshe Shelley"]
KEATS = ["John Keats"]

REVOLT = ["Byron and the Byronic Revolt"]
RADICAL = ["Shelley and Radical Romanticism"]
ODE = ["Keats and the Sensuous Ode"]
CRIT = ["Romantic Essay, Criticism and the Review"]

MAP_B2 = {
    "Hours of Idleness": (
        BYRON, ["Poetry", "Verse Epistle"],
        ["Patronage and the literary marketplace"], REVOLT),
    "English Bards and Scotch Reviewers": (
        BYRON, ["Mock-Heroic and Verse Satire", "Verse Epistle"],
        ["Wit, ridicule, and the war against dullness",
         "Patronage and the literary marketplace"], REVOLT),
    "Childe Harold's Pilgrimage, Cantos I and II": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Exile, travel, and the southern sojourn",
         "Rebellion, guilt, and the outcast hero",
         "The transience of earthly glory (ubi sunt)"], REVOLT),
    "The Giaour": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Rebellion, guilt, and the outcast hero",
         "Gothic confinement and the pursued heroine",
         "The supernatural ballad and willed belief"], REVOLT),
    "The Bride of Abydos": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Idealized love and the lost beloved",
         "Exile, travel, and the southern sojourn"], REVOLT),
    "The Corsair": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Rebellion, guilt, and the outcast hero", "Sea voyage and seafaring"],
        REVOLT),
    "Childe Harold's Pilgrimage, Canto the Third": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Exile, travel, and the southern sojourn",
         "The sublime, terror, and the ruin",
         "Poetic solitude and the conversation with nature"], REVOLT),
    "The Prisoner of Chillon": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Tyranny and the abuse of power", "Exile and homelessness",
         "Rebellion, guilt, and the outcast hero"], REVOLT),
    "Manfred": (
        BYRON, ["Closet Drama"],
        ["Rebellion, guilt, and the outcast hero",
         "Doubt, faith, and secular questioning",
         "The sublime, terror, and the ruin"], REVOLT),
    "Beppo": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Exile, travel, and the southern sojourn"], REVOLT),
    "Childe Harold's Pilgrimage, Canto the Fourth": (
        BYRON, ["Metrical Tale and Romance in Verse"],
        ["Exile, travel, and the southern sojourn",
         "The transience of earthly glory (ubi sunt)",
         "Imagination as a way of knowing"], REVOLT),
    "Mazeppa": (
        BYRON, ["Metrical Tale and Romance in Verse", "Lyrical Ballad and Popular Stanza"],
        ["Rebellion, guilt, and the outcast hero", "Exile and homelessness",
         "Border, ballad, and national memory"], REVOLT),
    "Don Juan": (
        BYRON, ["Metrical Tale and Romance in Verse", "Mock-Heroic and Verse Satire"],
        ["Exile, travel, and the southern sojourn",
         "Seduction and the betrayed heroine",
         "The marriage market and the limited estate",
         "Wit, ridicule, and the war against dullness"], REVOLT),
    "Cain": (
        BYRON, ["Closet Drama"],
        ["Doubt, faith, and secular questioning",
         "Rebellion, guilt, and the outcast hero",
         "Penance, confession, and sin"], REVOLT),
    "Marino Faliero": (
        BYRON, ["Closet Drama", "Tragedy"],
        ["Tyranny and the abuse of power", "Revenge and justice",
         "The transience of earthly glory (ubi sunt)"], REVOLT),
    "The Vision of Judgment": (
        BYRON, ["Mock-Heroic and Verse Satire"],
        ["Social satire and estates criticism",
         "Doubt, faith, and secular questioning",
         "Wit, ridicule, and the war against dullness"], REVOLT),

    "The Necessity of Atheism": (
        SHELLEY, ["Polemic, Pamphlet, and Open Letter"],
        ["Doubt, faith, and secular questioning",
         "Reason, faith, and the limits of understanding",
         "Liberty of conscience and religious toleration"], RADICAL),
    "Queen Mab": (
        SHELLEY, ["Political and Revolutionary Verse", "Metrical Tale and Romance in Verse"],
        ["Revolutionary hope and its disappointment",
         "Tyranny and the abuse of power",
         "Doubt, faith, and secular questioning"], RADICAL),
    "Alastor; or, The Spirit of Solitude: And Other Poems": (
        SHELLEY, ["Nature Lyric and Meditation", "Conversation Poem and Lyric Meditation"],
        ["Poetic solitude and the conversation with nature",
         "Imagination as a way of knowing",
         "Idealized love and the lost beloved"], RADICAL),
    "Mont Blanc": (
        SHELLEY, ["Nature Lyric and Meditation"],
        ["The sublime, terror, and the ruin",
         "Nature, landscape, and the shaping mind",
         "Reason, faith, and the limits of understanding"], RADICAL),
    "The Revolt of Islam": (
        SHELLEY, ["Political and Revolutionary Verse"],
        ["Revolutionary hope and its disappointment",
         "Tyranny and the abuse of power",
         "Love, constancy, and betrayal"], RADICAL),
    "The Cenci": (
        SHELLEY, ["Closet Drama", "Tragedy"],
        ["Revenge and justice", "Seduction and the betrayed heroine",
         "Doubt, faith, and secular questioning"], RADICAL),
    "Prometheus Unbound": (
        SHELLEY, ["Closet Drama"],
        ["Tyranny and the abuse of power",
         "Revolutionary hope and its disappointment",
         "Imagination as a way of knowing"], RADICAL),
    "Ode to the West Wind": (
        SHELLEY, ["Romantic Ode"],
        ["Revolutionary hope and its disappointment",
         "Time, death, and immortality through verse",
         "Poetic solitude and the conversation with nature"], RADICAL),
    "To a Skylark": (
        SHELLEY, ["Romantic Ode"],
        ["Imagination as a way of knowing",
         "Poetic solitude and the conversation with nature"], RADICAL),
    "Epipsychidion": (
        SHELLEY, ["Metrical Tale and Romance in Verse"],
        ["Idealized love and the lost beloved", "Exile and homelessness"],
        RADICAL),
    "Adonais": (
        SHELLEY, ["Elegy", "Romantic Ode"],
        ["Early death and the mourning of poets",
         "Time, death, and immortality through verse",
         "Idealized love and the lost beloved"], RADICAL + ODE),
    "Hellas": (
        SHELLEY, ["Closet Drama"],
        ["Revolutionary hope and its disappointment",
         "Exile, travel, and the southern sojourn",
         "Liberty, corruption, and the decline of nations"], RADICAL),
    "The Masque of Anarchy": (
        SHELLEY, ["Political and Revolutionary Verse", "Lyrical Ballad and Popular Stanza"],
        ["Revolutionary hope and its disappointment",
         "Industry, enclosure, and the changed countryside",
         "Tyranny and the abuse of power"], RADICAL),
    "A Defence of Poetry": (
        SHELLEY, ["Critical Treatise and Dissertation"],
        ["Imagination as a way of knowing",
         "Taste, decorum, and the rules of art",
         "Poverty, dependence, and the professional writer"], RADICAL + CRIT),

    "On First Looking into Chapman's Homer": (
        KEATS, ["Romantic Sonnet Revival", "English Sonnet"],
        ["Imagination as a way of knowing",
         "Primitive genius and national poetry"], ODE),
    "Endymion: A Poetic Romance": (
        KEATS, ["Metrical Tale and Romance in Verse"],
        ["Idealized love and the lost beloved",
         "Imagination as a way of knowing",
         "Early death and the mourning of poets"], ODE),
    "Isabella; or, The Pot of Basil": (
        KEATS, ["Lyrical Ballad and Popular Stanza", "Fairy Tale and Romantic Legend"],
        ["Love, constancy, and betrayal", "Revenge and justice"], ODE),
    "Hyperion: A Fragment": (
        KEATS, ["National Epic and Didactic Poem", "Meditative Blank Verse"],
        ["The transience of earthly glory (ubi sunt)",
         "Progress, decay, and the philosophy of history",
         "Imagination as a way of knowing"], ODE),
    "The Eve of St. Agnes": (
        KEATS, ["Metrical Tale and Romance in Verse", "Fairy Tale and Romantic Legend"],
        ["Idealized love and the lost beloved",
         "Gothic confinement and the pursued heroine",
         "Sensibility, feeling, and its critics"], ODE),
    "Lamia": (
        KEATS, ["Metrical Tale and Romance in Verse"],
        ["Idealized love and the lost beloved",
         "Appearance, dissembling, and self-fashioning",
         "Reason, faith, and the limits of understanding"], ODE),
    "Ode to a Nightingale": (
        KEATS, ["Romantic Ode"],
        ["Imagination as a way of knowing", "Dream, intoxication, and the divided mind",
         "Time, death, and immortality through verse"], ODE),
    "Ode on a Grecian Urn": (
        KEATS, ["Romantic Ode"],
        ["Imagination as a way of knowing",
         "Time, death, and immortality through verse",
         "Taste, decorum, and the rules of art"], ODE),
    "To Autumn": (
        KEATS, ["Romantic Ode", "Nature Lyric and Meditation"],
        ["Nature, landscape, and the shaping mind",
         "Time, death, and immortality through verse",
         "Poetic solitude and the conversation with nature"], ODE),
    "The Fall of Hyperion: A Dream": (
        KEATS, ["Vision Literature", "Meditative Blank Verse"],
        ["Dream, intoxication, and the divided mind",
         "Imagination as a way of knowing",
         "Early death and the mourning of poets"], ODE),
}
