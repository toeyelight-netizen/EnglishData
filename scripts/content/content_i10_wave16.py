"""Installment 10, wave 16: new Norton authors, in the order of The Norton Anthology of English
Literature (11th edition, vol. F), from Grace Nichols to Chinua Achebe.

Eight authors are new to the database: Grace Nichols, Linton Kwesi Johnson, Doris Lessing,
A. K. Ramanujan, Thom Gunn, Derek Walcott, Ted Hughes and Chinua Achebe. Each has one record
per Norton selection first published 1946-2000; a long poem is recorded whole (Walcott's
Omeros, for the extract Norton prints). Only the Norton selections are recorded: no other books
by these authors are added in this wave.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, MIN, NAEL  # noqa: E402

GN = "Grace Nichols"
LKJ = "Linton Kwesi Johnson"
DL = "Doris Lessing"
AKR = "A. K. Ramanujan"
TG = "Thom Gunn"
DW = "Derek Walcott"
TH = "Ted Hughes"
CA = "Chinua Achebe"
CAR = "Caribbean Literature in English"
BBW = "Black British Writing and the Windrush Generation"
DUB = "Dub Poetry"
SPW = "Performance and Spoken-Word Poetry"
POSTCOL = "Postcolonial Literature"
MOV = "The Movement"
AFR = "African Literature in English"
SAS = "South Asian Literature in English"
INDIG = "Indigenous Writing in Australia, Canada and New Zealand"

W_GN = "Grace Nichols (Wikipedia)"
W_LKJ = "Linton Kwesi Johnson (Wikipedia)"
W_DL = "Doris Lessing (Wikipedia)"
W_AKR = "A. K. Ramanujan (Wikipedia)"
W_TG = "Thom Gunn (Wikipedia)"
W_DW = "Derek Walcott (Wikipedia)"
W_TH = "Ted Hughes (Wikipedia)"
W_CA = "Chinua Achebe (Wikipedia)"
W_OMEROS = "Omeros (Wikipedia)"
W_CP = "Civil Peace (Wikipedia)"
AKR_SEL = "A. K. Ramanujan, Selected Poetry (PDF text of the poems, jpellegrino.com)"
GUNN_READ = "Thom Gunn, 'From the Wave', 'Still Life', 'The Missing' (readingnorton.wordpress.com)"
GUNN_WORLD = "Thom Gunn, Collected Poems (WorldCat contents listing)"
NICH_READ = "Grace Nichols, 'Epilogue', 'The Fat Black Woman Goes Shopping', 'Wherever I Hang' (readingnorton.wordpress.com)"
NICH_SEL = "Grace Nichols, I Have Crossed an Ocean: Selected Poems (contents listing)"
LESSING_ENC = "To Room Nineteen by Doris Lessing, 1963 (The Encyclopedia of the Short Story, encyclopedia.com)"
WALCOTT_OX = "Walcott, Derek (Oxford Research Encyclopedia of Literature)"
WALCOTT_SEL = "Derek Walcott, Selected Poems (Barnes and Noble contents listing)"
WALCOTT_CON = "Myths of Identity in Derek Walcott's 'The Schooner Flight' (Mary C. Fuller, Connotations)"
LKJ_PULM = "'I came to poetry through politics': Linton Kwesi Johnson's Other Lives (Presses universitaires de la Méditerranée)"
HUGHES_TEXT = "Ted Hughes, 'Wind' (text, The Wondering Minstrels)"
CROW_THESIS = "A Dark Green Counterculture in Ted Hughes's Crow (independent thesis, DiVA)"
HUGHES_CP = "Ted Hughes, Collected Poems, ed. Paul Keegan (Faber contents listing)"
SOYINKA_LH = "On Wole Soyinka's Death and the King's Horseman (David Damrosch, Literary Hub)"
NAIP_UPS = "Displacing the Displacement Novel: V. S. Naipaul's In a Free State (Neel Mukherjee, The Paris Review)"
MUNRO_ATL = "Alice Munro's Dance of the Happy Shades, 50 Years Later (The Atlantic)"
HILL_PF = "Weight of the Word, Weight of the World (Poetry Foundation, on Geoffrey Hill)"
HILL_OUP = "Geoffrey Hill, Broken Hierarchies: Poems 1952-2012 (Oxford University Press contents)"

AUTHORS = [
A10(GN, SEC, "1950", None, "Georgetown, Guyana",
  "Guyanese; poet writing in English and in Guyanese Creole, resident in Britain since 1977",
  "Guyanese-born poet of the Black British diaspora whose poems in Guyanese nation language and standard English "
  "give voice to the Middle Passage, the immigrant woman's body and the divided life of the Caribbean in Britain",
  "Grace Nichols was born in Georgetown, British Guiana, in 1950 and grew up in a village on the coast before her "
  "family moved to the city when she was eight. She took a diploma in communications at the University of Guyana "
  "and worked as a teacher from 1967 to 1970 and then as a journalist and in government information services. She "
  "migrated to Britain in 1977, the year her first pamphlet appeared, and worked as a teacher and freelance "
  "journalist in London. Her first collection, I is a Long-Memoried Woman (1983), a sequence spoken by an enslaved "
  "African woman, won the Commonwealth Poetry Prize, was dramatised for BBC radio and was filmed. The Fat Black "
  "Woman's Poems (1984) followed, then Lazy Thoughts of a Lazy Woman (1989), Sunris (1996), which won the Guyana "
  "Prize, and Startling the Flying Fish (2006). She has written novels, including Whole of a Morning Sky (1986), "
  "and many books for children, and edited anthologies of Caribbean women's poetry. Her partner is the poet John "
  "Agard. She was awarded the Queen's Gold Medal for Poetry in 2021 and lives in Lewes, East Sussex.",
  "Poetry: I is a Long-Memoried Woman (1983), The Fat Black Woman's Poems (1984), Lazy Thoughts of a Lazy Woman "
  "(1989), Sunris (1996), Startling the Flying Fish (2006), Picasso, I Want My Face Back (2009), The Insomnia "
  "Poems (2017) and Passport to Here and There (2020); the retrospective I Have Crossed an Ocean: Selected Poems "
  "(2010). Fiction: Whole of a Morning Sky (1986). She has also published stories and poems for children and "
  "edited anthologies of Caribbean women's writing.",
  "Short lyrics in mixed standard English and Guyanese Creole, using the rhythms of calypso and of Caribbean "
  "speech; stanza forms kept simple and firm; a comic, mocking extravagance (the Fat Black Woman poems) set "
  "against the elegiac and mythic sequences of the Middle Passage; frequent word-play across the two languages.",
  "Slavery, the Middle Passage and the survival of African culture in the Caribbean; migration, exile and the "
  "divided self of the Black British woman; the body, appetite and beauty against the standards of the metropolis; "
  "the Caribbean landscape and its folklore; mothers and daughters.",
  "One of the central poets of Black British writing and a leading voice among the Caribbean writers who settled "
  "in Britain after the Windrush; her work is widely taught at GCSE and A level and has been recognised with the "
  "Commonwealth Poetry Prize (1983) and the Queen's Gold Medal for Poetry (2021).",
  bib_status="incomplete",
  bib_note="The list of books is taken from Wikipedia's bibliography and checked against the contents of I Have "
           "Crossed an Ocean: the collections I is a Long-Memoried Woman (Karnak House, 1983), The Fat Black "
           "Woman's Poems (Virago, 1984), Lazy Thoughts of a Lazy Woman (Virago, 1989), Sunris (Virago, 1996) and "
           "Startling the Flying Fish (2006), with the later Picasso, I Want My Face Back (Bloodaxe, 2009), The "
           "Insomnia Poems (2017) and Passport to Here and There (Bloodaxe, 2020). None of these books has a work "
           "record: installment 10 records only the three Norton selections, 'Epilogue' (1983), 'The Fat Black "
           "Woman Goes Shopping' (1984) and 'Wherever I Hang' (1989), so the bibliography of the author's books is "
           "incomplete. Her children's books were not checked title by title.",
  ver="partially verified", sources=[W_GN, NICH_SEL]),
A10(LKJ, SEC, "1952", None, "Chapelton, Clarendon, Jamaica",
  "Jamaican; dub poet and recording artist, resident in Britain since 1963, writing in Jamaican Creole and English",
  "Jamaican-born dub poet of Brixton whose verse in Jamaican Creole, performed over reggae and collected in slim "
  "books, is the most influential body of British performance poetry of the late twentieth century",
  "Linton Kwesi Johnson was born on 24 August 1952 in Chapelton, Clarendon, in rural Jamaica, and joined his "
  "mother in Brixton, south London, in 1963. He attended Tulse Hill School, joined the British Black Panther "
  "movement while still at school, and studied sociology at Goldsmiths College, graduating in 1973. He worked as "
  "the first paid library resources and education officer at the Keskidee Centre, the black arts centre in "
  "Islington, and wrote for the music papers. His poems appeared in the journal Race Today, which published his "
  "first collection, Voices of the Living and the Dead (1974), followed by Dread Beat an' Blood (Bogle-L'Ouverture, "
  "1975) and Inglan Is a Bitch (Race Today, 1980); he also recorded the poems with the dub band of the producer "
  "Dennis Bovell, on albums including Dread Beat an' Blood (1978), Forces of Victory (1979) and Bass Culture "
  "(1980). He founded LKJ Records in 1981. Mi Revalueshanary Fren: Selected Poems (Penguin Modern Classics, 2002) "
  "made him one of the few living poets in the series, and his essays were collected in Time Come (2023). He holds "
  "the Jamaican Order of Distinction, was elected a Fellow of the Royal Society of Literature in 2013, and won "
  "the PEN Pinter Prize in 2020.",
  "Poetry: Voices of the Living and the Dead (1974), Dread Beat an' Blood (1975), Inglan Is a Bitch (1980), "
  "Tings an Times: Selected Poems (1991) and Mi Revalueshanary Fren: Selected Poems (2002). Criticism and prose: "
  "Time Come: Selected Prose (2023). Records: Dread Beat an' Blood (1978), Forces of Victory (1979), Bass Culture "
  "(1980), LKJ in Dub (1980) and Making History (1983).",
  "Poems written for performance in Jamaican Creole ('nation language'), with a strong stress beat, refrain and "
  "repetition; the diction is a transcription of the spoken language, unpunctuated in places and shaped for the "
  "voice; the printed texts stand as poems but assume the bass line of reggae behind them.",
  "Racial oppression and police violence in Britain; the daily exploitation of Black labour ('Inglan Is a Bitch'); "
  "the Brixton uprisings and the Black British struggle of the 1970s and 1980s; migration and belonging; "
  "solidarity, mourning and memorial.",
  "The founder of British dub poetry and the model for a generation of performance poets, from Jean 'Binta' Breeze "
  "to Benjamin Zephaniah; his records carried the poems to a mass audience and his work is credited as a precursor "
  "of rap. 'Inglan Is a Bitch' became an emblem of Black British experience in the Thatcher years.",
  bib_status="incomplete",
  bib_note="Books, from Wikipedia and the OpenEdition study of his work: Voices of the Living and the Dead (1974), "
           "Dread Beat an' Blood (Bogle-L'Ouverture, 1975), Inglan Is a Bitch (Race Today, 1980), Tings an Times "
           "(1991) and Mi Revalueshanary Fren (Penguin, 2002), with the prose collection Time Come (2023). Only "
           "the Norton selection, 'Inglan Is a Bitch' (1980), has a work record, so the bibliography is "
           "incomplete; the albums were not checked title by title and have no records.",
  ver="partially verified", sources=[W_LKJ, LKJ_PULM]),
A10(DL, MAJ, "1919", "2013", "Kermanshah, Persia (now Iran)",
  "British (born in Persia, raised in Southern Rhodesia); novelist, short-story writer and essayist",
  "Nobel laureate and one of the great novelists of postwar Britain, whose sequence of novels and stories from The "
  "Grass Is Singing to The Golden Notebook and the Canopus in Argos series tested the forms of realism, "
  "autobiography and speculative fiction against the politics of gender, race and empire",
  "Doris May Tayler was born on 22 October 1919 in Kermanshah, Persia, where her father, a former bank clerk "
  "crippled in the First World War, worked for the Imperial Bank of Persia; her mother had been a nurse. The "
  "family moved to Southern Rhodesia in 1925 and she grew up on a farm near Salisbury, educated at a convent "
  "school and then, briefly, in Salisbury, leaving school at fourteen. She married Frank Wisdom in 1939, had two "
  "children, and divorced in 1943; a second marriage, to the German communist Gottfried Lessing, ended in 1949. "
  "She had joined the Communist Party in Rhodesia and brought the manuscript of her first novel to London in 1949. "
  "The Grass Is Singing appeared in 1950, followed by the five novels of Children of Violence (1952-1969), The "
  "Golden Notebook (1962), Briefing for a Descent into Hell (1971), the five Canopus in Argos: Archives novels "
  "(1979-1983), The Good Terrorist (1985), The Fifth Child (1988) and, late, Love, Again (1996) and Alfred and "
  "Emily (2008). She wrote more than seventy books, including the stories of African Stories, A Man and Two Women "
  "and To Room Nineteen, the memoir Under My Skin (1994) and the essays of A Small Personal Voice and Prisons We "
  "Choose to Live Inside. She was awarded the David Cohen Prize in 2001 and the Nobel Prize in Literature in 2007. "
  "She died in London on 17 November 2013.",
  "Novels: The Grass Is Singing (1950), Children of Violence (Martha Quest, 1952; A Proper Marriage, 1954; A Ripple "
  "from the Storm, 1958; Landlocked, 1965; The Four-Gated City, 1969), The Golden Notebook (1962), Briefing for a "
  "Descent into Hell (1971), The Summer Before the Dark (1973), The Memoirs of a Survivor (1974), Canopus in "
  "Argos: Archives (Shikasta, 1979; The Marriages Between Zones Three, Four and Five, 1980; The Sirian "
  "Experiments, 1981; The Making of the Representative for Planet 8, 1982; Documents Relating to the Sentimental "
  "Agents in the Volyen Empire, 1983), The Diary of a Good Neighbour (1983, as Jane Somers), If the Old Could "
  "(1984), The Good Terrorist (1985), The Fifth Child (1988), Love, Again (1996), Mara and Dann (1999), Ben, in "
  "the World (2000), The Sweetest Dream (2001), The Cleft (2007) and Alfred and Emily (2008). Stories: This Was "
  "the Old Chief's Country (1951), Five (1953), The Habit of Loving (1957), A Man and Two Women (1963), African "
  "Stories (1964), The Story of a Non-Marrying Man (1972), To Room Nineteen: Collected Stories Volume One (1978) "
  "and The Temptation of Jack Orkney (1978). Nonfiction: Going Home (1957), In Pursuit of the English (1960), "
  "Particularly Cats (1967), A Small Personal Voice (1974), Prisons We Choose to Live Inside (1987), The Wind "
  "Blows Away Our Words (1987), African Laughter (1992) and Under My Skin (1994).",
  "From the strict realism of the early African novels and stories to the four-column notebook of The Golden "
  "Notebook, Lessing kept changing form: documentary realism, interior monologue, Sufi allegory, space fiction, "
  "horror and late fable. The prose is plain and fast, with a strong narrative pull, and she uses the short story "
  "as a clinical instrument for exposing the ordinary arrangements of marriage and class.",
  "The position of women, marriage and the search for a free self (the 'free women' of The Golden Notebook, Susan "
  "Rawlings in 'To Room Nineteen'); colonialism and racial guilt in southern Africa; communism and political "
  "disillusion; madness and breakdown as the price of conformity; the survival of the species (the Canopus "
  "novels, The Memoirs of a Survivor); Sufism and the idea of a higher order.",
  "The most important British novelist of the second half of the twentieth century to write from a colonial "
  "background, and with The Golden Notebook a founding text of the second wave of feminism, although Lessing "
  "resisted the label. The Nobel citation praised 'that epicist of the female experience, who with scepticism, "
  "fire and visionary power has subjected a divided civilisation to scrutiny'.",
  bib_status="incomplete",
  bib_note="The list of books is taken from Wikipedia and from general knowledge and has not been checked title by "
           "title against a bibliography; the dates are those of first British publication. Installment 10 records "
           "only the Norton selection, 'To Room Nineteen' (1963), so the author's bibliography is incomplete. The "
           "five volumes of Children of Violence are listed with their individual titles, but with no work records.",
  ver="partially verified", sources=[W_DL, LESSING_ENC]),
A10(AKR, SEC, "1929", "1993", "Mysore, Kingdom of Mysore (now Karnataka), India",
  "Indian; poet, translator, linguist and folklorist, professor at the University of Chicago from 1962",
  "Indian poet and scholar who wrote a small, exact body of English poems on family, body and memory and "
  "transformed the study and translation of classical Tamil and Kannada into English",
  "Attipate Krishnaswami Ramanujan was born in Mysore on 16 March 1929, the son of a professor of mathematics and "
  "astrologer, and was educated at Marimallappa's High School and the Maharaja College of Mysore, where he read "
  "English. He taught English at colleges in Quilon, Belgaum and Baroda, and went in 1959 to Indiana University as "
  "a Fulbright scholar, taking a doctorate in linguistics in 1963. In 1962 he joined the University of Chicago, "
  "where he spent the rest of his career in the departments of South Asian Languages and Civilizations and of "
  "Linguistics and on the Committee on Social Thought, becoming the William E. Colvin Professor. His first "
  "collection, The Striders (1966), was followed by Relations (1971), Selected Poems (1976) and Second Sight "
  "(1986); The Collected Poems appeared in 1995, with poems for a further volume, The Black Hen. As a translator "
  "and scholar he published The Interior Landscape: Love Poems from a Classical Tamil Anthology (1967), Speaking "
  "of Siva (1973), Hymns for the Drowning (1981), Poems of Love and War (1985), Folktales from India (1991) and, "
  "with Velcheru Narayana Rao and David Shulman, When God Is a Customer (1994); his essays include 'Is There an "
  "Indian Way of Thinking?' (1990) and 'Three Hundred Ramayanas' (1991). He was awarded the Padma Shri in 1976 and "
  "a MacArthur Fellowship in 1983. He died in Chicago on 13 July 1993, of a reaction to anaesthesia before "
  "surgery; the Sahitya Akademi Award came posthumously, in 1999, for The Collected Poems.",
  "Poetry: The Striders (London: Oxford University Press, 1966), Relations (1971), Selected Poems (1976), Second "
  "Sight (1986) and The Collected Poems (1995, with The Black Hen). Translations and studies: The Interior "
  "Landscape (1967), Speaking of Siva (1973), Hymns for the Drowning (1981), Poems of Love and War (1985), "
  "Folktales from India (1991) and When God Is a Customer (1994). Essays: 'Is There an Indian Way of Thinking?' "
  "(1990) and 'Three Hundred Ramayanas' (1991).",
  "Short free-verse lyrics in a spare, exact, often epigrammatic English; a poetry of lists, definitions and "
  "catalogues ('Elements of Composition' composes the self out of chemical elements); colloquial speech as a "
  "dramatic resource; the classical Tamil and Kannada metres of his translations carried over into his own line.",
  "Family resemblance and inheritance (the father's signature on a stranger's face); the body as a compound of "
  "earth, air, fire and water; the divided self of the Indian who lives in two languages; death, memory and the "
  "minute particulars of ordinary life; folklore and myth as living structures.",
  "The founding figure of Indian English poetry's second generation, who made the Indian-English lyric out of "
  "speech rather than imperial rhetoric; as a translator he changed the English reading of classical Tamil, and "
  "as a folklorist he helped establish the study of Indian oral narrative.",
  bib_status="incomplete",
  bib_note="The books are listed from Wikipedia and from the Oxford University Press and Selected Poetry "
           "materials, and checked against the contents of The Striders (1966) and Second Sight (1986). Only the "
           "two Norton selections, 'Self-Portrait' (1966) and 'Elements of Composition' (1986), have work "
           "records, so the bibliography is incomplete; the translations and scholarly books have no records, "
           "and the posthumous The Black Hen was not checked in detail.",
  ver="partially verified", sources=[W_AKR, AKR_SEL]),
A10(TG, MAJ, "1929", "2004", "Gravesend, Kent, England",
  "English; poet resident in the United States from 1954, writing in English",
  "English poet of The Movement who moved to California, wrote some of the finest formal verse of his generation "
  "and then, in The Man with Night Sweats, the defining English elegies of the AIDS epidemic",
  "Thomson William Gunn was born on 29 August 1929 in Gravesend, Kent, the son of two journalists; his parents "
  "divorced when he was ten and his mother, who had taught him to read poetry, killed herself when he was a "
  "teenager. He was educated at University College School in Hampstead and read English at Trinity College, "
  "Cambridge, graduating in 1953. His first collection, Fighting Terms, appeared in 1954 from the Fantasy Press, "
  "and in the same year he moved to the United States to teach at Stanford and to be with Michael Kitay, his "
  "partner for the rest of his life. He taught at Berkeley from 1958 to 1966 and again from 1973 to 2000. The "
  "Sense of Movement (1957) confirmed him as a poet of The Movement, but Touch (1967), with its free verse and its "
  "frank poems of gay life, began the change that Moly (1971), Jack Straw's Castle (1976) and The Passages of Joy "
  "(1982) carried through. The Man with Night Sweats (1992), written as his friends died of AIDS, won the Lenore "
  "Marshall Poetry Prize, and Boss Cupid (2000) was his last collection. He also published two books of essays, "
  "The Occasions of Poetry (1982) and Shelf Life (1993), and received the David Cohen Prize in 2003. He died in "
  "San Francisco on 25 April 2004.",
  "Poetry: Fighting Terms (1954), The Sense of Movement (1957), My Sad Captains and Other Poems (1961), Touch "
  "(1967), Moly (1971), Jack Straw's Castle (1976), The Passages of Joy (1982), The Man with Night Sweats (1992) "
  "and Boss Cupid (2000); Selected Poems 1950-1975 (1979) and Collected Poems (1993). Prose: The Occasions of "
  "Poetry (1982) and Shelf Life (1993).",
  "Early poems in tight stanza forms and strict metre, with a clipped, muscular syntax and a taste for the "
  "dramatic situation; the later work opens into syllabics and free verse without losing its measure; the AIDS "
  "elegies return to plain quatrains and iambic pentameter; a persistent concern with the body, surfaces and "
  "contact.",
  "Energy, violence and the will (the early poems of motorcycles, gangs and soldiers); drug-taking, sex and the "
  "bohemian life of San Francisco; friendship, loss and the AIDS epidemic (The Man with Night Sweats); balance, "
  "surfing and the discipline of form as an image of how to live; the meeting of English and American poetry.",
  "The most formally accomplished poet of The Movement after Larkin, and the one who remade himself most "
  "radically; The Man with Night Sweats is the central book of AIDS elegies in English and is credited with "
  "restoring poetry to a public role in the crisis.",
  bib_status="incomplete",
  bib_note="Books, from Wikipedia and the WorldCat contents of Collected Poems: Fighting Terms (1954), The Sense of "
           "Movement (1957), My Sad Captains and Other Poems (1961), Touch (1967), Moly (1971), Jack Straw's "
           "Castle (1976), The Passages of Joy (1982), The Man with Night Sweats (1992) and Boss Cupid (2000). "
           "Installment 10 records only the five Norton selections ('Black Jackets' and 'My Sad Captains', 1961; "
           "'From the Wave', 1971; 'Still Life' and 'The Missing', 1992), so the bibliography is incomplete; the "
           "essay collections have no records.",
  ver="partially verified", sources=[W_TG, GUNN_WORLD]),
A10(DW, MAJ, "1930", "2017", "Castries, Saint Lucia",
  "Saint Lucian; poet and playwright writing in English and Saint Lucian Creole, resident for long periods in "
  "Trinidad and the United States",
  "Saint Lucian poet and playwright, Nobel laureate, who made the Caribbean archipelago the matter of an epic "
  "poetry in English and Creole, from In a Green Night to Omeros",
  "Derek Alton Walcott was born on 23 January 1930 in Castries, Saint Lucia, the son of Warwick Walcott, a civil "
  "servant and sometime watercolourist who died when Derek was a year old, and Alix Maarlin, a teacher who ran a "
  "school in their house and recited poetry to her children. A twin, he was educated at Saint Mary's College in "
  "Castries and at the University College of the West Indies in Jamaica, taking a degree in 1953. He published his "
  "first poems in a private pamphlet at eighteen, founded the Saint Lucia Arts Guild in 1950, and made his name "
  "with the play Henri Christophe (1950) and the collection In a Green Night: Poems 1948-1960 (1962). He lived "
  "and taught in Trinidad from 1959 to 1976, founded the Trinidad Theatre Workshop in 1959 and wrote the plays of "
  "Dream on Monkey Mountain and Other Plays (1970); his poetry went on through The Castaway (1965), The Gulf "
  "(1969), Another Life (1973), Sea Grapes (1976), The Star-Apple Kingdom (1979), The Fortunate Traveller (1981) "
  "and Midsummer (1984) to the epic Omeros (1990), which many critics regard as his masterpiece. He was professor "
  "of poetry and creative writing at Boston University from 1981 to 2007. He received the Nobel Prize in "
  "Literature in 1992, the T. S. Eliot Prize in 2011 for White Egrets, and died at Cap Estate, Saint Lucia, on 17 "
  "March 2017.",
  "Poetry: 25 Poems (1948), Epitaph for the Young (1949), Poems (1951), In a Green Night (1962), Selected Poems "
  "(1964), The Castaway (1965), The Gulf (1969), Another Life (1973), Sea Grapes (1976), The Star-Apple Kingdom "
  "(1979), The Fortunate Traveller (1981), Midsummer (1984), The Arkansas Testament (1987), Omeros (1990), The "
  "Bounty (1997), Tiepolo's Hound (2000), The Prodigal (2004), Selected Poems (2007) and White Egrets (2010). "
  "Plays: Henri Christophe (1950), The Sea at Dauphin (1954), Dream on Monkey Mountain (1970), The Joker of "
  "Seville and O Babylon! (1978) and Remembrance and Pantomime (1980). Essays: What the Twilight Says (1998).",
  "Long, meditative, densely metaphorical poems in a syntactically elaborate English, set against the plain "
  "vernacular speech of Creole characters (Shabine, Achille); the hexameters and terza rima of Omeros; a habit of "
  "reading the Caribbean landscape through Homer, Dante and the Bible without letting the classical frame master "
  "it; the poet as painter, making and unmaking his island.",
  "Colonial history and the Middle Passage; the divided self of the Caribbean artist ('I have Dutch, nigger, and "
  "English in me, and either I'm nobody, or I'm a nation'); the sea, the fishermen and the landscape of Saint "
  "Lucia; exile and return; love, age and mortality (White Egrets); the vocation of poetry itself.",
  "The foremost poet of the anglophone Caribbean, who with Omeros gave the region its epic and in doing so "
  "reopened the epic as a living form for postcolonial writing; Nobel laureate in 1992 and the model for two "
  "generations of Caribbean poets.",
  bib_status="incomplete",
  bib_note="Books, from Wikipedia and the Oxford Research Encyclopedia, with the contents of Selected Poems: the "
           "collections from 25 Poems (1948) to White Egrets (2010) and the main plays. Installment 10 records "
           "only the four Norton selections, 'A Far Cry from Africa' (collected 1962), 'The Schooner Flight' "
           "(1979), 'The Season of Phantasmal Peace' (1981) and Omeros (1990), so the bibliography is incomplete; "
           "the plays have no records and the date of first publication of 'A Far Cry from Africa' is given as "
           "1962, the date of the collection.",
  ver="partially verified", sources=[W_DW, WALCOTT_OX]),
A10(TH, MAJ, "1930", "1998", "Mytholmroyd, Yorkshire, England",
  "English; poet, translator and children's writer, Poet Laureate 1984-1998",
  "English poet of the animal and the elemental, Poet Laureate from 1984, whose sequences Wodwo and Crow and the "
  "late Birthday Letters changed the sound of postwar English verse",
  "Edward James Hughes was born on 17 August 1930 at Mytholmroyd, in the Calder Valley of West Yorkshire, the "
  "youngest of the three children of Edith Farrar and William Henry Hughes, a joiner who had survived the First "
  "World War and ran a shop in the village. The family moved to Mexborough, in South Yorkshire, when he was seven, "
  "and the landscape of millstone grit and moorland of his childhood remained the ground of his poetry. He read "
  "English at Pembroke College, Cambridge, where he met Sylvia Plath, whom he married in 1956; they lived in the "
  "United States and then in Devon, and she killed herself in 1963. His first collection, The Hawk in the Rain "
  "(1957), won the New York Poetry Center's first publication award and made his name; Lupercal (1960) and Wodwo "
  "(1967) followed, and Crow (1970), the sequence of poems about a trickster bird, became his most influential "
  "book. He wrote the radio play Under Milk Wood's successor in his own idiom, the children's book The Iron Man "
  "(1968), and many volumes of translations and of poems for children; Gaudete (1977), Cave Birds (1978), Moortown "
  "(1979) and River (1983) came before he was appointed Poet Laureate in 1984. His later books include Flowers and "
  "Insects (1986), Wolfwatching (1989), the Ovid translations of Tales from Ovid (1997) and Birthday Letters "
  "(1998), the poems to Plath. He died in London on 28 October 1998.",
  "Poetry: The Hawk in the Rain (1957), Lupercal (1960), Wodwo (1967), Crow (1970), Gaudete (1977), Cave Birds "
  "(1978), Moortown (1979), River (1983), Flowers and Insects (1986), Wolfwatching (1989), Rain-Charm for the "
  "Duchy (1992), New Selected Poems 1957-1994 (1995), Tales from Ovid (1997) and Birthday Letters (1998); "
  "Collected Poems, ed. Paul Keegan (2003). Plays and prose: The Iron Man (1968), Seneca's Oedipus (1969), "
  "Shakespeare and the Goddess of Complete Being (1992) and Winter Pollen (1994).",
  "A poetry of hard stresses and dense consonantal sound, built on the cadence of Anglo-Saxon and of Hughes's "
  "Yorkshire speech; violent, exact imagery of animals, weather and machinery; repetitive, chant-like sequences "
  "in Crow and Cave Birds; the late poems in Birthday Letters plainer, quieter and more colloquial.",
  "The violence and energy of the natural world (hawks, pike, wind, the moor); the brute fact of animal "
  "existence as a rebuke to human consciousness; myth, folklore and the occult (Crow, Cave Birds, Gaudete); the "
  "First World War and the Yorkshire landscape of his childhood (Moortown, Remains of Elmet); marriage, "
  "bereavement and memory (Birthday Letters).",
  "The dominant English poet of his generation and, as Poet Laureate from 1984, the public face of poetry in "
  "Britain for fourteen years; Crow and the animal poems changed the register of postwar English verse, and "
  "Birthday Letters became one of the best-selling and most discussed volumes of poetry of the century.",
  bib_status="incomplete",
  bib_note="Books, from Wikipedia, the Faber Collected Poems contents and general knowledge: the collections from "
           "The Hawk in the Rain (1957) to Birthday Letters (1998), with the plays and prose. Installment 10 "
           "records only the six Norton selections ('Wind', 1957; 'Pike', 1960; 'Out' and 'Theology', 1967; "
           "'Crow's Last Stand' and 'Crow Tyrannosaurus', 1970), so the bibliography is incomplete; the books "
           "have no records and the children's books were not checked.",
  ver="partially verified", sources=[W_TH, HUGHES_CP]),
A10(CA, MAJ, "1930", "2013", "Ogidi, Anambra, colonial Nigeria",
  "Nigerian; novelist, poet, critic and essayist writing in English",
  "Nigerian novelist whose Things Fall Apart gave modern African literature its founding book and whose later "
  "fiction and essays carried the argument about the African writer, colonialism and the English language",
  "Albert Chinualumogu Achebe was born on 16 November 1930 in Ogidi, in the Igbo country of eastern Nigeria, the "
  "son of Isaiah Okafo Achebe, a teacher and evangelist of the Church Missionary Society, and Janet Anaenechi "
  "Iloegbunam; he grew up between the mission and the traditional religion of his grandfather's generation. He "
  "was educated at the Government College in Umuahia and at the University College, Ibadan, where he read English "
  "and became critical of the way Western literature represented Africa. He taught briefly and joined the Nigerian "
  "Broadcasting Service in Lagos in 1954; Things Fall Apart appeared in 1958, followed by No Longer at Ease "
  "(1960), Arrow of God (1964) and A Man of the People (1966). He was a founder and the first editor of the "
  "Heinemann African Writers Series. During the Biafran war (1967-1970) he supported Biafran independence and "
  "worked for its cause abroad; the poems of Beware, Soul Brother (1971) and the stories of Girls at War (1972) "
  "came out of the war, and his essay collection Morning Yet on Creation Day (1975) includes 'The Novelist as "
  "Teacher' and his reply to Conrad, 'An Image of Africa' (1975). A car crash in 1990 left him partly paralysed "
  "and he moved to the United States, teaching at Bard College and, from 2009, at Brown University. Anthills of "
  "the Savannah (1987) was his last novel. He won the Man Booker International Prize in 2007 and died in Boston on "
  "21 March 2013.",
  "Novels: Things Fall Apart (1958), No Longer at Ease (1960), Arrow of God (1964), A Man of the People (1966) and "
  "Anthills of the Savannah (1987). Stories: The Sacrificial Egg (1962), Girls at War and Other Stories (1972) "
  "and African Short Stories (1985, edited with C. L. Innes). Poetry: Beware, Soul Brother (1971) and "
  "Collected Poems (2004). Essays: Morning Yet on Creation Day (1975), Hopes and Impediments (1988), The "
  "Education of a British-Protected Child (2009) and There Was a Country (2012). Children's books: Chike and the "
  "River (1966), How the Leopard Got His Claws (1972) and The Flute (1977).",
  "A plain, measured English that carries the rhythm and idiom of Igbo speech, built out of proverbs, "
  "folk-tales and the cadences of the King James Bible; an ironic narrative manner that lets a community's own "
  "language judge its actions; the mature novels combine a large historical span with a tight, dramatic scene; "
  "the stories of the war are short, bare and unsparing.",
  "The collision of Igbo tradition and colonial Christianity (Things Fall Apart); the corruption and "
  "disillusionment of independence (No Longer at Ease, A Man of the People); the Biafran war and its aftermath "
  "(Girls at War, 'Civil Peace'); the responsibility of the African writer and the politics of language; "
  "masculinity, gender and the exercise of power in the Igbo world.",
  "The founding novel of modern African literature in English, translated into more than fifty languages and "
  "taught across the world; Achebe is called the father of modern African writing, a title he rejected, and his "
  "essays on Conrad and on the African writer set the terms of the postcolonial debate about the English "
  "language and the African novel.",
  bib_status="incomplete",
  bib_note="Books, from Wikipedia's list and general knowledge: the five novels, the story collections, the poetry "
           "and essay collections and the children's books listed. Installment 10 records only the Norton "
           "selection, 'Civil Peace' (1971), so the bibliography is incomplete; the novels, which would have "
           "their own records in a complete bibliography of the author, are not recorded here, and the dates of "
           "the essay collections were not checked title by title.",
  ver="partially verified", sources=[W_CA, W_CP], alt=["Albert Chinualumogu Achebe"]),
]

VSN = "V. S. Naipaul"
WS = "Wole Soyinka"
CC = "Caryl Churchill"
SH = "Seamus Heaney"
W_VSN = "V. S. Naipaul (Wikipedia)"
W_WS = "Wole Soyinka (Wikipedia)"
W_CC = "Caryl Churchill (Wikipedia)"
W_TG_PLAY = "Top Girls (Wikipedia)"
W_SH = "Seamus Heaney (Wikipedia)"
SH_WORKS = "Seamus Heaney: Works (Ricorso bibliography)"
SH_READ = "Seamus Heaney's principal poems (reading site, irisharoundtheworld)"
SH_HR = "100 Poems by Seamus Heaney (Harvard Review)"
NAIP_PR = "Displacing the Displacement Novel: V. S. Naipaul's In a Free State (Neel Mukherjee, The Paris Review)"
SOY_LH = "On Wole Soyinka's Death and the King's Horseman (David Damrosch, Literary Hub)"
CLEAR_READ = "Seamus Heaney, 'Clearances' (reading site, fawbie.info)"
NYRB_HAW = "Second Thoughts (New York Review of Books, on Heaney's The Haw Lantern)"

AUTHORS += [
A10(VSN, MAJ, "1932", "2018", "Chaguanas, Trinidad",
  "Trinidadian-born British; novelist, travel writer and essayist writing in English",
  "Trinidadian-born Nobel laureate whose novels of Trinidad, Africa, India and England, from A House for Mr Biswas to "
  "The Enigma of Arrival, and whose travel books made him the century's most exact and most contested chronicler of "
  "displacement",
  "Vidiadhar Surajprasad Naipaul was born on 17 August 1932 in Chaguanas, Trinidad, into a family of Indian "
  "brahmin descent; his father, Seepersad Naipaul, was a journalist and short-story writer, and the household's "
  "poverty and his father's ambitions are the matter of the early books. He won a scholarship to Queen's Royal "
  "College in Port of Spain and another, in 1950, to University College, Oxford, where he read English; he "
  "graduated in 1953 and lived in London from 1954, writing for the BBC Caribbean Service and reviewing. His first "
  "three novels, The Mystic Masseur (1957), The Suffrage of Elvira (1958) and Miguel Street (1959), were comedies "
  "of Trinidadian life; A House for Mr Biswas (1961) made his name. A visit to India in 1962 produced An Area of "
  "Darkness (1964), the first of the travel books that include The Middle Passage (1962), The Loss of El Dorado "
  "(1969), India: A Wounded Civilization (1977), Among the Believers (1981), Finding the Centre (1984), The "
  "Enigma of Arrival (1987), India: A Million Mutinies Now (1990) and Beyond Belief (1998). His later novels "
  "include The Mimic Men (1967), In a Free State (1971, Booker Prize), Guerrillas (1975), A Bend in the River "
  "(1979), The Enigma of Arrival, A Way in the World (1994), Half a Life (2001) and Magic Seeds (2004). He was "
  "knighted in 1990, received the Nobel Prize in Literature in 2001 and died in London on 11 August 2018.",
  "Novels: The Mystic Masseur (1957), The Suffrage of Elvira (1958), Miguel Street (1959), A House for Mr Biswas "
  "(1961), Mr Stone and the Knights Companion (1963), The Mimic Men (1967), In a Free State (1971), Guerrillas "
  "(1975), A Bend in the River (1979), The Enigma of Arrival (1987), A Way in the World (1994), Half a Life (2001) "
  "and Magic Seeds (2004). Travel and essays: The Middle Passage (1962), An Area of Darkness (1964), The Loss of "
  "El Dorado (1969), India: A Wounded Civilization (1977), Among the Believers (1981), Finding the Centre (1984), "
  "A Turn in the South (1989), India: A Million Mutinies Now (1990), Beyond Belief (1998) and The Writer and the "
  "World (2003).",
  "A precise, unhurried, declarative prose, with a journalist's eye for the revealing detail and a satirist's ear "
  "for Trinidadian speech; the travel books combine reportage, memoir and portrait; the later novels replace plot "
  "with meditation and the essayistic sequence, and the sentence grows longer and more qualified as the books "
  "proceed.",
  "Displacement and the search for a home (Mr Biswas's house, the narrator of The Enigma of Arrival); the "
  "colonial aftermath in Trinidad, Africa and India; the fragility of newly independent states and the "
  "predicament of the mimic man; the writer's exile and the immigrant's self-invention; order, dignity and the "
  "small decencies against disorder.",
  "One of the two or three most important novelists in English of the postwar period, and the most influential "
  "travel writer in the language; his work is central to postcolonial criticism, both as its subject and as its "
  "provocation, and the Nobel citation praised his 'incorruptible scrutiny' and his 'uncompromising scrutiny of "
  "the effects of colonialism'.",
  bib_status="incomplete",
  bib_note="The books are listed from Wikipedia's article and general knowledge, in order of first publication; only "
           "the Norton selection, 'One Out of Many' (in In a Free State, 1971), has a work record, so the "
           "bibliography is incomplete. The travel books and later novels have no records, and the dates of first "
           "publication were not checked title by title against a bibliography.",
  ver="partially verified", sources=[W_VSN, NAIP_PR]),
A10(WS, MAJ, "1934", None, "Abeokuta, British Nigeria",
  "Nigerian; playwright, poet, novelist and essayist, writing in English with Yoruba and Nigerian idiom, resident "
  "for long periods in Britain and the United States",
  "Nigerian playwright and Nobel laureate whose plays, from A Dance of the Forests to Death and the King's Horseman "
  "and The Road, fuse Yoruba ritual, myth and masquerade with the forms of European drama",
  "Akinwande Oluwole Soyinka was born on 13 July 1934 in Abeokuta, in western Nigeria, the son of Samuel Ayodele "
  "Soyinka, a schoolteacher and Anglican, and Grace Eniola Soyinka, a trader and activist in the women's movement "
  "of Abeokuta; he grew up in the mission compound of Aké, which he later described in Aké: The Years of Childhood "
  "(1981). He attended Government College, Ibadan, and University College, Ibadan, and in 1954 went to the "
  "University of Leeds, where he took a degree in English and wrote a thesis on the drama of the absurd. He "
  "returned to Nigeria in 1960 and founded the 1960 Masks and then the Orisun Theatre, writing and directing plays "
  "that drew on Yoruba masquerade and ritual; his early plays include The Swamp Dwellers (1958), The Lion and the "
  "Jewel (1959), A Dance of the Forests (1960, for the independence celebrations), The Strong Breed (1964), The "
  "Road (1965) and Kongi's Harvest (1967). During the Nigerian Civil War he was arrested and held in solitary "
  "confinement for nearly two years (1967-1969), an experience recorded in The Man Died (1972). Later plays "
  "include Madmen and Specialists (1971), Death and the King's Horseman (1975), Opera Wonyosi (1981), A Play of "
  "Giants (1984), and The Beatification of Area Boy (1995); his novels are The Interpreters (1965), Season of Anomy "
  "(1973) and Chronicles from the Land of the Happiest People on Earth (2021). He was awarded the Nobel Prize in "
  "Literature in 1986, the first African writer to receive it, and he has taught at Cambridge, Yale, Emory and "
  "Oxford.",
  "Plays: The Swamp Dwellers (1958), The Lion and the Jewel (1959), A Dance of the Forests (1960), The Strong Breed "
  "(1964), The Road (1965), Kongi's Harvest (1967), Madmen and Specialists (1971), Death and the King's Horseman "
  "(1975), Opera Wonyosi (1981), A Play of Giants (1984) and The Beatification of Area Boy (1995). Novels: The "
  "Interpreters (1965), Season of Anomy (1973) and Chronicles from the Land of the Happiest People on Earth "
  "(2021). Poetry: Idanre and Other Poems (1967), A Shuttle in the Crypt (1972), Ogun Abibiman (1976), Mandela's "
  "Earth (1988) and Samarkand (1990). Memoirs and essays: The Man Died (1972), Myth, Literature and the African "
  "World (1976), Aké (1981), Art, Dialogue and Outrage (1988) and You Must Set Forth at Dawn (2006).",
  "A theatre of total performance in which Yoruba ritual, drumming, dance, masquerade and the language of the "
  "market are set against the conventions of the European stage; a dense, punning, rhetorical English, often "
  "drawing on Yoruba proverbs and idiom; satire and farce alongside tragedy; plays built on processions, "
  "interruptions and the eruption of the supernatural into everyday life.",
  "The encounter of Yoruba traditional religion and culture with colonialism, Christianity and modernity; ritual "
  "sacrifice and the burden of the past (Death and the King's Horseman); political corruption and dictatorship "
  "in post-independence Africa (Kongi's Harvest, Madmen and Specialists); the artist's and the individual's "
  "relation to the community; memory, tyranny and exile.",
  "The central figure of modern African drama in English, the first African Nobel laureate in literature, and a "
  "writer whose work joined African performance traditions to world theatre; Death and the King's Horseman is "
  "regarded as his masterpiece and as one of the great plays of the twentieth century.",
  bib_status="incomplete",
  bib_note="Plays, novels, poems and memoirs are listed from Wikipedia's article and general knowledge; only the "
           "Norton selection, Death and the King's Horseman (1975), has a work record, so the bibliography is "
           "incomplete. The dates of the earlier plays are those of first performance rather than publication and "
           "were not checked against a bibliography.",
  ver="partially verified", sources=[W_WS, SOY_LH]),
A10(CC, MAJ, "1938", None, "Finsbury, London, England",
  "English; playwright, writing in English",
  "English playwright whose formally inventive plays, from Cloud 9 and Top Girls to Serious Money and Far Away, "
  "made her the most innovative political dramatist of the postwar British stage",
  "Caryl Lesley Churchill was born on 3 September 1938 in Finsbury, London, and grew up in Montreal and in "
  "Oxfordshire, where her family moved during the war. She read English at Lady Margaret Hall, Oxford, where she "
  "wrote two plays produced by student societies, and married David Harter in 1961, with whom she had three sons. "
  "Her first professional work was for radio, and her stage plays of the 1970s - Owners (1972), Objections to Sex "
  "and Violence (1976), Light Shining in Buckinghamshire (1976) and Vinegar Tom (1976) - were written for the "
  "fringe and for the Royal Court, the last two in collaboration with the feminist theatre company Monstrous "
  "Regiment. Cloud 9 (1979) and Top Girls (1982) made her reputation; they were followed by Fen (1983), Serious "
  "Money (1987, a satire in rhyming couplets on the City of London), Icecream (1989), The Skriker (1994), Blue "
  "Heart (1997), Far Away (2000), A Number (2002), Drunk Enough to Say I Love You? (2006), Seven Jewish Children "
  "(2009), Love and Information (2012), Here We Go (2015), Escaped Alone (2016) and What If If Only (2021). She "
  "has worked throughout with the director Max Stafford-Clark and with the Royal Court, and her plays are "
  "characterised by non-naturalistic devices: overlapping dialogue, doubling, time-shifts and abrupt shifts of "
  "register.",
  "Plays: Owners (1972), Objections to Sex and Violence (1976), Light Shining in Buckinghamshire (1976), Vinegar "
  "Tom (1976), Cloud 9 (1979), Top Girls (1982), Fen (1983), Softcops (1984), Serious Money (1987), Icecream "
  "(1989), Mad Forest (1990), The Skriker (1994), Blue Heart (1997), Far Away (2000), A Number (2002), Drunk "
  "Enough to Say I Love You? (2006), Seven Jewish Children (2009), Love and Information (2012), Here We Go "
  "(2015), Escaped Alone (2016) and What If If Only (2021).",
  "Non-naturalistic structure: overlapping dialogue, scenes played simultaneously, characters doubled and "
  "cross-cast, time-schemes that collide (Cloud 9 moves from Victorian Africa to 1979 London with the same "
  "characters aged by only twenty-five years); verse and rhyming couplets in Serious Money; short, elliptical "
  "scenes and abrupt reversals; language pared down to fragments in the late plays.",
  "The abuses of power, political and sexual (Top Girls, Serious Money); sexual politics and the construction of "
  "gender (Cloud 9, Vinegar Tom); women's history and the cost of success; Thatcherism, the City and the "
  "market (Top Girls, Serious Money); war, torture and complicity (Far Away, Seven Jewish Children); the fragility "
  "of language and of the family (A Number, Escaped Alone).",
  "The most important British playwright of her generation and, in the 2011 Village Voice poll of dramatists, the "
  "greatest living playwright; her formal inventions changed the possibilities of political theatre in Britain, "
  "and Top Girls and Cloud 9 are among the most frequently revived plays of the postwar repertoire.",
  bib_status="incomplete",
  bib_note="The plays are listed from Wikipedia's article and general knowledge; only the Norton selection, Top "
           "Girls (1982), has a work record, so the bibliography is incomplete. Dates are those of first "
           "production, which for Churchill's plays is usually the significant date, and were not checked one by "
           "one against a bibliography.",
  ver="partially verified", sources=[W_CC, W_TG_PLAY]),
A10(SH, MAJ, "1939", "2013", "Tamniaran, near Castledawson, County Londonderry, Northern Ireland",
  "Irish; poet, translator and playwright, resident in Dublin from 1976, writing in English",
  "Irish poet and Nobel laureate whose poems of the Mossbawn farm, the Troubles and the ordinary world, from Death "
  "of a Naturalist to Human Chain, made him the most widely read poet in English of his time",
  "Seamus Justin Heaney was born on 13 April 1939 at Mossbawn, the family farm in the townland of Tamniaran near "
  "Castledawson, County Londonderry, the eldest of the nine children of Patrick Heaney, a cattle dealer, and "
  "Margaret Kathleen McCann. The family moved to Bellaghy when he was a boy. He was educated at the local primary "
  "school and at St Columb's College in Derry, then read English at Queen's University Belfast, graduating in "
  "1961; he trained as a teacher and lectured at St Joseph's College in Belfast and at Queen's, where he "
  "encountered the poetry of Ted Hughes and began to publish. Death of a Naturalist (1966) made his name, and was "
  "followed by Door into the Dark (1969), Wintering Out (1972), North (1975), Field Work (1979), Station Island "
  "(1984), The Haw Lantern (1987), Seeing Things (1991), The Spirit Level (1996), Electric Light (2001), District "
  "and Circle (2006) and Human Chain (2010), with the translations of Sweeney Astray (1983), The Cure at Troy "
  "(1990), Beowulf (1999) and Aeneid VI (2016). He moved to Dublin in 1976 and taught at Harvard from 1981 and at "
  "Oxford as Professor of Poetry from 1989 to 1994. He received the Nobel Prize in Literature in 1995 and died in "
  "Dublin on 30 August 2013.",
  "Poetry: Death of a Naturalist (1966), Door into the Dark (1969), Wintering Out (1972), North (1975), Field Work "
  "(1979), Station Island (1984), The Haw Lantern (1987), Seeing Things (1991), The Spirit Level (1996), Electric "
  "Light (2001), District and Circle (2006) and Human Chain (2010); Opened Ground: Selected Poems 1966-1996 "
  "(1998). Translations: Sweeney Astray (1983), The Cure at Troy (1990), Beowulf (1999) and Aeneid VI (2016). "
  "Plays: The Cure at Troy and The Burial at Thebes (2004). Essays: Preoccupations (1980), The Government of the "
  "Tongue (1988) and Finders Keepers (2002).",
  "A poetry of the senses and of the soil, with a strong stress metre and a rich consonantal music; exact "
  "description of farm work, bogland and weather; the sonnet sequences and the longer meditative poems; a "
  "diction that holds Latinate abstraction and Ulster dialect together; the translations, especially Beowulf, "
  "carry the same muscular line.",
  "The labour and inheritance of the family farm (Digging, Follower); the Troubles and the poet's responsibility "
  "in the face of violence (North, Punishment, Casualty); the bog bodies and the archaeology of the past; place, "
  "soil and the names of places; the ordinary epiphanies of the later poems; memory, the dead and the "
  "consolations of the everyday.",
  "The best-known and most widely read poet in English of the late twentieth century, praised by Robert Lowell as "
  "'the most important Irish poet since Yeats'; his Nobel Prize in 1995 recognised a body of work that entered "
  "school syllabuses and public life without losing its formal ambition, and his death was treated as a national "
  "event in Ireland.",
  bib_status="incomplete",
  bib_note="The collections are listed from Wikipedia, the Ricorso bibliography and general knowledge, with the "
           "contents of Death of a Naturalist (1966), North (1975), Field Work (1979) and Station Island (1984) "
           "checked against the Ricorso listing. Installment 10 records only the six dated Norton selections "
           "('Digging', 1966; 'The Grauballe Man' and 'Punishment', 1975; 'Casualty', 1979; station Island XII, "
           "1984; 'Clearances', 1987); the bibliography is therefore incomplete, and the translations and prose "
           "have no records.",
  ver="partially verified", sources=[W_SH, SH_WORKS]),
]

WORKS = [
W10("Epilogue", GN, "1983", "Poem (four short lines)", "minor",
  genres=G("Lyric Poetry", "Political Poetry"),
  themes=T("Migration, exile and diaspora", "Language, writing and the limits of representation",
           "Race, racism and the struggle for civil rights"),
  movements=M(CAR, BBW),
  overview="The four-line lyric that closes Grace Nichols's first collection, I is a Long-Memoried Woman (1983): the "
           "poet has crossed an ocean and lost her tongue, but from the root of the old one a new one has sprung.",
  content="Four unrhymed lines in two couplets, spoken in the first person, which compress the history of the "
          "Middle Passage and of Caribbean English into a single image of language as a transplanted root.",
  summary="'I have crossed an ocean / I have lost my tongue / from the root of the old one / a new one has sprung.' "
          "The poem names the crossing and the loss in its first two lines and answers them in the second two: the "
          "lost tongue is not recovered but replaced, and the replacement grows from the root of what was lost. The "
          "speaker does not say which language the new tongue is; the poem's English, plain and uncreolised, is "
          "itself part of the answer, and the title's 'Epilogue' places the four lines after the long historical "
          "sequence of the collection, as its conclusion rather than its preface.",
  themes_text="Language as the inheritance of slavery and of survival: the mother tongue is lost in the crossing, "
              "yet the new tongue grows from its root, so that loss and continuity are held together. The poem also "
              "carries the larger argument of Nichols's work, that Caribbean English is not a broken form of the "
              "coloniser's language but a new growth with its own roots.",
  structure="Two unrhymed couplets, the first stating the loss ('crossed', 'lost') and the second the recovery "
            "('sprung'), so that the poem turns at its midpoint; the last line is also the last line of the "
            "collection, which gives it the force of a conclusion.",
  style="Plain, declarative monosyllables and a nursery-rhyme simplicity; the metaphor of the tongue as a plant is "
        "carried by 'root' and 'sprung' without being explained; the poem is written in standard English, unlike "
        "the Creole poems that precede it in the collection.",
  ctx="Nichols moved from Guyana to Britain in 1977, and I is a Long-Memoried Woman (1983) was published by Karnak "
      "House, the London black publisher, with a sequence spoken by an enslaved woman; the collection won the "
      "Commonwealth Poetry Prize and was dramatised for radio and film.",
  sig="The most anthologised short poem of Nichols's first collection and a compact statement of the central "
      "preoccupation of Black British and Caribbean writing, the relation of the new English to the languages it "
      "displaced; it is one of the three poems by Nichols in the Norton Anthology.",
  canon="Minor canon",
  biblio="Published at the end of I is a Long-Memoried Woman (London: Karnak House, 1983). A selection of The "
         "Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 752.",
  notes="The text is quoted from the readingnorton.com reading of the poem, which prints all four lines; the poem "
        "is the closing piece of the collection as its title indicates. The reading beneath the paraphrase is the "
        "record's own.",
  ver="partially verified", sources=[NICH_READ, W_GN, NAEL]),
W10("The Fat Black Woman Goes Shopping", GN, "1984", "Poem (six stanzas in free verse)", "significant",
  genres=G("Lyric Poetry", "Political Poetry", "Dramatic Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Gender, feminism and women's lives",
           "The city, the suburb and modern space"),
  movements=M(CAR, BBW),
  overview="The best known of the Fat Black Woman poems of 1984: a comic, angry monologue in which the Fat Black Woman "
           "shops for winter clothes in a London that has nothing in her size and watches her every move.",
  content="The Fat Black Woman goes from shop to shop in the cold, is ignored or inspected by assistants, finds "
          "'nothing much beyond size 14', and goes home to dream of the soft, bright, billowing clothes of her "
          "imagination; the last stanza widens the complaint to the black women of Britain, who swear in Swahili, "
          "Yoruba and nation language under their breath.",
  summary="The poem opens with the Fat Black Woman 'window shopping' in the winter sales, her body taking up more "
          "room than the shops allow: the choice is lean, and nothing much is to be had beyond size 14. The "
          "assistants are 'supercilious' and the mirrors conspire; she is watched as she walks, and the watching "
          "turns a private errand into a public offence. Against the grey cold and the narrow racks she sets the "
          "clothes she would buy if the world were made for her: soft, loose, brightly coloured things, a 'silky "
          "fresh' dress, a 'tumble of tropical laughter'. The poem ends by generalising the experience, so that the "
          "individual shopper becomes 'the fat black woman' who swears in Swahili, Yoruba and nation language, and "
          "the comedy of the fitting-room turns into a judgement on a country that cannot dress or see her.",
  themes_text="The poem makes the shopping trip a measure of exclusion: the body that does not fit the clothes is a "
              "body the society has not planned for, and the scrutiny of the shop assistants repeats in a minor "
              "key the larger racial and sexual policing of black women in Britain. The fantasy clothes are not "
              "mere escapism but a claim on beauty and pleasure, and the closing list of languages makes the "
              "private grievance a collective one.",
  structure="Six stanzas of irregular free verse in a speaking voice, moving from the street to the shop to the "
            "mirror to the imagined wardrobe and then out to the collective 'fat black woman'; the movement from "
            "'I' to 'she' in the last stanza turns the anecdote into a representative case.",
  style="Conversational free verse with Creole and Caribbean inflections ('she have to' for 'she has to'), comic "
        "hyperbole, a repeated refrain-like complaint and a sudden widening of scope in the last stanza; the "
        "diction is deliberately unliterary.",
  ctx="The Fat Black Woman's Poems appeared from Virago in 1984, in the period of the Thatcher governments, when "
      "the Black British women's movement and the black arts movement were at their height; Nichols had come to "
      "Britain in 1977 and the Fat Black Woman poems were written as a deliberate counter to the passive, "
      "exoticised black woman of the British imagination.",
  sig="The most famous poem of Nichols's Fat Black Woman sequence and one of the standard anthology pieces of "
      "Black British writing, widely taught in schools; it established the comic, bodily, first-person voice that "
      "made her work popular and it is one of the three Nichols poems in Norton.",
  canon="Secondary canon",
  biblio="Published in The Fat Black Woman's Poems (London: Virago, 1984). A selection of The Norton Anthology of "
         "English Literature, 11th edition, vol. F, beginning on page 752.",
  notes="The paraphrase follows the readingnorton.com reading, which quotes the key lines ('the choice is lean / "
        "Nothing much beyond size 14'; 'the fat woman swears in Swahili, Yoruba / and nation language under her "
        "breath'); the description of the imagined clothes is general knowledge of the poem rather than a "
        "quotation, since the full text was not consulted.",
  ver="partially verified", sources=[NICH_READ, W_GN, NAEL]),
W10("Wherever I Hang", GN, "1989", "Poem (five stanzas in Creole)", "significant",
  genres=G("Lyric Poetry", "Dub Poetry"),
  themes=T("Migration, exile and diaspora", "Identity, authenticity and the divided self",
           "Nationhood and national identity"),
  movements=M(CAR, BBW, SPW),
  overview="A poem in Guyanese Creole from Lazy Thoughts of a Lazy Woman (1989) about settling in England: the "
           "speaker sends home photographs of herself among the pigeons and the snow, learns to queue and to warn "
           "people before visiting, and ends divided 'to de bone' between two homes.",
  content="Five stanzas of Creole verse in which the immigrant speaker describes her adaptation to English life, the "
          "habits she has taken on and the homesickness she cannot cure, and concludes that wherever she hangs her "
          "knickers is her home.",
  summary="The speaker sends home photographs of herself among the pigeons and the snow and wards off the cold; "
          "little by little she changes her 'calypso ways', learning to give clear warning before visiting anybody "
          "and to wait her turn in the queue. After all this time she has grown accustomed to English life, but she "
          "still misses 'back-home side', and to tell the truth she does not know where she belongs: she is "
          "'divided to de ocean / divided to de bone'. The poem's last line drops the elegiac tone for a joke: "
          "'Wherever I hang me knickers - that's my home.' The joke does the argument's work, since it makes home "
          "a matter of daily habit and the body rather than of nation or blood, and refuses the pathos the poem has "
          "just earned.",
  themes_text="Home as practice rather than origin: the poem records the small disciplines of English life (queuing, "
              "appointments, warning before visits) as the materials out of which a new belonging is made, while "
              "keeping the loss of the old one in view. The divided self is stated in the 'divided to de ocean' "
              "image and then comically resolved, so that the poem neither sentimentalises exile nor pretends that "
              "assimilation is complete.",
  structure="Five stanzas of loose Creole verse, of unequal length; the first three accumulate the details of adaptation, "
            "the fourth turns to the speaker's uncertainty and the last delivers the joke that also concludes the "
            "argument. Each stanza begins with a connective ('And is so', 'Now', 'But') that gives the poem the "
            "air of talk.",
  style="Guyanese Creole spelling and syntax ('mi', 'de', 'belaang', 'accustom'), an unhurried conversational "
        "rhythm, internal rhyme and assonance in place of regular metre, and a deliberate anticlimax in the last "
        "line; the register moves between the elegiac and the comic within a stanza.",
  ctx="Lazy Thoughts of a Lazy Woman was published by Virago in 1989, a decade after Nichols settled in London; the "
      "poem belongs to the large body of Caribbean-British writing of the 1980s about migration and belonging, and "
      "its Creole is the 'nation language' of Kamau Brathwaite and of the dub poets.",
  sig="One of Nichols's most quoted poems on migration and one of the three of hers in the Norton Anthology; its "
      "last line has become a proverbial phrase in Caribbean-British writing, and the poem is a standard example "
      "of the use of Creole in English poetry.",
  canon="Secondary canon",
  biblio="Published in Lazy Thoughts of a Lazy Woman (London: Virago, 1989) and collected in I Have Crossed an "
         "Ocean: Selected Poems (Bloodaxe, 2010). A selection of The Norton Anthology of English Literature, 11th "
         "edition, vol. F, beginning on page 753.",
  notes="The summary follows the text printed in full by the greatbritishwriters reading and the extracts quoted "
        "by readingnorton.com; the stanza count follows that text and was not checked against the 1989 printing.",
  ver="partially verified", sources=[NICH_READ, W_GN, NAEL]),
]

WORKS += [
W10("Inglan Is a Bitch", LKJ, "1980", "Poem (dub poem, long line in Creole)", "significant",
  genres=G("Dub Poetry", "Political Poetry", "Performance Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Class, labour and social mobility",
           "Migration, exile and diaspora"),
  movements=M(DUB, BBW, SPW),
  overview="The title poem of Linton Kwesi Johnson's third collection (Race Today, 1980), spoken in the voice of a "
           "Jamaican immigrant who has worked in Britain for decades and is made redundant at fifty-five; a dub "
           "poem built on the refrain 'Inglan is a bitch, dere's no escapin it'.",
  content="A monologue in Jamaican Creole recounting a working life in London, from the underground and the "
          "dish-washing to a factory in Brackley and the dole, punctuated by the refrain that England is a bitch "
          "from which there is no running away.",
  summary="The speaker came to London and worked on the Underground, then as a dish-washer, then digging ditches, "
          "and found that hard work brought him nothing: after a while he stopped the overtime and put down his "
          "tools. The chorus returns: 'Inglan is a bitch, dere's no escapin it', and there is no running away from "
          "it. He works day shifts and night shifts, clean work and dirty work, while the society says that black "
          "men are lazy; if you saw how he works you'd say he was crazy. In a factory in Brackley they have done "
          "nothing for fifteen years but pack crockery, and after fifteen years' labour he falls out of favour. "
          "There is work in abundance, yet he is made redundant at fifty-five and sent to draw the dole. The poem "
          "ends by turning the complaint outward - 'is whey wi a goh dhu 'bout it?' - from a lament into a question "
          "about action.",
  themes_text="The poem is an anatomy of the exploitation of black immigrant labour: the hardest work for the least "
              "pay, the taxes that claw back the wage packet, the accusation of laziness levelled at the worker who "
              "works two shifts, and the redundancy that ends a working life. Its refrain refuses consolation: "
              "England cannot be escaped, only faced, and the final question moves from endurance to politics. The "
              "comic, proverbial force of 'bitch' carries the anger without softening it.",
  structure="A single long monologue in stanzas of varying length, each closed by the refrain, which recurs with "
            "small variations ('dere's no escapin it', 'dere's no runnin' whey fram it', 'y'u bettah face up to "
            "it'); the movement is chronological, from arrival to redundancy, and the last line breaks the pattern "
            "with a question.",
  style="Jamaican Creole transcribed for the page ('mi', 'w'en', 'bwoy', 'noh'), a heavy stress beat and long "
        "breath-lines shaped for performance over a reggae bass line; repetition and refrain instead of rhyme; "
        "documentary detail (Brackley, the dole, the tax racket) carried in the plainest diction.",
  ctx="The poem was the title piece of Inglan Is a Bitch, published by Race Today Publications in 1980, the year of "
      "the Brixton uprising and of the Thatcher government's first budget; it was performed with Dennis Bovell's "
      "dub band and recorded on Bass Culture (1980). Its picture of black labour in Britain belongs to the "
      "Windrush generation's experience of the 1970s and 1980s.",
  sig="The best known poem of British dub poetry and a standard anthology piece; its refrain passed into common "
      "speech and it is the work by which Johnson is most often represented, including in the Norton Anthology.",
  canon="Secondary canon",
  biblio="Published in Inglan Is a Bitch (London: Race Today Publications, 1980); recorded on the album Bass "
         "Culture (Island, 1980). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, "
         "beginning on page 755.",
  notes="The paraphrase follows the text printed with the Bass Culture recording and quoted at length in the "
        "OpenEdition study; the printed collection's text was not collated against it, and the stanza division "
        "given here follows the recording's refrain pattern rather than the 1980 page setting.",
  ver="partially verified", sources=[LKJ_PULM, W_LKJ, NAEL]),
W10("To Room Nineteen", DL, "1963", "Short story", "major",
  genres=G("Short Story", "Psychological Novel", "Domestic Fiction"),
  themes=T("Gender, feminism and women's lives", "Madness, breakdown and confinement", "Family, marriage and domestic life"),
  movements=M("Second-Wave Feminist Writing",),
  overview="Doris Lessing's story of 1963, collected in A Man and Two Women, about Susan Rawlings, a clever, "
           "happily married mother of four who finds that her sensible life has no room for her and takes a hotel "
           "room in which to be alone, until the room too is taken from her.",
  content="A third-person narrative, framed by an intrusive narrator's opening remark that this is a story about 'a "
          "failure in intelligence', which follows Susan Rawlings from her marriage and the birth of four children "
          "through her growing sense of vacancy to the rented room nineteen and her suicide.",
  summary="The Rawlings' marriage is grounded in intelligence: they married late, 'amid general rejoicing', have "
          "four healthy children and a large white house with a garden, and manage their lives so well that they "
          "seem to have arranged an abstinence from pain. Matthew is briefly unfaithful, and the affair is absorbed "
          "as an eminently sensible arrangement; but something has been let in. When the youngest children go to "
          "school, Susan finds the house empty and herself without occupation, and a 'demon' begins to wait for her "
          "in the garden. She tries the remedies the story offers her: she takes a job, gives it up; she arranges "
          "an au pair and a cleaner; she takes a room in a hotel in Bloomsbury, room nineteen, where she sits for "
          "hours doing nothing, and comes home refreshed and able to be a wife and mother again. Matthew, unable to "
          "accept that she wants nothing but solitude, presses her for an explanation, and she invents a lover "
          "because a lover is a reason he can understand. The deception grows; he hires a private detective and "
          "believes himself betrayed. With the last place of her own discovered, Susan goes back to room nineteen, "
          "stops up the cracks of the gas fire and kills herself. The story's final paragraphs present her death "
          "not as breakdown but as a release into a 'fructifying' dark, and the narrator's judgement falls on the "
          "intelligence that could explain everything and understand nothing.",
  themes_text="The story examines what a rationally arranged life leaves out: the Rawlings' intelligence is a "
              "machine for avoiding pain, and it produces a woman with no reason to live. Lessing keeps three "
              "explanations in play - the class-bound boredom of the middle-class housewife, the gender order that "
              "makes the wife's identity a function of her family, and a more general account of the sensitive "
              "soul in a sensible world - and refuses to settle the case. The invented lover is the story's "
              "sharpest stroke: a wife's need for solitude cannot be heard, so it must be translated into the "
              "language of sex that the husband and the society can understand. Room nineteen itself is the " \
              "ambiguous symbol of the whole: a place of nothing, which is also the only place where Susan is "
              "herself.",
  structure="A framed third-person narrative in numbered sections, beginning with a narrator's essay-like "
            "statement and ending with a lyrical account of the suicide; the narration moves between free indirect "
            "discourse inside Susan's mind and a cold, analytic view of the marriage, and the temporal frame runs "
            "from courtship to death with the detective's report as its turning point.",
  style="Plain, exact, deliberately unadorned prose that reports feeling with clinical detachment; the key word "
        "'sensible' recurs as a refrain; the narrator interrupts the fiction with general statements, in the "
        "manner of the eighteenth-century essay-novel; the imagery of water and of the dark river gathers towards "
        "the end.",
  ctx="Written in London and published in the collection A Man and Two Women (1963), the story belongs to the "
      "moment in which the dissatisfaction of educated housewives became a public subject, four years before The "
      "Feminine Mystique. Lessing had come to England from Southern Rhodesia in 1949 and had been a member of the "
      "Communist Party until 1956; the story's analysis of marriage is continuous with the 'free women' of The "
      "Golden Notebook, which was published the year before.",
  sig="One of the most anthologised English short stories of the postwar period and a central text in the literary "
      "history of second-wave feminism; it is the Lessing story in the Norton Anthology and the one on which her "
      "account of female breakdown is most often based.",
  canon="Major canon",
  biblio="Published in A Man and Two Women (London: MacGibbon and Kee, 1963) and collected in To Room Nineteen: "
         "Collected Stories Volume One (1978). A selection of The Norton Anthology of English Literature, 11th "
         "edition, vol. F, beginning on page 764.",
  crit="The story is a standing point of reference in feminist criticism of the postwar short story, read by "
       "Lessing's commentators as a case study in the 'problem that has no name' and, more recently, as a subtler "
       "text than that reading allows: critics of the 1980s and 1990s emphasised the story's refusal to choose "
       "between social, psychological and metaphysical explanations, and its careful management of a narrator who "
       "judges as well as reports. It belongs with the stories of A Man and Two Women and of To Room Nineteen, "
       "where Lessing worked out the themes that The Golden Notebook would take up on a larger scale, and it is "
       "the Lessing text most often set in courses on the modern short story.",
  notes="The plot account is drawn from the story as summarised and quoted in the Encyclopedia of the Short Story "
        "entry (encyclopedia.com) and from general knowledge of the text; quotations were checked against that "
        "entry. The interpretation of the ending is the record's own and does not follow any single critic.",
  ver="partially verified", sources=[LESSING_ENC, W_DL, NAEL]),
]

WORKS += [
W10("Self-Portrait", AKR, "1966", "Poem (fourteen short lines)", "minor",
  genres=G("Lyric Poetry", "Modernist Poetry"),
  themes=T("Identity, authenticity and the divided self", "Family, marriage and domestic life"),
  movements=M(SAS, POSTCOL),
  overview="A short poem from A. K. Ramanujan's first collection, The Striders (1966), in which the speaker sees, in "
           "shop windows and against the laws of optics, the portrait of a stranger who resembles everyone but "
           "himself.",
  content="A single sentence of fourteen short lines: the speaker resembles everyone but himself, sees a stranger's "
          "portrait in shop windows, dated unknown but often signed in a corner by his father.",
  summary="'I resemble everyone / but myself.' The speaker sometimes sees, in shop windows and despite the "
          "well-known laws of optics, the portrait of a stranger, date unknown, often signed in a corner by his "
          "father. The poem's joke is a serious one: the mirror of the shop window gives back not the self but the "
          "family, so that identity is inheritance before it is anything else. The missing date and the father's "
          "signature make the portrait an old-master likeness in a family album, and they leave the speaker unable "
          "to say when or whether he began. In fourteen lines the poem states the theme that runs through all of "
          "Ramanujan's poetry, the self as a copy of others, and it does so in an idiom so plain that the "
          "metaphysical pun on resemblance is easy to miss.",
  themes_text="Resemblance as the ground of identity and the obstacle to it: to resemble everyone is to have no "
              "portrait of one's own, and the father's signature on the stranger's face makes inheritance both the "
              "source of the self and the reason it cannot be seen. The poem is also about the migrant's double "
              "sight, the Indian in America who finds his family in every face.",
  structure="A single sentence in fourteen short lines, without stanza breaks and with almost no punctuation in "
            "the middle; the syntax enacts a process of looking that never arrives at the self, and the last line's "
            "revelation ('signed in a corner / by my father') reverses the poem's direction.",
  style="Plain, clipped free verse of two- and three-word lines; the diction is abstract and legalistic "
        "('the well-known laws / of optics', 'date unknown'), and the flatness of the statement is what makes the "
        "last line's turn effective.",
  ctx="The Striders was published by Oxford University Press in London in 1966, while Ramanujan was teaching at "
      "Chicago; the poem belongs to the first generation of Indian English poetry written by professional "
      "linguists, and its theme of family resemblance is a recurring one in his work.",
  sig="One of the most often quoted of Ramanujan's early poems and the standard short introduction to his theme of "
      "inherited identity; it is the first of his two selections in the Norton Anthology.",
  canon="Minor canon",
  biblio="Published in The Striders (London: Oxford University Press, 1966) and collected in Selected Poems (1976) "
         "and The Collected Poems (1995). A selection of The Norton Anthology of English Literature, 11th edition, "
         "vol. F, beginning on page 797.",
  notes="The text is quoted from the Selected Poetry PDF and from the University of Hyderabad introduction to "
        "Ramanujan, which print the poem complete and agree; the reading is the record's own.",
  ver="partially verified", sources=[AKR_SEL, W_AKR, NAEL]),
W10("Elements of Composition", AKR, "1986", "Poem (twenty-eight short lines)", "significant",
  genres=G("Lyric Poetry", "Experimental Poetry"),
  themes=T("Identity, authenticity and the divided self", "Nature, ecology and environmental crisis",
           "Language, writing and the limits of representation"),
  movements=M(SAS, POSTCOL),
  overview="The opening poem of Ramanujan's third collection, Second Sight (1986), which composes the self out of the "
           "chemical elements and then, in the second half, sets the constant elements against the moving eyes that "
           "can see only by moving.",
  content="Two movements: a list of the elements that make up the body, from the father's seed and the mother's egg "
          "through earth, air, fire and water to calcium, carbon, gold and magnesium, and then a meditation on the "
          "self so composed, 'a chattering self tangled in love and work', capable of seeing the constancy of "
          "things only by moving constantly.",
  summary="The poem begins 'Composed as I am, like others, / of elements on certain well-known lists', and names the "
          "ingredients: the father's seed and the mother's egg gathering earth, air, fire and mostly water into a "
          "'mulberry mass', moulding calcium, carbon, 'even gold, magnesium and such' into a chattering self "
          "tangled in love and work and scary dreams. The second half turns to what such a self can see: the eyes "
          "can see the constancy of things only by moving constantly. The poem ends with a sequence of images of "
          "constancy - a child's face, a remembered street, a woman's hand - that the moving eye catches only as it "
          "passes, so that knowledge is a matter of motion and the self a compound that knows itself only in "
          "passing. The title is a pun on two senses of 'composition': the chemical constitution of a body and the "
          "writing of a poem.",
  themes_text="The poem sets the fixity of the elements against the mobility of the consciousness they make, and "
              "asks what kind of knowledge a moving observer can have of a stable world. The 'well-known lists' "
              "invoke both the periodic table and the classical elements, so that the modern chemistry and the "
              "ancient cosmology compose the same body; the 'mulberry mass' and the 'chattering self' keep the "
              "tone comic and bodily. As a proem it sets out the programme of Second Sight: a poetry of particulars "
              "that knows that truth is only grasped in passing.",
  structure="A single poem in two unequal movements, the first a catalogue in short lines that accumulates the "
            "elements, the second a meditation turning on 'only by moving constantly'; the caesural line-breaks and "
            "the switch from list to argument give it the shape of a thesis and its qualification.",
  style="Short free-verse lines, abrupt enjambments and a colloquial, apparently casual syntax ('and such', "
        "'scary dreams') set against technical and archaic diction ('mulberry mass', 'constancy'); the list form "
        "is carried by parallelism and the poem's argument by a single turn.",
  ctx="Second Sight was published in Delhi and New York by Oxford University Press in 1986, after Ramanujan's "
      "return from a stay in Sri Lanka in 1983 and his renewed reading of the Upanishads and Buddhist philosophy; "
      "the poem opens the volume and announces its changed vision.",
  sig="The proem of Second Sight and the clearest statement of Ramanujan's late poetics of particulars and motion; "
      "with 'Self-Portrait' it is one of his two selections in the Norton Anthology and the one by which his "
      "philosophical ambition is usually introduced.",
  canon="Secondary canon",
  biblio="Published as the opening poem of Second Sight (Delhi and New York: Oxford University Press, 1986) and "
         "collected in The Collected Poems (1995). A selection of The Norton Anthology of English Literature, 11th "
         "edition, vol. F, beginning on page 797.",
  notes="The text and the sequence of images in the second half were read in the Selected Poetry PDF, which prints "
        "the poem complete; the poem's page number in the Norton volume follows the list (797) and the second "
        "poem's exact placing was not checked.",
  ver="partially verified", sources=[AKR_SEL, W_AKR, NAEL]),
W10("Black Jackets", TG, "1961", "Poem (lyric in eight-line stanzas)", "minor",
  genres=G("Lyric Poetry", "Social Poetry"),
  themes=T("Class, labour and social mobility", "Counterculture, drugs and rebellion", "Childhood, adolescence and coming of age"),
  movements=M(MOV),
  overview="A poem from Thom Gunn's My Sad Captains (1961) about a group of young bikers in leather jackets who stand "
           "in a café and, for the length of a record, embody a style of rebellion the poet watches from outside.",
  content="The speaker describes the red-haired boy who drove a van and his friends in their black leather jackets, "
          "their studied poses and their music, and reflects on the self-sufficiency of their world and his own "
          "distance from it.",
  summary="The poem begins in the silence after a record ends: the red-haired boy who drove a van in weekday "
          "overalls, but like his friends, has put on his black jacket, and the group of them stand at the café "
          "counter in a dress that is a uniform and a statement. Gunn describes the jackets, the hair, the boots and "
          "the poses with the exactness of a fashion plate, and notes the self-containment of the group, its "
          "indifference to the watcher and its own internal codes. The speaker is outside this world and knows it: "
          "he records rather than joins, and the poem's sympathy is with the completeness of the style rather than "
          "with any politics it might carry. The last stanzas turn the observation into a judgement on the price of "
          "belonging to such a group, and on the outsider's freedom to leave.",
  themes_text="The poem is an early study of the postwar youth style that would become the emblem of the 1960s: "
              "leather, motorcycles, a music-driven solidarity, the body turned into a sign. Gunn's interest is "
              "aesthetic and sociological at once, in how a group makes a complete world out of dress and gesture, "
              "and in what that world costs. Class is present throughout in the weekday overalls under the jackets, "
              "and the poem's calm, unpatronising tone is part of its achievement.",
  structure="Eight-line stanzas in a loose iambic line, moving from the record's silence to a general "
            "reflection; the descriptive stanzas give way to a concluding meditation, and the whole is held "
            "together by the repeated image of the jackets.",
  style="Exact, unsentimental description in plain diction; enjambment used to keep the stanza moving; a "
        "conversational, slightly clipped syntax; the rhythm of ordinary speech held in a firm stanzaic frame, "
        "characteristic of the Movement manner.",
  ctx="My Sad Captains was published by Faber in 1961, when Gunn had been in California for seven years; the poem "
      "belongs to the British 'Movement' moment but its subject, the style-culture of young working-class men, "
      "already points to the American poems that follow.",
  sig="One of the poems by which Gunn's early 'Movement' manner is represented in the Norton Anthology, and a "
      "frequently anthologised study of postwar youth style; with 'My Sad Captains' it stands for the 1961 "
      "collection.",
  canon="Minor canon",
  biblio="Published in My Sad Captains and Other Poems (London: Faber and Faber, 1961), collected in Collected "
         "Poems (1993). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning "
         "on page 800.",
  notes="The summary was written from the opening lines quoted in the poemhunter selection and from general "
        "knowledge of the poem, not from a complete text; the description of the closing stanzas is therefore "
        "general and the paraphrase claims no quotation beyond the quoted first stanza.",
  ver="partially verified", sources=[GUNN_WORLD, W_TG, NAEL]),
W10("My Sad Captains", TG, "1961", "Poem (short lyric in quatrains)", "minor",
  genres=G("Lyric Poetry", "Elegiac Poetry"),
  themes=T("Death, illness and mourning", "Love, intimacy and loss", "Art, the artist and the creative life"),
  movements=M(MOV),
  overview="The title poem of Thom Gunn's 1961 collection: a night meditation in which friends, some of them with "
           "'historical names', appear one by one in the darkness like stars, and the poet takes his leave of them.",
  content="The speaker watches a group of friends appear in the dark, one by one, some with historical names; he "
          "notes how late they start to shine, how they drift, and how he must part from them, and the poem ends "
          "with his acceptance of the separation.",
  summary="'One by one they appear in the darkness: a few friends, and a few with historical names.' The figures "
          "come out like stars, and the speaker notes how late they start to shine, how their light is steady and "
          "how they move apart from one another. The poem holds them in view as a constellation, a company that is "
          "also a pattern, and then acknowledges that he cannot keep them: the last lines turn from the observed "
          "group to the observer's own position, alone in the dark and free. The title's 'sad captains' derives "
          "from Shakespeare's Antony and Cleopatra, where Antony's captains desert him, and the poem quietly "
          "reverses the allusion: these captains do not desert the speaker, he leaves them, and the sadness is "
          "his own.",
  themes_text="Friendship, loss and the poet's relation to a company he cannot join: the poem is about the cost of "
              "the observer's freedom, and it reads as a farewell to the Movement's collective, the group of poets "
              "with whom Gunn had been identified. The starlight metaphor gives the friends a permanence in the "
              "poem that they do not have in life, and the act of naming them is the elegy.",
  structure="Short quatrains, with a single sentence running through most of the poem and a "
            "turn in the last stanza from description to address; the poem's movement is from the many to the one, "
            "from the constellation to the solitary watcher.",
  style="Short lines of three or four stresses; a lucid, almost epigrammatic syntax; the images are astronomical "
        "and maritime at once ('captains'), and the diction is deliberately plain, with the Shakespearean allusion "
        "left unglossed.",
  ctx="The title poem of My Sad Captains (Faber, 1961), the collection that marked the end of Gunn's strict "
      "Movement phase and the beginning of the free-verse poems of Touch (1967); he had been in California since "
      "1954 and the poem's solitary watcher belongs to that distance.",
  sig="The title poem of Gunn's central early collection and a standard anthology piece; with 'Black Jackets' it "
      "represents the 1961 volume in the Norton Anthology, and its Shakespearean echo is one of the most discussed "
      "moments in his early work.",
  canon="Minor canon",
  biblio="Published as the title poem of My Sad Captains and Other Poems (London: Faber and Faber, 1961), collected "
         "in Collected Poems (1993). A selection of The Norton Anthology of English Literature, 11th edition, vol. "
         "F, beginning on page 801.",
  notes="The opening is quoted from the poemhunter text; the account of the closing lines is based on general "
        "knowledge and on the poem's reported argument, and the Antony and Cleopatra allusion is a standard "
        "observation rather than a quotation from a critic.",
  ver="partially verified", sources=[GUNN_WORLD, W_TG, NAEL]),
]

WORKS += [
W10("From the Wave", TG, "1971", "Poem (six eight-line stanzas)", "minor",
  genres=G("Nature Poetry", "Lyric Poetry"),
  themes=T("Nature, ecology and environmental crisis", "Art, the artist and the creative life", "Love, intimacy and loss"),
  movements=M(MOV),
  overview="A poem from Thom Gunn's Moly (1971) describing surfers riding a wave off the California coast, in which "
           "the balance of the riders becomes an image of the discipline and surrender of the poetic art.",
  content="The wave mounts and the surfers appear on their boards, holding still against its face, half wave and half "
          "men, until they slide down it and paddle out to wait for the next; the poem watches the whole cycle of "
          "the wave from its building to its breaking.",
  summary="The wave mounts at sea like a concave wall and pushes forward; from hiding the black shapes of the "
          "surfers rise into sight on their boards. Their pale feet poise with a learned skill, and it is the wave "
          "they imitate that keeps them so still: for seconds the marbling bodies are half wave, half men. They "
          "wait as late as they can and then slice the face of the water in timed procession, for 'balance is "
          "triumph in this place, / triumph possession'. The mindless heave they rode breaks as they leave it and "
          "loses itself; their bodies loosen, and the bare foot feels the suck of shingle. They paddle in the "
          "shallows, splash each other, and swim out to wait for the right waves to gather. The poem's grammar "
          "keeps the wave as the subject even while the men act, so that the surfers are a function of the sea "
          "rather than its masters, and their skill is described as an imitation of what they ride.",
  themes_text="Surfing is an image of the artist's relation to a power he does not own: the riders imitate the wave, "
              "hold to its form, and are released when it breaks. 'Balance is triumph ... triumph possession' "
              "states the poem's ethic, that mastery consists in a momentary agreement with a force larger than "
              "the self. The writing also carries Gunn's pleasure in surfaces and contact, the substance of bodies "
              "brought against the substance of water.",
  structure="Six eight-line stanzas rhyming ababcdcd, moving through the wave's cycle from its mounting to its "
            "breaking and the swimmers' return; the regular stanza is itself an image of the balance the poem "
            "describes.",
  style="Firmly metred eight-line stanzas with a buoyant rhythm; liquid consonant clusters and long vowels "
        "('mottles', 'shingle', 'suck') imitate the water; the diction is physical and exact, with almost no "
        "abstraction; the tone is absorbed and unironic.",
  ctx="Moly (1971) was written in California, in the period of Gunn's looser free-verse experiments, but 'From the "
      "Wave' keeps a strict stanza; its subject, the surfing culture of the Pacific coast, is one of the poems by "
      "which Gunn's American life entered his English work.",
  sig="One of Gunn's most admired descriptions and a standard anthology piece from Moly; it is in the Norton "
      "Anthology as the representative poem of his American middle period.",
  canon="Minor canon",
  biblio="Published in Moly (London: Faber and Faber, 1971), collected in Collected Poems (1993). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 801.",
  notes="The text was read complete in the poemhunter printing, and the stanzaic description follows it; the "
        "reading of the poem's argument is the record's own.",
  ver="partially verified", sources=[GUNN_WORLD, W_TG, NAEL]),
W10("Still Life", TG, "1992", "Poem (four-line stanzas)", "minor",
  genres=G("Elegiac Poetry", "Lyric Poetry"),
  themes=T("Death, illness and mourning", "Love, intimacy and loss"),
  movements=M("Gay and Lesbian Literature after Stonewall",),
  overview="An elegy from The Man with Night Sweats (1992) for a friend dying of AIDS: the poet sits at the hospital "
           "bed of a man whose body has become a still life, and watches for the breath he cannot give up.",
  content="A bedside poem in short rhyming stanzas: the dying friend's greyish-yellow skin, the angle of his head "
          "wrenched sideways, the tube in his mouth, and the poet's inability to look away or to forget.",
  summary="The poem begins 'I shall not soon forget', and gives the details: the angle of the friend's head, "
          "wrenched sideways as he lay and stared unseeing at the wall; the greyish-yellow skin; the mouth held "
          "open by the tube 'in an astonished O'. The title's pun runs through the poem: the friend is a still "
          "life in the painter's sense, an arrangement of objects, and he is still alive, still breathing, 'a "
          "life-long breather' as the poem says with bitter irony. The watcher cannot help him and cannot leave, "
          "and the poem ends on the image of the tube and the astonished mouth, which is both a clinical detail and "
          "an accusation. Gunn's elegy refuses consolation and refuses horror: it holds the dying body in view with "
          "the same exactness he gave to the surfers of 'From the Wave'.",
  themes_text="The poem's subject is the body of a friend transformed by illness into something the watcher can only "
              "describe; the pun on 'still life' insists on the continuity between the dying man and the objects of "
              "a painting, and the poem's tenderness lies in the precision of its looking. It is also a poem about "
              "helplessness, the watcher's position at the bedside, and about the AIDS epidemic as a daily "
              "experience of hospitals and tubes rather than of public rhetoric.",
  structure="Short four-line stanzas, loosely rhymed, in which each stanza gives one detail of the bedside scene; "
            "the poem's progress is not narrative but a sequence of perceptions held under the pressure of "
            "memory, and the closing image returns to the mouth.",
  style="Spare, exact, unornamented language with a strong iambic base; the rhyme is irregular and often "
        "off-rhyme; the syntax is clipped and the tone level, so that the horror is carried by the precision "
        "rather than by exclamation.",
  ctx="The Man with Night Sweats (Faber, 1992) was written as Gunn's friends in San Francisco died of AIDS; the "
      "collection won the Lenore Marshall Poetry Prize and is the central book of AIDS elegies in English. 'Still "
      "Life' is a memorial for Larry Hoyt, as Neil Powell's obituary of Gunn states.",
  sig="One of the most anthologised poems of The Man with Night Sweats and, with 'The Missing', the representative "
      "of Gunn's AIDS elegies in the Norton Anthology; the collection is credited with restoring poetry to a "
      "public role in the crisis.",
  canon="Minor canon",
  biblio="Published in The Man with Night Sweats (London: Faber and Faber, 1992), collected in Collected Poems "
         "(1993). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on "
         "page 802.",
  notes="The phrases quoted ('I shall not soon forget', 'greyish-yellow skin', the tube 'in an astonished O') are "
        "taken from the text as printed in Neil Powell's Guardian obituary and in the New York Times review; the "
        "dedication to Larry Hoyt is stated by Powell.",
  ver="partially verified", sources=[GUNN_WORLD, W_TG, NAEL]),
W10("The Missing", TG, "1992", "Poem (three twelve-line stanzas)", "significant",
  genres=G("Elegiac Poetry", "Lyric Poetry"),
  themes=T("Death, illness and mourning", "Love, intimacy and loss", "Sexuality, desire and the closet"),
  movements=M("Gay and Lesbian Literature after Stonewall",),
  overview="The central elegy of The Man with Night Sweats: watching his friends die of AIDS, the poet sees himself "
           "as a half-finished statue, outside the warm network of friendships that is disappearing around him.",
  content="Three stanzas of twelve lines in which the speaker watches the plague thin the circle of his friends, "
          "feels his own shape grow sharper and colder as they die, and remembers the 'supple entwinement' of the "
          "community that is being destroyed.",
  summary="'Now as I watch the progress of the plague, / The friends surrounding me fall sick, grow thin, / And "
          "drop away.' The speaker asks whether his own shape is less vague now, bared and sharply exposed, and "
          "answers that he does not like the statue's chill contour, not nowadays: the warmth that used to invest "
          "him went outward through mind and limb and feeling in an 'involved increasing family'. Contact of friend "
          "led to another friend, a 'supple entwinement through the living mass' which might have had no end and "
          "was an image of an unlimited embrace. Now the entwinement is broken and the speaker is left as the "
          "statue, defined by the loss of those who made him. The poem's title carries both senses: the friends are "
          "missing, and the speaker is one of the missing, a survivor who has been left outside the company that "
          "gave him his shape.",
  themes_text="The poem is about identity as relation: the speaker's self was made by the network of friends and "
              "lovers, and their deaths leave him not more himself but less. The statue image reverses the usual "
              "consolation of elegy, since what survives is cold and defined only by absence. The 'unlimited "
              "embrace' gives the gay community of San Francisco a value that the poem states without apology, and "
              "the plague is named as a plague, a public catastrophe experienced privately.",
  structure="Three twelve-line stanzas, unrhymed but metrically regular, moving from the observation of the dying "
            "friends to the self-scrutiny of the statue and then to the remembered embrace; the poem's argument is "
            "carried by a single extended comparison rather than by narrative.",
  style="Iambic pentameter in long stanzas, with a grave, measured movement; the diction is abstract and sculptural "
        "('shape', 'contour', 'definition') set against bodily words ('supple', 'entwinement', 'warmth'); the tone "
        "is elegiac without being rhetorical.",
  ctx="Written in San Francisco in the late 1980s and published in The Man with Night Sweats (1992); the poem's "
      "image of the statue and its 'living mass' belongs to the Gay Liberation culture of the 1970s as much as to "
      "the epidemic that followed it, and the collection is a document of the AIDS years.",
  sig="One of the central poems of The Man with Night Sweats and the longest of Gunn's AIDS elegies to be "
      "anthologised; with 'Still Life' it is his representation in the Norton Anthology and the poem most often "
      "cited for the collection's vision of community.",
  canon="Secondary canon",
  biblio="Published in The Man with Night Sweats (London: Faber and Faber, 1992), collected in Collected Poems "
         "(1993). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on "
         "page 803.",
  notes="The poem's first lines and the 'supple entwinement' passage are quoted from the text printed in the New "
        "York Times review and in Neil Powell's Guardian obituary; the stanza description follows those texts and "
        "was not checked against the 1992 printing.",
  ver="partially verified", sources=[GUNN_WORLD, W_TG, NAEL]),
]

WORKS += [
W10("A Far Cry from Africa", DW, "1962", "Poem (three eight-line stanzas)", "significant",
  genres=G("Political Poetry", "Lyric Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Decolonisation, the end of empire and the new nation",
           "Identity, authenticity and the divided self"),
  movements=M(CAR, POSTCOL),
  overview="Derek Walcott's best-known early poem, collected in In a Green Night (1962): a meditation on the Mau Mau "
           "rebellion in Kenya which asks how a Caribbean poet of African and European descent can take sides in "
           "the violence of decolonisation.",
  content="Three eight-line stanzas on the Kikuyu and the British in Kenya: the 'gorillas' of the Mau Mau, the "
          "colonist with his English tongue, and the speaker's divided inheritance, which leaves him unable either "
          "to condemn the violence or to accept the empire that provoked it.",
  summary="The poem opens on the Mau Mau fighters, described as 'gorillas' wrestling with the British, and sets the "
          "brutality of the uprising against the rhetoric of empire; the 'white child' is speared in his bed while "
          "the Kikuyu 'dance' and the English language is spoken over the dead. Walcott refuses the division: he "
          "is 'poisoned with the blood of both', and the poem turns on the question of how to choose between an "
          "Africa that is his inheritance and the English tongue that is his instrument. 'How choose / Between this "
          "Africa and the English tongue I love?' The stanzas move rapidly between scenes and registers, from the "
          "documentary violence of the rebellion to the lyric address to a 'drunken officer of the Empire', and end "
          "with the poet's confession that he will die 'in a country / Where the trees are tall and the rivers "
          "are wide', neither wholly African nor wholly English. The title's 'far cry' is both distance and "
          "protest, the cry from far away and the difference that cannot be closed.",
  themes_text="The poem is a study of the divided colonial subject: Walcott, descended from English and African "
              "Caribbean ancestors, can neither disown the English language nor accept the empire that brought it, "
              "and the Mau Mau emergency makes that division a matter of life and death. The refusal to take a "
              "side is not neutrality but a historical condition, and the poem's force lies in its refusal to "
              "resolve it into comfort. Race, violence and language are shown to be one question.",
  structure="Three eight-line stanzas of loose pentameter with an irregular rhyme scheme; the poem moves by sudden "
            "transitions between the African and English scenes, and its argument is carried by rhetorical "
            "questions and apostrophes rather than by narrative.",
  style="Rich, allusive, syntactically complex verse, with the English literary inheritance (the Bible and "
        "Shakespeare) heard in the cadence; hard consonants and violent verbs for the rebellion; the mature "
        "Walcott's habit of holding two languages and two histories in a single sentence is already present.",
  ctx="Written in the 1950s and collected in In a Green Night: Poems 1948-1960 (Cape, 1962), the poem responds to "
      "the Mau Mau emergency in Kenya (1952-1960), the most violent episode of British decolonisation in Africa, "
      "and to Walcott's own mixed inheritance in Saint Lucia.",
  sig="Walcott's most frequently anthologised early poem and the standard introduction to his theme of the divided "
      "colonial self; it is the first of his four selections in the Norton Anthology.",
  canon="Major canon",
  biblio="First published in the collection In a Green Night: Poems 1948-1960 (London: Jonathan Cape, 1962); the "
         "date of its first periodical publication was not established, so the poem is dated by its collection. A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 804.",
  notes="The paraphrase follows the text as quoted in the Oxford Research Encyclopedia and the Connotations "
        "article, which print the opening and the 'How choose' question; the exact date of first publication is "
        "given as 1962 in the Norton list, and no earlier printing was found, so the record follows the collection.",
  ver="partially verified", sources=[WALCOTT_OX, W_DW, NAEL]),
W10("The Schooner Flight", DW, "1979", "Poem (eleven-section narrative poem)", "major",
  genres=G("Narrative Poetry", "Long Poem", "Political Poetry"),
  themes=T("Migration, exile and diaspora", "Race, racism and the struggle for civil rights",
           "Nationhood and national identity"),
  movements=M(CAR, POSTCOL),
  overview="The long monologue of Shabine, a mixed-race sailor who leaves Trinidad on the schooner Flight, from The "
           "Star-Apple Kingdom (1979): Walcott's most ambitious poem before Omeros and the fullest statement of "
           "his vision of Caribbean identity, spoken in eleven sections by a man who is 'either nobody, or a "
           "nation'.",
  content="Eleven sections in the voice of Shabine, a sailor nicknamed for the patois for a 'red nigger', who "
          "quarrels with his wife Maria Concepcion, goes to sea on the Flight, remembers the colonial history of "
          "the islands and the massacres of the past, and ends by singing from the depths of the sea.",
  summary="Shabine introduces himself as 'a rusty head sailor with sea-green eyes' whom they nickname Shabine, 'the "
          "patois for any red nigger', a man with Dutch, African and English blood who had a sound colonial "
          "education and is 'either nobody, or a nation'. He fights with his wife Maria Concepcion and leaves "
          "Trinidad on the schooner Flight, and the poem follows the voyage through the islands from Monos to "
          "Nassau. As he sails, Shabine remembers the history of the archipelago: the Amerindian past, the "
          "plantations, the massacres of colonial rule, the corruption of the new states, and his own love for the "
          "sea and for the ordinary people of the islands. He reflects on the poet's vocation, on language and on "
          "the colour line that cuts through his own family, and in the last sections his voice moves out of the "
          "frame of the narrative altogether: 'Shabine sang to you from the depths of the sea.' The poem's "
          "eleven sections are held together by the speaking voice rather than by a plot, and its model is the "
          "Odyssey (Shabine, like Odysseus, is 'nobody') as much as the Caribbean ballad and the calypso. Along "
          "the way the poem registers the corruption of the independent Caribbean states, the continuities of "
          "colonial power and the ordinary decency of the people Shabine sails among, and its narrator's voice is "
          "by turns boastful, tender, furious and elegiac, so that the single monologue holds the whole archipelago "
          "in view without ever settling into a single judgement of it.",
  themes_text="Identity without a single origin: Shabine's mixed descent, which denies him a place in either the "
              "black or the white society of the islands, becomes the ground of a representative Caribbean self, "
              "'either nobody, or a nation'. The poem sets the beauty of the sea and the islands against the "
              "violence of their history, and makes the poet's song the only form of belonging that survives. "
              "Exile is both the wound and the condition of the poetry, and the final transformation of the "
              "speaker into a voice singing from the sea turns loss into art.",
  structure="Eleven numbered sections in a flexible pentameter, spoken by Shabine and interrupted by quoted speech, "
            "song and invective; the narrative is recursive rather than linear, returning to the quarrel with "
            "Maria and to the history of the islands, and the last section dissolves the narrative frame into pure "
            "song.",
  style="A flexible, muscular pentameter carrying the spoken idiom of the islands ('I had a sound colonial "
        "education') and the high rhetoric of the English literary tradition in the same breath; a rapid "
        "succession of registers, from calypso comedy to prophetic denunciation; the sea imagery gives the poem its "
        "recurring music.",
  ctx="Published in The Star-Apple Kingdom (Farrar, Straus and Giroux, 1979; Cape, 1980), the poem belongs to "
      "Walcott's Trinidad years and to the moment of Black Power and the New Jewel Movement in the Caribbean; it "
      "is the poem in which he worked out the long narrative form that Omeros would take up in 1990.",
  sig="Walcott's major poem of the 1970s and the work in which his Caribbean everyman, Shabine, is created; it is "
      "the poem by which his ambition to write a Caribbean epic is usually dated, and a central text of "
      "postcolonial poetry in English. Its pentameter and its speaking sailor are the direct preparation for "
      "Omeros, and its 'either nobody, or a nation' has become the most quoted line in Walcott's work.",
  canon="Major canon",
  biblio="Published in The Star-Apple Kingdom (New York: Farrar, Straus and Giroux, 1979; London: Jonathan Cape, "
         "1980), with sections collected in Selected Poems (2007). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning on page 805.",
  crit="Fuller and later Caribbean critics have made 'The Schooner Flight' the test case for Walcott's politics "
       "of identity, reading Shabine's mixed descent as a rejection of both Black Power's and the colonial "
       "order's claims on him; others have objected that the poem's solution, the transformation of the speaker "
       "into pure song, evades the political questions it raises. Its relation to Omeros has been central to that "
       "debate, since the later poem expands the sailor's monologue into an epic and gives his 'nobody or a "
       "nation' a whole archipelago to inhabit.",
  notes="The passages quoted ('I'm just a red nigger who love the sea', 'either I'm nobody, or I'm a nation', "
        "'Shabine sang to you from the depths of the sea') are taken from Mary C. Fuller's Connotations article "
        "and the Oxford Research Encyclopedia; the section-by-section account is based on that article and on "
        "general knowledge, not on a complete reading of the 1979 text.",
  ver="partially verified", sources=[WALCOTT_CON, WALCOTT_OX, NAEL]),
W10("The Season of Phantasmal Peace", DW, "1981", "Poem (five stanzas)", "significant",
  genres=G("Lyric Poetry", "Religious Poetry"),
  themes=T("War, combat and its aftermath", "Faith, doubt and the sacred", "Nature, ecology and environmental crisis"),
  movements=M(CAR, POSTCOL),
  overview="The short visionary poem that closes The Fortunate Traveller (1981): an imagined peace in which all the "
           "birds of the world carry the light through the dark, and the nations are, for a moment, reconciled.",
  content="A sequence of images in which the birds of many species come together, carrying a light through the "
          "darkness, and the poem addresses the 'season of phantasmal peace' that they bring, a peace that is "
          "neither of this world nor wholly beyond it.",
  summary="The poem imagines all the birds of the world - the shearlings, the albatross, the 'dark-chanting' "
          "pigeons, the birds of every continent - gathering in one place and carrying the light between them "
          "through the night, as the nations of the world cannot. Walcott asks the season of phantasmal peace to "
          "come, and describes the procession of birds as a 'net' of wings that draws the sea and the light "
          "together. The peace is 'phantasmal' because it exists only in the vision of the poem, and the poem's "
          "beauty is inseparable from its awareness that the vision is not history. The last stanzas hold the "
          "moment of reconciliation as long as the poem can, and then release it; the birds return to their "
          "ordinary lives and the poem ends with the image of their flight, which is also the poem's own motion.",
  themes_text="A vision of peace that knows itself to be a vision: the poem sets the unity of the natural world, in "
              "which the birds of every continent share a single flight, against the divisions of the human one, "
              "and offers the poem itself as the only place where the reconciliation can be seen. The religious "
              "language ('phantasmal', the light, the net of wings) is used without orthodox belief, and the "
              "poem's sadness comes from the gap between the image and the world.",
  structure="Five stanzas of long unrhymed lines, moving from the gathering of the birds to the address to the "
            "season and then to the release; the poem's structure is that of a vision that is granted and then "
            "withdrawn, and the single sentence that runs through the first stanzas enacts the continuity of the "
            "flight.",
  style="Long, incantatory free-verse lines with heavy internal assonance and a liturgical cadence; the diction "
        "oscillates between the technical names of birds and the abstract language of vision ('phantasmal', "
        "'peace'); the syntax is elaborate and the imagery sustained, with almost no plot.",
  ctx="The Fortunate Traveller (1981) was Walcott's first book of poems written with his new American academic "
      "life in view, and this poem, which closes it, is his most explicit visionary statement; the critic Mervyn "
      "Morris called it a 'vision of universal love', and other readers have seen in it the limit of the high "
      "style.",
  sig="Walcott's most discussed short visionary poem and the last of his four selections in the Norton Anthology; "
      "it is the poem in which his late style, with its long lines and liturgical movement, is most clearly on "
      "display.",
  canon="Secondary canon",
  biblio="Published as the closing poem of The Fortunate Traveller (New York: Farrar, Straus and Giroux, 1981; "
         "London: Faber and Faber, 1982), collected in Selected Poems (2007). A selection of The Norton Anthology "
         "of English Literature, 11th edition, vol. F, beginning on page 807.",
  notes="The account follows the Oxford Research Encyclopedia, which quotes Mervyn Morris's phrase and describes "
        "the poem as the book's closing visionary piece, and the poem's own reported imagery; the complete text "
        "was not consulted and the description of individual birds is therefore general.",
  ver="partially verified", sources=[WALCOTT_OX, WALCOTT_SEL, NAEL]),
W10("Omeros", DW, "1990", "Epic poem (seven books, sixty-four chapters)", "major",
  genres=G("Epic Poetry", "Long Poem", "Narrative Poetry"),
  themes=T("History, truth and the uses of the past", "Race, racism and the struggle for civil rights",
           "Migration, exile and diaspora"),
  movements=M(CAR, POSTCOL),
  overview="Derek Walcott's epic of Saint Lucia, published in 1990: in seven books and sixty-four chapters of terza "
           "rima, the fishermen Achille and Philoctete, the housemaid Helen and the poet's alter ego traverse the "
           "island, Africa, Europe and North America, and Homer is rewritten from the Caribbean.",
  content="A long narrative poem that interweaves the lives of the St Lucian fishermen Achille and Philoctete and "
          "the beautiful Helen with the poet's own memories of his island, his travels in Europe and America, and "
          "his meditations on history, language and the sea; its characters bear Homeric names and its form is "
          "modelled on the epic.",
  summary="Omeros opens with Philoctete's wound, a leg ulcer he attributes to the curse of the Middle Passage, and "
          "with the fishermen Achille and Hector competing for Helen, the island's Helen of Troy. Walcott's "
          "narrator, a St Lucian poet living in the United States, moves between the island and his memories of "
          "his father, his travels in Europe and America, and the history of the Caribbean; in the middle books "
          "Achille sails to Africa in a vision and encounters his enslaved ancestors, while the poet visits "
          "Dublin, Lisbon and London and meets a blind woman, Ma Kilman, whose shop and church heal Philoctete. The "
          "poem's seven books close with a sequence of farewells: Hector is killed in a bus crash, Helen and "
          "Achille are reconciled, and the poet returns to the island and to the sea, which is the poem's true "
          "subject. The Homeric frame is neither a mask nor a joke: the Odyssey supplies the pattern of voyage and "
          "return, the Iliad the quarrel over Helen, and Walcott rewrites both so that the Caribbean is the centre "
          "and Homer one of its ancestors. Walcott's seven books carry the action through a hurricane, a village "
          "festival and the death of a major character, and each of them closes in a different key, from the "
          "comedy of the market to the elegy of the final voyage home, so that the poem's epic scale is matched by "
          "a lyric attentiveness to the ordinary detail of island life. The narrative returns repeatedly to the "
          "sea, the poem's first and last subject, and to the figure of the poet himself, whose memories of his "
          "father and of his own divided education are woven into the story of the fishermen.",
  themes_text="History and the uses of the past: the poem insists that the Middle Passage is not a gap in the record "
              "but the origin of the Caribbean present, and it gives the wound of Philoctete a historical as well "
              "as a mythic meaning. Race and the colonial inheritance are explored through the mixed descent of "
              "the characters and of the narrator, and exile and return through the poet's own double life in "
              "America. Language is a theme throughout: the poem asks what an epic in English can be when English "
              "is the language of the coloniser, and answers by writing the island's speech into terza rima.",
  structure="Seven books and sixty-four chapters, mostly in terza rima, with lyric interludes and passages of "
            "prose-like narrative; the narrative is polyphonic, moving between the fishermen, Helen, the poet and "
            "historical figures, and its time is cyclical rather than linear, so that the epic voyage and the "
            "middle passage are present in the same moment.",
  style="Terza rima in English, with a flexible pentameter and a high proportion of enjambment; a diction that "
        "mixes the fishermen's Creole with the elaborate rhetoric of the European epic; sustained metaphors of the "
        "sea, the wound and the sword; a syntax of long, suspended sentences; the poem's line is its most "
        "distinctive achievement.",
  ctx="Published by Farrar, Straus and Giroux in 1990, the poem was written in St Lucia, Trinidad and Boston over "
      "the 1980s and marks Walcott's response to the quincentenary of 1492 and to the debate over the Caribbean's "
      "history; it was awarded the W. H. Smith Literary Award and is the work for which he is most often said to "
      "have deserved the Nobel Prize, which came in 1992.",
  sig="The major long poem of the anglophone Caribbean and one of the central English poems of the late twentieth "
      "century; it reopened the epic as a form available to postcolonial writing and gave Saint Lucia its "
      "national poem. Norton prints an extract, and the record covers the whole work.",
  canon="Major canon",
  biblio="Published in 1990 by Farrar, Straus and Giroux (New York) and Faber and Faber (London); seven books, "
         "sixty-four chapters. Norton prints an extract beginning on page 808; this record covers the whole poem.",
  crit="Omeros was received as the major long poem of the Caribbean and has generated a large criticism on its "
       "relation to Homer, to Dante's terza rima and to the epic tradition, and on its politics of history and "
       "race; admirers treat its fusion of Creole speech and classical form as the fulfilment of Walcott's "
       "lifelong project, while sceptical readers have questioned the epic's treatment of women and its "
       "elegiac relation to the colonial past. Its place beside Derek Walcott's Nobel Prize of 1992 is "
       "secure, and it is now the work by which the twentieth-century English epic is usually measured.",
  notes="The account of the seven books and of the main characters follows Wikipedia and the Oxford Research "
        "Encyclopedia and is stated at the level of the poem's overall design; no chapter-by-chapter reading was "
        "attempted, and the description of particular episodes is limited to those documented in those sources.",
  ver="partially verified", sources=[W_OMEROS, WALCOTT_OX, NAEL]),
]

WORKS += [
W10("Wind", TH, "1957", "Poem (five eight-line stanzas)", "significant",
  genres=G("Nature Poetry", "Lyric Poetry"),
  themes=T("Nature, ecology and environmental crisis", "Land, place and regional belonging"),
  movements=M("The Movement",),
  overview="A poem from Ted Hughes's first collection, The Hawk in the Rain (1957): a night of wind on the moor seen "
           "from inside a house that seems to be at sea, in which the storm becomes an image of a power the human "
           "world cannot withstand.",
  content="Five eight-line stanzas describing a night and a day of gale: the house 'far out at sea all night', the "
          "woods crashing, the hills displaced under an orange sky, the poet struggling to the coal-house door, and "
          "the family sitting in front of the fire feeling the roots of the house move.",
  summary="The poem opens with the famous line 'This house has been far out at sea all night', and gives the wind a "
          "body: the woods crash through darkness, the hills boom, and the winds stampede the fields 'floundering "
          "black astride and blinding wet'. Day rises under an orange sky and the hills have new places; the wind "
          "wields a 'blade-light, luminous black and emerald', flexing like the lens of a mad eye. At noon the "
          "speaker scales along the house side to the coal-house door and looks up through wind 'that dented the "
          "balls of my eyes'; the tent of the hills drums and strains its guy-rope, the skyline is 'a grimace' "
          "about to bang and vanish, a magpie is flung away and a black-backed gull bends like an iron bar. The "
          "house rings 'like some fine green goblet in the note / That any second would shatter it', and the poem "
          "ends indoors: the people sit deep in chairs before the fire, gripping their hearts, unable to entertain "
          "book, thought or each other, watching the window tremble to come in and hearing the stones cry out "
          "under the horizons.",
  themes_text="The wind is the poem's absolute: it takes the house out to sea, rewrites the landscape and reduces "
              "human company to silence in front of a fire. Hughes's interest is in the energy that the human world "
              "cannot domesticate, and the poem's images are all of containment about to fail, the goblet, the "
              "tent, the trembling window. The firelit interior at the end is not a refuge but the measure of the "
              "storm outside, and the poem's power comes from the exchange of scales by which a house becomes a "
              "ship and the hills a tent.",
  structure="Five eight-line stanzas rhyming abbaacca or with a loose variant, moving from the night through dawn "
            "and noon to evening indoors; the poem's action is a single storm watched from one house, and its "
            "repetitions (the house, the hills, the fire) give it the feel of a refrain.",
  style="Heavy stresses and dense consonantal clusters ('booming', 'floundering', 'flung'); an imagery of ships, "
        "tents, blades and glass drawn from the moorland world; the personification of the wind as a living body; "
        "a syntax of long suspended sentences released at the stanza's end.",
  ctx="Written in the mid-1950s when Hughes was living in Cambridge and then in Yorkshire, and collected in The "
      "Hawk in the Rain (Faber, 1957), the book that won the New York Poetry Center award and made him the most "
      "talked-about young poet in England; the poem's weather belongs to the Pennine landscape of his childhood.",
  sig="One of the most anthologised poems of Hughes's first book and the standard example of his early nature "
      "writing; it is the first of his six selections in the Norton Anthology and the one that establishes the "
      "elemental weather of his imagination.",
  canon="Secondary canon",
  biblio="Published in The Hawk in the Rain (London: Faber and Faber, 1957), collected in Selected Poems (1972) "
         "and Collected Poems (2003). A selection of The Norton Anthology of English Literature, 11th edition, vol. "
         "F, beginning on page 812.",
  notes="The poem was read complete in the Wondering Minstrels printing; the paraphrase quotes its first line and "
        "the phrases 'floundering black astride and blinding wet', 'dented the balls of my eyes' and 'like some "
        "fine green goblet', which that text and the Collected Poems contents agree on.",
  ver="partially verified", sources=[HUGHES_TEXT, W_TH, NAEL]),
W10("Pike", TH, "1960", "Poem (four stanzas of varying length)", "significant",
  genres=G("Nature Poetry", "Lyric Poetry"),
  themes=T("Nature, ecology and environmental crisis", "Violence, crime and justice", "Childhood, adolescence and coming of age"),
  movements=M("The Movement",),
  overview="A poem from Lupercal (1960) about the pike, the pond's 'killer from the egg', and about the boy who "
           "keeps them in a glass tank and watches them eat each other; one of Hughes's definitive animal poems.",
  content="Four stanzas: pike in a pond among lily pads, a memory of keeping three pike in a glass tank at home until "
          "one ate the others, and a final stanza in which the poet, fishing at night, feels the pond's darkness "
          "and its 'immense' age as something inhuman and listening.",
  summary="The poem begins with pike 'in a pond I know' beneath the lily pads, 'perfect pike in all parts, "
          "green tigering the gold' - the phrase that fixes the fish's colour and its predatory nature. Hughes "
          "describes their stillness, their jaws and their patience, then remembers keeping three in a glass tank "
          "at home, where two were eaten and the survivor 'grinned' at the dark. The last stanza moves to a pond at "
          "night, where the poet casts for pike and feels, in the darkness and the depth, something immense and "
          "listening, older than the human world. The poem is at once exact natural history and myth: the pike is "
          "a 'killer from the egg', and the pond at night becomes a place where the human observer is the one "
          "watched.",
  themes_text="Predation as a fact of nature that human moral language cannot contain: the pike is beautiful and "
              "murderous at once, and the poem's admiration for it is an admiration for a life that has no "
              "conscience. The memory of the glass tank turns the poem into an anecdote about a boy's education in "
              "the reality of violence, and the final stanza makes the pond itself a presence, so that nature is "
              "shown as both creature and place. The poem refuses the sentimental view of nature without "
              "substituting a merely brutal one.",
  structure="Four stanzas of unequal length, moving from the pond, to the pike's appearance, to the remembered tank, "
            "to the night fishing; the poem's structure is a widening of frame from the observed fish to the "
            "observer's own exposure, and its last line returns to the water.",
  style="Hard, exact consonants and an imagery of armour and weaponry ('iron', 'jaw', 'grin'); the compound "
        "epithets and the verb-derived adjectives ('green tigering', 'gold') give the fish a heraldic presence; "
        "the metre is loose, the line-endings often run on, and the diction is drawn from angling and natural "
        "history.",
  ctx="Lupercal (Faber, 1960) was Hughes's second collection and confirmed his reputation; the poem belongs to the "
      "Yorkshire and Devon fishing country of his boyhood and to the postwar nature poetry that reacted against "
      "the genteel tradition of Georgian verse.",
  sig="One of the two or three poems by which Hughes's animal poetry is universally represented, and the second of "
      "his six selections in the Norton Anthology; 'green tigering the gold' is among the most quoted lines in "
      "postwar English poetry.",
  canon="Major canon",
  biblio="Published in Lupercal (London: Faber and Faber, 1960), collected in Selected Poems (1972) and Collected "
         "Poems (2003). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning "
         "on page 812.",
  notes="The paraphrase follows the poem as quoted in school and anthology extracts and in general knowledge of the "
        "text; the phrases quoted ('green tigering the gold', 'killer from the egg') were checked in those "
        "extracts, and the stanza count follows the standard printing, which was not collated with the 1960 "
        "edition.",
  ver="partially verified", sources=[W_TH, HUGHES_CP, NAEL]),
]

WORKS += [
W10("Out", TH, "1967", "Poem (short lyric)", "minor",
  genres=G("Lyric Poetry", "Dark Fantasy"),
  themes=T("Violence, crime and justice", "Death, illness and mourning"),
  movements=M("The Movement",),
  overview="A short poem from Wodwo (1967) in which a child is turned out of the house into a world that will not "
           "have him, and the poem's brutal little fable becomes one of Hughes's starkest studies of rejection.",
  content="A few lines of hard, nursery-rhyme-like verse: a figure is put out of doors, and the world beyond the "
          "door is shown to be as pitiless as the hand that expelled him.",
  summary="'Out' is one of the shortest poems in Wodwo: a child, or a creature in the shape of a child, is put out "
          "of the house, and the poem follows him into a landscape that offers nothing. The diction is bare and "
          "the lines short, so that the poem reads like a fragment of a ballad or a bad dream; the figure's "
          "expulsion is presented without explanation, and the world outside is described with the same "
          "matter-of-factness as the door closing behind him. The poem's power lies in what it withholds: no reason "
          "is given for the expulsion, no rescue follows, and the 'out' of the title is both a direction and a "
          "state of being. It belongs with the Wodwo poems in which Hughes explored the boundary between the human "
          "and the animal, and with the poems of Crow in its vision of a creature alone in a hostile creation.",
  themes_text="Rejection and exposure: the poem makes a small parable of being cast out, and it refuses the "
              "consolations of either explanation or protest. The child-figure's solitude is the human condition "
              "as Hughes's poems of the mid-1960s saw it, a creature in a world not made for him, and the poem's "
              "brevity is part of its cruelty.",
  structure="A short poem in uneven short lines, without narrative development; its shape is that of an anecdote "
            "cut off before it can comfort, and the last line closes the door on the figure as the poem began by "
            "closing the house's.",
  style="Bare diction and short lines, with hard consonant sounds and little metaphor; the poem's flatness is "
        "deliberate, so that the horror is carried by the absence of comment; it has the quality of a fragment or "
        "a charm.",
  ctx="Wodwo (Faber, 1967) was Hughes's third collection and the one in which he moved from the animal poems of his "
      "first two books towards the mythic sequences of Crow; the title poem, 'Wodwo', is spoken by a creature "
      "between animal and man, and 'Out' belongs to the same exploration.",
  sig="A frequently anthologised short poem of Wodwo and the third of Hughes's six selections in the Norton "
      "Anthology; its compression makes it a standard example of his mid-period manner.",
  canon="Minor canon",
  biblio="Published in Wodwo (London: Faber and Faber, 1967), collected in Collected Poems (2003). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 813.",
  notes="The full text was not consulted; the record describes the poem from general knowledge and from its place "
        "in the Wodwo sequence, and it deliberately makes no quotation and no claim about details it could not "
        "verify. The poem's shortness and its situation are certain; the specific imagery is not described.",
  ver="unverified", sources=[HUGHES_CP, NAEL]),
W10("Theology", TH, "1967", "Poem (eight short lines)", "minor",
  genres=G("Religious Poetry", "Satirical Fiction"),
  themes=T("Faith, doubt and the sacred", "Nature, ecology and environmental crisis"),
  movements=M("The Movement",),
  overview="An eight-line comic poem from Wodwo (1967) that retells the Fall as a food chain: Adam ate the apple, Eve "
           "ate Adam, the serpent ate Eve, and God goes calling through Paradise while the serpent sleeps off his "
           "meal.",
  content="A short, sardonic rewriting of Genesis in which the characters of Eden devour one another in turn, "
          "leaving the serpent asleep and God's voice unanswered.",
  summary="The poem's whole text is a joke with a theological edge: 'No, the serpent did not / Seduce Eve to the "
          "apple. / All that's simply / Corruption of the facts.' What happened, the poem says, is that Adam ate "
          "the apple, Eve ate Adam, the serpent ate Eve, and this is 'the dark intestine'. The serpent, meanwhile, "
          "sleeps his meal off in Paradise, smiling to hear God's querulous calling. In eight short lines Hughes "
          "converts the Fall into a food chain and makes digestion the truth of the story, so that the human claim "
          "to a special relation with God is reduced to a place in the same intestine as everything else. The "
          "comedy is savage rather than light: the serpent's smile and God's 'querulous' voice are the poem's only "
          "expressions of feeling, and both are unflattering.",
  themes_text="The poem sets the biblical account of the Fall against the facts of predation and digestion, and finds "
              "in the food chain a more honest theology than the story of seduction. God is reduced to a voice "
              "calling querulously in a Paradise where the serpent sleeps, and the human pretension to moral "
              "centrality is the poem's real target. The comic tone is the vehicle of a bleak vision, and the "
              "phrase 'the dark intestine' gives the poem its image of a universe that consumes its creatures.",
  structure="Eight short lines in two sentences, the first correcting the record and the second giving the true "
            "sequence of eating; the poem's structure is that of a joke with a punchline, and the final couplet "
            "withdraws to the sleeping serpent and the distant God.",
  style="Colloquial, clipped sentences and a flatly comic tone; the short line and the absence of ornament make the "
        "bathos work; the diction is deliberately ordinary ('Corruption of the facts', 'Sleeps his meal off'), and "
        "the only poetic word is the closing 'querulous'.",
  ctx="One of the short poems of Wodwo (1967), written while Hughes was working on the Crow material; its comic "
      "rewriting of Genesis anticipates the Crow poems' treatment of the biblical story as raw material for "
      "myth, and its God is the same baffled creator who appears in Crow.",
  sig="A frequently quoted short poem and a compact example of Hughes's myth-making comedy; it is the fourth of his "
      "six selections in the Norton Anthology and the shortest of them.",
  canon="Minor canon",
  biblio="Published in Wodwo (London: Faber and Faber, 1967), collected in Collected Poems (2003). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 815.",
  notes="The quoted lines ('No, the serpent did not / Seduce Eve to the apple', 'Corruption of the facts', 'the "
        "dark intestine', 'Sleeps his meal off in Paradise', 'querulous') were read in a quotation flashcard set "
        "of Hughes's poems, which prints the poem complete; the reading is the record's own.",
  ver="partially verified", sources=[HUGHES_CP, W_TH, NAEL]),
W10("Crow's Last Stand", TH, "1970", "Poem (ten short lines)", "minor",
  genres=G("Mythological Retelling", "Dark Fantasy"),
  themes=T("Death, illness and mourning", "Nature, ecology and environmental crisis"),
  movements=M("The Movement",),
  overview="A poem from Crow (1970) in which the sun burns the world down to one thing it cannot consume: Crow's "
           "eye-pupil, 'in the tower of its scorched fort'.",
  content="A single sentence of ten short lines describing a conflagration in which everything is burned and "
          "rendered down, until the fire meets the black pupil of Crow's eye and cannot burn it.",
  summary="'Burning burning burning there was finally something / The sun could not burn.' The poem imagines a "
          "universal fire in which the world is 'rendered / Everything down' to a final obstacle against which the "
          "sun rages and chars; among the glaring furnace clinkers, the pulsing blue tongues and the red, yellow "
          "and green lickings of the conflagration, the one thing that survives is 'Limpid and black - Crow's "
          "eye-pupil, in the tower of its scorched fort'. The poem is a single sentence, and its movement is from "
          "the general burning to the minute, indestructible point of the eye; the echo of the witches' 'burning, "
          "burning, burning' in Macbeth gives the poem a liturgical refrain. Crow, the trickster of the sequence, "
          "survives the end of the world by being the one thing fire cannot eat, and the last image makes the eye "
          "a fortress in a burnt landscape.",
  themes_text="Survival as the poem's subject: the fire consumes everything except the black pupil, and the poem "
              "finds in that exception an image of the stubborn persistence of life, or of consciousness, at the "
              "end of the world. The 'scorched fort' gives the eye a military and architectural presence, so that "
              "the creature's survival is a last stand rather than a triumph. The poem's comedy is grim, and it "
              "belongs to Crow's larger comedy of a creation that cannot be finished off.",
  structure="One sentence in ten short lines, moving from the general burning to the single surviving point; the "
            "repetition of 'burning' at the start and the dash that introduces the eye at the end give it the "
            "shape of an apocalypse in miniature.",
  style="Incantatory repetition, hard consonants and a vocabulary of fire and metal ('furnace clinkers', 'scorched "
        "fort'); the short lines have the force of a chant, and the one long phrase ('Limpid among the glaring "
        "furnace clinkers') holds the poem's only elaborate image.",
  ctx="Crow (Faber, 1970) was written in the late 1960s after the death of Sylvia Plath and in the period of "
      "Hughes's reading of myth, folklore and the occult; the sequence presents Crow as a trickster who survives "
      "the destruction of the world, and 'Crow's Last Stand' is one of its closing poems.",
  sig="A frequently anthologised poem of Crow and the fifth of Hughes's six selections in the Norton Anthology; its "
      "image of the eye in the burnt fort is one of the sequence's most memorable.",
  canon="Minor canon",
  biblio="Published in Crow: From the Life and Songs of the Crow (London: Faber and Faber, 1970), collected in "
         "Collected Poems (2003). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, "
         "beginning on page 815.",
  notes="The poem's text was read in the Genius page for 'Crow's Last Stand', which prints it complete; the Macbeth "
        "echo is a standard observation and the reading is the record's own.",
  ver="partially verified", sources=[HUGHES_CP, NAEL]),
]

WORKS += [
W10("Crow Tyrannosaurus", TH, "1970", "Poem (twenty-nine short lines)", "significant",
  genres=G("Mythological Retelling", "Dark Fantasy"),
  themes=T("Nature, ecology and environmental crisis", "Violence, crime and justice", "Death, illness and mourning"),
  movements=M("The Movement",),
  overview="One of the central poems of Crow (1970): walking through creation, Crow hears the whole food chain at "
           "work and asks whether he should stop eating and try to become the light, before his own body stabs at "
           "a grub.",
  content="Crow walks through a creation in which every creature is eating another: a bird carries the anguish of the "
          "insects it has swallowed, cats and dogs and man are abbatoirs of innocents, and Crow, horrified, "
          "considers giving up eating - then sees a grub and stabs.",
  summary="The poem begins with a sound: 'Creation quaked voices - / It was a cortege / Of mourning and lament.' "
          "Crow hears and looks around fearfully as a swift's body flees past, pulsating with the insects it has "
          "eaten 'and their anguish'; the world is a funeral procession of the eaten. He sees the predators above "
          "and below him, cats and dogs and then a man, 'a walking / Abattoir / Of innocents', whose brain "
          "incinerates their outcry, and he wonders if he should stop eating and try to become the light. But his "
          "eye sees a grub, and his head, 'trap sprung', stabs: he listens and hears weeping, grubs, grubs, and "
          "stabs again, weeping. The poem's comedy and horror are inseparable: Crow's moral revolt lasts a few "
          "lines and his nature wins, and the poem ends not with judgement but with the sound of the bird's own "
          "eating.",
  themes_text="The poem makes the food chain a vision of universal suffering and finds that consciousness cannot "
              "escape it: Crow, who can hear the anguish of everything that has been eaten, is himself a predator, "
              "and his brief wish to 'become the light' is defeated by his body. Hughes's target is the human "
              "claim to stand outside nature as its judge, and the man as 'walking abattoir' is the poem's most "
              "savage image. The grub at the end gives the vision its scale: the catastrophe is a bird's beak in "
              "the grass.",
  structure="Twenty-nine short lines without stanza breaks, moving from the sound of creation to Crow's vision of "
            "the predators to his resolution and its collapse; the poem's sentences are broken by dashes and "
            "exclamations, and the last lines shorten as the bird's attention narrows to the grub.",
  style="Short, hard-stressed free verse, with frequent dashes and a syntax of interrupted thought; the vocabulary "
        "is violent and technical ('abattoir', 'incinerating', 'trap sprung'), the images of predation exact; the "
        "repetition of 'grubs grubs' and 'stabbed stabbed' gives the ending a gruesome music.",
  ctx="From Crow: From the Life and Songs of the Crow (Faber, 1970), the sequence written in the years after Sylvia "
      "Plath's death and dedicated to the memory of the Crow's creator; the poem is one of the sequence's fullest "
      "statements of its vision of a creation that is all appetite, and Hughes's later poems and essays return to "
      "it.",
  sig="The most discussed single poem of Crow and the last of Hughes's six selections in the Norton Anthology; its "
      "'walking abattoir' and Crow's failed resolution are central to the reading of the sequence as myth.",
  canon="Secondary canon",
  biblio="Published in Crow: From the Life and Songs of the Crow (London: Faber and Faber, 1970), collected in "
         "Collected Poems (2003). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, "
         "beginning on page 816.",
  notes="The parody of poetic bird-description and the 'cortege / Of mourning and lament' passage were read in the "
        "DiVA thesis on Crow, which quotes them; the later lines are described from general knowledge of the poem "
        "and are not quoted, and the account makes no claim beyond what those two sources support.",
  ver="partially verified", sources=[CROW_THESIS, HUGHES_CP, NAEL]),
W10("Civil Peace", CA, "1971", "Short story", "significant",
  genres=G("Short Story", "War Novel", "Realist Fiction"),
  themes=T("War, combat and its aftermath", "Family, marriage and domestic life", "Faith, doubt and the sacred"),
  movements=M(AFR),
  overview="Chinua Achebe's story of 1971, collected in Girls at War and Other Stories (1972), about Jonathan Iwegbu "
           "and his family in the 'civil peace' after the Nigerian Civil War, and the robbery that tests his "
           "extraordinary optimism.",
  content="A short story set in eastern Nigeria just after the Biafran war: Jonathan Iwegbu, who has survived with "
          "his wife and three of his four children, turns his bicycle into a taxi, finds his house still standing, "
          "sets his family to selling mangoes and akara, receives an 'egg rasher' from the Treasury, and is robbed "
          "of it by armed men - after which he goes on with his life.",
  summary="The story opens in the aftermath of the war, when Jonathan Iwegbu is pleased with himself and with his "
          "bicycle, which he turns into a taxi and which earns him a hundred and fifteen pounds in two weeks. He "
          "travels to Enugu and finds his house still standing among the ruins, patches it up, brings his family "
          "back, and sets them all to work: the children pick mangoes to sell to soldiers' wives and his wife "
          "Maria makes akara balls for the neighbours. He learns that his old job as a miner is finished, so he "
          "opens a bar at home for the customers of the mineral water he used to sell. He receives an 'egg rasher' "
          "of twenty pounds from the Treasury for handing in rebel currency, and that night a band of robbers "
          "demands a hundred pounds; when he says he has only twenty, the leader takes it through the window and "
          "the gang leaves. The story ends with Jonathan and his family going back to sleep and to work, his "
          "repeated phrase 'Nothing puzzles God' standing as the story's answer to the robbery.",
  themes_text="The story's subject is survival, and its measure is Jonathan's phrase 'Nothing puzzles God', which "
              "holds together gratitude for what has been kept - his head, his wife's head, three of his four "
              "children's heads - and a refusal of despair over what has been lost. Achebe neither sentimentalises "
              "the optimism nor ironises it: the robbery is real, the war was real, and the family's ability to go "
              "on is presented as a strength rather than a blindness. The 'civil peace' of the title is a bitter "
              "phrase for a peace without justice, in which armed men take what a family has just earned, and the "
              "story's quietness makes the point that the poor carry the cost of the war and of the peace.",
  structure="A single narrative in short scenes, moving from the bicycle to the house to the family's work to the "
            "bar to the robbery and the morning after; the story is told in a plain chronological sequence by a "
            "third-person narrator who stays close to Jonathan's point of view, and its ending returns to the "
            "family's daily routine.",
  style="A plain, bare, reportorial prose, with dialogue in Nigerian English and the cadences of Igbo speech; "
        "proverbs and the repeated catchphrase carry the moral weight; the detail is domestic and exact (the "
        "bicycle, the mangoes, the akara, the egg rasher); Achebe's irony is light and the story's tone is warm "
        "without being sentimental.",
  ctx="Published in 1971, a year after the end of the Nigerian Civil War (1967-1970) and the defeat of Biafra, the "
      "story belongs to the literature of the war that also produced Achebe's poems of Beware, Soul Brother; the "
      "'egg rasher' (ex gratia) payment was a real postwar measure, and the story's eastern Nigerian setting is "
      "the Biafran heartland that Achebe had supported.",
  sig="One of the most anthologised Nigerian short stories in English and the Achebe prose selection in the Norton "
      "Anthology; it is the standard short introduction to his treatment of the civil war and to the Igbo "
      "survivor's resilience.",
  canon="Secondary canon",
  biblio="Published in 1971 and collected in Girls at War and Other Stories (London: Heinemann, 1972). A selection "
         "of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 818.",
  notes="The plot follows the Wikipedia summary, checked against general knowledge of the story; the dialogue and "
        "the phrase 'Nothing puzzles God' are quoted from that summary, which uses the text's own words. The "
        "Nigerian Civil War dates and the ex gratia payment are confirmed in the same article.",
  ver="partially verified", sources=[W_CP, W_CA, NAEL]),
]

MU = "Alice Munro"
GH = "Geoffrey Hill"
MUNRO_READ = "Alice Munro, 'Walker Brothers Cowboy' (reading blog, emeire)"
HILL_KINGS = "Geoffrey Hill, 'Requiem for the Plantagenet Kings' (poeticous text)"

AUTHORS += [
A10(MU, MAJ, "1931", "2024", "Wingham, Ontario, Canada",
  "Canadian; short-story writer in English",
  "Canadian short-story writer and Nobel laureate whose stories of small-town Ontario and of women's lives, from "
  "Dance of the Happy Shades to Dear Life, remade the short story as a form of long, retrospective knowledge",
  "Alice Ann Laidlaw was born on 10 July 1931 on a fox farm outside Wingham, in Huron County, Ontario, the daughter "
  "of Robert Laidlaw, a fox farmer who later worked as a foundry labourer and watchman, and Anne Clarke, a "
  "schoolteacher. She read English at the University of Western Ontario, where she spent two years, and married "
  "James Munro in 1951, moving with him to Vancouver, where she ran a bookshop and began publishing stories in "
  "Canadian periodicals. Her first collection, Dance of the Happy Shades, appeared in 1968 and won the Governor "
  "General's Award; it was followed by Lives of Girls and Women (1971), a sequence of linked stories that reads as "
  "a novel, Something I've Been Meaning to Tell You (1974), Who Do You Think You Are? (1978), The Moons of Jupiter "
  "(1982), The Progress of Love (1986), Friend of My Youth (1990), Open Secrets (1994), The Love of a Good Woman "
  "(1998), Hateship, Friendship, Courtship, Loveship, Marriage (2001), Runaway (2004), The View from Castle Rock "
  "(2006), Too Much Happiness (2009) and Dear Life (2012). She separated from her first husband and lived from the "
  "1970s with Gerald Fremlin in Clinton, Ontario, and in Comox, British Columbia. She won the Man Booker "
  "International Prize in 2009 and the Nobel Prize in Literature in 2013, and died at Port Hope, Ontario, on 13 "
  "May 2024.",
  "Stories: Dance of the Happy Shades (1968), Something I've Been Meaning to Tell You (1974), Who Do You Think You "
  "Are? (1978), The Moons of Jupiter (1982), The Progress of Love (1986), Friend of My Youth (1990), Open Secrets "
  "(1994), The Love of a Good Woman (1998), Hateship, Friendship, Courtship, Loveship, Marriage (2001), Runaway "
  "(2004), The View from Castle Rock (2006), Too Much Happiness (2009) and Dear Life (2012). Lives of Girls and "
  "Women (1971) is a sequence of linked stories. Selected Stories appeared in 1996 and Family Furnishings: "
  "Selected Stories 1995-2014 in 2014.",
  "Plain, unhurried prose that moves freely in time, beginning in the middle or near the end of a life and working "
  "back; the reveal withheld until the last paragraph; a narrator who is often a woman looking back at a girl's "
  "misunderstanding; the ordinary Ontario small town rendered with documentary exactness and no condescension.",
  "The gap between what a child or a young woman understands and what has actually happened; sex, marriage and the "
  "unequal arrangements between men and women; class and respectability in small-town Ontario; the work of memory "
  "and the way a life is revised in the telling; the natural world and the farm as a place of labour and of "
  "casual cruelty.",
  "The most important writer of short stories in English in the second half of the twentieth century, and the "
  "first Canadian to win the Nobel Prize in Literature; her stories are credited with widening the form's "
  "capacity for time, memory and moral ambiguity, and she is the standard against which later short-story writers "
  "in English are measured.",
  bib_status="incomplete",
  bib_note="The list of collections is taken from Wikipedia and general knowledge and checked against the "
           "published volumes' titles and dates; only the Norton selection, 'Walker Brothers Cowboy' (in Dance of "
           "the Happy Shades, 1968), has a work record, so the bibliography is incomplete. The stories themselves "
           "are not recorded individually, and no text of them was consulted beyond the summaries cited for the "
           "Norton story.",
  ver="partially verified", sources=["Alice Munro's Dance of the Happy Shades, 50 Years Later (The Atlantic)"]),
A10(GH, MAJ, "1932", "2016", "Bromsgrove, Worcestershire, England",
  "English; poet and professor, teaching in Leeds and then at Boston University from 1988, writing in English",
  "English poet of history, guilt and the religious conscience, whose dense, formally exact poems from For the "
  "Unfallen to Broken Hierarchies made him the most admired and most difficult poet of his generation",
  "Geoffrey William Hill was born on 18 June 1932 in Bromsgrove, Worcestershire, the son of a policeman, and grew "
  "up in the Worcestershire village of Fairfield. He read English at Keble College, Oxford, where he was taught "
  "by F. W. Bateson, and worked as a schoolteacher and lecturer before becoming a professor of English at Leeds, "
  "where he taught from 1981 to 1988. His first collection, For the Unfallen, appeared in 1959 from the Fantasy "
  "Press, and established the historical and elegiac manner of his early work; King Log (1968), which won the "
  "Hawthornden Prize, was followed by Mercian Hymns (1971), a sequence of thirty prose poems about Offa, king of "
  "Mercia, and his own childhood, Tenebrae (1978), The Mystery of the Charity of Charles Péguy (1983), the "
  "Collected Poems (1985), Canaan (1996), The Triumph of Love (1998), Speech! Speech! (2000), The Orchards of "
  "Syracuse (2002), A Treatise of Civil Power (2007), Odi Barbare (2012) and The Book of Baruch by the Gnostic "
  "Justin (2015); his poems were gathered in Broken Hierarchies: Poems 1952-2012 (2013). He taught at Boston "
  "University from 1988 and died in Cambridge on 30 June 2016.",
  "Poetry: For the Unfallen (1959), Preghiere (1964), King Log (1968), Mercian Hymns (1971), Tenebrae (1978), The "
  "Mystery of the Charity of Charles Péguy (1983), Collected Poems (1985), Canaan (1996), The Triumph of Love "
  "(1998), Speech! Speech! (2000), The Orchards of Syracuse (2002), A Treatise of Civil Power (2007), Odi Barbare "
  "(2012) and The Book of Baruch by the Gnostic Justin (2015); Broken Hierarchies: Poems 1952-2012 (2013). "
  "Criticism: The Lords of Limit (1984), The Enemy's Country (1991) and Style and Faith (2003).",
  "Dense, allusive, syntactically compressed verse in strict forms; the early poems in regular stanzas and "
  "pentameters, the later in a baroque, punning, self-interrogating free verse; a vocabulary drawn from law, "
  "theology, music and etymology; the prose poems of Mercian Hymns; a habit of quotation and of echoing earlier "
  "English poets.",
  "History as guilt and complicity, from the Wars of the Roses to the Holocaust and the twentieth-century state; "
  "the English past and the English landscape (Offa's Mercia, the Welsh border); religious faith, grace and "
  "theology, especially in Tenebrae; the poet's vocation and its compromised relation to power and money; "
  "language itself as a fallen, contested inheritance.",
  "The most highly regarded English poet of his generation, the central figure in the revival of a difficult, "
  "historically conscious and religiously serious poetry after the Movement, and a poet whose later work divided "
  "readers into those who found in it the fullest statement of the century's guilt and those who found it "
  "obscure, bombastic and increasingly a poetry of commentary rather than creation.",
  bib_status="incomplete",
  bib_note="The books are listed from Wikipedia's bibliography and checked against the contents of Broken "
           "Hierarchies (2013) for the poems of 1959 and 1968. Installment 10 records only the three dated Norton "
           "selections ('In Memory of Jane Fraser' and 'Requiem for the Plantagenet Kings', 1959; 'September "
           "Song', 1968), so the bibliography is incomplete; 'Broken Hierarchies' (the 2013 collection) is "
           "undated in the Norton list and is not recorded. The prose and the later collections have no records.",
  ver="partially verified", sources=[HILL_PF, HILL_OUP]),
]

WORKS += [
W10("In Memory of Jane Fraser", GH, "1959", "Poem (five quatrains)", "minor",
  genres=G("Elegiac Poetry", "Religious Poetry"),
  themes=T("Death, illness and mourning", "Faith, doubt and the sacred", "Gender, feminism and women's lives"),
  movements=M("The Movement",),
  overview="An elegy from Geoffrey Hill's first collection, For the Unfallen (1959), for a woman who kept her house "
           "through a hard winter and died in it, and whose death the poem sets against the thaw that follows.",
  content="Five quatrains: a winter landscape of snow and cold, a woman besieged in her house, the thaw that comes "
          "after her death and the speaker's address to the dead woman, whose keeping of the house becomes an "
          "image of endurance and of its limit.",
  summary="The poem begins with snow lying 'like sheep' in the fold, winds begging at every door, hills blue with "
          "cold and a cold shroud on the moor, and a woman who 'kept the siege' - the poem's military metaphor "
          "makes her house a fortress and her dying an act of defence. The seasons turn: the thaw comes, the "
          "water runs, and the world goes on without her, so that her death is set against a nature that is "
          "indifferent rather than consoling. The last stanzas address her directly, and the poem closes on the "
          "speaker's sense of her as someone whose patience and refusal to surrender were both her virtue and the "
          "condition of her death. Hill later disliked the poem intensely, reprinted an amended version as an "
          "appendix to King Log and called its publication 'a necessary penitential exercise' - a judgement that "
          "has not stopped it from becoming one of his most anthologised early poems.",
  themes_text="The elegy's subject is a death understood through the metaphors of siege and season: the woman's "
              "keeping of the house is courage, and the thaw that follows is the world's indifference. Hill's "
              "religious imagination is present in the liturgical cadence and in the image of the shroud, but "
              "there is no consolation, only the exact registration of a loss. The poem also shows the early "
              "Hill's characteristic procedure, the reading of a private grief through a public and historical "
              "vocabulary.",
  structure="Five quatrains rhyming abab, moving from the winter landscape to the siege, then to the thaw and the "
            "address to the dead; the poem's turn comes at the point where the season changes and the elegy "
            "becomes a meditation on survival.",
  style="Tight quatrains in regular metre, with an archaic, almost ballad-like simplicity of diction ('kept the "
        "siege', 'shroud', 'fold') and a landscape drawing on the English pastoral; the imagery is homely and "
        "biblical at once, and the tone is restrained to the point of coldness.",
  ctx="For the Unfallen (1959) appeared from the Fantasy Press when Hill was twenty-seven, and its poems of "
      "history and elegy were taken as a rebuke to the Movement's domestic ironies; the volume's title promises a "
      "memorial for the living, and this poem is one of its earliest elegies.",
  sig="One of the best-known poems of Hill's first collection and a standard anthology piece; the Norton Anthology "
      "prints it as the first of his four selections, and Hill's own later repudiation of it has made it a case "
      "study in the poet's relation to his early work.",
  canon="Minor canon",
  biblio="Published in For the Unfallen: Poems 1952-1958 (London: The Fantasy Press, 1959); an amended version was "
         "printed as an appendix to King Log (1968). A selection of The Norton Anthology of English Literature, "
         "11th edition, vol. F, beginning on page 833.",
  notes="The first stanza is quoted from the text printed in the Poetry Foundation essay and in the poeticous "
        "selection, which agree; Hill's remark about the amended version is quoted from the Poetry Foundation "
        "essay. The paraphrase of the closing stanzas is general and makes no further quotation.",
  ver="partially verified", sources=[HILL_PF, HILL_OUP, NAEL]),
W10("Requiem for the Plantagenet Kings", GH, "1959", "Poem (three quatrains)", "minor",
  genres=G("Elegiac Poetry", "Historical Writing"),
  themes=T("History, truth and the uses of the past", "War, combat and its aftermath", "Power, the state and surveillance"),
  movements=M("The Movement",),
  overview="A short historical elegy from For the Unfallen (1959) for the Plantagenet kings, in which the violence of "
           "medieval England is offered to the modern reader as a burden of inheritance rather than a spectacle.",
  content="Three quatrains addressing the dead kings and their age, in which the poet asks that the past be allowed "
          "to rest and admits that it cannot, since the violence of the Plantagenet centuries survives in the "
          "language and the land.",
  summary="The poem is an address to the Plantagenet dead, whose wars and cruelties it names without "
          "sentimentalising: the kings are remembered for their violence, and the poem's request is that they be "
          "released from the memory that keeps them alive. Hill's characteristic move is to make the modern poet "
          "the one who cannot let them go, so that the elegy becomes an acknowledgement of complicity: the "
          "historical crimes are not past, because the language in which they are mourned is their inheritance. "
          "The requiem is therefore double - for the kings and for the England that produced them - and the "
          "poem's brevity keeps it from any consoling resolution.",
  themes_text="History as a burden that the present carries rather than a story it has finished with: the poem "
              "refuses the comfortable distance of the historical poem and makes the act of remembrance itself "
              "part of the guilt. The Plantagenet kings stand for the whole inheritance of English power, and the "
              "requiem's liturgical form gives the poem a public, ceremonial weight that its scepticism "
              "undermines.",
  structure="Three quatrains, with a single sentence or two carrying most of the poem, moving from the address to "
            "the kings to the poet's own position; the turn is from commemoration to self-implication.",
  style="Compressed, formal quatrains with a strong caesura and a deliberate archaism of diction; the metre is "
        "regular and the rhyme exact, and the poem's difficulty lies in its syntax rather than its vocabulary; the "
        "tone is ceremonial and cold.",
  ctx="One of the historical poems of For the Unfallen (1959), written in the 1950s when the memory of the Second "
      "World War and the moral claims of English history were live literary questions; the Plantagenet theme "
      "anticipates the Mercian Hymns of 1971.",
  sig="A standard early Hill poem and the second of his four selections in the Norton Anthology; it is the poem by "
      "which his treatment of English history is usually introduced.",
  canon="Minor canon",
  biblio="Published in For the Unfallen: Poems 1952-1958 (London: The Fantasy Press, 1959) and collected in Broken "
         "Hierarchies: Poems 1952-2012 (2013). A selection of The Norton Anthology of English Literature, 11th "
         "edition, vol. F, beginning on page 834.",
  notes="The record describes the poem from the account of For the Unfallen in the Poetry Foundation essay and "
        "from the poem's title and known form; the text was not read complete, and the paraphrase therefore makes "
        "no quotation and no claim about individual stanzas beyond their number.",
  ver="partially verified", sources=[HILL_PF, HILL_OUP, NAEL]),
W10("September Song", GH, "1968", "Poem (six short sections)", "significant",
  genres=G("Elegiac Poetry", "Political Poetry"),
  themes=T("The Holocaust, atrocity and historical memory", "War, combat and its aftermath", "Death, illness and mourning"),
  movements=M("The Movement",),
  overview="A poem from King Log (1968) for a child killed in the Holocaust, written as a birthday elegy that "
           "addresses the dead child by the date of birth and refuses every consolation.",
  content="Six short sections, some of them a single line, in which the poet names a child born in 1936 or 1937 and "
          "killed in the camps, and measures the ordinary English September against the fact of the murder.",
  summary="The poem begins 'September Song' and gives a date of birth, 'born 19.6.32', and a date of death, "
          "'deported 24.9.42', as though it were an archival record, then addresses the child directly. The date "
          "is also a birthday: the poem's title and its opening make the reader expect a song of the season, and "
          "the bureaucratic exactness of the dates turns it into an elegy for a specific murdered child. Hill "
          "refuses the rhetoric of commemoration: the poem's short lines and its abrupt shifts between the "
          "language of record and the language of lyric prevent any comfortable mourning, and the closing section "
          "turns on the poet's own complicity, since the poem's art is made out of the atrocity it deplores. The "
          "work is one of the earliest and most uncompromising English poems about the Holocaust, and its "
          "procedures - the documentary date, the broken form, the self-accusation - became models for later "
          "writing on the subject.",
  themes_text="The Holocaust as a fact that defeats the elegy's consolations: Hill's poem refuses to make the "
              "child's death beautiful or meaningful, and its formal austerity is an ethical position. The "
              "documentary dates place the murder in history, while the lyric address insists on the individual "
              "life; the tension between the two is the poem's subject. The self-accusation of the last section "
              "extends the guilt to the poet and to the reader who is moved by the poem, and it is this that has "
              "made 'September Song' central to discussions of poetry after Auschwitz.",
  structure="Six short sections, some of them a single line, without regular stanza form; the poem moves between "
            "the archival statement of dates, the direct address to the child and the poet's reflection, and its "
            "fragmentation enacts the refusal of a continuous elegiac narrative.",
  style="Bare, clipped lines with strong caesurae; a mixture of bureaucratic and liturgical diction ('deported', "
        "'born', 'requiem'); the rhyme is intermittent and often off-rhyme; the rhythm is deliberately halting, "
        "and the poem's brevity is part of its refusal of eloquence.",
  ctx="Published in King Log (1968), which won the Hawthornden Prize and established Hill as the leading English "
      "poet of his generation; the poem belongs to the first English reception of Holocaust testimony, before the "
      "term 'Holocaust' itself was general, and it has been read alongside Celan and Sachs as one of the founding "
      "texts of postwar poetry of atrocity.",
  sig="The most discussed poem of King Log and the poem on which Hill's reputation as a poet of historical guilt "
      "principally rests; it is the third of his four selections in the Norton Anthology and a standard text in "
      "the criticism of Holocaust poetry.",
  canon="Major canon",
  biblio="Published in King Log (London: André Deutsch, 1968) and collected in Broken Hierarchies: Poems 1952-2012 "
         "(2013). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on "
         "page 834.",
  notes="The dates ('born 19.6.32', 'deported 24.9.42') and the opening are quoted from the accounts of the poem in "
        "the Poetry Foundation essay and general knowledge of King Log; the text was not read complete in a "
        "scholarly edition, and the description of the last section is general.",
  ver="partially verified", sources=[HILL_PF, HILL_OUP, NAEL]),
W10("Walker Brothers Cowboy", MU, "1968", "Short story", "significant",
  genres=G("Short Story", "Realist Fiction", "Regional Fiction"),
  themes=T("Childhood, adolescence and coming of age", "Class, labour and social mobility", "Family, marriage and domestic life"),
  movements=M("Canadian Literary Nationalism",),
  overview="The opening story of Alice Munro's first collection, Dance of the Happy Shades (1968): a girl goes on "
           "her father's rounds as a travelling salesman during the Depression and discovers, at one farmhouse, a "
           "woman who was once his sweetheart.",
  content="A first-person narrative in which the narrator remembers a summer evening of her childhood in a small "
          "Ontario town: her father, a former fox farmer, now sells for the Walker Brothers, and takes her and her "
          "younger brother on his rounds, ending at the house of a woman called Nora, where the girl learns "
          "something about her father's earlier life.",
  summary="The story opens with the narrator and her father walking by the lake, and moves back to explain how the "
          "family lost the fox farm and came to town, where her mother has sunk into depression and her father has "
          "become a pedlar for the Walker Brothers, selling a mixed line of groceries and household goods from his "
          "car. One evening he takes the children with him on his rounds; they visit farms where a customer nearly "
          "empties a chamber pot on him, and then a house where a woman named Nora, a former schoolteacher, greets "
          "him with an intimacy that the girl does not understand. Nora gives them tea and shows them her gramophone "
          "and her garden, and the father's manner with her is different from his manner at home: the girl senses "
          "a whole earlier life, and the possibility of a different father, without being able to name it. On the "
          "way home he buys a package of licorice and shares it, and the narrator understands that there are "
          "things not to be mentioned. The story ends with the child's recognition of the mother's sadness and of "
          "the father's separate existence, neither of which she can put into words.",
  themes_text="The story's subject is the child's discovery that her parents have lives she cannot enter: the "
              "father's former sweetheart and the mother's depression are two halves of a knowledge the narrator "
              "approaches but does not possess. Class and labour are present in the pedlar's rounds and in the "
              "family's fall from the fox farm, and the Depression is rendered as a set of small domestic "
              "arrangements rather than as history. Munro's characteristic method is already visible: the story "
              "gives the child's limited perspective, and the adult narrator's retrospective wording lets the "
              "reader see what the child cannot.",
  structure="A first-person retrospective narrative in a single continuous movement, framed by the walk by the "
            "lake and ordered by the rounds of the evening; the story's revelation is withheld and displaced onto "
            "detail, and its ending refuses the explicit statement of what the girl has learned.",
  style="Plain, unhurried prose with a rural Ontario vocabulary and a precise registration of speech; the "
        "narration moves between the child's perceptions and the adult's phrasing; dialogue is sparse and the "
        "detail - the licorice, the gramophone, the chamber pot - carries the meaning.",
  ctx="Dance of the Happy Shades (1968) won the Governor General's Award and established Munro as the leading "
      "Canadian short-story writer of her generation; the story draws on her own childhood in Wingham, Ontario, "
      "and on her father's work as a fox farmer and, after the farm failed, as a labourer and night watchman, and "
      "it belongs to the renaissance of Canadian writing in the 1960s.",
  sig="The opening story of Munro's first collection and one of the most anthologised Canadian short stories; it "
      "is her selection in the Norton Anthology and the standard introduction to her method of retrospective "
      "narration and withheld revelation.",
  canon="Secondary canon",
  biblio="Published as the first story of Dance of the Happy Shades (Toronto: Ryerson Press, 1968) and collected in "
         "Selected Stories (1996). A selection of The Norton Anthology of English Literature, 11th edition, vol. "
         "F, beginning on page 823.",
  notes="The plot follows The Atlantic's retrospective essay on the collection and a reading blog's summary, which "
        "agree on the father's rounds, the former sweetheart and the licorice; the mother's depression and the "
        "story's closing are described from those sources and general knowledge, and the text itself was not read "
        "complete.",
  ver="partially verified", sources=["Alice Munro's Dance of the Happy Shades, 50 Years Later (The Atlantic)", MUNRO_READ, NAEL]),
]

WORKS += [
W10("One Out of Many", VSN, "1971", "Novelette (one of the two 'supporting narratives' of In a Free State)", "significant",
  genres=G("Novella", "Psychological Novel", "Political Novel"),
  themes=T("Migration, exile and diaspora", "Identity, authenticity and the divided self", "Race, racism and the struggle for civil rights"),
  movements=M(POSTCOL, SAS),
  overview="The second of the two 'supporting narratives' in V. S. Naipaul's In a Free State (1971): Santosh, a Bombay "
           "servant, follows his employer to Washington and discovers that freedom in America is a condition he has "
           "no equipment to live in.",
  content="A first-person narrative spoken by Santosh, an Indian servant who comes to Washington with a diplomat, "
          "loses his place in the household, moves into a basement room, and finds himself alone in a country whose "
          "codes he cannot read; his encounter with a black American woman who runs a restaurant becomes his only "
          "means of belonging.",
  summary="Santosh opens his story at the end, or near it: he is in Washington, and he explains how he came there as "
          "the servant of a government man posted to the embassy, a man who had chosen him because he was "
          "unobtrusive. In Bombay Santosh had a place, a hut, a routine and a sense of himself; on the aeroplane he "
          "is terrified, and he hopes the plane will crash. Washington overwhelms him: the abundance of the "
          "supermarket, the size of the buildings, the strangeness of the people he calls 'hubshi', and the "
          "humiliation of being told he must not cook or dress as he did at home, because he now represents his "
          "country. When his employer takes a flat in a distant suburb, Santosh is left in the city with a little "
          "money and a basement room, and he learns to live alone: he cooks, he cleans, he walks the streets, and "
          "he discovers that his invisibility as a servant was also his protection. He meets a black woman who "
          "runs a restaurant and who takes him in; he is bewildered by her, by her body and by the American "
          "openness of her manner, and he marries her, in part because marriage is the way to become legal in a "
          "country where he otherwise does not exist. At the end he looks in a mirror and decides to be free: he "
          "leaves his employer's service and his wife, and the story closes with him in the street, at night, one "
          "part of the flow, and free in a way that the story has taught the reader to hear as desolation.",
  themes_text="Naipaul's subject is the immigrant who gains the forms of freedom and loses the structure that gave him "
              "a self: Santosh's place in Bombay was a servitude, but it was also a home, and America offers him "
              "rights without a role. The story's racial vocabulary is deliberately uncomfortable - the narrator's "
              "'hubshi' is the word of an Indian who has his own hierarchy of colour - and the marriage at its "
              "centre is a transaction on both sides, a green card for the man and a servant for the woman. The "
              "closing claim to freedom is the most ironised sentence in the book, and the story's first-person "
              "voice, with its broken syntax and its dignity, keeps the reader inside a consciousness that cannot "
              "see what has happened to it.",
  structure="A first-person narrative spoken in Santosh's own idiom, beginning with the end and circling back; the "
            "story moves by scenes - the flight, the embassy flat, the basement room, the restaurant, the "
            "marriage, the mirror - rather than by plot, and its chronology is deliberately broken so that the "
            "reader knows the outcome before the causes.",
  style="A careful, slightly off-key English, with Indian idiom and a servant's deference in its phrasing; short "
        "sentences and simple clauses; the descriptive passages are flat and exact, and the absence of metaphor is "
        "itself the effect; the voice is dignified, observant and uncomprehending at once.",
  ctx="In a Free State (1971) consists of a prologue and epilogue from Naipaul's journals, two 'supporting "
      "narratives' - 'One Out of Many' and 'Tell Me Who to Kill' - and the title novella; it won the Booker Prize "
      "in 1971. The story draws on Naipaul's own first years in London and on the Indian diaspora he had "
      "described in An Area of Darkness (1964), and it belongs to the literature of postwar migration that "
      "includes Selvon's London stories and Rushdie's later fiction.",
  sig="One of Naipaul's most anthologised stories and the text by which his treatment of the immigrant's freedom is "
      "usually introduced; it is his selection in the Norton Anthology and, with 'Tell Me Who to Kill', the "
      "narrative that frames the Booker Prize-winning novel.",
  canon="Secondary canon",
  biblio="Published in In a Free State (London: André Deutsch, 1971). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning on page 837.",
  notes="The plot follows Neel Mukherjee's account of the book for The Paris Review and the character study read as "
        "a search extract; the closing scene and the mirror are described from those sources and general "
        "knowledge. The text was not read complete, so the record makes no quotation except the reported phrases.",
  ver="partially verified", sources=[NAIP_PR, W_VSN, NAEL]),
W10("Death and the King's Horseman", WS, "1975", "Play (five acts, with a prologue-like opening scene)", "major",
  genres=G("Modern Tragedy", "Historical Drama", "Political Theatre"),
  themes=T("History, truth and the uses of the past", "Faith, doubt and the sacred", "Power, the state and surveillance"),
  movements=M(AFR, POSTCOL),
  overview="Wole Soyinka's tragedy of 1975, based on an event in colonial Oyo in 1946: Elesin, the king's horseman, "
           "must follow his dead king into the afterlife, and the intervention of a British district officer, "
           "determined to stop what he takes for barbarism, destroys him and his family and leaves the community "
           "unable to complete the rite on which its order depends.",
  content="A play in five acts set in the Yoruba city of Oyo during the Second World War: Elesin prepares for his "
          "ritual suicide, the colonial officer Simon Pilkings tries to stop it, the market women resist the "
          "police, and Elesin's son Olunde, returned from medical studies in England, takes his father's place.",
  summary="The play opens in a market in Oyo, where Elesin Oba, the king's horseman, moves through the crowd in a "
          "trance of celebration: the king has died a month earlier and Elesin, who has lived a life of privilege "
          "in expectation of this duty, is to follow him into the afterlife, and his final hours are given to "
          "dancing, poetry and the taking of a young bride. The news reaches the house of Simon Pilkings, the "
          "district officer, who is dressed for a masquerade ball; his subordinate Amusa, a Yoruba policeman, "
          "reports that the ritual is about to take place, and Pilkings, confident that the customs of the "
          "colonised are barbarous, has Elesin arrested to prevent it. The market women block Amusa's way and mock "
          "him; the ball goes ahead at the Residency with the carved egungun mask that Pilkings' wife Jane has "
          "turned into a costume, while Elesin waits in a cell and the ritual remains uncompleted, a rupture in "
          "the order of the world. Olunde, Elesin's eldest son, who has been studying medicine in England, "
          "returns on the same ship as the governor's aide and confronts Pilkings with the colonial platitude that "
          "a father's ritual suicide is worse than the mass deaths of the war in Europe. In the last act Elesin, "
          "broken and ashamed, is brought before Iyaloja, the mother of the market, who tells him that he has "
          "failed; the women bring in a body wrapped in cloth - Olunde, who has killed himself to restore the "
          "order his father failed to restore. At the sight of his son, Elesin strangles himself with his chains, "
          "and the play ends with Iyaloja's final words over the two bodies.",
  themes_text="The play's central subject is what Soyinka called the metaphysical dimension of the ritual: the "
              "king's horseman must die not from superstition but because the survival of the community depends on "
              "the passage of the king's spirit, and the colonial intervention, however humane its intention, "
              "destroys a structure on which the world depends. The British are given their own arguments and "
              "their own dancing bodies - the ball, the masks, the ceremonial - so that the play stages two "
              "rituals rather than one, and refuses the comfortable opposition of superstition and reason. "
              "Elesin's failure is also his own: the play shows him delayed by appetite and vanity before the "
              "arrest, so that guilt is distributed. Olunde's suicide and Iyaloja's contempt close the circle, "
              "and the ending is a tragedy of the family as much as of the state.",
  structure="Five acts, moving between the market and the Residency, the Yoruba world and the colonial one, with a "
            "chorus of market women and a shifting focus from Elesin to Pilkings and Olunde; the movement is "
            "spatial and ritual rather than linear, and the final act's revelation of Olunde's body provides the "
            "classic reversal and recognition that Soyinka has compared to Sophoclean tragedy.",
  style="A flexible verse-like prose, rising into poetry in Elesin's speeches and the market women's exchanges; "
        "Yoruba songs, proverbs, drum rhythms and calls and responses built into the dialogue; the colonial "
        "speech rendered in the flat idiom of the English officer class and in a comic English-accented "
        "pastiche by the women; the whole play assumes a performance of music, dance and masquerade.",
  ctx="The play is based on the death in 1946 of the horseman of the Alafin of Oyo, who was prevented by the "
      "British colonial administration from committing ritual suicide and whose son took his place; Soyinka "
      "wrote it while in exile at the University of Cambridge, where it was first performed by the Oxford "
      "University Dramatic Society in 1975 and published in the same year. It was written in the aftermath of "
      "the Nigerian Civil War and of the decade in which African writers were reasserting the cultural "
      "sovereignty of their own traditions.",
  sig="The central play of modern African theatre in English and the work by which Soyinka's drama is usually "
      "represented; it is his selection in the Norton Anthology and is staged across the world, and its "
      "argument about the colonial destruction of a metaphysical world has been central to the criticism of "
      "African drama.",
  canon="Major canon",
  biblio="Published by Eyre Methuen (London) in 1975, first performed in 1975. A selection of The Norton Anthology of "
         "English Literature, 11th edition, vol. F, beginning on page 860.",
  crit="The play has been the centre of the long debate about how African drama should be read: Soyinka's own "
       "preface insists that the play is not about the colonial clash of cultures but about the metaphysical "
       "order and its violation, an argument taken up by critics who read Elesin's death as a ritual necessity "
       "rather than a defeat, while others have emphasised the play's staging of colonial complicity, its "
       "treatment of women and its relation to Greek tragedy. Its first production at Cambridge in 1975 and its "
       "revival at the National Theatre in 1990 established it as a modern classic, and it remains the most "
       "widely studied African play in English.",
  notes="The plot and the historical basis follow David Damrosch's essay on the play for Literary Hub, which quotes "
        "Iyaloja's 'burden' and Olunde's 'Is that worse than mass suicide?'; the reading is the record's own. The "
        "play's first performance and publication dates were not checked beyond that source and general "
        "knowledge.",
  ver="partially verified", sources=[SOY_LH, W_WS, NAEL]),
]

WORKS += [
W10("Top Girls", CC, "1982", "Play (three acts)", "major",
  genres=G("Stage Comedy", "Modern Tragicomedy", "Political Theatre"),
  themes=T("Gender, feminism and women's lives", "Class, labour and social mobility", "History, truth and the uses of the past"),
  movements=M("Second-Wave Feminist Writing", "Political Theatre and the Fringe"),
  overview="Caryl Churchill's play of 1982, first staged at the Royal Court: Marlene, a newly promoted manager at a "
           "London employment agency, gives a dinner party for five women out of history and legend, and the play's "
           "other two acts show the office she has conquered and the sister and daughter she has left behind.",
  content="A play in three acts: a surreal dinner party at which Marlene entertains Pope Joan, the explorer Isabella "
          "Bird, Dull Gret from Bruegel, Chaucer's Patient Griselda and the Japanese courtesan Lady Nijo; a week "
          "in the 'Top Girls' employment agency, where women compete for jobs and Marlene's ruthlessness is on "
          "show; and a visit to Marlene's sister Joyce and her daughter Angie, in a Suffolk backwater, which "
          "reveals the cost of Marlene's success.",
  summary="Act One is the dinner party: Marlene, celebrating her promotion, is joined by five guests drawn from "
          "history, art and literature, each of whom tells the story of her life. Pope Joan, who was stoned after "
          "giving birth during a papal procession; Isabella Bird, the Victorian traveller; Dull Gret, who led an "
          "army of women into hell; Patient Griselda, whose husband tested her by taking her children; and Lady "
          "Nijo, the courtesan of a thirteenth-century emperor, all speak of the sacrifices and cruelties their "
          "worlds demanded of women, and the conversation slides from celebration into confession, complaint and "
          "sudden violence. Act Two is the office: Marlene's agency, where women are interviewed, humiliated and "
          "selected, and where Marlene's toughness - she has beaten a male colleague to the promotion - is shown "
          "to be inseparable from the system she has entered. Act Three is set a year earlier, at Christmas in "
          "Suffolk, in the kitchen of Marlene's sister Joyce: Angie, a sullen teenager, and Kit, the child she "
          "looks after, are there, and the sisters' quarrel reveals that Marlene's rise was paid for by Joyce, who "
          "stayed and brought up Angie - Marlene's daughter, passed off as her niece. The play closes with Angie's "
          "hallucinated cry of 'frightening' and Marlene's refusal to hear it.",
  themes_text="The play asks what a woman has to become in order to succeed, and answers with a structure rather "
              "than a moral: Marlene's career is real and her toughness is real, and the price is paid by Joyce and "
              "Angie, whose lives are the unseen condition of the office's glamour. The historical guests widen the "
              "question, since every one of them was praised or punished for the same bargain, and the "
              "cross-cutting of acts makes the play an argument about class as well as gender: Marlene's feminism "
              "is a middle-class individualism, and the working-class woman who stays at home is the one who "
              "subsidises it. Churchill's refusal to provide a sympathetic heroine is the play's most radical "
              "gesture, and its political target is Thatcherism as much as patriarchy.",
  structure="Three acts in reverse chronology, the dinner party, the office week and the Suffolk Christmas of the "
            "previous year; the acts are linked by doubling (the actresses who play the historical women play the "
            "modern characters) and by overlapping dialogue, and the play's final image belongs to the child "
            "rather than the protagonist.",
  style="Overlapping dialogue, with two or three conversations crossing at once; short scenes cut without "
        "transition; the historical women speak in pastiche registers - medieval chronicle, Victorian travel "
        "writing, Chaucer's rhyme royal - while the office scenes use the clipped idiom of the employment "
        "interview; the play's language is plain and its structure is the argument.",
  ctx="Written in 1982, the third year of Margaret Thatcher's government, and premiered at the Royal Court on 28 "
      "August 1982 in a production by Max Stafford-Clark; it was the play in which Churchill's feminism and her "
      "analysis of the market met, and it has been revived repeatedly (the National Theatre, 2019) as a document "
      "of the Thatcher years.",
  sig="Churchill's best-known play and one of the defining British plays of the 1980s; its all-female cast, its "
      "overlapping dialogue and its refusal of a heroine changed the possibilities of political theatre, and it is "
      "her selection in the Norton Anthology.",
  canon="Major canon",
  biblio="First performed at the Royal Court Theatre, London, on 28 August 1982; published by Methuen in 1982. A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 911.",
  crit="Criticism of Top Girls has centred on three questions: whether the play endorses or exposes Marlene's "
       "Thatcherite feminism, whether its historical women illuminate or displace the modern story, and whether "
       "the Suffolk act, with its realism and its child, offers the play's judgement or merely its context. "
       "Feminist critics have debated the play's treatment of class and race, and later productions have "
       "emphasised the office scenes' satire of the recruitment industry. It is the play by which Churchill's "
       "political theatre is most widely taught, and it has been set beside Cloud 9 and Serious Money as the "
       "central trilogy of her critique of power.",
  notes="The premiere, cast and subject follow Wikipedia's article on the play; the plot account uses that article's "
        "acts and characters and general knowledge of the text. The full play was not read, so the record makes no "
        "quotation and its reading of the ending is stated as the play's reported action.",
  ver="partially verified", sources=[W_TG_PLAY, W_CC, NAEL]),
]

WORKS += [
W10("Digging", SH, "1966", "Poem (eight stanzas)", "major",
  genres=G("Lyric Poetry", "Regional Poetry"),
  themes=T("Class, labour and social mobility", "Family, marriage and domestic life", "Art, the artist and the creative life"),
  movements=M("Northern Irish Poetry and the Belfast Group",),
  overview="The poem that opens Seamus Heaney's first collection, Death of a Naturalist (1966): the poet at his desk "
           "watches his father digging potatoes below the window, remembers his grandfather cutting turf on the bog, "
           "and resolves, in the poem's last line, to take up the pen as his own spade and dig with it.",
  content="Eight stanzas of memory and observation: the father's spade sinking into the potato drills under the "
          "window, his rhythm and the sounds and smells of the work, the grandfather cutting turf on Toners bog "
          "thirty years before, and the poet's decision, with the pen between his finger and thumb, that he will "
          "dig with it.",
  summary="'Between my finger and my thumb / The squat pen rests; snug as a gun.' Under the window the father's "
          "spade is 'sinking' into the gravelly ground, and the poet looks down at him through the pane: he has no "
          "spade like the men of the family, and the poem's opening places the pen in the hand as an awkward, "
          "unearned instrument. The father, who dug potatoes on the family farm for forty years, has a rhythm the "
          "poet remembers - the 'coarse boot' on the spade, the 'clean rasping sound' of the blade among the "
          "'cold smell of potato mould' - and the grandfather cut more turf in a day than any other man on "
          "Toners bog, the last time the poet saw him. Both men dug for a living, and their labour produced the "
          "potatoes and the turf that fed and warmed the family; the poet's work produces nothing but the poem. "
          "The last stanza resolves the difficulty by an act of analogy rather than of claim: 'Between my finger "
          "and my thumb / The squat pen rests. / I'll dig with it.' The pen is not a spade, but the poem makes "
          "digging the image of both, and the word 'dig' carries the whole argument about inheritance, work and "
          "the poet's right to his own tool. The father's spade and the grandfather's turf-slane are both "
          "instruments of a skill the poet does not possess, and the poem's exactness about that skill - the "
          "boot, the handle, the 'nicking and slicing' of the turf - is how it pays its respects; the closing "
          "claim is therefore modest as well as bold, since it asks only that the pen be allowed to count as "
          "work. Heaney's later poems return to the same ground, and 'Digging' sets the terms for a career in "
          "which the farm at Mossbawn is the measure of everything the poetry does.",
  themes_text="The poem is about inheritance and vocation: the poet comes from a family of diggers and has no spade "
              "of his own, and the poem's task is to find a way of claiming the labour he did not do. The father's "
              "expertise, rendered with an exactness that is itself a form of respect, is set against the poet's "
              "sedentary work, and the closing analogy refuses both the sentimental claim that poetry is the same "
              "as digging and the resigned claim that it has nothing to do with it. Class and the move from farm "
              "to university are present throughout, and the poem's 'snug as a gun' is a deliberate shock: the pen "
              "is both comfort and weapon, and its power is not innocent.",
  structure="Eight stanzas of variable length, opening with the pen and closing with the pen, with the father's "
            "digging and the grandfather's turf in between; the poem's frame is the window through which the poet "
            "looks, and its movement is from observation to memory to decision.",
  style="A four-beat line with loose rhyme and half-rhyme, heavy with consonantal sound ('the squelch and slap / "
        "Of soggy peat'); the vocabulary is drawn from farm work and is exact ('gravelly', 'rasping', 'sod', "
        "'mould'); the poem's music is in its stresses rather than its metre, and the opening simile and the "
        "closing line are deliberately plain.",
  ctx="Death of a Naturalist (Faber, 1966) was Heaney's first collection, published when he was twenty-seven and "
      "living in Belfast, and it made him the leading poet of the Northern Irish generation that also included "
      "Michael Longley and Derek Mahon. The poem draws on the family farm at Mossbawn and on Heaney's own passage "
      "from the farm to Queen's University, and it has become the standard poem about the poet's relation to a "
      "manual-labour inheritance in English.",
  sig="The poem that opens Heaney's first book and the one by which his whole career is usually introduced; it is "
      "his first selection in the Norton Anthology, and its closing analogy has entered the common language of "
      "writing about poetry and work. It is the poem most often taught as an introduction to Heaney, and the one "
      "in which his themes of inheritance, labour and vocation are first set out.",
  canon="Major canon",
  biblio="Published as the opening poem of Death of a Naturalist (London: Faber and Faber, 1966) and collected in "
         "Opened Ground: Selected Poems 1966-1996 (1998). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning on page 969.",
  crit="'Digging' has been read as the founding poem of Heaney's career and as the clearest statement of the "
       "postwar poet's relation to a manual-labour inheritance; critics have traced its analogy of spade and pen "
       "through his later work, and have debated whether the closing line claims too much for poetry or "
       "dignifies it. Its place at the head of Death of a Naturalist has made it the standard point of entry to "
       "the collection, and it is among the most frequently anthologised poems in English of the second half of "
       "the century.",
  notes="The opening and closing lines and the phrases 'squelch and slap / Of soggy peat' and 'cold smell of potato "
        "mould' are quoted from the text as printed in the reading list and in general knowledge; the poem's "
        "stanza count follows the standard printing and was not collated with the 1966 edition.",
  ver="partially verified", sources=[SH_WORKS, W_SH, NAEL]),
W10("The Grauballe Man", SH, "1975", "Poem (eight stanzas)", "significant",
  genres=G("Elegiac Poetry", "Historical Writing"),
  themes=T("The Holocaust, atrocity and historical memory", "Violence, crime and justice", "History, truth and the uses of the past"),
  movements=M("Northern Irish Poetry and the Belfast Group",),
  overview="One of the bog-body poems of North (1975): Heaney looks at the preserved body of the Grauballe Man, "
           "killed in the Iron Age and dug from a Danish bog, and asks what it means to make a poem out of a "
           "murder.",
  content="Eight stanzas describing the exhumed body - the throat cut, the hands, the leathery skin, the 'slashed "
          "and festering' wound - and turning from the corpse to the question of the poet's own art and of the "
          "violence of the present.",
  summary="The poem begins with the body itself, 'taken in the bog', and describes it with the exactness of an "
          "archaeological report: the head, the 'perished' face, the 'slashed and festering' throat, the hands "
          "that seem to be 'bruised like a mollusc', the 'leathery' skin. Heaney compares the corpse to a work of "
          "art, a 'Dying Gaul' and a 'reclining figure', and then turns the comparison against himself: 'Who will "
          "say 'vigour' to the face, / 'beauty' to the wound?' The poem's last stanzas move outward to the "
          "present, to the 'tribal, intimate revenge' that the body records, and to the poet's own position as "
          "one who has looked at the corpse and made a poem of it. The Grauballe Man was found in a Danish bog in "
          "1952, and Heaney's poem belongs with 'The Tollund Man', 'Bog Queen' and 'Punishment' in the sequence of "
          "bog poems that makes the prehistoric past a mirror for the sectarian violence of Northern Ireland.",
  themes_text="The poem's central question is the ethics of art: to describe the murdered body beautifully is to "
              "repeat, in aesthetic form, the violence that killed it, and Heaney's adjectives are chosen to make "
              "the reader complicit in that repetition. The bog body is also a political image, since the "
              "'tribal, intimate revenge' of the Iron Age is offered as a parallel to the killings of the "
              "Troubles, and the poem refuses to let the parallel become an excuse. The writing's tenderness "
              "towards the corpse and its suspicion of its own tenderness are held together, and the poem's "
              "unresolved ending is its argument.",
  structure="Eight stanzas of varying length, moving from the body's parts to the poet's reflection and then to the "
            "tribal past and the present; the poem is organised as a description that becomes a judgement, and its "
            "last stanza turns from the body to the poet's own consciousness.",
  style="A dense, consonantal line with archaeological and anatomical vocabulary; the similes are deliberately "
        "incongruous ('bruised like a mollusc', 'a Dying Gaul'), and the poem's tension lies between the "
        "precision of the description and the moral discomfort it produces; the rhyme is intermittent and the "
        "stanza forms are irregular.",
  ctx="North (Faber, 1975) was written after Heaney's move south to County Wicklow and in the worst years of the "
      "Troubles; the bog poems draw on P. V. Glob's The Bog People (1965), which Heaney read in the late 1960s, and "
      "on the archaeological discoveries of Tollund, Grauballe and other Danish and Irish bodies. The collection "
      "was controversial for its use of myth and prehistory as a way of writing about contemporary political "
      "violence.",
  sig="One of the central bog poems of North and the poem in which Heaney's treatment of art and atrocity is most "
      "directly posed; it is his second selection in the Norton Anthology and a standard text in the criticism of "
      "Northern Irish poetry.",
  canon="Secondary canon",
  biblio="Published in North (London: Faber and Faber, 1975) and collected in Opened Ground (1998). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 970.",
  notes="The poem's subject and the phrases quoted ('slashed and festering', 'tribal, intimate revenge') follow the "
        "reading list and the Harvard Review's account of the bog poems; the stanza count and the description of "
        "the opening were checked there and in general knowledge, and the text was not read complete.",
  ver="partially verified", sources=[SH_WORKS, SH_HR, SH_READ, NAEL]),
]

WORKS += [
W10("Punishment", SH, "1975", "Poem (eleven quatrains)", "significant",
  genres=G("Political Poetry", "Elegiac Poetry"),
  themes=T("Violence, crime and justice", "Gender, feminism and women's lives", "History, truth and the uses of the past"),
  movements=M("Northern Irish Poetry and the Belfast Group",),
  overview="The most controversial of the bog poems of North (1975): Heaney addresses the body of a young woman "
           "executed in the Iron Age for adultery, and connects her punishment with the tarring and feathering of "
           "young Catholic women in Belfast, admitting that he would have stood by and watched.",
  content="Eleven quatrains: the exhumed body of the 'Windeby girl' in her noose, the poet's intimate address to her "
          "as 'my poor scapegoat', and his recognition that he has looked on, and would look on, at the same "
          "punishment in the streets of his own time.",
  summary="The poem begins with the body: 'I can feel the tug / of the halter at the nape / of her neck, the wind / "
          "on her naked front.' Heaney addresses the dead woman with a terrible intimacy, naming her body part by "
          "part - the 'frail rigging of ribs', the 'drowned' breasts, the 'stone of the tribe' at her ankles - and "
          "imagining her shaved head and her 'blinded' face. He reads her as an adulteress punished by her "
          "community, and then makes the connection that has made the poem famous and notorious: to the young "
          "Catholic women of Belfast who were tarred and feathered for keeping company with British soldiers, "
          "'cauled in tar' and 'caged' on the railings. The poem's last quatrains are the confession: he "
          "understands the 'exact and mutual' moment of the punishment, and he admits that he would have cast "
          "stones with the tribe, and would have stood by, 'artfully' - the word is the poem's self-indictment - "
          "while the punishment was "
          "carried out. The poem ends with his identification with both the victim and the executioners, and the "
          "admission is not resolved.",
  themes_text="'Punishment' is an examination of complicity: the poet's empathy for the murdered woman is turned "
              "against him, since the same tribal logic that killed her operates in his own community, and he "
              "confesses that he would have been part of it. The poem's sexual politics are inseparable from its "
              "politics of violence: the woman is punished for her sexuality, and the 'tribal, intimate revenge' "
              "of the Iron Age is offered as the pattern of the sectarian punishment of women in Belfast. The "
              "address to the body gives the victim a voice that the poem also takes from her, and the "
              "self-accusation is Heaney's way of refusing the consolations of the historical parallel.",
  structure="Eleven quatrains, mostly unrhymed, moving from the intimate description of the body to the modern "
            "parallel and then to the poet's confession; the poem's turn comes at the moment of connection "
            "between past and present, and its last stanza returns to the 'artful' position of the watcher.",
  style="Heaney's dense consonantal line at its most physical, with anatomical and archaeological terms "
        "('halter', 'rigging of ribs', 'stone of the tribe'); the direct address ('my poor scapegoat') gives the "
        "poem its intimacy, and the switch into the language of contemporary Belfast ('cauled in tar', "
        "'tar-black face') breaks the archaeological frame.",
  ctx="North (1975) was written in the worst years of the Troubles, and 'Punishment' was read by some critics as "
      "an apology for Republican violence and by others as the strongest example of Heaney's refusal of easy "
      "positions; the tarring and feathering of women in Belfast was a documented practice of the early 1970s. "
      "The poem has been central to the critical debate about Heaney's politics ever since.",
  sig="The most discussed and most controversial poem in North and the one on which the argument about Heaney's "
      "politics has principally turned; it is his third selection in the Norton Anthology and a standard text in "
      "courses on poetry and the Troubles.",
  canon="Major canon",
  biblio="Published in North (London: Faber and Faber, 1975) and collected in Opened Ground (1998). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 971.",
  notes="The opening lines and the phrases 'my poor scapegoat', 'cauled in tar' and 'artfully' are quoted from the "
        "reading list and general knowledge of the poem; the paraphrase of the last stanza follows the poem's "
        "reported admission and does not claim to reproduce its exact words.",
  ver="partially verified", sources=[SH_READ, SH_WORKS, NAEL]),
]

WORKS += [
W10("Casualty", SH, "1979", "Poem (six sections)", "significant",
  genres=G("Elegiac Poetry", "Political Poetry"),
  themes=T("War, combat and its aftermath", "Death, illness and mourning", "Faith, doubt and the sacred"),
  movements=M("Northern Irish Poetry and the Belfast Group",),
  overview="The elegy at the centre of Field Work (1979) for Louis O'Neill, a Belfast fisherman and drinking companion "
           "killed in a pub bombing after breaking the curfew that followed Bloody Sunday, and a poem about the "
           "cost of Heaney's own refusal to take sides.",
  content="Six sections of memory and elegy: the dead man's dignity and independence, his refusal to be told where he "
          "could drink, the bombing that killed him, and the poet's visit to the morgue and to the funeral, with "
          "the 'richt' of the requiem mass and the guilt of the survivor.",
  summary="The poem begins with the fisherman's world - the boats, the water, the 'promising' morning - and with the "
          "dead man's character: he was a man of 'dignity' and stubborn independence, who would not be ordered "
          "about, and who on the night of the bombing went out to drink despite the curfew, because to stay in "
          "would have been to accept the conditions the violence imposed. Heaney remembers his own meetings with "
          "him, the drink and the talk, and then the killing: a bomb in a pub, the body brought in, the "
          "'armless' and 'blinded' corpse, the morgue, the funeral and the burial. The poem's later sections turn "
          "to the poet's own position, to the guilt of the man who did not go out that night, and to the "
          "'omissions' and 'substitutions' of a life that has been spared; the ending invokes the ritual language "
          "of the requiem - 'the richt' - and the poem's closing image is of the dead man as a kind of "
          "sacramental figure, a casualty of a war whose terms he refused. The poem is an elegy for a friend and a "
          "meditation on the poet's relation to the violence around him, and it is the most personal of Heaney's "
          "Troubles poems.",
  themes_text="'Casualty' is about a death that is also a judgement: the fisherman's refusal to observe the curfew "
              "is an assertion of freedom, and the bomb that kills him is the violence of a community that will "
              "not leave its members alone. Heaney's guilt is that he stayed in, and the poem refuses to "
              "congratulate him: the elegy measures his own caution against his friend's recklessness. The "
              "religious language of the requiem and the 'richt' gives the death a ritual frame, but the poem's "
              "consolation is incomplete, and its last image holds the dead man at a distance the poem cannot "
              "close.",
  structure="Six numbered sections, moving from the fisherman's world and character to the killing, the morgue, the "
            "funeral and the poet's reflection; the sections alternate between narrative and meditation, and the "
            "poem's last movement is a prayer-like address.",
  style="A plain, moving, largely unrhymed verse that allows the narrative to carry the emotion; the diction is "
        "colloquial and Ulster-inflected, with liturgical phrases used sparingly; the elegy's power comes from "
        "its restraint, and the poem is among the least 'poetic' in Field Work.",
  ctx="Field Work (Faber, 1979) was written in Glanmore, County Wicklow, where Heaney had moved in 1972, and it "
      "marks his turn from the mythic method of North to a more personal and local poetry. Louis O'Neill was "
      "killed in a bomb attack on a pub in Belfast in 1973, after the curfew imposed on the Falls Road following "
      "Bloody Sunday (30 January 1972).",
  sig="Heaney's most direct and most personal poem about the Troubles and the central elegy of Field Work; it is "
      "his fourth selection in the Norton Anthology and a standard text in the criticism of his politics.",
  canon="Major canon",
  biblio="Published in Field Work (London: Faber and Faber, 1979) and collected in Opened Ground (1998). A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 972.",
  crit="Critics have treated 'Casualty' as Heaney's most candid poem about the Troubles, reading the fisherman's "
       "defiance as a rebuke to the poet's caution and the elegy as an act of expiation; it has also been "
       "discussed for its use of the Catholic requiem, which gives the poem a communal frame that Heaney's own "
       "position in the sectarian conflict could not supply. Along with 'The Strand at Lough Beg' and the bog "
       "poems, it is central to the debate about whether Heaney's poetry rises to the political crisis of his "
       "time.",
  notes="The plot follows the account in the reading list and the Harvard Review review, which agree on the "
        "fisherman friend killed in a pub bombing after the curfew; the sections and the requiem language are "
        "described from general knowledge of the poem, and the text was not read complete.",
  ver="partially verified", sources=[SH_READ, SH_HR, SH_WORKS, NAEL]),
]

WORKS += [
W10("Station Island", SH, "1984", "Poem (a twelve-section sequence)", "significant",
  genres=G("Narrative Poetry", "Long Poem", "Religious Poetry"),
  themes=T("Faith, doubt and the sacred", "Death, illness and mourning", "History, truth and the uses of the past"),
  movements=M("Northern Irish Poetry and the Belfast Group",),
  overview="The title sequence of Heaney's 1984 collection: a poet makes the three-day pilgrimage to Lough Derg, the "
           "station island of Saint Patrick's Purgatory in County Donegal, and is visited by the dead of his own "
           "life and of Irish history, Norton printing the twelfth and last section.",
  content="Twelve sections, spoken by a pilgrim who circles the island's penitential beds and fasts and prays with the "
          "barefoot pilgrims, and who is met in turn by a schoolteacher, a murdered cousin, a victim of the "
          "Troubles and a series of Irish writers, most memorably James Joyce, each of whom demands an account of "
          "him.",
  summary="The sequence takes the poet to Lough Derg, the island in County Donegal where, since the middle ages, "
          "pilgrims have kept a three-day vigil of fasting, barefoot circling of the penitential beds and "
          "all-night prayer. The pilgrim is at first an observer, self-conscious about his own scepticism and his "
          "reluctance to join in; then the dead begin to appear to him. In section VI he meets the ghost of a "
          "cousin murdered during the Troubles, whom he had avoided in life; in section VII a victim of sectarian "
          "violence asks him to remember; in section VIII his schoolteacher, who had told him to write, reappears "
          "as a demanding 'Master'; in section IX he is visited by the ghost of James Joyce, who mocks his "
          "pieties, tells him to write for the joy of it and, in the celebrated exchange, taunts him about the "
          "Irish corpse road and the 'soul' he is carrying. The twelfth section, printed in the Norton Anthology, "
          "is the last of the sequence and the most intimate: the pilgrim, watching a child in the church, takes "
          "the hand of a woman beside him and remembers his own childhood, and the sequence ends with a vision of "
          "a train carrying the dead away and the poet's sense of a peace that is 'utterly empty'.",
  themes_text="The sequence is an examination of conscience in the traditional sense, and its subject is the poet's "
              "responsibility: to the dead of his family and of the Troubles, to the writers who made his "
              "language, and to the community whose violence he has written about but not suffered. Lough Derg "
              "provides the pattern - a pilgrimage in which the penitent is confronted with what he has "
              "suppressed - and the appearance of Joyce turns the religious exercise into a literary one, since "
              "the dead make their demands in the name of art as well as of faith. The last section's vision "
              "offers no consolation, only a clearing in which the poet is left alone with the ordinary.",
  structure="Twelve sections of different lengths and forms, some in quatrains and some in longer stanzas, moving "
            "from the outer world of the pilgrimage to the inner world of the visitations; the sequence has the "
            "shape of the three-day vigil itself, and the final section is the quietest and the most personal.",
  style="A flexible stanzaic verse, moving between the descriptive and the conversational; the ghostly dialogues "
        "are in a plain, spoken idiom, and Joyce's speech is given a bristling Dublin cadence; the last section "
        "modulates into a slower, more lyrical movement, with a repeated image of the empty peace.",
  ctx="Station Island (Faber, 1984) followed Heaney's move south and the public controversy over North; the Lough "
      "Derg pilgrimage, which he had made as a young man, gave him a structure for a poem about the claims of the "
      "dead. The sequence's meeting with Joyce is one of the most discussed moments in postwar Irish poetry.",
  sig="The central sequence of Heaney's mid-career and the poem in which his argument with his own inheritance is "
      "most fully dramatised; the Norton Anthology prints the twelfth section, and the record covers the whole "
      "sequence as the source of that selection.",
  canon="Major canon",
  biblio="Published in Station Island (London: Faber and Faber, 1984) and collected in Opened Ground (1998). The "
         "Norton Anthology prints section 12, beginning on page 975; this record covers the whole sequence.",
  notes="The account follows the description of the sequence in the literary reference entry and general knowledge "
        "of the poem, including the meetings with the murdered cousin, the schoolmaster and Joyce; the final "
        "section is described from the Norton list's bracketed first line and from general knowledge, and the "
        "text was not read complete.",
  ver="partially verified", sources=[SH_WORKS, W_SH, NAEL]),
W10("Clearances", SH, "1987", "Poem (a sequence of eight sonnets)", "significant",
  genres=G("Elegiac Poetry", "Lyric Poetry"),
  themes=T("Death, illness and mourning", "Family, marriage and domestic life", "Memory, trauma and testimony"),
  movements=M("Northern Irish Poetry and the Belfast Group",),
  overview="The eight-sonnet sequence at the centre of The Haw Lantern (1987), written after the death of Heaney's "
           "mother in 1984, which remembers her through a handful of domestic scenes and ends at her deathbed.",
  content="Eight sonnets, most of them recalling a single moment of family life - peeling potatoes with his mother, "
          "folding sheets, the words of a Protestant great-grandmother - and the last of them describing her "
          "death and the 'clearance' her absence leaves.",
  summary="The sequence is composed of eight sonnets, each a separate memory, and their accumulated force is the "
          "poem. The first recalls a cobblestone thrown at the young poet, aimed, as he now understands, at his "
          "great-grandmother, a Protestant who married a Catholic and was derided for it; the third remembers "
          "peeling potatoes alone in the kitchen with his mother while the rest of the household was away at "
          "Mass, an intimacy the poem sets against the priest's prayers at her deathbed; the fifth has mother and "
          "son unpinning and folding sheets together, the linen becoming sails and, though the word is not used, a "
          "shroud. The sixth remembers her teaching him to split a coal block by finding the grain. The last "
          "sonnet describes her death: the family round the bed, the 'pulsebeat' failing at the wrist, the "
          "breath, and the 'clearance' that opens where she was, an emptiness the survivors inherit. The title "
          "carries both senses: the political 'clearances' of Irish history and the cleared space of grief, and "
          "the sequence is Heaney's most sustained poem of family love.",
  themes_text="The sequence's subject is the ordinary intimacy of a mother and son, rendered through domestic work "
              "rather than statement, and the grief that follows its loss. The religious frame is present but "
              "displaced: the priest's prayers for the dying are set against the memory of peeling potatoes, and "
              "the poem prefers the sacrament of shared work. 'Clearance' also implicates Irish history, since the "
              "word names the dispossession of the Catholic population, and the sequence's private loss is set "
              "within a longer history of the land and of the family's mixed inheritance.",
  structure="Eight sonnets, each a discrete memory, with the sequence moving from childhood and the "
            "great-grandmother's story, through the domestic scenes, to the deathbed and its aftermath; the "
            "sonnet form gives each memory its completeness, and the sequence's order is emotional rather than "
            "chronological.",
  style="The sonnet used with great freedom: lines of nine to twelve syllables, rhyme schemes varied or "
        "abandoned, heavy enjambment, and a diction that moves between the domestic and the liturgical; the "
        "sequence's music is quiet and its images are drawn from kitchen, linen and coal.",
  ctx="The Haw Lantern (Faber, 1987) was written after the death of Heaney's mother, Margaret Kathleen Heaney, in "
      "1984, and the sonnet sequence at its centre is the collection's acknowledged heart; Heaney had used the "
      "sonnet sequence before in 'Glanmore Sonnets', and here he turned it to elegy.",
  sig="Heaney's most admired elegiac sequence and the central poem of The Haw Lantern; it is his sixth selection in "
      "the Norton Anthology and one of the most frequently anthologised sequences in postwar English poetry.",
  canon="Major canon",
  biblio="Published in The Haw Lantern (London: Faber and Faber, 1987) and collected in Opened Ground (1998). A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 977.",
  notes="The sequence's form and several of its scenes - the potato peeling, the folded sheets, the coal block and "
        "the deathbed - are described from the line-by-line notes read as a search extract and from the New York "
        "Review of Books review, which agree on the eight sonnets and the mother's death in 1984; the text was not "
        "read complete.",
  ver="partially verified", sources=[CLEAR_READ, NYRB_HAW, SH_WORKS, NAEL]),
]
