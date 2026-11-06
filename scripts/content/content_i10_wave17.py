"""Installment 10, wave 18: new Norton authors in the English anthology's order, from Les Murray to
Arundhati Roy.

Five authors are new to the database: Les Murray, J. G. Ballard, Bessie Head, Ben Okri and Arundhati
Roy. One record per Norton selection first published 1946-2000, and nothing else: an excerpt is
recorded as the book it comes from (Ballard's The Drowned World, Roy's The God of Small Things).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL  # noqa: E402

LM = "Les Murray"
JB = "J. G. Ballard"
BH = "Bessie Head"
BO = "Ben Okri"
AR = "Arundhati Roy"
POSTCOL = "Postcolonial Literature"
AFR = "African Literature in English"
SAS = "South Asian Literature in English"
INDIG = "Indigenous Writing in Australia, Canada and New Zealand"
NWAVE = "New Wave Science Fiction"
MAGIC = "Magical Realism in English"
SAAP = "South African Writing under Apartheid"

W_LM = "Les Murray (poet) (Wikipedia)"
W_JB = "J. G. Ballard (Wikipedia)"
W_DW = "The Drowned World (Wikipedia)"
W_BH = "Bessie Head (Wikipedia)"
W_BO = "Ben Okri (Wikipedia)"
W_AR = "Arundhati Roy (Wikipedia)"
MUR_ABR = "Peter Goldsworthy reviews Les Murray's Collected Poems (Australian Book Review)"
MUR_CP = "Les Murray, Collected Poems (contents listing, readfrom.net)"
HEAD_NOTE = "'Looking for a Rain God' by Bessie Head (study notes, acharyar.com.np)"
OKRI_SCALAR = "Ben Okri's 'What the Tapster Saw' (Niger Delta Black Gold Blues, University of Southern California)"
OKRI_READ = "Ben Okri, 'What the Tapster Saw' (reading notes, Scalar)"

AUTHORS = [
A10(LM, MAJ, "1938", "2019", "Nabiac, New South Wales, Australia",
  "Australian; poet, anthologist and critic writing in English",
  "Australian poet of the bush, the suburb, the Aboriginal world and the English language itself, whose nearly "
  "thirty volumes made him the leading Australian poet of his generation",
  "Leslie Allan Murray was born on 17 October 1938 at Nabiac, on the north coast of New South Wales, and grew up on "
  "his family's dairy farm at Bunyah, in the Manning River valley, a landscape that remained the ground of his "
  "poetry. His mother died when he was twelve, an event that recurs in his work. He was educated at Taree High "
  "School and the University of Sydney, where he read German and English, and travelled to Europe in the late "
  "1950s. His first collection, The Ilex Tree (1965), was written with Geoffrey Lehmann; The Weatherboard "
  "Cathedral (1969), Lunch and Counter Lunch (1974), The Vernacular Republic (1976), Ethnic Radio (1977), The "
  "People's Otherworld (1983), The Daylight Moon (1987), Dog Fox Field (1990), Translations from the Natural "
  "World (1992), Subhuman Redneck Poems (1996, T. S. Eliot Prize), Conscious and Verbal (1999), Poems the Size of "
  "Photographs (2002), Fredy Neptune (1998, a verse novel), The Biplane Houses (2006), Taller When Prone (2010) and "
  "Waiting for the Past (2015) followed. He was a noted anthologist, editor of the journal Quadrant and a "
  "controversial essayist, and lived at Bunyah, where he returned in 1985, and later at Taree. He died on 29 April "
  "2019.",
  "Poetry: The Ilex Tree (1965, with Geoffrey Lehmann), The Weatherboard Cathedral (1969), Poems Against "
  "Economics (1972), Lunch and Counter Lunch (1974), The Vernacular Republic (1976), Ethnic Radio (1977), The "
  "Boys Who Stole the Funeral (1980), The People's Otherworld (1983), The Daylight Moon (1987), Dog Fox Field "
  "(1990), Translations from the Natural World (1992), Subhuman Redneck Poems (1996), Conscious and Verbal "
  "(1999), Poems the Size of Photographs (2002), The Biplane Houses (2006), Taller When Prone (2010) and Waiting "
  "for the Past (2015); the verse novels The Boys Who Stole the Funeral (1980) and Fredy Neptune (1998), and the "
  "Collected Poems (2018). Prose: The Peasant Mandarin (1978), Persistence in Folly (1984) and A Working Forest "
  "(1997).",
  "Long, rhythmically insistent free verse and loose stanza forms, with a strongly percussive, alliterative music "
  "and a taste for strange compounds and lists; a diction that moves between the demotic Australian and the "
  "ornate; narrative and satirical poems as well as lyrics; the 'translations from the natural world' in the "
  "voices of animals.",
  "The Australian landscape and the rural life of the Manning valley; the vernacular and the survival of "
  "Aboriginal culture; class, the suburbs and the 'barbecue of the ordinary'; religion, Catholicism and the "
  "sacramental; depression, illness and the body; the English language as a living, plural inheritance.",
  "The leading Australian poet of his generation and the only one to have won the T. S. Eliot Prize, Murray's work "
  "was central to the emergence of a distinctively Australian poetry in the 1970s and 1980s; his vernacular "
  "nationalism and his political essays made him a controversial public figure, but his best poems are among the "
  "most original in postwar English poetry.",
  bib_status="incomplete",
  bib_note="The collections are listed from Wikipedia, the contents of Collected Poems (2018) and general "
           "knowledge. Installment 10 records only the two Norton selections, 'Morse' (The People's Otherworld, "
           "1983) and 'Corniche' (Subhuman Redneck Poems, 1996); 'The Kitchen Grammars' (2006) is outside the "
           "period. The bibliography is therefore incomplete, and the verse novels and prose have no records.",
  ver="partially verified", sources=[W_LM, MUR_CP, MUR_ABR]),
A10(JB, MAJ, "1930", "2009", "Shanghai International Settlement, China",
  "English; novelist, short-story writer and essayist writing in English, resident at Shepperton from 1960",
  "English novelist of the 'inner space' and the disaster, who took science fiction into the terrain of "
  "psychology, consumer culture and the media, from The Drowned World to Crash and Empire of the Sun",
  "James Graham Ballard was born on 15 November 1930 in the Shanghai International Settlement, where his father "
  "managed a chemical company, and spent the war years in the Lunghua internment camp after the Japanese "
  "occupation of the city, an experience he later used in Empire of the Sun (1984). He was sent to England in "
  "1946, educated at The Leys School in Cambridge and read medicine at King's College, Cambridge, intending to "
  "become a psychiatrist, before leaving for London and working as an advertising copywriter and on a trade "
  "journal. His first stories appeared in New Worlds in the late 1950s, and The Wind from Nowhere (1961) and The "
  "Drowned World (1962) made his name as a writer of catastrophe fiction; The Drought (1965) and The Crystal "
  "World (1966) completed the sequence. The Atrocity Exhibition (1970), Crash (1973), Concrete Island (1974) and "
  "High-Rise (1975) turned to the 'inner space' of the media landscape and the eroticism of technology, while "
  "Empire of the Sun (1984) and The Kindness of Women (1991) returned to Shanghai. His later novels include "
  "Cocaine Nights (1996), Super-Cannes (2000) and Millennium People (2003). He died at Shepperton on 19 April "
  "2009.",
  "Novels: The Wind from Nowhere (1961), The Drowned World (1962), The Drought (1965), The Crystal World (1966), "
  "The Atrocity Exhibition (1970), Crash (1973), Concrete Island (1974), High-Rise (1975), The Unlimited Dream "
  "Company (1979), Hello America (1981), Empire of the Sun (1984), The Day of Creation (1987), Running Wild "
  "(1988), The Kindness of Women (1991), Rushing to Paradise (1994), Cocaine Nights (1996), Super-Cannes (2000), "
  "Millennium People (2003) and Kingdom Come (2006). Stories: The Voices of Time (1962), Billenium (1962), The "
  "Four-Dimensional Nightmare (1963), The Terminal Beach (1964), The Disaster Area (1967), The Overloaded Man "
  "(1967), Vermilion Sands (1971) and The Complete Short Stories (2001). Nonfiction: A User's Guide to the "
  "Millennium (1996) and Miracles of Life (2008).",
  "A cool, exact, medically precise prose, with a clinician's detachment from violence and sex; the imagery of "
  "drained pools, empty motorways, abandoned airports and flooded cities; the rejection of character psychology "
  "in favour of 'inner space'; the short story built as a sequence of tableaux; the late novels in a plainer, "
  "more conventional narrative mode.",
  "Catastrophe as revelation: the flood, the drought, the crystallising forest and the emptied city reveal what "
  "the society concealed; the psychology of the media, of celebrity and of violence (The Atrocity Exhibition, "
  "Crash); the erosion of the boundary between the human and the technological; childhood, imprisonment and "
  "survival (Empire of the Sun); the gated community and the pathology of affluence in the late novels.",
  "The most important British science-fiction writer of the postwar period and the one who did most to move the "
  "genre into the mainstream of literary fiction; the adjective 'Ballardian' has entered the dictionaries, and "
  "his catastrophe novels of the 1960s are now read as founding texts of climate fiction.",
  bib_status="incomplete",
  bib_note="The books are listed from Wikipedia and general knowledge, with the publication details of The Drowned "
           "World checked against its own article. Installment 10 records only the Norton selection, The Drowned "
           "World (1962), so the bibliography is incomplete; the stories, the later novels and the essays have no "
           "records, and the dates of first publication were not checked title by title.",
  ver="partially verified", sources=[W_JB, W_DW]),
A10(BH, SEC, "1937", "1986", "Pietermaritzburg, Natal, South Africa",
  "South African-born; short-story writer and novelist who lived in Botswana from 1964 and became a Botswana "
  "citizen in 1979, writing in English",
  "South African-born writer of Botswana whose novels and stories of Serowe, from When Rain Clouds Gather to A "
  "Question of Power, made her one of the most original voices of southern African fiction",
  "Bessie Amelia Emery Head was born on 6 July 1937 in Pietermaritzburg, Natal, the daughter of a white woman and a "
  "black man, and was raised in foster homes and then in a mission orphanage after her mother was committed to a "
  "mental hospital. She trained as a teacher at a mission college in Durban and taught in Natal and in the "
  "Cape, and worked as a journalist in Cape Town and Johannesburg, where she was associated with the Pan Africanist "
  "Congress and wrote for its paper. She left South Africa in 1964 on a one-way exit permit, taught in Serowe, in "
  "Bechuanaland (now Botswana), and settled there, writing in poverty and isolation. Her first novel, When Rain "
  "Clouds Gather, appeared in 1968, followed by Maru (1971) and A Question of Power (1973), the last a harrowing "
  "account of mental breakdown that made her reputation; The Collector of Treasures and Other Botswana Village "
  "Tales (1977) and Serowe: Village of the Rain Wind (1981) drew on the history and oral tradition of her adopted "
  "home, and her posthumous works include Tales of Tenderness and Power (1989), A Woman Alone (1990) and The "
  "Cardinals (1993). She became a Botswana citizen in 1979 and died in Serowe on 17 April 1986.",
  "Novels: When Rain Clouds Gather (1968), Maru (1971) and A Question of Power (1973). Stories: The Collector of "
  "Treasures and Other Botswana Village Tales (1977) and Tales of Tenderness and Power (1989, posthumous). "
  "Nonfiction and oral history: Serowe: Village of the Rain Wind (1981). Letters and journalism: A Woman Alone "
  "(1990) and A Gesture of Belonging (1991).",
  "A spare, translucent prose that moves without strain between realistic village narrative and visionary or "
  "hallucinated interior states; the short story built as a parable or a folk tale told by a narrator close to "
  "the community; direct speech in a Botswana idiom; a moral clarity that is never merely schematic.",
  "Racial and sexual oppression in southern Africa; the position of women in village society and their "
  "resistance (The Collector of Treasures); madness, spiritual crisis and the divided self (A Question of "
  "Power); drought, poverty and survival; exile, belonging and the possibility of a just community.",
  "One of the central writers of southern African fiction in English and, with Bessie Head's own account of "
  "mental illness, one of the first African novelists to write from inside a breakdown; her stories are widely "
  "anthologised and taught, and she is regarded as Botswana's most influential writer.",
  bib_status="incomplete",
  bib_note="The books are listed from Wikipedia and general knowledge; only the Norton selection, 'Looking for a "
           "Rain God' (in The Collector of Treasures, 1977), has a work record, so the bibliography is incomplete. "
           "The posthumous volumes were not checked title by title, and no text of the story was consulted beyond "
           "the synopsis cited in its record.",
  ver="partially verified", sources=[W_BH, HEAD_NOTE]),
A10(BO, SEC, "1959", None, "Minna, Nigeria",
  "Nigerian-born British; novelist, short-story writer, poet and essayist writing in English, resident in London "
  "from 1978",
  "Nigerian-born novelist of the spirit world and the Nigerian street, whose The Famished Road won the Booker Prize "
  "in 1991 and whose stories of the 1980s made him the leading inheritor of Tutuola's fabulous mode",
  "Ben Golden Emuobowho Okri was born on 15 March 1959 in Minna, in what is now Niger State, Nigeria, and grew up "
  "in Lagos and Ibadan, where his father, a clerk, moved the family; he has described a childhood of crowded "
  "compound life, of stories told by his mother and of the Nigerian civil war, which he witnessed as a child. He "
  "moved to England in 1978 and read comparative literature at the University of Essex, and published his first "
  "novel, Flowers and Shadows, in 1980, followed by The Landscapes Within (1981). The short-story collection "
  "Incidents at the Shrine (1986) and Stars of the New Curfew (1988) established his voice, and The Famished Road "
  "(1991), the first of a trilogy with Songs of Enchantment (1993) and Infinite Riches (1998), won the Booker "
  "Prize. Later work includes Astonishing the Gods (1995), Dangerous Love (1996), A Way of Being Free (1997), "
  "Starbook (2007), The Age of Magic (2008) and The Freedom Artist (2019), with poetry in An African Elegy (1992), "
  "Mental Fight (1999) and A Fire in My Head (2021). He was awarded the OBE in 2001 and knighted in 2023.",
  "Novels: Flowers and Shadows (1980), The Landscapes Within (1981), The Famished Road (1991), Songs of "
  "Enchantment (1993), Astonishing the Gods (1995), Infinite Riches (1998), Starbook (2007), The Age of Magic "
  "(2008) and The Freedom Artist (2019). Stories: Incidents at the Shrine (1986), Stars of the New Curfew (1988) "
  "and Prayer for the Living (2019). Poetry: An African Elegy (1992), Mental Fight (1999) and A Fire in My Head "
  "(2021). Essays: A Way of Being Free (1997) and A Time for New Dreams (2011).",
  "A dense, lyrical, incantatory prose that draws on Yoruba myth, the ghost story and the oral tale; a "
  "first-person narration poised between dream and street; catalogue, repetition and proverb; a refusal of the "
  "conventions of the realist novel in favour of the fabulous and the parabolic.",
  "The spirit world and its intrusion into the world of the living (The Famished Road); poverty, corruption and "
  "the exploitation of the poor in the Nigerian oil economy ('What the Tapster Saw'); childhood, hunger and "
  "survival; myth, prophecy and the artist's vocation; freedom, dreams and the possibility of transformation.",
  "The best-known African novelist of his generation in Britain, and the writer who carried Amos Tutuola's "
  "fabulous mode into the postmodern novel; the Booker Prize of 1991 made him an international figure, and his "
  "short stories of the 1980s are now read as early examples of what critics call 'petro-magic realism'.",
  bib_status="incomplete",
  bib_note="The books are listed from Wikipedia and general knowledge; only the Norton selection, 'What the Tapster "
           "Saw' (in Stars of the New Curfew, 1988), has a work record, so the bibliography is incomplete. The "
           "story collections' dates were checked against the cited study material, but the novels were not "
           "checked title by title.",
  ver="partially verified", sources=[W_BO, OKRI_SCALAR, OKRI_READ]),
A10(AR, MAJ, "1961", None, "Shillong, Assam, India",
  "Indian; novelist and political essayist writing in English",
  "Indian novelist and activist whose first novel, The God of Small Things (1997), won the Booker Prize and gave "
  "Indian writing in English one of its most widely read and formally distinctive books",
  "Suzanna Arundhati Roy was born on 24 November 1961 in Shillong, in Assam, the daughter of Mary Roy, a Syrian "
  "Christian teacher and women's rights campaigner from Kerala, and a Bengali Hindu tea planter; her parents "
  "separated when she was two, and she grew up with her mother and brother in Ayemenem, in Kerala, where the "
  "family ran a small factory and a pickle business, and where her mother founded a school. She trained as an "
  "architect at the School of Planning and Architecture in New Delhi, worked as a designer, and wrote the "
  "screenplays for the films In Which Annie Gives It Those Ones (1989) and Electric Moon (1992), and acted in "
  "Masay Sahib (1992). The God of Small Things, published in 1997, won the Booker Prize and became the "
  "best-selling book by a non-expatriate Indian author. Since then she has written chiefly political essays and "
  "books, including The End of Imagination (1998), The Algebra of Infinite Justice (2001), Power Politics (2001), "
  "War Talk (2003), An Ordinary Person's Guide to Empire (2004), Field Notes on Democracy (2009), Broken "
  "Republic (2011), Capitalism: A Ghost Story (2014), The Doctor and the Saint (2017) and Azadi (2020), and the "
  "novel The Ministry of Utmost Happiness (2017). She won the Sydney Peace Prize in 2004 and the PEN Pinter Prize "
  "in 2024, and is a leading campaigner on the Narmada dams, Kashmir and civil liberties.",
  "Fiction: The God of Small Things (1997) and The Ministry of Utmost Happiness (2017). Nonfiction: The End of "
  "Imagination (1998), The Cost of Living (1999), The Algebra of Infinite Justice (2001), Power Politics (2001), "
  "War Talk (2003), An Ordinary Person's Guide to Empire (2004), Public Power in the Age of Empire (2004), Field "
  "Notes on Democracy (2009), Broken Republic (2011), Walking with the Comrades (2011), Capitalism: A Ghost Story "
  "(2014), The Doctor and the Saint (2017) and Azadi (2020). Screenplays: In Which Annie Gives It Those Ones "
  "(1989) and Electric Moon (1992).",
  "A prose of great syntactic agility, moving between the child's-eye view and the retrospective narrator's "
  "irony; word-play, puns and typographic games (capital letters used as emphasis in the manner of "
  "children's speech); a non-linear chronology that withholds its catastrophe; the essay written in a direct, "
  "polemical, often sarcastic first person.",
  "The caste and class order of Kerala and the 'love laws' that punish transgression (The God of Small Things); "
  "childhood, twins and a divided family; the position of women and of the 'untouchable' in Indian society; "
  "colonial and post-colonial power, and the history of the Syrian Christian community; in the essays, "
  "globalisation, dams, nuclear weapons and the Indian state's violence.",
  "The God of Small Things was the most celebrated Indian novel in English of its decade, the first by an Indian "
  "woman to win the Booker Prize, and a book that changed the market for Indian writing in English. Roy has since "
  "become one of the most prominent writer-activists in the world, and her essays are central to the literature "
  "of globalisation and dissent.",
  bib_status="incomplete",
  bib_note="The books are listed from Wikipedia and general knowledge. Installment 10 records only the Norton "
           "selection, The God of Small Things (1997), for the extract the anthology prints under the title "
           "God's Own Country; the bibliography is therefore incomplete, and the essay collections have no "
           "records. The dates of the essays were not checked one by one.",
  ver="partially verified", sources=[W_AR]),
]

WORKS = [
W10("Morse", LM, "1983", "Poem", "minor",
  genres=G("Lyric Poetry", "Experimental Poetry"),
  themes=T("Land, place and regional belonging", "Language, writing and the limits of representation", "Technology, media and consumer society"),
  movements=M(INDIG, POSTCOL),
  overview="A poem from Les Murray's The People's Otherworld (1983) that takes the dots and dashes of the telegraph "
           "code and turns them into the sound of the Australian landscape, its birds and its distance.",
  content="A short poem built on the percussive rhythm of Morse code, in which the dashes and dots become the noise "
          "of the country - the birds, the wires, the empty distances - rather than a message to be decoded.",
  summary="'Morse' is one of Murray's performance poems, and its argument is in its sound: the code's long and short "
          "signals are made to beat out the noise of the Australian bush and of the telegraph line that crosses it. "
          "The poem treats the code as a vernacular, a way of talking that belongs to the country rather than to "
          "the engineers who laid the wire, and its rhythm is deliberately mechanical and hypnotic. The effect is "
          "of a landscape that has learned to speak in dots and dashes, and of a poetry that prefers the signal's "
          "sound to its meaning. Murray's interest in the colonial technologies of communication, and in the way "
          "they became part of the Australian idiom, is compressed into the poem's refusal to decode.",
  themes_text="The poem's subject is the sound of a place and the way a foreign technology is absorbed into a "
              "vernacular; the code's rhythm becomes an image of the country's distances and of the isolation "
              "the telegraph was built to cross. Murray's larger argument, that Australian English is a living "
              "and plural inheritance rather than a provincial dialect, is present in miniature.",
  structure="A short poem in a strongly stressed line, built on repetition and on the alternation of long and "
            "short units that imitates the code; it has no narrative development and its form is its meaning.",
  style="Percussive rhythms, heavy alliteration and a deliberately unmusical, mechanical beat; the diction is "
        "plain and the poem's music is in its stresses rather than its metre; Murray called himself tone-deaf, "
        "and the poem is a performance of sound over melody.",
  ctx="The People's Otherworld (Angus and Robertson, 1983) is the collection in which Murray's vernacular and "
      "narrative powers were at their height; 'Morse' belongs to the group of poems that the critic Peter "
      "Goldsworthy calls Murray's 'performance' mode, alongside 'The Smell of Coal Smoke' and the "
      "Buladelah-Taree Holiday Song Cycle.",
  sig="A frequently anthologised short poem and a standard example of Murray's sound-driven poetry; it is his first "
      "selection in the Norton Anthology.",
  canon="Minor canon",
  biblio="Published in The People's Otherworld (Sydney: Angus and Robertson, 1983) and collected in Collected Poems "
         "(2018). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on "
         "page 965.",
  notes="The collection is established from the contents of Collected Poems and from Peter Goldsworthy's review, "
        "which group 'Morse' with The People's Otherworld (1983); the poem's text was not read complete, so the "
        "record describes its method and makes no quotation.",
  ver="partially verified", sources=[MUR_CP, MUR_ABR, NAEL]),
W10("Corniche", LM, "1996", "Poem (short lyric)", "minor",
  genres=G("Lyric Poetry", "Confessional Poetry"),
  themes=T("Death, illness and mourning", "Madness, breakdown and confinement", "Identity, authenticity and the divided self"),
  movements=M(INDIG, POSTCOL),
  overview="A poem from Les Murray's Subhuman Redneck Poems (1996) in which the fear of dying turns into a longing for "
           "death as the only cure; one of the bleakest poems of his late middle age.",
  content="A short poem set in the pre-dawn hours, in which the speaker's dread of death becomes a desire for it, and "
          "the poem's argument turns on the discovery that the thing feared is also the only release.",
  summary="'Corniche' belongs to the group of poems in Subhuman Redneck Poems that Murray wrote out of depression, "
          "and its movement is the reverse of the elegy's: instead of mourning a death, it finds in the thought of "
          "death a kind of peace. The speaker, awake in the hours before dawn, follows the fear to its end and "
          "discovers that the fear has become a wish, and the poem's short lines and plain diction keep the "
          "argument from becoming a consolation. The title names a coast road, the kind of road that runs along a "
          "cliff edge, and the poem's position is that of someone driving between the sea and the drop. The poem "
          "is not a suicide note but an honest record of a state of mind, and Murray's later work returned to the "
          "subject of depression with the same refusal of comfort.",
  themes_text="The poem's subject is the mutability of feeling: the fear of death that drives the speaker becomes, by "
              "the end of the poem, a longing for it, and the poem traces that reversal without judging it. "
              "Depression is described from inside, as a condition in which the worst thing and the only cure are "
              "the same, and the poem's brevity keeps the reader in that moment rather than resolving it into "
              "either consolation or despair.",
  structure="A short poem in brief lines, with little narrative and a single turn from fear to longing; its form is "
            "the argument's movement, and the title provides the landscape the poem does not otherwise describe.",
  style="Plain, short-breathed lines with no ornament; the diction is ordinary and the tone level, so that the "
        "reversal arrives without rhetorical preparation; the poem's power is in what it withholds.",
  ctx="Subhuman Redneck Poems (Duffy and Snellgrove, 1996) won the T. S. Eliot Prize and is Murray's darkest "
      "collection, written in the period of his severe depression; 'Corniche' is one of the poems critics single "
      "out as among the most difficult and most honest in it.",
  sig="A key poem of Murray's darkest collection and a standard example of his late manner; it is his second "
      "selection in the Norton Anthology, and its treatment of depression is among the most discussed in his "
      "work.",
  canon="Minor canon",
  biblio="Published in Subhuman Redneck Poems (Sydney: Duffy and Snellgrove, 1996) and collected in Collected Poems "
         "(2018). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on "
         "page 966.",
  notes="The collection and the poem's subject are established from Peter Goldsworthy's review of Collected Poems, "
        "which discusses 'Corniche' and the pre-dawn poems of Subhuman Redneck Poems; the text was not read "
        "complete, so the record makes no quotation.",
  ver="partially verified", sources=[MUR_ABR, MUR_CP, NAEL]),
W10("The Drowned World", JB, "1962", "Novel", "major",
  genres=G("Science Fiction", "Apocalyptic Fiction", "Post-Apocalyptic Fiction"),
  themes=T("Nature, ecology and environmental crisis", "Alienation, absurdity and existential freedom", "Utopia, dystopia and imagined futures"),
  movements=M(NWAVE, "Contemporary Gothic"),
  overview="J. G. Ballard's second novel (1962), in which solar radiation has melted the polar ice caps and turned "
           "London into a tropical lagoon, and a biologist, Robert Kerans, chooses the drowned world and its "
           "Triassic pull over the work of restoring the old one.",
  content="A novel in which a small scientific team, marooned in the flooded ruins of London, tries to salvage "
          "what it can while the biologist Robert Kerans finds himself drawn by the heat, the reptiles and the "
          "triassic jungle that has replaced the city towards a regression into deep evolutionary time.",
  summary="The novel is set in a future, some decades after solar radiation has melted the ice caps and raised the "
          "seas, when the drowned cities of Europe have become lagoons and reefs. Robert Kerans, a biologist, is "
          "part of a small expedition surveying the drowned London; the heat is rising year by year, and the "
          "survivors live in the upper floors of the great buildings, diving into the submerged streets and "
          "hunting the giant reptiles and iguanas that have colonised the lagoon. Kerans, his colleague Bodkin "
          "and the soldier Riggs are joined by Beatrice Dahl, a wealthy and detached woman whose apartment on the "
          "water is the novel's centre of what remains of civilised life, and by Strangman, the leader of a gang "
          "of scavengers who drains the lagoon around the city to loot it. As the temperature climbs, Kerans "
          "begins to dream of the drowned world and to feel the pull of the Triassic past, and Bodkin, an older "
          "scientist who has studied the fossils of the sun, walks south into the jungle and is not seen again. "
          "When Strangman's men drain the lagoon and expose the city, Kerans sees the drowned world he loved "
          "destroyed, and after the water returns he refuses the expedition's plan to evacuate north and sets "
          "out southward after Bodkin, towards the sun, the reptiles and the lost evolutionary age. The novel "
          "ends with Kerans alone in the jungle, having chosen regression rather than recovery, and with the "
          "question of whether he is mad or has understood something the others cannot.",
  themes_text="The novel's central idea is that the catastrophe is not a disaster to be survived but a "
              "transformation to be accepted: the flood has returned the earth to its prehistoric state, and "
              "Kerans's dreams are the human mind responding to the same evolutionary pull. Ballard's 'inner "
              "space' is already at work here, since the drowned city is less a setting than a projection of "
              "the psyche, and the novel's refusal of the conventional adventure plot - there is no rescue, no "
              "rebuilding of civilisation - is its argument. The sun and the lagoon are narcotic, and the novel "
              "is ambivalent about them: the regression is both a liberation from the old social order and a "
              "surrender of everything that made Kerans a person. Read now, the book is also an early "
              "climate-fiction fable, in which the earth's warming is not reversed.",
  structure="A short novel in three parts, set almost entirely in the drowned London and its lagoon; the plot is a "
            "sequence of encounters and discoveries rather than a quest, and the final movement is westward and "
            "southward, away from the expedition's route home; the ending refuses the rescue that the earlier "
            "chapters seem to promise.",
  style="A cool, exact, descriptive prose, with the temperature and the light registered on every page; the "
        "imagery of drained swimming pools, submerged office blocks, giant reptiles and stagnant water; little "
        "dialogue and almost no interior monologue of the conventional kind; the science is delivered as "
        "observation rather than explanation.",
  ctx="The Drowned World appeared in shortened form in Science Fiction Adventures in January 1962 and in book form "
      "from Victor Gollancz in 1962; it belongs with The Drought (1965) and The Crystal World (1966) to the "
      "'ambiguous apocalypse' sequence of Ballard's early novels and to the New Wave of British science fiction, "
      "and it has since been read as a foundational text of climate fiction.",
  sig="The novel that established Ballard's reputation and the first of his catastrophe books; it is his selection "
      "in the Norton Anthology (printed as the extract 'The Causeways of the Sun'), and the record covers the "
      "whole novel. It is now read as a founding text of climate fiction as well as a key novel of the New Wave, "
      "and it gave the word 'Ballardian' its first clear reference.",
  canon="Major canon",
  biblio="First published in shortened form in Science Fiction Adventures (January 1962) and in book form by Victor "
         "Gollancz (London, 1962), with an American edition from Berkley Medallion. Norton prints an extract "
         "beginning on page 984; this record covers the whole novel.",
  crit="The Drowned World was praised at once by Kingsley Amis and Michael Moorcock for its imaginative power and "
       "literary ambition, and it has since become the founding text of the reading of Ballard as a writer of "
       "'inner space' rather than of gadgetry; critics group it with The Drought and The Crystal World as "
       "'ambiguous apocalypse' novels that reject the recovery plot, and later criticism has treated it as an "
       "important early work of climate fiction. Its place in the Norton Anthology, as the Ballard selection, has "
       "consolidated its standing as the most literary of his early books.",
  notes="The plot and the novel's critical placing follow Wikipedia's article on the book, which was read directly; "
        "the account of Kerans's decision and the ending follows that summary, and the text itself was not read "
        "complete.",
  ver="partially verified", sources=[W_DW, W_JB, NAEL]),
]

WORKS += [
W10("Looking for a Rain God", BH, "1977", "Short story", "significant",
  genres=G("Short Story", "Regional Fiction"),
  themes=T("Nature, ecology and environmental crisis", "Faith, doubt and the sacred", "Family, marriage and domestic life"),
  movements=M(AFR, SAAP),
  overview="A story from Bessie Head's The Collector of Treasures (1977): during a seven-year drought in Botswana, a "
           "family sacrifices two young girls to the rain god, the rain does not come, and the crime is found out.",
  content="A spare narrative of a village in drought, of Mokgobja and his son Ramadi's decision to perform an old "
          "rain-making sacrifice with Ramadi's two daughters, and of the discovery and punishment that follow.",
  summary="The story opens with the drought: the rains have failed for seven years, the harvests have been lost, and "
          "some of the villagers have hanged themselves rather than face the hunger. Mokgobja, an old man, and his "
          "son Ramadi take their family to plough a patch of land when a little rain comes, but the rain lasts "
          "only a fortnight and the women of the family begin to weep at night at the prospect of starvation. "
          "Mokgobja remembers an ancient ceremony, a sacrifice to the rain god, and he and Ramadi agree to it, "
          "taking the two little girls, Neo and Boseyong, out into the land and killing them. The rain does not "
          "come. The family returns to the village and the absence of the children is noticed; the police "
          "investigate, and Tiro, the girls' mother, breaks down and tells what happened. The story ends with "
          "Mokgobja and Ramadi sentenced to death for ritual murder, and with the narrator's flat statement that "
          "the family's hope of rain had been met by nothing. Head's method is to tell the story without "
          "sensationalism, so that the horror lies in the ordinariness of the decision and in the drought that "
          "made it conceivable.",
  themes_text="The story examines what extreme scarcity does to belief: the rain-making sacrifice is not presented "
              "as exotic superstition but as the last resource of people who have nothing else, and the old "
              "man's faith is shown to be as rational, in its own terms, as the women's weeping. Head refuses "
              "to make the family monstrous, and the story's judgement falls on the drought, on the poverty "
              "that leaves no alternative, and on the collision between an inherited ritual and the law that "
              "will punish it. The girls themselves are barely present, and their absence is the story's moral "
              "centre.",
  structure="A single continuous narrative, moving from the general description of the drought to the family's "
            "hopes, the sacrifice, the failure of the rain and the discovery; the point of view is close to the "
            "community rather than to any one character, and the ending delivers the legal consequence in a "
            "single flat sentence.",
  style="A plain, measured, almost biblical prose, with short declarative sentences and little metaphor; the "
        "narrative voice is that of a storyteller close to the village, using its idiom and its proverbs; the "
        "horror is conveyed by understatement and by the absence of commentary.",
  ctx="The Collector of Treasures and Other Botswana Village Tales (Heinemann, 1977) was written in Serowe, where "
      "Head lived from 1964, and draws on the oral history she had collected for Serowe: Village of the Rain "
      "Wind; the story's drought and ritual belong to the remembered life of rural Botswana, and it was "
      "published in the Heinemann African Writers Series.",
  sig="The best-known of Head's Botswana stories and one of the most widely taught African short stories in "
      "English; it is her selection in the Norton Anthology.",
  canon="Secondary canon",
  biblio="Published in The Collector of Treasures and Other Botswana Village Tales (London: Heinemann, 1977). A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 992.",
  notes="The plot follows the study notes read as a search extract, which agree with general knowledge on the "
        "drought, the sacrifice of Neo and Boseyong and the death sentences; the names and the ending were "
        "checked there, and the text was not read complete.",
  ver="partially verified", sources=[HEAD_NOTE, W_BH, NAEL]),
W10("What the Tapster Saw", BO, "1988", "Short story", "significant",
  genres=G("Short Story", "Experimental Fiction", "Satirical Fiction"),
  themes=T("Power, the state and surveillance", "Nature, ecology and environmental crisis", "Utopia, dystopia and imagined futures"),
  movements=M(AFR, MAGIC, POSTCOL),
  overview="The last story in Ben Okri's Stars of the New Curfew (1988): a palm-wine tapper falls from his tree and, "
           "in a week-long coma, sees the corruption, the oil wells and the violence of his country in a vision.",
  content="A first-person narrative in which the tapster, having fallen from a palm tree, drifts between this world "
          "and the next, witnessing oil companies destroying the forest, voices that beat him when he speaks, a "
          "rainbow snake in a river, and three turtles who talk with the authority of the powerful.",
  summary="The story begins in confusion - 'I had died. Not even I' - and follows the tapster's spirit as it leaves "
          "his body after a fall from a palm tree he has climbed every day for thirty years. In the vision the "
          "land is being destroyed by the oil companies: forests are cut down and blown up, the earth is opened "
          "and left with oil and animal bones spewing out of it, bridges and roads are ruined by unexploded "
          "bombs from an old war, travellers are killed, and people the tapster knows are executed by bullets "
          "'with their names on them'. A rainbow-coloured snake swims in a river and makes it clear and luminous; "
          "voices speak around him and beat him when he answers, giving him thoughts to replace the ones they "
          "have knocked out of him, such as 'the bigger mouth eats the smaller head'. Three turtles, one of them "
          "with the face of his herbalist friend, discuss the number of moons and stars with complete authority "
          "and complete ignorance. He meets a man who died reading the Bible upside down and recognises himself. "
          "At the end he wakes in his friend's house, where two turtles stand in a shrine in the corner, and he "
          "is left carrying a knowledge he cannot express.",
  themes_text="The story is a satire of the Nigerian oil economy written as a dream vision: the oil companies, the "
              "government and the voices that beat the tapster all belong to a system that destroys the land and "
              "punishes anyone who questions it, and the turtles' ignorant authority is the story's image of "
              "power without knowledge. Okri's method is to give the poor man's vision the authority of "
              "revelation, so that the reader sees what the tapster sees without the mediation of reportage, "
              "and the ending's silence - a truth that cannot be spoken - is itself a political statement about "
              "who is permitted to speak.",
  structure="A first-person narrative in a single continuous vision, with no chapter divisions and a dream logic "
            "that moves between scenes without transition; the frame is the fall and the waking, and the "
            "vision's material is organised by recurrence (the snake, the turtles, the voices) rather than by "
            "plot.",
  style="A dense, incantatory prose with the rhythms of oral narration; short sentences, repetition and "
        "catalogue; vivid, surreal imagery (the 'roseate' snake, the luminous river, the upside-down Bible); "
        "proverbs and aphorisms embedded in the narration; the first person is that of an uneducated man whose "
        "diction is nonetheless lyrical.",
  ctx="Stars of the New Curfew (Secker and Warburg, 1988) gathers stories of Lagos and the oil-producing Delta "
      "written in the 1980s, the decade of the Nigerian oil boom's collapse; 'What the Tapster Saw' draws on "
      "Amos Tutuola's The Palm-Wine Drinkard (1952) and has been read by critics as an early example of "
      "'petro-magic realism', the meeting of magical realism and the oil economy.",
  sig="The best known of Okri's short stories and a standard example of African magical realism; it is his "
      "selection in the Norton Anthology and the story through which his early fiction is usually introduced.",
  canon="Secondary canon",
  biblio="Published in Stars of the New Curfew (London: Secker and Warburg, 1988). A selection of The Norton "
         "Anthology of English Literature, 11th edition, vol. F, beginning on page 996.",
  notes="The plot follows the two Scalar project pages on the story read as search extracts, which quote its "
        "opening and describe the vision in detail and agree with each other; the text itself was not read "
        "complete, and the quotations are those printed in those pages.",
  ver="partially verified", sources=[OKRI_SCALAR, OKRI_READ, W_BO, NAEL]),
]

WORKS += [
W10("The God of Small Things", AR, "1997", "Novel", "major",
  genres=G("Literary Novel", "Historical Novel", "Family Saga"),
  themes=T("Family, marriage and domestic life", "Class, labour and social mobility", "Childhood, adolescence and coming of age"),
  movements=M(SAS, POSTCOL, MAGIC),
  overview="Arundhati Roy's first novel (1997), the story of twins Estha and Rahel in Ayemenem, Kerala, and of the "
           "'love laws' that punish the affair between their mother Ammu and the untouchable Velutha, told out of "
           "chronological order and moving towards its catastrophe.",
  content="A novel in which the twins, separated as children and reunited as adults, remember the events of 1969 - "
          "the visit of their English cousin Sophie Mol, the death by drowning that followed, and the police "
          "destruction of Velutha - and the family's history across three generations in Kerala.",
  summary="The novel is set mostly in Ayemenem, in Kerala, in two times: the present, when Rahel returns as an adult "
          "to the family house and finds her twin Estha silent and damaged, and 1969, when the two were seven "
          "years old. Their mother Ammu, divorced and living with her children in her parents' house, falls in "
          "love with Velutha, an untouchable carpenter and communist, and the affair is discovered by the family: "
          "Ammu's brother Chacko, her aunt Baby Kochamma, and the police, who beat Velutha nearly to death and "
          "blame him for the drowning of Sophie Mol, the English cousin who had come to stay with her mother "
          "Margaret and who dies in the river during the children's attempt to run away. The twins are separated "
          "after the crisis, Estha is sent to his father and stops speaking, Ammu dies alone in a hotel, and "
          "Rahel drifts through an unhappy marriage. The novel's narration circles these events, moving "
          "backwards and forwards between the 1960s, the 1970s and the 1990s and between the children's "
          "perceptions and the adult narrator's retelling, so that the catastrophe is known from the first pages "
          "and its causes are assembled gradually. The title is taken from a line about the 'God of Loss' and "
          "the 'God of Small Things', and the novel's subject is the way the small, ordinary details of a "
          "childhood carry the whole of a life.",
  themes_text="The novel's central subject is the 'love laws' that decide 'who should be loved, and how, and how "
              "much': the caste and class order of Kerala forbids Ammu's love for Velutha, and the family "
              "enforces it with a cruelty that is both social and personal. The twins' bond is the counter-law, "
              "a love that survives separation and damage, and the novel's method - the child's-eye view, the "
              "withheld chronology - makes the reader experience the adult world as the children did, as a "
              "series of incomprehensible prohibitions that turn violent. History is present throughout: "
              "communism in Kerala, the Syrian Christian community, the memory of colonialism, and the "
              "post-independence order in which the police can destroy an untouchable man without consequence.",
  structure="A non-linear narration in twenty-one chapters, moving between 1969, the 1970s and the 1990s, and "
            "between the twins' childhood perspective and an adult retrospective voice; information is "
            "withheld and revealed out of order, and the novel's central events are shown twice, from "
            "different points in time.",
  style="A prose of great syntactic invention, with word-play, portmanteau compounds and capitalised phrases "
        "that render the children's speech ('Being made to stand outside the door', 'the Orangedrink Lemondrink "
        "Man'); a lyricism that is precise about the material world (pickles, bananas, boats, the river) and "
        "ironic about the adult one; dialogue in a Kerala English with Malayalam cadences.",
  ctx="The God of Small Things was published by IndiaInk and Penguin in 1997 and won the Booker Prize in the same "
      "year; it drew on Roy's childhood in Ayemenem and on her mother's family, and its publication was a "
      "landmark in the international reception of Indian writing in English. Roy's subsequent career as a "
      "political essayist has shaped the reading of the novel's politics ever since.",
  sig="The most celebrated Indian novel in English of the 1990s and the first by an Indian woman to win the Booker "
      "Prize; it is Roy's selection in the Norton Anthology, printed as the extract 'God's Own Country', and the "
      "record covers the whole novel. Its opening sentence and its children's-eye narration are among the most "
      "widely quoted in postcolonial fiction in English.",
  canon="Major canon",
  biblio="Published in 1997 by IndiaInk (New Delhi) and Penguin Books (London). Norton prints an extract under the "
         "title 'God's Own Country', beginning on page 1002; this record covers the whole novel.",
  crit="The novel's reception has been divided between admiration for its language and structure and suspicion "
       "of its commercial success: critics have praised the child's-eye narration and the treatment of caste, and "
       "have debated whether its lyricism aestheticises the violence it describes. Roy's later political writing "
       "has made the novel's politics a continuing subject, and its place in the syllabus of postcolonial fiction "
       "is secure; The Ministry of Utmost Happiness (2017) was read against it as a return to fiction after twenty "
       "years of essays.",
  notes="The plot follows Wikipedia's article on Roy and general knowledge of the novel, whose chronology and "
        "catastrophe are widely summarised; the text was not read complete in this session, so the record's "
        "quotations are limited to the phrase 'love laws', which is the novel's own term, and to the reported "
        "title of the extract found in the Norton list.",
  ver="partially verified", sources=[W_AR, NAEL]),
]
