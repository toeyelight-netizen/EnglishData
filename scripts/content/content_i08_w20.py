"""Installment 8: works of the American poets and the Native American
autobiography (part 20)."""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _lib import wk, wks  # noqa: F407

WOM = "The woman question, married disability, and the New Woman"
SEX = "Sexuality, the double standard, and the literature of the social evil"
LEIS = "Leisure class, the idle rich, and the unearned income"
ART = "Art versus life, and the romance of the artist"
EDU = "Education, the schools, and the cultivation of the self"
LAB = "Wage labour, the strike, and the two nations"
IND = "gospel of accumulation"
ECON = "credit, speculation, and the joint-stock imagination"
EMPIRE = "Empire, jingoism, and the literature of the metropole"
MET2 = "moneyed metropolis"
DOUBT = "Doubt, agnosticism, and the Broad Church conscience"
GRIEF = "Bereavement, immortality, and the argument from grief"
CHILD = "child labourer, and the sentimental child"
MEL = "Self-destruction, melancholy, and the coroner's verdict"
MAD = "Madness, the asylum, and the diagnosis of the will"
PRINT = "machinery of print"
GRUB = "Bohemia, the professional writer, and the Grub Street market"
SCI = "question of design"
RACE = "Race, voice, and the dialect of freedom"
SLAVE = "Slavery, emancipation, and the unfinished Reconstruction"
WILD = "The American wilderness and the myth of the forest"
FRONT = "The closing of the American frontier"
DEM = "Democracy, individualism, and the American experiment"
REG = "Regional identity and the American sectional character"
INN = "Innocence, experience, and the lost American Eden"

LAZARUS = wks("Emma Lazarus", [
 dict(title="'The New Colossus'", year="1883",
   gb="Political Verse and the Poem of Public Cause, Sonnet Revival and Sequenced Sonnet",
   tb=DEM + ", " + RACE + ", " + WOM,
   mb="The Aesthetic Turn in 1890s America, American Realism and the Howells Program",
   comp=["1883"], form="Sonnet",
   desc="Written in 1883 for the Bartholdi Pedestal Fund and inscribed on the Statue of Liberty in 1903: the founding poem of American immigration.",
   plot="The sonnet contrasts the Colossus of Rhodes, the giant of antiquity that celebrated conquest, with the American statue that stands at the harbour and cries to the old world to give her the tired, the poor, the huddled masses yearning to breathe free.",
   ctx="1883: the campaign to fund the pedestal of the Statue of Liberty, the mass immigration of the 1880s, and the American debate on the admission of the poor of Europe.",
   sig="'The New Colossus' is the most quoted American sonnet and the founding poem of the American immigration tradition: its inscription on the Statue of Liberty in 1903 made it the national statement of the purpose of America, and its lines have been quoted in every debate on immigration since.",
   canon="Major canon"),
 dict(title="Songs of a Semite: The Dance to Death and Other Poems", year="1882",
   gb="Victorian Verse Drama and Revived Tragedy, Political Verse and the Poem of Public Cause",
   tb=RACE + ", " + SLAVE + ", " + GRIEF,
   mb="The Aesthetic Turn in 1890s America",
   comp=["1880", "1882"], form="Poetry collection with verse drama",
   desc="Published in 1882 and the first English book of poetry to treat the Jewish people as a modern nation: poems of the persecutions and the Zionist hope.",
   plot="The volume contains 'The Dance to Death', a verse tragedy on the massacre of the Jews of Nordhausen in 1349, together with lyrics on the Russian pogroms of 1881, the Jewish exile, and the hope of a return to Palestine.",
   ctx="1880-82: the Russian pogroms of 1881, the beginning of American Zionism, the Jewish immigration to New York, and the English tradition of the verse tragedy.",
   sig="Songs of a Semite is the founding text of American Zionist literature and the first English poetry collection to treat Jewish persecution as a contemporary political subject: its verse tragedy on a medieval massacre made it a landmark, and it prepared the way for 'The New Colossus' and for the literature of American Zionism.",
   canon="Major canon",
   chars="Süsskind von Orb and his daughter Liebhaid ('The Dance to Death')"),
 dict(title="Admetus and Other Poems", year="1871",
   gb="Victorian Verse Drama and Revived Tragedy, Dramatic Monologue and Masked Lyric",
   tb=GRIEF + ", " + ART + ", " + SEX,
   mb="",
   comp=["1868", "1871"], form="Poetry collection with verse drama",
   desc="Published in 1871 and Lazarus's first mature collection: a verse drama on the Alcestis myth and a series of classical and personal lyrics.",
   plot="The title poem retells the story of Admetus, whose wife Alcestis dies for him, and of Heracles who brings her back from the dead; the other poems treat love, art, death and the classical inheritance in the manner of the English romantic poets.",
   ctx="1871: the American classical revival, the influence of the English poets on American verse, and the New York literary world of the 1870s.",
   sig="Admetus and Other Poems established Lazarus as one of the most accomplished American poets of her generation: its classical verse drama and its lyrics of love and death showed a mastery of form rare among American women poets, and it was praised by Emerson.",
   chars="Admetus; Alcestis; Heracles; Apollo"),
 dict(title="The Poems of Emma Lazarus", year="1889",
   gb="Dramatic Monologue and Masked Lyric, Political Verse and the Poem of Public Cause",
   tb=RACE + ", " + ART + ", " + GRIEF,
   mb="",
   comp=["1866", "1887"], form="Collected poems (two volumes, posthumous)",
   desc="Published posthumously in 1889 and the collected edition that made Lazarus's reputation: the lyrics, the verse dramas and the poems of the Jewish nation.",
   plot="The two volumes gather the whole of her poetry — the early classical lyrics, 'Admetus', 'The Spagnoletto', the Heine translations, 'The Dance to Death', the poems of the pogroms and 'The New Colossus' — with a biographical memoir by her sister.",
   ctx="1889: the year of her death, the American Jewish community of the 1880s, and the posthumous recognition of a poet who had died at thirty-eight.",
   sig="The Poems of Emma Lazarus is the collected edition that established her as the first American poet of the Jewish people and of immigration: it made 'The New Colossus' available to the campaign that inscribed it on the Statue of Liberty, and it is the essential text of her achievement.",
   canon="Major canon"),
])

