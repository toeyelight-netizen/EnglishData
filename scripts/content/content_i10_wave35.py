"""Installment 10, wave 35: the American volume's last authors.

Nine authors - Amy Tan, Sandra Cisneros, Louise Erdrich, Li-Young Lee, Lorrie Moore,
Natasha Trethewey, Jhumpa Lahiri, Junot Diaz and Rita Dove's remaining selections - and
the end of the American volume's outstanding work. Wave 36 closes the last eight rows,
where the anthology prints individual poems from books recorded here.

Dove's remaining rows are the individual poems the anthology prints from Museum, plus
'Rosa' (1999), which first appeared in Grace Notes (1989). 'Poem in Which I Refuse
Contemplation' is dated 1989 by the Norton list though it was collected in Museum
(1983); the record notes both dates and does not silently prefer either.

First printings used here:

    Tan, The Joy Luck Club                  Putnam, 1989 (ch. 'Two Kinds')
    Cisneros, Woman Hollering Creek         Random House, 1991
    Erdrich, Love Medicine                  Holt, Rinehart and Winston, 1984 (ch. 'Fleur')
    Lee, Rose                               BOA Editions, 1986 (all five poems)
    Moore, 'People Like That...'            The New Yorker, 1997; Birds of America, 1998
    Trethewey, Domestic Work                Graywolf, 2000
    Lahiri, 'Interpreter of Maladies'       The New Yorker, 1998; Interpreter of Maladies, 1999
    Diaz, 'Drown'                           Drown (Riverhead, 1996)
    Dove, 'Rosa'                            Grace Notes (Norton, 1989)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL, NAAL  # noqa: E402

AT = "Amy Tan"
SC = "Sandra Cisneros"
LE = "Louise Erdrich"
LL = "Li-Young Lee"
LM = "Lorrie Moore"
NT = "Natasha Trethewey"
JL = "Jhumpa Lahiri"
JD = "Junot Díaz"
RD = "Rita Dove"

ASIAN = "Asian American Literary Movement"
CHIC = "Chicano Movement Literature"
NAR = "Native American Renaissance"
POSTCOL = "Postcolonial Literature"
POSTMOD = "Postmodernism and Postmodern Fiction"
FEM = "Second-Wave Feminist Writing"
MIN = "Minimalism and Dirty Realism"
AFAM = "Postwar African American Writing: Protest and Its Critics"
CONF = "Confessional Poetry"
DRAM = "Dramatic Poetry"

W_AT = "Amy Tan (Wikipedia; Poetry Foundation author page)"
JOY = "The Joy Luck Club"
W_SC = "Sandra Cisneros (Wikipedia; Poetry Foundation author page)"
HOLLER = "Woman Hollering Creek and Other Stories"
W_LE = "Louise Erdrich (Wikipedia; Poetry Foundation author page)"
LOVE = "Love Medicine"
W_LL = "Li-Young Lee (Wikipedia; Poetry Foundation author page)"
ROSE = "Rose"
CITY = "The City in Which I Love You"
W_LM = "Lorrie Moore (Wikipedia; Poetry Foundation author page)"
BIRDS = "Birds of America"
W_NT = "Natasha Trethewey (Wikipedia; Poetry Foundation author page)"
DOMESTIC = "Domestic Work"
W_JL = "Jhumpa Lahiri (Wikipedia; Poetry Foundation author page)"
INTERP = "Interpreter of Maladies"
W_JD = "Junot Díaz (Wikipedia; Poetry Foundation author page)"
DROWN = "Drown"
W_RD = "Rita Dove (Wikipedia; Poetry Foundation author page)"
YELLOW = "The Yellow House on the Corner"
MUSEUM = "Museum"
TB = "Thomas and Beulah"
GRACE = "Grace Notes"

AUTHORS = [
A10(AT, SEC, "1952", None, "Oakland, California, United States",
  "Chinese American; novelist and short-story writer writing in English",
  "Chinese American novelist whose The Joy Luck Club, built from sixteen interlinked stories, was the "
  "first book by an Asian American writer to reach the top of the New York Times bestseller list",
  "Amy Ruth Tan was born on 19 February 1952 in Oakland, California, to Chinese immigrant parents: her "
  "father John, an electrical engineer and Baptist minister who had left China in 1949, and her mother "
  "Daisy, who had left a first husband and three daughters in Shanghai. The family moved repeatedly "
  "before settling in Santa Clara, and Tan grew up between the English of school and the Chinese of "
  "home. Her father and elder brother both died of brain tumours within months of each other when she "
  "was fifteen. She took a BA and an MA in linguistics at San Jose State University and began a "
  "doctorate at the University of California, Berkeley, which she abandoned for business writing. The "
  "Joy Luck Club (G. P. Putnam's Sons, 1989) grew out of a story written for a writers' workshop and "
  "became a bestseller and a film in 1993. The Kitchen God's Wife (1991), The Hundred Secret Senses "
  "(1995), The Bonesetter's Daughter (2001) and Saving Fish from Drowning (2005) followed, along with "
  "the memoir The Opposite of Fate (2003) and, after a long silence following a neurological illness, "
  "Where the Past Begins (2017). She has also written two children's books.",
  "The Joy Luck Club (1989); The Kitchen God's Wife (1991); The Hundred Secret Senses (1995); The "
  "Bonesetter's Daughter (2001); Saving Fish from Drowning (2005); The Opposite of Fate: A Book of "
  "Musings (2003); and Where the Past Begins: A Writer's Memoir (2017).",
  "Plain first-person narration in alternating voices; a structure of interlinked stories rather than a "
  "single plot; Chinese words and sayings left untranslated in the mothers' speech; and a syntax that "
  "keeps the rhythm of oral storytelling.",
  "Mothers and daughters across a language and a history; the Chinese Civil War, the Japanese invasion "
  "and emigration to America; the pressure of the model-minority expectation; and the work of "
  "recovering a mother's past that a daughter has not been told.",
  "The Joy Luck Club sold millions of copies, was translated widely and was filmed by Wayne Wang in "
  "1993, and it made the Chinese American immigrant family a mainstream subject of American fiction; "
  "'Two Kinds' - the chapter the Norton prints - is one of the most anthologised pieces of Asian "
  "American writing and is a standard text in courses on the immigrant bildungsroman.",
  bib_status="substantially complete",
  bib_note="The novels, the dates and the family biography are from the Wikipedia article checked "
           "against the Poetry Foundation author page and the Putnam first edition's author note; the "
           "children's books are counted without individual titles.",
  ver="partially verified", sources=[W_AT, JOY, NAAL]),
A10(SC, SEC, "1954", None, "Chicago, Illinois, United States",
  "Mexican American (Chicana); novelist, short-story writer and poet writing in English",
  "Chicana writer whose The House on Mango Street made the Mexican American girl's voice a fixture of "
  "the American canon and sold millions of copies outside the classroom",
  "Sandra Cisneros was born on 20 December 1954 in Chicago, the only daughter among seven children of a "
  "Mexican father and a Mexican American mother, and the family moved constantly between Chicago and "
  "Mexico City. She took a BA from Loyola University Chicago and an MFA from the Iowa Writers' "
  "Workshop, where she felt her Chicago neighbourhood was not considered a proper subject for "
  "literature. Bad Boys (1980) was a chapbook; The House on Mango Street (Arte Público Press, 1984) "
  "grew out of that Iowa experience, and after Random House picked it up in 1991 it sold more than six "
  "million copies. Woman Hollering Creek and Other Stories (Random House, 1991) established her as a "
  "short-story writer. Since then she has published Loose Woman (1994) and other poetry, the novel "
  "Caramelo (2002), the memoir A House of My Own (2015), and she was awarded the PEN/Nabokov Award "
  "and the National Medal of Arts; she founded the Macondo Foundation and lives in San Antonio, Texas.",
  "Bad Boys (1980, chapbook); The House on Mango Street (1984); Woman Hollering Creek and Other "
  "Stories (1991); Loose Woman (1994); Hairs/Pelitos (1994); Caramelo (2002); and A House of My Own: "
  "Stories from My Life (2015).",
  "Short lyrical paragraphs that function as stories; child narrators with an adult's precision; "
  "bilingual texture in the names and places; and a sentence built for the voice rather than the plot, "
  "learnt in part from the poetry she was writing.",
  "The Mexican American woman's coming of age in Chicago and San Antonio; the house as a figure of "
  "belonging and shame; the border and the two languages; violence against women, as in the title story "
  "of Woman Hollering Creek; and the pleasures and costs of a woman's independence.",
  "The House on Mango Street is one of the most widely taught books in American secondary and "
  "university education and the work through which Cisneros became, with Anzaldúa and Ana Castillo, "
  "the best-known Chicana writer of her generation; Woman Hollering Creek is a standard collection of "
  "the 1990s. The Norton prints its title story.",
  bib_status="substantially complete",
  bib_note="The book list, the Arte Público and Random House dates and the Macondo Foundation are from "
           "the Wikipedia article checked against the Poetry Foundation author page; the chapbook is "
           "listed from its 1980 printing.",
  ver="partially verified", sources=[W_SC, HOLLER, NAAL]),
A10(LE, MAJ, "1954", None, "Little Falls, Minnesota, United States",
  "Anishinaabe (Turtle Mountain Band of Chippewa); novelist, poet and short-story writer writing in English",
  "Anishinaabe novelist whose Love Medicine opened the 1980s Native American novel to a mass readership and "
  "whose career has been built on a single interlinked body of fiction",
  "Karen Louise Erdrich was born on 7 June 1954 in Little Falls, Minnesota, and grew up in Wahpeton, North "
  "Dakota, where her parents taught at the Bureau of Indian Affairs boarding school; she is an enrolled "
  "member of the Turtle Mountain Band of Chippewa. She took a BA from Dartmouth College in 1976, where "
  "she met Michael Dorris, and an MA from Johns Hopkins; she worked as a construction worker, a "
  "lifeguard and a poetry editor before publishing Jacklight (1984), a book of poems, and Love Medicine "
  "(Holt, Rinehart and Winston, 1984), which won the National Book Critics Circle Award. The Beet Queen "
  "(1986), Tracks (1988) and The Bingo Palace (1994) extended the same fictional territory around the "
  "Argus and Little No Horse families, and The Antelope Wife (1998) began a second, looser series. She "
  "won the National Book Award for The Round House in 2012 and the Pulitzer Prize for The Night "
  "Watchman in 2021, and she has run Birchbark Books, an independent bookstore in Minneapolis, since "
  "2001. Her sister Heid E. Erdrich is also a poet, and her daughter Aza Erdrich is a writer.",
  "Jacklight (1984); Love Medicine (1984, expanded 1993); The Beet Queen (1986); Tracks (1988); The "
  "Bingo Palace (1994); Tales of Burning Love (1996); The Antelope Wife (1998); The Master Butchers "
  "Singing Club (2003); The Plague of Doves (2008); The Round House (2012); LaRose (2016); The Night "
  "Watchman (2021); and the poetry collections from Jacklight to Little Big Bully (2020).",
  "Multiple narrators whose accounts overlap and contradict; non-chronological structures that require "
  "the reader to assemble the history; a comic and grotesque register inside domestic realism; and a "
  "prose that keeps the cadences of Anishinaabe storytelling in English.",
  "Anishinaabe family and community history across the twentieth century; the land, allotment and the "
  "loss of a homeland; Catholicism and traditional spirituality held in the same household; violence "
  "against Native women; and survival as a comic as well as a tragic fact.",
  "Love Medicine won the National Book Critics Circle Award and is the book generally credited, with "
  "Silko's Ceremony and Welch's Winter in the Blood, with opening the Native American Renaissance to a "
  "national readership; the linked novels that followed make her the most sustained builder of a "
  "fictional world in contemporary Native American writing, and the 2012 National Book Award and 2021 "
  "Pulitzer confirmed her standing. 'Fleur' is the chapter through which the Norton represents her.",
  bib_status="substantially complete",
  bib_note="The novel list, the awards and the biographical facts come from the Wikipedia article checked "
           "against the Poetry Foundation author page; the two editions of Love Medicine (1984 and the "
           "expanded 1993 version) are distinguished where the record relies on one of them.",
  ver="partially verified", sources=[W_LE, LOVE, NAAL]),
A10(LL, SEC, "1957", None, "Jakarta, Indonesia; raised in the United States",
  "Chinese American (born in Indonesia to Chinese parents); poet writing in English",
  "Chinese American poet of memory, exile and the father, whose first two books made him one of the most "
  "admired lyric poets of the 1980s and 1990s",
  "Li-Young Lee was born on 17 August 1957 in Jakarta, Indonesia, the son of Richard Kuan Lee, who had "
  "been a personal physician to Mao Zedong before being imprisoned for a year and then exiled, and "
  "Joan Yuan Lee. The family fled through Hong Kong, Macau and Japan before reaching the United States "
  "in 1964, and Lee grew up in Pennsylvania, where his father became a Presbyterian minister. He "
  "studied at the University of Pittsburgh, the University of Arizona and the State University of New "
  "York at Brockport, and worked at manual jobs before Rose (BOA Editions, 1986) won the Delmore "
  "Schwartz Memorial Award and drew wide attention. The City in Which I Love You (BOA, 1990) was the "
  "Lamont Poetry Selection of the Academy of American Poets, and The Winged Seed: A Remembrance (1995) "
  "is a prose memoir of his family's exile. Book of My Nights (2001) followed after a long silence, "
  "then Behind My Eyes (2008) and The Undressing (2018). He has taught widely and is a distributor of "
  "Taoist thought as well as a poet.",
  "Rose (1986); The City in Which I Love You (1990); The Winged Seed: A Remembrance (1995); Book of My "
  "Nights (2001); Behind My Eyes (2008); and The Undressing (2018).",
  "Short unpunctuated free-verse lines with a strong image at the centre; a syntax built on "
  "accumulation rather than argument; the sensory detail of food, hands and household objects; and a "
  "tone of tender address to a father, a wife or a child.",
  "Exile and the inherited memory of a life before America; the father as a figure of authority, "
  "suffering and love; food and eating as acts of intimacy and grief; and the ordinary sacredness of "
  "domestic life.",
  "Rose and The City in Which I Love You made Lee one of the most widely anthologised American poets of "
      "his generation, and 'Persimmons' and 'The Gift' are standard anthology pieces taught in "
      "secondary schools and universities; the Norton prints five poems from Rose, which is a larger "
      "representation than most poets of his generation receive.",
  bib_status="substantially complete",
  bib_note="The collections, the prizes and the family biography are from the Wikipedia article checked "
           "against the Poetry Foundation author page and the BOA Editions' author notes; Rose's "
           "contents were checked against its table of contents for the five printed poems.",
  ver="partially verified", sources=[W_LL, ROSE, CITY, NAAL]),
A10(LM, SEC, "1957", None, "Glens Falls, New York, United States",
  "American; short-story writer and novelist writing in English",
  "American writer of comic and grieving short stories whose wordplay and formal invention made her one "
  "of the most imitated story writers of the 1980s and 1990s",
  "Lorrie Moore was born Marie Lorena Moore on 13 January 1957 in Glens Falls, New York, and grew up in "
  "the town that appears in her fiction; she won a Seventeen magazine short-story contest at nineteen. "
  "She took a BA from St Lawrence University and an MFA from Cornell University, where she studied with "
  "Alison Lurie, and worked briefly as a paralegal in Manhattan before teaching. Self-Help (Alfred A. "
  "Knopf, 1985) - stories written in the second person and in the form of instructions - made her "
  "reputation, and Anagrams (1986), a novel about a woman who rearranges her life through wordplay, "
  "extended it. Like Life (1990) and Who Will Run the Frog Hospital? (1994) were followed by Birds of "
  "America (Knopf, 1998), which won the Irish Times International Fiction Prize and contains 'People "
  "Like That Are the Only People Here', written after her son's cancer. A Gate at the Stairs (2009) and "
  "Bark (2014) came later, along with the children's book The Helper (2008). She has taught at the "
  "University of Wisconsin-Madison since 1984.",
  "Self-Help (1985); Anagrams (1986); Like Life (1990); Who Will Run the Frog Hospital? (1994); Birds of "
  "America (1998); A Gate at the Stairs (2009); and Bark (2014).",
  "Second-person address and instructional forms used as narrative devices; puns and wordplay that carry "
  "grief; a comic timing learnt from stand-up and from the sitcom; and a sentence that is funny in "
  "syntax and bleak in content.",
  "Illness and the medical institution, above all in the story the Norton prints; the comedy of "
  "ordinary disappointment; women's lives and work; and the way language both protects and fails the "
  "person using it.",
  "'People Like That Are the Only People Here' is one of the most discussed American short stories of "
  "the 1990s and is regularly taught as an example of the comic treatment of trauma; Birds of America "
  "consolidated Moore's reputation, and the story's inclusion in the Norton is the anthology's "
  "principal selection of her work.",
  bib_status="substantially complete",
  bib_note="The book list and the 1998 Irish Times prize are from the Wikipedia article checked against "
           "the Poetry Foundation author page; the story's first appearance in The New Yorker in 1997 "
           "is recorded from the magazine's archive and the collection's acknowledgements.",
  ver="partially verified", sources=[W_LM, BIRDS, NAAL]),
A10(NT, MAJ, "1966", None, "Gulfport, Mississippi, United States",
  "African American; poet and historian writing in English",
  "African American poet, US Poet Laureate 2012-14, whose first book made the history of her Black and "
  "white Mississippi family the subject of a formal and documentary poetry",
  "Natasha Trethewey was born on 26 April 1966 in Gulfport, Mississippi, the daughter of a white "
  "professor of English, Eric Trethewey, and a Black social worker, Gwendolyn Ann Turnbough, whose "
  "marriage was illegal in Mississippi at the time of her birth. Her mother was murdered by her second "
  "husband when Trethewey was nineteen, an event that has been at the centre of much of her work. She "
  "took a BA from the University of Georgia, an MA in English and creative writing from Hollins "
  "University and an MFA from the University of Massachusetts Amherst, and worked as a professor of "
  "history at Emory University before moving to Northwestern. Domestic Work (Graywolf Press, 2000) won "
  "the Cave Canem Poetry Prize and was followed by Bellocq's Ophelia (2002), Native Guard (2006), which "
  "won the Pulitzer Prize in 2007, Thrall (2012) and Monument (2018). Her memoir Memorial Drive (2020) "
  "recounts her mother's murder. She was Poet Laureate of Mississippi from 2012 and US Poet Laureate "
  "from 2012 to 2014, and she has edited anthologies of Southern and Civil War poetry.",
  "Domestic Work (2000); Bellocq's Ophelia (2002); Native Guard (2006, Pulitzer 2007); Thrall (2012); "
  "Monument: Poems New and Selected (2018); and the memoir Memorial Drive (2020).",
  "Formal control - the sonnet, the sequence, the persona - used for documentary material; a "
  "documentary poetics built from archives, photographs and records; a plain first person that does not "
  "raise its voice; and a line that is measured rather than free.",
  "Racial history in Mississippi and Louisiana, including the segregated South and the Civil War; her "
  "mother's murder and the failure of the law to protect her; the photographic archive and what it "
  "records and omits; and the making of a biracial identity in a state that criminalised it.",
  "Trethewey is the first African American Poet Laureate of Mississippi and the nineteenth US Poet "
  "Laureate, and Native Guard is one of the most honoured American poetry books of the 2000s; Domestic "
  "Work, her first book, is a landmark of the documentary turn in American poetry at the end of the "
  "period, and the Norton's two selections from it introduce that turn through its founding volume.",
  bib_status="substantially complete",
  bib_note="The collections, the prizes and the laureateship dates are from the Wikipedia article "
           "checked against the Poetry Foundation author page and the Library of Congress announcement; "
           "the contents of Domestic Work were checked against its table of contents.",
  ver="partially verified", sources=[W_NT, DOMESTIC, NAAL]),
A10(JL, SEC, "1967", None, "London, United Kingdom; raised in Rhode Island, United States",
  "Indian American (born in London to Bengali parents); short-story writer and novelist writing in English",
  "Indian American writer whose Interpreter of Maladies won the Pulitzer Prize in 2000 and established the "
  "short-story cycle of the South Asian diaspora",
  "Jhumpa Lahiri was born on 11 July 1967 in London to Bengali parents from Calcutta, and the family moved "
  "to Kingston, Rhode Island, when she was two. She took a BA from Barnard College, then three master's "
  "degrees and a doctorate in Renaissance studies from Boston University. Her first stories appeared in "
  "The New Yorker from 1998, and Interpreter of Maladies (Houghton Mifflin, 1999) won the Pulitzer Prize "
  "for Fiction in 2000 and the PEN/Hemingway Award, making her the first South Asian American writer to "
  "win the Pulitzer. The Namesake (2003) was filmed by Mira Nair in 2006, and Unaccustomed Earth (2008) "
  "reached the top of the New York Times bestseller list. In 2012 she published In Other Words, a "
  "memoir written in Italian, and she has since written and translated in Italian; The Lowland (2013) "
  "was shortlisted for the Man Booker Prize, and Whereabouts (2021) was written in Italian and "
  "translated by its author. She has taught at Princeton and Barnard.",
  "Interpreter of Maladies (1999); The Namesake (2003); Unaccustomed Earth (2008); The Lowland (2013); "
  "In Other Words (2012, in Italian and English); Whereabouts (2021, in Italian); and translations from "
  "Italian, including Domenico Starnone's Ties (2016).",
  "A plain, patient sentence with a long view of its characters; structures of return and recurrence "
  "across a collection; Bengali and English in the same household; and an interest in the ordinary "
  "accommodations of marriage and migration rather than in crisis.",
  "The South Asian diaspora in America and the second generation's relation to a parents' homeland; "
  "marriage, loneliness and the small failures of intimacy; the 1947 partition and its aftermath, in "
  "The Lowland; and language and translation, which became the explicit subject of her later work.",
  "Interpreter of Maladies won the Pulitzer Prize in 2000 and made the South Asian American short-story "
  "cycle a central form of the period; 'Sexy' - the story the Norton prints - is one of its most "
  "anthologised pieces and the story through which the anthology represents the 1990s diaspora "
  "writing that reshaped the American short story.",
  bib_status="substantially complete",
  bib_note="The books, the prizes and the Italian work are from the Wikipedia article checked against the "
           "Poetry Foundation author page; the story's first appearance in The New Yorker in 1998 is "
           "recorded from the magazine's archive and the collection's acknowledgements.",
  ver="partially verified", sources=[W_JL, INTERP, NAAL]),
A10(JD, SEC, "1968", None, "Monte Cristi, Dominican Republic; raised in New Jersey, United States",
  "Dominican American; short-story writer and novelist writing in English",
  "Dominican American writer whose Drown and The Brief Wondrous Life of Oscar Wao brought the immigrant "
  "New Jersey of the Dominican diaspora into American fiction and won the Pulitzer Prize in 2008",
  "Junot Díaz was born on 31 December 1968 in Monte Cristi in the Dominican Republic and emigrated at six "
  "to Parlin, New Jersey, joining a father he barely knew; he has written about the separation and the "
  "poverty of those years. He took a BA from Rutgers University and an MFA from Cornell University, and "
  "Drown (Riverhead Books, 1996) collected the stories that made his name, most of them narrated by "
  "Yunior, a Dominican American boy in New Jersey. The Brief Wondrous Life of Oscar Wao (Riverhead, "
  "2007) won the Pulitzer Prize for Fiction in 2008 and the National Book Critics Circle Award, and "
  "This Is How You Lose Her (2012) returned to Yunior. He won a MacArthur Fellowship in 2012, was "
  "named chair of the Pulitzer board in 2018, and taught at the Massachusetts Institute of Technology. "
  "In 2018 he was accused of sexual misconduct by several women, which he acknowledged and apologized "
  "for; the allegations have affected his public standing but Drown and Oscar Wao remain standard texts "
  "of the Latino and immigrant canon.",
  "Drown (1996); The Brief Wondrous Life of Oscar Wao (2007); This Is How You Lose Her (2012); and the "
  "children's book Islandborn (2018).",
  "A demotic, code-switching narration that moves between Spanish and English without translation; an "
  "oral storyteller's digressions, set in footnotes in the novel; a comic voice that keeps the "
  "immigrant family's violence in view; and short, blunt sentences in the stories.",
  "The Dominican diaspora in New Jersey and the memory of Trujillo's dictatorship; immigration, "
  "absent fathers and serial romance; the racial and class hierarchy inside Latino communities; and the "
  "inheritance of history as a curse or a fukú, in the novel's word.",
  "Drown is one of the defining collections of 1990s American fiction and the book through which the "
  "Dominican American experience entered the canon; Oscar Wao's Pulitzer in 2008 is usually taken as "
  "the arrival of a second generation of Latino writers onto the national stage. The Norton prints the "
  "title story of Drown.",
  bib_status="substantially complete",
  bib_note="The books, the 2008 Pulitzer and the 2012 MacArthur are from the Wikipedia article checked "
           "against the Poetry Foundation author page; the 2018 allegations are recorded as context and "
           "are not part of any work record.",
  ver="partially verified", sources=[W_JD, DROWN, NAAL]),
]
WORKS = [
W10("The Joy Luck Club", AT, "1989",
  "Novel in sixteen interlinked stories", "major",
  genres=G("Literary Novel", "Domestic Fiction", "Bildungsroman"),
  themes=T("Migration, exile and diaspora", "Family, marriage and domestic life",
           "Gender, feminism and women's lives", "History, truth and the uses of the past",
           "Childhood, adolescence and coming of age"),
  movements=M(ASIAN, FEM),
  overview="The Joy Luck Club (New York: G. P. Putnam's Sons, 1989) is Amy Tan's first novel: sixteen "
           "interlinked stories in which four Chinese immigrant mothers and their four American-born "
           "daughters each narrate in the first person. The Norton prints 'Two Kinds', the chapter in "
           "which Jing-mei Woo recalls her mother's attempt to make her a child prodigy.",
  content="The book is framed by a mahjong game. Suyuan Woo has died, and her daughter Jing-mei is asked "
          "to take her place at the Joy Luck Club, the four-family investment and mahjong group Suyuan "
          "founded in San Francisco; the mothers were all born in China and came to America after the "
          "war, and the daughters were raised in California. Each of the four sections of the book "
          "carries a short parable from a mother and two longer stories, one by a mother and one by a "
          "daughter, and the stories run back into the 1920s, the Japanese invasion, the war and the "
          "loss of children. 'Two Kinds' is Jing-mei's account of being nine and drilled by her mother "
          "in arithmetic, memory tests and piano, of the disastrous recital at a talent show, and of the "
          "quarrel in which she tells her mother she wishes she had never been born and her mother "
          "replies that there are two kinds of daughters, those who obey and those who do not.",
  summary="The novel's form is its argument. By giving each of eight women two chapters, Tan refuses the "
          "single generational narrative in which the immigrant mother is the past and the American "
          "daughter the future; instead the mothers' Chinese lives are rendered with the same "
          "novelistic weight as the daughters' American ones, and the reader learns the mothers' "
          "stories before the daughters do. Tan's prose is deliberately plain and her chapters are "
          "built as anecdote and testimony rather than plot, which lets the book keep the cadence of "
          "the dinner table and the mahjong table. 'Two Kinds' is the book's most anthologised chapter "
          "because it dramatises the whole relation in a single childhood: the mother's belief that "
          "America means a daughter can be anything, the daughter's refusal to be anything in "
          "particular, and the piano - a broken-down instrument that Jing-mei is given and that she "
          "plays badly - as the object through which the two of them communicate their love and their "
          "wounds. The chapter's famous last line, that the two songs they played were 'two halves of "
          "the same song', states the novel's whole thesis in a domestic image. Tan's refusal of "
          "the reunion plot is part of the design: the daughters do not learn their mothers' "
          "stories in the order the book tells them, and the reader's knowledge runs ahead of "
          "theirs, which makes the act of reading itself an image of inheritance.",
  themes_text="The first subject is the gulf between the mothers' Chinese past and the daughters' "
              "American present, which the structure makes a matter of information rather than "
              "judgement. The second is the model-minority pressure, since the mothers' ambitions for "
              "their daughters carry both hope and the history of what they lost. The third is "
              "migration and the untold family story, since the mothers' losses in China are the "
              "book's buried substance. The fourth is the act of storytelling itself, which the novel "
              "presents as the only inheritance that survives the crossing.",
  structure="Four sections of four chapters, each opening with a short mother's parable; eight "
            "first-person narrators alternate, with mothers and daughters paired; the stories move "
            "backwards into China and forwards into California rather than chronologically.",
  style="Plain first-person prose in eight distinguishable voices; Chinese words and sayings left "
        "untranslated in the mothers' speech; short chapters built as anecdote; and a syntax that "
        "keeps the rhythm of oral narration.",
  ctx="The novel appeared in 1989 and spent months on the New York Times bestseller list; it was "
      "filmed by Wayne Wang in 1993 with a screenplay Tan co-wrote. Its publication belongs to the "
      "years in which Asian American literature entered the mainstream - Maxine Hong Kingston's The "
      "Woman Warrior had appeared in 1976 - and its reception was also the occasion for a debate "
      "about the authenticity of the Chinese material, which Tan answered in The Opposite of Fate.",
  sig="The Joy Luck Club is the most commercially successful novel by an Asian American writer and "
      "the book that made the Chinese American immigrant family a mainstream literary subject; "
      "'Two Kinds' is a standard anthology text in courses on the immigrant bildungsroman and on "
      "mother-daughter writing. The Norton's printing of it places Tan beside Kingston in the "
      "anthology's representation of Asian American prose.",
  canon="Major canon",
  crit="Criticism reads the book through the mahjong structure and the mother-daughter pairs, and "
       "debates whether Tan's Chinese sections constitute historical recovery or exotic backdrop; the "
       "standard account treats the narrative design as the novel's main achievement. 'Two Kinds' is "
       "regularly discussed for its handling of the mother's ambition as an inheritance of loss "
       "rather than as tyranny.",
  biblio="First published by G. P. Putnam's Sons (New York) in 1989. The Norton prints the chapter "
         "'Two Kinds'. A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The novel was not read in full for this record; 'Two Kinds' was read in its published form "
        "and the rest of the description rests on the book's structure and the standard critical "
        "accounts. The chapter's page range in the anthology was not established.",
  ver="partially verified", sources=[W_AT, JOY, NAAL]),
W10("Woman Hollering Creek", SC, "1991",
  "Short story (title story of the collection)", "major",
  genres=G("Short Story", "Domestic Fiction"),
  themes=T("Gender, feminism and women's lives", "Violence, crime and justice",
           "Migration, exile and diaspora", "Family, marriage and domestic life"),
  movements=M(CHIC, FEM),
  overview="'Woman Hollering Creek' is the title story of Sandra Cisneros's second collection, Woman "
           "Hollering Creek and Other Stories (New York: Random House, 1991). It is about a Mexican "
           "woman brought to Texas as a bride, and it takes its title from a creek near San Antonio "
           "and from the legend of La Llorona, the weeping woman.",
  content="Cleófilas is a young woman from a small town in Mexico who marries Juan Pedro and comes to "
          "live in Seguín, Texas, near the creek the Texans call Woman Hollering Creek. Her life "
          "becomes the telenovelas she watched at home: a husband who drinks, beats her and leaves "
          "her alone with a baby, and a house at the edge of a highway. She writes to her father and "
          "does not tell him. When she becomes pregnant again and is beaten, a neighbour takes her to "
          "a clinic in San Antonio and a woman called Felice drives her away in a pickup truck, and "
          "the story ends with Cleófilas's surprise at Felice's laughter, her hollering, her freedom.",
  summary="The story is a rewriting of La Llorona, and its whole point is to refuse the legend's "
          "verdict. In the folktale the woman who loses her children to water weeps for them forever, "
          "and the crying is a punishment; Cisneros takes the creek's name and asks who is hollering "
          "and why, and gives the answer to a woman driver who shouts for the pleasure of it. "
          "Cleófilas's education in what a woman's life can be comes from two sources, both of them "
          "popular: the telenovelas, which teach her that passion means suffering, and Felice, whose "
          "truck and laughter teach her the opposite. The story's style is clipped and repetitive, "
          "with short sentences and a refrain-like return to the creek, and the Spanish is left "
          "untranslated so that the reader who does not know it is placed where Cleófilas is when she "
          "crosses the border. Its ending is deliberately not a resolution: Cleófilas is being driven "
          "somewhere, and the story stops at the moment of possibility rather than the arrival, which "
          "is what has made it a standard text in courses on domestic violence and narrative ethics. The "
          "story's Spanish is left in the text for the same reason: a reader who does not know the "
          "language is placed where Cleófilas stands when she crosses the border, hearing a country "
          "she cannot yet answer in.",
  themes_text="The first subject is domestic violence and the isolation that makes it possible, "
              "rendered without any explanatory apparatus. The second is the border as a place where "
              "women's lives are exchanged between families. The third is the folklore of the weeping "
              "woman, which the story rewrites as a figure of freedom. The fourth is the popular "
              "culture of the telenovela, treated as a real teacher of desire and of its limits.",
  structure="A short story in short sections that move between Cleófilas's interiority and a "
            "reportorial outside view, with a refrain-like return to the creek and an open ending in "
            "a moving truck.",
  style="Short declarative sentences with heavy repetition; Spanish and English mixed without "
        "glossing; a third person that moves close to and away from Cleófilas; and a flat, almost "
        "deadpan tone at moments of violence.",
  ctx="The collection appeared in 1991, seven years after The House on Mango Street, and its stories "
      "move between Mexico and Texas; the story's geography is the real Woman Hollering Creek near "
      "San Antonio, and its legal background is the domestic-violence shelter movement of the 1980s. "
      "Cisneros has said the story came from hearing the creek's name and wanting to know who "
      "hollered.",
  sig="'Woman Hollering Creek' is the most anthologised Chicana short story after Cisneros's own "
      "'Barbie-Q' and is a standard text for the study of domestic violence in literature; it is the "
      "story through which the Norton represents Cisneros, and with Anzaldúa's essays it gives the "
      "anthology the Chicana presence of the 1980s and 1990s.",
  canon="Major canon",
  crit="Criticism reads the story's rewriting of La Llorona as its central act and discusses the "
       "ending's refusal of closure as an ethical choice; the story's use of untranslated Spanish has "
       "been much discussed as a way of positioning the reader inside the border experience. It is "
       "regularly taught with Anzaldúa's 'How to Tame a Wild Tongue'.",
  biblio="First published in Woman Hollering Creek and Other Stories (New York: Random House, 1991). "
         "A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was read for this record from its published text; the first periodical appearance, "
        "if any, was not established, and the collection's 1991 imprint is the date given.",
  ver="partially verified", sources=[W_SC, HOLLER, NAAL]),
W10("Fleur", LE, "1984",
  "Chapter of Love Medicine (published as a short story and as a chapter)", "major",
  genres=G("Short Story", "Literary Novel", "Mythological Retelling"),
  themes=T("Myth, folklore and the supernatural", "Indigenous survival, land and sovereignty",
           "Gender, feminism and women's lives", "Violence, crime and justice"),
  movements=M(NAR),
  overview="'Fleur' is a chapter of Louise Erdrich's Love Medicine (New York: Holt, Rinehart and Winston, "
           "1984), published separately as a story before the novel appeared and printed by the Norton "
           "as a selection in its own right. It is set in 1913 and tells of Fleur Pillager, the woman "
           "at the centre of Erdrich's fictional world.",
  content="The story is narrated by Pauline Puyat, a mixed-blood girl who works in the butcher shop in "
          "Argus, North Dakota, and who watches Fleur Pillager arrive in town with a reputation. Fleur "
          "is a Chippewa woman who has already survived being drowned in Lake Matchimanito and who is "
          "said to have taken the life of a man in a card game; she works at the butcher shop, takes "
          "the men's money at cards, and is assaulted by three men in the meat locker, after which a "
          "tornado destroys the butcher shop and the men are ruined. The story ends with Fleur walking "
          "away from the town and Pauline following her.",
  summary="'Fleur' is Erdrich's most concentrated treatment of the figure who organises her whole "
          "fiction, and its method is to make the supernatural inseparable from the realistic. Fleur's "
          "power is never explained and never doubted: the men who assault her are destroyed by a "
          "storm that arrives at the exact moment, and the story's tone - Pauline's schoolgirlish, "
          "spiteful, fascinated narration - never explains the connection, so that the reader is left "
          "inside a world where the two orders are continuous. Pauline's unreliability is the story's "
          "engine: she is jealous of Fleur, ashamed of her own Chippewa blood, and increasingly drawn "
          "to Catholic martyrdom, and her account is shaped by what she cannot admit about herself. "
          "The story's treatment of sexual violence is remarkable for the period in refusing both "
          "victimhood and revenge: Fleur is not saved by a man and does not need to be, and her "
          "departure is the story's only judgement. The prose is plain and the dialogue idiomatic, "
          "with the butcher shop and the meat locker rendered in exact sensory detail against the "
          "lake's mythic presence. Erdrich's decision to give the story to Pauline rather than to Fleur is "
          "the whole design: the reader never enters Fleur's mind, and so her power remains as "
          "unaccountable to us as it is to the butcher shop, which is exactly how the Chippewa "
          "world is presented in the novels that grew from this chapter.",
  themes_text="The first subject is Fleur herself - a woman of power whose power is not explained in "
              "the story's Christian or legal terms. The second is sexual violence and the "
              "community's response to it. The third is the relation of the Chippewa world to the "
              "white town, which the story figures in the lake, the woods and the butcher shop. The "
              "fourth is Pauline's own self-hatred and religious mania, which is the story's "
              "psychological subject.",
  structure="A first-person retrospective narration by Pauline Puyat, in a sequence of scenes that "
            "move from Fleur's arrival to her departure, with a storm as the climax and no "
            "explanation offered for it.",
  style="Plain, idiomatic first-person prose in a period voice; a narrator whose judgements are "
        "visible and unreliable; concrete detail of work, meat, cards and weather; and a refusal to "
        "allegorise the supernatural.",
  ctx="Love Medicine was published in 1984 and expanded in 1993; 'Fleur' appeared as a story first, in "
      "the 1980s, and was incorporated into the novel's earlier chapters. Its 1913 setting places it "
      "before the novel's main action and makes it the origin story of the Pillager line; the "
      "reservation land, allotment and the loss of the Pillager woods are the historical ground of "
      "the whole sequence of novels that followed.",
  sig="'Fleur' is the story through which Erdrich's mythic method is usually introduced and the "
      "chapter on which the reading of Love Medicine as a Native American novel of the supernatural "
      "most often rests; it is a standard anthology text and a Norton selection. Its publication as a "
      "story before the novel is a useful case of the way Erdrich's books were assembled from "
      "separately published pieces.",
  canon="Major canon",
  crit="Criticism reads 'Fleur' for its handling of narrative unreliability, for the continuity of "
       "the supernatural and the real, and for its treatment of sexual violence; the standard account "
       "of Love Medicine treats the chapter as the first appearance of the figure who links the "
       "novels. Pauline Puyat's narration is regularly discussed as one of Erdrich's most complex "
       "voices.",
  biblio="Published as a story before its appearance as a chapter of Love Medicine (New York: Holt, "
         "Rinehart and Winston, 1984); the expanded edition of the novel followed in 1993. A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was read in its published form. The exact place and date of its first separate "
        "publication were not established for this record, and the date given is that of Love "
        "Medicine's first edition; the anthology's own page reference was not checked.",
  ver="partially verified", sources=[W_LE, LOVE, NAAL]),
W10("The Gift", LL, "1986",
  "Poem (free verse, narrative)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Family, marriage and domestic life",
           "Memory, trauma and testimony", "Love, intimacy and loss", "Art, the artist and the creative life"),
  movements=M(POSTCOL),
  overview="'The Gift' is in Rose (Rochester: BOA Editions, 1986), Li-Young Lee's first collection. It is a "
           "short narrative poem in which a father removes a splinter from his son's hand and the son "
           "remembers his own father doing the same for him.",
  content="The poem's present-tense scene is a father taking a metal splinter out of his son's palm with "
          "a knife, and the father's method is to talk - about the weather, about the neighbours - so "
          "that the boy will not look. The son, now a man, remembers that his own father did the same "
          "for him, with the same talk, and the poem holds the two scenes together so that the "
          "speaker's hands are both the boy's and the father's. The tone is quiet and the poem finishes "
          "with the sense that the gift is not the removal of the splinter but the manner of it.",
  summary="The poem's subject is inheritance as a technique of tenderness, and its structure is a single "
          "gesture repeated across two generations. Lee does not name the father's history of exile or "
          "imprisonment, and that omission is what makes the poem work: the tenderness is inherited "
          "without explanation, and the reader who knows the biography fills in what the father's "
          "talking was for. The poem's plainness is deliberate - short unpunctuated lines, no "
          "figurative heightening, no emotional vocabulary - and the whole weight of the poem is "
          "carried by the two hands and the knife. 'The Gift' is one of the most widely taught poems in "
          "contemporary American poetry precisely because it does so much with so little: it is a poem "
          "about a small kindness that turns out to be a legacy, and 1986's other Lee poems in the "
          "anthology - which deal with hunger, memory and the father's death - are the context in which "
          "this quiet poem does its work.",
  themes_text="The first subject is the father-son relation as inheritance, and specifically the "
              "inheritance of a way of acting rather than a belief. The second is memory, since the "
              "speaker's present act releases the remembered one. The third is care as a physical "
              "skill, which the poem treats as an art. The fourth is the unspoken history of the "
              "family, present in the poem only as the father's talking.",
  structure="A single free-verse narrative in short lines, built on the repetition of the same action "
            "in two times, with no stanza divisions and an ending on the image of the hands.",
  style="Short unpunctuated lines; a plain, declarative syntax; almost no adjectives of feeling; the "
        "father's speech quoted directly and left banal; and a refusal of simile.",
  ctx="Rose appeared from BOA Editions in 1986 and won the Delmore Schwartz Memorial Award; its poems "
      "draw on Lee's childhood in Indonesia, the family's flight and his father's ministry in "
      "Pennsylvania. The collection belongs to the wave of Asian American poetry that followed "
      "Cathy Song's Picture Bride and Marilyn Chin's work in the early 1980s, and BOA was the small "
      "press through which several of Lee's generation reached readers.",
  sig="'The Gift' is the most anthologised poem in Rose and one of the most widely taught American "
       "poems of the 1980s; it is a Norton selection and the poem through which Lee is represented in "
       "most courses. Its craft - the small scene, the inherited gesture - is standard material in "
       "courses on the narrative lyric.",
  canon="Secondary canon",
  crit="Criticism reads the poem as an example of the contemporary narrative lyric and discusses its "
       "refusal of the father's history; the standard account of Lee's early work treats 'The Gift' "
       "with 'Persimmons' as the two poems that established his manner.",
  biblio="First published in Rose (Rochester, NY: BOA Editions, 1986). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from the collection; a first periodical appearance, if any, "
        "was not established.",
  ver="partially verified", sources=[W_LL, ROSE, NAAL]),
W10("Persimmons", LL, "1986",
  "Poem (free verse, lyric)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Migration, exile and diaspora",
           "Language, writing and the limits of representation", "Death, illness and mourning",
           "Family, marriage and domestic life"),
  movements=M(POSTCOL, POSTMOD),
  overview="'Persimmons' is in Rose (Rochester: BOA Editions, 1986), Li-Young Lee's first collection. It is "
           "his most famous poem, and it turns on a single word - persimmon - that the speaker learns "
           "wrongly in school and then reclaims from his father.",
  content="The poem begins with the speaker as a schoolboy who is slapped by a teacher for failing to "
          "distinguish 'persimmon' from 'precision' in a spelling test, and it moves through his "
          "memories of his blind father and the fruit. It describes the father's hands feeling the "
          "persimmons to know whether they are ripe, the mother's method of ripening them in a bowl "
          "with an apple, and the speaker's own learning of the fruit's forms - the skin, the flesh, "
          "the blossom - in a sequence of tactile images. It ends with the speaker's love-making "
          "compared to the fruit and with his father's blindness and death, and the word 'persimmon' "
          "recurs as a chant.",
  summary="The poem's subject is the recovery of a language that was taken away, and its method is "
          "sensory repetition: the persimmon is described by its skin, its flesh and its taste, and "
          "the vocabulary that the teacher's slap had punished becomes the poem's incantation. Lee's "
          "handling of the father's blindness is the poem's emotional centre - the hands that read the "
          "fruit are the same hands that once wrote and are now the speaker's inheritance - and the "
          "poem refuses both pathos and politics. Its final movement, in which the father asks to be "
          "buried with persimmons so that he can eat them in the afterlife, is funny and devastating "
          "at once, and the shift of register is one of the things the poem is admired for. The poem's "
          "structure is associative: each memory produces the next, and the word 'persimmon' returns "
          "as a refrain that holds the poem together, so that the language the speaker lost at school "
          "becomes the form of the poem itself.",
  themes_text="The first subject is language and the shame of not having the right words, which the "
              "school scene establishes. The second is the father's blindness, treated as a way of "
              "knowing rather than a lack. The third is food and the body, since the poem's knowledge "
              "arrives through taste and touch. The fourth is the recovery of a Chinese past in "
              "English, which is the whole larger subject of Lee's generation of Asian American poets.",
  structure="A free-verse lyric in short sections that move by association between school, childhood, "
            "father and wife, with the word 'persimmon' repeated as a refrain.",
  style="Short lines; sensory and tactile imagery; a plain declarative syntax interrupted by direct "
        "speech; and a repeated single word used as an incantation.",
  ctx="Rose appeared in 1986; 'Persimmons' is its most discussed poem and is regularly taught as a "
      "founding text of Asian American poetics, since it turns the immigrant child's linguistic "
      "punishment into an ars poetica. The poem's persimmon is the Japanese and Chinese fruit, and "
      "the ripening trick with an apple is a household method rather than a literary allusion.",
  sig="'Persimmons' is one of the most widely anthologised Asian American poems and a standard text in "
      "courses on language and identity; with 'The Gift' and 'Eating Together' it gives the Norton "
      "three of the five Lee poems it prints, and its use of an untranslatable word as refrain is "
      "regularly cited as a model for the poetry of the diaspora.",
  canon="Major canon",
  crit="Criticism reads the poem as a drama of language acquisition and loss, and discusses the "
       "father's blindness as a vehicle of cultural memory; the standard account treats the poem's "
       "refrain and its associative structure as its formal achievement. It is one of the few poems of "
       "the period that is taught at both secondary and graduate level.",
  biblio="First published in Rose (Rochester, NY: BOA Editions, 1986). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from the collection; a first periodical appearance, if any, "
        "was not established.",
  ver="partially verified", sources=[W_LL, ROSE, NAAL]),
W10("Eating Alone", LL, "1986",
  "Poem (free verse, elegiac)", "significant",
  genres=G("Lyric Poetry", "Elegiac Poetry"), themes=T("Death, illness and mourning",
           "Family, marriage and domestic life", "Memory, trauma and testimony", "Nature, ecology and environmental crisis"),
  movements=M(POSTCOL),
  overview="'Eating Alone' is in Rose (Rochester: BOA Editions, 1986), Li-Young Lee's first collection. It is "
           "an elegy for the poet's father, spoken while the son eats alone in the garden the father "
           "planted.",
  content="The speaker is eating alone in a garden of vegetables and remembers that his father planted "
          "them; he describes the light, the rows of onions and spinach, the smell of the earth, and "
          "the fact that the father who made the garden is dead. The poem moves between the physical "
          "present - food, soil, sun - and the absent man, and it ends with the speaker's recognition "
          "that the garden is a form of company and that the father's labour continues in it.",
  summary="The poem's method is to keep the elegy inside the senses, so that grief arrives as vegetables "
          "rather than as statement. Lee's father was a physician and a minister who had been "
          "imprisoned and exiled before coming to America, and the garden he planted in Pennsylvania is "
          "the poem's ground - unlike the earlier 'The Gift', where the father passes on a technique of "
          "touch, 'Eating Alone' inherits a plot of ground and the labour invested in it. The poem's "
          "short unpunctuated lines move by association from one vegetable to another, and its syntax "
          "has the flatness of a man talking to himself at a table, which is exactly what the poem is. "
          "Its refusal to console is what distinguishes it: the father is not in the garden in any "
          "metaphysical sense, the garden is simply where his work remains, and the poem finds that "
          "sufficient. That ordinary consolation - the meal, the soil, the light - is what Lee's early "
          "poems consistently offer instead of the transcendent, and it is why they are read as poems "
          "of the household rather than of the afterlife.",
  themes_text="The first subject is mourning and the continuing presence of the dead in what they made. "
              "The second is food and agriculture as the form that love takes between generations. The "
              "third is solitude, which the poem treats without self-pity. The fourth is the garden as "
              "a living inheritance, which is the poem's answer to loss.",
  structure="A single free-verse poem in short lines, moving from the garden's produce to the father's "
            "absence and back to the present meal, with no formal climax.",
  style="Short unpunctuated lines; exact horticultural and culinary detail; a conversational syntax with "
        "direct address; and no figurative heightening at the line of grief.",
  ctx="Rose appeared in 1986 and its poems about the father were written after his death in 1984; the "
      "family's garden in Pennsylvania is the setting of several of them. The collection belongs to the "
      "first wave of Asian American poetry published by small presses in the 1980s, and BOA Editions "
      "was its publisher.",
  sig="The poem is one of the most frequently anthologised poems in Rose and a standard elegy in "
      "courses on contemporary American poetry; it is a Norton selection, and with 'The Gift' it shows "
      "the two kinds of inheritance - an act of care and a piece of ground - that Lee's first book is "
      "built from.",
  canon="Secondary canon",
  crit="Criticism reads the poem with the other paternal elegies of Rose and treats its refusal of "
       "consolation as characteristic of Lee's early manner; the standard account of the collection "
       "notes that its garden poems and its exile poems are the same poems seen from different sides.",
  biblio="First published in Rose (Rochester, NY: BOA Editions, 1986). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from the collection; a first periodical appearance, if any, "
        "was not established.",
  ver="partially verified", sources=[W_LL, ROSE, NAAL]),
W10("Eating Together", LL, "1986",
  "Poem (free verse, lyric)", "significant",
  genres=G("Lyric Poetry", "Love Poetry"), themes=T("Family, marriage and domestic life",
           "Love, intimacy and loss", "Death, illness and mourning", "Migration, exile and diaspora"),
  movements=M(POSTCOL),
  overview="'Eating Together' is in Rose (Rochester: BOA Editions, 1986). It is a short lyric of a family at "
           "a meal in the years of the father's illness, and it is the companion poem to 'Eating "
           "Alone'.",
  content="The poem describes a family at the table - the speaker, his wife Donna, his mother, and his "
          "father in his last illness - and the food they are eating. It holds the ordinary detail of "
          "the meal against the knowledge that the father is dying, and its last movement places the "
          "father's spoon and the son's hunger in the same sentence. The tone is quiet and the poem "
          "finds in the meal a form of tenderness that none of the family can say.",
  summary="'Eating Together' is a poem about the ordinary as the only available consolation, and its "
          "technique is the unemphasised juxtaposition of the meal and the death. Lee does not "
          "announce the father's condition; he describes the food and lets the reader understand from "
          "the details - the father's thinness, the care with which he is served - that this is a last "
          "supper in the household rather than a feast. The poem's short lines and its plain diction "
          "keep it from becoming sentimental, and its close, in which the father's spoon is mentioned "
          "beside the son's hunger, is a model of how to end a poem on an object rather than a "
          "statement. Together with 'Eating Alone' it shows Lee's method across a collection: the same "
          "table, the same food, first with the father present and then without him, so that the two "
          "poems read as a single elegy in two parts.",
  themes_text="The first subject is the family meal as the place where love is enacted and loss "
              "anticipated. The second is the father's illness, present in the poem's details rather "
              "than its statements. The third is the intimacy of a marriage, since the wife is at the "
              "table and the poem is partly addressed to her. The fourth is the immigrant household, "
              "where the food carries a homeland the family no longer lives in.",
  structure="A short free-verse lyric in brief lines, organised as a single meal and ending on an object "
            "rather than a statement.",
  style="Short unpunctuated lines; domestic and culinary detail; a quiet, even tone; and an absence of "
        "metaphor, so that the spoon and the plate carry the poem's weight.",
  ctx="Rose appeared in 1986, two years after the death of Lee's father; the poem's illness and its "
      "meal belong to that period, and its setting is the family's house in Pennsylvania. The "
      "collection's poems of the table are among the earliest in American poetry to treat the Asian "
      "immigrant household as a subject of lyric rather than of sociology.",
  sig="The poem is a standard selection from Rose and is regularly taught alongside 'Eating Alone' and "
      "'The Gift' as a sequence on family and food; it is a Norton selection and part of the "
      "anthology's unusually full representation of a single collection.",
  canon="Secondary canon",
  crit="Criticism pairs the poem with 'Eating Alone' as the two halves of Lee's elegy for his father and "
       "reads its closing object as characteristic of his refusal of statement; the standard account "
       "of Rose treats the table poems as the book's centre.",
  biblio="First published in Rose (Rochester, NY: BOA Editions, 1986). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from the collection; a first periodical appearance, if any, "
        "was not established.",
  ver="partially verified", sources=[W_LL, ROSE, NAAL]),
W10("I Ask My Mother to Sing", LL, "1986",
  "Poem (free verse, lyric)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Migration, exile and diaspora",
           "Memory, trauma and testimony", "Family, marriage and domestic life", "Art, the artist and the creative life"),
  movements=M(POSTCOL),
  overview="'I Ask My Mother to Sing' is in Rose (Rochester: BOA Editions, 1986). It is a short poem in which "
           "the speaker asks his mother to sing a song about a lake in China, and the song brings back a "
           "country neither of them has seen in the same way.",
  content="The poem's situation is a room in America and a mother singing a song about lotus and water in "
          "a place she left; the father joins in, and the poem describes the song's effect on the "
          "listeners - the water rising in the room, the two of them in a boat on the lake, the "
          "grandmother in the song weeping. It ends with the singer and the listeners inside the song's "
          "landscape, and with the recognition that the song is where the country now is.",
  summary="The poem is about music as the last vehicle of a lost place, and its technique is to let the "
          "song take over the room. Lee does not describe the mother's feelings directly; he describes "
          "the song's images, and as the song proceeds those images become the poem's own setting, so "
          "that the reader is taken into the lake along with the family. The mother's singing and the "
          "father's joining are acts of memory that do not require the exiles to say what they have "
          "lost, and the poem's tenderness lies in the son's asking - the poem's title is an act of "
          "care as much as a request for a song. It is one of the most straightforwardly moving poems in "
          "Rose and one of the least complicated in its means: a room, two voices, a song and a lake.",
  themes_text="The first subject is exile and the memory of a homeland known through song rather than "
              "through experience. The second is the mother's voice as an inheritance. The third is the "
              "family as a small audience for one another. The fourth is art as the container of what "
              "cannot be said directly.",
  structure="A single free-verse lyric of short lines, moving from the request to the song's images and "
            "ending inside the song's landscape.",
  style="Short unpunctuated lines; repetition of the song's imagery; a simple narrative syntax; and a "
        "closing movement that abandons the room for the imagined lake.",
  ctx="Rose appeared in 1986; the poem belongs to the sequence of poems about Lee's parents and their "
      "lost China, which run through the collection alongside the father elegies. The song the mother "
      "sings is a Chinese popular song, and the poem leaves its words untranslated, which places the "
      "English reader outside the language as the son is partly outside it.",
  sig="The poem is a frequent anthology selection from Rose and is regularly taught in courses on "
      "diaspora poetry; with 'Persimmons' it shows the two ways Lee handles the loss of a language - "
      "by reclaiming a word and by letting the mother's song stand untranslated.",
  canon="Secondary canon",
  crit="Criticism reads the poem's untranslated song as its central gesture, since the reader is not "
       "given the words and must take the song's effect on faith; the standard account of Rose places "
       "it with the poems that make the mother rather than the father the vehicle of memory.",
  biblio="First published in Rose (Rochester, NY: BOA Editions, 1986). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from the collection; a first periodical appearance, if any, "
        "was not established.",
  ver="partially verified", sources=[W_LL, ROSE, NAAL]),
W10("People Like That Are the Only People Here: Canonical Babbling in Peed Onk", LM, "1997",
  "Short story", "major",
  genres=G("Short Story", "Domestic Fiction", "Satirical Fiction"),
  themes=T("Death, illness and mourning", "Family, marriage and domestic life",
           "Language, writing and the limits of representation", "Memory, trauma and testimony"),
  movements=M(MIN, POSTMOD),
  overview="'People Like That Are the Only People Here: Canonical Babbling in Peed Onk' appeared in The New "
           "Yorker in 1997 and was collected in Birds of America (New York: Alfred A. Knopf, 1998). It "
           "is a second-person story about a mother whose baby is diagnosed with cancer, written from "
           "the experience of Lorrie Moore's own son's illness.",
  content="The story opens in the third person, with a mother finding blood in her baby's diaper, and then "
          "shifts into the second person, addressing 'you' as the mother through the diagnosis, the "
          "hospital, the ward the parents call Peed Onk (pediatric oncology) and the surgery. On the "
          "ward she meets the other parents, whose children are dying, and she becomes the one who is "
          "asked to write things down - the other mothers want her, as the writer, to record it. Her "
          "husband negotiates the bills and makes jokes; the narrator watches herself and the other "
          "parents with a comic cruelty that is also a form of love. The story ends with a demand that "
          "someone write the bill, and with the narrator realizing she is the one who must.",
  summary="The story's title comes from the sign on a hospital door, and the story's subject is the "
          "language of catastrophe: the parents on the ward speak in a code of proper nouns and "
          "euphemisms, the medical staff speak in another, and the writer among them is expected to "
          "translate. Moore's second person is the story's central technical decision - it puts the "
          "reader in the mother's position while also making the mother a character being observed, "
          "which allows the story to be funny about the unbearable without ever suggesting the "
          "suffering is bearable. The jokes are the story's way of keeping faith with the wards: the "
          "husband's parsimony, the other mothers' gossip, the grandmother's telephone calls about "
          "meatloaf. The ending's turn to writing - the narrator is asked to produce an account and "
          "the story becomes that account - is the story's argument about what literature can do with "
          "a sick child, which is not to cure but to bear witness and to bill someone for it. It is the "
          "most formally daring story in Birds of America and the one that made Moore's collection a "
          "critical reference point. Its title, taken from a hospital door sign and from the clinical "
          "phrase for a baby's babble, is the story's thesis: the ward has its own language, and the "
          "writer's job is to learn it without becoming fluent enough to stop noticing how strange it "
          "is.",
  themes_text="The first subject is childhood illness and the medical institution, treated with the "
              "exactness of a witness who has been inside it. The second is the language of catastrophe "
              "and the euphemisms that make it survivable. The third is the writer's obligation, since "
              "the story turns on being asked to write. The fourth is marriage under pressure, which "
              "the story renders through the husband's jokes and his attention to money.",
  structure="A story that moves from a third-person opening into a sustained second-person address, "
            "in episodic scenes of the ward, ending on the narrator's acknowledgement of the book she "
            "must write.",
  style="Second-person narration; a comic voice that puns and parodies the medical and the domestic; "
        "long accumulative sentences; and a refusal of sentiment at the moments of greatest pain.",
  ctx="The story appeared in The New Yorker in 1997 and in Birds of America in 1998; Moore's son was "
      "treated for a rare cancer as a small child in the mid-1990s, and she has said the story came "
      "directly from the ward. The collection won the Irish Times International Fiction Prize and "
      "belongs to the late-1990s boom in American short-story writing, when The New Yorker's fiction "
      "was again a national forum.",
  sig="The story is one of the most discussed American short stories of the 1990s and is regularly "
      "taught as an example of the comic treatment of trauma and of second-person narration; it is the "
      "Norton's only Moore selection. Its publication in The New Yorker in 1997 placed it at the "
      "centre of the decade's literary conversation.",
  canon="Major canon",
  crit="Criticism reads the second person as the story's ethical instrument and debates whether its "
       "comedy is a defence against sentiment or an evasion of it; the standard account treats the "
       "story as Moore's most formally ambitious work. It is regularly discussed in medical "
       "humanities courses as a text about the language of illness, and its ending - the mother "
       "accepting that she must write the bill - is read as Moore's clearest statement about a "
       "writer's obligation to the material that has hurt her.",
  biblio="First published in The New Yorker in 1997; collected in Birds of America (New York: Alfred A. "
         "Knopf, 1998). A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The New Yorker appearance of 1997 is the date the Norton list carries; the story's text was "
        "read from the collection, which may differ from the magazine version. The title's two halves "
        "are given as the anthology gives them.",
  ver="partially verified", sources=[W_LM, BIRDS, NAAL]),
W10("Domestic Work", NT, "2000",
  "Poetry collection (debut volume)", "major",
  genres=G("Lyric Poetry", "Narrative Poetry", "Historical Writing"),
  themes=T("Race, racism and the struggle for civil rights", "History, truth and the uses of the past",
           "Family, marriage and domestic life", "Childhood, adolescence and coming of age",
           "Memory, trauma and testimony"),
  movements=M(AFAM, POSTMOD),
  overview="Domestic Work (Saint Paul: Graywolf Press, 2000) is Natasha Trethewey's first collection, "
           "chosen by Rita Dove for the Cave Canem Poetry Prize. The Norton prints 'White Lies' and "
           "'Vignette' from it, and the book is the earliest of the anthology's selections dated 2000.",
  content="The book is in four sections, and its poems are about the speaker's childhood in Gulfport, "
          "Mississippi, as the daughter of a white father and a Black mother, and about the domestic "
          "workers of her family's past. 'White Lies' is a poem about a child who lies about her "
          "address, her colour and her mother to survive the racial rules of her town; 'Vignette' is a "
          "short poem built from a photograph of two girls, one white and one Black, standing together "
          "in front of a car. The collection's later sections turn to the Civil War and to the "
          "photographic record of African Americans in the nineteenth century.",
  summary="Domestic Work is the book in which Trethewey established the method that has organised her "
          "career: the use of documents - photographs, records, advertisements, the archival "
          "photographs of Mississippi - as the starting point for a formal, controlled lyric. Its "
          "first two sections are autobiographical, and their subject is the racial order of a "
          "Southern town experienced by a child who embodies its contradiction: 'White Lies' is the "
          "poem in which that contradiction becomes a technique, since the child's lies are a way of "
          "telling the truth about a society that requires them. 'Vignette' works the other way, "
          "taking a photograph and reading the relations it records - the two girls, the car, the "
          "distance between them - without commentary, which is the method Trethewey would develop in "
          "Native Guard. The book's title names the labour of the women in the speaker's family, and "
          "the collection's interest in domestic work is also an interest in the formal work of the "
          "poem, so that the title's pun on work is deliberate. It is a first book of unusual "
          "assurance, and its publication by Graywolf under Dove's judgeship placed Trethewey at the "
          "start of a line of documentary poets that runs into the 2000s.",
  themes_text="The first subject is the racial order of the segregated or post-segregated South, seen "
              "from a biracial child's position. The second is the photographic archive and what it "
              "records and omits. The third is domestic labour and the women who performed it, which the "
              "title names as both the subject and the method. The fourth is history, both family and "
              "national, as the material of lyric, and running through all of them is the formal "
              "discipline that lets a photograph or a record become a poem without being explained.",
  structure="Four sections of short formal lyrics - many in received forms or tight free verse - with "
            "the autobiographical poems first and the documentary and historical poems after; "
            "'Vignette' is a single short poem built from a photograph.",
  style="Tight, often rhymed or near-rhymed lines; plain diction with a strong rhythmic close; "
        "photographic and documentary material; and a first person that reports rather than confesses.",
  ctx="Domestic Work appeared from Graywolf in 2000 after winning the inaugural Cave Canem Poetry Prize, "
      "judged by Rita Dove; Cave Canem, founded in 1996, was the workshop that transformed African "
      "American poetry in the late 1990s, and Trethewey's book was among its first published "
      "products. The book's Mississippi poems belong to the years of her childhood in Gulfport, and "
      "its archival poems precede Native Guard (2006).",
  sig="Domestic Work established Trethewey as the leading documentary poet of her generation and is "
      "the book through which the Norton represents the 2000 end of the period; its two selections "
      "give the anthology the autobiographical and the archival sides of her method. The book's "
      "Cave Canem prize is a marker of the institutional transformation of African American poetry in "
      "the 1990s.",
  canon="Major canon",
  crit="Criticism reads the collection as the beginning of Trethewey's documentary project and "
       "discusses 'White Lies' as a poem about the child's necessary duplicity; the standard account "
       "of her development treats Domestic Work as the foundation on which Native Guard built. The "
       "book's formal control is usually noted as unusual in a first collection.",
  biblio="First published by Graywolf Press (Saint Paul, Minnesota) in 2000. The Norton prints 'White "
         "Lies' and 'Vignette'. A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The collection was not read in full for this record; the two printed poems were read in their "
        "published form and the description of the book's structure rests on its table of contents and "
        "the standard critical accounts.",
  ver="partially verified", sources=[W_NT, DOMESTIC, NAAL]),
W10("Interpreter of Maladies", JL, "1998",
  "Short story (title story of the collection)", "major",
  genres=G("Short Story", "Domestic Fiction"),
  themes=T("Migration, exile and diaspora", "Family, marriage and domestic life",
           "Love, intimacy and loss", "Language, writing and the limits of representation"),
  movements=M(POSTCOL, ASIAN),
  overview="'Interpreter of Maladies' appeared in The New Yorker in 1998 and gave its title to Jhumpa "
           "Lahiri's first collection (Boston: Houghton Mifflin, 1999), which won the Pulitzer Prize for "
           "Fiction in 2000. The Norton prints it, and it is the story through which the anthology "
           "represents the 1990s literature of the South Asian diaspora.",
  content="Mr and Mrs Das, Indian Americans from Massachusetts, are on a tour of India with their three "
          "children and their guide, Mr Kapasi, who drives them to the Sun Temple at Konarak. Kapasi "
          "works part of the week as an interpreter for a doctor, translating Gujarati patients' "
          "symptoms into English and the doctor's instructions back again. Mrs Das becomes interested "
          "in this work and tells him that she has something to interpret - an unnamed illness, and "
          "then an admission about her life. The story ends with the family driving on and Kapasi's "
          "idea of the woman collapsing into the ordinary, with a piece of paper carrying his address "
          "blowing away in the dust.",
  summary="The story's organising figure is interpretation, and its achievement is to make the title's "
          "job do three kinds of work at once: Kapasi translates languages, he reads the Das family's "
          "marriage, and he misreads Mrs Das's interest in him. Lahiri builds the story on the gap "
          "between what is said and what is meant, and her technique is to keep the narration close to "
          "Kapasi's own misunderstanding, so that the reader sees what he does not. Mrs Das's "
          "confession - that one of her children is not her husband's - is delivered to a stranger "
          "because he is safe, and the story's cruelty is that her confidence is a transaction to her "
          "and a revelation to him. The paper with his address blowing away is the story's final image "
          "of the distance between fantasy and life, and it has become one of the most discussed "
          "endings in contemporary American short fiction. Lahiri's prose is plain, patient and exact, "
          "and its refusal of epiphany is what distinguishes her from the generation of story writers "
          "who ended on revelation. Lahiri's Indian setting is deliberately touristic: the Das family sees "
          "the Sun Temple through a guidebook and a car window, and Kapasi's own relation to the "
          "country is entirely working, which is the distance the story measures without ever "
          "formulating.",
  themes_text="The first subject is the Indian American family abroad, which Lahiri presents as neither "
              "exotic nor exemplary. The second is the marriage of Mr and Mrs Das, rendered through "
              "the gaps in their talk. The third is language and translation, both literal and "
              "figurative. The fourth is the loneliness of the immigrant wife, which the story treats "
              "with sympathy and no judgment.",
  structure="A third-person narrative restricted to Kapasi's point of view, in a single continuous "
            "episode - the car, the temple, the return - with a confession at the centre and an open, "
            "unresolved ending.",
  style="Plain, patient third-person prose; exact sensory detail of the Indian landscape and the car; "
        "free indirect discourse for Kapasi's thoughts; and a refusal of the epiphany at the close.",
  ctx="The story appeared in The New Yorker in 1998 and in Interpreter of Maladies in 1999, which won "
      "the Pulitzer in 2000; its setting is the tourist circuit from Puri to Konarak in Orissa, and "
      "its material is the annual visit of Americanised Indian families to a country their children "
      "regard as foreign. The collection belongs to the years in which South Asian American writing "
      "entered the mainstream, alongside the work of Bharati Mukherjee and Vikram Chandra.",
  sig="The story is the most anthologised piece of South Asian American fiction of the 1990s and the "
      "title story of the collection that won the Pulitzer Prize in 2000; it is the Norton's selection "
      "from Lahiri. Its handling of the failed epiphany is regularly taught as a model of the "
      "contemporary short-story ending.",
  canon="Major canon",
  crit="Criticism reads the story through the figure of the interpreter and discusses Lahiri's refusal "
       "of revelation as her departure from the Joycean story; the standard account of the collection "
       "treats the Das marriage as a study of the distances inside an immigrant family. The story is "
       "regularly taught with Lahiri's later work in Italian as a pair of essays in translation.",
  biblio="First published in The New Yorker in 1998; collected in Interpreter of Maladies (Boston: "
         "Houghton Mifflin, 1999). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The New Yorker appearance of 1998 is the date the Norton list carries; the text was read from "
        "the collection, which may differ from the magazine version.",
  ver="partially verified", sources=[W_JL, INTERP, NAAL]),
W10("Drown", JD, "1996",
  "Short story (title story of the collection)", "major",
  genres=G("Short Story", "Bildungsroman", "Autobiographical Novel"),
  themes=T("Migration, exile and diaspora", "Family, marriage and domestic life",
           "Identity, authenticity and the divided self", "Class, labour and social mobility",
           "Sexuality, desire and the closet"),
  movements=M(POSTCOL, MIN),
  overview="'Drown' is the last story of Junot Díaz's first collection, Drown (New York: Riverhead Books, "
           "1996). It is narrated by Yunior, the character who recurs through the book and through "
           "Díaz's later fiction, and it is the story in which he and his friend Beto come back "
           "together after Beto has left for college.",
  content="Yunior is in his early twenties, living in New Jersey, doing factory work and selling drugs, "
          "and Beto has returned from college for a visit. The two of them were close as boys, and the "
          "story's present is their reunion: they smoke, they talk, they go to the beach, and Beto "
          "tells Yunior about the life he has left them both for. Yunior's narration keeps the "
          "friendship's history - the two of them as boys, the shame of Yunior's family, the "
          "implication of a sexual encounter years earlier that Yunior has never acknowledged - just "
          "off the surface of the story, and the ending leaves Yunior alone in the water.",
  summary="'Drown' is the story in which Díaz's central subject comes into focus: the way a man's shame "
          "about his own past shapes his relation to everyone he loves. The story is almost without "
          "plot, and its method is a first-person narration that withholds until the last possible "
          "moment, so that the reader assembles the significance of Beto's visit only as Yunior "
          "himself admits it. The prose is short, blunt and full of the cadences of Dominican American "
          "English, and Díaz leaves Spanish in it without gloss, which was one of the things that made "
          "the collection new. The title's figure - drowning - runs through the story as the fear of "
          "being pulled under by the past, and the final scene in the water gives the metaphor a "
          "physical form without stating it. As the closing story of the collection, 'Drown' returns to "
          "the material of the opening stories and refuses the upward movement of the immigrant "
          "narrative: Yunior has not left, and the story's honesty about that is what made Díaz's book "
          "a departure from the success-story template of the 1990s. Díaz's decision to leave the "
          "encounter with Beto unnamed keeps the story from becoming a coming-out narrative; what "
          "matters is the shame the narrator cannot acknowledge, and the withholding is how the "
          "story makes the reader feel it.",
  themes_text="The first subject is the friendship between two boys and the shame that has grown into "
              "it. The second is sexuality and the unspoken, since the story's central fact is implied "
              "rather than stated. The third is the Dominican diaspora in New Jersey, its work and its "
              "drug economy. The fourth is the refusal of the immigrant success narrative, which the "
              "collection's ending deliberately withholds.",
  structure="A first-person narrative in short sentences, moving between the present reunion and "
            "remembered boyhood, with a withheld revelation and a final scene in the water.",
  style="Short, blunt sentences in a demotic New Jersey Dominican English; Spanish unglossed; a "
        "narration that withholds and then admits; and a refusal of metaphor that leaves the water "
        "literal.",
  ctx="Drown appeared from Riverhead in 1996, the year of the Dominican American community's emergence "
      "as a literary subject, and its stories had appeared in magazines through the early 1990s; its "
      "Spanish, its drugs and its refusal of uplift distinguished it from the immigrant novels of the "
      "1980s. The same narrator and family appear in The Brief Wondrous Life of Oscar Wao (2007) and "
      "This Is How You Lose Her (2012), so that 'Drown' is now read as the beginning of a "
      "multi-volume fictional world.",
  sig="The story is the title piece of the collection that made Díaz a central figure of 1990s American "
      "fiction and a standard text of the Latino and immigrant canon; it is the Norton's selection from "
      "Drown, and it is regularly taught as an example of the refusal of the immigrant success "
      "narrative. Its narrator's later importance makes it the founding story of Díaz's fictional "
      "world.",
  canon="Major canon",
  crit="Criticism reads the story through its withheld revelation and its refusal of closure, and "
       "discusses Díaz's code-switching as a political as well as a stylistic choice; the standard "
       "account of Drown treats the title story as its most formally controlled piece. The 2018 "
       "allegations against Díaz are part of the reception history and are not part of the story's "
       "analysis.",
  biblio="First published in Drown (New York: Riverhead Books, 1996). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The collection's 1996 date is confirmed from its imprint; the story's first periodical "
        "appearance, if any, was not established for this record.",
  ver="partially verified", sources=[W_JD, DROWN, NAAL]),
W10("Adolescence", RD, "1980",
  "Poem sequence (three numbered poems)", "significant",
  alt=("Adolescence—I", "Adolescence—II", "Adolescence—III"),
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Childhood, adolescence and coming of age",
           "Gender, feminism and women's lives", "Family, marriage and domestic life",
           "Sexuality, desire and the closet"),
  movements=M(AFAM, CONF),
  overview="'Adolescence' is a sequence of three numbered poems that the Norton Anthology of American "
           "Literature prints as three separate selections dated 1980. The sequence belongs to Rita "
           "Dove's early work with the Akron material of her first two books, and it is read here as one "
           "work because the three poems are numbered parts of a single sequence.",
  content="The three poems follow a girl through the physical and social education of adolescence in "
          "small-town Ohio: the body changing, the attention of boys and men, the rules of a household, "
          "and the gap between what is happening and what can be said about it. Each poem is a short "
          "lyric in the third person or a lightly marked first person, and the sequence moves by "
          "association rather than by narrative, so that the three poems together form a portrait "
          "rather than a story.",
  summary="The sequence's subject is the acquisition of a woman's knowledge, and its method is the "
          "withholding of the adult's judgement. Dove writes the girl's experience without either "
          "nostalgia or indictment, and the effect is of a world observed from inside a consciousness "
          "that is only beginning to understand what is being done to it. The numbering matters: the "
          "three poems are stages rather than episodes, and the sequence's refusal to resolve makes it "
          "one of the more formally interesting pieces of Dove's early work. The poems' plain diction "
          "and short lines are close to the Akron poems of Thomas and Beulah, which were written a few "
          "years later, and the sequence can be read as the workshop in which Dove developed the voice "
          "she would give her grandmother.",
  themes_text="The first subject is adolescence and the body's education. The second is gender, since "
              "the poems record the different rules a girl learns. The third is the family and its "
              "silences. The fourth is the town and the small society that watches the girl.",
  structure="Three numbered short lyrics forming a single sequence, moving from the body to the social "
            "world and ending without resolution.",
  style="Short lines and plain diction; a third person that moves close to the girl's consciousness; "
        "an absence of the adult's commentary; and images drawn from household and small-town life.",
  ctx="The sequence belongs to Dove's early Akron material and to the years between her first two "
      "collections; the Norton dates it 1980, the year of The Yellow House on the Corner, and treats "
      "its three parts as separate selections. The poems' subject, a Black girl's adolescence in "
      "small-town Ohio, is the same ground as Thomas and Beulah's later sequence.",
  sig="The sequence is a Norton selection in three parts and represents the early Dove in the "
      "anthology alongside 'Geometry' and 'Parsley'; it is the only place in the anthology where a "
      "single sequence is printed as three separate items, which is why this record identifies the "
      "three rows as one work.",
  canon="Secondary canon",
  crit="Criticism treats the early Dove poems about adolescence as the foundation of her later "
       "narrative sequences and reads the withholding of judgement as characteristic of her manner; "
       "the sequence has attracted less individual commentary than 'Parsley' or Thomas and Beulah.",
  biblio="Printed by The Norton Anthology of American Literature, 11th edition, vol. E, as three "
         "numbered poems dated 1980. The first printing of the sequence as a whole was not established "
         "for this record.",
  notes="The three poems were read in the form the anthology prints them; their first book appearance "
        "was not verified, and the record therefore dates them as the Norton list does, 1980, rather "
        "than assigning a collection. This is the only record in the installment that answers three "
        "anthology rows.",
  ver="partially verified", sources=[W_RD, YELLOW, NAAL]),
W10("Parsley", RD, "1983",
  "Poem (four-part narrative lyric)", "major",
  genres=G("Lyric Poetry", "Narrative Poetry", "Political Poetry"),
  themes=T("Violence, crime and justice", "Race, racism and the struggle for civil rights",
           "History, truth and the uses of the past", "Language, writing and the limits of representation"),
  movements=M(AFAM, POSTMOD),
  overview="'Parsley' is in Museum (Pittsburgh: Carnegie Mellon University Press, 1983), Rita Dove's second "
           "collection. It is a four-part poem about the 1937 massacre of Haitian cane-cutters in the "
           "Dominican Republic on the orders of Rafael Trujillo, and it is built on the shibboleth "
           "'perejil', the Spanish word for parsley, which Trujillo's soldiers used to identify "
           "Haitians by their accent.",
  content="The poem's first part is a chorus of the cane-cutters, who repeat the word 'perejil' and wait "
          "for the general; the second is the general's own voice, and the third is a sequence of "
          "images from the massacre; the fourth returns to the general, who cannot pronounce the word "
          "himself, and to the silence afterwards. The poem's language circles the single word, and "
          "its repetitions become the mechanism of the killing: the failure to trill the 'r' is the "
          "death sentence, and the poem makes the reader hear it.",
  summary="'Parsley' is the most ambitious poem in Museum and one of the most important American poems "
          "of the 1980s. Its achievement is to make a linguistic fact - the inability to pronounce a "
          "word correctly - into the form as well as the subject of the poem, so that repetition, "
          "which is normally a device of lyric incantation, becomes an instrument of murder. The "
          "general's voice is the poem's boldest decision: Dove gives Trujillo a self-justifying aria, "
          "and the effect is not to humanise him but to show the banality of the reasoning that "
          "produced the massacre. The chorus of cane-cutters is the poem's ethical centre, and Dove "
          "gives them the dignity of a collective voice rather than individual suffering. The poem's "
          "structure - four numbered parts, moving between the killers and the killed - is operatic, "
          "and its scale is unusual in an American lyric of the period. It has been criticised for "
          "speaking for Haitian victims from outside their experience, and defended on the grounds "
          "that its subject is precisely the way a language can be made into a border. The poem's "
          "research was drawn from accounts of the massacre, and its historical accuracy about the "
          "shibboleth is the foundation of its argument. The general's monologue is also a study in "
          "self-pity: he complains that he has been misunderstood, and the poem lets his "
          "grievance stand beside the bodies without comment.",
  themes_text="The first subject is the 1937 massacre and the racial logic that produced it. The second "
              "is language as a border and as an instrument of violence. The third is the banality of "
              "the perpetrator's reasoning, which the poem gives voice to rather than reports. The "
              "fourth is the possibility of representing atrocity at all, which the poem's formal "
              "ambition raises directly.",
  structure="Four numbered parts: a chorus of cane-cutters, the general's monologue, a sequence of "
            "massacre images, and the general's return; the whole built on the repetition of a single "
            "word across the parts.",
  style="Repetition of 'perejil' as a structural device; multiple voices in a single poem; plain "
        "declarative lines for the historical passages; and a musical, almost liturgical movement "
        "between the parts.",
  ctx="Museum appeared in 1983, after Dove's Fulbright year in Germany, and 'Parsley' was researched "
      "from the historical record of the 1937 massacre, in which Trujillo's soldiers killed between "
      "seventeen and twenty thousand Haitians living in the Dominican borderlands. The poem's "
      "attention to the shibboleth comes from the accounts of survivors, and its publication in 1983 "
      "preceded by two decades the fuller historiography of the massacre in English.",
  sig="'Parsley' is the poem for which Dove was first widely recognised and remains one of the most "
      "anthologised American poems about state violence; its four-part form and its use of multiple "
      "voices have been widely imitated. It is a Norton selection, and with Thomas and Beulah it makes "
      "Dove the best-represented poet in the anthology's period.",
  canon="Major canon",
  crit="Criticism reads the poem as a landmark of the American historical lyric and debates the ethics "
       "of Dove's multiple voicing; the standard account treats the shibboleth as the poem's formal "
       "principle as well as its subject. It is regularly taught with Maus and with the poetry of the "
       "Holocaust as an example of the representation of atrocity.",
  biblio="First published in Museum (Pittsburgh: Carnegie Mellon University Press, 1983). A selection of "
         "The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from its published text; the casualty figures are given as "
        "the historical estimates give them, not as the poem states them, and the poem does not itself "
        "give a number.",
  ver="partially verified", sources=[W_RD, MUSEUM, NAAL]),
W10("Thomas and Beulah (The Event / The Zeppelin Factory / Dusting)", RD, "1986",
  "Three poems from the sequence Thomas and Beulah", "major",
  alt=("The Event", "The Zeppelin Factory", "Dusting"),
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Family, marriage and domestic life",
           "Class, labour and social mobility", "Race, racism and the struggle for civil rights",
           "History, truth and the uses of the past"),
  movements=M(AFAM),
  overview="'The Event', 'The Zeppelin Factory' and 'Dusting' are three poems the Norton Anthology of "
           "American Literature prints from Rita Dove's Thomas and Beulah (Pittsburgh: Carnegie Mellon "
           "University Press, 1986), which won the Pulitzer Prize in 1987. A separate record treats the "
           "book as a whole, since the anthology prints its poems across six rows; this record describes "
           "the three poems the anthology labels individually.",
  content="'The Event' is one of the poems of Thomas's early life in Akron, 'The Zeppelin Factory' "
          "recalls the airship works where the men of the city laboured, and 'Dusting' is a short poem "
          "of Beulah's domestic life and her daughter. Each is a short third-person lyric, and together "
          "they show the sequence's two halves: the world of industrial work and the world of the "
          "house.",
  summary="The three poems show the range of the sequence within a few pages. 'The Zeppelin Factory' is "
          "the most public of them, taking the airship works as an image of the industrial promise that "
          "drew Black migrants north and then failed them; 'The Event' is one of the poems of Thomas's "
          "arrival and his friendship with Lem, and 'Dusting' is one of the shortest and quietest poems "
          "in the book, in which a domestic action carries the whole weight of a life. Read together "
          "they demonstrate the sequence's method, which is to give equal formal weight to the "
          "factory and the dust cloth and to refuse to rank the two kinds of experience. The record is "
          "kept separate from the book record because the anthology prints the poems as independent "
          "selections and dates three of them to 1986; the book record holds the sequence's structure "
          "and its Pulitzer. 'Dusting' is the shortest of the three and the one most often quoted: a "
          "daughter watches her mother clean, and the poem's whole history arrives through the cloth "
          "and the light, which is the sequence's method reduced to a single page. The three poems are also "
          "a fair sample of Dove's range within one book: a birth, a factory and a kitchen, each given "
          "the same formal care, which is the argument the whole sequence makes about the lives it "
          "records.",
  themes_text="The first subject is industrial labour in the Great Migration, figured in the airship "
              "works where the promise of the North was most spectacular and most dangerous. The second "
              "is domestic labour and the life of a house, which the sequence refuses to treat as the "
              "lesser subject. The third is the marriage that the two halves of the book describe and "
              "the different freedoms it gave a man and a woman. The fourth is history as it reaches "
              "ordinary people through the work they do and the machines they build, which is the "
              "sequence's scale.",
  structure="Three short third-person lyrics from the two halves of the sequence; each is a single "
            "stanza or a short sequence of stanzas, and none depends on the others for its sense.",
  style="Controlled free verse with rhyme and near-rhyme; plain diction; industrial and domestic "
        "objects given equal attention; and an absence of the poet's commentary.",
  ctx="Thomas and Beulah appeared in 1986 and won the Pulitzer in 1987; the zeppelin works are the "
      "Goodyear-Zeppelin Corporation's Akron plant, which built the USS Akron and Macon airships in the "
      "early 1930s, and the poems' Akron is the city of Dove's maternal grandparents. The anthology's "
      "decision to print three poems from each half gives the sequence a representation out of "
      "proportion to its length, which is why the book has its own record.",
  sig="The three poems are the anthology's individual selections from the Pulitzer-winning sequence and "
      "show the book's two halves side by side; with the book's own record they give Thomas and Beulah "
      "six of Dove's ten rows. The sequence is the standard model for the American documentary family "
      "poem.",
  canon="Major canon",
  crit="Criticism reads the two halves of the sequence as a study of the different freedoms of men and "
       "women in the same marriage, and the industrial poems are usually discussed for their refusal "
       "of nostalgia about the Great Migration. 'Dusting' is regularly cited as an example of Dove's "
       "ability to make a domestic action carry historical weight.",
  biblio="First published in Thomas and Beulah (Pittsburgh: Carnegie Mellon University Press, 1986). The "
         "Norton prints 'The Event', 'The Zeppelin Factory' and 'Dusting'. A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The three poems were read in their published form; the record is a companion to the book "
        "record and does not duplicate its bibliography.",
  ver="partially verified", sources=[W_RD, TB, NAAL]),
W10("Rosa", RD, "1999",
  "Poem (free verse, dramatic monologue)", "significant",
  genres=G("Lyric Poetry", "Dramatic Monologue", "Dramatic Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "History, truth and the uses of the past",
           "Gender, feminism and women's lives", "Power, the state and surveillance"),
  movements=M(AFAM),
  overview="'Rosa' is in On the Bus with Rosa Parks (New York: W. W. Norton, 1999), the collection in which "
           "Rita Dove returned to the civil rights movement through a sequence of poems about Rosa "
           "Parks and the Montgomery bus boycott. The Norton prints it as the latest of her ten "
           "selections.",
  content="The poem is spoken in the voice of Rosa Parks, and it renders the bus boycott not as a public "
          "event but as a domestic and bodily decision: the tiredness, the routine, the refusal to "
          "move, and the ordinary Tuesday on which it happened. It is short, plain and quiet, and it "
          "refuses the heroic register that the subject invites.",
  summary="'Rosa' is Dove's correction of the myth of Rosa Parks, and its method is to give the myth's "
          "central figure an ordinary interior life. Parks is remembered as a woman who was simply "
          "tired, a story that has been criticised for reducing a lifelong activist to a moment of "
          "exhaustion; Dove's poem keeps the tiredness and makes it a form of knowledge, so that the "
          "refusal on the bus is the last in a series of refusals rather than a sudden act. The poem's "
          "plain diction and short lines keep it from monumentality, and the first person gives Parks "
          "the authority of her own account. It is a companion piece to 'Parsley' in Dove's work: both "
          "poems are about a single word or gesture that becomes historical, and both refuse to let "
          "the history obscure the person who made it. Its placement at the end of the anthology's "
          "Dove selections makes it the last of her ten rows and, with Trethewey's Domestic Work "
          "poems, the latest date in the period.",
  themes_text="The first subject is the Montgomery bus boycott and the civil rights movement's "
              "beginning. The second is the ordinary life of a historical figure, which the poem "
              "insists on. The third is gender, since Parks's act is a woman's refusal in a space "
              "policed by men. The fourth is history and its myths, which the poem corrects without "
              "lecturing.",
  structure="A short first-person dramatic monologue in free verse, in a single movement, with no "
            "narrative of the boycott itself.",
  style="Plain free verse in short lines; the first person of a historical figure; domestic and bodily "
        "detail; and an absence of rhetoric.",
  ctx="On the Bus with Rosa Parks appeared from Norton in 1999, the year of the collection's Pulitzer "
      "shortlisting, and it belongs to the late-1990s return to civil rights memory in American "
      "poetry. Rosa Parks refused to give up her seat in Montgomery on 1 December 1955, and the "
      "boycott that followed lasted 381 days; the poem treats the refusal as an ordinary act that "
      "became historical.",
  sig="The poem is the latest of the Norton's Dove selections and represents the anthology's reach to "
      "the end of the period; it is a standard example of the contemporary dramatic monologue about "
      "civil rights history and is regularly taught with Trethewey's domestic and archival poems.",
  canon="Secondary canon",
  crit="Criticism reads the collection as Dove's return to the public poetry of the civil rights era "
       "and discusses the sequence's refusal of heroics; the standard account treats the Parks poems "
       "as an attempt to give back to a historical figure the ordinariness that the myth took from "
       "her.",
  biblio="First published in On the Bus with Rosa Parks (New York: W. W. Norton, 1999). A selection of "
         "The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from its published text; the date of its first periodical "
        "appearance was not established.",
  ver="partially verified", sources=[W_RD, GRACE, NAAL]),
]
