"""Installment 7 batch b5: the American strand.

Keys match data/works/installment_07_works_batch5.json exactly; taxonomy names
are taken from scripts/_i07_taxonomy_names.txt (installment-7 rows plus the
pre-existing database rows). Author strings are those the task permits for this
batch. A work is left with an empty author list only when its real author (named
in the record) is outside the permitted set for this batch, or when the record
does not attribute it confidently; the central gate reports those gaps.
"""

BROWN = ["Charles Brockden Brown"]
IRVING = ["Washington Irving"]
COOPER = ["James Fenimore Cooper"]
BRYANT = ["William Cullen Bryant"]
SEDGWICK = ["Catharine Maria Sedgwick"]
PAULDING = ["James Kirke Paulding"]
SIGOURNEY = ["Lydia Howard Sigourney"]
NEAL = ["John Neal"]
POE = ["Edgar Allan Poe"]
BRACKENRIDGE = ["Hugh Henry Brackenridge"]
DWIGHT = ["Timothy Dwight"]
WEBSTER = ["Noah Webster"]
CHANNING = ["William Ellery Channing"]
SPARKS = ["Jared Sparks"]
DANA = ["Richard Henry Dana"]
MORSE = ["Jedidiah Morse"]
HALE = ["Sarah Josepha Hale"]
HALLECK = ["Fitz-Greene Halleck"]
WEEMS = ["Mason Locke Weems"]
NONE = []

REP = ["The Early American Republic and Its Letters"]
BROWN_MOV = ["Charles Brockden Brown and the American Gothic"]
KNICK = ["The Knickerbocker Group and the American Sketch"]
COOPER_MOV = ["Cooper and the American Romance of Forest and Sea"]
BRYANT_MOV = ["Bryant and the American Nature Lyric"]
BYRON = ["Byron and the Byronic Revolt"]
CRIT = ["Romantic Essay, Criticism and the Review"]

