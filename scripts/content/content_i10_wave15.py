"""Installment 10, wave 15: new Norton authors, in the order of The Norton Anthology of English
Literature (11th edition, vol. F), from Stevie Smith to Salman Rushdie.

Seven authors are new to the database: Stevie Smith, Dylan Thomas, Louise Bennett, Kamau
Brathwaite, Ngugi wa Thiong'o, M. NourbeSe Philip and Salman Rushdie. Each has one record per
Norton selection first published 1946-2000; an excerpt has a record for its whole book
(Brathwaite's History of the Voice, Ngugi's Decolonising the Mind, Rushdie's Imaginary
Homelands). Una Marson, the next author in Norton's order, is out of the period: both her
selections were published before 1946 (see the Norton list).

Selections still undated are not recorded: Stevie Smith's 'Pretty', Louise Bennett's 'Jamaica
Language', 'Dry-Foot Bwoy' and 'Jamaica Oman', and Brathwaite's '[On Sycorax Video Style]'.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL  # noqa: E402

SMITH = "Stevie Smith"
DT = "Dylan Thomas"
LB = "Louise Bennett"
KB = "Kamau Brathwaite"
NGUGI = "Ngũgĩ wa Thiong'o"
NP = "M. NourbeSe Philip"
SR = "Salman Rushdie"
CAR = "Caribbean Literature in English"
POSTCOL = "Postcolonial Literature"
POSTTH = "Postcolonial Theory"
AFR = "African Literature in English"
SAS = "South Asian Literature in English"
MAGIC = "Magical Realism in English"

W_SMITH = "Stevie Smith (Wikipedia)"
W_NWBD = "Not Waving but Drowning (Wikipedia)"
UMINHO = "The Religious Poetry of Stevie Smith and Emily Brontë (RepositoriUM, University of Minho)"
NOELTOD = "Why, Porson (Jeremy Noel-Tod, Some Flowers Soon)"
W_DT = "Dylan Thomas (Wikipedia)"
W_DNGG = "Do not go gentle into that good night (Wikipedia)"
W_LB = "Louise Bennett-Coverley (Wikipedia)"
DOUMERC = "Louise Bennett and the Mento Tradition (Eric Doumerc, via CORE)"
W_KB = "Kamau Brathwaite (Wikipedia)"
W_NATION = "Nation language (Wikipedia)"
MDPI_ZONG = "'Sing the Bones Home': Material Memory and the Project of Freedom in M. NourbeSe Philip's Zong! (Humanities, MDPI)"
ARCHIP = "'I know the world by how I speak the world': TikTok ABCs, Disaster Language, and Andrew Salkey's Hurricane (Archipelagos)"
XSELF = "Versions of X/Self: Kamau Brathwaite's Caribbean Discourse (Semantic Scholar)"
W_NGUGI = "Ngũgĩ wa Thiong'o (Wikipedia)"
W_DTM = "Decolonising the Mind (Wikipedia)"
W_NP = "M. NourbeSe Philip (Wikipedia)"
ANGLOSAX = "M. NourbeSe Philip's She Tries her Tongue, her Silence Softly Breaks and the Possibilities of Language (Revista Anglo Saxonica)"
W_SR = "Salman Rushdie (Wikipedia)"
LRB_PH = "The Prophet's Hair, by Salman Rushdie (London Review of Books, vol. 3, no. 7)"
W_IH = "Imaginary Homelands (Wikipedia)"

AUTHORS = [
A10(SMITH, SEC, "1902", "1971", "Kingston upon Hull, England",
  "English; poet and novelist of London (Palmers Green), writing in English",
  "English poet and novelist whose short, deceptively simple poems, often printed with her own drawings, joke and grieve "
  "about death, loneliness, faith and doubt; best known for 'Not Waving but Drowning' (1957)",
  "Florence Margaret Smith, known as Stevie Smith, was born on 20 September 1902 at 34 De La Pole Avenue in Kingston upon "
  "Hull, the second daughter of Charles Ward Smith, a shipping agent, and Ethel Rahel Spear. Her father's business and marriage "
  "failed and he ran away to sea, and when she was three she moved with her mother and sister to 1 Avondale Road, "
  "Palmers Green, in north London, where she lived for the rest of her life with her aunt Madge Spear, the 'Lion Aunt'. "
  "At five she developed tuberculous peritonitis and spent three years in a sanatorium near Broadstairs; she dated her "
  "preoccupation with death from that time. Her mother died when she was sixteen. She was educated at Palmers Green High "
  "School, the North London Collegiate School for Girls and Mrs Hoster's Secretarial College, and from 1923 to 1953 was "
  "private secretary to Sir Neville Pearson at the publishers Newnes. Her first two novels and her first book of poems, A "
  "Good Time Was Had by All (1937), made her name before the war. After retiring from Newnes following a nervous breakdown she "
  "gave readings and broadcasts that won her a younger audience; Sylvia Plath wrote to her in 1962 as 'a desperate "
  "Smith-addict'. She described herself as a 'lapsed atheist', and her essay 'The Necessity of Not Believing' (1958) was "
  "read to the Cambridge Humanist Society. She received the Cholmondeley Award (1966) and the Queen's Gold Medal for Poetry "
  "(1969), and died of a brain tumour on 7 March 1971 in Ashburton, Devon. Hugh Whitemore's play Stevie (filmed in 1978 "
  "with Glenda Jackson) is based on her life.",
  "Smith wrote three lightly fictionalised novels, Novel on Yellow Paper (1936), Over the Frontier (1938) and The Holiday "
  "(1949), and published nine volumes of poems in her lifetime, from A Good Time Was Had by All (1937) through Harold's "
  "Leap (1950), Not Waving but Drowning (1957), Selected Poems (1962), The Frog Prince (1966) and The Best Beast (1969); "
  "Scorpion and Other Poems (1972) and the Collected Poems (1975) followed her death. Her best-known poem is 'Not Waving "
  "but Drowning'.",
  "Short poems in irregular lines and comic rhymes, borrowing the rhythms of hymns, nursery rhymes and ballads; dramatic "
  "monologues and dialogues; deliberate naivety and awkwardness that turn suddenly bleak; her own drawings, often "
  "incongruous with the text. Hermione Lee called 'peculiar' the best word for her effects.",
  "Death as friend and release; loneliness and misunderstanding; faith and unbelief, and the Christianity she could "
  "neither accept nor leave; human cruelty and war; myth, legend and fairy tale; middle-class English life; women's "
  "independence.",
  "A singular voice in twentieth-century English poetry, without school or followers, whose readings in the 1960s won her "
  "a new generation of readers. 'Not Waving but Drowning' is among the best-known English poems of the century, and her "
  "reputation has grown since her death with new collected editions.",
  bib_status="incomplete",
  bib_note="Books, as listed by Wikipedia: the novels Novel on Yellow Paper (1936), Over the Frontier (1938) and The Holiday "
           "(1949); the poems A Good Time Was Had by All (1937), Tender Only to One (1938), Mother, What Is Man? (1942), "
           "Harold's Leap (1950), Not Waving but Drowning (1957), Selected Poems (1962), The Frog Prince (1966), The Best "
           "Beast (1969), Scorpion and Other Poems (1972, posthumous) and Collected Poems (1975, posthumous); Some Are More "
           "Human Than Others (1958), Cats in Colour (1959) and Me Again (1984, posthumous). Wikipedia also lists Alone in "
           "the Woods (1947), which was not checked. Installment 10, which records only Norton selections, holds 'Our Bog "
           "Is Dood' (1950), 'Not Waving but Drowning' (1957) and 'Thoughts About the Person from Porlock' (1962); 'Pretty' "
           "is undated and unrecorded. The books have no work records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_SMITH, W_NWBD],
  alt=["Florence Margaret Smith"]),
A10(DT, MAJ, "1914", "1953", "Swansea, Wales",
  "Welsh; poet, short-story writer and broadcaster writing in English",
  "Welsh poet and writer of richly rhythmic, image-dense lyrics, of the stories of Portrait of the Artist as a Young Dog and "
  "of the 'play for voices' Under Milk Wood, whose readings and broadcasts made him the most popular poet of his day",
  "Dylan Marlais Thomas was born on 27 October 1914 at 5 Cwmdonkin Drive, Swansea, the son of Florence Williams, a "
  "seamstress, and David John Thomas, a grammar-school English master with a first-class degree from Aberystwyth; both "
  "parents spoke Welsh as well as English. He left school in 1932 to work as a reporter on the South Wales Daily Post. Of "
  "the some two hundred poems he wrote between 1931 and 1935, a number were printed while he was still a teenager, "
  "beginning in May 1933 with 'And death shall have no dominion'. In London he met Caitlin Macnamara, whom he married in "
  "1937; they had three children. Finding it hard to live by writing, he added reading tours and radio work; his BBC "
  "broadcasts of the late 1940s brought him a wide public. His reading tours of the United States in the 1950s made him "
  "famous while his drinking and erratic behaviour worsened. On his fourth visit to New York, in 1953, he fell into "
  "a coma and died on 9 November 1953, aged thirty-nine; he is buried at St Martin's churchyard, Laugharne.",
  "Thomas's poems were collected in 18 Poems (1934), Twenty-five Poems (1936), The Map of Love (1939), Deaths and Entrances "
  "(1946), In Country Sleep (1952) and Collected Poems, 1934-1952 (1952); his prose includes Portrait of the Artist as a "
  "Young Dog (1940) and A Child's Christmas in Wales, and his radio play Under Milk Wood was produced after his death.",
  "Dense, incantatory verse built on sound, rhythm and paradoxical imagery, often in strict and intricate forms (the "
  "villanelle of 'Do not go gentle', the syllabic and rhyming patterns of the later poems); biblical cadence; a "
  "celebratory, elegiac lyricism.",
  "Birth, sex and death as one process; childhood and the Welsh landscape; time and mortality; religious imagery without "
  "orthodox belief; the poet's vocation.",
  "One of the most popular poets of the twentieth century in Britain and America, whose recordings and readings changed "
  "the public life of poetry; criticism since his centenary editions has emphasised his modernist poetics over the legend "
  "of the 'roistering, drunken and doomed poet'.",
  bib_status="incomplete",
  bib_note="Installment 10 records only his Norton selection first published in the period, 'Do not go gentle into that good "
           "night' (1951; collected in In Country Sleep and Collected Poems, 1934-1952, both 1952). His other Norton poems "
           "were first printed before 1946 and are not recorded. Books (Wikipedia and general knowledge, not checked "
           "title by title): 18 Poems (1934), Twenty-five Poems (1936), The Map of Love (1939), Portrait of the Artist as a "
           "Young Dog (1940), Deaths and Entrances (1946), In Country Sleep (1952), Collected Poems, 1934-1952 (1952), and, "
           "posthumously, Under Milk Wood (1954) and A Child's Christmas in Wales. None has a work record, so the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_DT, W_DNGG],
  alt=["Dylan Marlais Thomas"]),
A10(LB, SEC, "1919", "2006", "Kingston, Jamaica",
  "Jamaican; poet, folklorist, actress and broadcaster writing and performing in Jamaican Creole (Patois), later "
  "resident in Canada",
  "Jamaican poet, folklorist and performer, 'Miss Lou', whose comic monologues and poems in Jamaican Creole established the "
  "local language as a medium of literature",
  "Louise Simone Bennett was born on 7 September 1919 on North Street in Kingston, Jamaica, the only child of Augustus "
  "Cornelius Bennett, who owned a bakery in Spanish Town, and Kerene Robinson, a dressmaker; after her father's death in "
  "1926 she was raised mainly by her mother. She was educated in Kingston and in 1943 studied Jamaican folklore at Friends "
  "College, Highgate; that year her poems first appeared in the Sunday Gleaner. In 1945 a British Council scholarship made "
  "her the first black student at the Royal Academy of Dramatic Art in London; she worked in repertory and revue in "
  "England and presented the BBC programmes Caribbean Carnival (1945-1946) and West Indian Night (1950). Back in Jamaica "
  "she worked for the Jamaica Social Welfare Commission (1955-1959), taught folklore and drama at the University of the "
  "West Indies, produced the radio monologues Miss Lou's Views (1965-1982) and hosted the children's television programme "
  "Ring Ding (1970-1982). She married the theatre promoter Eric Winston Coverley in 1954. She later lived in Scarborough, "
  "Ontario, and died in Toronto in July 2006; she lay in state in Kingston and was buried in National Heroes Park.",
  "Bennett's poems and stories were published in Anancy Stories and Poems in Dialect (1944), Laugh with Louise (1961), "
  "Jamaica Labrish (1966), Selected Poems (1982) and Aunty Roachy Seh (1993); she also made many recordings of Jamaican "
  "folk songs and of her radio and television work.",
  "Dramatic monologues and conversational poems in Jamaican Creole, usually in ballad quatrains, addressed to a listener "
  "such as 'Miss Mattie'; comic irony, proverb and wordplay drawn from the mento and folk traditions; written to be "
  "performed.",
  "Jamaican language and identity; colonialism and its reversals; migration; the pretensions of the colour and class "
  "hierarchy; the everyday lives of working-class Jamaican women; independence and national culture.",
  "A founding figure of Caribbean poetry in nation language, credited by Linton Kwesi Johnson, Mutabaruka and others; she "
  "received the MBE (1960), the Order of Jamaica (1974), the Musgrave Medal (1978) and the Jamaican Order of Merit (2001).",
  bib_status="incomplete",
  bib_note="Books (Wikipedia's selected publications): Anancy Stories and Poems in Dialect (1944), Laugh with Louise (1961), "
           "Jamaica Labrish (1966), Selected Poems (1982) and Aunty Roachy Seh (1993), with recordings from Jamaican Folk "
           "Songs (1954) onwards. Installment 10, which records only Norton selections, holds 'Colonization in Reverse' "
           "(Jamaica Labrish, 1966). Her other three Norton selections ('Jamaica Language', 'Dry-Foot Bwoy', 'Jamaica "
           "Oman') are not yet dated and not recorded, and the books have no work records, so the bibliography is "
           "incomplete.",
  ver="partially verified", sources=[W_LB, DOUMERC],
  alt=["Louise Bennett-Coverley", "Louise Simone Bennett-Coverley"], pseudo=["Miss Lou"]),
A10(KB, MAJ, "1930", "2020", "Bridgetown, Barbados",
  "Barbadian; Caribbean poet, historian and critic writing in English and nation language, who worked in Ghana, Jamaica, "
  "Britain and the United States",
  "Barbadian poet and historian, author of The Arrivants trilogy and of History of the Voice, which made 'nation language' "
  "the term for the Caribbean's own English, and inventor of the 'Sycorax video style' of his later books",
  "Lawson Edward Brathwaite was born on 11 May 1930 in Bridgetown, Barbados, to Hilton and Beryl Brathwaite. At Harrison "
  "College he started a school newspaper, wrote on jazz and contributed to the magazine Bim; in 1949 he won the Barbados "
  "Island Scholarship to Cambridge, where he took a degree in history at Pembroke College in 1953 and began broadcasting "
  "poems and stories on the BBC's Caribbean Voices. From 1955 he worked as an education officer in the Gold Coast, "
  "witnessing Ghana's independence, which transformed his sense of Caribbean culture; there he married Doris Monica "
  "Wellcome (1960) and wrote the play Odale's Choice (1962). He taught in St Lucia and from 1963 in the history department "
  "of the University of the West Indies at Mona, Jamaica, co-founded the Caribbean Artists Movement in London in 1966, "
  "took his doctorate at Sussex (1968) and launched the journal Savacou in 1971, the year he received the name Kamau in "
  "Kenya. After his wife's death in 1986, the destruction of his archive by Hurricane Gilbert in 1988 and a near-fatal "
  "attack in Kingston in 1990, his 'time of salt', he became Professor of Comparative Literature at New York University "
  "(1992). He won the Neustadt Prize (1994) and the Griffin Poetry Prize (2006), and died in Barbados on 4 February 2020.",
  "His poetry includes the trilogy The Arrivants (1973), gathering Rights of Passage (1967), Masks (1968) and Islands "
  "(1969); the second trilogy of Mother Poem (1977), Sun Poem (1982) and X/Self (1987); Middle Passages (1992) and Born to "
  "Slow Horses (Griffin Poetry Prize, 2006); his histories and criticism include The Development of Creole Society in Jamaica, 1770-1820 (1971), "
  "Contradictory Omens (1974) and History of the Voice (1984).",
  "Long sequences built from many voices and registers, mixing standard English with nation language; the rhythms of "
  "jazz, calypso, work song and ritual; typographic experiment, culminating in the 'Sycorax video style' of computer "
  "fonts and layouts.",
  "The African diaspora and the Middle Passage; the recovery of African elements in Caribbean culture; creolisation; "
  "language, voice and the inheritance of colonial forms; history, catastrophe and survival.",
  "One of the major voices of Caribbean literature and its leading theorist of nation language; The Arrivants is "
  "generally considered his best work.",
  bib_status="incomplete",
  bib_note="Books (Wikipedia's selected works, not checked title by title): poetry from Rights of Passage (1967), Masks "
           "(1968) and Islands (1969), gathered as The Arrivants (1973), through Other Exiles (1975), Black + Blues (1976), "
           "Mother Poem (1977), Sun Poem (1982), Third World Poems (1983), X/Self (1987), Shar (1992), Middle Passages "
           "(1992), Barabajan Poems (1994), DreamStories (1994), Ancestors (2001) and Born to Slow Horses (dated 2006 by Wikipedia); prose "
           "including Folk Culture of the Slaves in Jamaica (1970), The Development of Creole Society in Jamaica, "
           "1770-1820 (1971), Contradictory Omens (1974), History of the Voice (1984) and The Zea Mexican Diary (1993). "
           "Installment 10, which records only Norton selections, holds History of the Voice (1984), 'Calypso' (1967) and "
           "'Letter SycoraX' (1992); '[On Sycorax Video Style]' is undated and unrecorded. Doris Monica Brathwaite's EKB: "
           "His Published Prose & Poetry, 1948-1986 (1986) was not consulted. The bibliography is incomplete.",
  ver="partially verified", sources=[W_KB, XSELF],
  alt=["Edward Kamau Brathwaite", "Edward Brathwaite", "Lawson Edward Brathwaite"]),
A10(NGUGI, MAJ, "1938", "2025", "Kamiriithu, Kenya",
  "Kenyan; novelist, playwright, essayist and academic writing first in English and from the late 1970s in Gikuyu, in exile "
  "from the early 1980s, latterly in the United States",
  "Kenyan novelist and theorist, East Africa's leading writer, whose Decolonising the Mind (1986) bade farewell to English "
  "and argued for African literatures in African languages",
  "Ngũgĩ wa Thiong'o was born James Ngugi on 5 January 1938 in Kamiriithu, in the Kenya Colony. He studied at Makerere "
  "University and at the University of Leeds, and published his first novels in English, among them Weep Not, Child "
  "(1964), The River Between (1965), A Grain of Wheat (1967) and Petals of Blood (1977). In 1977 the play Ngaahika Ndeenda "
  "(I Will Marry When I Want), written with Ngũgĩ wa Mirii, was a commercial success but was shut down by the "
  "authoritarian government six weeks after it opened, and in December of that year he was imprisoned for more than a "
  "year; Amnesty International adopted him as a prisoner of conscience. After his release he turned to writing in Gikuyu "
  "and left Kenya. He taught at Yale, New York University and Northwestern, and became Distinguished Professor of "
  "Comparative Literature and English at the University of California, Irvine. In 1992 he founded the Gikuyu-language "
  "journal Mũtĩiri, which he edited until his death. He won the International Nonino Prize (2001) and the Park Kyong-ni "
  "Prize (2016), was often named for the Nobel Prize, and died on 28 May 2025 in Buford, Georgia.",
  "His fiction runs from Weep Not, Child (1964) through A Grain of Wheat (1967) and Petals of Blood (1977) to the Gikuyu "
  "novels Matigari ma Njiruungi (1986) and Mũrogi wa Kagogo (Wizard of the "
  "Crow, 2006); his essays include Decolonising the Mind (1986).",
  "Realist novels of the Mau Mau war and of independent Kenya that grow increasingly allegorical and satirical; "
  "participatory theatre; polemical, autobiographical essays.",
  "Colonialism and neocolonialism, land and class in Kenya, the Mau Mau rebellion, the betrayal of independence, and "
  "language as the carrier of culture and memory.",
  "Described as East Africa's leading novelist and an important figure in modern African literature, and the most "
  "influential advocate of writing in African languages; Decolonising the Mind is one of the most cited texts of "
  "postcolonial studies.",
  bib_status="incomplete",
  bib_note="Installment 10, which records only Norton selections, holds Decolonising the Mind (1986). His novels, plays, "
           "stories, memoirs and other essays, named in Wikipedia's notable works (Weep Not, Child, 1964; The River "
           "Between, 1965; A Grain of Wheat, 1967; Petals of Blood, 1977; Matigari ma Njiruungi, 1986; Wizard of the "
           "Crow, 2006), have no work records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_NGUGI, W_DTM],
  alt=["Ngugi wa Thiong'o", "James Ngugi"]),
A10(NP, SEC, "1947", None, "Moriah, Tobago (Trinidad and Tobago)",
  "Trinidad and Tobago-born Canadian; poet, novelist, essayist and playwright living in Toronto since the late 1960s",
  "Caribbean-Canadian poet and former lawyer whose She Tries Her Tongue, Her Silence Softly Breaks (1989) and Zong! (2008) "
  "break and remake English to confront colonial and slave histories",
  "Marlene Nourbese Philip, usually credited as M. NourbeSe Philip, was born on 3 February 1947 in Woodlands, Moriah, on "
  "Tobago. She graduated from Bishop Anstey High School in 1965 and took a B.Sc. in economics at the University of the "
  "West Indies. Moving to Canada in 1968, she took graduate degrees in political science and law at the University of "
  "Western Ontario and practised law in Toronto for seven years, leaving the law in 1983 to write. She has published five "
  "books of poetry, two novels, four books of essays and two plays. The manuscript of She Tries Her Tongue, Her Silence "
  "Softly Breaks won the Casa de las Américas Prize; her novel Harriet's Daughter (1988) became a school text in Ontario "
  "and the Caribbean; and Zong! (2008), a poem cycle made from the legal report of the Zong massacre, has been performed "
  "in collective readings. She has held Guggenheim (1990) and MacDowell fellowships and received the PEN/Nabokov Award "
  "(2020), the Molson Prize (2021) and the Windham-Campbell Prize (2024).",
  "Her poetry includes Thorns (1980), Salmon Courage (1983), She Tries Her Tongue, Her Silence Softly Breaks (1989) and "
  "Zong! (2008); her prose includes the novels Harriet's Daughter (1988) and Looking for Livingstone (1991) and the essays "
  "of Frontiers (1992), Genealogy of Resistance and Other Essays (1997) and Bla_k (2017).",
  "Experimental, multi-voiced texts that fragment and collage English, set poems against prose, edicts and textbook "
  "language on the page, and play on etymology and sound; Caribbean demotic beside standard English.",
  "Language and silence; the mother tongue and the 'father tongue' imposed by colonialism and slavery; race, gender and "
  "the body; memory of the Middle Passage; social justice.",
  "Widely taught and much studied for her experiments with form and her commitment to social justice; She Tries Her "
  "Tongue is her best-known book and 'Discourse on the Logic of Language' her most anthologised poem.",
  bib_status="incomplete",
  bib_note="Books (Wikipedia): poetry, Thorns (1980), Salmon Courage (1983), She Tries Her Tongue, Her Silence Softly Breaks "
           "(1989) and Zong! (2008); novels, Harriet's Daughter (1988) and Looking for Livingstone (1991); essays, "
           "Frontiers (1992), Showing Grit (1993), Caribana (1996), Genealogy of Resistance and Other Essays (1997) and Bla_k (2017); "
           "plays, Coups and Calypsos (1999) and Harriet's Daughter (2000). Installment 10, which records only Norton "
           "selections, holds 'Discourse on the Logic of Language' (1989); the books have no work records, so the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_NP, ANGLOSAX],
  alt=["Marlene Nourbese Philip", "Marlene NourbeSe Philip"],
  unc="Wikipedia's infobox gives her birthplace as Woodlands, Moriah, Trinidad and Tobago, while its text says she was born "
      "in 'St. Ann, Jamaica'; the infobox is followed here, since she was schooled in Trinidad."),
A10(SR, MAJ, "1947", None, "Bombay, British India",
  "Indian-born British and American; novelist, short-story writer and essayist writing in English, in Britain from the 1960s "
  "and later in the United States (a citizen from 2016)",
  "Indian-born novelist whose Midnight's Children (1981) remade the English novel of the subcontinent and whose The Satanic "
  "Verses (1988) brought a fatwa calling for his death",
  "Ahmed Salman Rushdie was born on 19 June 1947 in Bombay, in British India, two months before independence. He was "
  "educated at King's College, Cambridge, where he took a degree in history in 1968, and became a British citizen in 1964. "
  "His first novel, Grimus, appeared in 1975; his second, Midnight's Children (1981), won "
  "the Booker Prize and was later twice judged the best of all its winners. He wrote half a dozen pieces for the London "
  "Review of Books in its early years, among them the story 'The Prophet's Hair' (1981) and the essay 'Imaginary "
  "Homelands' (1982). After his fourth novel, The Satanic Verses (1988), Ayatollah Khomeini issued a fatwa calling for his "
  "death; the book was banned in twenty countries, and numerous killings and bombings were carried out by "
  "extremists who cited it. He was elected a fellow of the Royal Society of Literature in 1983 and knighted in 2007, and "
  "became an American citizen in 2016. In 2022 he survived a stabbing at the Chautauqua Institution that cost him the "
  "sight of his right eye.",
  "His novels of the period include Grimus (1975), Midnight's Children (1981), Shame (1983), The Satanic Verses (1988), "
  "Haroun and the Sea of Stories (1990), The Moor's Last Sigh (1995) and The Ground Beneath Her Feet (1999); his essays are "
  "collected in Imaginary Homelands (1991) and his stories in East, West (1994).",
  "Magical realism joined to historical fiction; exuberant, digressive, punning prose that mixes English with Hindustani "
  "and the idioms of Bombay; narrators who are self-conscious storytellers.",
  "Migration and the migrant as the defining figure of the century; the history of India and Pakistan after partition; "
  "religion, fanaticism and secularism; the freedom of the imagination and of speech; hybridity and the relations of East "
  "and West.",
  "One of the most celebrated novelists of his generation; The Times ranked him thirteenth of the fifty greatest British "
  "writers since 1945, and the Satanic Verses affair made him a world symbol of the freedom to write.",
  bib_status="incomplete",
  bib_note="Installment 10, which records only Norton selections, holds 'The Prophet's Hair' (1981, collected in East, West, "
           "1994) and Imaginary Homelands (1991), the essay collection from which Norton's two bracketed excerpts come. His "
           "novels, stories and other non-fiction have no work records. Titles of 1975-1999 named here beyond Midnight's "
           "Children and The Satanic Verses are general knowledge, not checked against a consulted bibliography; the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_SR, W_IH, LRB_PH],
  alt=["Ahmed Salman Rushdie", "Sir Salman Rushdie"]),
]

WORKS = [
W10("Our Bog Is Dood", SMITH, "1950", "Poem (rhymed dialogue in quatrains)", "minor",
  genres=G("Light Verse", "Religious Poetry"),
  themes=T("Faith, doubt and the sacred", "Childhood, adolescence and coming of age", "Power, the state and surveillance"),
  overview="A poem by Stevie Smith from Harold's Leap (1950): children lisp that 'Our Bog is dood', and the speaker's "
           "questions expose a faith held only because they wish it, ready to crucify the doubter.",
  content="A dialogue between the speaker and a group of children about their 'Bog', ending with the children quarrelling "
          "and the speaker walking alone by the sea.",
  summary="'Our Bog is dood,' the children lisp, but when the speaker asks them to explain they grow a little wild. They "
          "know their Bog is dood because they wish it so, they cry, and if she does not think it so she shall be "
          "crucified. Asked what 'dood' is, they answer that it is just what they think it is; they bow their heads: their "
          "Bog is theirs and they are wholly his. When they raise their heads they have forgotten her, and glare at one "
          "another in pride and misery, for they can never agree what their Bog is. It is sweet to leave them and to walk "
          "alone beside the encroaching sea, which will soon drown them all.",
  themes_text="A satire on dogmatic belief as wish-fulfilment, with the sectarian hatred it breeds; the baby talk turns "
              "'God is good' into nonsense and exposes faith held without understanding.",
  structure="Rhymed quatrains of ballad metre, moving from dialogue to the children's quarrel and the speaker's closing "
            "solitude.",
  style="Nursery-rhyme simplicity and baby talk put to sharp theological satire; the liturgical echo of 'Our Bog is ours "
        "/ And we are wholly his'.",
  ctx="Written in the post-war years in which Smith moved between the Anglican faith of her childhood and the unbelief "
      "she later defended in 'The Necessity of Not Believing' (1958).",
  sig="One of Smith's best-known poems on religion, often read as 'Our God is good' (or 'dead') in baby talk, and a "
      "Norton selection.",
  canon="Minor canon",
  biblio="Published in Harold's Leap (London: Jonathan Cape, 1950). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning on page 586.",
  notes="The paraphrase is stated from the text. A University of Minho dissertation dates the poem to 1950 and cites James "
        "Najarian (2003) on its echo of Anglican liturgy.",
  ver="partially verified", sources=[UMINHO, W_SMITH, NAEL]),
W10("Not Waving but Drowning", SMITH, "1957", "Poem (twelve lines in three quatrains)", "significant",
  genres=G("Lyric Poetry", "Elegiac Poetry"),
  themes=T("Death, illness and mourning", "Identity, authenticity and the divided self", "Madness, breakdown and confinement"),
  overview="Stevie Smith's most famous poem, published in 1957 in the collection of the same title and printed with one of "
           "her drawings: a dead man, whose movements in the sea were taken for waving, insists that he was drowning, and "
           "always had been.",
  content="The onlookers' comments on a drowned man who 'always loved larking', set against the dead man's own words: he "
          "was much further out than they thought, all his life, and not waving but drowning.",
  summary="Nobody heard him, the dead man, but still he lay moaning: he was much further out than they thought, and not "
          "waving but drowning. The onlookers say what people say: poor chap, he always loved larking, and now he is dead; "
          "it must have been too cold for him, his heart gave way. No, no, no, the dead man answers, still moaning, it was "
          "too cold always; he was much too far out all his life, and not waving but drowning. A remembered accident at sea "
          "becomes a figure for a whole life of misunderstood distress, in which the signals of despair were read as high "
          "spirits.",
  themes_text="Isolation and misunderstanding: others mistake a cry for help for a cheerful wave, and the joking manner "
              "that hides suffering also prevents its being seen. Critics have read the drowning man as Smith herself, "
              "treated for depression, while noting that the poem's humour resists being read simply as a cry for help.",
  structure="Three quatrains in loose rhyme; the dead man's voice frames the bystanders' clichés in the middle stanza, and "
            "the refrain returns transformed from a single moment to 'all my life'.",
  style="Simple, colloquial diction that Clive James saw as carefully crafted to seem ignorant of convention; the "
        "macabre comedy of a dead man still moaning; the incongruous drawing of a smiling girl.",
  ctx="Smith was treated for depression and had contemplated suicide; she retired from Newnes after a breakdown in 1953. "
      "The poem appeared in Not Waving but Drowning (André Deutsch, 1957).",
  sig="The most famous of Smith's poems and one of the best-known English poems of the century, its title a proverbial "
      "phrase for unnoticed despair.",
  crit="Ingrid Hotz-Davies reads the drowning man as Smith but warns against reading the poem only as a cry for help; "
       "Laura Severin discusses the drawing's 'mysterious smile'; Janice Thaddeus sees an androgyny of speakers in Smith's "
       "work; Clive James wrote that her poems, if pills to cure melancholy, did not work for her, but worked like charms "
       "for everyone else.",
  canon="Secondary canon",
  biblio="Published in Not Waving but Drowning (London: André Deutsch, 1957). A selection of The Norton Anthology of "
         "English Literature, 11th edition, vol. F, beginning on page 587.",
  notes="Critical views are as reported by Wikipedia (citing Sternlicht, Hotz-Davies, Severin, Thaddeus and James); none of "
        "those works was consulted directly.",
  ver="partially verified", sources=[W_NWBD, W_SMITH, NAEL]),
W10("Thoughts About the Person from Porlock", SMITH, "1962", "Poem (irregular rhymed stanzas)", "minor",
  genres=G("Light Verse", "Lyric Poetry"),
  themes=T("Art, the artist and the creative life", "Death, illness and mourning", "Faith, doubt and the sacred"),
  overview="A poem by Stevie Smith that first appeared in her Selected Poems (1962): a comic revision of the story of the "
           "visitor who interrupted Coleridge's 'Kubla Khan', which turns into the speaker's longing to be interrupted "
           "herself.",
  content="Coleridge and the Person from Porlock; the visitor's imagined life; the speaker's own wish for a Person from "
          "Porlock to bring her thoughts to an end; a closing reflection on smiling and submitting.",
  summary="Coleridge received the Person from Porlock and ever after called him a curse, but why did he hurry to let him "
          "in? The truth, the speaker suspects, is that he was already stuck with 'Kubla Khan', and the visitor took the "
          "blame. She imagines the Person's modest life at the bottom of the hill, with a cat named Flo, and then admits "
          "that she longs for him herself, to bring her thoughts to an end; she runs to the gate and is hungry to be "
          "interrupted for ever and ever. The poem ends with mock-cheerful advice to smile and submit to the purposes of "
          "One Above, who is experimenting with human characters.",
  themes_text="Creative block and the excuses of poets; the wish for thought, and life, to be interrupted, which carries "
              "Smith's familiar longing for death; an ironic view of providence.",
  structure="Stanzas of uneven length with irregular rhyme, moving from literary anecdote to confession and a sardonic "
            "close.",
  style="Chatty, digressive and comic, with nonsense touches (the warlock grandmother, the cat named Flo) and a sudden "
        "darkening of tone.",
  ctx="Selected Poems (Longmans, 1962) gathered Smith's earlier work with seventeen previously unpublished poems at the time "
      "her readings and broadcasts were winning new readers.",
  sig="A favourite of anthologists and of writers on the 'Person from Porlock' legend, and a Norton selection.",
  canon="Minor canon",
  biblio="First published in Selected Poems (London: Longmans, 1962). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning on page 588.",
  notes="The first publication in Selected Poems (1962) rests on Jeremy Noel-Tod's newsletter essay, seen as a search "
        "extract, and is corroborated by two poets' websites; the paraphrase is stated from the text.",
  ver="partially verified", sources=[NOELTOD, W_SMITH, NAEL]),
W10("Do Not Go Gentle into That Good Night", DT, "1951", "Poem (villanelle)", "significant",
  genres=G("Lyric Poetry", "Elegiac Poetry", "Formal Verse"),
  themes=T("Death, illness and mourning", "Family, marriage and domestic life"),
  overview="Dylan Thomas's villanelle urging his father to 'rage, rage against the dying of the light', first published in "
           "the journal Botteghe Oscure in 1951 and collected in In Country Sleep and Collected Poems, 1934-1952 (both "
           "1952). It is one of his best-known poems.",
  content="The speaker's appeal to his father not to accept death quietly, supported by four kinds of men, wise, good, "
          "wild and grave, who each in their way rage against the end.",
  summary="Old age should burn and rave at close of day, the speaker says: do not go gentle into that good night; rage, "
          "rage against the dying of the light. Wise men know at their end that dark is right, but because their words "
          "forked no lightning they do not go gently. Good men, seeing how bright their frail deeds might have danced, "
          "rage against the dying of the light. Wild men who caught and sang the sun in flight, and learn too late that "
          "they grieved it on its way, do not go gentle. Grave men near death, who see with blinding sight that blind eyes "
          "could blaze like meteors, rage too. In the last stanza the speaker turns to his father, 'there on the sad "
          "height', and asks him to curse and bless him now with his fierce tears, repeating both refrains.",
  themes_text="Resistance to death and the refusal of resignation, set against the knowledge that death is right and "
              "necessary; the son's love for a dying father; the regret of lives unfulfilled. Seamus Heaney saw in the "
              "form a figure of the union of opposites, balancing natural grief and the recognition of necessity.",
  structure="A villanelle: five tercets and a closing quatrain, nineteen lines on two rhymes, with two refrains ('Do not "
            "go gentle into that good night' and 'Rage, rage against the dying of the light') alternating and joined at "
            "the end.",
  style="Incantatory iambic pentameter; puns ('good night', 'grave men') and paradoxes ('blinding sight', 'curse, bless'); "
        "intense, rhetorical repetition.",
  ctx="Thomas's father, David John Thomas, a schoolmaster, was going blind and died just before Christmas 1952; Wikipedia "
      "reports that the poem was written in 1947 in Florence, though its dating and its connection with his father's "
      "illness are disputed. It was printed in Botteghe Oscure, the Rome review, in 1951.",
  sig="One of the most famous villanelles in English and among the best-known poems of the century, often quoted and set "
      "to music (Stravinsky's In Memoriam Dylan Thomas sets the full text).",
  crit="Heaney called it 'obviously a threshold poem about death'; Jonathan Westphal reads the 'sad height' as a "
       "metaphorical plateau of loneliness before death, while Walford Davies hears King Lear on the heath and Gloucester "
       "at Dover cliff.",
  canon="Secondary canon",
  biblio="First published in Botteghe Oscure (1951); collected in In Country Sleep, and Other Poems (New Directions, 1952) "
         "and Collected Poems, 1934-1952 (Dent, 1952). A selection of The Norton Anthology of English Literature, 11th "
         "edition, vol. F, beginning on page 693.",
  notes="Wikipedia states that Thomas wrote the poem in 1947 in Florence (citing Ferris) and flags as failed verification "
        "its claim that the poem was written for his dying father. The composition date is not recorded for that reason.",
  ver="partially verified", sources=[W_DNGG, W_DT, NAEL]),
W10("Colonization in Reverse", LB, "1966", "Poem (dramatic monologue in Jamaican Creole, ballad quatrains)", "significant",
  genres=G("Performance Poetry", "Light Verse", "Political Poetry"),
  themes=T("Migration, exile and diaspora", "Decolonisation, the end of empire and the new nation", "Nationhood and national identity"),
  movements=M(CAR, POSTCOL),
  overview="A poem by Louise Bennett, collected in Jamaica Labrish (1966), in which a Jamaican speaker tells Miss Mattie "
           "the 'joyful news' that Jamaicans are emigrating to England by the shipload and the planeload, colonising "
           "England in reverse.",
  content="The speaker's account of the post-war migration of Jamaicans to Britain, their hopes of good jobs, their "
          "readiness to live on the dole, and her wonder at how England will stand being colonised in reverse.",
  summary="'Wat a joyful news, Miss Mattie,' the speaker begins, she feels as if her heart will burst: Jamaica people are "
          "colonising England in reverse. By the hundred and the thousand, from country and from town, by the shipload and "
          "the planeload, Jamaica is England bound. Everyone's future plan is to get a big-time job and settle in the "
          "mother land; some set up cheap-fare-to-England agencies to show their loyalty. Once they arrive, the speaker "
          "goes on, they find their different roles, and some prefer to draw the dole rather than work, since England is "
          "now paying them. What an island, what a people, she exclaims, who faced war and braved the worst; but she "
          "wonders how the English will stand being colonised in reverse.",
  themes_text="The poem turns the history of empire upside down: the colonised now settle the 'mother country'. Its "
              "comedy mocks both the migrants' grand hopes and English fears of immigration, and asserts Jamaican "
              "language and wit as a match for the coloniser's.",
  structure="Ballad quatrains rhyming on the second and fourth lines, addressed throughout to Miss Mattie, a recurrent "
            "listener in Bennett's poems who creates the illusion of a dialogue.",
  style="Jamaican Creole in the rhythms of speech and of mento song; irony, hyperbole and puns; written for performance.",
  ctx="Large-scale migration from Jamaica to Britain followed the Second World War, from the arrival of the Empire Windrush "
      "in 1948 until the Commonwealth Immigrants Act of 1962. Bennett, who had lived in England in the late 1940s, "
      "collected the poem in Jamaica Labrish (Sangster's, 1966), introduced by Rex Nettleford.",
  sig="Bennett's best-known poem and a classic of Caribbean writing on the Windrush migration, widely anthologised, "
      "taught and performed.",
  crit="Eric Doumerc reads Bennett's poems as rooted in the mento tradition, with Miss Mattie as the average Jamaican woman "
       "and comic distance used to defuse hardship; postcolonial critics read the poem as subversive mimicry of colonial "
       "rhetoric.",
  canon="Secondary canon",
  biblio="Collected in Jamaica Labrish (Kingston: Sangster's Book Stores, 1966), pp. 179-180. A selection of The Norton "
         "Anthology of English Literature, 11th edition, vol. F, beginning on page 722.",
  notes="The earliest printing was not established; the subject (migration after 1948) places its writing within the "
        "period. The page numbers come from Doumerc and from an article in the Journal of Contemporary Issues in "
        "Education, both citing Jamaica Labrish. The paraphrase is stated from the text; the dates of the migration are "
        "general knowledge.",
  ver="partially verified", sources=[DOUMERC, W_LB, NAEL]),
W10("History of the Voice", KB, "1984", "Lecture-essay (literary criticism)", "significant",
  genres=G("Postcolonial Criticism", "Literary Essay"),
  themes=T("Language, writing and the limits of representation", "Nationhood and national identity", "History, truth and the uses of the past"),
  movements=M(POSTTH, CAR),
  alt=["History of the Voice: The Development of Nation Language in Anglophone Caribbean Poetry"],
  overview="Kamau Brathwaite's History of the Voice: The Development of Nation Language in Anglophone Caribbean Poetry "
           "(London: New Beacon Books, 1984), a lecture-essay that named 'nation language', the English of the Caribbean's "
           "African-descended people, and argued that Caribbean poetry must break with the pentameter. Norton prints an "
           "excerpt under the title 'Nation Language'.",
  content="An account of the languages of the Caribbean and of the submergence of African languages under English; the "
          "tyranny of the pentameter; the definition of nation language; its oral and musical qualities; the poets, "
          "calypsonians and performers who have used it.",
  summary="Brathwaite begins from the linguistic history of the Caribbean, where the imported languages of slaves and "
          "labourers were suppressed and given the status of inferiority, while the colonisers' languages became official. "
          "What English has given the Caribbean as a model for poetry is the pentameter, which carries an experience that "
          "is not the islands' own: 'The hurricane does not roar in pentameters.' The problem is how to find a rhythm "
          "close to the natural and environmental experience. His answer is nation language, which he distinguishes from "
          "'dialect', a word carrying the pejorative overtones of caricature: an English that is not the standard, "
          "imported, educated English, but that of the submerged, surrealist experience and sensibility that has always "
          "been there and is now coming to the surface. Nation language is strongly influenced by African models; it is "
          "oral, so that its noise, rhythm and timbre are part of its meaning, and it is tied to the music of the region, "
          "from calypso to dub. He credits T. S. Eliot with introducing the notion of the speaking voice and the "
          "conversational tone, and traces the line of poets and performers, from Louise Bennett to the dub poets, who "
          "have made nation language a literary medium.",
  themes_text="Language as a site of colonial power and of resistance; the recovery of submerged African culture; the "
              "claim that Caribbean experience needs its own forms and rhythms; the unity of word, sound and music in "
              "an oral tradition.",
  structure="A lecture expanded into an essay, moving from history to theory and to illustration, with many quoted and "
            "performed examples.",
  style="Conversational and performative, close to the spoken lecture, with Brathwaite's own coinages and typographic "
        "emphasis.",
  ctx="Brathwaite gave the lecture in 1979 (Wikipedia lists a History of the Voice of that year) and published the expanded "
      "text with New Beacon Books, the London publisher associated with John La Rose and the Caribbean Artists Movement, "
      "in 1984; it came out of the movement's debates of the late 1960s on Caribbean aesthetics.",
  sig="The publication established Brathwaite as the authority on nation language, the term now commonly preferred to "
      "'dialect' for the non-standard English of Caribbean and African diaspora writing; 'the hurricane does not roar in "
      "pentameters' is among the most quoted sentences of Caribbean criticism.",
  crit="Later critics apply its arguments to oral and performance poetry, disaster writing and social media, and set it "
       "beside Glissant's 'forced poetics'; some note its debt to Eliot's conversational tone, which Brathwaite himself "
       "acknowledged.",
  canon="Secondary canon",
  biblio="History of the Voice: The Development of Nation Language in Anglophone Caribbean Poetry (London: New Beacon Books, "
         "1984). Norton's excerpt, '[Nation Language]', is a selection of The Norton Anthology of English Literature, 11th "
         "edition, vol. F, beginning on page 725.",
  notes="Quotations come from articles citing the 1984 edition (pp. 7-16) seen as search extracts; the 1979 lecture is "
        "inferred from Wikipedia's list of works, and its venue was not established. The discussion of Louise Bennett "
        "and New Beacon's association with La Rose are general knowledge.",
  ver="partially verified", sources=[W_NATION, ARCHIP, MDPI_ZONG, W_KB, NAEL]),
W10("Calypso", KB, "1967", "Poem (section of the sequence Rights of Passage)", "minor",
  genres=G("Lyric Poetry", "Political Poetry"),
  themes=T("History, truth and the uses of the past", "Class, labour and social mobility", "Land, place and regional belonging"),
  movements=M(CAR),
  overview="A poem from Kamau Brathwaite's Rights of Passage (1967), the first book of The Arrivants trilogy: a history of "
           "the Caribbean islands from their creation to the tourist present, told in the rhythms of calypso.",
  content="The islands imagined as a stone skipped across the sea; their transformation into sugar plantations; the "
          "carnival and steel band of the present; the servility of the tourist economy.",
  summary="The poem opens with the islands' creation: a stone skids, arcs and blooms into islands, Cuba and San Domingo, "
          "Jamaica and Puerto Rico, Grenada, Guadeloupe, Bonaire. The islands then roar into green plantations ruled by "
          "silver sugar cane, sweat and profit, and history becomes the story of slavery and the plantation. In the "
          "present the steel drums beat and the rum flows in a carnival that no one can stop, while the tourist "
          "trade keeps the islanders in service.",
  themes_text="The bright surface of Caribbean pleasure set against its history of slavery and its present of "
              "dependence; the music of calypso used to tell an unhappy story.",
  structure="Several sections in different rhythms, from the incantatory list of island names to calypso and dance "
            "measures, forming one movement of Rights of Passage.",
  style="Short, percussive lines; place-names as music; calypso rhythm and Caribbean speech; irony beneath celebration.",
  ctx="Rights of Passage (1967) follows the African diaspora from Africa to the Caribbean and the cities of the West; "
      "with Masks (1968) and Islands (1969) it formed The Arrivants (1973), generally considered Brathwaite's best work.",
  sig="One of the most anthologised parts of The Arrivants and an early demonstration of Brathwaite's use of Caribbean "
      "musical forms.",
  canon="Minor canon",
  biblio="Published in Rights of Passage (London: Oxford University Press, 1967); reprinted in The Arrivants: A New World "
         "Trilogy (1973). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on "
         "page 730.",
  notes="The paraphrase and the description of Rights of Passage are stated from general knowledge of the text, not "
        "from a consulted source, and the publisher of Rights of Passage is general knowledge; the dates of the trilogy come from Wikipedia.",
  ver="partially verified", sources=[W_KB, NAEL]),
W10("Letter SycoraX", KB, "1992", "Poem (verse letter in nation language and 'Sycorax video style')", "minor",
  genres=G("Experimental Poetry", "Visual Poetry"),
  themes=T("Language, writing and the limits of representation", "Technology, media and consumer society", "Decolonisation, the end of empire and the new nation"),
  movements=M(CAR, POSTCOL),
  overview="A poem by Kamau Brathwaite in Middle Passages (1992): Caliban writes to his mother Sycorax on the computer, in "
           "nation language and in the computer fonts, sizes and layouts that Brathwaite called 'Sycorax video style'. It "
           "revises 'X/Self xth letter from the thirteenth provinces' from X/Self (1987).",
  content="A letter from Caliban to his mother, the witch Sycorax of The Tempest, about writing on the computer and about "
          "language, power and memory, set out in shifting typefaces.",
  summary="Caliban, the colonised slave of The Tempest, writes a letter to his mother Sycorax, the poem's 'X', telling her "
          "about the computer he is learning to write on and about the language he is making of the master's English. "
          "The letter mixes complaint, comedy and visionary excitement; its broken words, spellings and changing fonts and "
          "sizes make the page itself part of the meaning, and the letter X recurs as a visual sign of Sycorax and of the "
          "unnamed self.",
  themes_text="The colonised writer's struggle with Prospero's language and technology, turned into a new medium of "
              "expression; the recovery of the suppressed mother; revision as survival after catastrophe.",
  structure="A long verse letter with salutation and sign-off, its layout varied by font, size and alignment.",
  style="Nation language, puns and neologisms, and typographic experiment that slows and complicates reading.",
  ctx="Brathwaite developed the Sycorax video style after the 'time of salt' of 1986-1990, the death of his wife, the loss "
      "of his archive to Hurricane Gilbert and a near-fatal attack; Middle Passages printed the poem while, its "
      "publishers noted, the style was still being developed.",
  sig="A key text of Brathwaite's late experimental poetics and of Caribbean rewritings of The Tempest.",
  canon="Minor canon",
  biblio="Published in Middle Passages (Newcastle upon Tyne: Bloodaxe, 1992; New York: New Directions, 1993), a revision of "
         "'X/Self xth letter from the thirteenth provinces' in X/Self (1987). A selection of The Norton Anthology of "
         "English Literature, 11th edition, vol. F, beginning on page 1103.",
  notes="The publication history comes from a study of the versions of the X/Self letter (seen as a search extract), "
        "which counts four printings, each revised. The publishers of Middle Passages are general knowledge. The paraphrase "
        "is general, since the text was not consulted.",
  ver="partially verified", sources=[XSELF, W_KB, NAEL]),
W10("Decolonising the Mind", NGUGI, "1986", "Essays (four lectures on language and literature)", "significant",
  genres=G("Postcolonial Criticism", "Political Essay"),
  themes=T("Language, writing and the limits of representation", "Decolonisation, the end of empire and the new nation", "Power, the state and surveillance"),
  movements=M(POSTTH, AFR),
  alt=["Decolonising the Mind: The Politics of Language in African Literature"],
  overview="Ngũgĩ wa Thiong'o's Decolonising the Mind: The Politics of Language in African Literature (London: James Currey, "
           "1986), four essays arguing that African writers should write in African languages; it is his 'farewell to "
           "English' and one of the most cited texts of postcolonial studies. Norton prints part of the first essay, 'The "
           "Language of African Literature'.",
  content="Four essays, 'The Language of African Literature', 'The Language of African Theatre', 'The Language of African "
          "Fiction' and 'The Quest for Relevance', mixing autobiography, history, theory and pedagogy.",
  summary="Ngũgĩ describes the book as a summary of issues in which he had been passionately involved for twenty years of "
          "fiction, theatre, criticism and teaching. The first essay argues that language carries culture and that the "
          "imposition of European languages on African children, through schools that punished them for speaking their "
          "mother tongues, separated them from their own history and community and colonised the mind; he recalls his "
          "own schooling in Gikuyu and then in English. Writing in English or French, however brilliant, builds a "
          "literature for an elite and for foreign readers. The second essay tells the story of the Kamiriithu theatre "
          "and of the play Ngaahika Ndeenda, performed in Gikuyu by villagers until the government closed it; the third "
          "describes the writing of his first Gikuyu novel, Caitaani Mũtharaba-inĩ, in prison; the fourth calls for "
          "African literature, languages and peoples to be placed at the centre of education. He closes by bidding "
          "farewell to English as the vehicle of any of his writing.",
  themes_text="Language as both means of communication and carrier of culture; colonial education as cultural "
              "domination; neocolonialism; the writer's choice of medium, audience and purpose; the dignity of African "
              "languages.",
  structure="Four essays, several of them first given as lectures, with an introduction and a statement of farewell.",
  style="Direct, polemical and autobiographical, combining memoir with Marxist and anti-imperialist analysis.",
  ctx="After the closure of Ngaahika Ndeenda in 1977 Ngũgĩ was imprisoned without trial and, on his release, went into "
      "exile; he had already turned to Gikuyu for his fiction. The book entered the 'language debate' of postcolonial "
      "studies, opposed by writers such as Achebe and Rushdie who defended the use of English.",
  sig="One of Ngũgĩ's best-known and most cited works, which made him the pre-eminent voice in the debate on African "
      "languages; it is a standard text of postcolonial theory courses.",
  crit="Oliver Lovesey calls it the book that cemented his place in the language debate; critics weigh its call for "
       "African languages against the practical case for English as a means of international communication and of "
       "subversive appropriation.",
  canon="Secondary canon",
  biblio="Decolonising the Mind: The Politics of Language in African Literature (London: James Currey; Nairobi: Heinemann "
         "Kenya, 1986), 114 pages. Norton's excerpt, from 'The Language of African Literature', is a selection of The "
         "Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 732.",
  notes="The Heinemann Kenya imprint, the account of his schooling and the content of the third and fourth essays are "
        "general knowledge; the essays' titles, the farewell to English and the dedication come from Wikipedia. The "
        "excerpt's title is the CSV's 'From The Language of African Literature'.",
  ver="partially verified", sources=[W_DTM, W_NGUGI, NAEL]),
W10("Discourse on the Logic of Language", NP, "1989", "Poem (multi-voiced text of verse, prose and edicts)", "significant",
  genres=G("Experimental Poetry", "Political Poetry"),
  themes=T("Language, writing and the limits of representation", "Race, racism and the struggle for civil rights", "Gender, feminism and women's lives"),
  movements=M(CAR, POSTCOL),
  overview="A poem by M. NourbeSe Philip in She Tries Her Tongue, Her Silence Softly Breaks (1989): a page-spanning collage "
           "in which a stuttering verse on English as 'my mother tongue' and 'a foreign anguish' is set beside a story of "
           "a mother licking her newborn daughter, two edicts on the treatment of slaves' languages, and textbook "
           "passages on the brain.",
  content="The speaker's verse on English as mother tongue and father tongue; a narrative of a mother blowing words into "
          "her child's mouth; Edicts I and II on separating slaves by language and cutting out the tongue of any slave "
          "who speaks it; scientific accounts of the speech centres of the brain; a multiple-choice question.",
  summary="The central verse begins 'English / is my mother tongue', then breaks down: a mother tongue is not a foreign "
          "lan lan lang, language, l/anguish, anguish, a foreign anguish. English is her father tongue, and she has no "
          "mother tongue, only a 'dumb-tongued', 'dub-tongued' speech, and she asks what she is to do. Beside it, in "
          "capitals, a narrative tells of a mother who licks her newborn daughter clean and blows her own words, her "
          "mother's words, into the child's mouth. Two edicts in italics, in the cool voice of administration, advise "
          "slave owners to mix their slaves of different language groups so that they cannot plot rebellion, and order "
          "that any slave caught speaking his native language have his tongue removed. Passages in the style of a "
          "physiology textbook describe the brain's speech centres and nineteenth-century theories of racial difference, "
          "and the poem ends with a multiple-choice test on the tongue.",
  themes_text="The violence of colonial and slave history embodied in language: English as the imposed father tongue and "
              "the mother tongue that survives in secret transmission between women. The poem exposes the apparent "
              "objectivity of the coloniser's discourses, legal and scientific, and makes the reader's difficulty part "
              "of its meaning.",
  structure="Several texts on the page at once, verse in the centre, the mother's story in a margin, edicts and textbook "
            "passages elsewhere, so that the page must be read in more than one direction.",
  style="Stammering repetition and wordplay (language, languish, anguish), capitals, italics and documentary registers set "
        "against each other; collage and fragmentation.",
  ctx="She Tries Her Tongue, Her Silence Softly Breaks won the Casa de las Américas Prize in manuscript and was published in "
      "1989; it belongs to the Caribbean debates on nation language and to the feminist writing of black women in "
      "Canada.",
  sig="Philip's most anthologised poem and a central text of Caribbean and Canadian experimental writing on language, "
      "much taught and studied.",
  crit="Critics read it through Brathwaite's nation language, Bhabha's in-betweenness and theories of the violence of "
       "language, as deconstructing the apparent objectivity and logic of English; reviewers of the book quoted its "
       "'foreign anguish' as its key pun.",
  canon="Secondary canon",
  biblio="Published in She Tries Her Tongue, Her Silence Softly Breaks (Charlottetown: Ragweed Press, 1989). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 743.",
  notes="The publisher is general knowledge. Wikipedia also lists Discourse on the Logic of Language (1989) as a separate "
        "item, presumably a separate printing, which was not checked. Details of the edicts and textbook passages are "
        "stated from general knowledge of the text and corroborated by student and review extracts that were not cited.",
  ver="partially verified", sources=[ANGLOSAX, W_NP, NAEL]),
W10("The Prophet's Hair", SR, "1981", "Short story", "significant",
  genres=G("Short Story", "Satirical Fiction"),
  themes=T("Faith, doubt and the sacred", "Family, marriage and domestic life", "Violence, crime and justice"),
  movements=M(SAS, MAGIC),
  overview="A short story by Salman Rushdie, first published in the London Review of Books on 16 April 1981 and collected, "
           "revised, in East, West (1994). In Srinagar, a secular moneylender who comes upon the stolen relic of the "
           "Prophet Muhammad's hair becomes a tyrannical zealot, with disastrous results for his family.",
  content="Hashim the moneylender keeps the relic stolen from the Hazratbal shrine; its effect on him and his household; "
          "his children's plan to have it stolen back by the master thief Sheikh Sin; the night on which everything goes "
          "wrong.",
  summary="In a fierce winter in Srinagar, the moneylender's son Atta goes into the city's most dangerous quarter to hire "
          "a thief and is beaten nearly to death. The story then explains. Hashim, a rich moneylender who prides himself "
          "on his rational, honourable life, found floating in the lake a silver phial holding the famous hair of the "
          "Prophet, stolen the previous morning from the shrine at Hazratbal. A collector, he decided to keep it. At once "
          "he changed: he ordered his family to read the holy book for hours each day, forbade the cinema, told terrible "
          "truths about his marriage and his mistress, insulted his son and accused his daughter Huma of lewdness, and "
          "beat her. When Atta tried to return the relic it seemed to come back to the house by itself. Huma hires the "
          "thief Sheikh Sin to steal it; but on the night, Hashim, waking, grabs a sword, rushes out, and in the darkness "
          "kills his daughter, and then himself; the injured Atta dies, and Hashim's wife goes mad. The relic is "
          "restored to the shrine, and the thief's crippled sons, miraculously cured, lose their living as beggars.",
  themes_text="Religious fanaticism as a possession that destroys the possessor; the clash of secular rationalism and "
              "faith; greed and the urge to collect; the comic and terrible ironies of miracles.",
  structure="A short story opening in medias res and moving back through flashback to the climactic night and an ironic "
            "coda.",
  style="Long, rolling sentences full of clauses, wit and Kashmiri detail; magical realism handled with comic deadpan.",
  ctx="The story draws on the theft of the relic from the Hazratbal shrine in December 1963 and its recovery about two "
      "weeks later; Rushdie wrote it for the London Review of Books in the year of Midnight's Children. After the "
      "Satanic Verses affair its subject gained new resonance.",
  sig="One of Rushdie's most anthologised stories, read as a parable of religious zeal and a forecast of the themes of "
      "his later work.",
  canon="Secondary canon",
  biblio="First published in the London Review of Books, vol. 3, no. 7 (16 April 1981); collected in a revised version in "
         "East, West (London: Jonathan Cape, 1994). A selection of The Norton Anthology of English Literature, 11th "
         "edition, vol. F, beginning on page 1064.",
  notes="The LRB page (seen as a search extract) confirms the date and parts of the plot; the rest of the plot is stated "
        "from general knowledge of the text and agrees with study summaries that were not cited. The Hazratbal theft of "
        "1963, the revision for East, West and its publisher are general knowledge.",
  ver="partially verified", sources=[LRB_PH, W_SR, NAEL]),
W10("Imaginary Homelands", SR, "1991", "Essays and criticism (collection)", "significant",
  genres=G("Literary Essay", "Political Essay", "Postcolonial Criticism"),
  themes=T("Migration, exile and diaspora", "Language, writing and the limits of representation", "Nationhood and national identity"),
  movements=M(SAS, POSTCOL),
  alt=["Imaginary Homelands: Essays and Criticism 1981-1991"],
  overview="Salman Rushdie's Imaginary Homelands: Essays and Criticism 1981-1991 (London: Granta, in association with "
           "Penguin, 1991), a collection of essays and reviews whose title essay calls the migrant the central or "
           "defining figure of the twentieth century. Norton prints two bracketed excerpts from it.",
  content="Essays on India, Pakistan and Britain, on politics (the assassination of Indira Gandhi, the 1983 general "
          "election, censorship, the Labour Party, Palestinian identity), on the Satanic Verses affair, and on writers "
          "including Naipaul, Greene, Barnes and Ishiguro, with the title essay on memory, migration and Midnight's "
          "Children.",
  summary="The title essay, first printed in the London Review of Books on 7 October 1982, begins from Rushdie's "
          "attempt to recover the Bombay of his childhood in Midnight's Children and argues that exiles and migrants, "
          "looking back, create not actual cities or villages but imaginary homelands, fragmentary and partial, whose "
          "broken mirror is a truth of its own. Comparing his novel with other literature of diaspora, he claims that the "
          "migrant, whether from one country, language or culture to another or from a traditional village to a modern "
          "city, is perhaps the central or defining figure of the twentieth century, and that writers of the Indian "
          "diaspora in Britain may claim English and the English tradition as their own. Other essays dispute the "
          "category of 'Commonwealth literature', review contemporary novelists, attack the politics of Thatcher's "
          "Britain and its racism, and, in the later pieces, respond to the attacks on The Satanic Verses.",
  themes_text="Migration and memory, the right of the migrant writer to English and to many traditions, the politics of "
              "Britain, India and Pakistan, and the freedom of literature.",
  structure="Essays, lectures and reviews of 1981-1991, grouped in sections by subject, with the title essay first.",
  style="Witty, combative, conversational prose, mixing memoir, polemic and close reading.",
  ctx="Published two years into the fatwa, the book gathered a decade of Rushdie's journalism, lectures and "
      "criticism, from the years of Midnight's Children to the Satanic Verses affair.",
  sig="A key statement of migrant and postcolonial writing in Britain; its title has become a common term for the "
      "imagined homelands of diaspora.",
  canon="Secondary canon",
  biblio="Imaginary Homelands: Essays and Criticism 1981-1991 (London: Granta Books, in association with Penguin, 1991). "
         "Norton's two excerpts, '[The British Indian Writer and a Dream-England]' and '[English Is an Indian Literary "
         "Language]', are selections of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on "
         "pages 747 and 750.",
  notes="The essays from which Norton's two excerpts come were not identified; the second is commonly taken from "
        "\"'Commonwealth Literature' Does Not Exist\" (1983), which is general knowledge, not checked. The summary of "
        "the title essay beyond Wikipedia's account (the broken mirror, the claim to English), the grouping of the essays and "
        "the essays beyond those Wikipedia names are general knowledge.",
  ver="partially verified", sources=[W_IH, LRB_PH, NAEL]),
]
