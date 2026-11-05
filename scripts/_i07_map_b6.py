"""Installment 7 batch b6: British prose of argument.

Keys match data/works/installment_07_works_batch6.json exactly; taxonomy names
are taken from scripts/_i07_taxonomy_names.txt (installment-7 rows plus the
pre-existing database rows). Author strings are those the task permits for this
batch. A work is left with an empty author list only when its real author (named
in the record) is outside the permitted set for this batch; the central gate
reports those gaps rather than inventing a name.
"""

BURKE = ["Edmund Burke"]
PAINE = ["Thomas Paine"]
GODWIN = ["William Godwin"]
MALTHUS = ["Thomas Robert Malthus"]
PALEY = ["William Paley"]
CHALMERS = ["Thomas Chalmers"]
MORE = ["Hannah More"]
BENTHAM = ["Jeremy Bentham"]
JAMES_MILL = ["James Mill"]
JEFFREY = ["Francis Jeffrey"]
DAVY = ["Humphry Davy"]
JENNER = ["Edward Jenner"]
ROSCOE = ["William Roscoe"]
TAYLOR = ["Jane Taylor"]
EDGEWORTHS = ["Maria Edgeworth", "Richard Lovell Edgeworth"]
OWEN = ["Robert Owen"]
MCCULLOCH = ["John Ramsay McCulloch"]
GRAHAM = ["Maria Graham"]
SHERWOOD = ["Mary Martha Sherwood"]
MACKINTOSH = ["James Mackintosh"]
LANCASTER = ["Joseph Lancaster"]
NONE = []

REVIEW = ["Romantic Essay, Criticism and the Review"]
GODWIN_MOV = ["Philosophical Fiction and the Godwin Circle"]
LATIT = ["The Anglican and Latitudinarian Divines"]
EVANG = ["The Evangelical Revival and Hymn Writing"]
NEWSCI = ["The New Science and the Royal Society"]
DEIST = ["The English Enlightenment and Deist Controversy"]
ABOL = ["Abolitionist and Anti-Slavery Writing"]