MAP_B5 = {
    "Wieland; or, The Transformation": (
        BROWN, ["American Gothic Tale"],
        ["Puritan inheritance and the secret sin",
         "Enthusiasm and the disease of the imagination",
         "Gothic confinement and the pursued heroine"], BROWN_MOV),
    "Ormond; or, The Secret Witness": (
        BROWN, ["American Gothic Tale"],
        ["Women's experience and the feminine voice",
         "Gothic confinement and the pursued heroine",
         "Transatlantic exchange and cultural dependence"], BROWN_MOV),
    "Arthur Mervyn; or, Memoirs of the Year 1793": (
        BROWN, ["Picaresque and Journey Novel"],
        ["The city and urban life", "Medicine, healing, and the body",
         "Commerce, luxury, and commercial society"], BROWN_MOV + REP),
    "Edgar Huntly; or, Memoirs of a Sleep-Walker": (
        BROWN, ["American Gothic Tale", "Epistolary Fiction"],
        ["The wilderness, settlement, and Indian removal",
         "Dream, intoxication, and the divided mind",
         "Rebellion, guilt, and the outcast hero"], BROWN_MOV),

    "Salmagundi": (
        IRVING, ["Periodical Essay and Spectator Paper"],
        ["The city and urban life", "Wit, ridicule, and the war against dullness",
         "Familiar prose and the essayist's persona"], KNICK + REP),
    "A History of New York from the Beginning of the World to the End of the Dutch Dynasty": (
        IRVING, ["Prose Fiction and the Early Novel"],
        ["Republican nationhood and the claim to a national literature",
         "The city and urban life",
         "Wit, ridicule, and the war against dullness"], KNICK + REP),
    "The Sketch Book of Geoffrey Crayon, Gent.": (
        IRVING, ["The Sketch and Character Tale", "Fairy Tale and Romantic Legend"],
        ["Transatlantic exchange and cultural dependence",
         "Border, ballad, and national memory",
         "The supernatural ballad and willed belief"], KNICK),
    "Tales of a Traveller": (
        IRVING, ["The Sketch and Character Tale", "Fairy Tale and Romantic Legend"],
        ["Transatlantic exchange and cultural dependence",
         "Commerce, luxury, and commercial society",
         "The supernatural ballad and willed belief"], KNICK),
    "The Alhambra": (
        IRVING, ["Local Guide and Topographical Prose", "Fairy Tale and Romantic Legend"],
        ["The transience of earthly glory (ubi sunt)",
         "Transatlantic exchange and cultural dependence",
         "Border, ballad, and national memory"], KNICK),

    "The Precaution": (
        COOPER, ["Novel of Manners and Fashion"],
        ["The marriage market and the limited estate",
         "Transatlantic exchange and cultural dependence",
         "Sensibility, feeling, and its critics"], COOPER_MOV),
    "The Spy": (
        COOPER, ["Historical Novel and Romance"],
        ["Warfare and battle", "Heroism and the heroic code",
         "Republican nationhood and the claim to a national literature"],
        COOPER_MOV + REP),
    "The Pioneers": (
        COOPER, ["Frontier and Maritime Romance"],
        ["The wilderness, settlement, and Indian removal",
         "Nature, landscape, and the shaping mind",
         "Heroism and the heroic code"], COOPER_MOV),
    "The Last of the Mohicans": (
        COOPER, ["Frontier and Maritime Romance", "Historical Novel and Romance"],
        ["The wilderness, settlement, and Indian removal", "Warfare and battle",
         "Heroism and the heroic code",
         "Gothic confinement and the pursued heroine"], COOPER_MOV),
    "The Prairie": (
        COOPER, ["Frontier and Maritime Romance"],
        ["The wilderness, settlement, and Indian removal",
         "Nature, landscape, and the shaping mind",
         "Heroism and the heroic code"], COOPER_MOV),
    "The Crater": (
        COOPER, ["Frontier and Maritime Romance", "Humanist Dialogue and Utopian Fiction"],
        ["Sea voyage and seafaring", "Tyranny and the abuse of power",
         "Enthusiasm and the disease of the imagination",
         "Doubt, faith, and secular questioning"], COOPER_MOV),
    "Notions of the Americans, Picked Up by a Travelling Bachelor": (
        COOPER, ["Familiar Essay and Character Sketch"],
        ["Republican nationhood and the claim to a national literature",
         "Transatlantic exchange and cultural dependence",
         "The public sphere, print, and the periodical"], COOPER_MOV + REP),
    "The Bravo": (
        COOPER, ["Historical Novel and Romance"],
        ["Tyranny and the abuse of power",
         "Liberty, corruption, and the decline of nations",
         "Revenge and justice"], COOPER_MOV),

    "Thanatopsis": (
        BRYANT, ["Nature Lyric and Meditation"],
        ["Poetic solitude and the conversation with nature",
         "Death, mourning, and the graveyard meditation",
         "Nature, landscape, and the shaping mind"], BRYANT_MOV),
    "To a Waterfowl": (
        BRYANT, ["Nature Lyric and Meditation"],
        ["Poetic solitude and the conversation with nature",
         "Faith, grace, and the pilgrim's journey",
         "Nature, landscape, and the shaping mind"], BRYANT_MOV),
    "The Embargo; or, Sketches of the Times": (
        BRYANT, ["Mock-Heroic and Verse Satire", "Political Verse"],
        ["Commerce, luxury, and commercial society",
         "Liberty, corruption, and the decline of nations"], REP),
    "Poems (Bryant)": (
        BRYANT, ["Nature Lyric and Meditation"],
        ["Poetic solitude and the conversation with nature",
         "Nature, landscape, and the shaping mind",
         "Republican nationhood and the claim to a national literature"], BRYANT_MOV),
    "The Prairies": (
        BRYANT, ["Nature Lyric and Meditation", "Topographical and Descriptive Poetry"],
        ["The wilderness, settlement, and Indian removal",
         "Nature, landscape, and the shaping mind",
         "The transience of earthly glory (ubi sunt)"], BRYANT_MOV),

    "A New-England Tale": (
        SEDGWICK, ["Sentimental and Domestic Novel"],
        ["Puritan inheritance and the secret sin",
         "Doubt, faith, and secular questioning",
         "Women's experience and the feminine voice"], REP),
    "Redwood": (
        SEDGWICK, ["Sentimental and Domestic Novel"],
        ["The wilderness, settlement, and Indian removal",
         "Women's experience and the feminine voice",
         "Sensibility, feeling, and its critics"], REP),
    "Hope Leslie": (
        SEDGWICK, ["Historical Novel and Romance", "Sentimental and Domestic Novel"],
        ["The wilderness, settlement, and Indian removal",
         "Puritan inheritance and the secret sin",
         "Women's experience and the feminine voice"], REP),

    "The Backwoodsman": (
        PAULDING, ["National Epic and Didactic Poem", "Topographical and Descriptive Poetry"],
        ["Republican nationhood and the claim to a national literature",
         "The wilderness, settlement, and Indian removal",
         "Transatlantic exchange and cultural dependence"], KNICK + REP),
    "The Dutchman's Fireside": (
        PAULDING, ["The Sketch and Character Tale"],
        ["Border, ballad, and national memory",
         "The marriage market and the limited estate",
         "Nature, landscape, and the shaping mind"], KNICK),

    "Alnwick Castle, with Other Poems": (
        HALLECK, ["Nature Lyric and Meditation", "Elegy"],
        ["The transience of earthly glory (ubi sunt)",
         "Early death and the mourning of poets",
         "Nature, landscape, and the shaping mind"], KNICK),
    "Poems (Sigourney)": (
        SIGOURNEY, ["Elegy", "Nature Lyric and Meditation"],
        ["Death, mourning, and the graveyard meditation",
         "Women's experience and the feminine voice",
         "Consolation and endurance"], REP),
    "The Genius of Oblivion and Other Original Poems": (
        HALE, ["Elegy", "Nature Lyric and Meditation"],
        ["Death, mourning, and the graveyard meditation",
         "Consolation and endurance",
         "Women's experience and the feminine voice"], REP),
    "Mary's Lamb": (
        HALE, ["Juvenile, School and Educational Book", "Lyrical Ballad and Popular Stanza"],
        ["Childhood, innocence, and education",
         "Sympathy, benevolence, and the moral sense"], REP),

    "Logan": (
        NEAL, ["Frontier and Maritime Romance"],
        ["The wilderness, settlement, and Indian removal", "Revenge and justice",
         "Border, ballad, and national memory"], REP),
    "Seventy-Six": (
        NEAL, ["Historical Novel and Romance"],
        ["Warfare and battle",
         "Republican nationhood and the claim to a national literature",
         "Heroism and the heroic code"], REP),
    "American Writers": (
        NEAL, ["Critical Review and Periodical Essay"],
        ["Republican nationhood and the claim to a national literature",
         "Transatlantic exchange and cultural dependence",
         "The public sphere, print, and the periodical"], REP + CRIT),
    "Brother Jonathan": (
        NEAL, ["Historical Novel and Romance"],
        ["Warfare and battle",
         "Republican nationhood and the claim to a national literature",
         "Heroism and the heroic code"], REP),
    "Rachel Dyer": (
        NEAL, ["American Gothic Tale", "Historical Novel and Romance"],
        ["The wilderness, settlement, and Indian removal",
         "Gothic confinement and the pursued heroine",
         "Sea voyage and seafaring"], BROWN_MOV + REP),

    "Tamerlane and Other Poems": (
        POE, ["Metrical Tale and Romance in Verse", "Elegy"],
        ["Rebellion, guilt, and the outcast hero",
         "Idealized love and the lost beloved", "Exile and homelessness"],
        REP + BYRON),
    "Al Aaraaf, Tamerlane, and Minor Poems": (
        POE, ["Metrical Tale and Romance in Verse", "Vision Literature"],
        ["Imagination as a way of knowing", "Idealized love and the lost beloved",
         "Creation and cosmology", "Death, the soul, and the afterlife"], REP),
    "Poems (Poe)": (
        POE, ["Metrical Tale and Romance in Verse", "Elegy"],
        ["Imagination as a way of knowing", "Idealized love and the lost beloved",
         "Early death and the mourning of poets"], REP + BYRON),
    "To Helen": (
        POE, ["Lyric"],
        ["Idealized love and the lost beloved",
         "Imagination as a way of knowing"], REP),
    "The Doomed City": (
        POE, ["Vision Literature"],
        ["Death, mourning, and the graveyard meditation",
         "Penance, confession, and sin",
         "Death, the soul, and the afterlife"], REP),

    "The Life of Washington": (
        WEEMS, ["Prose Biography", "Juvenile, School and Educational Book"],
        ["Republican nationhood and the claim to a national literature",
         "Heroism and the heroic code",
         "Childhood, innocence, and education"], REP),
    "Modern Chivalry": (
        BRACKENRIDGE, ["Picaresque and Journey Novel"],
        ["Chivalry and knighthood", "Social satire and estates criticism",
         "Republican nationhood and the claim to a national literature"], REP),
    "Greenfield Hill": (
        DWIGHT, ["Topographical and Descriptive Poetry"],
        ["Country retirement and the estate poem",
         "Nature, landscape, and the shaping mind",
         "Puritan inheritance and the secret sin"], REP),
    "Travels in New-England and New-York": (
        DWIGHT, ["Local Guide and Topographical Prose", "Travel and Wonders Literature"],
        ["Nature, landscape, and the shaping mind",
         "Industry, enclosure, and the changed countryside",
         "Republican nationhood and the claim to a national literature"], REP),
    "A Compendious Dictionary of the English Language": (
        WEBSTER, ["Lexicography and Philological Writing", "Grammar and Didactic Prose"],
        ["The English vernacular and national letters",
         "Republican nationhood and the claim to a national literature",
         "National identity and Englishness"], REP),
    "An American Dictionary of the English Language": (
        WEBSTER, ["Lexicography and Philological Writing"],
        ["The English vernacular and national letters",
         "Republican nationhood and the claim to a national literature",
         "National identity and Englishness"], REP),
    "Unitarian Christianity": (
        CHANNING, ["Homily (Sermon)", "Natural and Revealed Theology"],
        ["Reason, faith, and the limits of understanding",
         "Doubt, faith, and secular questioning",
         "Liberty of conscience and religious toleration"], REP),
    "The American Universal Geography": (
        MORSE, ["Grammar and Didactic Prose", "Local Guide and Topographical Prose"],
        ["Colonial enterprise and the New World",
         "Republican nationhood and the claim to a national literature",
         "Mission, conversion, and the Church"], REP),
    "Annals of the American Revolution": (
        MORSE, ["History and Chronicle"],
        ["Warfare and battle",
         "Republican nationhood and the claim to a national literature",
         "Progress, decay, and the philosophy of history"], REP),
    "The Diplomatic Correspondence of the American Revolution": (
        SPARKS, ["History and Chronicle", "Letters"],
        ["Republican nationhood and the claim to a national literature",
         "Warfare and battle", "National identity and Englishness"], REP),
    "The Buccaneer, and Other Poems": (
        DANA, ["Metrical Tale and Romance in Verse"],
        ["Sea voyage and seafaring", "Rebellion, guilt, and the outcast hero",
         "Nature, landscape, and the shaping mind"], REP),
}
