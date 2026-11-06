"""Installment 10, wave 26: John Ashbery, Anne Sexton, Adrienne Rich, Martin Luther King Jr., Donald Barthelme.

Five new authors and seventeen works, one record per Norton selection.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

JA = "John Ashbery"
AS = "Anne Sexton"
AR = "Adrienne Rich"
MLK = "Martin Luther King Jr."
DB = "Donald Barthelme"

NYS = "The New York School"
CONF = "Confessional Poetry"
SWF = "Second-Wave Feminist Writing"
POST = "Postmodernism and Postmodern Fiction"
META = "Metafiction"
BLACKHUM = "Black Humour and the Absurdist Novel"
PAW = "Postwar African American Writing: Protest and Its Critics"
GAY = "Gay and Lesbian Literature after Stonewall"

W_JA = "John Ashbery (Wikipedia)"
W_ST = "Some Trees (Wikipedia)"
W_SP = "Self-Portrait in a Convex Mirror, poetry collection (Wikipedia)"
W_PF_SP = "From the Archive: John Ashbery (Poetry Foundation)"
W_NFTA = "Notes from the Air: Selected Later Poems, contents (Carcanet Press)"
W_HC = "How to Continue (Poetry Foundation poem page)"
W_AS = "Anne Sexton (Wikipedia)"
W_HK = "Her Kind (poem) (Wikipedia)"
W_SD = "Sylvia's Death (Wikipedia)"
W_LOD = "Live or Die, poetry collection (Wikipedia)"
W_PF_SD = "Sylvia's Death, Poetry, January 1964 (Poetry Foundation archive)"
W_CP = "The Complete Poems: Anne Sexton, contents (Ecco Press)"
W_AR = "Adrienne Rich (Wikipedia)"
W_DW = "Diving into the Wreck: Poems 1971-1972 (Wikipedia)"
W_DCL = "The Dream of a Common Language (Wikipedia)"
W_MLK = "Martin Luther King Jr. (Wikipedia)"
W_LBJ = "Letter from Birmingham Jail (Wikipedia)"
W_DB = "Donald Barthelme (Wikipedia)"
W_DBB = "Donald Barthelme bibliography (Wikipedia)"
W_BAL = "The Balloon, The New Yorker, 16 April 1966 (newyorker.com archive)"
W_SCH = "A Close Reading of the Best Short Story Ever Written (Literary Hub, on The School)"
W_YR = "Ashbery's Pastoral Art (The Yale Review)"
W_NYR = "The Long Awakening of Adrienne Rich (The New Yorker, 30 November 2020)"
W_PF_BAL = "The Ballad of the Lonely Masturbator (Poetry Foundation poem page)"
W_HRC = "Adrienne Rich's Poetry and Prose, Norton Critical Edition, contents (library catalogue record)"

AUTHORS = [
A10(JA, MAJ, "1927", "2017", "Rochester, New York, United States",
  "American; poet, art critic and editor writing in English",
  "American poet and art critic, the most influential and most imitated American poet of the half-century "
  "after 1955, whose Some Trees and Self-Portrait in a Convex Mirror made difficulty, digression and "
  "unresolved tone the working conditions of American poetry",
  "John Lawrence Ashbery was born in Rochester, New York, on 28 July 1927 and grew up on a fruit farm near "
  "Sodus, in the orchard country south of Lake Ontario, a landscape that recurs in his early poems. He was "
  "educated at Deerfield Academy, where he first read Auden and Dylan Thomas and had two poems printed in "
  "Poetry without his knowledge, and at Harvard, where he wrote on Auden, edited the Harvard Advocate and "
  "met Frank O'Hara and Kenneth Koch. He took an MA at Columbia in 1951 with a thesis on Henry Green, "
  "worked as a copywriter for Oxford University Press and then for McGraw-Hill, and in 1955 went to France "
  "on a Fulbright, remaining in Paris for most of a decade and writing art criticism for the New York "
  "Herald Tribune and Art News. Some Trees, chosen by W. H. Auden for the Yale Series of Younger Poets, "
  "appeared in 1956 and sold slowly; The Tennis Court Oath (1962) divided its first readers, Rivers and "
  "Mountains (1966) restored his standing, and The Double Dream of Spring (1970) and Three Poems (1972) "
  "established the meditative, disjunctive manner of his maturity. Self-Portrait in a Convex Mirror (1975) "
  "won the Pulitzer Prize, the National Book Award and the National Book Critics Circle Award, and was "
  "followed by Houseboat Days (1977), As We Know (1979), Shadow Train (1981), A Wave (1984), April "
  "Galleons (1987), Flow Chart (1991), Hotel Lautre\u0301amont (1992), And the Stars Were Shining (1994), "
  "Wakefulness (1998), Girls on the Run (1999), Chinese Whispers (2002), Where Shall I Wander (2005) and "
  "later volumes; he was poet laureate of New York State from 2001 to 2003, and the Library of America "
  "issued his Collected Poems 1956-1987 in 2008, the first such volume devoted to a living poet. He died "
  "at his home in Hudson, New York, on 3 September 2017.",
  "Poetry: Turandot and Other Poems (1953), Some Trees (1956), The Tennis Court Oath (1962), Rivers and "
  "Mountains (1966), The Double Dream of Spring (1970), Three Poems (1972), Self-Portrait in a Convex "
  "Mirror (1975), Houseboat Days (1977), As We Know (1979), Shadow Train (1981), A Wave (1984), April "
  "Galleons (1987), Flow Chart (1991), Hotel Lautre\u0301amont (1992), And the Stars Were Shining (1994), "
  "Wakefulness (1998), Girls on the Run (1999), Your Name Here (2000), Chinese Whispers (2002), Where "
  "Shall I Wander (2005), A Worldly Country (2007), Planisphere (2009), Quick Question (2012), Breezeway "
  "(2015) and Commotion of the Birds (2016). Prose: Reported Sightings (1989), Other Traditions (2000) "
  "and Selected Prose (2004). Novels, with James Schuyler: A Nest of Ninnies (1969).",
  "Long poems built of short, flat, syntactically exact sentences that change subject without warning; a "
  "tone that is courteous, melancholy and ironic at once, so that no single attitude can be assigned to "
  "it; abstraction and ordinary speech held in the same line; puns, cliche\u0301s and quoted fragments used "
  "as materials rather than as jokes; prose poems and prose paragraphs in which the sentence does the work "
  "of the line.",
  "The mind as it actually moves, in fits and starts, rather than as argument or narrative would arrange "
  "it; the instability of the self and of the pronoun that speaks; painting, film and popular music as "
  "models of composition; the ordinary happiness and ordinary grief of American middle life; the "
  "impossibility and the necessity of meaning; age, memory and the deaths of friends.",
  "Ashbery is the central American poet of the last half-century and the one against whom almost every "
  "later American poet has had to define a position; Self-Portrait in a Convex Mirror is the only book to "
  "have won the Pulitzer Prize, the National Book Award and the National Book Critics Circle Award, and "
  "'Self-Portrait in a Convex Mirror' is among the most discussed American poems of the century. His "
  "influence on the Language poets, on the New York School's successors and on the conversational, "
  "digressive poetry of the 1990s and 2000s is acknowledged on every side, and he is a standard presence "
  "in anthologies and in the teaching of postwar American poetry.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Ashbery, on Some Trees and on "
           "Self-Portrait in a Convex Mirror, and from the contents listings of Notes from the Air and of "
           "Hotel Lautre\u0301amont, read directly; they were not checked against a printed bibliography, and "
           "the contents of the later volumes are given only in outline. Installment 10 records the three "
           "Norton selections - 'Illustration' (Some Trees, 1956), 'Self-Portrait in a Convex Mirror' "
           "(Poetry, August 1974; collected 1975) and 'How to Continue' (Hotel Lautre\u0301amont, 1992) - so "
           "the other twenty-odd collections and the prose have no records, and the bibliography is "
           "incomplete.",
  ver="partially verified", sources=[W_JA, W_ST, W_SP, W_NFTA, NAAL]),
A10(AS, MAJ, "1928", "1974", "Newton, Massachusetts, United States",
  "American; poet writing in English",
  "American confessional poet whose five Houghton Mifflin collections of 1960-1969 and her readings made "
  "madness, motherhood, menstruation, adultery and suicide the matter of American poetry, and whose Live "
  "or Die won the Pulitzer Prize in 1967",
  "Anne Gray Harvey was born in Newton, Massachusetts, on 9 November 1928, the daughter of a woollen "
  "manufacturer, and grew up in Wellesley. She attended Garland Junior College and in 1948 married Alfred "
  "Muller Sexton, with whom she had two daughters, Linda Gray and Joyce Ladd; a third, Mary Gray, was born "
  "in 1955 and died within days. After a breakdown in 1956 she began writing poetry at the suggestion of "
  "her psychiatrist, Dr Martin Orne, and studied with Robert Lowell at Boston University from 1958, where "
  "she met Sylvia Plath; John Holmes and W. D. Snodgrass were early readers and advocates. To Bedlam and "
  "Part Way Back (1960) announced her subject: the asylum, the double image of mother and daughter, and "
  "the wish to die. All My Pretty Ones (1962), a finalist for the National Book Award, was followed by "
  "Live or Die (1966), which won the Pulitzer Prize for Poetry in 1967, and by Love Poems (1969), "
  "Transformations (1971), The Book of Folly (1972) and The Death Notebooks (1974). She taught and gave "
  "readings widely, performed with the jazz group Her Kind, and was elected a Fellow of the Royal Society "
  "of Literature. She divorced in 1973 and died by suicide at Weston, Massachusetts, on 4 October 1974, "
  "aged forty-five.",
  "Poetry: To Bedlam and Part Way Back (1960), All My Pretty Ones (1962), Live or Die (1966), Love Poems "
  "(1969), Transformations (1971), The Book of Folly (1972), The Death Notebooks (1974) and The Awful "
  "Rowing Toward God (1975, posthumous). Children's book: Eggs of Things (1963), with Maxine Kumin. "
  "Posthumous prose and letters: Anne Sexton: A Self-Portrait in Letters (1977) and No Evil Star: "
  "Selected Essays, Interviews, and Prose (1985).",
  "Short, flat, declarative lines that turn without warning into incantation; a nursery-rhyme or ballad "
  "music used for the most private material; startling similes drawn from the household and the hospital; "
  "direct address to the dead, to the body, to the daughter and to the reader; repetition of a single "
  "phrase as the spine of a poem; a spoken, performable rhetoric shaped by her reading voice.",
  "Mental illness, hospitalisation and the talking cure; motherhood and the inheritance of a mother's "
  "life; the female body, menstruation, abortion and desire; marriage, adultery and divorce; the wish to "
  "die and the guilt of surviving; fairy tale, myth and religion as frames for a private life; poetry "
  "itself as an act of exposure.",
  "Sexton is one of the two or three defining American confessional poets and, with Plath, the writer "
  "through whom the poetry of the 1960s is most often taught; she brought subjects that had been kept out "
  "of American verse - abortion, menstruation, masturbation, psychiatric hospitalisation - into the "
  "anthologies, and her readings and recordings made poetry a public performance again. Live or Die is a "
  "Pulitzer Prize winner, Transformations is a standard text in courses on the fairy tale, and her "
  "influence runs through the poetry of the 1970s and through the later poetry of trauma and of the body.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Sexton, on Live or Die and on "
           "'Her Kind', and from the contents listing of The Complete Poems, read directly; they were not "
           "checked against a printed bibliography, and the periodical first printings of the individual "
           "poems are documented unevenly. Installment 10 records the five Norton selections - 'The Starry "
           "Night' (All My Pretty Ones, 1962), 'Her Kind' (To Bedlam and Part Way Back, 1960), 'Sylvia's "
           "Death' (Poetry, January 1964; collected 1966), 'Little Girl, My String Bean, My Lovely Woman' "
           "(Live or Die, 1966) and 'The Ballad of the Lonely Masturbator' (Love Poems, 1969) - so the "
           "other collections, the children's book and the posthumous prose have no records, and the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_AS, W_HK, W_SD, W_LOD, W_PF_SD, W_CP, NAAL]),
A10(AR, MAJ, "1929", "2012", "Baltimore, Maryland, United States",
  "American; poet, essayist and feminist writing in English",
  "American poet and essayist whose work moved from the formal verse of A Change of World to the "
  "documentary, feminist and lesbian poetry of Diving into the Wreck and The Dream of a Common Language, "
  "and who was for half a century the most influential political poet in the language",
  "Adrienne Cecile Rich was born in Baltimore on 16 May 1929, the elder daughter of Arnold Rich, a "
  "pathologist at Johns Hopkins, and Helen Gravely Jones, a composer and pianist; she was educated at "
  "Radcliffe College, graduated Phi Beta Kappa in 1951, and in the same year won the Yale Series of "
  "Younger Poets with A Change of World, chosen by W. H. Auden. She married Alfred H. Conrad, an "
  "economist, in 1953 and had three sons; The Diamond Cutters (1955) followed, and Snapshots of a "
  "Daughter-in-Law (1963) - written over three years and initially ignored or attacked - began the turn "
  "towards the political and the personal that the rest of her work completes. Necessities of Life "
  "(1966), Leaflets (1969) and The Will to Change (1971) record the years of anti-war activism and of her "
  "marriage's collapse; she divorced in 1970 and Conrad died the same year. Diving into the Wreck (1973) "
  "won the National Book Award, which she refused as an individual and accepted with Audre Lorde and "
  "Alice Walker on behalf of all women. She came out as a lesbian in 1976; Of Woman Born (1976), The "
  "Dream of a Common Language (1978), A Wild Patience Has Taken Me This Far (1981), The Fact of a "
  "Doorframe (1984), Your Native Land, Your Life (1986), Time's Power (1989), An Atlas of the Difficult "
  "World (1991), Dark Fields of the Republic (1995), Midnight Salvage (1999), Fox (2001), The School Among "
  "the Ruins (2004) and Tonight No Poetry Will Serve (2011) followed, with the essays of On Lies, Secrets, "
  "and Silence (1979), Blood, Bread, and Poetry (1986) and What Is Found There (1993). She refused the "
  "National Medal of Arts in 1997, taught for many years at Stanford and elsewhere, and died in Santa "
  "Cruz, California, on 27 March 2012.",
  "Poetry: A Change of World (1951), The Diamond Cutters (1955), Snapshots of a Daughter-in-Law (1963), "
  "Necessities of Life (1966), Leaflets (1969), The Will to Change (1971), Diving into the Wreck (1973), "
  "Poems: Selected and New, 1950-1974 (1974), The Dream of a Common Language (1978), A Wild Patience Has "
  "Taken Me This Far (1981), The Fact of a Doorframe (1984), Your Native Land, Your Life (1986), Time's "
  "Power (1989), An Atlas of the Difficult World (1991), Collected Early Poems 1950-1970 (1993), Dark "
  "Fields of the Republic (1995), Midnight Salvage (1999), Fox (2001), The School Among the Ruins (2004) "
  "and Tonight No Poetry Will Serve (2011). Prose: Of Woman Born (1976), On Lies, Secrets, and Silence "
  "(1979), Blood, Bread, and Poetry (1986), What Is Found There (1993) and A Human Eye (2009).",
  "Lines that break where the thought breaks, not where the metre would; a documentary notation of dates, "
  "places and quotations; the long poem built as a sequence of numbered sections; the direct second "
  "person and the collective 'we'; images drawn from geology, cartography, medicine and the sea; an "
  "argument carried by the poem's own hesitations and revisions.",
  "The politics of gender and the institution of motherhood; sexuality, the closet and the love of women; "
  "language as an instrument of power and the possibility of a common language; history, war and the "
  "American state; race and the responsibilities of the white poet; the relation of the living to the "
  "dead, and of a poem to the world it intervenes in; art as work rather than as transcendence.",
  "Rich is the most influential political poet in English of the last half-century and a founding figure "
  "of second-wave feminist criticism: 'When We Dead Awaken: Writing as Re-Vision' and Of Woman Born are "
  "standard texts in women's studies, Diving into the Wreck is a National Book Award winner, and the "
  "refusal of the National Medal of Arts in 1997 made her a public example of the writer's relation to "
  "the state. Her influence on feminist, lesbian and documentary poetry in the United States and Britain "
  "is pervasive, and the later prose on compulsory heterosexuality remains central to queer theory's "
  "genealogy.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Rich, on Diving into the Wreck "
           "and on The Dream of a Common Language, and from the contents listing of the Norton critical "
           "Poetry and Prose, read directly; they were not checked against a printed bibliography. "
           "Installment 10 records the six Norton selections - 'Snapshots of a Daughter-in-Law' (1963), "
           "'I Am in Danger-Sir-' (Necessities of Life, 1966), 'A Valediction Forbidding Mourning' (The "
           "Will to Change, 1971), 'Diving into the Wreck' (1973), 'Power' and 'Transcendental Etude' "
           "(both The Dream of a Common Language, 1978) - so the other collections, the essays and the "
           "critical prose have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_AR, W_DW, W_DCL, W_HRC, NAAL]),
A10(MLK, MAJ, "1929", "1968", "Atlanta, Georgia, United States",
  "American; Baptist minister, orator and essayist writing in English",
  "American Baptist minister and leader of the civil rights movement, whose sermons, speeches and prison "
  "letter made him the greatest American orator of the century and one of its most widely reprinted "
  "prose writers",
  "Michael King Jr. was born in Atlanta, Georgia, on 15 January 1929, the son of the pastor of Ebenezer "
  "Baptist Church, and took his father's adopted name of Martin Luther King. He entered Morehouse College "
  "at fifteen, graduated in 1948, took a divinity degree at Crozer Theological Seminary in 1951 and a "
  "doctorate in systematic theology at Boston University in 1955, the year in which he became pastor of "
  "Dexter Avenue Baptist Church in Montgomery, Alabama. The Montgomery bus boycott, begun after Rosa "
  "Parks's arrest in December 1955 and lasting 381 days, made him a national figure; he founded the "
  "Southern Christian Leadership Conference in 1957 and led campaigns in Birmingham in 1963, in "
  "Washington the same year, where he delivered 'I Have a Dream' on 28 August, in Selma in 1965 and in "
  "Chicago in 1966. He received the Nobel Peace Prize in 1964, broke publicly with the Johnson "
  "administration over Vietnam in 1967, and was organising the Poor People's Campaign when he was "
  "assassinated in Memphis, Tennessee, on 4 April 1968. His books are Stride Toward Freedom (1958), "
  "Strength to Love (1963), Why We Can't Wait (1964), Where Do We Go from Here: Chaos or Community? "
  "(1967) and, posthumously, The Trumpet of Conscience (1968).",
  "Books: Stride Toward Freedom (1958), Strength to Love (1963), Why We Can't Wait (1964), Where Do We Go "
  "from Here: Chaos or Community? (1967) and The Trumpet of Conscience (1968). Sermons and addresses: "
  "'I Have a Dream' (1963), 'Beyond Vietnam: A Time to Break Silence' (1967) and 'I've Been to the "
  "Mountaintop' (1968). Letters: 'Letter from Birmingham City Jail' (1963). Posthumous editions: The "
  "Papers of Martin Luther King, Jr., ed. Clayborne Carson and others (1992- ), and The Autobiography of "
  "Martin Luther King, Jr. (1998), compiled by Clayborne Carson.",
  "Prose built on the cadences of the Black Baptist sermon: long periodic sentences that rise through "
  "repetition, antithesis and parallel clauses to a declaratory close; quotation of Scripture, the "
  "Declaration of Independence, Aquinas, Augustine, Buber and Tillich as shared authorities; the "
  "parable-like example; the direct address to a named or implied audience; an orator's sense of the "
  "paragraph as a breath and of the list as a climax.",
  "Racial segregation and the moral obligation to disobey unjust law; nonviolence as method and as "
  "theology; the difference between just and unjust laws; the failure of white moderates and of the white "
  "church; the relation of American democracy to its own founding promises; poverty, war and the "
  "international struggle for freedom; suffering, redemption and the meaning of hope.",
  "King is the central orator of the American twentieth century and the writer through whom the civil "
  "rights movement is most often read; 'Letter from Birmingham Jail' is anthologised in American "
  "literature, composition, history, law and theology courses and was reprinted about fifty times in "
  "college readers between 1964 and 1968 alone. It is a founding document of the modern theory of civil "
  "disobedience in the United States, its central sentence - 'Injustice anywhere is a threat to justice "
  "everywhere' - is among the most quoted in American public speech, and King's writings remain the "
  "reference point for every later American argument about race, law and nonviolence.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on King and on the Letter from "
           "Birmingham Jail, together with the account of the letter's printing history given there and by "
           "the dealers' and archive records consulted; they were not checked against a printed "
           "bibliography, and the sermons are listed by title and date only. Installment 10 records the "
           "one Norton selection, the 'Letter from Birmingham Jail' (16 April 1963; first printed as a "
           "pamphlet by the American Friends Service Committee in May 1963 and in Liberation in June "
           "1963; collected in Why We Can't Wait, 1964), so the books of sermons and the later essays have "
           "no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_MLK, W_LBJ, NAAL]),
A10(DB, MAJ, "1931", "1989", "Philadelphia, Pennsylvania, United States",
  "American; short-story writer, novelist and editor writing in English",
  "American short-story writer and collagist, the most inventive practitioner of American postmodern "
  "fiction, whose hundred-odd stories in The New Yorker remade the short story as a structure of jokes, "
  "quotations and interruptions",
  "Donald Barthelme Jr. was born in Philadelphia on 7 April 1931, the son of an architect, and grew up in "
  "Houston, Texas, where his father taught at the University of Houston. He studied journalism there, "
  "wrote for the Houston Post, founded and edited the literary magazine Forum, was drafted into the army "
  "in 1953 and served in Korea as editor of an army newspaper, and in 1961 became director of the "
  "Contemporary Arts Museum in Houston, the year he published his first story. He was managing editor of "
  "Location and a co-founder of Fiction, and from 1963 The New Yorker published more than a hundred of his "
  "stories. Come Back, Dr. Caligari (1964) collected the first of them; Snow White (1967), first serialised "
  "in The New Yorker, was his first novel, followed by Unspeakable Practices, Unnatural Acts (1968), City "
  "Life (1970), the children's book The Slightly Irregular Fire Engine (1971, National Book Award 1972), "
  "Sadness (1972), Guilty Pleasures (1974), The Dead Father (1975), Amateurs (1976), Great Days (1979), "
  "Sixty Stories (1981), Overnight to Many Distant Cities (1983), Paradise (1986), Forty Stories (1987) "
  "and The King (1990, posthumous). He taught at Boston University, the University at Buffalo and the City "
  "College of New York, where he was distinguished visiting professor in 1974-75, and died of throat "
  "cancer in Houston on 23 July 1989.",
  "Stories: Come Back, Dr. Caligari (1964), Unspeakable Practices, Unnatural Acts (1968), City Life "
  "(1970), Sadness (1972), Amateurs (1976), Great Days (1979), Sixty Stories (1981), Overnight to Many "
  "Distant Cities (1983), Forty Stories (1987), Flying to America (2008) and Collected Stories (2021). "
  "Novels: Snow White (1967), The Dead Father (1975), Paradise (1986) and The King (1990). Non-fiction "
  "and satire: Guilty Pleasures (1974), The Teachings of Don B. (1992) and Not-Knowing (1997). Children's "
  "book: The Slightly Irregular Fire Engine (1971).",
  "Stories without plot in the traditional sense, built by accumulation and juxtaposition; the "
  "non-sequitur as a structural device; parody of found forms - the questionnaire, the catalogue, the "
  "academic essay, the newspaper column, the interview; dialogue of great flatness and precision; "
  "typographic and visual play; a deadpan narrator who reports the absurd as though it were ordinary.",
  "The making of art and the reception of the artwork by a public that wants it explained; the "
  "arbitrariness of the signs and objects among which Americans live; marriage, divorce and desire "
  "conducted in a language of cliche\u0301; the city as a grid and as a joke; death, and the difficulty of "
  "saying anything true about it; the exhaustion of inherited literary forms and the freedom that "
  "exhaustion offers.",
  "Barthelme is the representative American postmodernist and the writer through whom the American short "
  "story after 1965 is usually periodised; his stories are standard anthology and workshop texts, 'The "
  "Balloon' and 'The School' are among the most widely reprinted American short stories of the postwar "
  "decades, and his influence is acknowledged by writers as different as George Saunders, David Foster "
  "Wallace and Lydia Davis. The Library of America collected his stories in 2021, the first such volume "
  "for a postwar American experimental short-story writer.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Barthelme and on his "
           "bibliography, read directly, with the first periodical printings of the two Norton selections "
           "taken from The New Yorker's own archive and from the bibliography's tables; they were not "
           "checked against a printed bibliography. Installment 10 records the two Norton selections - "
           "'The Balloon' (The New Yorker, 16 April 1966; collected 1968) and 'The School' (The New "
           "Yorker, 17 June 1974; collected 1976) - so the novels, the other hundred stories and the "
           "non-fiction have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_DB, W_DBB, W_BAL, W_SCH, NAAL]),
]

WORKS = [
W10("Illustration", JA, "1956", "Poem (two-part lyric narrative)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry", "Free Verse"),
  themes=T("Art, the artist and the creative life", "Death, illness and mourning", "Faith, doubt and the sacred"),
  movements=M(NYS),
  overview="'Illustration' is a two-part poem from John Ashbery's first collection, Some Trees (Yale University "
           "Press, 1956), the book that won the Yale Series of Younger Poets and carried a foreword by W. H. "
           "Auden. The first part is a short narrative with a medieval-religious colouring: a novice sits on a "
           "cornice high over a modern city while angels and police, a lady, a mother and a blind man offer her "
           "gifts and plead with her to come down; the second part turns from the scene to a meditation on "
           "sacrifice, art and indifference. It is one of the poems in which the manner of the New York School "
           "is most clearly on show inside a book that still reads, for the most part, as late modernist verse.",
  content="The first of the poem's two parts fixes a scene: a novice is sitting on a cornice high over the city, "
          "and angels 'combined their prayers with those of the police' to beg her to come down. A lady offers "
          "friendship and is refused; a mother offers the nylons stripped from her own legs; others bring fruit, "
          "candy and flowers, the blind man all his flowers. The novice tells them that she wants no gifts but "
          "that they should remember she died accepting them, asks for monuments, and says she wants to move "
          "figuratively 'as waves caress the thoughtless shore'; then the wind unpins her robes and she drifts "
          "naked and soft downward, out of the angels' tenderness and out of the minds of men. The second part "
          "begins 'Much that is beautiful must be discarded / so that we may resemble a taller impression of "
          "ourselves', speaks of moths climbing in the flame that wish to be the flame, and ends with rockets "
          "over the city, a night of feasting, and the judgement that the girl was 'only an effigy of "
          "indifference, a miracle not meant for us'.",
  summary="The poem works by a double exposure. Its first half is a legend or a stained-glass panel: a holy woman "
          "on a high ledge, a crowd beneath her with its offers, her refusal, her voluntary descent. The gifts "
          "are absurdly mixed in period - angels and police in one sentence, a mother's nylons beside fruit and "
          "candy - and this mixture is what makes the scene Ashbery's rather than a medieval author's: the "
          "sacred and the commercial arrive in the same syntax and with the same courtesy. Her speech is the "
          "hinge of the poem. She will not be consoled, she asks to be remembered as having accepted what she "
          "did not want, and she asks for a monument, that is, for the very 'illustration' the poem is. The "
          "descent that follows is described in the language of hagiography - 'naked as a roc's egg' - but it "
          "ends 'out of the angels' tenderness and the minds of men', which is to say out of the reach of both "
          "religion and art. The second half then turns to us, or to the spectators, and argues that something "
          "beautiful has to be given up if we are to become a larger version of ourselves: the moths climbing "
          "in the flame want to be the flame and are not diminished by wanting it. The poem closes on the "
          "evening of her disappearance - rockets, feasting, 'so many attitudes toward that flame' - and on a "
          "correction: she was an effigy of indifference, a miracle not meant for us, as the leaves are not "
          "winter's simply because winter has come. What the two halves do together is refuse the moral that "
          "the first half seems to promise; the illustration illustrates nothing, or illustrates the cost of "
          "wanting it to.",
  themes_text="The poem's subject is the relation of art to sacrifice, and it takes the religious image "
              "seriously enough to make the aesthetic one visible behind it: the novice who wants monuments and "
              "who is remembered for accepting what she refused is a figure for the artwork that asks to be "
              "read as martyrdom. The second half's argument about discarding beauty to resemble a taller "
              "impression of ourselves is an argument about what spectators do with such a figure, and the "
              "moths that wish to be the flame are the audience as much as the artist. Death is present "
              "throughout but never solemnised: the descent is graceful, the feasting continues, and the last "
              "judgement is delivered flatly, as a fact about leaves and winter.",
  structure="Two unequal parts. The first is a narrative in short lines with a clear sequence - the scene, the "
            "offers, the refusal, the speech, the descent - and it carries the poem's only action. The second "
            "is a meditation that begins with a maxim ('Much that is beautiful must be discarded'), proceeds by "
            "image rather than by argument, and ends with a qualification that withdraws the significance the "
            "first part seemed to have earned. The relation between the halves is that of scene and gloss, and "
            "the gloss declines to gloss.",
  style="Short, regular, mostly unrhymed lines with a marked tendency to fall into quatrains; a diction that is "
        "courteous, archaic and administratively modern at once ('combined their prayers with those of the "
        "police'); the definite article used as though the reader already knew the story; syntax that keeps its "
        "balance while its content goes wrong; almost no metaphor that cannot be read as literal stage "
        "business.",
  ctx="Written in the early 1950s, while Ashbery was working in New York as a copywriter and moving among the "
      "painters and poets who would be called the New York School, and collected in Some Trees, published on 28 "
      "March 1956 as volume 52 of the Yale Series of Younger Poets, with a foreword by Auden, who had chosen the "
      "manuscript and later said that he had not understood much of it. The book printed 817 copies and sold "
      "slowly - 456 copies in four years, the whole run in ten - and the only good review it received was Frank "
      "O'Hara's in Poetry.",
  sig="'Illustration' is one of the poems by which the early Ashbery is taught: it shows the New York School's "
      "taste for the legendary and the banal in one frame, and it is the poem in which the two-part structure "
      "that recurs throughout his work - scene and commentary, image and its withdrawal - first appears clearly. "
      "It is regularly anthologised with 'Some Trees' and 'The Instruction Manual' as the representative poem "
      "of his first book, and later critics have read it as an early statement of his poetics of "
      "non-interpretation.",
  canon="Secondary canon",
  crit="Commentary has treated the poem as a parable of the artwork and its public, as a parody of "
       "hagiography, and as an exercise in the pastoral that Ashbery inherited from the French surrealists and "
       "from Wallace Stevens; the Yale Review's essay on his pastoral art reads the novice as a version of the "
       "naive shepherd, that is, of the poet himself, in a 'pastoral greenness that he may never be able to "
       "shake off'. The comparison with Stevens, first made by O'Hara in his review of Some Trees, has been "
       "pursued by critics ever since.",
  biblio="First collected in Some Trees (New Haven: Yale University Press, Yale Series of Younger Poets, vol. "
         "52, 1956); reprinted in The Mooring of Starting Out: The First Five Books of Poetry (1998) and in "
         "Collected Poems 1956-1987 (Library of America, 2008). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The poem was read in the text printed in Some Trees and in the collected editions. Its first magazine "
        "printing was not established from the sources consulted, so the record dates it from its first book "
        "appearance (1956), the date the anthology gives; the publication details of Some Trees follow "
        "Wikipedia's article on the collection.",
  ver="partially verified", sources=[W_ST, W_JA, W_YR, NAAL]),
W10("Self-Portrait in a Convex Mirror", JA, "1974", "Poem (long meditative poem in free verse)", "major",
  genres=G("Lyric Poetry", "Long Poem", "Free Verse", "Postmodern Poetry"),
  themes=T("Art, the artist and the creative life", "Identity, authenticity and the divided self",
           "Language, writing and the limits of representation"),
  movements=M(NYS, POST),
  overview="'Self-Portrait in a Convex Mirror' is John Ashbery's longest and most celebrated poem, published in "
           "Poetry in August 1974 and used as the title poem of the collection that appeared from Viking Press on "
           "15 May 1975. It is an extended meditation on Parmigianino's painting of about 1524, a convex mirror "
           "portrait in which the young painter's face is swollen and distorted by the curvature of the glass, "
           "and it takes that distortion as a model for the way the mind, and the poem, can hold nothing "
           "without changing it. The collection won the Pulitzer Prize for Poetry, the National Book Award and "
           "the National Book Critics Circle Award, the only book to have taken all three.",
  content="The poem opens with the painting - 'As Parmigianino did it, the right hand / Bigger than the head, "
          "thrusting toward / The viewer' - and describes the image closely: the fur, the pleated muslin, the "
          "coral ring, the room reflected in the glass behind the head, the 'soul' that 'establishes itself, "
          "permanently, in the gloss of / This polished surface'. From there it moves outward by association: to "
          "Vasari's life of the painter, to the young man's absorption in his art and his early death, to the "
          "question of whether a portrait can hold a life at all, to the poet's own situation in a New York "
          "afternoon, and to the recurring figure of the hand and the glass. Its best-known passage compares the "
          "soul to a room that is always being rearranged, 'a small / Circular breathing space' that cannot be "
          "entered from outside. The poem returns repeatedly to the painting's promise of permanence and to the "
          "knowledge that the promise is an effect of surface, and it ends by leaving the image where it found "
          "it, in the mirror.",
  summary="The poem is a single movement of roughly five hundred and fifty lines in unrhymed verse paragraphs, "
          "and its argument is carried by description, anecdote and digression rather than by theses. It begins "
          "in the painting's presence and stays there while ranging over everything the painting suggests. "
          "Parmigianino, Ashbery reports from Vasari, was a young man of great accomplishment and strange "
          "manners who was said to have become absorbed in alchemy and to have died young; the portrait's "
          "convexity makes the hand that draws it the largest thing in the frame, so that the artist's "
          "instrument, not his face, is the true subject, and Ashbery reads this as an emblem of the artwork "
          "that can never include the act of making it. Against the painting's claim to permanence he sets the "
          "movement of the mind, which cannot hold an idea for more than a moment without altering it: the "
          "meditation on the soul as a room - 'a small / Circular breathing space' that has its own weather and "
          "its own furniture - is the poem's centre. The middle sections turn to the question of what a "
          "portrait is for, and to the disappointment of finding that the answer is always the surface; there "
          "are passages on the city, on the sound of a piano, on the weather of a particular afternoon, and on "
          "the difficulty of ending anything. The last part slows down and addresses the image directly, "
          "conceding that it will outlast the poem and that the poem's own attempt to hold it is another "
          "version of the mirror's promise; the final lines leave the reader in the ordinary present, with the "
          "portrait still 'there', and with the poem's own voice admitting that it has not solved the problem "
          "it set out to describe.",
  themes_text="The poem's subject is representation itself: the impossibility of seeing the self except through "
              "a distorting medium, and the possibility, which the poem keeps testing, that the distortion is "
              "the only honest account available. The painting stands for every artwork that offers to preserve "
              "a life, and the poem's long resistance to its charm is an argument about what art can and "
              "cannot do. Its second subject is time: the surface is permanent, the sitter is not, and the "
              "meditation on the soul as a room is an attempt to describe a self that is a process rather than "
              "an object. A third is the practice of poetry itself; the poem repeatedly turns from the painting "
              "to the business of writing about it, and treats its own hesitations as evidence.",
  structure="Unrhymed verse paragraphs of varying length in a single continuous movement of about 550 lines, "
            "without numbered sections or breaks of scene; the transitions are made by echo and association "
            "rather than by argument, and a phrase from one paragraph frequently returns, altered, several "
            "pages later. The painting supplies the poem's frame and its recurring images - the hand, the "
            "glass, the room, the weather - and the poem's movement is circular rather than linear, ending "
            "near where it began.",
  style="Conversational, exact, unhurried long lines, many of them end-stopped, in a diction that mixes the "
        "vocabulary of art history with that of the newspaper and the lecture; a syntax of qualification and "
        "parenthesis in which each sentence corrects the one before; quotation and near-quotation of Vasari and "
        "of art-historical commonplaces; sudden shifts of register within a single sentence; an almost complete "
        "absence of metaphor of the decorative kind.",
  ctx="Composed in the early 1970s while Ashbery was writing art criticism and teaching at Brooklyn College, and "
      "first published in Poetry in August 1974, the month in which Richard Nixon resigned; the painting and the "
      "poem were printed side by side in Art in America in the January-February 1975 issue. The collection "
      "followed The Double Dream of Spring (1970) and Three Poems (1972) and appeared from Viking Press on 15 "
      "May 1975; in 1976 it took the Pulitzer Prize, the National Book Award and the National Book Critics "
      "Circle Award, and it made Ashbery the most discussed American poet of his generation.",
  sig="The title poem is the most discussed American poem of the last half-century and the work by which "
      "Ashbery's centrality is measured; the book is the only one to have won the Pulitzer, the National Book "
      "Award and the National Book Critics Circle Award, and the poem's long, discursive, self-interrupting "
      "manner set the terms for American poetry after 1975. It is a standard text in courses on postwar "
      "poetry, on ekphrasis and on postmodernism, and Harold Bloom's admiration for it - he called Ashbery the "
      "most remarkable poet of his time - made it a testing case for the canon of the late twentieth century.",
  canon="Major canon",
  crit="Criticism has read the poem as ekphrasis and as an argument against ekphrasis, as a meditation on "
       "subjectivity and time, as an oblique commentary on American political life (Stephen Paul Miller reads "
       "it against the Watergate summer in which it was published), and as the culmination of the romantic "
       "fragment. Its relation to Stevens, to Parmigianino's own text and to the tradition of the "
       "self-portrait has been extensively discussed; the poem is also a standing test case in the argument "
       "about whether difficulty is a value or an evasion.",
  biblio="Published in Poetry, vol. 124, no. 5 (August 1974), 247-261; collected as the title poem of "
         "Self-Portrait in a Convex Mirror (New York: Viking Press, 15 May 1975); reprinted in Collected Poems "
         "1956-1987 (Library of America, 2008). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The poem was read in the printed text; quotations are short and confined to the passages for which it "
        "is universally known. The date 1974 is the date of first publication in Poetry, which the anthology "
        "gives; the book appeared in 1975.",
  ver="partially verified", sources=[W_SP, W_PF_SP, W_JA, NAAL]),
W10("How to Continue", JA, "1992", "Poem (lyric narrative in rhymed and unrhymed lines)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry", "Free Verse", "Postmodern Poetry"),
  themes=T("Death, illness and mourning", "Love, intimacy and loss", "Memory, trauma and testimony"),
  movements=M(NYS),
  overview="'How to Continue' is the closing poem of Hotel Lautre\u0301amont, John Ashbery's twenty-first book of "
           "poems, published by Farrar, Straus and Giroux in 1992; Ashbery later chose it for his selected "
           "later poems, Notes from the Air (2007), where it is the last poem from that collection. It begins "
           "as a story - 'Oh there once was a woman and she kept a shop / selling trinkets to tourists' - and "
           "turns under the reader's hands into an elegy for a world of parties, friends and lovers that has "
           "ended. It is one of the few late Ashbery poems that readers have been willing to call "
           "autobiographical.",
  content="The poem's first movement has the rhyme and cadence of a ballad or a nursery tale: a woman on an "
          "island keeps a shop selling trinkets to tourists not far from a dock, and 'it was always a party "
          "there / always different but very nice', with new friends, advice and love, each growing perfectly "
          "from the other, 'a marvel of poetry and irony'. The unsafe quarter is scary and dirty but nobody "
          "minds; the parties go from house to house, there are friends and lovers galore, moonshine in winter "
          "and starshine in summer. Then the poem's music changes and its story ends: 'And then one day the ship "
          "sailed away. / There were no more dreamers just sleepers in heavy attitudes / on the dock'. A gale "
          "comes and says it is time to take all of them away, from the tops of the trees to the little houses "
          "on little paths, and 'when it became time to go / they none of them would leave without the other', "
          "for they said 'we are all one here'; the wind whispers it to the stars, the people get up to go, and "
          "'looked back on love'.",
  summary="The poem moves in three stages and does not signal the transitions. The first is a tale, told in "
          "rhymed couplets and a sing-song measure, about an island economy of trinkets and tourists that is "
          "really an account of a small, happy, improvised society - a circle of friends and lovers whose "
          "hospitality is its own justification, and whose 'marvel of poetry and irony' is the poem's own "
          "description of itself. The second stage is the loss: the ship sails, the dreamers become sleepers "
          "standing heavily on the dock, and the tone drops from the sing-song into a slower, flatter line. The "
          "third is the departure, in which a gale orders everyone away and the community discovers that it "
          "cannot be divided - 'they none of them would leave without the other' - and goes, all together, "
          "having looked back on love. Read in the context of Ashbery's later work, the ship and the gale are "
          "the AIDS epidemic and the deaths of friends, and the poem's refusal to name them is exactly what has "
          "made readers read it that way: it gives the shape of the loss without its documentation, and finds in "
          "a nursery rhyme the cadence for an obituary. The title is then a question the poem answers "
          "indirectly: one continues by telling the story in the rhythm of a story, and by letting the last "
          "line stand as a definition of what was lost.",
  themes_text="The poem is an elegy that refuses the elegiac vocabulary: its subject is a community of friends "
              "and lovers destroyed by an unnamed epidemic, and its method is to describe the happiness first, "
              "in the present tense of a fairy tale, so that the loss arrives without announcement. Its second "
              "subject is survival - 'How to Continue' is the question the bereaved ask - and its answer is "
              "formal rather than consoling: the poem continues by keeping the measure of the lost world, the "
              "couplets and the party, in the same lines that report its end. The final look back at love is "
              "both the community's gesture and the poem's own.",
  structure="A single poem in three unmarked movements. It opens in rhymed couplets and a ballad measure, moves "
            "into long loose free verse when the ship sails, and returns to a rhymed, chant-like measure for "
            "the departure and the closing line. There is no stanza break between the stages; the change of "
            "music is the only signal, so that the reader experiences the loss as a change in the poem's body "
            "rather than as a turn in an argument.",
  style="A deliberately naive, sing-song beginning - 'Oh there once was a woman' - in lines short enough to "
        "scan; rhyme used for its nursery and ballad associations rather than for wit; a middle section in long "
        "unrhymed lines with the flatness of report ('there were no more dreamers just sleepers in heavy "
        "attitudes'); repeated connectives ('And then', 'And when') that keep the poem in the grammar of "
        "storytelling; a last line that drops the rhyme and ends the poem on four monosyllables.",
  ctx="Published in Hotel Lautre\u0301amont (New York: Farrar, Straus and Giroux, 1992), a book whose title takes "
      "the pseudonym of Isidore-Lucien Ducasse, the Comte de Lautre\u0301amont, and which appeared as Ashbery's "
      "friends were dying in the AIDS epidemic; Ashbery chose it as the final poem from that collection in "
      "Notes from the Air: Selected Later Poems (2007), which selects from ten books published between 1988 and "
      "2005 and won the International Griffin Poetry Prize in 2008.",
  sig="'How to Continue' is among the most anthologised and most discussed poems of Ashbery's later career and "
      "the one most often cited in accounts of his elegiac manner; it is read as his response to the AIDS "
      "epidemic and as the poem in which his late style - the fairy tale that turns into a memorial - is fully "
      "formed. It appears in Notes from the Air and in the selected editions of his work, and it is a standard "
      "piece in the criticism of American poetry of the 1990s.",
  canon="Secondary canon",
  crit="Critics have read the poem as an elegy for the New York art world of the 1970s and 1980s, as a parable "
       "of community and of its loss, and as a late instance of the pastoral Ashbery had practised since Some "
       "Trees; its shift of metre has been discussed as an instance of his habit of letting form carry "
       "argument. The poem's refusal to name its occasion is usually treated as its ethical centre rather than "
       "as evasion.",
  biblio="Collected in Hotel Lautre\u0301amont (New York: Farrar, Straus and Giroux, 1992), where it is the final "
         "poem, and reprinted in Notes from the Air: Selected Later Poems (New York: Ecco, 2007). A selection "
         "of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem's first periodical printing was not established from the sources consulted; it is dated here "
        "from its first book appearance in 1992, which settles the anthology's undated selection. The text was "
        "read in the extract printed by the Poetry Foundation from Notes from the Air and in the contents "
        "listing of Hotel Lautre\u0301amont, which confirms its position as the last poem of the book.",
  ver="partially verified", sources=[W_NFTA, W_HC, W_JA, NAAL]),
]

WORKS += [
W10("Her Kind", AS, "1960", "Poem (three seven-line stanzas)", "major",
  genres=G("Confessional Poetry", "Lyric Poetry", "Formal Verse"),
  themes=T("Gender, feminism and women's lives", "Madness, breakdown and confinement",
           "Sexuality, desire and the closet"),
  movements=M(CONF, SWF),
  overview="'Her Kind' is the most anthologised poem of Anne Sexton's first book, To Bedlam and Part Way Back "
           "(Houghton Mifflin, 1960), and the poem through which she is usually introduced. It is three "
           "seven-line stanzas, each ending with the same line - 'I have been her kind' - and each presenting a "
           "version of the woman who does not fit: the witch who flies over the houses at night, the housewife "
           "who furnishes the cave in the woods, and the woman burned as a heretic who is 'not ashamed to die'. "
           "It was written in the months after her first breakdown and hospitalisation, and it turns the "
           "psychiatric case history into a legend of three women.",
  content="The first stanza sends the speaker out as 'a possessed witch, / haunting the black air, braver at "
          "night', who has done her 'hitch / over the plain houses, light by light': she calls herself a 'lonely "
          "thing, twelve-fingered, out of mind', and concludes that 'A woman like that is not a woman, quite'. "
          "The second stanza is domestic: the speaker has found 'the warm caves in the woods' and filled them "
          "with skillets, carvings, shelves, closets, silks and 'innumerable goods', fixed suppers 'for the "
          "worms and the elves', and is 'whining, rearranging the misaligned' - a woman who is misunderstood. "
          "The third stanza returns to persecution: the speaker has ridden in the driver's cart, waved her nude "
          "arms at the villages going by, and learned 'the last bright routes' as a survivor while the flames "
          "'still bite my thigh' and her ribs crack where the wheels turn; a woman like that, the line says, 'is "
          "not ashamed to die'. Each stanza closes on the refrain that claims all three as the speaker's own "
          "kind.",
  summary="The poem's three parts are three historical roles for the same woman, arranged as a descent from "
          "legend to hearth to stake. The witch of the first stanza is the woman out of doors and out of mind, "
          "whose crime is a freedom of movement - she flies over other people's houses, counting their lights - "
          "and whose punishment is the sentence 'not a woman, quite', the withdrawal of the category itself. "
          "The housewife of the second stanza is the same woman brought inside: her cave is furnished, her "
          "suppers are cooked for worms and elves, and her occupation is 'rearranging the misaligned', which is "
          "both housework and madness. The third stanza is the martyr, and it is the only one in which the poem "
          "gives its speaker triumph: she rides in the cart to the burning, she is a 'survivor' even as the "
          "flames bite, and the closing line - 'not ashamed to die' - replaces the judgement of the first two "
          "stanzas with a claim. The refrain that follows each stanza holds the three together and holds the "
          "poet to them: 'I have been her kind' is simultaneously a confession, a boast and an act of "
          "solidarity, and it is what turns a poem about a witch, a housewife and a heretic into a poem about "
          "the woman writing it. The stanza form enacts the argument: each stanza begins with ordinary rhymed "
          "lines and loosens toward its end, as though the poem could not maintain its own decorum.",
  themes_text="'Her Kind' is a poem about the social construction of the madwoman, and its three figures are the "
              "three available explanations of a woman who will not stay put: she is a witch, she is a shrew, she "
              "is a heretic. Sexton's move is to accept all three accusations and to reverse their valence, so "
              "that the outsider becomes the poem's heroine and the ordinary house her prison. The poem is also "
              "about confinement - the cave, the cart, the stake - and about the body, which is twelve-fingered "
              "in the first stanza, naked in the third, and burned in both. Its refrain makes the speaker a "
              "member of a lineage, and so converts a private diagnosis into a history of women.",
  structure="Three stanzas of seven lines each, with the seventh line of every stanza identical ('I have been "
            "her kind'). The first four lines of each stanza rhyme on an alternating pattern that the last "
            "three abandon; the sixth line of each stanza delivers a judgement on 'a woman like that', and the "
            "refrain answers it. The poem's three-part progress - flight, housekeeping, martyrdom - is a "
            "narrative of escalation.",
  style="Plain, short, mostly monosyllabic lines; a ballad-like movement set up by the rhymes of the first four "
        "lines and deliberately broken by the last three; a syntax of simple declaratives ('I have gone out', "
        "'I have found', 'I have ridden'); startling compound adjectives ('twelve-fingered', 'out of mind', "
        "'knock-kneed'); the plainest possible diction for the most sensational material.",
  ctx="Written in 1958-59, after Sexton's breakdown of 1956 and her hospitalisation at Westwood Lodge, and "
      "collected in To Bedlam and Part Way Back (Boston: Houghton Mifflin, 1960), her first book, which John "
      "Holmes helped to place and whose title announces its subject, the road to and part of the way back from "
      "the asylum. She was studying in Robert Lowell's seminar at Boston University at the time, and the poem "
      "belongs to the moment at which American poetry began to admit the psychiatric hospital as a legitimate "
      "subject; Holmes is said to have advised against the poem's frankness.",
  sig="'Her Kind' is the standard introduction to Sexton and one of the founding poems of American confessional "
      "poetry; its three figures have been read as a feminist counter-mythology, and its refrain has passed into "
      "the common vocabulary of writing about women and madness. It is anthologised in the Norton anthologies "
      "and in most surveys of postwar American poetry, it gave its name to a Boston women's poetry collective "
      "and press, and it is the poem most often quoted in accounts of Sexton's relation to the witch trials and "
      "to second-wave feminism.",
  canon="Major canon",
  crit="Critics read the poem through the Salem witch trials and through the figure of the hysteric, as an "
       "early feminist reclamation of the accusation of madness, and as a formal achievement in which a tight "
       "stanza is made to carry a breakdown. Its relation to Plath's 'Lady Lazarus' and to Lowell's "
       "'Skunk Hour' is a standard comparison in accounts of confessional poetry, and its refrain has been "
       "central to feminist readings of Sexton since the 1970s.",
  biblio="Collected in To Bedlam and Part Way Back (Boston: Houghton Mifflin, 1960); reprinted in The Complete "
         "Poems (Boston: Houghton Mifflin, 1981) and in Selected Poems of Anne Sexton (1988). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem's first magazine printing was not established from the sources consulted; it is dated from "
        "its first book appearance in 1960, which is the date the anthology gives. The text was read in the "
        "widely reproduced printed version; quotations are short.",
  ver="partially verified", sources=[W_HK, W_AS, NAAL]),
W10("The Starry Night", AS, "1962", "Poem (free verse lyric)", "major",
  genres=G("Confessional Poetry", "Lyric Poetry", "Free Verse"),
  themes=T("Art, the artist and the creative life", "Death, illness and mourning", "Madness, breakdown and confinement"),
  movements=M(CONF),
  overview="'The Starry Night' is the best known poem of Anne Sexton's second collection, All My Pretty Ones "
           "(Houghton Mifflin, 1962), and one of the most direct poems she wrote about the wish to die. It takes "
           "its title and its occasion from Vincent van Gogh's painting of 1889, and it reads the painting as an "
           "image of a world boiling with a life the speaker wants to enter by dying. The collection was a "
           "finalist for the National Book Award and made her, with Robert Lowell and Sylvia Plath, one of the "
           "three names of American confessional poetry.",
  content="The poem addresses the town in the painting and then the sky above it: the town does not exist, the "
          "speaker says, 'except where one black-haired tree slips / up like a drowned woman into the hot sky'. "
          "The town is silent; the night boils with eleven stars; the moon, in its orange irons, pushes the "
          "children out of bed; an old serpent swallows the stars. The speaker looks at the painting and says 'Oh "
          "starry starry night! This is how / I want to die', and the line is repeated at the end of the second "
          "stanza. The third stanza moves into the painting's other life - the town, the church, the people - "
          "and the poem ends with the speaker imagining herself swallowed up, 'into that night / of eleven stars', "
          "and asking to be drunk 'with that old, old wine'.",
  summary="The poem is short, and its argument is made by description. It begins by denying the town's reality "
          "so that the tree, the one vertical in the painting, can be the poem's first figure: it slips up 'like "
          "a drowned woman into the hot sky', which yokes the painting's upward movement to a death by water. "
          "The sky then takes over: the night boils, the eleven stars are a fever, the moon in its 'orange irons' "
          "is a madhouse instrument that pushes the children out of bed, and the old serpent which swallows the "
          "stars is at once the Milky Way and the serpent of the asylum. Against this the speaker sets her own "
          "desire without argument - 'This is how I want to die' - and repeats it, so that the wish becomes the "
          "poem's refrain and its only proposition. The last stanza returns to the human detail of the painting, "
          "the town and its people, and imagines being swallowed into the night's eleven stars. The poem's "
          "closing wish, to be drunk with 'that old, old wine', is a wish for absorption and for the loss of the "
          "self that sees, which is why the poem has been read both as an ars poetica and as a suicide note. It "
          "matters that the speaker never describes the painting's colour or its composition: what she takes "
          "from it is a movement and a temperature, the upwardness of the tree and the boiling of the sky, and "
          "the poem's own language heats up to match. The three repetitions of the wish to die are separated by "
          "description, so that each returns as a discovery rather than as a refrain, and the last of them is "
          "given to the town rather than to the speaker: the stars are where the dead are, and the poem's "
          "grammar quietly concedes that it is describing a place it wants to be.",
  themes_text="The poem's subject is the relation between a work of art and the desire it releases: van Gogh's "
              "painting is not a consolation but an invitation, and Sexton's speaker wants what the painting "
              "shows rather than what it means. Its second subject is confinement - the moon's orange irons, the "
              "asylum, the 'old serpent' - and its third is the artist's own madness, which the poem treats as "
              "the price of the vision it admires. The repetition of 'This is how I want to die' is the poem's "
              "ethical crux: it is stated as a fact about the painting's beauty, which is what makes it "
              "disturbing.",
  structure="Three stanzas of free verse, the second and third longer than the first, with the line 'This is how "
            "I want to die' repeated at the end of stanzas one and two and the wish restated, transformed, in the "
            "last lines. The poem's movement follows the eye: tree, sky, stars, moon, then the town, then the "
            "speaker's wish. There is no argumentative connective and no conclusion, only a final image.",
  style="Short lines, many of them end-stopped, with an incantatory repetition of 'This is how I want to die'; "
        "similes that are domestic and violent at once ('like a drowned woman', 'orange irons', 'old serpent'); "
        "a diction of simple nouns and strong verbs; an exclamatory register ('Oh starry starry night!') that "
        "belongs to address and to prayer rather than to description.",
  ctx="Van Gogh's 'The Starry Night' was painted at Saint-Re\u0301my in June 1889; Sexton wrote the poem in the late "
      "1950s or early 1960s for All My Pretty Ones (Boston: Houghton Mifflin, 1962), her second book, written "
      "after her father's death in 1959 and her mother's in 1959 and 1960, and the book in which the death of "
      "parents, the inheritance of a mother's life and the wish to die are worked together. The poem belongs to "
      "the moment at which American poets began to write directly about mental illness and hospitalisation, and "
      "it is contemporary with Plath's own poems on the same subjects.",
  sig="'The Starry Night' is one of the most widely reprinted poems of postwar American poetry and the poem "
      "through which Sexton's treatment of suicide is usually taught; it is a staple of anthologies and "
      "secondary-school and university courses, it is regularly paired with Plath's 'Ariel' and with the "
      "ekphrastic tradition from Auden's 'Muse\u0301e des Beaux Arts' onward, and its refrain is among the most "
      "recognised in American poetry since 1960.",
  canon="Major canon",
  crit="Criticism has read the poem as ekphrasis, as a confessional document, and as an instance of the "
       "feminist recovery of the madwoman; its relation to van Gogh's letters and to the actual composition of "
       "the painting has been examined, and its repetitions have been discussed as a technique of "
       "self-persuasion. It is a standard exhibit in the argument about whether confessional poetry can be "
       "read apart from the biography of the poet.",
  biblio="Collected in All My Pretty Ones (Boston: Houghton Mifflin, 1962); reprinted in The Complete Poems "
         "(1981) and in Selected Poems of Anne Sexton (1988). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The first periodical printing of the poem was not established from the sources consulted; it is dated "
        "from its first book appearance in 1962, which is the date the anthology gives.",
  ver="partially verified", sources=[W_AS, W_CP, NAAL]),
W10("Sylvia's Death", AS, "1966", "Poem (elegy in couplets)", "significant",
  genres=G("Confessional Poetry", "Elegiac Poetry", "Free Verse"),
  themes=T("Death, illness and mourning", "Gender, feminism and women's lives", "Art, the artist and the creative life"),
  movements=M(CONF),
  overview="'Sylvia's Death' is Anne Sexton's elegy for Sylvia Plath, written on 17 February 1963, six days "
           "after Plath's suicide, and first published in Poetry in January 1964 before being collected in the "
           "sequence of Live or Die (Houghton Mifflin, 1966) that won the Pulitzer Prize. It is a long poem in "
           "couplets that addresses the dead poet directly, and it is remarkable for admitting, inside its "
           "grief, the envy and anger that the survivor feels. It is one of the central documents of the "
           "relationship between the two poets who studied together in Robert Lowell's seminar at Boston "
           "University.",
  content="The poem opens by addressing Plath - 'O Sylvia, Sylvia, / with a dead box of stones and spoons' - and "
          "asks where she went after writing her last poems, how she found the courage to 'crawl down alone / "
          "into the death'. It describes her house, her children ('two meteors / wandering loose in the tiny "
          "playroom'), the domestic furniture of a life that the speaker also knew, and the telephone call that "
          "never came. It remembers their meetings in Boston, their letters and conversations, their shared "
          "knowledge of the wish to die, and it accuses her - 'thief!' - of taking a death that the speaker had "
          "wanted for herself. Suicide is personified as 'our boy', the third party of the relationship, whose "
          "'job' of killing them is 'a necessity, a window in a wall or a crib'. The poem ends by naming Plath "
          "in a series of endearments - 'my friend, / my little mother, / my funny duchess, / my blonde thing' - "
          "and by letting her go.",
  summary="'Sylvia's Death' is an elegy that refuses the decorum of elegy. Its first movement establishes the "
          "dead woman in her house, among stones and spoons, with two small children; the domestic detail is "
          "exact and unsentimental, and it is the same detail that Sexton used for her own life. The second "
          "movement asks the unanswerable questions - where did you go, how did you do it, why did you not take "
          "me - and the third remembers the friendship itself: the meetings in Boston, the letters, the shared "
          "nights and the shared knowledge. The poem's most disturbing move is its confession of envy: Plath is "
          "called a thief for dying first, and suicide is figured as 'our boy', a lover the two women had in "
          "common, whose attentions the survivor still wants. That confession is followed by anger and then by "
          "tenderness, and the poem ends in a series of names that are also a leave-taking, each one diminishing "
          "the dead woman to something small enough to be held. The couplet form holds the whole poem in an "
          "even, deliberate tread, so that the wildest statements arrive in the most orderly syntax.",
  themes_text="The poem is about grief as a compound of love, anger and envy, and it is unusual in refusing to "
              "separate them. Its second subject is the shared wish to die, which makes the friend's suicide both "
              "a betrayal and a promise. Its third is the condition of the woman poet in the early 1960s: the "
              "house of stones and spoons, the children like meteors, the domestic imprisonment that the poem "
              "treats as the setting of both women's art. The elegy's final naming turns the dead rival back "
              "into a friend without resolving the competition, which is the poem's honesty.",
  structure="A long poem in unrhymed couplets, running to about a hundred and forty lines, with no stanza "
            "divisions and no numbered sections; its movement is associative and returns repeatedly to the same "
            "phrases - 'O Sylvia, Sylvia', the question of where she went, the figure of death as a boy. Direct "
            "address throughout, with the dead woman as the poem's only audience until the last lines, when the "
            "speaker turns to her own survival.",
  style="Short, tight couplets with a strong caesura in the middle of many lines; a spoken, colloquial diction "
        "broken by exclamations and by repetition; domestic nouns used as the furniture of elegy ('stones and "
        "spoons', 'the tiny playroom'); personification of death and of suicide; a refusal of metaphor in the "
        "places where elegy usually supplies it.",
  ctx="Written in Boston on 17 February 1963, six days after Plath's death on 11 February, and first published "
      "in Poetry, vol. 103, no. 4 (January 1964), 224-226, as part of the memoir 'The Barfly Ought to Sing' "
      "commissioned by TriQuarterly for its 1966 tribute to Plath; collected in Live or Die (Boston: Houghton "
      "Mifflin, 16 September 1966), which won the Pulitzer Prize for Poetry in 1967. Sexton and Plath had met "
      "in Robert Lowell's seminar at Boston University in 1959, and the poem is the earliest substantial "
      "response by a fellow poet to Plath's death, written three years before Ariel appeared in the United "
      "States.",
  sig="'Sylvia's Death' is the founding poem of the Sexton-Plath relationship as literary history and one of the "
      "first poems in which a woman poet mourns another without suppressing the competition between them; it is "
      "a standard text in the study of confessional poetry, of elegy and of the literary friendship, and the "
      "body of writing it started - Sexton's memoir, the Plath biographies, the arguments about the two poets' "
      "mutual influence - has made it a document as well as a poem.",
  canon="Secondary canon",
  crit="Critics have read the poem as an elegy that inverts the conventions of the form, as a document of the "
       "Sexton-Plath friendship and its one-sided record, and as an early instance of the feminist critique of "
       "domestic confinement; its couplets, unusually regular for Sexton, have been discussed as a way of "
       "containing material that the poem says cannot be contained. Its relation to Plath's own late poems, and "
       "to the question of influence between the two, remains a continuing argument.",
  biblio="First published in Poetry, vol. 103, no. 4 (January 1964), 224-226, with Sexton's memoir 'The Barfly "
         "Ought to Sing'; collected in Live or Die (Boston: Houghton Mifflin, 1966); reprinted in The Complete "
         "Poems (1981). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The 1964 printing in Poetry predates the book, and the anthology's date of 1966 is the date of the "
        "collection. The poem's composition date of 17 February 1963 is given by the scholarship on the "
        "Sexton-Plath friendship; the sources disagree on whether TriQuarterly's Plath tribute appeared in 1963 "
        "or 1966, so the record cites only the Poetry printing, which is documented.",
  ver="partially verified", sources=[W_SD, W_PF_SD, W_LOD, W_AS, NAAL]),
W10("Little Girl, My String Bean, My Lovely Woman", AS, "1966", "Poem (free verse address)", "significant",
  genres=G("Confessional Poetry", "Lyric Poetry", "Free Verse"),
  themes=T("Family, marriage and domestic life", "Gender, feminism and women's lives",
           "Childhood, adolescence and coming of age"),
  movements=M(CONF, SWF),
  overview="'Little Girl, My String Bean, My Lovely Woman' is a poem to Anne Sexton's elder daughter, Linda Gray "
           "Sexton, written as the girl approached twelve, and collected in Live or Die (Houghton Mifflin, 1966). "
           "It is one of the few poems in her work that is unambiguously celebratory: the mother looks at her "
           "daughter's changing body and finds in it 'nothing ... that lies', and the poem's subject is the "
           "continuity of women's bodies rather than the damage they do. It is also, read beside the poems of "
           "the same book, a poem about what a mother cannot protect a daughter from.",
  content="The poem begins with the daughter at eleven, 'almost twelve', and compares her to a garden ('my"
          " daughter, at eleven / (almost twelve), is like a garden'). It watches her grow - the string bean of the "
          "title, the long-legged girl - and addresses her directly about the body she is acquiring, about its "
          "changes and about the beauty of what is happening to her. The mother says that there is nothing in the "
          "daughter's body that lies, that all that is new is telling the truth; she remembers her own body and "
          "her own mother, and the poem moves between three generations of women. Its later passages celebrate "
          "the daughter's future - the lovers, the children - and the poem ends in an act of handing over, the "
          "mother naming the girl 'my lovely woman' and letting her go.",
  summary="The poem is built as a series of addresses to a daughter who is present in the room, and its "
          "argument is that the body tells the truth. Sexton begins with the garden simile, which makes the girl "
          "a growing thing, and develops it into a description of the changes of puberty that is both exact and "
          "affectionate: the lengthening legs, the new hips, the 'string bean' thinness that is about to become "
          "something else. The mother's voice moves between admiration and memory, and the memory is of her own "
          "girlhood and of her mother, so that the poem becomes a genealogy of the female body in three "
          "generations. Where Sexton's other poems of the same period record the damage done by mothers to "
          "daughters, this one records the attempt to break the sequence: the mother says that the daughter's "
          "body does not lie, that she has nothing to hide from her, and that she will not repeat the silence she "
          "inherited. The poem's ending gives the daughter away to her future without regret, and the title's "
          "three names - little girl, string bean, lovely woman - are the poem's summary of what a mother sees at "
          "once.",
  themes_text="The poem is about the mother-daughter relation as the transmission of a body and of a history; "
              "its central claim is that the female body, far from being the site of shame that the culture "
              "makes it, is a source of knowledge. It is also about time, since the mother sees the girl's future "
              "in her present and knows that her own body is the past of it. The poem's place in Sexton's work is "
              "defined by contrast: it belongs to the same book as 'Wanting to Die' and 'Sylvia's Death', and its "
              "happiness is therefore inseparable from the knowledge of what surrounds it.",
  structure="A single continuous poem in short free-verse lines, addressed throughout to the daughter; its "
            "movements are marked by changes of subject rather than by stanza breaks - the garden, the body, the "
            "grandmother, the future, the leave-taking. The repetition of the daughter's names as a refrain holds "
            "the sections together and makes the poem a lullaby as much as an address.",
  style="Short lines with heavy enjambment, so that the sentence runs across the line break and the poem keeps "
        "its spoken quality; a diction of the kitchen and the garden ('string bean', 'garden', 'the good earth'); "
        "direct second-person address with imperatives and questions; a lullaby rhythm in the repeated names; "
        "almost no punctuation at the ends of lines.",
  ctx="Written in the mid-1960s and collected in Live or Die (Boston: Houghton Mifflin, 16 September 1966), the "
      "book that won the Pulitzer Prize in 1967; Linda Gray Sexton was born in 1953, so the poem's daughter of "
      "'eleven (almost twelve)' dates it to about 1965. The poem belongs to the years of Sexton's most intense "
      "public success and of her continuing treatment, and it is one of the poems in which she writes against "
      "the grain of her own subject matter.",
  sig="The poem is among the most anthologised of Sexton's poems of motherhood and the one most often set beside "
      "Plath's 'Morning Song' and 'Nick and the Candlestick' in accounts of the poetry of maternity; it is a "
      "standard exhibit in feminist readings of Sexton, which have used it to argue against the view of her as "
      "purely a poet of breakdown, and its title has become one of the recognisable phrases of postwar American "
      "poetry.",
  canon="Secondary canon",
  crit="Critics have read the poem as a counterweight to the poems of maternal damage in the same collection, as "
       "an instance of the feminist revaluation of the body, and as a poem about the possibility of breaking the "
       "mother-daughter inheritance. Its relation to Linda Gray Sexton's own memoirs, and to the ethics of "
       "writing about one's children, has been discussed since the 1990s.",
  biblio="Collected in Live or Die (Boston: Houghton Mifflin, 1966); reprinted in The Complete Poems (1981) and "
         "in Selected Poems of Anne Sexton (1988). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The first periodical printing was not established from the sources consulted; the poem is dated from "
        "its collection in 1966, which is the date the anthology gives. Its composition can be dated "
        "approximately from the daughter's age.",
  ver="partially verified", sources=[W_LOD, W_CP, W_AS, NAAL]),
W10("The Ballad of the Lonely Masturbator", AS, "1969", "Poem (ballad in rhymed stanzas)", "significant",
  genres=G("Confessional Poetry", "Love Poetry", "Formal Verse"),
  themes=T("Sexuality, desire and the closet", "Love, intimacy and loss", "Gender, feminism and women's lives"),
  movements=M(CONF, SWF),
  overview="'The Ballad of the Lonely Masturbator' is the best known poem of Anne Sexton's Love Poems (Houghton "
           "Mifflin, 1969), a book written during and after the affair that ended her marriage. It is a ballad "
           "in seven-line stanzas whose sixth line is always 'At night, alone, I marry the bed', and it "
           "describes the end of an affair and the ritual of solitary sex that replaces it. The title's "
           "bluntness was scandalous in 1969 and is the point of the poem: it takes the most private of acts and "
           "gives it the most public of forms.",
  content="The poem opens on a judgement - 'The end of the affair is always death' - and then, in the first "
          "stanza, describes the lover's absence: 'She's my workshop. Slippery eye, / out of the tribe of myself "
          "my breath / finds you gone'. The refrain follows at the end of the stanza: 'At night, alone, I marry "
          "the bed'. The following stanzas move through the body, through memory and through anger: 'Finger to "
          "finger, now she's mine', 'I beat her like a bell', 'You borrowed me on the flowered spread'. A rival "
          "appears - 'Then my black-eyed rival came. / The lady of water, rising on the beach' - and the speaker "
          "is left as 'the knock-kneed broom instead'. The poem goes on to return the lover's books and fishing "
          "tack, notes that the newspaper says he is married, and ends with the boys and girls of the town "
          "coupling while the speaker, alone, marries the bed again.",
  summary="The poem is a narrative of the aftermath of an affair, and it uses the ballad's repetitions to make "
          "the aftermath a ritual. Its first stanza establishes the death of the affair and the double figure of "
          "the beloved, who is both 'she' and 'you' - the body that is remembered and the person who has gone - "
          "and the refrain converts the loss into a ceremony performed every night. The middle stanzas are "
          "explicit about the solitary sex that the title names, and they are deliberately unembarrassed: the "
          "bed is a wife, a workshop and an instrument, and the speaker's pleasure is described with the same "
          "plainness as her grief. The arrival of the rival, 'the lady of water, rising on the beach', gives the "
          "poem its turn into anger and self-mockery; the speaker becomes 'the knock-kneed broom', the left-over "
          "domestic object. The last stanzas are the most ordinary and the most desolate: the return of borrowed "
          "books and fishing tackle, the newspaper announcement of the lover's marriage, and the final image of "
          "the town's couples together while the speaker keeps her appointment with the bed. The refrain, "
          "repeated seven times, is both a joke and a vow, and by the last repetition it has become the poem's "
          "definition of a life.",
  themes_text="The poem's subject is desire after abandonment, and its method is to refuse the separation of "
              "the sexual from the domestic and the comic from the grievous. It is a poem about the ownership of "
              "the body: the speaker's pleasure is hers, taken in the bed that was shared, and the 'marriage' of "
              "the refrain is a claim of autonomy as much as a confession of loneliness. Its second subject is "
              "the replaceability of the lover - the rival, the newspaper marriage, the town's couples - and its "
              "third is the deliberate scandal of a woman writing plainly about masturbation in 1969, which is "
              "what has made the poem a document of second-wave feminism as well as of confessional poetry.",
  structure="Seven-line stanzas in which the sixth line is always the same ('At night, alone, I marry the bed') "
            "and the seventh varies or repeats; the poem runs to seven stanzas plus a closing repetition, so that "
            "the refrain accumulates rather than merely recurs. The narrative is chronological - the end, the "
            "grief, the solitary ritual, the rival, the ordinary aftermath - but the refrain holds each stanza at "
            "the same point of the night.",
  style="Ballad measure and rhyme used flatly, without ornament; short lines with strong end-stops; a diction "
        "that mixes the erotic and the domestic ('workshop', 'flowered spread', 'fishing tack'); blunt "
        "monosyllables for the sexual passages; the refrain's four stresses as the poem's fixed pulse; an "
        "occasional shocking simile ('I beat her like a bell', 'the knock-kneed broom').",
  ctx="Written in 1968-69, during and after Sexton's affair with a man she calls only 'the man' in her letters, "
      "and collected in Love Poems (Boston: Houghton Mifflin, 1969), the book that followed the Pulitzer Prize "
      "and that her publisher promoted as a book of love poems; the affair contributed to the end of her "
      "marriage, which was dissolved in 1973. The poem belongs to the moment at which American poetry, and "
      "second-wave feminism with it, began to write openly about female sexual experience.",
  sig="The poem is one of the most discussed and most anthologised of Sexton's later poems and a standard text "
      "in the history of the literature of sexuality; it is regularly cited in accounts of second-wave "
      "feminism's reclamation of the female body, in studies of confessional poetry's ethics, and in the "
      "criticism that asks what it means for a woman poet to publish such material in 1969. Its title has "
      "become a byword for the frankness of Sexton's late work.",
  canon="Secondary canon",
  crit="Feminist critics have read the poem as an assertion of female sexual autonomy and as a parody of the "
       "courtly love tradition that the word 'ballad' invokes; others have read it as an instance of the "
       "confessional mode's risk, in which the poem's scandal is inseparable from its commercial reception. Its "
       "formal control - a strict refrain in a book of loose poems - has been noted as evidence against the view "
       "that Sexton's late work abandoned craft.",
  biblio="Collected in Love Poems (Boston: Houghton Mifflin, 1969); reprinted in The Complete Poems (1981) and "
         "in Selected Poems of Anne Sexton (1988). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The first periodical printing was not established from the sources consulted; the poem is dated from "
        "its collection in 1969, which is the date the anthology gives. The text was read in the Poetry "
        "Foundation's printing of the poem; quotations are short.",
  ver="partially verified", sources=[W_PF_BAL, W_AS, W_CP, NAAL]),
]

WORKS += [
W10("Snapshots of a Daughter-in-Law", AR, "1963", "Poem (ten-part sequence in free verse)", "major",
  genres=G("Lyric Poetry", "Free Verse", "Political Poetry", "Narrative Poetry"),
  themes=T("Gender, feminism and women's lives", "Family, marriage and domestic life",
           "Language, writing and the limits of representation"),
  movements=M(SWF, CONF),
  overview="'Snapshots of a Daughter-in-Law' is the ten-part title poem of Adrienne Rich's third collection, "
           "Snapshots of a Daughter-in-Law: Poems 1954-1962 (Harper & Row, 1963), the book in which she broke "
           "with the formal, Audenesque verse of A Change of World and The Diamond Cutters and began to write "
           "the poem of her own life. Written over three years while she was raising three sons in Cambridge, "
           "Massachusetts, it is a sequence of scenes of women - a daughter-in-law at the sink, a mother-in-law, "
           "Emily Dickinson, Mary Wollstonecraft - held together by a voice that moves between them, and it is "
           "the first poem in which Rich's feminism becomes a poetic method rather than a subject.",
  content="The sequence moves through ten numbered sections. The first presents two handsome women 'gripped in "
          "argument', 'like Furies cornered from their prey', and the second the daughter-in-law at her dishes, "
          "who scalds herself deliberately and thinks of her mother, whose mind is 'mouldering like wedding-cake'; "
          "she resolves 'to be another way'. Later sections quote and answer a masculine tradition - Baudelaire's "
          "'ma semblable, ma soeur' is turned against him - and bring in Emily Dickinson, writing letters in her "
          "father's house, and Mary Wollstonecraft, and the fifteenth-century poet Christine de Pisan. The poem's "
          "images are those of enclosure: a 'commodious steamer-trunk', a pantry, a birdcage, a vault, a "
          "'mail of the mind'. It ends with a winter landscape and a voice that is no longer sure whether it is "
          "the daughter-in-law's or the poet's, and with the line 'the doors of the prison-house stand open'.",
  summary="The poem is a sequence of 'snapshots', and its method is montage: each section holds a scene or a "
          "quotation for a moment and then cuts to the next, so that the reader has to supply the argument that "
          "connects them. Section one gives us two women screaming at one another across cut glass and majolica, "
          "'cornered from their prey', and makes their quarrel a quarrel between a woman and the image of herself "
          "that her world has given her. Section two gives us the domestic interior and the daughter-in-law's "
          "self-harm at the sink, which is also an act of privacy, and the mother whose mind is 'mouldering like "
          "wedding-cake' - the marriage plot arriving as decay. The middle sections turn to the women writers who "
          "lived the same contradiction: Dickinson, who wrote in her father's house, Wollstonecraft, and the "
          "medieval Christine, whose learning was counted against her. The poem's quotations of male poets are "
          "not simply rejected; they are answered, turned inside out, so that 'ma semblable, ma soeur' becomes a "
          "description of the relation between women rather than a sneer. What the sequence argues, without "
          "stating it, is that the entrapment of the daughter-in-law in her kitchen and the achievement of the "
          "woman writer are the same history seen at different distances. The ending opens the prison-house doors "
          "but does not say what is outside them, and that hesitation is the poem's honesty.",
  themes_text="The poem's subject is the relation between a woman's domestic life and her intellectual life, and "
              "it refuses the choice the culture offers between them: the daughter-in-law scalds herself at the "
              "sink, and the poet quotes Dickinson. Its second subject is the tradition of women's writing, which "
              "the poem constructs as a set of precursors - Dickinson, Wollstonecraft, Christine - who are "
              "present in the same poem as the dishes. Its third is enclosure and its figures: the trunk, the "
              "pantry, the cage, the vault. The violence of the language - Furies, prey, flies, knives - makes "
              "the poem's account of domesticity anything but gentle, and its ending holds out a release that it "
              "refuses to describe.",
  structure="Ten numbered sections of unequal length, in free verse with a strong rhythmic organisation by "
            "phrase and by repetition rather than by metre; sections juxtapose the contemporary domestic scene "
            "with historical and literary material, and the transitions are made by image rather than by "
            "argument. Quotation is set into the verse without quotation marks, so that the poem's 'own' voice "
            "and its borrowed voices are not clearly separated.",
  style="Long, irregular lines whose measure is rhetorical rather than metrical; a syntax that runs over the line "
        "break and often over the stanza break; dense imagery drawn from domestic objects and from myth; "
        "quotation and near-quotation of other writers; a tone that moves from the satiric to the elegiac within "
        "a section; an undercurrent of bodily disgust and of desire for escape.",
  ctx="Written between 1958 and 1960, while Rich was living in Cambridge, Massachusetts, married to the economist "
      "Alfred Conrad and raising three small sons, and published in Snapshots of a Daughter-in-Law: Poems "
      "1954-1962 (New York: Harper & Row, 1963). She later wrote that the book had taken her three years to "
      "write and six to publish, that the Times ignored it after praising her first two books, and that her "
      "father called the poems 'sordid, irritable and often nasty'. It appeared the year after The Feminine "
      "Mystique, and is one of the first books of American poetry to register the dissatisfaction that book "
      "described.",
  sig="'Snapshots of a Daughter-in-Law' is the poem in which Adrienne Rich's feminism becomes visible and the "
      "book from which her later poetry is usually dated; it is a standard anthology text in courses on "
      "postwar American poetry and on women's writing, and it is one of the poems through which the origins of "
      "second-wave feminist poetry in the United States are taught. Its montage method - the historical "
      "fragment beside the contemporary kitchen - became one of the standard procedures of feminist poetry in "
      "the 1970s.",
  canon="Major canon",
  crit="Criticism has read the poem as a transitional work between the formal early Rich and the political later "
       "Rich, as an early instance of feminist montage, and as a poem divided against itself in ways that are "
       "thematically productive; the question of its relation to the confessional poetry of Lowell and Sexton "
       "has been discussed at length, since Rich's 'I' is historical rather than therapeutic. Its treatment of "
       "Dickinson in particular has been central to the feminist criticism of the 1970s and after.",
  biblio="Collected as the title poem of Snapshots of a Daughter-in-Law: Poems 1954-1962 (New York: Harper & "
         "Row, 1963); reprinted in Collected Early Poems 1950-1970 (1993) and in Adrienne Rich's Poetry and "
         "Prose (Norton Critical Edition, 1993). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The first periodical printing of the poem was not established from the sources consulted, so the record "
        "dates it from its first book appearance in 1963, which is the date the anthology gives. The text was "
        "read through the printed extracts and the critical accounts consulted; quotations are short.",
  ver="partially verified", sources=[W_AR, W_NYR, W_HRC, NAAL]),
W10("\"I Am in Danger\u2014Sir\u2014\"", AR, "1966", "Poem (free verse monologue)", "significant",
  genres=G("Lyric Poetry", "Dramatic Poetry", "Free Verse"),
  themes=T("Art, the artist and the creative life", "Gender, feminism and women's lives",
           "Language, writing and the limits of representation"),
  movements=M(SWF),
  overview="'I Am in Danger-Sir-' is a short poem in the voice of Emily Dickinson, collected in Adrienne Rich's "
           "Necessities of Life: Poems 1962-1965 (W. W. Norton, 1966). Its title is a quotation from Dickinson's "
           "letters to Thomas Wentworth Higginson, the man of letters who became her correspondent and who "
           "advised her not to publish; the poem takes that sentence and gives it back as a declaration, so that "
           "the poet's famous seclusion and her refusal of the literary market become an assertion of authority.",
  content="The poem addresses a 'Sir' - Higginson, the editor and critic, and, behind him, the whole apparatus of "
          "publication and taste - and answers his advice. It speaks in Dickinson's voice about the conditions of "
          "her writing: the house, the garden, the room upstairs, the poems written on scraps of paper, the "
          "letters that were her public. It refuses the terms in which she was offered help, and it claims for "
          "her work the very danger that the phrase in the title mentions, so that 'I am in danger, sir' becomes "
          "not a confession of female fragility but a statement about what the writing is. It is short, "
          "compressed and epigrammatic in Dickinson's manner.",
  summary="The poem is a monologue of some twenty lines in which Rich inhabits Dickinson and answers her editor. "
          "Its occasion is the correspondence with Higginson that began in 1862, when Dickinson wrote to him "
          "asking whether her verse was 'alive', and continued until her death; Higginson's advice, in effect, "
          "was to wait, to regularise her metre, and not to publish. Rich's poem takes his intervention as the "
          "type of all masculine mediation of women's writing and answers it from inside Dickinson's own "
          "vocabulary - the house, the room, the garden, the letter, the 'Balm' and the 'Bee'. The title's "
          "quotation is the poem's argument: Dickinson's declaration of danger, written to the man who had "
          "offered to protect her, is reread as a claim to the risk that writing is. The poem does not narrate; "
          "it asserts, and it ends on an assertion that is also a refusal - the refusal of the terms on which "
          "genius was to be licensed.",
  themes_text="The poem is about the relation of a woman writer to her editor and to the literary institution he "
              "represents, and it reads Dickinson's seclusion not as pathology but as a choice about the "
              "conditions of work. Its second subject is the materiality of writing - paper scraps, letters, the "
              "room - which Rich, later a great editor of Dickinson's manuscripts, insists on. Its third is "
              "aesthetics: the poem is an argument, made in Dickinson's own compressed measure, that the formal "
              "strangeness for which she was criticised is the mark of the poetry's life.",
  structure="A single short poem without stanza divisions in most printings, in short free-verse lines that echo "
            "Dickinson's hymn measure without adopting it; a dramatic monologue spoken throughout by Dickinson, "
            "with no frame and no narrator's commentary. The title is part of the poem: it supplies the "
            "addressee and the quotation that the body of the poem answers.",
  style="Short lines, abrupt syntax and heavy dashes in Dickinson's manner, used sparingly rather than imitated; "
        "a diction of the household and of the garden; capitalised abstractions; a rhetorical structure of "
        "assertion and withdrawal; a voice that is cool, ironic and absolute by turns.",
  ctx="Collected in Necessities of Life: Poems 1962-1965 (New York: W. W. Norton, 1966), the book written during "
      "Rich's years of anti-war and civil rights activism, when her marriage was under strain and her poetry was "
      "moving from the formal verse of her first two books to the documentary and political manner of The Will "
      "to Change. The poem belongs to the same period as 'When We Dead Awaken: Writing as Re-Vision' (1971), in "
      "which Rich argued that women must reread the literary tradition in order to write at all.",
  sig="'I Am in Danger-Sir-' is a standard text in the feminist criticism of the 1960s and 1970s and one of the "
      "earliest poems in which a twentieth-century woman poet enters the voice of a nineteenth-century one in "
      "order to argue with the institution that mediated her; it is anthologised in the Norton anthologies and "
      "in collections of American women's poetry, and it prepared the ground for Rich's own later work on "
      "Dickinson, including her editions of the fascicles and her essay 'Vesuvius at Home'.",
  canon="Secondary canon",
  crit="Critics have read the poem as a founding instance of the feminist practice of 'writing back' to the "
       "tradition, as an intervention in the editing and reception of Dickinson, and as a poem about the "
       "institutional mediations - editors, letters, publication - that surround a woman's text. Its relation "
       "to Rich's later essay on Dickinson, and to the feminist recovery of Dickinson's manuscripts, has been "
       "widely discussed.",
  biblio="Collected in Necessities of Life: Poems 1962-1965 (New York: W. W. Norton, 1966); reprinted in "
         "Collected Early Poems 1950-1970 (1993) and in Adrienne Rich's Poetry and Prose (Norton Critical "
         "Edition, 1993). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first periodical printing was not established from the sources consulted; the poem is dated from "
        "its collection in 1966, which is the date the anthology gives. The title's quotation from Dickinson's "
        "letters is given in the anthology's punctuation.",
  ver="partially verified", sources=[W_AR, W_HRC, NAAL]),
W10("A Valediction Forbidding Mourning", AR, "1971", "Poem (free verse lyric)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Political Poetry"),
  themes=T("Gender, feminism and women's lives", "Language, writing and the limits of representation",
           "Love, intimacy and loss"),
  movements=M(SWF),
  overview="'A Valediction Forbidding Mourning' is the poem of Adrienne Rich's The Will to Change: Poems "
           "1968-1970 (W. W. Norton, 1971) that most directly confronts the literary tradition: it takes its "
           "title from John Donne's famous poem of parting and answers it, in a woman's voice, about the "
           "impossibility of using a language that has been made by and for men. It belongs to the years of "
           "Rich's divorce, of her anti-war activism and of the essays that became 'When We Dead Awaken', and it "
           "is one of the first poems in which she makes the critique of language itself her subject.",
  content="The poem begins with a refusal of the metaphor by which Donne's lovers are joined: it speaks of the "
          "difficulty of writing at all, of 'the thing I came for', and of a language that is 'the enemy'. Its "
          "images are of maps, tools and instruments, of the 'tongue of the past', of the 'spike' and the "
          "'compass', and it quotes and reverses the terms of Donne's conceit so that the circle drawn by the "
          "compass becomes a trap rather than a proof of union. The poem is short, compressed, and ends on the "
          "recognition that the words available to it are 'the enemy's' words, and that the poem must use them "
          "anyway.",
  summary="The poem's occasion is a parting, but its subject is the language in which a parting can be said. "
          "Donne's 'A Valediction: Forbidding Mourning' consoles two lovers by comparing their souls to the twin "
          "legs of a drafting compass, one fixed at the centre and one travelling the circle back to it; Rich's "
          "poem takes the same instrument and makes it an image of the constraint under which a woman writes, "
          "so that the circle that Donne meant as fidelity becomes the closed circuit of a tradition that "
          "returns every woman's sentence to its origin in a man's. The poem's short lines refuse the "
          "discursive ease of its model: where Donne argues, Rich asserts and then withdraws, and the syntax is "
          "broken so that the reader has to supply the connections. Its repeated words - 'the thing', 'the "
          "enemy', 'the tongue' - make it a poem about naming, and its refusal to name the beloved directly is "
          "part of its argument about what a woman's love poem can and cannot say in the inherited forms. The "
          "ending neither consoles nor wins; it records the condition of writing against a language one cannot "
          "do without.",
  themes_text="The poem is about the politics of the literary tradition: the recognition that the forms and "
              "metaphors a poet inherits carry the assumptions of the society that made them, and that a woman "
              "writer's relation to them is therefore never neutral. Its second subject is the possibility of a "
              "love poetry that is not founded on the exchange of one person into another's figure. Its third is "
              "the practical experience of writing in the early 1970s, when Rich was making, in her poetry and "
              "her essays, the argument that a woman must reread and rewrite the tradition in order to write at "
              "all.",
  structure="A short free-verse poem in irregularly broken lines, with no stanza divisions in most printings; "
            "its argument is made by the juxtaposition of the inherited conceit and a contemporary voice that "
            "cannot use it. The title announces its relation to Donne and the poem does not explain the "
            "relation, so that the reader's recognition is part of the poem's method.",
  style="Short lines broken at the point of syntactic strain; a vocabulary of instruments and of the body; "
        "repetition of a small number of charged words; a refusal of the simile and the conceit that the poem "
        "is criticising, so that the poem's own figures are minimal; a tone that is cold, exact and finally "
        "unresolved.",
  ctx="Collected in The Will to Change: Poems 1968-1970 (New York: W. W. Norton, 1971), the book written during "
      "Rich's divorce, her activism against the Vietnam War and her turn to feminism; it is contemporary with "
      "the essay 'When We Dead Awaken: Writing as Re-Vision' (1971), in which she argued that women must "
      "re-read the tradition 'with new eyes' in order to write. The title alludes to Donne's 'A Valediction: "
      "Forbidding Mourning', first printed in 1633.",
  sig="The poem is the standard exhibit in accounts of Rich's turn to the critique of language and of the "
      "literary tradition, and it is anthologised as one of the first American poems to make the answer to a "
      "canonical male text its formal principle; it is regularly taught beside Donne's poem and beside the "
      "essays of 'When We Dead Awaken', and it belongs to the small group of poems through which the feminist "
      "practice of revisionist reading was established in the 1970s.",
  canon="Secondary canon",
  crit="Criticism has read the poem as an example of 're-vision' in the sense Rich gave the word, as an "
       "intervention in the metaphysical tradition, and as a poem about the difficulty of writing love poetry "
       "in a political moment; its relation to Donne's conceit, and to the question of whether a poem can "
       "criticise the language it uses, has been extensively discussed.",
  biblio="Collected in The Will to Change: Poems 1968-1970 (New York: W. W. Norton, 1971); reprinted in "
         "Collected Early Poems 1950-1970 (1993) and in Adrienne Rich's Poetry and Prose (Norton Critical "
         "Edition, 1993). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first periodical printing was not established from the sources consulted; the poem is dated from "
        "its collection in 1971, which is the date the anthology gives. The record shares its title with "
        "Donne's poem but is a distinct work.",
  ver="partially verified", sources=[W_AR, W_HRC, NAAL]),
W10("Diving into the Wreck", AR, "1973", "Poem (long free-verse lyric)", "major",
  genres=G("Lyric Poetry", "Free Verse", "Political Poetry", "Narrative Poetry"),
  themes=T("Gender, feminism and women's lives", "Language, writing and the limits of representation",
           "History, truth and the uses of the past"),
  movements=M(SWF),
  overview="'Diving into the Wreck' is the title poem of Adrienne Rich's seventh book, Diving into the Wreck: "
           "Poems 1971-1972 (W. W. Norton, 1973), and the poem through which her middle period is known. It "
           "describes a scuba diver descending to a wreck, with a book of myths in which the diver's name does "
           "not appear, in order to see the damage that was done and the treasures that prevail; it turns the "
           "descent into an allegory of the woman writer's relation to history. The book won the National Book "
           "Award for Poetry in 1974, which Rich refused as an individual and accepted, with Audre Lorde and "
           "Alice Walker, on behalf of all women.",
  content="The poem is in ten sections. It begins with the preparation of the diver - 'I put on / the body-armor "
          "of black rubber, / the absurd flippers, / the grave and awkward mask' - and the descent, which is "
          "also a descent out of the ordinary social world: 'the sea is another story'. The diver descends a "
          "ladder that 'hangs / from the side of the schooner' into water that is 'the same as always'. The "
          "wreck appears, and the diver explores its cabin, its cargo, its instruments, finding 'the thing itself "
          "and not the myth'. The poem's most quoted lines describe the diver as 'she who is me' and the "
          "creature in the wreck as 'I am she: I am he', a merging of the sexes in the figure of the survivor. "
          "The book of myths, in which 'our names do not appear', is carried down and remains, and the poem ends "
          "in the wreck's cabin, among its treasures and its damage.",
  summary="The poem's narrative is a dive, described with technical precision and without allegorical pointing. "
          "The diver dresses - the rubber suit, the flippers, the mask, the knife - and the equipment is "
          "insisted on as equipment, absurd and necessary, before it becomes a figure for anything. The descent "
          "is a passage out of one medium into another: the sea is 'another story', the ladder descends from the "
          "schooner into water that does not change, and the diver's breathing is audible all the way down. The "
          "wreck appears first as a shadow and then as a structure, and the exploration of it is an exploration "
          "of a ruined household: the cabin, the cargo, the 'silver, copper, vermeil cargo', the drowned faces. "
          "The poem's central recognition is that the diver has come to see the damage and not the myth, and that "
          "the book of myths in which the divers' names do not appear is nonetheless carried along. Its most "
          "famous lines dissolve the distinction between the selves - 'I am she: I am he' - and the wreck's "
          "survivor becomes both the woman and the man, the drowned and the living, so that the poem's "
          "allegory, if it has one, is about the recovery of a common history rather than a separate one. The "
          "ending refuses both rescue and consolation: the diver is in the wreck, among the tools and the "
          "corrosion, and that is where the poem leaves her.",
  themes_text="The poem's subject is the relation of the present to a damaged past, and it makes the dive a "
              "method: to go down to the wreck is to refuse the available versions of history and to look at the "
              "damage directly. Its second subject is gender, and its treatment of it is deliberately "
              "unsettling: the diver, 'she who is me', becomes 'he' in the wreck and the wreck's survivor is "
              "'I am she: I am he', which makes the poem an argument about the commonness of the catastrophe "
              "rather than a separate women's history. Its third subject is the book of myths in which the "
              "divers' names do not appear - the written record that has excluded them - and the poem's own "
              "relation to it, since the poem is itself a book that names them.",
  structure="Ten numbered sections, in free verse, whose sequence follows the dive: the equipment, the descent, "
            "the approach, the wreck, the cabin, the cargo, the recognition, the ending. The sections are held "
            "together by repetition of phrases from section to section ('the sea is another story', 'the book of "
            "myths') and by the persistence of the second person, so that the poem addresses a companion who is "
            "also the reader and also the self.",
  style="Long unrhymed lines with a strong caesura and a prose-like clarity; technical vocabulary used literally "
        "and only then figuratively; repetition of whole sentences as refrain; a second-person address that "
        "shifts its object; almost no simile in the dive itself, so that the allegory is carried by the "
        "narrative rather than by ornament.",
  ctx="Written in 1972 and collected in Diving into the Wreck: Poems 1971-1972 (New York: W. W. Norton, 1973), "
      "the book that followed Rich's divorce, her move to New York and her increasing involvement in the "
      "women's movement; it won the National Book Award for Poetry in 1974, a prize she declined as an "
      "individual and accepted jointly with Audre Lorde and Alice Walker 'on behalf of all women', a gesture "
      "that became a defining moment of second-wave feminist literary politics. The poem's wreck is not any "
      "particular ship; the dive is a figure for the encounter with a history that has been submerged.",
  sig="'Diving into the Wreck' is the central poem of Rich's middle period and one of the most influential "
      "American poems of the 1970s; its images - the body-armour, the book of myths, the wreck - have become "
      "part of the common vocabulary of feminist criticism, and the National Book Award gesture made the poem "
      "and its book a public event. It is a standard anthology text in courses on postwar American poetry, "
      "women's writing and the literature of the 1970s.",
  canon="Major canon",
  crit="Criticism has read the poem as an allegory of feminist historiography, as a rewriting of the descent "
       "narratives of epic and of psychoanalysis, and as a poem whose dissolving of gender - 'I am she: I am "
       "he' - has been central to the debate about essentialism in feminist poetics. Its relation to Rich's "
       "essays of the same years, and to the work of Adrienne Rich's contemporaries among women poets, has been "
       "extensively discussed.",
  biblio="Collected as the title poem of Diving into the Wreck: Poems 1971-1972 (New York: W. W. Norton, 1973); "
         "reprinted in Poems: Selected and New, 1950-1974 (1974) and in Adrienne Rich's Poetry and Prose "
         "(Norton Critical Edition, 1993). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The first periodical printing was not established from the sources consulted; the poem is dated from "
        "its collection in 1973, which is the date the anthology gives. The book's fifth printing is sometimes "
        "dated 1975 in library records; 1973 is the first edition.",
  ver="partially verified", sources=[W_DW, W_AR, NAAL]),
]

WORKS += [
W10("Power", AR, "1978", "Poem (free verse lyric)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Political Poetry"),
  themes=T("Gender, feminism and women's lives", "Art, the artist and the creative life",
           "History, truth and the uses of the past"),
  movements=M(SWF),
  overview="'Power' is the poem that opens Adrienne Rich's The Dream of a Common Language: Poems 1974-1977 "
           "(W. W. Norton, 1978), the first book she published after coming out as a lesbian in "
           "1976. It is a short poem in five couplets about Marie Curie, who discovered polonium and radium and "
           "died of the radiation that made her famous, and it reads her life as a parable of the cost at which "
           "women have been permitted power. It is one of Rich's most quoted poems and the clearest statement of "
           "the book's argument about power, gender and knowledge.",
  content="The poem's first image is an archaeological one: the speaker has been 'living in the earth-deposits of "
          "our history', and a backhoe has uncovered a bottle of 'a hundred-year-old cure for fever or "
          "melancholy' - a tonic, a patent medicine, an old promise of relief. The poem then turns to Marie "
          "Curie, 'denying / her wounds / denying / her wounds came from the same source as her power'. The "
          "final image is of Curie's hands, and of the notebooks that are still radioactive and must be kept in "
          "lead-lined boxes. The poem's argument is carried by the juxtaposition of the two women: the anonymous "
          "maker of the tonic and the famous scientist, both of whom worked with the substances of the earth and "
          "both of whom paid for it in the body.",
  summary="The poem works as a diptych. Its first movement uncovers the past as an excavation: 'living in the "
          "earth-deposits of our history', the speaker watches a backhoe split open the ground and reveal a "
          "bottle, amber and perfect, 'a hundred-year-old cure for fever or melancholy', a tonic 'for living on "
          "this earth / in the winters of this climate'. The bottle is a woman's remedy, a domestic medicine, "
          "and the poem treats it without condescension: it is a real attempt at relief, made by someone whose "
          "name is not recorded. The second movement names Marie Curie, who 'died a famous woman denying / her "
          "wounds / denying / her wounds came from the same source as her power'. The lines have the flatness of "
          "an epitaph, and their force comes from the double denial: Curie denied that the radium was killing "
          "her, and the world has denied that her achievement and her destruction were one thing. The poem does "
          "not resolve the relation between the anonymous herbalist and the Nobel laureate; it sets them side by "
          "side as two women who worked with what the earth contained, and it asks the reader to see that the "
          "difference between them is a difference in public record rather than in kind.",
  themes_text="The poem's subject is the cost of women's power and the way that cost is written out of the "
              "record: Curie's fame depends on the denial of her wounds, and the anonymous maker of the tonic is "
              "not famous at all. Its second subject is knowledge as a physical practice - the backhoe, the "
              "bottle, the lead-lined notebooks - and the body as the instrument and the casualty of that "
              "practice. Its third is history itself, figured as stratified earth that has to be excavated: the "
              "'earth-deposits of our history' contain both the cure and the poison, and the poem refuses to "
              "choose between them.",
  structure="Five unrhymed couplets, with a turn between the third and fourth: the first three couplets are the "
            "excavation and the tonic, the last two are Curie and her denial. The poem's brevity is part of its "
            "argument; it offers no explanation of the connection it draws, and its two halves are held together "
            "only by the phrase 'earth-deposits' and by the idea of a substance that both heals and harms.",
  style="Short, flat, declarative lines; a couplet form that sets two statements against each other; a diction "
        "that mixes the archaeological and the medical ('earth-deposits', 'backhoe', 'tonic', 'melancholy'); a "
        "deliberate refusal of metaphor in the Curie section, where the plainest possible statement is the most "
        "damning; repetition ('denying / her wounds / denying') used to make the denial visible.",
  ctx="Collected in The Dream of a Common Language: Poems 1974-1977 (New York: W. W. Norton, 1978), the first "
      "book Rich published after coming out as a lesbian in 1976 and the book in which she began to write "
      "explicitly for a community of women; its three sections - 'Power', 'Twenty-One Love Poems' and 'Not "
      "Somewhere Else, But Here' - are organised around the question the title announces. Marie Curie "
      "(1867-1934) won the Nobel Prize in Physics in 1903 and in Chemistry in 1911 and died of aplastic "
      "anaemia caused by radiation exposure; her notebooks remain radioactive and are kept in lead-lined boxes.",
  sig="'Power' is one of the most anthologised poems of Rich's later work and the standard text for her argument "
      "about women, knowledge and cost; its lines about Curie are among the most quoted in American feminist "
      "poetry, and the poem is central to the teaching of The Dream of a Common Language and of the poetry of "
      "the women's movement of the 1970s.",
  canon="Secondary canon",
  crit="Critics have read the poem as an exemplary feminist history, as a critique of the ideology of scientific "
       "heroism, and as a poem about the materiality of knowledge; its pairing of Curie with an anonymous maker "
       "of patent medicine has been discussed as a model of Rich's practice of constructing a women's tradition "
       "out of the surviving record. Its relation to the rest of The Dream of a Common Language has been "
       "extensively analysed.",
  biblio="Opens The Dream of a Common Language: Poems 1974-1977 (New York: W. W. Norton, 1978); reprinted in Adrienne Rich's Poetry and Prose (Norton Critical Edition, "
         "1993). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first periodical printing was not established from the sources consulted; the poem is dated from "
        "its collection in 1978, which is the date the anthology gives.",
  ver="partially verified", sources=[W_DCL, W_AR, NAAL]),
W10("Transcendental Etude", AR, "1978", "Poem (long free-verse meditation)", "major",
  genres=G("Lyric Poetry", "Long Poem", "Free Verse"),
  themes=T("Art, the artist and the creative life", "Gender, feminism and women's lives",
           "Love, intimacy and loss"),
  movements=M(SWF),
  overview="'Transcendental Etude' is the final poem of Adrienne Rich's The Dream of a Common Language: Poems "
           "1974-1977 (W. W. Norton, 1978), and the long meditation in which the book's argument about art, "
           "women and a common language is gathered up. Its title takes the name of Liszt's piano studies and "
           "turns it against virtuosity: what the poem asks for is not transcendence or brilliance but a "
           "'composition' made of ordinary materials by a woman in a room, and its closing lines - about a whole "
           "new poetry beginning 'here' - are among the most quoted in Rich's work.",
  content="The poem begins in a landscape of hills, birches and a woman walking, and moves inward to a room and "
          "to the act of making something: it wants 'to choose a way of life' and to find a composition that has "
          "'nothing to do with eternity, / the striving for greatness, brilliance'. It thinks about the history "
          "of women, about being 'rootless, dismembered', and about the difference that knowing this makes. Its "
          "central images are a woman's hands, a piece of cloth or a quilt, and the ordinary light of a room; its "
          "later passages address a 'you' who is a lover and a listener, and it ends with the two women making "
          "'a whole new poetry beginning here' out of the materials at hand.",
  summary="'Transcendental Etude' is a long poem in loosely broken free verse paragraphs, and it is structured as "
          "a meditative walk: it begins outdoors, among birches and hills, and the walk turns into thinking, and "
          "the thinking turns into a room and an act of making. The poem's opening is a refusal of the heroic "
          "vocabulary of art - it will not strive for 'greatness, brilliance' - and it proposes instead a "
          "'composition' that has to do with a mind 'one with her body' and with 'care for the many-lived, "
          "unending / forms in which she finds herself'. From this it moves to the history of women, to the "
          "recognition that 'in fact we were always like this, / rootless, dismembered: knowing it makes the "
          "difference', and to the materials of a women's tradition: the quilt, the cloth, the hands that have "
          "made things out of what was available. The poem's last movement is domestic and precising: two women "
          "in a room, one making something, the other watching, and the poem ends by naming what they are doing "
          "as 'a whole new poetry beginning here'. The 'here' is deliberately unglamorous - a rented room, a "
          "kitchen, a table - and the poem's argument is that the beginning of a common language is a material "
          "practice rather than a revelation.",
  themes_text="The poem is about the possibility of an art made by women out of ordinary materials, and it "
              "defines that art against the masculine model of the masterpiece: not transcendence but "
              "composition, not brilliance but care. Its second subject is the history of women's dispossession - "
              "the 'rootless, dismembered' condition that the poem says it is a difference to know - and the "
              "possibility of making a tradition out of what survives. Its third is love, which the poem treats "
              "as the ground of the work: the 'you' addressed in its later sections is the lover whose presence "
              "makes the room a workshop.",
  structure="A single continuous poem in verse paragraphs of varying length, without numbered sections; its "
            "movements are a walk, a meditation, a history and a scene, connected by association and by the "
            "recurrence of a few images - the hills, the birches, the room, the hands, the cloth. It is the "
            "longest poem in the book and it is placed last, so that it functions as the book's conclusion.",
  style="Long, unrhymed, heavily enjambed lines that move at the pace of thinking; a syntax of qualification and "
        "apposition; a diction that mixes the domestic ('a piece of cloth', 'the rooms we live in') with the "
        "philosophical ('transcendence', 'composition', 'the many-lived'); quotation of the title's musical form "
        "as an irony; a closing line that turns on a single deictic, 'here'.",
  ctx="Written in the mid-1970s and collected in The Dream of a Common Language: Poems 1974-1977 (New York: W. W. "
      "Norton, 1978), the book that followed Rich's coming out and her move into the women's movement; its title "
      "alludes to Franz Liszt's Douze e\u0301tudes d'exe\u0301cution transcendante (1851), piano studies of extreme "
      "difficulty, and the poem deliberately sets the domestic and the unspectacular against them. The book is "
      "dedicated to the idea of a language women might share, and its final poem is the fullest statement of "
      "that idea.",
  sig="'Transcendental Etude' is the poem in which Rich's later poetics is most fully stated and one of the most "
      "widely anthologised American poems of the 1970s; its closing phrase, 'a whole new poetry beginning here', "
      "has become a slogan of feminist writing, and the poem is a standard text in courses on women's poetry, "
      "on the long poem and on the literature of the women's movement.",
  canon="Major canon",
  crit="Criticism has read the poem as a feminist ars poetica, as a critique of the ideology of genius, and as "
       "the culmination of the book's search for a common language; its relation to the tradition of the "
       "American long poem, from Whitman and Pound to the postwar sequences, has been discussed, as has its "
       "use of the domestic as a ground for aesthetic argument.",
  biblio="Collected as the final poem of The Dream of a Common Language: Poems 1974-1977 (New York: W. W. "
         "Norton, 1978); reprinted in Adrienne Rich's Poetry and Prose (Norton Critical Edition, 1993). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first periodical printing was not established from the sources consulted; the poem is dated from "
        "its collection in 1978, which is the date the anthology gives.",
  ver="partially verified", sources=[W_DCL, W_AR, NAAL]),
W10("Letter from Birmingham Jail", MLK, "1963", "Essay (open letter)", "major",
  genres=G("Political Essay", "Social Criticism", "Personal Essay"),
  themes=T("Race, racism and the struggle for civil rights", "Power, the state and surveillance",
           "Faith, doubt and the sacred"),
  movements=M(PAW),
  overview="The 'Letter from Birmingham Jail' is an open letter written by Martin Luther King Jr. in the city "
           "jail of Birmingham, Alabama, on 16 April 1963, in answer to a statement by eight white Alabama "
           "clergymen published as 'A Call for Unity' in the Birmingham News on 12 April. It defends the "
           "Birmingham campaign of nonviolent direct action, sets out the difference between just and unjust "
           "laws, and criticises white moderates and the white church for urging patience. It was first printed "
           "as a pamphlet by the American Friends Service Committee in May 1963 and has become one of the "
           "central documents of American political prose.",
  content="The letter opens by answering the clergymen's charge that the demonstrations are 'unwise and "
          "untimely' and that King is an outsider: he is in Birmingham, he writes, because 'injustice is "
          "anywhere ... a threat to justice everywhere'. It then sets out the four steps of a nonviolent "
          "campaign - collection of the facts, negotiation, self-purification and direct action - and explains "
          "why negotiation had failed. Its central section distinguishes just from unjust laws: 'A just law is a "
          "man-made code that squares with the moral law'; 'an unjust law is a code that is out of harmony with "
          "the moral law', and segregation is unjust because it distorts the soul and gives the segregator a "
          "false sense of superiority. From there it answers the charge of extremism by accepting the word and "
          "asking what kind of extremist one will be, criticises the white moderate who prefers 'a negative "
          "peace' to 'a positive peace', and reproaches the white church for standing at the side of the status "
          "quo. It closes with praise for the demonstrators rather than the police, and with the hope that the "
          "South will one day recognise its real heroes.",
  summary="The letter is an argument in five movements, and it is written to be read aloud. Its first movement "
          "establishes the writer's standing: King answers the charge of being an outsider by describing the "
          "network of the Southern Christian Leadership Conference and by asserting the interdependence of all "
          "communities - 'I am cognizant of the interrelatedness of all communities and states'. The second "
          "movement explains why the campaign could not wait: the four steps of nonviolent action, the broken "
          "promises of the Birmingham merchants, and the long list of the reasons why 'we must come to see ... "
          "that human progress never rolls in on wheels of inevitability'. The third and most famous movement "
          "distinguishes just from unjust laws, using Aquinas, Augustine, Buber and Tillich, and it ends with "
          "the claim that one has not only a legal but a moral responsibility to obey just laws and a moral "
          "responsibility to disobey unjust ones. The fourth answers the accusation of extremism, turning it "
          "into a question - 'will we be extremists for hate or for love?' - and delivers the letter's strongest "
          "attack on the white moderate, whose 'shallow understanding' is more frustrating than 'absolute "
          "misunderstanding'. The fifth addresses the white church and the praise of the police, and closes on "
          "the demonstrators as the South's real heroes. Throughout, the argument is carried by the resources of "
          "the sermon: the periodic sentence, the quoted authority, the example, the repetition that builds to a "
          "climax.",
  themes_text="The letter's subjects are the moral obligation to disobey unjust law, the method and theology of "
              "nonviolence, and the responsibility of the church and of the moderate. Its argument about law is "
              "the most influential thing in it: segregation is unjust not because it is inconvenient but "
              "because it denies the personhood of those it segregates, and a law that a minority had no part in "
              "making and cannot vote to change is not binding in conscience. Its second subject is time - the "
              "clergymen's 'wait' and King's answer that 'justice too long delayed is justice denied' - and its "
              "third is the relation of the American present to its founding promises, which the letter quotes "
              "against the country that made them.",
  structure="An open letter of about seven thousand words in the form of a single continuous argument with no "
            "headings, moving from the charge of outsider interference to the justification of direct action, "
            "then to the theory of law, then to the charge of extremism, then to the church, and closing with a "
            "peroration. Its paragraphs are long and rhythmically organised, and its transitions are managed by "
            "direct address ('you may well ask', 'but though I was initially disappointed') so that the reader "
            "is kept inside an argument that is also a performance.",
  style="The cadences of the Black Baptist sermon: long periodic sentences that rise through parallel clauses to "
        "a declaratory close; anaphora and repetition; quotation of Scripture, the Declaration of Independence, "
        "Aquinas, Augustine, Buber and Tillich; the rhetorical question answered by the next sentence; concrete "
        "example and anecdote set beside abstract argument; a first person that speaks for a movement as well as "
        "for a man.",
  ctx="Written on 16 April 1963 in the Birmingham city jail, where King was held after his arrest on Good Friday, "
      "12 April, for violating an injunction obtained by the city against demonstrations; he wrote the first "
      "part in the margins of a newspaper and continued on scraps of paper supplied through his lawyers, and "
      "the text was assembled by Wyatt Tee Walker and Willie Pearl Mackey. It answers 'A Call for Unity', "
      "published by eight white Alabama clergymen in the Birmingham News on 12 April 1963, which had called the "
      "protests unwise and untimely and urged negotiation in the courts. The complete letter was first published "
      "as 'Letter from Birmingham City Jail' by the American Friends Service Committee in May 1963, then in "
      "Liberation (June 1963), The Christian Century (12 June 1963) and The New Leader (24 June 1963); The "
      "Progressive printed it in July 1963 as 'Tears of Love' and The Atlantic Monthly in August 1963 as 'The "
      "Negro Is Your Brother'. King included a version in Why We Can't Wait (1964).",
  sig="The letter is the most anthologised American prose document of the civil rights movement and one of the "
      "central statements of the theory of civil disobedience in English; it was reprinted about fifty times in "
      "college readers between 1964 and 1968, it is a standard text in American literature, composition, "
      "history, law and theology courses, and its sentence 'Injustice anywhere is a threat to justice "
      "everywhere' is among the most quoted in American public speech. Its argument about just and unjust law "
      "remains the reference point for every later American debate about the relation of law to justice.",
  canon="Major canon",
  crit="Criticism has read the letter as a sermon, as a work of political theory, as an intervention in the "
       "theology of the American church and as a rhetorical performance whose power depends on its occasion; "
       "its relation to Thoreau, Gandhi, Augustine and Aquinas has been traced, and its reception - including "
       "the fact that the New York Times Magazine declined to publish it - has been studied as a case in the "
       "politics of the press. It is also a founding document in the study of American protest literature.",
  biblio="Written in the Birmingham city jail on 16 April 1963; first published in full as Letter from "
         "Birmingham City Jail (Philadelphia: American Friends Service Committee, May 1963); printed in "
         "Liberation (June 1963), The Christian Century (12 June 1963), The New Leader (24 June 1963), The "
         "Progressive (July 1963) and The Atlantic Monthly (August 1963); collected in Why We Can't Wait (New "
         "York: Harper & Row, 1964) and in Testament of Hope: The Essential Writings of Martin Luther King, Jr. "
         "(1986). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The printing history above follows Wikipedia's article on the letter, which is supported by the "
        "dealers' and archive records consulted; the sources agree on the May 1963 pamphlet, the June 1963 "
        "Liberation printing and the August 1963 Atlantic printing. Quotations are confined to the sentences for "
        "which the letter is universally known.",
  ver="partially verified", sources=[W_LBJ, W_MLK, NAAL]),
]

WORKS += [
W10("The Balloon", DB, "1966", "Short story (first-person narrative)", "major",
  genres=G("Short Story", "Postmodern Fiction", "Experimental Fiction", "Satirical Fiction"),
  themes=T("Art, the artist and the creative life", "The city, the suburb and modern space",
           "Language, writing and the limits of representation"),
  movements=M(POST, META, BLACKHUM),
  overview="'The Balloon' is a short story by Donald Barthelme first published in The New Yorker of 16 April "
           "1966 and collected in Unspeakable Practices, Unnatural Acts (Farrar, Straus and Giroux, 1968). Its "
           "narrator, an unnamed New Yorker, inflates a vast balloon over Manhattan one night; it stays for "
           "twenty-two days, the city adapts to it, critics and citizens try to interpret it, and then it is "
           "removed as casually as it arrived, having been, the narrator says, 'a spontaneous autobiographical "
           "disclosure' occasioned by a lover's absence. It is the most discussed of Barthelme's early stories "
           "and the one most often read as a statement of his poetics.",
  content="The story begins in the flat, official tone of a report: 'The balloon, beginning at a point on "
          "Fourteenth Street, the exact location of which I cannot reveal, expanded northward all one night, "
          "while people were sleeping, until it reached the Park'. The balloon's surface is 'structured' so that "
          "a landscape of valleys and knolls is presented, and children jump on it and stroll across it while "
          "adults try to read a meaning into its shifting shapes; ideas of 'bloat' and 'float' are introduced, "
          "along with concepts of dream and responsibility, and the city authorities attempt to destroy it and "
          "fail. There are traffic jams, discussions, 'a number of people' who are 'quite angry', and a general "
          "effort to decide what the balloon means. In the final paragraph the narrator meets the woman for whom "
          "the balloon was made, on her return from Norway, tells her it is a 'spontaneous autobiographical "
          "disclosure' having to do with 'the unease I felt at your absence, and with sexual deprivation', and "
          "has it removed; trailer trucks carry away the fabric, which is stored in West Virginia 'awaiting some "
          "other time of unhappiness'.",
  summary="The story's plot is minimal and its interest is in the distribution of response. The narrator makes "
          "the balloon; the city encounters it; and the encounter sorts the population into types. The children "
          "use it - they jump on it, walk across it, take it as a surface - and are entirely without "
          "interpretive anxiety. The adults cannot use it: they want it to mean, they propose readings ('bloat' "
          "and 'float', dream, responsibility), they write and talk, and their efforts are comic because the "
          "balloon's shape changes and because no reading can be confirmed. The authorities try to destroy it, "
          "which is also comic, since the balloon is not an object that can be defeated. The narrator watches "
          "all this with the detachment of a bureaucrat, and only in the last paragraph does he supply the "
          "explanation that everyone has been looking for, and the explanation is a refusal: the balloon was a "
          "private gesture, it had no meaning beyond the occasion of his lover's absence, and it is removed as "
          "soon as she returns. The story's final line - the fabric stored in West Virginia, awaiting 'some "
          "other time of unhappiness' - turns the joke into something else, since it promises that the "
          "unhappiness will recur and that the balloon is a renewable resource of the private life.",
  themes_text="'The Balloon' is a story about the reception of art, and its argument is that the artwork is what "
              "cannot be absorbed into the terms its audience brings to it: the balloon is available to the "
              "children as a surface, and to the adults only as a demand for meaning that it refuses to satisfy. "
              "Its second subject is the city itself, the 'grid of precise, rectangular pathways' against which "
              "the balloon's randomness is measured, which makes the story a fable about what escapes urban "
              "planning. Its third is the relation of a private occasion to a public object, since the "
              "narrator's grief and desire are the balloon's real content and are entirely invisible to the "
              "crowd that interprets it.",
  structure="A single continuous narrative in the present or recent past, with no scene breaks, moving from the "
            "balloon's appearance through the city's responses to the final explanation and removal. The "
            "narrative order is chronological but the proportion is inverted: most of the story is given to the "
            "public reception and only the last paragraph to the private cause, so that the explanation arrives "
            "as an afterthought and has the effect of a joke that also functions as a moral.",
  style="A flat, official, faintly bureaucratic prose that reports the fantastic as though it were an incident "
        "in a municipal report; long sentences with subordinate clauses and qualifications ('the exact location "
        "of which I cannot reveal'); abstract nouns used where a novelist would use description; a complete "
        "absence of metaphor in the narration and a positive refusal of symbolism in the ending; dialogue "
        "summarised rather than quoted.",
  ctx="Written in the mid-1960s, when Barthelme was publishing regularly in The New Yorker and was becoming the "
      "most visible of the American writers who had absorbed the examples of Kafka, Beckett, Ionesco and the "
      "French New Novel; it appeared in the issue of 16 April 1966 and was collected in Unspeakable Practices, "
      "Unnatural Acts (1968), the book that also contains 'The Indian Uprising' and 'Robert Kennedy Saved from "
      "Drowning'. It belongs to the moment at which American fiction began to absorb the examples of "
      "French theory and of the visual arts, and its balloon has been read as a response to the Minimalist and "
      "Pop objects of the New York art world.",
  sig="'The Balloon' is the most anthologised of Barthelme's stories apart from 'The School' and the standard "
      "text for his account of what a story is; it is a fixture of American short-fiction anthologies and of "
      "courses on postmodernism and metafiction, it is widely read as a parable of the reception of avant-garde "
      "art, and it is the story most often cited in the criticism that established Barthelme as the central "
      "American postmodernist of the 1960s.",
  canon="Major canon",
  crit="Critics have read the story as an ars poetica, as a satire of critical interpretation, as a meditation "
       "on the public life of artworks and as an example of Barthelme's 'non-knowing', his term for writing "
       "that proceeds without a prior meaning; its relation to Manet's balloon, to the Olympia scandal and to "
       "the New York art world of the 1960s has been proposed by critics, and its ending has been central to "
       "the argument about whether postmodern fiction can be sentimental.",
  biblio="First published in The New Yorker, 16 April 1966; collected in Unspeakable Practices, Unnatural Acts "
         "(New York: Farrar, Straus and Giroux, 1968), in Sixty Stories (New York: G. P. Putnam's Sons, 1981) "
         "and in Collected Stories (Library of America, 2021). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The periodical publication was confirmed from The New Yorker's own archive, which prints the story and "
        "gives the issue of 16 April 1966; quotations are short and confined to the passages for which the "
        "story is known.",
  ver="partially verified", sources=[W_BAL, W_DB, W_DBB, NAAL]),
W10("The School", DB, "1974", "Short story (first-person monologue)", "significant",
  genres=G("Short Story", "Postmodern Fiction", "Experimental Fiction"),
  themes=T("Death, illness and mourning", "Education, institutions and the academy",
           "Childhood, adolescence and coming of age"),
  movements=M(POST, BLACKHUM),
  overview="'The School' is a very short story by Donald Barthelme, first published in The New Yorker on 17 June "
           "1974 and collected in Amateurs (Farrar, Straus and Giroux, 1976) and in Sixty Stories (1981). It is "
           "narrated by a teacher who tells, in a single breathless monologue, how the plants, animals and "
           "people connected with his school kept dying, and how the children finally asked him where they had "
           "gone; it ends with the arrival of a new gerbil. It is Barthelme's most accessible story and one of "
           "the most widely reprinted American short stories of the postwar decades.",
  content="The narrator begins in the middle of things - 'Well, we had all these children out planting trees, "
          "see, because we figured that ... that was part of their education' - and reports a series of deaths: "
          "the trees the children planted failed; the snakes in the science room died; the herb garden died; the "
          "tropical fish died; a puppy called Edgar died; then the children's parents began to die. The children "
          "ask questions, and the teacher answers them as best he can, in the language of a liberal education - "
          "'life is like that', 'death is a part of life'. The tone of the monologue stays cheerful and "
          "reasonable, and the deaths accumulate with the logic of a joke. At the end Helen, a new gerbil, "
          "arrives in a box, and the children are delighted; the narrator says he is delighted too, and the story "
          "closes on the last of its questions and the last of its answers.",
  summary="The story is a monologue of about twelve hundred words, delivered by a teacher who is trying to give "
          "an account of a term in which everything died. Its structure is that of the escalation joke: the "
          "pattern is established with the trees ('we had all these children out planting trees'), repeated with "
          "the snakes and the herb garden, raised with the tropical fish and with Edgar the puppy, and then "
          "raised again - past the point where the joke can be contained - when the children's parents begin to "
          "die. The humour is entirely a matter of register: the narrator reports catastrophe in the mild, "
          "reasonable, slightly fatuous vocabulary of a progressive school ('we figured that ... that was part "
          "of their education', 'that was a blow', 'we were at a loss'), and the gap between the language and "
          "the events is the story. The children's questions get sharper as the deaths mount, and the teacher's "
          "answers get thinner, until the questions become metaphysical - where did they go, why, what happens "
          "to us - and the teacher can only offer the cliche\u0301s of consolation. The arrival of Helen the gerbil "
          "at the end reverses the movement without resolving it: the children are happy, the teacher says he "
          "is happy, and the story ends on the possibility that a new life can be received after all the "
          "others, which is either a consolation or the grimmest joke in the story.",
  themes_text="The story is about death, and about the inadequacy of the language in which adults explain it to "
              "children: every one of the teacher's consolations is a cliche\u0301, and the story's comedy is the "
              "comedy of watching a vocabulary fail. Its second subject is the institution - the school as a "
              "place where living things are kept, planted and buried - and its third is the children "
              "themselves, who move from curiosity to grief to a demand for meaning in the space of a page. The "
              "gerbil at the end makes the story a test case for the reader: whether the arrival of a new "
              "creature is a promise of continuation or a repetition of the pattern that has just killed "
              "everything.",
  structure="A single unbroken monologue in the first person, with no scene divisions and no narrated action "
            "outside the speaker's report; its organisation is that of the list, with each death adding a unit "
            "to the pattern and each unit slightly exceeding the last. The questions of the children are "
            "reported directly and become the story's structural markers, and the final arrival of the gerbil "
            "provides the only turn.",
  style="Colloquial, rambling, comma-spliced sentences that reproduce the hesitations of speech ('see, because "
        "we figured that ... that was part of their education'); the vocabulary of progressive education applied "
        "to catastrophe; an absence of metaphor; dialogue reported rather than dramatised; a deadpan delivery "
        "that never acknowledges the absurdity of what it is describing.",
  ctx="Published in The New Yorker of 17 June 1974, in the year in which Barthelme was teaching at the City "
      "College of New York and had published Guilty Pleasures; collected in Amateurs (New York: Farrar, Straus "
      "and Giroux, 1976) and reprinted in Sixty Stories (1981). The story belongs to the period in which "
      "Barthelme's short fiction was appearing in the magazine several times a year and in which his work was "
      "becoming the standard exhibit of American postmodernism in the classroom.",
  sig="'The School' is Barthelme's most anthologised story and one of the most widely reprinted American short "
      "stories of the last half-century; it is a standard text in introductions to the short story and to "
      "postmodern fiction, it is regularly cited in the criticism of Barthelme's comedy, and its escalation "
      "structure is taught as a model of the comic short story. George Saunders has written about it as a "
      "pattern story, and it is among the stories through which Barthelme's influence on the American short "
      "story of the 1980s and 1990s is traced.",
  canon="Secondary canon",
  crit="Critics have read the story as an escalation or pattern story, as a parable about the inadequacy of "
       "consolation, and as an instance of Barthelme's method of letting a flat voice carry an extreme "
       "situation; George Saunders's essay on Barthelme places it in a lineage of pattern stories from Chekhov "
       "and Gogol, and the story's ending - the gerbil - has been the focus of the argument about whether "
       "Barthelme's fictions are finally affirmative.",
  biblio="First published in The New Yorker, 17 June 1974; collected in Amateurs (New York: Farrar, Straus and "
         "Giroux, 1976), in Sixty Stories (1981) and in Collected Stories (Library of America, 2021). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The periodical date follows the New Yorker archive reference given in the sources consulted; the "
        "anthology's date of 1974 is the date of first publication rather than of the collection. Quotations "
        "are short and confined to the opening sentences for which the story is known.",
  ver="partially verified", sources=[W_SCH, W_DB, W_DBB, NAAL]),
]
