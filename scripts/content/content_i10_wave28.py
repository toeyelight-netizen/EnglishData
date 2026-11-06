"""Installment 10, wave 28: Toni Morrison, John Updike, Philip Roth, Philip K. Dick,
Ursula K. Le Guin and Octavia E. Butler.

Six new authors and six works, one record per Norton selection, in the
American anthology's order after Plath. Each author's single in-scope
selection is the whole of that author's Norton presence in the period.

First printings settled here:

    Toni Morrison, "The Nobel Lecture in Literature"   lectured 7 Dec 1993;
        book: Knopf, 1994
    John Updike, "New York Girl"                       The New Yorker, 1 Apr 1996;
        collected in Licks of Love (2000)
    Philip Roth, "The Conversion of the Jews"          The Paris Review 18 (Spring 1958);
        collected in Goodbye, Columbus (1959)
    Philip K. Dick, "Precious Artifact"                Galaxy Magazine, October 1964
    Ursula K. Le Guin, "Schrodinger's Cat"             Universe 5 (1974), ed. Terry Carr
    Octavia E. Butler, "Bloodchild"                    Asimov's SF Magazine, June 1984
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

TM = "Toni Morrison"
JU = "John Updike"
PR = "Philip Roth"
PKD = "Philip K. Dick"
UKL = "Ursula K. Le Guin"
OEB = "Octavia E. Butler"

JAF = "Jewish American Fiction"
AAW = "Postwar African American Writing: Protest and Its Critics"
PM = "Postmodernism and Postmodern Fiction"
MR = "Magical Realism in English"
NWSF = "New Wave Science Fiction"
FSF = "Feminist Science Fiction"
SWF = "Second-Wave Feminist Writing"

W_TM = "Toni Morrison (Wikipedia)"
W_NOBEL = "The Nobel Lecture in Literature, 1993, first edition (Alfred A. Knopf, 1994)"
W_NOBELPRIZE = "Nobel Prize in Literature 1993, award announcement and lecture (NobelPrize.org)"
W_JU = "John Updike (Wikipedia)"
W_NYG = "New York Girl, The New Yorker, 1 April 1996 (newyorker.com archive)"
W_LICKS = "Licks of Love: Short Stories and a Sequel, contents (library catalogue record)"
W_PR = "Philip Roth (Wikipedia)"
W_GC = "Goodbye, Columbus (Wikipedia)"
W_PF_CJ = "The Conversion of the Jews (Poetry Foundation and Paris Review archive references)"
W_PKD = "Philip K. Dick (Wikipedia)"
W_PKDB = "Philip K. Dick bibliography (Wikipedia)"
W_FMI = "The FictionMags Index (Phil Stephenson-Payne), Philip K. Dick story entries"
W_UKL = "Ursula K. Le Guin (Wikipedia)"
W_U5 = "Universe 5 (1974), ed. Terry Carr, contents and copyright page"
W_OEB = "Octavia E. Butler (Wikipedia)"
W_BC = "Bloodchild and Other Stories, first edition (Seven Stories Press, 1995)"

AUTHORS = [
A10(TM, MAJ, "1931", "2019", "Lorain, Ohio, United States",
  "American; novelist, essayist and editor writing in English",
  "American novelist and the first Black woman to receive the Nobel Prize in Literature (1993), whose "
  "eleven novels remade the language of American historical memory and whose editorship at Random House "
  "brought Black American writing into the mainstream of trade publishing",
  "Toni Morrison was born Chloe Ardelia Wofford in Lorain, Ohio, on 18 February 1931, the second of four "
  "children of a working-class Black family; she took the name Toni at Howard University, where she "
  "graduated in English in 1953, and took an MA in American literature at Cornell in 1955 with a thesis "
  "on William Faulkner and Virginia Woolf. She taught at Texas Southern University and at Howard, where "
  "she met and married the architect Harold Morrison; the marriage ended in 1964, and she moved with her "
  "two sons to Syracuse to work as an editor at Random House, where in the late 1960s she became the "
  "first Black woman senior editor in the company's fiction department and published Gayl Jones, Toni "
  "Cade Bambara, Angela Davis and Muhammad Ali. Her first novel, The Bluest Eye (1970), was written in "
  "the early mornings around her editorial work; it was followed by Sula (1973), Song of Solomon (1977), "
  "which won the National Book Critics Circle Award, Tar Baby (1981) and Beloved (1987), which won the "
  "Pulitzer Prize for Fiction in 1988 and was adapted for film in 1998. She taught at Princeton from "
  "1989 to 2006, held the Robert F. Goheen chair, and wrote Jazz (1992), Paradise (1997), Love (2003), A "
  "Mercy (2008) and God Help the Child (2015), as well as Playing in the Dark (1992), The Nobel Lecture "
  "in Literature (1994) and the libretto for Richard Danielpour's Margaret Garner (2005). She was "
  "awarded the Nobel Prize in Literature in 1993, the first Black woman to receive it, and the "
  "Presidential Medal of Freedom in 2012. She died at Montefiore Medical Center in the Bronx on 5 "
  "August 2019.",
  "Novels: The Bluest Eye (1970), Sula (1973), Song of Solomon (1977), Tar Baby (1981), Beloved (1987), "
  "Jazz (1992), Paradise (1997), Love (2003), A Mercy (2008) and God Help the Child (2015). Other prose: "
  "Playing in the Dark: Whiteness and the Literary Imagination (1992), The Nobel Lecture in Literature, "
  "1993 (1994), What Moves at the Margin: Selected Nonfiction (2008) and The Origin of Others (2017). "
  "Children's books, with Slade Morrison: The Big Box (1999), The Book of Mean People (2002) and Peeny "
  "Butter Fudge (2003). Drama and libretto: Dreaming Emmett (1986) and Margaret Garner (2005).",
  "A prose of long, cadenced sentences that move between the vernacular and the biblical; a narrative "
  "that withholds its central event and circles it from several voices; the repeated image that returns "
  "with a changed meaning; an interior monologue in which memory and present action are not separated; "
  "and a refusal of the explanatory paragraph, so that the reader must assemble the history the novel "
  "is about.",
  "Slavery and its afterlife in American memory; the construction of race and of whiteness; the "
  "mother-child bond under conditions of ownership; the Black community as a source of both shelter and "
  "judgement; language as the medium in which the dead and the living speak to one another; music, "
  "especially jazz and the blues, as a model of form; and the ethics of remembering what a nation would "
  "rather forget.",
  "Morrison is the central American novelist of the last half-century and the one whose work redefined "
  "what the American historical novel could do with the enslaved and the dispossessed. Beloved is "
  "routinely placed among the finest American novels of the century, the Nobel Prize of 1993 made her "
  "the first Black woman to hold it, and her essays on whiteness and on the Africanist presence in "
  "American literature have changed the teaching of the subject. Her influence on the generation of "
  "Black American writers after 1980 is acknowledged on every side.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Morrison, which agrees with the "
           "publisher's and prize records consulted; they were not checked against a printed "
           "bibliography. Installment 10 records one Norton selection - the Nobel lecture of 1993 - so "
           "the eleven novels, the essays, the children's books and the libretto have no records, and "
           "the bibliography is incomplete.",
  ver="partially verified", sources=[W_TM, W_NOBEL, NAAL]),
A10(JU, MAJ, "1932", "2009", "Reading, Pennsylvania, United States",
  "American; novelist, short-story writer, poet, essayist and critic writing in English",
  "American novelist and man of letters, the most prolific and technically accomplished of the postwar "
  "American realists, whose Rabbit tetralogy, Couples and the stories of ordinary Protestant middle life "
  "made him the chronicler of the American suburbs and twice won him the Pulitzer Prize",
  "John Hoyer Updike was born in Reading, Pennsylvania, on 18 March 1932 and grew up in the small town "
  "of Shillington, the only child of a schoolteacher father and a mother who wrote and painted; the "
  "town became the Olinger of his early fiction. He was a brilliant student, edited the Harvard Lampoon, "
  "graduated summa cum laude in 1954, and spent a year at the Ruskin School of Drawing in Oxford before "
  "joining the staff of The New Yorker in 1955, where he wrote the Talk of the Town column and began "
  "publishing the stories and poems that made his name. He left the magazine in 1957 for Ipswich, "
  "Massachusetts, where he lived for the rest of his life and wrote, on average, a book a year. The "
  "Poorhouse Fair (1959) and Rabbit, Run (1960) were followed by The Centaur (1963, National Book "
  "Award), Of the Farm (1965), Couples (1968), Rabbit Redux (1971), A Month of Sundays (1975), The Coup "
  "(1978), Rabbit Is Rich (1981, Pulitzer Prize), The Witches of Eastwick (1984), Roger's Version "
  "(1986), Rabbit at Rest (1990, Pulitzer Prize), Memories of the Ford Administration (1992), Brazil "
  "(1994), In the Beauty of the Lilies (1996), Toward the End of Time (1997), Gertrude and Claudius "
  "(2000), Seek My Face (2002), Villages (2004), Terrorist (2006) and The Widows of Eastwick (2008); "
  "the stories were collected in The Same Door (1959), Pigeon Feathers (1962), The Music School (1966), "
  "Bech: A Book (1970), Problems (1979), Too Far to Go (1979), Bech Is Back (1982), Trust Me (1987), "
  "The Afterlife (1994), Bech at Bay (1998), Licks of Love (2000), The Early Stories 1953-1975 (2003) "
  "and My Father's Tears (2009). He was a prolific critic and reviewer for The New Yorker and The New "
  "York Review of Books, wrote the memoir Self-Consciousness (1989), and died at Danvers, Massachusetts, "
  "on 27 January 2009.",
  "Novels: The Poorhouse Fair (1959), Rabbit, Run (1960), The Centaur (1963), Of the Farm (1965), "
  "Couples (1968), Rabbit Redux (1971), A Month of Sundays (1975), Marry Me (1976), The Coup (1978), "
  "Rabbit Is Rich (1981), The Witches of Eastwick (1984), Roger's Version (1986), S. (1988), Rabbit at "
  "Rest (1990), Memories of the Ford Administration (1992), Brazil (1994), In the Beauty of the Lilies "
  "(1996), Toward the End of Time (1997), Gertrude and Claudius (2000), Seek My Face (2002), Villages "
  "(2004), Terrorist (2006) and The Widows of Eastwick (2008). Stories: The Same Door (1959), Pigeon "
  "Feathers (1962), The Music School (1966), Museums and Women (1972), Problems (1979), Trust Me "
  "(1987), The Afterlife (1994), Licks of Love (2000), The Early Stories 1953-1975 (2003) and My "
  "Father's Tears (2009). Poetry, criticism and memoir: The Carpentered Hen (1958), Assorted Prose "
  "(1965), Picked-Up Pieces (1975), Hugging the Shore (1983), Self-Consciousness (1989) and Odd Jobs "
  "(1991).",
  "A precise, sensory prose that gives equal weight to the surface of things and to what they conceal; "
  "the present tense used for immediacy, and the long retrospective paragraph for judgement; a narrator "
  "who is at once inside a character's consciousness and above it, commenting; a vocabulary drawn from "
  "theology, science and the consumer goods of the American century; and a habit of ending a story on a "
  "small, unresolved gesture rather than a revelation.",
  "Sexual desire and its consequences in marriage and the suburb; the residue of Calvinism and of "
  "Protestant small-town life in the American present; mortality, ageing and the body's decline; the "
  "ordinary American century - the Depression, the war, the postwar boom, the 1960s - as it is lived by "
  "unremarkable people; the relation of art and faith; and the moral weight of the trivial.",
  "Updike is the most decorated American novelist of his generation - two Pulitzer Prizes, two National "
  "Book Awards, three National Book Critics Circle Awards - and the standard chronicler in fiction of "
  "the American suburb and of the Protestant middle class in the second half of the twentieth century. "
  "The Rabbit novels are a continuous social history of the United States from 1959 to 1989, and his "
  "short stories are a standing exhibit in the teaching of the form; his critical essays on American and "
  "European writing are a substantial part of his reputation.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Updike, with the contents of "
           "Licks of Love taken from a library catalogue record of the Knopf first edition; they were "
           "not checked against a printed bibliography. Installment 10 records one Norton selection - "
           "'New York Girl' - so the twenty-four novels, the poems, the criticism and the other stories "
           "have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_JU, W_NYG, W_LICKS, NAAL]),
A10(PR, MAJ, "1933", "2018", "Newark, New Jersey, United States",
  "American; novelist, short-story writer and essayist writing in English",
  "American novelist whose Goodbye, Columbus, Portnoy's Complaint and the Zuckerman and Roth books made "
  "the American Jewish family and the American male ego the matter of a fifty-year comic and "
  "self-lacerating project",
  "Philip Milton Roth was born in Newark, New Jersey, on 19 March 1933, the second son of first-"
  "generation American parents of Galician Jewish descent; the Weequahic neighbourhood in which he grew "
  "up became the setting of his first book and of much of his later work. He graduated from Bucknell "
  "University in 1954 and took an MA in English at the University of Chicago in 1955, then taught "
  "writing at Chicago, Iowa and Princeton while publishing stories in The Paris Review, The New Yorker "
  "and Commentary. Goodbye, Columbus (1959), a novella and five stories, won the National Book Award in "
  "1960 and made him, at twenty-six, a controversial figure in the American Jewish community. Letting Go "
  "(1962), When She Was Good (1967) and Portnoy's Complaint (1969) followed; the last made him a "
  "celebrity and remains one of the most discussed American novels of the period. From the 1970s he "
  "wrote the sequence of books narrated by his alter ego Nathan Zuckerman - The Ghost Writer (1979), "
  "Zuckerman Unbound (1981), The Anatomy Lesson (1983), The Prague Orgy (1985), The Counterlife (1986), "
  "American Pastoral (1997, Pulitzer Prize), I Married a Communist (1998) and The Human Stain (2000) - "
  "as well as The Breast (1972), My Life as a Man (1974), Sabbath's Theater (1995, National Book Award), "
  "The Dying Animal (2001), The Plot Against America (2004), Everyman (2006), Indignation (2008), The "
  "Humbling (2009) and Nemesis (2010). He edited the eight-volume complete edition of his own work for "
  "the Library of America, published in the last years of his life, and died in New York on 22 May "
  "2018; he is buried in the Mount Zion cemetery in Queens.",
  "Fiction: Goodbye, Columbus (1959), Letting Go (1962), When She Was Good (1967), Portnoy's Complaint "
  "(1969), Our Gang (1971), The Breast (1972), The Great American Novel (1973), My Life as a Man "
  "(1974), The Ghost Writer (1979), Zuckerman Unbound (1981), The Anatomy Lesson (1983), The Prague "
  "Orgy (1985), The Counterlife (1986), Deception (1990), Operation Shylock (1993), Sabbath's Theater "
  "(1995), American Pastoral (1997), I Married a Communist (1998), The Human Stain (2000), The Dying "
  "Animal (2001), The Plot Against America (2004), Everyman (2006), Indignation (2008), The Humbling "
  "(2009) and Nemesis (2010). Nonfiction: Reading Myself and Others (1975), The Facts (1988), Patrimony "
  "(1991) and Why Write? (2017).",
  "A first-person voice of enormous comic energy that turns on itself, exaggerating its own grievance "
  "until the complaint becomes a critique; dialogue recorded with an ear for the exact cliché of its "
  "speaker; a narrative that offers several incompatible explanations for the same event and declines "
  "to choose; and an insistence on the body, its appetites and humiliations, as the ground of the moral "
  "life.",
  "The American Jewish family as the crucible of assimilation and guilt; the sexual life of the "
  "American male and its entanglement with vanity and shame; the difference between the story one tells "
  "about oneself and the life one has led; Newark and the American city in decline; the political "
  "history of the American century, from the Second World War to the Bush years; and the question of "
  "what a novelist does with a life that is his own.",
  "Roth is the most awarded American novelist of his generation and, in the judgement of the Library of "
  "America, one of the four or five whose work is printed in a complete authorised edition during his "
  "lifetime. Goodbye, Columbus is still the standard American story of the child who takes his father's "
  "religion more seriously than the adults, and the Zuckerman books and American Pastoral are among the "
  "most discussed American novels of the last half-century; his influence on the American autobiographical "
  "novel after 1980 is impossible to overstate.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Roth and on Goodbye, Columbus, "
           "which give the first printing of 'The Conversion of the Jews' in The Paris Review 18 (Spring "
           "1958); they were not checked against a printed bibliography. Installment 10 records one "
           "Norton selection - 'The Conversion of the Jews' - so the thirty-one books and the essays "
           "have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_PR, W_GC, W_PF_CJ, NAAL]),
A10(PKD, MAJ, "1928", "1982", "Chicago, Illinois, United States",
  "American; novelist and short-story writer writing in English",
  "American science-fiction writer whose novels of unstable reality, simulacra and bureaucratic "
  "theocracy - The Man in the High Castle, Do Androids Dream of Electric Sheep?, Ubik - moved science "
  "fiction into the literary mainstream and into the Library of America",
  "Philip Kindred Dick was born in Chicago on 16 December 1928, twin to a sister who died six weeks "
  "later, and grew up in Berkeley, California, where his family moved after his parents separated. He "
  "attended Berkeley High School and the University of California at Berkeley for a year, worked in a "
  "record shop and as a radio announcer, and from 1952 published science fiction at a rate that made "
  "him, by the end of the decade, one of the most prolific writers in the field: forty-five novels and "
  "one hundred and twenty-one short stories. Solar Lottery (1955) was his first novel; Eye in the Sky "
  "(1957), Time Out of Joint (1959), The Man in the High Castle (1962, Hugo Award), Martian Time-Slip "
  "(1964), The Three Stigmata of Palmer Eldritch (1965), Do Androids Dream of Electric Sheep? (1968, "
  "the source of Blade Runner), Ubik (1969), Flow My Tears, the Policeman Said (1974) and A Scanner "
  "Darkly (1977) followed. From 1974 he experienced the series of visions and voices he called "
  "2-3-74, which he explored in the exegesis published posthumously as The Exegesis of Philip K. Dick "
  "(2011) and which informs VALIS (1981), The Divine Invasion (1982) and The Transmigration of Timothy "
  "Archer (1982). He died of a stroke in Santa Ana, California, on 2 March 1982, weeks before the "
  "release of Blade Runner; the Library of America issued three volumes of his novels between 2007 and "
  "2009, the first science fiction the series had admitted.",
  "Novels: Solar Lottery (1955), Eye in the Sky (1957), The Cosmic Puppets (1957), Time Out of Joint "
  "(1959), Dr. Futurity (1960), Vulcan's Hammer (1960), The Man in the High Castle (1962), The Game-"
  "Players of Titan (1963), Martian Time-Slip (1964), The Three Stigmata of Palmer Eldritch (1965), "
  "Dr. Bloodmoney (1965), Now Wait for Last Year (1966), Counter-Clock World (1967), Do Androids Dream "
  "of Electric Sheep? (1968), Ubik (1969), A Maze of Death (1970), Flow My Tears, the Policeman Said "
  "(1974), A Scanner Darkly (1977), VALIS (1981), The Divine Invasion (1982) and The Transmigration of "
  "Timothy Archer (1982). Stories: A Handful of Darkness (1955), The Variable Man (1957), The Preserving "
  "Machine (1969), The Golden Man (1980), We Can Remember It for You Wholesale (1990) and the five-"
  "volume Collected Stories (1987). Nonfiction: The Shifting Realities of Philip K. Dick (1995) and The "
  "Exegesis of Philip K. Dick (2011).",
  "A plain, hurried, colloquial prose that reports metaphysical catastrophe in the tone of a man "
  "describing a bad day at work; dialogue full of the slang and the commercial jargon of the American "
  "1960s and 1970s; plots that turn on a single ontological doubt - is this world the real one, and is "
  "this self the one that woke up; a cast of small-time entrepreneurs, repairmen, police and addicts; "
  "and an ending that refuses the consolation of a solved mystery.",
  "The instability of the perceived world and the possibility that reality is a fabrication or a "
  "simulation; the human and the machine, and the point at which a person can no longer tell them "
  "apart; entropy, decay and the second law as a moral fact; the theodicy question, asked through "
  "cults, gurus and false messiahs; surveillance, bureaucracy and the police state; and addiction, "
  "which he wrote about from the inside.",
  "Dick is the most influential science-fiction writer of the postwar period after Asimov and Le Guin, "
  "and the one whose work has most thoroughly crossed into the literary canon: the Library of America "
  "admitted him in 2007, and the films adapted from his novels and stories - Blade Runner, Total "
  "Recall, Minority Report, A Scanner Darkly, The Adjustment Bureau - have made his premises part of "
  "the common intellectual furniture of the present. His influence on cyberpunk and on the literary "
  "novel of the 2000s is acknowledged by writers as different as William Gibson and Jonathan Lethem.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's bibliography of Dick and from the "
           "FictionMags Index, which give 'Precious Artifact' in Galaxy Magazine for October 1964 and "
           "its collection in We Can Remember It for You Wholesale (1990); they were not checked "
           "against a printed bibliography. Installment 10 records one Norton selection - 'Precious "
           "Artifact' - so the forty-five novels and the other hundred and twenty stories have no "
           "records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_PKD, W_PKDB, W_FMI, NAAL]),
A10(UKL, MAJ, "1929", "2018", "Berkeley, California, United States",
  "American; novelist, short-story writer, poet and essayist writing in English",
  "American writer of speculative fiction and the most decorated author in the field, whose Earthsea "
  "books, The Left Hand of Darkness and The Dispossessed made anthropology, gender and anarchist "
  "politics the matter of science fiction and brought it into the American literary canon",
  "Ursula Kroeber Le Guin was born in Berkeley, California, on 21 October 1929, the daughter of the "
  "anthropologist Alfred Kroeber and the writer Theodora Kroeber, and grew up among the anthropologists "
  "and Native American informants who visited her parents' house - an education she later called the "
  "source of her interest in invented cultures. She took a BA at Radcliffe in 1951, an MA at Columbia "
  "in 1952 with a thesis on the French poet Pierre de Ronsard, and a Fulbright to Paris, where she met "
  "the historian Charles Le Guin; they married in 1953 and settled in Portland, Oregon, where she "
  "taught French at Portland State University and wrote in the early mornings. Rocannon's World (1966) "
  "began the Hainish sequence; A Wizard of Earthsea (1968), The Tombs of Atuan (1970) and The Farthest "
  "Shore (1972) made the Earthsea archipelago one of the founding landscapes of modern fantasy; The "
  "Left Hand of Darkness (1969) won both the Hugo and the Nebula and is the novel through which the "
  "field thinks about gender; The Lathe of Heaven (1971), The Dispossessed (1974), which won the Hugo, "
  "the Nebula and the Locus and is the most discussed anarchist novel in English, and The Word for "
  "World Is Forest (1976) followed. Always Coming Home (1985) and the later Earthsea books - Tehanu "
  "(1990), Tales from Earthsea (2001) and The Other Wind (2001) - deepened the sequence, and her essays "
  "in The Language of the Night (1979), Dancing at the Edge of the World (1989) and Words Are My Matter "
  "(2016) made her the field's most articulate critic. She was awarded the National Book Foundation's "
  "Medal for Distinguished Contribution to American Letters in 2014, and died in Portland on 22 January "
  "2018.",
  "Novels: Rocannon's World (1966), Planet of Exile (1966), City of Illusions (1967), A Wizard of "
  "Earthsea (1968), The Left Hand of Darkness (1969), The Tombs of Atuan (1970), The Lathe of Heaven "
  "(1971), The Farthest Shore (1972), The Dispossessed (1974), The Word for World Is Forest (1976), "
  "Malafrena (1979), The Beginning Place (1980), The Eye of the Heron (1982), Always Coming Home "
  "(1985), Tehanu (1990), The Other Wind (2001) and Lavinia (2008). Stories: The Wind's Twelve Quarters "
  "(1975), Orsinian Tales (1976), The Compass Rose (1982), Buffalo Gals and Other Animal Presences "
  "(1987), A Fisherman of the Inland Sea (1994), Four Ways to Forgiveness (1995), Unlocking the Air "
  "(1996) and Changing Planes (2003). Essays and poetry: The Language of the Night (1979), Dancing at "
  "the Edge of the World (1989), Steering the Craft (1998), Words Are My Matter (2016) and the "
  "collection of poetry Late in the Day (2015).",
  "A plain, exact and rhythmically poised prose that never strains for effect; invented cultures "
  "presented through their own habits, food, kinship terms and proverbs rather than through exposition; "
  "a narrator who is a visiting anthropologist or a participant-observer; dialogue that carries the "
  "moral argument; and an ending that resolves the plot while leaving the ethical question open.",
  "The anthropologist's question of how a society makes its members - kinship, taboo, gift, ritual; "
  "gender and the arbitrariness of the roles attached to it; anarchism, ownership and the possibility "
  "of a just political order; death, ageing and the price of immortality; the relation of humans to "
  "other species and to the land; and language itself as the technology that makes a world.",
  "Le Guin is the most honoured writer in the history of science fiction and fantasy - six Hugos, six "
  "Nebulas, the National Book Award, the PEN/Malamute and a Library of Congress Living Legend award - "
  "and the writer who did most to make the field's treatment of gender, politics and anthropology "
  "respectable to the literary mainstream. The Left Hand of Darkness and The Dispossessed are set texts "
  "in courses on science fiction, on utopia and on feminist theory, and her essays on writing are among "
  "the most quoted in the language.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Le Guin, with the first "
           "printing of 'Schrodinger's Cat' in Universe 5 (1974), edited by Terry Carr, taken from the "
           "anthology's copyright page and from the several accounts of the story's publication; they "
           "were not checked against a printed bibliography. Installment 10 records one Norton "
           "selection - 'Schrodinger's Cat' - so the twenty-one novels, the other stories and the "
           "essays have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_UKL, W_U5, NAAL]),
A10(OEB, MAJ, "1947", "2006", "Pasadena, California, United States",
  "American; novelist and short-story writer writing in English",
  "American science-fiction writer and the first of the field to receive a MacArthur Fellowship, whose "
  "Patternist, Xenogenesis and Parable books made race, power and biological necessity the central "
  "questions of American speculative fiction",
  "Octavia Estelle Butler was born in Pasadena, California, on 22 June 1947 and was raised by her "
  "widowed mother and grandmother; shy, dyslexic and, as she later said, 'a black girl in a white "
  "world', she began writing at twelve after seeing the film Devil Girl from Mars and deciding that she "
  "could do better. She took an associate's degree at Pasadena City College, attended California State "
  "University at Los Angeles and the Clarion Science Fiction Writers' Workshop in 1970, and published "
  "Patternmaster (1976), the first of the five Patternist books, which were followed by Mind of My Mind "
  "(1977), Survivor (1978), Wild Seed (1980) and Clay's Ark (1984). Kindred (1979), the novel in which a "
  "Black woman of 1976 is pulled back to a Maryland plantation to save the life of her white ancestor, "
  "made her reputation outside the genre and is now a standard text in American literature courses. The "
  "Xenogenesis trilogy - Dawn (1987), Adulthood Rites (1988) and Imago (1989) - was collected as Lilith's "
  "Brood; the Parable books, Parable of the Sower (1993) and Parable of the Talents (1998), which won "
  "the Nebula, imagined a near-future America of climate collapse and religious fundamentalism. Her "
  "stories were collected in Bloodchild and Other Stories (1995) and her journals and essays in Earthseed "
  "and elsewhere. She received a MacArthur Fellowship in 1995 - the first given to a science-fiction "
  "writer - and the PEN Lifetime Achievement Award in 2000, and died of a stroke in Lake Forest Park, "
  "Washington, on 24 February 2006.",
  "Fiction: Patternmaster (1976), Mind of My Mind (1977), Survivor (1978), Kindred (1979), Wild Seed "
  "(1980), Clay's Ark (1984), Dawn (1987), Adulthood Rites (1988), Imago (1989), Parable of the Sower "
  "(1993) and Parable of the Talents (1998). Stories: Bloodchild and Other Stories (1995, expanded "
  "2005). Nonfiction and journals: Earthseed: The Books of the Living (in the Parable novels) and "
  "uncollected essays and interviews. Posthumous: Fledgling (2005) and the unfinished Parable of the "
  "Trickster (2020, published in manuscript).",
  "A plain, declarative prose that reports the most extreme bodily and social situations without "
  "raising its voice; a first-person narrator who is usually a survivor and who explains the rules of "
  "her world as she learns them; a structural patience that withholds the meaning of an institution "
  "until the reader has lived inside it; and a refusal of the villain, since the oppressor is usually "
  "also a person with reasons that can be understood.",
  "Slavery, coerced reproduction and the ownership of bodies, transposed into alien biology; race and "
  "the inheritance of racial power; symbiosis, dependency and the impossibility of a clean escape from "
  "the other; community, mutual obligation and the founding of a religion; climate collapse, scarcity "
  "and migration; and the ethics of survival, which is always someone else's cost.",
  "Butler is the most influential Black American writer of speculative fiction and the one through whom "
  "the genre's engagement with race and power is dated into two periods. Kindred is taught as American "
  "literature rather than as genre fiction, the MacArthur Fellowship of 1995 was the first given to a "
  "science-fiction writer, and 'Bloodchild' - with its Hugo, Nebula and Locus awards - is the story "
  "most often used to show that the field's best work is about love and obligation rather than "
  "gadgets; her influence on the writers who followed, and on the political reading of "
  "science fiction after 2016, is acknowledged on every side.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Butler and from the account of "
           "'Bloodchild' in its first book collection; the first printing in Isaac Asimov's Science "
           "Fiction Magazine for June 1984 is recorded from that account. They were not checked against "
           "a printed bibliography. Installment 10 records one Norton selection - 'Bloodchild' - so the "
           "twelve novels and the other stories have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_OEB, W_BC, NAAL]),
]

WORKS = [
W10("Nobel Lecture in Literature", TM, "1993", "Lecture (nonfiction prose)", "major",
  genres=G("Nonfiction Prose (1946–2000)", "Literary Essay", "Political Essay", "Cultural Criticism"),
  themes=T("Language, writing and the limits of representation", "Race, racism and the struggle for civil rights",
           "Memory, trauma and testimony"),
  movements=M(AAW),
  overview="Toni Morrison delivered the Nobel Lecture in Literature in Stockholm on 7 December 1993, on "
           "accepting the prize awarded to her that October, and published it the following year as The "
           "Nobel Lecture in Literature, 1993 (New York: Alfred A. Knopf, 1994). It is a parable rather "
           "than an address. An old blind woman, known to her neighbours as a witch, is visited by a "
           "group of children who demand that she tell them something - 'a story', 'something to think "
           "about' - and who threaten her when she does not. She answers them with a riddle about a bird "
           "in her hands: whether it is living or dead, she says, is not her business but theirs. The "
           "lecture is the fullest statement of Morrison's belief that language is the medium in which "
           "human life is made worth living, and that the writer's obligation is to refuse the "
           "degradations of official speech.",
  content="The lecture opens by naming the occasion - 'I entered this hall as an old woman, but I leave "
          "it as a child' - and then retires behind the parable, so that the voice that speaks is not the "
          "laureate's but the community's. The children arrive at the old woman's house, mocking her, "
          "demanding that she 'tell us what it is', and one of them holds out a bird. She answers: 'I "
          "don't know whether that bird is living or dead. It is in your hands.' From there the lecture "
          "turns to the uses and abuses of language: the 'dead language' of officialdom, of the state "
          "and of the academy, which 'sores' the mind and 'sanctions ignorance, and worse, actively "
          "impairs knowledge'; the 'language of the law' and of 'the press', which she calls 'the "
          "language of the master'; and the countervailing language of 'the village' - the vernacular, "
          "the improvised, the sung language in which a people keeps its memory. She speaks of her own "
          "grandparents, of the songs and stories that surrounded her childhood, and of the writers who "
          "showed her what literature could do with the speech of ordinary people. The lecture closes "
          "with the claim that 'we die. That may be the meaning of life. But we do language. That may be "
          "the measure of our lives.'",
  summary="The lecture's argument is conducted entirely through narrative and image, and its structure "
          "is that of a call and response. The children's demand - 'Tell us what it is' - is the "
          "question the lecture is answering, and the old woman's refusal to answer it directly is the "
          "method. Language, she says, is not a tool the writer picks up but a living thing that the "
          "community holds, as the child holds the bird: whether it lives or dies depends on how it is "
          "used. The middle movement of the lecture is a jeremiad against the language of the state and "
          "the market, which she describes as having been 'sapped' of its capacity to mean; the third "
          "movement is a defence of the vernacular, the ungrammatical, the sung and the improvised, as "
          "the place where meaning survives. The essay's most quoted sentence - 'we die. That may be the "
          "meaning of life. But we do language. That may be the measure of our lives' - both closes the "
          "argument and states its stakes: language is what humans do with their mortality, and it is "
          "the only measure of a life that the lecture is prepared to trust. It is a public lecture that "
          "refuses the conventions of the form, and that is its point: a laureate's address that "
          "declines to speak in the voice of official culture.",
  themes_text="The lecture's first subject is language as the material of human life, which Morrison "
              "treats as a living creature held between speakers rather than a code to be decoded. Its "
              "second is the corruption of public speech - the language of the state, the press and the "
              "academy - which she describes as actively impairing knowledge, and which she sets against "
              "the speech of the village. The third is memory and its transmission: the grandparents and "
              "the songs, the stories and the sermons by which a people keeps its history and makes it "
              "usable. The fourth is the writer's responsibility, which the lecture locates not in "
              "public positions taken but in the care of the language itself, so that the Nobel address "
              "becomes a defence of literary craft as an ethical act.",
  structure="A single continuous lecture of about thirty-five hundred words in the printed Knopf edition, "
            "framed as a parable told to children and developed as a three-part argument: the parable, "
            "the indictment of official language, and the defence of the vernacular and of memory; there "
            "are no section headings, and the parable returns at the close to answer itself.",
  style="Plain, cadenced, largely dialect-free prose with a strong rhetorical pulse; direct address and "
        "reported speech; repetition of a single phrase as a refrain ('Tell us what it is'); a "
        "vocabulary that deliberately mixes the biblical and the vernacular; and a refusal of the "
        "academic and the bureaucratic registers that the lecture is attacking.",
  ctx="Delivered in Stockholm on 7 December 1993, two months after the Swedish Academy announced the "
      "award on 7 October, and published by Knopf in 1994 as a small book. Morrison was the first Black "
      "woman to receive the Nobel Prize in Literature, and the lecture's subject - the language of the "
      "master and the language of the village - is a direct answer to the expected European audience. It "
      "belongs to the group of essays and addresses of the early 1990s, with Playing in the Dark (1992), "
      "in which she was rethinking the relation of American literary language to race.",
  sig="The Nobel Lecture is Morrison's most widely circulated statement on the ethics of language and "
      "one of the handful of Nobel addresses of the postwar period that are read as literature in their "
      "own right; its closing sentences are among the most quoted in modern American prose, and it is a "
      "standing text in the teaching of the essay, of rhetoric and of African American literary "
      "tradition.",
  canon="Major canon",
  crit="Critics have read the lecture as a deliberate refusal of the European oratorical model it "
       "inhabits, as an extension of the call-and-response aesthetic of Black vernacular culture into "
       "the space of the laureate address, and as a companion to Playing in the Dark; the parable of the "
       "bird has been discussed for its refusal to answer the question it raises, and the lecture's "
       "attack on 'the language of the master' has been the starting point for the later criticism on "
       "Morrison and public speech.",
  biblio="Delivered in Stockholm on 7 December 1993; first published as The Nobel Lecture in Literature, "
         "1993 (New York: Alfred A. Knopf, 1994), 37 pp.; also issued in London by Chatto and Windus in "
         "1994. The Norton selection 'The Nobel Lecture in Literature' is recorded here under "
         "the title 'Nobel Lecture in Literature'. A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The lecture was delivered in 1993 and published as a book in 1994; the record uses the date of "
        "delivery, which is also the date in the title, and the note gives the publication year. The "
        "page count follows the Knopf first edition as recorded by booksellers; no printed bibliography "
        "was consulted.",
  ver="partially verified", sources=[W_TM, W_NOBEL, W_NOBELPRIZE, NAAL]),
W10("New York Girl", JU, "1996", "Short story (first-person narrative)", "significant",
  genres=G("Short Story", "Realist Fiction", "Domestic Fiction"),
  themes=T("Love, intimacy and loss", "The city, the suburb and modern space",
           "Class, labour and social mobility"),
  movements=M("Minimalism and Dirty Realism"),
  overview="'New York Girl' was published in The New Yorker for 1 April 1996 and collected in Licks of "
           "Love (New York: Alfred A. Knopf, 2000), the volume that also contains the sequel to the "
           "Rabbit novels, 'Rabbit Remembered'. It is narrated by a married man in his fifties who looks "
           "back on his affair, twenty-five years earlier, with a young woman who had come to New York "
           "from the Midwest to make her way in publishing. The story is one of Updike's several "
           "variations on the theme of the suburban husband and the city mistress, and it is told with "
           "the retrospective clarity of a man who understands his own behaviour too late to change it.",
  content="The narrator, a dealer or editor of some kind with a comfortable life in the suburbs, recalls "
          "the period of his affair with a woman he calls, in the story's title, a New York girl - a "
          "young woman in her twenties who lives in the city, works in publishing, dresses with a "
          "deliberate elegance and knows restaurants and galleries that he does not. The affair is "
          "conducted in her apartment and in the restaurants he takes her to, and it is described with "
          "Updike's characteristic attention to surfaces: the clothes, the food, the light in the room, "
          "the smell of the city in summer. The narrator's wife and children appear mostly as the "
          "background against which the affair is measured, and the story's drama is not whether he will "
          "be found out but the slow recognition, on both sides, that the affair is a season and not a "
          "life. The girl eventually leaves the city, or the narrator loses her to a life she has chosen "
          "elsewhere; the story closes with the narrator's sense of what he had, and what he could not "
          "have imagined losing.",
  summary="'New York Girl' is a story about the difference between the city and the suburb, and about "
          "the way an affair borrows the energy of the first while depending on the stability of the "
          "second. Updike's narrator is a man who notices everything and understands very little while "
          "it is happening; the story's retrospective frame allows him to be both the participant who "
          "was delighted and the older man who is now appalled at his own ease. The girl is drawn with a "
          "mixture of desire and condescension that the story does not entirely endorse: she is "
          "ambitious, funny, a little ruthless, and she wants the city in a way the narrator, who "
          "already has a life, cannot. The prose does what Updike's prose always does - it makes the "
          "world thick with detail until the moral question is embedded in a fabric rather than stated - "
          "and the ending refuses the two easy resolutions, the exposure and the escape, in favour of a "
          "third: the affair simply ends, and the narrator is left with the memory of a season in which "
          "he was happier than he had a right to be.",
  themes_text="The story's first subject is the opposition of city and suburb as two ways of living in "
              "time - the city as the place of the present tense, the suburb as the place of the "
              "calendar and the child's school term. Its second is the asymmetry of the affair: the "
              "older man risks nothing he values, and the younger woman spends the years in which she "
              "might have made a life. The third is the retrospective voice itself, which Updike uses to "
              "make the narrator's present judgement part of the story's action, so that the reader is "
              "watching a man watch himself.",
  structure="A single retrospective narration in the past tense, without chapter breaks, moving forward "
            "from the beginning of the affair to its end and returning at the close to the narrator's "
            "present; the temporal shifts are managed by the narrator's memory rather than by scene "
            "breaks.",
  style="Long, comma-heavy, sensory sentences; the present tense used inside remembered scenes for "
        "immediacy; a vocabulary that is precise about clothes, food and interiors and moralistic about "
        "almost nothing else; and direct address to the reader withheld until the final paragraphs, "
        "where the narrator turns to the second person to generalise his case.",
  ctx="Published in The New Yorker for 1 April 1996 and collected in Licks of Love (Knopf, 2000), a "
      "volume of twelve stories and the novella 'Rabbit Remembered'. It belongs to the group of late "
      "Updike stories about marriage, adultery and the New York of the 1960s and 1970s, and it was "
      "broadcast by BBC Radio 3 in a reading by the author on 28 December 1996.",
  sig="'New York Girl' is one of the best known of Updike's late stories and a standard example of the "
      "late-twentieth-century American story of adultery; it is anthologised and taught as a model of "
      "the retrospective first-person narrative, and it belongs to the small group of his stories in "
      "which the subject is the city itself.",
  canon="Secondary canon",
  crit="Critics have read the story as an instance of Updike's late style - the long sentence, the "
       "sensory catalogue, the moral judgement withheld - and as a companion to the Rabbit books in its "
       "treatment of the American male at mid-life; feminist readings have attended to the asymmetry of "
       "the affair and to the way the girl is seen by a narrator who does not quite see her.",
  biblio="First published in The New Yorker, 1 April 1996; collected in Licks of Love: Short Stories and "
         "a Sequel (New York: Alfred A. Knopf, 2000) and in John Updike: Collected Later Stories "
         "(Library of America, 2013). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The New Yorker printing of 1 April 1996 is recorded from the magazine's archive and from the "
        "published index of Updike's contributions; the collection date of 2000 follows the Knopf first "
        "edition's contents as recorded by library catalogues.",
  ver="partially verified", sources=[W_JU, W_NYG, W_LICKS, NAAL]),
W10("The Conversion of the Jews", PR, "1958", "Short story (third-person narrative)", "major",
  genres=G("Short Story", "Realist Fiction", "Domestic Fiction"),
  themes=T("Faith, doubt and the sacred", "Childhood, adolescence and coming of age",
           "Education, institutions and the academy"),
  movements=M(JAF),
  overview="'The Conversion of the Jews' first appeared in The Paris Review, no. 18 (Spring 1958), and "
           "was collected in Goodbye, Columbus (Boston: Houghton Mifflin, 1959), Roth's first book, "
           "which won the National Book Award in 1960. Its hero is Ozzie Freedman, a thirteen-year-old "
           "boy in a Hebrew school in Newark who asks his rabbi whether God could have made a child "
           "without intercourse, is slapped for it, runs to the roof of the synagogue, and refuses to "
           "come down until the rabbi and the assembled adults - his mother, the rabbi, the rabbi's son, "
           "the firemen with a net - acknowledge that God can do anything. It is the founding story of "
           "Roth's career and the first appearance of the Newark Jewish childhood that he would spend "
           "fifty years revisiting.",
  content="Ozzie Freedman is a pupil in the Hebrew school attached to a synagogue in Newark, taught by "
          "Rabbi Marvin Binder, a man of 'a certain amount of flesh' and an uncertain temper. Ozzie's "
          "friend Itzie Lieberman reports that Ozzie has been asking the rabbi whether God can create a "
          "child without a man, which the rabbi takes as impertinence; Ozzie persists, arguing that if "
          "God is all-powerful then the virgin birth must be possible, and the rabbi, goaded, slaps him "
          "and bloodies his nose. Ozzie runs from the classroom to the roof of the building, and the "
          "story's second half is the siege: the rabbi, the principal, Ozzie's mother and a crowd gather "
          "below; the fire department is called; a net is spread. Ozzie threatens to jump unless the "
          "adults - the rabbi, his mother, and the rabbi's son - tell him that God can do anything, and "
          "they do, one by one, shouting their assent up to the roof. He jumps into the net, and the "
          "story ends with the rabbi weeping and Ozzie, in the air, asking God to forgive the adults for "
          "having lied to him about what they believed.",
  summary="The story is built as a comedy of theological literalism, and its engine is Ozzie's refusal to "
          "accept the difference between what the adults say about God and what they believe. He is not "
          "a rebel against his religion; he is a boy who takes it more seriously than the men who teach "
          "it, and the story's satire is aimed at the rabbi, whose God is a matter of institutional "
          "decorum rather than omnipotence. The slap is the pivot: after it, Ozzie's argument stops "
          "being a classroom exchange and becomes a public claim, and the roof is the place from which "
          "he can make the adults say what they have been teaching him. The siege is staged by Roth with "
          "the timing of a farce - the firemen, the net, the neighbours, the mother's distress - and the "
          "ending is both a victory and a betrayal: Ozzie wins the words he wanted, and in the moment of "
          "winning he sees that the adults have said them to save him rather than because they believe "
          "them, so that his last gesture is a prayer for their forgiveness. The story's formal "
          "achievement is that it carries a real theological question inside a boy's practical joke and "
          "never lets either swallow the other. It is also, in miniature, the whole of Roth's later "
          "method: the narrator who is smarter than the adults around him, the scene that escalates "
          "from embarrassment into spectacle, the comic surface that turns out to be carrying an "
          "argument about what a religion actually asks of the people who inherit it, and the ending "
          "that leaves the hero suspended - here literally, in the air above a firemen's net - between "
          "the childhood he has lost and the adulthood he is not ready for.",
  themes_text="The first subject is faith as a literal proposition, which Ozzie holds and the adults only "
              "administer: the question of whether God can do anything is not, for him, a rhetorical "
              "one, and the story's comedy comes from the adults' discomfort at being taken at their "
              "word. The second is the institution - the Hebrew school, the rabbi, the principal, the "
              "fire department - as a system for managing belief rather than for holding it. The third "
              "is adolescence as the moment when a child discovers that the adults do not mean what they "
              "say, which is the real conversion of the title: Ozzie does not leave his faith, he "
              "discovers the gap between it and its teachers. The fourth is Newark, the Jewish "
              "neighbourhood of Roth's childhood, which is here for the first time the whole world of a "
              "story.",
  structure="A single continuous narrative in two movements - the classroom, told largely through "
            "Itzie's report of the previous day, and the siege on the roof - with a short coda of "
            "Ozzie in the air; the point of view stays close to Ozzie but is reported by a third person "
            "who can see the adults as well as the boy.",
  style="Comic, fast, colloquial narration with a heavy use of direct speech and of Jewish-American "
        "idiom; the rabbi's and the mother's speech rendered phonetically; free indirect discourse that "
        "slips into Ozzie's vocabulary; and a control of timing that turns a theological argument into a "
        "farce without diminishing it.",
  ctx="First published in The Paris Review, no. 18 (Spring 1958), and collected in Goodbye, Columbus "
      "(Boston: Houghton Mifflin, 1959), which won the National Book Award for Fiction in 1960. Roth was "
      "twenty-four when the story appeared and twenty-six when the book was published; the Newark "
      "setting, the Hebrew school and the rabbi are drawn from his own childhood in the Weequahic "
      "district, and the book's reception - attacked by some Jewish readers as self-hating - began the "
      "long argument about Roth's representation of American Jewish life.",
  sig="'The Conversion of the Jews' is the story with which Roth's career begins and one of the most "
      "anthologised American short stories of the postwar period; it is the standard introduction to the "
      "Newark Jewish childhood that his later books return to, and it is a set text in the teaching of "
      "the American short story and of Jewish-American literature.",
  canon="Major canon",
  crit="Criticism has read the story as a comedy of assimilation, as a theological argument conducted "
       "through a child's literalism, and as the first appearance of the themes - the father's absence, "
       "the rabbi as a failed authority, the son who out-argues his teachers - that run through Roth's "
       "work. Its reception in 1959 as an act of Jewish self-exposure, and Roth's reply to that charge "
       "in later essays and interviews, are part of the story's critical history; more recent readings "
       "have emphasised its comic technique and its debt to the Yiddish anecdote.",
  biblio="First published in The Paris Review, no. 18 (Spring 1958); collected in Goodbye, Columbus and "
         "Five Short Stories (Boston: Houghton Mifflin, 1959), which won the National Book Award in "
         "1960; reprinted in Reading Myself and Others (1975) and in the Library of America edition of "
         "Roth's early novels and stories. A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The Paris Review issue number and season are recorded from Wikipedia's article on Goodbye, "
        "Columbus and from the magazine's own archive note; the exact day of publication in the issue "
        "was not established from the sources consulted.",
  ver="partially verified", sources=[W_PR, W_GC, W_PF_CJ, NAAL]),
W10("Precious Artifact", PKD, "1964", "Short story (science-fiction narrative)", "significant",
  genres=G("Short Story", "Science Fiction", "Soft Science Fiction"),
  themes=T("Technology, media and consumer society", "Alienation, absurdity and existential freedom",
           "Utopia, dystopia and imagined futures"),
  movements=M(NWSF),
  overview="'Precious Artifact' appeared in Galaxy Magazine for October 1964 and was collected in We Can "
           "Remember It for You Wholesale (1990) and in later volumes of Dick's collected stories. It is "
           "one of the handful of stories Dick wrote in 1964, the year in which he produced 'Oh, to Be a "
           "Blobel!', 'The Little Black Box' and 'Cantata 140', and it belongs to his early-1960s manner: "
           "a small-time professional - here a man who rebuilds and repairs the machines of a ruined "
           "civilisation - discovers that the world he is trying to restore is not the world that "
           "existed, and that the artefact he has been preserving is a record of somebody else's "
           "catastrophe.",
  content="The story is set on a depopulated and ruined Earth in the aftermath of a war between human "
          "settlements on other planets, and its protagonist makes his living by salvaging and repairing "
          "the mechanical and electronic remains of the old civilisation - the 'precious artifacts' of "
          "the title. He is visited by an agent or investigator from one of the off-world colonies, who "
          "wants a particular object recovered from the ruins; the object turns out to be a recording or "
          "a data store that contains the history of the war and, in particular, the fact that the "
          "colony the visitor represents was responsible for the destruction of the Earth. The "
          "protagonist's trade - the careful restoration of broken things - becomes the story's moral "
          "centre, since what he recovers is not a piece of machinery but a truth that the purchaser "
          "would rather have left in the rubble. The story ends with the artefact in the hands of "
          "someone who understands what it is, and with the protagonist's small, compromised decision "
          "about what to do with it.",
  summary="'Precious Artifact' is a story about restoration as a form of remembering, and it works by "
          "withholding the nature of the object until the protagonist has already committed himself to "
          "recovering it. Dick's ruined Earth is described with the flatness of a man describing his own "
          "backyard: the salvage is ordinary work, the machinery is ordinary machinery, and the war that "
          "made the ruins is reported as a fact of the trade rather than as a catastrophe. The arrival "
          "of the off-world visitor introduces the political question, and the story's turn is the "
          "discovery that the artefact is a piece of evidence - that the history of the war has been "
          "rewritten by the side that won, and that the object the protagonist has been paid to find "
          "will contradict the official account. The ending is characteristically Dick: it does not "
          "stage a trial or a revelation, but leaves the protagonist with a decision he makes alone and "
          "for reasons the story only partly explains, so that the reader is left with the sense that "
          "the moral question has been answered privately rather than publicly.",
  themes_text="The story's first subject is the artefact as a carrier of memory - the object that "
              "survives a catastrophe and tells a different story from the one the survivors tell. Its "
              "second is the ordinary worker inside a ruined economy, whose trade keeps him alive and "
              "also implicates him in the lies of his customers. The third is the politics of the "
              "record: who owns the history of a war, and what the victor does to the evidence. The "
              "fourth is Dick's recurring question of the false world - the sense that the reality one "
              "inhabits has been constructed for someone else's convenience - which this story poses in "
              "the modest form of a piece of salvage rather than a cosmic vision.",
  structure="A single linear narrative in the third person, following the protagonist through one "
            "commission from the arrival of the visitor to the disposal of the artefact; the backstory "
            "of the war is given in dialogue and in the protagonist's own recollection rather than in "
            "exposition.",
  style="Plain, rapid, colloquial American prose with a heavy proportion of dialogue; technical "
        "vocabulary used casually and without explanation, so that the reader learns the world from the "
        "trade; a deadpan tone applied to grotesque or apocalyptic material; and an ending that closes "
        "the action without explaining the protagonist's motive.",
  ctx="Published in Galaxy Magazine for October 1964, in the middle of the most productive decade of "
      "Dick's career and in the year of 'Oh, to Be a Blobel!', 'The Little Black Box', 'Cantata 140' and "
      "'A Game of Unchance'. It was collected in We Can Remember It for You Wholesale (1990) and in The "
      "Collected Stories of Philip K. Dick. Its ruined-Earth setting belongs to the postwar science-"
      "fiction tradition of the aftermath narrative, and its concern with the politics of the record "
      "belongs to the Cold War culture of the early 1960s.",
  sig="'Precious Artifact' is a representative rather than a famous Dick story, and it is valuable "
      "precisely for that: it shows his characteristic procedures - the working protagonist, the object "
      "that carries a suppressed history, the flat tone applied to catastrophe - at short-story length. "
      "It is included in the standard collected editions of his stories and is used in criticism to "
      "illustrate the 1964 phase of his work.",
  canon="Secondary canon",
  crit="Criticism of Dick's short fiction places the 1964 stories in the phase between the realist "
       "novels of the late 1950s and the metaphysical novels after 1965, and reads 'Precious Artifact' "
       "as an early instance of his interest in the manufactured record and in the politics of memory; "
       "the story is discussed more often in surveys of his career than in single-author studies.",
  biblio="First published in Galaxy Magazine, October 1964; collected in We Can Remember It for You "
         "Wholesale (1990) and in The Collected Stories of Philip K. Dick, vol. 2. A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The Galaxy printing of October 1964 is recorded from the FictionMags Index and from the "
        "finding aid of the Philip K. Dick collection at the University of California; the story's "
        "first book collection is given as We Can Remember It for You Wholesale (1990). No printed "
        "bibliography of Dick was consulted.",
  ver="partially verified", sources=[W_PKD, W_PKDB, W_FMI, NAAL]),
W10("Schrödinger's Cat", UKL, "1974", "Short story (first-person science-fiction narrative)", "significant",
  genres=G("Short Story", "Science Fiction", "Speculative Fiction (1946–2000)"),
  themes=T("Alienation, absurdity and existential freedom", "Myth, folklore and the supernatural",
           "Language, writing and the limits of representation"),
  movements=M(NWSF),
  overview="'Schrodinger's Cat' was first published in Universe 5 (1974), the anthology edited by Terry "
           "Carr, and collected in The Compass Rose (1982) and in Buffalo Gals and Other Animal "
           "Presences (1987). A narrator in a house in the American countryside is visited, in quick "
           "succession, by a cat, by a dog-like creature carrying a knapsack, a box and a photon gun, "
           "and by a series of further visitors, each of whom explains the quantum-mechanical thought "
           "experiment that gives the story its title. The story is a comedy of explanation and a "
           "parable about observation: the cat in the box is neither alive nor dead until someone opens "
           "the lid, and the narrator discovers that the same is true of the world she is standing in.",
  content="The story begins with the narrator noticing that 'things appear to be coming to some sort of "
          "climax': a cat has arrived in her house and will not leave. The doorbell rings, and a "
          "creature that looks like a dog - large, earnest, carrying a huge knapsack - enters and begins "
          "to unpack: a box, a photon gun, and the apparatus of an experiment. The dog recognises the "
          "cat as 'Schrodinger's cat' and explains the thought experiment: a cat sealed in a box with a "
          "device that may or may not kill it is, according to quantum mechanics, neither alive nor dead "
          "until the box is opened and the outcome observed. The cat, obligingly, jumps into the box and "
          "closes the lid with its tail, and the narrator is left with the decision of whether to open "
          "it. Before she can, a series of further visitors arrives - each with a different account of "
          "the experiment and of what the narrator ought to do - and the house itself begins to come "
          "apart, the roof being removed by something larger than the story can name. The story ends "
          "with the narrator's recognition that she is inside a thought experiment and that her own "
          "observation is what the experiment is waiting for.",
  summary="'Schrodinger's Cat' is a story about the moment before a decision, and its method is "
          "escalation. Each visitor explains the experiment more fully and less helpfully than the last; "
          "the box stays closed; and the narrator, who is the only person in the story with the power to "
          "open it, becomes increasingly unable to act. Le Guin's prose is comic and exact - the dog is "
          "earnest, the cat is insufferable, the narrator is put-upon - and the comedy carries a genuine "
          "philosophical question: if observation is what makes a thing determinate, then the observer "
          "is part of the experiment, and there is no position outside it from which to decide. The "
          "story's final movement, in which the house is opened from above by something vast, extends "
          "the joke one level further: the narrator is herself a cat in a box, and the reader is the "
          "observer who has been waiting for her to act. It is one of the small number of stories "
          "credited with bringing Schrodinger's thought experiment into popular culture, and it does so "
          "not by explaining the physics but by making the reader feel the vertigo of the position.",
  themes_text="The story's first subject is observation and determinacy - the proposition that a thing "
              "is not settled until it is seen, and the corollary that the observer is never outside "
              "the system she observes. Its second is the comedy of explanation: every visitor arrives "
              "with a theory, and the theories multiply rather than resolve. The third is the ordinary "
              "domestic setting - the house, the doorbell, the cat on the sofa - used as the stage for a "
              "metaphysical crisis, which is Le Guin's characteristic way of making abstraction "
              "habitable. The fourth is the anthropologist's interest in how other minds model the "
              "world: the dog is a reasoner, the cat is a fact, and the narrator is the field in which "
              "their models collide.",
  structure="A single continuous first-person narration in the present tense, built as a series of "
            "arrivals at the narrator's house; each arrival adds a layer of explanation, and the story "
            "escalates from the domestic to the cosmic without a scene break.",
  style="Plain, dry, comic first-person prose in the present tense; short paragraphs and quick beats; a "
        "domestic vocabulary set against the technical vocabulary of quantum mechanics; and dialogue in "
        "which each speaker is characterised by the way he explains.",
  ctx="Written in September 1972 and first published in Universe 5 (1974), edited by Terry Carr, then "
      "collected in The Compass Rose (1982) and Buffalo Gals and Other Animal Presences (1987). Le Guin "
      "had learned of the thought experiment while researching quantum mechanics for The Dispossessed "
      "(1974), and the story is credited by historians of science with helping to bring Schrodinger's "
      "cat into popular culture in the 1970s and 1980s.",
  sig="'Schrodinger's Cat' is the story most often credited with popularising Schrodinger's thought "
      "experiment outside physics, and it is a standard example of Le Guin's comic mode; it is "
      "anthologised in collections of science fiction and of writing about science, and it is used in "
      "teaching to show how a philosophical problem can be dramatised rather than explained.",
  canon="Secondary canon",
  crit="Critics have read the story as a comedy of the observer problem, as an instance of Le Guin's "
       "interest in the models by which minds construe the world, and as a companion to 'The Author of "
       "the Acacia Seeds' in its play with non-human perspectives; historians of science have cited it "
       "in accounts of how the thought experiment entered popular culture, and Le Guin herself called "
       "it a 'slight, playful story with an undercurrent of sorrow'.",
  biblio="Written September 1972; first published in Universe 5, ed. Terry Carr (1974); collected in The "
         "Compass Rose (1982) and Buffalo Gals and Other Animal Presences (1987). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The date of 1974 in the list is the date of first publication in Universe 5, not of "
        "composition; the story was finished in September 1972. The anthology's copyright page gives "
        "the 1974 first appearance, and the several published accounts of the story agree on it.",
  ver="partially verified", sources=[W_UKL, W_U5, NAAL]),
W10("Bloodchild", OEB, "1984", "Short story (novelette; first-person science-fiction narrative)", "major",
  genres=G("Short Story", "Science Fiction", "Soft Science Fiction"),
  themes=T("Sexuality, desire and the closet", "Power, the state and surveillance",
           "Family, marriage and domestic life"),
  movements=M(FSF, NWSF),
  overview="'Bloodchild' was first published in Isaac Asimov's Science Fiction Magazine for June 1984 "
           "and won the Hugo, the Nebula, the Locus and the Science Fiction Chronicle awards for best "
           "novelette; it became the title story of Butler's collection Bloodchild and Other Stories "
           "(1995). It is narrated by Gan, a young human man living on a reservation on an alien world "
           "governed by the Tlic, a large insect-like species that needs human bodies to carry its "
           "young. The story is usually described as a story about male pregnancy, and Butler insisted "
           "that it was a love story: a story about what a person will consent to for the sake of the "
           "people he loves, and about the price of a bargain that keeps both species alive.",
  content="Gan opens the story on 'my last night of childhood', when T'Gatoi, the Tlic official who has "
          "been his family's patron since before his birth, brings two sterile eggs - a drug that "
          "produces euphoria and protects against the Tlic parasite - and insists that Gan eat one "
          "alone. His mother refuses hers, and watches him. Gan's older brother and sisters have already "
          "been chosen or passed over; his sister wants to be chosen, and his mother is still coming to "
          "terms with the choice that was made for Gan when he was an infant. The night's crisis arrives "
          "when another human family, the Lomas, arrive with a man, Bram Lomas, in the final stage of "
          "an infestation: a Tlic grub has grown inside him and must be cut out before it kills him, and "
          "the operation is performed on the family's kitchen table with the animals of the house "
          "watching. Gan, who is expected to watch as part of his education, is horrified, and the "
          "horror changes the terms of his consent. In the end he agrees to carry T'Gatoi's children, but "
          "on a condition that he negotiates himself - that his own sister and brother be protected and "
          "not sold - and the story closes with the two of them together, and with Gan no longer a child.",
  summary="'Bloodchild' is a story about a bargain, and its achievement is to make the bargain feel "
          "simultaneously monstrous and reasonable. The Tlic need human bodies to reproduce, and humans "
          "need the Tlic for protection and for the eggs that make life bearable; the arrangement is "
          "slavery in one reading and symbiosis in another, and Butler refuses to settle it. Gan's "
          "narration is calm, exact and loving: he describes T'Gatoi's limbs and her smell with "
          "affection, and he describes the operation on Bram Lomas with the same flat attention, so that "
          "the reader cannot separate the tenderness from the horror. The story's turning point is not "
          "the operation but Gan's decision afterwards, which he makes not out of submission but out of "
          "a clear-eyed calculation about what he can bear and what his family needs. Butler said that "
          "readers who took the story as an allegory of slavery had missed what she meant, and that she "
          "had written a love story about a man who chooses to bear a child; the story supports both "
          "readings without collapsing into either, which is why it is taught as an exercise in the "
          "ethics of consent. Butler's control of tone is the story's real technical achievement: Gan "
          "reports the cutting of a man's belly open with the same calm he brings to the smell of the "
          "kitchen or the weight of T'Gatoi's limbs, and because he does not tell the reader to be "
          "horrified, the horror arrives without interference. The result is a story that can be read "
          "as body horror, as a coming-of-age narrative, as a political allegory or as a love story, "
          "and that is diminished by any reading which chooses only one of them.",
  themes_text="The first subject is reproduction and the ownership of the body, which the story "
              "literalises by giving the pregnancy to a man and the institution to an alien species. The "
              "second is consent: Gan's agreement is not freely given in any simple sense - he has been "
              "chosen before he could speak - and yet the story insists that a bargain can be entered "
              "into with knowledge and love, and that this is different from being used. The third is "
              "the family as the place where the political arrangement is lived: the mother's refusal of "
              "the egg, the sister's wish to be chosen, the brother's fear, and Gan's negotiation for "
              "their protection all make the reservation a domestic space rather than a metaphor. The "
              "fourth is the animal: the Tlic are not villains, and Butler gives them a biology, a "
              "politics and an affection that make them legible as persons.",
  structure="A single first-person narration in the past tense, covering one night and the following "
            "morning; the backstory of the reservation and the Tlic is given in Gan's recollections as "
            "they are triggered by the night's events, and the story's climax - the operation - arrives "
            "at the centre rather than at the end, so that the decision that follows is the real "
            "climax.",
  style="Calm, exact, unhurried first-person prose; sensory detail used sparingly and precisely, so that "
        "the alien is described in domestic terms; dialogue that carries the political argument without "
        "becoming an argument; and a refusal of the horror-genre vocabulary that the material would "
        "justify, which is what makes the horror land.",
  ctx="First published in Isaac Asimov's Science Fiction Magazine, June 1984, and collected in Bloodchild "
      "and Other Stories (1995), expanded in 2005. Butler wrote it while preparing for a trip to the "
      "Amazon to research the Xenogenesis series, and said that the story began as a way of managing her "
      "fear of parasitic insects - the botfly in particular. It won the Hugo and Nebula awards for best "
      "novelette in 1985, and the Locus award, and it is the story most often cited in the argument for "
      "Butler's place in the canon of American literature.",
  sig="'Bloodchild' is Butler's most awarded story and one of the most anthologised American short "
      "stories of the 1980s; it is a set text in courses on science fiction, on gender and on the "
      "ethics of consent, and its triple award - Hugo, Nebula and Locus - together with its appearance "
      "in The Weird and The Big Book of Science Fiction has made it the standard introduction to "
      "Butler's shorter work.",
  canon="Major canon",
  crit="Critics have read the story as an allegory of slavery (a reading Butler resisted), as a "
       "thought-experiment about male pregnancy and the ownership of reproductive labour, and as a "
       "study in consent and dependency; feminist and queer readings have been central since the 1990s, "
       "and the story's refusal to resolve the question of whether the arrangement is exploitation or "
       "mutualism is the point on which most criticism turns.",
  biblio="First published in Isaac Asimov's Science Fiction Magazine, June 1984; collected in Bloodchild "
         "and Other Stories (New York: Seven Stories Press, 1995; expanded 2005). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first printing in the June 1984 issue of Isaac Asimov's Science Fiction Magazine is "
        "recorded from the several published accounts of the story and from the collection's own "
        "acknowledgements; the exact page numbers of the magazine printing were not established from "
        "the sources consulted.",
  ver="partially verified", sources=[W_OEB, W_BC, NAAL]),
]