LANIER = wks("Sidney Lanier", [
 dict(title="'The Marshes of Glynn'", year="1878",
   gb="Dramatic Monologue and Masked Lyric, Idyll and Domestic Narrative Poem",
   tb=WILD + ", " + DOUBT + ", " + MEL,
   mb="The Aesthetic Turn in 1890s America",
   comp=["1878"], form="Poem (irregular ode)",
   desc="Published in 1878 and the greatest American nature poem of the South: the poet's vision of the Georgia marshes at dawn.",
   plot="The poet goes out among the marshes of Glynn at dawn and feels himself dissolved into the ocean of light and air; the poem moves from the description of the marsh to a vision of the infinite, in which the self is lost and found in the divine unity of the natural world.",
   ctx="1878: the Georgia coast, the post-war South, the transcendentalist inheritance of Emerson and Whitman, and Lanier's own tuberculosis and poverty.",
   sig="'The Marshes of Glynn' is the finest American nature poem between Whitman and Frost and the central poem of the Southern landscape: its musical structure and its mystical vision made it a landmark, and it is the poem in which Lanier's theory of verse as music is most completely realized.",
   canon="Major canon"),
 dict(title="The Science of English Verse", year="1880",
   gb="Review Essay and Quarterly Argument, Social Inquiry and the Documented Survey",
   tb=ART + ", " + SCI + ", " + EDU,
   mb="",
   comp=["1879", "1880"], form="Critical treatise",
   desc="Published in 1880 and the founding work of American prosody: an attempt to reduce English verse to the laws of music.",
   plot="Lanier argues that verse is a form of music: that the rhythms of English poetry can be analysed in musical notation, that stress, quantity and pitch combine in a system of bars and notes, and that the whole history of English verse can be read as a series of musical arrangements of the same materials.",
   ctx="1880: the new science of acoustics, the American study of prosody after Lowell, the musical training of the period, and the professionalisation of literary study in the American university.",
   sig="The Science of English Verse is the founding work of American prosody and the most original English-language theory of verse of the century: its musical analysis of metre influenced Pound, Eliot and the whole modern study of versification, and it remains the starting point of any serious discussion of English rhythm.",
   canon="Major canon"),
 dict(title="Poems (Lanier, 1877)", year="1877",
   alt=["Poems"],
   gb="Dramatic Monologue and Masked Lyric, Pastoral Elegy and the Mourning Sequence",
   tb=WILD + ", " + GRIEF + ", " + ART,
   mb="",
   comp=["1867", "1877"], form="Poetry collection",
   desc="Published in 1877 and Lanier's first collection: the Southern lyrics, the war poems and the poems of music.",
   plot="The volume, the only collection Lanier published in his lifetime, contains 'Corn', 'The Symphony' and 'The Psalm of the West' with a handful of shorter lyrics, in forms that show Lanier's gift for long, musical lines and for the orchestration of a whole poem.",
   ctx="1867-77: the post-war South, the American magazine market of the 1870s, and the revival of Southern letters after Reconstruction.",
   sig="Poems established Lanier as the finest Southern poet of the post-war generation: its lyrics of the Georgia landscape and its poems of music made him a national figure, and it prepared the way for the great poems of 1878-81.",
   canon="Major canon"),
 dict(title="The English Novel", year="1883",
   gb="Review Essay and Quarterly Argument, Lecture and Popular Address",
   tb=ART + ", " + EDU + ", " + PRINT,
   mb="",
   comp=["1881"], form="Critical lectures",
   desc="Published posthumously in 1883 and Lanier's lectures on the history of the English novel: a formalist account of the development of fiction.",
   plot="Lanier traces the English novel from its origins in the romance through Fielding, Richardson, Scott, Dickens, Thackeray and Eliot, arguing that the novel is a work of art with its own laws of structure, and that its greatness lies in the organisation of character and incident into a unified design.",
   ctx="1881-83: the American lecture circuit, the professional study of literature, and the Victorian debate on the art of fiction after James and Besant.",
   sig="The English Novel is one of the earliest American works of formalist criticism of fiction and a landmark in the academic study of the novel: its lectures influenced the teaching of fiction in American universities, and it is the first American book to treat the novel as a serious art form.",
   canon="Major canon"),
])