MAP_B6 = {
    "Reflections on the Revolution in France": (
        BURKE, ["Polemic, Pamphlet, and Open Letter"],
        ["Revolutionary hope and its disappointment",
         "Order and degree: the body politic",
         "Liberty, corruption, and the decline of nations"], REVIEW),
    "An Appeal from the New to the Old Whigs": (
        BURKE, ["Polemic, Pamphlet, and Open Letter"],
        ["Revolutionary hope and its disappointment",
         "Order and degree: the body politic",
         "Liberty, corruption, and the decline of nations"], REVIEW),
    "A Letter to a Member of the National Assembly": (
        BURKE, ["Polemic, Pamphlet, and Open Letter"],
        ["Revolutionary hope and its disappointment",
         "Tyranny and the abuse of power",
         "Order and degree: the body politic"], REVIEW),
    "Letters on a Regicide Peace": (
        BURKE, ["Polemic, Pamphlet, and Open Letter", "Letters"],
        ["Revolutionary hope and its disappointment", "Warfare and battle",
         "Tyranny and the abuse of power",
         "Order and degree: the body politic"], REVIEW),
    "A Letter to a Noble Lord": (
        BURKE, ["Polemic, Pamphlet, and Open Letter"],
        ["Commerce, luxury, and commercial society",
         "Order and degree: the body politic",
         "Poverty, dependence, and the professional writer"], REVIEW),

    "Rights of Man": (
        PAINE, ["Political Treatise", "Polemic, Pamphlet, and Open Letter"],
        ["Revolutionary hope and its disappointment",
         "Order and degree: the body politic",
         "Liberty, corruption, and the decline of nations"], GODWIN_MOV),
    "The Age of Reason": (
        PAINE, ["Polemic, Pamphlet, and Open Letter", "Natural and Revealed Theology"],
        ["Doubt, faith, and secular questioning",
         "Reason, faith, and the limits of understanding",
         "Liberty of conscience and religious toleration"],
        GODWIN_MOV + DEIST),
    "Agrarian Justice": (
        PAINE, ["Political Economy and Commercial Writing", "Polemic, Pamphlet, and Open Letter"],
        ["Industry, enclosure, and the changed countryside",
         "Poverty, dependence, and the professional writer",
         "Commerce, luxury, and commercial society"], GODWIN_MOV),
    "Dissertation on First Principles of Government": (
        PAINE, ["Political Treatise"],
        ["Revolutionary hope and its disappointment",
         "Tyranny and the abuse of power",
         "Liberty, corruption, and the decline of nations"], GODWIN_MOV),

    "An Enquiry Concerning Political Justice": (
        GODWIN, ["Philosophical and Anarchist Fiction", "Political Treatise"],
        ["Revolutionary hope and its disappointment", "Tyranny and the abuse of power",
         "Progress, decay, and the philosophy of history",
         "Liberty, corruption, and the decline of nations"], GODWIN_MOV),

    "An Essay on the Principle of Population": (
        MALTHUS, ["Political Economy and Commercial Writing", "Moral Philosophy and the Theory of Society"],
        ["Poverty, dependence, and the professional writer",
         "Commerce, luxury, and commercial society",
         "Progress, decay, and the philosophy of history"], GODWIN_MOV),

    "A View of the Evidences of Christianity": (
        PALEY, ["Natural and Revealed Theology"],
        ["Reason, faith, and the limits of understanding",
         "Reformation faith and the authority of scripture",
         "Doubt, faith, and secular questioning"], LATIT),
    "Horae Paulinae": (
        PALEY, ["Natural and Revealed Theology", "Biblical Commentary and Exegesis"],
        ["Reformation faith and the authority of scripture",
         "Reason, faith, and the limits of understanding",
         "Typology and biblical interpretation"], LATIT),
    "Natural Theology": (
        PALEY, ["Natural and Revealed Theology"],
        ["Creation and cosmology",
         "Reason, faith, and the limits of understanding",
         "Nature, landscape, and the shaping mind"], LATIT),

    "Natural Theology (Bridgewater Treatise)": (
        CHALMERS, ["Natural and Revealed Theology"],
        ["Creation and cosmology",
         "Reason, faith, and the limits of understanding",
         "The New Science and experimental philosophy"], EVANG),
    "The Christian and Civic Economy of Large Towns": (
        CHALMERS, ["Moral Philosophy and the Theory of Society", "Homily (Sermon)"],
        ["The city and urban life",
         "Poverty, dependence, and the professional writer",
         "Sympathy, benevolence, and the moral sense"], EVANG),

    "Strictures on the Modern System of Female Education": (
        MORE, ["Conduct, Education, and Domestic Prose", "Humanist Educational Treatise"],
        ["Women's education and intellectual friendship",
         "Marriage and women's conduct",
         "Revolutionary hope and its disappointment"], EVANG),
    "The Cheap Repository Tracts": (
        MORE, ["Conduct, Education, and Domestic Prose", "Homily (Sermon)"],
        ["Poverty, dependence, and the professional writer",
         "The public sphere, print, and the periodical",
         "Sympathy, benevolence, and the moral sense"], EVANG),
    "Practical Piety": (
        MORE, ["Conduct, Education, and Domestic Prose", "Devotional and Mystical Writing"],
        ["Evangelical experience and assurance",
         "Conscience and moral self-examination",
         "Politeness, fashion, and the codes of conduct"], EVANG),

    "Chrestomathia": (
        BENTHAM, ["Humanist Educational Treatise", "Grammar and Didactic Prose"],
        ["Childhood, innocence, and education",
         "Humanist education and the ideal commonwealth",
         "Wisdom and learning"], GODWIN_MOV),
    "The Rationale of Reward": (
        BENTHAM, ["Moral Philosophy and the Theory of Society", "Political Economy and Commercial Writing"],
        ["Commerce, luxury, and commercial society",
         "Tyranny and the abuse of power",
         "Patronage and the literary marketplace"], GODWIN_MOV),
    "Rationale of Judicial Evidence": (
        BENTHAM, ["Critical Treatise and Dissertation", "Moral Philosophy and the Theory of Society"],
        ["Revenge and justice", "Tyranny and the abuse of power",
         "Order and degree: the body politic"], GODWIN_MOV),

    "The History of British India": (
        JAMES_MILL, ["Philosophical and National History", "History and Chronicle"],
        ["Slavery, empire, and the Atlantic world",
         "Progress, decay, and the philosophy of history",
         "Order and degree: the body politic"], GODWIN_MOV),
    "Elements of Political Economy": (
        JAMES_MILL, ["Political Economy and Commercial Writing"],
        ["Commerce, luxury, and commercial society",
         "Industry, enclosure, and the changed countryside",
         "Poverty, dependence, and the professional writer"], GODWIN_MOV),

    "Vindiciae Gallicae": (
        MACKINTOSH, ["Polemic, Pamphlet, and Open Letter", "Political Treatise"],
        ["Revolutionary hope and its disappointment",
         "Liberty, corruption, and the decline of nations",
         "Progress, decay, and the philosophy of history"], GODWIN_MOV),

    "The Edinburgh Review": (
        JEFFREY, ["Critical Review and Periodical Essay"],
        ["The public sphere, print, and the periodical",
         "Wit, ridicule, and the war against dullness",
         "Taste, decorum, and the rules of art"], REVIEW),

    "Elements of Chemical Philosophy": (
        DAVY, ["Medical and Scientific Writing", "Philosophy and Scholastic Writing"],
        ["The New Science and experimental philosophy", "Creation and cosmology",
         "Natural history, science, and the poetic eye"], NEWSCI),
    "Researches, Chemical and Philosophical": (
        DAVY, ["Medical and Scientific Writing"],
        ["The New Science and experimental philosophy",
         "Dream, intoxication, and the divided mind",
         "Medicine, healing, and the body"], NEWSCI),
    "An Inquiry into the Causes and Effects of the Variolae Vaccinae": (
        JENNER, ["Medical and Scientific Writing"],
        ["Medicine, healing, and the body",
         "The New Science and experimental philosophy"], NEWSCI),

    "The Life of Lorenzo de Medici": (
        ROSCOE, ["Prose Biography", "Philosophical and National History"],
        ["Patronage and the literary marketplace", "Tyranny and the abuse of power",
         "Taste, decorum, and the rules of art",
         "Liberty, corruption, and the decline of nations"], REVIEW),
    "The Life and Pontificate of Leo the Tenth": (
        ROSCOE, ["Prose Biography", "Philosophical and National History"],
        ["Reformation faith and the authority of scripture",
         "Ecclesiastical reform and criticism",
         "Patronage and the literary marketplace",
         "Taste, decorum, and the rules of art"], REVIEW),
    "The Wrongs of Africa": (
        ROSCOE, ["Political and Revolutionary Verse"],
        ["The slave trade and abolition", "Slavery, empire, and the Atlantic world",
         "Sympathy, benevolence, and the moral sense",
         "Commerce, luxury, and commercial society"], ABOL),
    "The Butterfly's Ball, and the Grasshopper's Feast": (
        ROSCOE, ["Fable and Apologue", "Juvenile, School and Educational Book"],
        ["Childhood, innocence, and education",
         "Natural history, science, and the poetic eye"], []),

    "Original Poems for Infant Minds": (
        TAYLOR, ["Juvenile, School and Educational Book", "Lyrical Ballad and Popular Stanza"],
        ["Childhood, innocence, and education",
         "Natural history, science, and the poetic eye",
         "Sympathy, benevolence, and the moral sense"], []),
    "Rhymes for the Nursery": (
        TAYLOR, ["Juvenile, School and Educational Book", "Lyrical Ballad and Popular Stanza"],
        ["Childhood, innocence, and education",
         "Nature, landscape, and the shaping mind",
         "Sympathy, benevolence, and the moral sense"], []),

    "The History of Little Henry and his Bearer": (
        GRAHAM, ["Juvenile, School and Educational Book", "Devotional and Mystical Writing"],
        ["Mission, conversion, and the Church", "Childhood, innocence, and education",
         "Colonial enterprise and the New World",
         "Evangelical experience and assurance"], EVANG),
    "The History of the Fairchild Family": (
        SHERWOOD, ["Juvenile, School and Educational Book", "Conduct, Education, and Domestic Prose"],
        ["Childhood, innocence, and education", "Penance, confession, and sin",
         "Evangelical experience and assurance",
         "Puritan inheritance and the secret sin"], EVANG),
    "The Little Woodman and his Dog Cæsar": (
        SHERWOOD, ["Juvenile, School and Educational Book"],
        ["Childhood, innocence, and education", "Penance, confession, and sin",
         "Sympathy, benevolence, and the moral sense",
         "Evangelical experience and assurance"], EVANG),

    "Practical Education": (
        EDGEWORTHS, ["Humanist Educational Treatise", "Conduct, Education, and Domestic Prose"],
        ["Childhood, innocence, and education",
         "The education of princes and magistrates",
         "Self-knowledge and the philosophy of the mind",
         "Humanist education and the ideal commonwealth"], GODWIN_MOV),
    "An Experiment in Education, Made at the Male Asylum of Madras": (
        LANCASTER, ["Humanist Educational Treatise", "Conduct, Education, and Domestic Prose"],
        ["Childhood, innocence, and education",
         "Humanist education and the ideal commonwealth",
         "Poverty, dependence, and the professional writer"], REVIEW),
    "Improvements in Education, as it Respects the Industrious Classes of the Community": (
        LANCASTER, ["Humanist Educational Treatise", "Conduct, Education, and Domestic Prose"],
        ["Childhood, innocence, and education",
         "Humanist education and the ideal commonwealth",
         "Poverty, dependence, and the professional writer"], REVIEW),

    "A New View of Society": (
        OWEN, ["Moral Philosophy and the Theory of Society", "Conduct, Education, and Domestic Prose"],
        ["Industry, enclosure, and the changed countryside",
         "Poverty, dependence, and the professional writer",
         "Commerce, luxury, and commercial society",
         "Childhood, innocence, and education"], GODWIN_MOV),
    "A Report to the County of Lanark": (
        OWEN, ["Political Economy and Commercial Writing", "Moral Philosophy and the Theory of Society"],
        ["Industry, enclosure, and the changed countryside",
         "Poverty, dependence, and the professional writer",
         "Commerce, luxury, and commercial society"], GODWIN_MOV),

    "The Principles of Political Economy": (
        MCCULLOCH, ["Political Economy and Commercial Writing"],
        ["Commerce, luxury, and commercial society",
         "Industry, enclosure, and the changed countryside",
         "Progress, decay, and the philosophy of history"], REVIEW),
}