RILEY = wks("James Whitcomb Riley", [
 dict(title="The Old Swimmin'-Hole and 'Leven More Poems", year="1883",
   gb="Dialect Poem and Vernacular Performance, Idyll and Domestic Narrative Poem",
   tb=CHILD + ", " + MEL + ", " + REG,
   mb="Local Colour and the Regionalist School, Mark Twain and the Vernacular Performance",
   comp=["1882", "1883"], form="Poetry collection (dialect)",
   desc="Published in 1883 and the little book that made Riley the Hoosier Poet: twelve dialect poems of an Indiana boyhood.",
   plot="The poems remember the swimming hole, the old schoolhouse, the country fair and the dead friends of a rural Indiana boyhood, in the Hoosier dialect of the 1850s and with a sentiment that made them instantly popular across the Midwest.",
   ctx="1882-83: rural Indiana, the small-town American Midwest of the 1850s, the newspaper poetry market, and the vogue of the dialect poem after Harte and Lowell.",
   sig="The Old Swimmin'-Hole made Riley the most popular poet in America and founded the American dialect school of verse: its combination of exact speech and nostalgic recollection gave the Midwest a poetry of its own, and it sold in enormous numbers for decades.",
   canon="Major canon"),
 dict(title="Rhymes of Childhood", year="1890",
   gb="Dialect Poem and Vernacular Performance, Idyll and Domestic Narrative Poem",
   tb=CHILD + ", " + MEL + ", " + EDU,
   mb="Local Colour and the Regionalist School, Mark Twain and the Vernacular Performance",
   comp=["1885", "1890"], form="Poetry collection (children's verse)",
   desc="Published in 1890 and the collection containing 'Little Orphant Annie': the classic American poems of childhood.",
   plot="The poems present the world of the Indiana child — the orphan girl who tells ghost stories, the boy at the swimming hole, the child at the window on Christmas Eve, the old couple and the grandchild — in dialect narratives that move from comedy to sentiment and back.",
   ctx="1885-90: the American small town of the 1880s, the children's market for recitation verse, and the vogue of the dialect poem in the schools.",
   sig="Rhymes of Childhood contains 'Little Orphant Annie', the most famous American children's poem of the century and a permanent part of American popular culture: the collection made Riley the national poet of childhood, and it is the essential document of the American small-town imagination before the machine.",
   canon="Major canon"),
 dict(title="A Child-World", year="1896",
   gb="Dialect Poem and Vernacular Performance, Novel of Development and the Growth Story",
   tb=CHILD + ", " + MEL + ", " + REG,
   mb="Local Colour and the Regionalist School, Mark Twain and the Vernacular Performance",
   comp=["1895", "1896"], form="Narrative poem sequence",
   desc="Published in 1896 and Riley's most sustained work: a sequence of poems on a single Indiana childhood and the town that surrounded it.",
   plot="The sequence follows a boy and a girl through the seasons of a small-town childhood — the school, the church, the circus, the illness and death of a child, the first love and the departure — and ends with the town remembered by the grown man who has left it.",
   ctx="1895-96: the Indiana of the 1850s, the American small town before the railway and the factory, and the market for the nostalgic verse narrative.",
   sig="A Child-World is Riley's most ambitious and most unified book: its sequence form and its elegiac tone made it something more than a collection of recitation pieces, and it is the finest American verse narrative of small-town childhood before Edgar Lee Masters.",
   canon="Major canon"),
 dict(title="Pipes o' Pan at Zekesbury", year="1889",
   gb="Tall Tale and South-Western Humour Sketch, Dialect Poem and Vernacular Performance",
   tb=REG + ", " + CHILD + ", " + LEIS,
   mb="Local Colour and the Regionalist School, Mark Twain and the Vernacular Performance",
   comp=["1888", "1889"], form="Prose sketches with verse",
   desc="Published in 1889 and Riley's prose masterpiece: sketches of the Indiana town of Zekesbury and its characters.",
   plot="The sketches present the inhabitants of a small Indiana town — the old soldier, the village doctor, the travelling salesman, the revivalist, the boy and the schoolteacher — in dialect narratives that are comic, affectionate and occasionally bitter, and that record a whole community.",
   ctx="1888-89: the Indiana small town of the 1880s, the American local-colour movement, and the newspaper sketch tradition of the Midwest.",
   sig="Pipes o' Pan at Zekesbury is the finest American small-town sketchbook after Twain: its portraits and its dialect made it a landmark of the local-colour movement, and it is the book in which Riley's prose and his poetry are most completely united.",
   canon="Major canon"),
])

ROBINSON = wks("Edwin Arlington Robinson", [
 dict(title="The Children of the Night", year="1897",
   gb="Dramatic Monologue and Masked Lyric, Local-Colour Sketch and the Regional Portrait",
   tb=MEL + ", " + REG + ", " + GRUB,
   mb="The Aesthetic Turn in 1890s America, Local Colour and the Regionalist School",
   comp=["1896", "1897"], form="Poetry collection",
   desc="Published in 1897 and the book that founded modern American poetry: the first Tilbury Town poems and the lyrics of failure and endurance.",
   plot="The collection contains 'Richard Cory', the rich man who goes home and puts a bullet through his head, 'Luke Havergal', the ghost-haunted lover, 'The House on the Hill', the abandoned house, and 'Credo', the poem of a faith that survives doubt, in plain, hard, traditional verse.",
   ctx="1896-97: the depression of 1893-97, the small New England town in decline, the American magazine poetry of the 1890s, and Robinson's own poverty in New York.",
   sig="The Children of the Night is the founding book of modern American poetry: 'Richard Cory' became one of the most anthologised American poems, the Tilbury Town method changed the subject of American verse, and the collection made Robinson the first American poet to write modern poetry in traditional forms.",
   canon="Major canon",
   chars="Richard Cory; Luke Havergal; John Evereldown; Aaron Stark; Cliff Klingenhagen; Reuben Bright; Fleming Helphenstine"),
 dict(title="The Man against the Sky", year="1916",
   gb="Dramatic Monologue and Masked Lyric",
   tb=DOUBT + ", " + MEL + ", " + ART,
   mb="",
   comp=["1915", "1916"], form="Poetry collection",
   desc="Published in 1916 and the collection that established Robinson as a major poet: the title poem on the human figure against the void, and the Tilbury Town portraits.",
   plot="The title poem presents the human being standing against the sky, face to face with the immensity and the indifference of the universe, and asks whether the courage to endure is not itself a kind of answer; the collection also contains 'Ben Jonson Entertains a Man from Stratford', 'Eros Turannos' and 'The Gift of God'.",
   ctx="1915-16: the First World War, the American reception of modernism, and the philosophical debate on the meaning of human existence after Darwin and Nietzsche.",
   sig="The Man against the Sky made Robinson famous and is the finest single collection of American poetry of the 1910s: its title poem gave the age its image of human courage in an indifferent universe, and it confirmed Robinson's position as the leading American poet of his generation before the modernists.",
   canon="Major canon",
   chars="Flammonde; Ben Jonson and the man from Stratford; the wife of 'Eros Turannos'; the mother of 'The Gift of God'; Bewick Finzer; the Poor Relation; Llewellyn and Priscilla ('Llewellyn and the Tree'); Old King Cole"),
 dict(title="Tristram", year="1927",
   gb="Idyll and Domestic Narrative Poem, Epic and the Long Philosophical Poem",
   tb=SEX + ", " + GRIEF + ", " + MEL,
   mb="",
   comp=["1925", "1927"], form="Narrative poem in blank verse",
   desc="Published in 1927 and the Pulitzer Prize-winning climax of Robinson's Arthurian trilogy: the tragedy of Tristram and Isolt.",
   plot="Tristram, married without love to Isolt of the white hands in Brittany, returns to Isolt of Ireland, King Mark's queen; after a summer together at Lancelot's castle of Joyous Gard she is taken back to Cornwall, and when Tristram comes to her there the jealous Andred stabs him to death as she lies dying, while the poem ends, as it began, with Isolt of Brittany gazing at the empty sea, in a retelling that strips the legend of its magic and leaves only the human cost.",
   ctx="1925-27: the American Arthurian revival of the 1920s, the aftermath of the First World War, and the modern scepticism about romantic love.",
   sig="Tristram won the Pulitzer Prize in 1928 and is the finest American narrative poem of the century: its treatment of the Tristan legend as a study of human failure and its blank-verse music made it a landmark, and it completes the Arthurian trilogy that is Robinson's most ambitious work.",
   canon="Major canon",
   chars="Tristram; Isolt of Ireland; Isolt of Brittany; King Mark; Andred; Gawaine; Brangwaine; Queen Morgan; Lancelot and Guinevere"),
 dict(title="'Richard Cory'", year="1897",
   gb="Dramatic Monologue and Masked Lyric, Local-Colour Sketch and the Regional Portrait",
   tb=MEL + ", " + LEIS + ", " + REG,
   mb="The Aesthetic Turn in 1890s America, Local Colour and the Regionalist School",
   comp=["1896", "1897"], form="Lyric poem",
   desc="Published in 1897 and one of the most anthologised American poems ever written: the rich gentleman who is envied by the whole town and shoots himself.",
   plot="The poem describes Richard Cory, the gentleman who is admired and envied by the people of the town, and then ends in two lines: 'And Richard Cory, one calm summer night, / Went home and put a bullet through his head.'",
   ctx="1896-97: the American small town of the 1890s, the depression of 1893-97, and the popular assumption that wealth brings happiness.",
   sig="'Richard Cory' is one of the most famous American poems of the century: its two-line reversal and its study of the gap between appearance and reality made it a permanent part of the American canon, it has been set to music and adapted many times, and it is the poem by which Robinson is most widely known.",
   canon="Major canon",
   chars="Richard Cory; the townspeople, the speakers"),
])

EASTMAN = wks("Charles Eastman", [
 dict(title="Indian Boyhood", year="1902",
   gb="Social Inquiry and the Documented Survey, Local-Colour Sketch and the Regional Portrait",
   tb=CHILD + ", " + RACE + ", " + WILD,
   mb="Local Colour and the Regionalist School, American Realism and the Howells Program",
   comp=["1900", "1902"], form="Autobiography",
   desc="Published in 1902 and the classic Native American account of a traditional childhood: a Dakota boy's life on the plains and in the woods of Canada.",
   plot="Ohiyesa remembers his Dakota boyhood: the games that trained him to hunt and to endure, the stories of the old people, the first buffalo hunt, the snowshoe journeys, the ceremonies and the moral education of a warrior, before he was taken at fifteen to be educated as a white man.",
   ctx="1860s-70s: the Santee Dakota after the 1862 uprising, the traditional life of the northern plains and the Canadian woods, and the American boarding-school policy of the 1870s.",
   sig="Indian Boyhood is the classic Native American autobiography and one of the most widely read Native American books ever written: its account of a traditional Dakota childhood preserved a way of life that was disappearing, and it made Eastman the best-known Native American writer of his generation.",
   canon="Major canon",
   chars="Ohiyesa (Charles Eastman), the narrator; Uncheedah, his grandmother; Mysterious Medicine, his uncle; Many Lightnings, his father"),
 dict(title="The Soul of the Indian", year="1911",
   gb="Social Inquiry and the Documented Survey, Review Essay and Quarterly Argument",
   tb=DOUBT + ", " + RACE + ", " + SCI,
   mb="",
   comp=["1911"], form="Essay collection",
   desc="Published in 1911 and the foundational English account of Dakota religion: an interpretation of Native American spirituality for a white readership.",
   plot="Eastman explains the Dakota belief in the Great Mystery, the practice of prayer and the vision quest, the reverence for the natural world and for the dead, and argues that the Native American religion is a form of natural monotheism closer to the spirit of Christianity than the white man's own conduct.",
   ctx="1911: the missionary campaign among Native Americans, the Society of American Indians, and the American debate on the assimilation and the 'vanishing race'.",
   sig="The Soul of the Indian is the foundational English account of Native American religion and one of the most important Native American books of the century: its interpretation of Dakota spirituality shaped the white American understanding of Native religion, and it remains the classic statement of the Native American religious tradition.",
   canon="Major canon"),
 dict(title="From the Deep Woods to Civilization", year="1916",
   gb="Social Inquiry and the Documented Survey, Local-Colour Sketch and the Regional Portrait",
   tb=RACE + ", " + EDU + ", " + DOUBT,
   mb="",
   comp=["1914", "1916"], form="Autobiography (sequel to Indian Boyhood)",
   desc="Published in 1916 and the second volume of Eastman's autobiography: the passage from the Dakota world to Dartmouth, Boston and Wounded Knee.",
   plot="Eastman recounts his father's return, his education at Beloit, Dartmouth and Boston University, his work as the physician at Pine Ridge, the massacre at Wounded Knee that he witnessed, and his later career as a writer and spokesman for the Native cause.",
   ctx="1873-1916: the assimilation policy of the 1880s, the Ghost Dance movement, the massacre at Wounded Knee in 1890, and the emergence of the Society of American Indians.",
   sig="From the Deep Woods to Civilization is one of the most important Native American autobiographies and the central first-hand account of the massacre at Wounded Knee: its narrative of the passage between two worlds made it a classic, and it is the essential Native American document of the assimilation era.",
   canon="Major canon",
   chars="Charles Eastman (Ohiyesa), the narrator; Many Lightnings (Jacob Eastman), his father; Elaine Goodale Eastman, his wife"),
 dict(title="Old Indian Days", year="1907",
   gb="Local-Colour Sketch and the Regional Portrait, Tall Tale and South-Western Humour Sketch",
   tb=RACE + ", " + WILD + ", " + MEL,
   mb="Local Colour and the Regionalist School, American Realism and the Howells Program",
   comp=["1904", "1907"], form="Short stories",
   desc="Published in 1907 and Eastman's finest collection of stories: the warrior life of the Dakota before the reservation.",
   plot="The stories follow the young Dakota men and women of the old life: the warrior who counts coup, the woman who follows the camp, the hunter, the medicine man and the lover, in narratives that record the code of honour and the daily life of the plains before the treaties.",
   ctx="1904-07: the last years of the free Dakota life, the reservation system, and the American market for the 'vanishing race' story.",
   sig="Old Indian Days is the finest collection of Native American short stories of the period: its narratives of the warrior code and the daily life of the plains made it a classic, and it is one of the few Native-authored accounts of the old life written by someone who had lived it.",
   canon="Major canon"),
])

WORKS = []
for _group in (LAZARUS, LANIER, RILEY, ROBINSON, EASTMAN):
    WORKS.extend(_group)
