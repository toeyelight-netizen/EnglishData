"""Installment 10, wave 08: Samuel Selvon's 1946-2000 bibliography (Caribbean writing in English).

The second Caribbean author of installment 10, and the first Indo-Caribbean one. All ten
novels (1952-1983), the collection of stories (1957), the two books of plays (1988, 1991)
and the selection of prose (1989) are recorded. They were checked against the list of
published works, with first publishers, in South Asian Britain: Connecting Histories; the
Wikipedia articles on Selvon and The Lonely Londoners; Encyclopaedia Britannica; Kwame
Dawes's article in EBSCO Research Starters; Bill Schwarz's essay on The Lonely Londoners in
London Fictions (2013); GradeSaver's plot summary of that novel; the Toronto Metropolitan
University Library's guide, which reprints publishers' synopses; and Peepal Tree Press's
pages for the two books of plays. Accounts of the other novels rest on search-result
extracts only: Caribbean Beat (2023), an unsigned essay at Northern Arizona University,
eNotes on A Brighter Sun, two scholarly discussions of The Plains of Caroni, the Penguin
description of Moses Ascending, Mawenzi House's description of An Island Is a World and an
Anthurium introduction (2025). None of the books was read.

Sources disagree on the dates of Turn Again Tiger (1958 or 1959), Ways of Sunlight (1957 or
1958), I Hear Thunder (1963 or 1962) and Eldorado West One (1988 or 1989), on the number of
novels (ten or eleven) and on the place of Selvon's death; each record states the
disagreement. Every work is linked to "Caribbean Literature in English"; the books set
among West Indians in London (The Lonely Londoners, Ways of Sunlight, The Housing Lark, the
two later Moses novels and Eldorado West One) are also linked to "Black British Writing and
the Windrush Generation", whose taxonomy entry names The Lonely Londoners. No other
movement is assigned.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ  # noqa: E402

WIKI_SS = "Sam Selvon (Wikipedia)"
WIKI_TLL = "The Lonely Londoners (Wikipedia)"
SCHWARZ = "Samuel Selvon: 'The Lonely Londoners' - 1956, by Bill Schwarz (London Fictions)"
GS = "The Lonely Londoners Full Plot Summary (GradeSaver)"
BRIT = "Samuel Selvon (Encyclopaedia Britannica)"
DAWES = "Samuel Selvon, by Kwame S. N. Dawes (EBSCO Research Starters)"
SAB = "Sam Selvon (South Asian Britain: Connecting Histories)"
TMU = "Samuel Selvon (Asian Heritage in Canada, Toronto Metropolitan University Library)"
PT_ELD = "Eldorado West One (Peepal Tree Press)"
PT_HIGH = "Highway in the Sun (Peepal Tree Press)"
CBEAT = "Sam Selvon at 100 (1923-2023), by Shireen Ali (Caribbean Beat)"
NAU = "Race and Community in Sam Selvon's Fiction (Northern Arizona University web essay)"
ENOTES = "A Brighter Sun Summary (eNotes)"
JWIL = "Journal of West Indian Literature 24.2 (November 2016), Caribbean Ecocriticism special issue"
NOV70 = "The Novel since 1970 (ResearchGate PDF)"
PENG_MA = "Moses Ascending (Penguin Modern Classics description, as reproduced by booksellers)"
MAWENZI = "An Island Is a World (Mawenzi House)"
ANTH = "Of Selvon and Sentimentality: Diasporic Rememberings (Anthurium)"
SS = "Samuel Selvon"
CAR = "Caribbean Literature in English"
WIN = "Black British Writing and the Windrush Generation"
MIGR = "Migration, exile and diaspora"
RACE = "Race, racism and the struggle for civil rights"
IDENT = "Identity, authenticity and the divided self"
CLASS = "Class, labour and social mobility"
LAND = "Land, place and regional belonging"

AUTHORS = [
A10(SS, MAJ, "1923", "1994", "San Fernando, Trinidad",
  "Trinidadian; Indo-Trinidadian Caribbean (West Indian) novelist, short-story writer and playwright writing in English, of Indian and Scottish-Indian descent, in England from 1950 to 1978 and in Canada from 1978",
  "Trinidad-born novelist whose The Lonely Londoners (1956), narrated as well as spoken in Trinidadian creole, founded the fiction of Caribbean migrant London, and whose novels of Indo-Trinidadian village life, from A Brighter Sun (1952) to The Plains of Caroni (1970), trace the meeting of Indian and Creole Trinidad.",
  "Samuel Dickson Selvon was born on 20 May 1923 in San Fernando, in the south of Trinidad, the sixth of seven children. His father, Bertwyn Fraser Selvon, was a Christian of Madrasi Indian descent who managed a dry-goods store; his mother, Daisy Irene Dickson, was the daughter of a Scotsman and of Keasoo, a woman of South Asian origin. Peepal Tree Press, drawing on his own accounts, describes a creolised household with little part in Hindu ritual, and a boy formed by the American films at the local cinemas. He left Naparima College at fifteen and from 1940 to 1945 was a wireless operator with the Trinidad branch of the Royal Naval Reserve (Dawes calls him a telegraph operator), the post that brought him into contact with the wartime American presence. From 1945 (1946 in Britannica) to 1950 he worked for the Trinidad Guardian as a reporter and on its literary page, South Asian Britain says as literary editor of the Sunday Guardian, publishing stories and sketches under the names Michael Wentworth, Esses, Ack-Ack and Big Buffer. He married Draupadi Persaud in 1947. In 1950 he moved to London, where he lived first in a hostel near Earl's Court, took menial jobs and became a clerk at the Indian Embassy, while reading for the BBC's Caribbean Voices and placing stories and poems in the London Magazine, the New Statesman and The Nation. Guggenheim Fellowships (1955 and 1968 in Wikipedia; 1954 and 1968 in Dawes), a Society of Authors travelling scholarship (1958) and Arts Council grants (1960) supported his work, and in 1969 Trinidad and Tobago awarded him the Hummingbird Medal (Gold). He wrote more than twenty radio plays and several television scripts for the BBC, scripted Horace Ové's Pressure (1976), the first full-length Black British feature film, and in the late 1960s took part in the Caribbean Artists Movement. In 1963 he married Althea Daroux. After a creative writing fellowship at the University of Dundee (1975-77) he moved in 1978 to Canada and settled in Calgary, Alberta; he taught creative writing as a visiting professor at the University of Victoria, worked for some months as a janitor at the University of Calgary and then became its writer-in-residence, and Dawes adds residencies at Alberta and Winnipeg. The University of the West Indies (1985) and Warwick (1989) gave him honorary doctorates. He died of respiratory failure on 16 April 1994 during a visit to Trinidad, at Piarco International Airport according to Wikipedia (Britannica says Port of Spain), and received the Chaconia Medal (Gold) posthumously that year.",
  "Selvon published ten novels between 1952 and 1983 (Peepal Tree and Dawes count eleven), one collection of stories, two books of plays and a selection of prose. Six of the novels are set in Trinidad, mostly among Indo-Trinidadians: A Brighter Sun (1952) and its sequel Turn Again Tiger (1958), An Island Is a World (1955), I Hear Thunder (1963), The Plains of Caroni (1970) and Those Who Eat the Cascadura (1972). The others follow West Indians in London: The Lonely Londoners (1956), The Housing Lark (1965) and the two later Moses novels, Moses Ascending (1975) and Moses Migrating (1983); the stories of Ways of Sunlight (1957) move between the two settings. Much of his drama was written for the BBC, and two collections, Eldorado West One (1988) and Highway in the Sun (1991), preserve some of it; Foreday Morning (1989) gathers prose from 1946 onwards.",
  "In The Lonely Londoners Selvon used creolised English, or 'nation language', for narration as well as dialogue, an innovation Wikipedia calls groundbreaking; he explained that the novel 'just shot along' once he wrote both in dialect. Dawes praises folk idioms of 'sophistication and sheer virtuosity', a rare union of empathy and humour, and a Lonely Londoners told like a 'ballad' or calypso. Schwarz finds in Selvon's London an exact geography and an echo of Eliot's 'unreal' city, and Britannica singles out the 'extensive and striking use of dialect' in Turn Again Tiger.",
  "Creolisation and the relations of Indian and African Trinidadians; the peasant culture of the cane fields and its passing under mechanisation; manhood, marriage and domestic violence; migration to Britain, racism, poverty and the improvised community of 'the boys'; return, Anglophilia and the divided loyalties of the migrant; Carnival as a fleeting image of a society beyond race.",
  "Selvon came to attention in the 1950s with other Caribbean writers, Naipaul among them (Britannica), and is a founder of Caribbean migrant fiction in Britain. The Lonely Londoners, his most widely known book, is read as a forerunner of Zadie Smith's White Teeth and Hanif Kureishi's The Buddha of Suburbia, and Dawes finds his influence 'consistently apparent' in the many fiction writers who followed him. Britannica judged A Brighter Sun the first book in which an East Indian author wrote 'with such quiet authority and simple charm' about Indo-Trinidadian life, and it was long a set text on the Caribbean Examinations Council syllabus.",
  bib_status="substantially complete",
  bib_note="Bibliography status, 1946-2000: substantially complete for books. Recorded as works: the novels A Brighter Sun (1952), An Island Is a World (1955), The Lonely Londoners (1956), Turn Again Tiger (1958), I Hear Thunder (1963), The Housing Lark (1965), The Plains of Caroni (1970), Those Who Eat the Cascadura (1972), Moses Ascending (1975) and Moses Migrating (1983); the stories Ways of Sunlight (1957); the plays Eldorado West One (1988) and Highway in the Sun and Other Plays (1991); and Foreday Morning: Selected Prose 1946-1986 (1989). Not recorded as works, because their contents were not examined: 'A Meap Story' (1954), listed only in Wikipedia's bibliography, and 'A Drink of Water' (1968), listed only by Dawes, neither of them described anywhere consulted; stories and poems in Trinidad papers (1945-50), on Caribbean Voices and in the London Magazine, New Statesman, The Nation and Evening Standard, including 'Cane is Bitter' (whether it is in Ways of Sunlight was not checked); more than twenty BBC radio plays and the television scripts Anansi the Spider Man and Home, Sweet India, except as collected in the two books of plays; the screenplay of Pressure (1976), written with Horace Ové; the essays 'The West Indian Patchwork' (1955, for the Royal Geographical Society), 'Three into one can't go - East Indian, Trinidadian or West Indian?' (Wasafiri 3.5, 1986, pp. 8-11) and 'Finding West Indian Identity in London' (Kunapipi 9.3, 1987, pp. 34-38; dated 1988 by Schwarz and reprinted in Tiger's Triumph, 1995); a film script of The Lonely Londoners, finished before his death (Dawes); and, unfinished at his death, the novel 'A High of Zero' and an autobiography (Dawes). Outside the period: Poems of Sam Selvon (ed. Kenneth Ramchand, 2012) and Calypso in London (2023). Checked against the list of published works with first publishers in South Asian Britain, Wikipedia's bibliography, Dawes's list of works and Britannica. Discrepancies: Turn Again Tiger is 1958 in South Asian Britain, Dawes and Britannica but 1959 in Wikipedia's list and Caribbean Beat; Ways of Sunlight is 1957 except in Britannica (1958); I Hear Thunder is 1963 except in Britannica (1962); Eldorado West One is 1988 except in Wikipedia's list (1989); the Guggenheim years (1955 or 1954, and 1968); his wartime post (wireless or telegraph operator); his start at the Trinidad Guardian (1945 or 1946); the number of his novels (ten, or eleven in Peepal Tree, Dawes and the Harry Ransom Center inventory cited by Wikipedia); and the place of his death (Piarco International Airport or Port of Spain).",
  ver="verified", sources=[WIKI_SS, SAB, BRIT, DAWES, PT_HIGH, SCHWARZ],
  infl=["T. S. Eliot"], alt=["Sam Selvon", "Samuel Dickson Selvon"],
  pseudo=["Michael Wentworth", "Esses", "Ack-Ack", "Big Buffer"]),
]

WORKS = [
W10("A Brighter Sun", SS, "1952", "Novel", "significant",
  genres=G("Bildungsroman", "Social Novel"),
  themes=T("Childhood, adolescence and coming of age", RACE, "Family, marriage and domestic life", CLASS),
  movements=M(CAR),
  overview="Selvon's first novel, published in London by Allan Wingate in 1952, follows Tiger, a sixteen-year-old Indo-Trinidadian married off to the still younger Urmilla, through his first years of adult life in the suburban village of Barataria during the Second World War. Britannica summarises its subject as East Indians and Creoles in Trinidad, their prejudices and mutual distrust, and the effect of that animosity on a young man; Wikipedia notes that the building of the Churchill-Roosevelt Highway is seen through Tiger's eyes.",
  content="Tiger's first years of marriage, set against the war and the American presence in Trinidad: the move from the cane district of Chaguanas to Barataria, friendship with Creole neighbours, work on the highway the Americans build, a crisis in Urmilla's pregnancy and Tiger's resolve to build a better house.",
  summary="At sixteen Tiger is married by his family to Urmilla and sent from the sugar-cane district of Chaguanas to Barataria, where the couple begin life in a mud hut and Tiger farms. Away from their parents' influence they make friends with their Afro-Creole neighbours, Joe and Rita, whose brick house, with electricity and running water, Tiger envies. The couple have a daughter, and Tiger longs for a son. When the American military arrives to build a highway through the farmland, Tiger does not protest but takes work on the construction, and he tries to learn better English in order to rise. Anxious to prove himself a man, he invites his American bosses to dinner, gets drunk and beats the pregnant Urmilla. She falls ill; an Indian doctor and a Creole doctor both refuse to treat her, and an English doctor agrees to. The son Tiger wanted is stillborn. Chastened and more mature, Tiger begins to build a new house with the help of friends and neighbours.",
  themes_text="The publisher's synopsis reprinted by Toronto Metropolitan University Library names the novel's two concerns as Tiger's quest for manhood and the creolisation that he and Urmilla undergo in multiracial Barataria, away from their parents. Britannica stresses the prejudice and distrust between Indians and Creoles; the refusal of the Indian and Creole doctors and the help of the English one turn that theme into the crisis of the plot. Better English is Tiger's chosen route to advancement, and eNotes's analysis links his drinking, his violence and his refusal to accept that the child might not be a boy to his efforts to prove his manhood.",
  structure="A chronological narrative that follows Tiger from his wedding through the war years to the start of the new house; Dawes describes it as a novel of maturation set in a rural Indian community.",
  style="Britannica found in it, for the first time, an East Indian author writing 'with such quiet authority and simple charm' about Indo-Trinidadian life; Dawes credits Selvon's work in general with an innovative use of folk idiom.",
  ctx="Selvon wrote it in London after 1950, looking back to the years when he served as a wireless operator and, as Peepal Tree's author profile puts it, was closely involved with the wartime American presence that provides the novel's backdrop: American bases and the highway built to serve them.",
  sig="Wikipedia notes that it was a popular choice on the Caribbean Examinations Council's English literature syllabus for many years. It began Selvon's fiction of Indo-Trinidadian life, which Turn Again Tiger (1958) continues, and Selvon later adapted its story of Tiger and Urmilla's first year of marriage as the play Highway in the Sun (published 1991).",
  chars="Tiger, a young Indo-Trinidadian; Urmilla, his wife; Joe and Rita, their Afro-Creole neighbours; American supervisors on the highway; an English doctor",
  canon="Secondary canon",
  biblio="First edition: Allan Wingate, London, 1952 (South Asian Britain). Reissued by Longman, London, 1979 (Toronto Metropolitan University Library).",
  notes="Not read. The plot follows eNotes's summary, seen only as a search-result extract, checked against the synopsis printed under Turn Again Tiger in the Toronto Metropolitan University guide (which describes this novel), Britannica, Wikipedia and Dawes; the record is partially verified for that reason.",
  ver="partially verified", sources=[ENOTES, TMU, BRIT, WIKI_SS, DAWES, SAB, PT_HIGH]),

W10("An Island Is a World", SS, "1955", "Novel", "minor",
  genres=G("Literary Novel"),
  themes=T(MIGR, IDENT),
  movements=M(CAR),
  overview="Selvon's second novel, published by Allan Wingate in London in 1955, is set in Trinidad after the Second World War. Its present publisher calls it a novel of personal and intellectual quest; the Anthurium special issue on Selvon (2025) reports Ramabai Espinet's case for reconsidering its place in his work.",
  content="Two brothers leave post-war Trinidad, one for England and one for the United States, while their elders think of returning to India.",
  summary="In the post-war colony, as an earlier generation thinks of returning to India, the young Foster goes to England and his brother Rufus leaves for the United States, each in search of himself and his world. Mawenzi House's description, the only account of the plot consulted, presents the book as a moving story of personal and intellectual quest told with Selvon's humour and vivid sense of place.",
  themes_text="Departure and return: the brothers' journeys to England and America set against an older generation's dream of India, and the search for an identity that the colony cannot supply.",
  structure="Built, in the publisher's account, on the parallel quests of two brothers; the arrangement of the narrative was not examined.",
  style="The Globe and Mail, quoted by the publisher, praised Selvon's evocative description, affectionate humour and subtle use of folklore.",
  ctx="Published between A Brighter Sun and The Lonely Londoners; Nalini Mohabir, in the Anthurium issue, reads it with Selvon's 1955 essay 'The West Indian Patchwork' and his BBC play Home Sweet India as part of his thinking about return.",
  sig="One of Selvon's least discussed novels, though Espinet argues for its importance; it was reissued in Toronto by TSAR (1993) and Mawenzi House (2019).",
  canon="Minor canon",
  biblio="First edition: Allan Wingate, London, 1955 (South Asian Britain). Reissued by TSAR, Toronto, 1993 (Toronto Metropolitan University Library) and by Mawenzi House, Toronto, 2019 (304 pp.).",
  notes="Not read. The only account of the plot consulted is the publisher's description, seen as a search-result extract.",
  ver="partially verified", sources=[MAWENZI, ANTH, SAB, TMU, DAWES, WIKI_SS]),

W10("The Lonely Londoners", SS, "1956", "Novel", "major",
  genres=G("Social Novel", "Comic Novel"),
  themes=T(MIGR, RACE, "The city, the suburb and modern space", CLASS, "Language, writing and the limits of representation"),
  movements=M(CAR, WIN),
  overview="Selvon's third novel, published in London by Allan Wingate in 1956 and in New York by St Martin's Press (142 pages), follows a group of West Indian migrants, 'the boys', through about three years of their lives in post-war London. It has no plot in the usual sense: its episodes are held together by Moses Aloetta, a Trinidadian who has lived in London longer than the others and whose room the newcomers visit every Sunday morning. Its narrator speaks the same creolised English as its characters, a choice Wikipedia calls groundbreaking, and Wikipedia ranks it, with George Lamming's The Emigrants (1954), among the first novels about poor, working-class black migrants after the British Nationality Act of 1948. In 2022 it was one of the seventy books chosen for the BBC's Big Jubilee Read.",
  content="A sequence of episodes and character sketches rather than a continuous story. It opens on a foggy winter evening as Moses takes the number 46 bus from the corner of Chepstow Road and Westbourne Grove to Waterloo to meet a newcomer off the boat-train, and moves among the men he knows: Galahad, Cap, Bart, Lewis, Big City, Five Past Twelve, Harris and Tolroy's family, with the redoubtable Tanty. About two-thirds of the way through, a long passage without punctuation celebrates summer in the parks; winter and unemployment return, and the book ends with Moses on Chelsea Embankment, looking at the Thames and wondering whether he could write a book.",
  summary="On a grim winter evening Moses Aloetta, a Trinidadian night worker to whom people at home keep sending newcomers, goes to Waterloo to meet Henry Oliver, just arrived on the boat-train. At the station he finds his Jamaican friend Tolroy waiting for his mother, who arrives with the whole family, including Tolroy's aunt, Tanty Bessy, although he had asked her to come alone; Tanty makes everyone pose for a reporter, and the next day the photograph appears under the headline 'Now Jamaican Families Come to Britain'. Henry steps off the train in light clothes, with no luggage or winter coat and so cheerfully confident that Moses calls him Sir Galahad. Moses feeds him in his room in Bayswater and offers advice; Galahad, an electrician at home, insists on finding work alone, loses his way and his nerve in the street, and is rescued by Moses, who takes him to the employment exchange, where there are no openings but he registers for an insurance card.\n\nThe narrative turns to Moses' acquaintances. Cap, a Nigerian sent to London to study law, has spent his parents' money on drink and women, lives on loans he never repays and marries a French woman only to abandon her. Bart, light-skinned, passes himself off as South American and avoids other immigrants; he loses his English girlfriend, Beatrice, and is left searching London for her. Lewis, who works nights in the same factory as Moses, takes Moses' teasing claim that wives receive other men while their husbands are on the night shift as proof against his wife, Agnes, and beats her until she leaves him. Tanty, who never strays from her district, becomes a regular at a local shop that stocks West Indian goods, and makes her first journey alone by train and bus so easily that no one would have guessed it was her first. In summer Galahad, newly dressed in fine clothes, is wounded when a white child remarks on his colour, and alone in his room he addresses his own blackness: 'Colour, is you that causing all this'. Big City, who grew up in an orphanage in Trinidad, flaunts money whose source no one knows, and Harris, who prides himself on English manners, holds a dance at which the boys embarrass him: Tanty sweeps him on to the floor, Five Past Twelve dances close with one of his guests, and the night gets out of hand, ending with a bottle broken over Five's head. A long unpunctuated passage celebrates London in summer, when the boys 'coast a lime' in the parks and the city's sexual traffic between black men and white women runs through the night, until Moses closes it with 'a long sigh like a man who live life and see nothing at all in it'.\n\nWinter brings lay-offs. Hungry and out of work, Galahad catches a pigeon in a park while an old woman threatens to report him, and he and Moses cook it and laugh over stories of home until the talk turns sombre. At one of the Sunday gatherings Moses looks round at the boys with affection, unreliable as some of them are. At the end he stands on Chelsea Embankment, feeling in the river 'a greatness and a vastness', 'like it was something solid after feeling everything else give way'. Remembering Daniel's talk of taxi-drivers, porters and road-sweepers in France who had written best-sellers, he watches a tugboat on the Thames, 'wondering if he could ever write a book like that, what everybody would buy'.",
  themes_text="The novel shows a city that offers the migrants the worst jobs, exploitative landlords and liaisons that rarely go beyond sex, while their accents and colour mark them as outsiders and push them into a group identity formed by segregation; Wikipedia's account stresses their hopes of upward mobility, the self-hatred and disappointment that dog them and a stagnation summed up in Moses' complaint that after all these years he is 'neither forward nor backward'. London 'divide up in little worlds', he says, and you know nothing of the others 'except what you read in the papers'. Bill Schwarz reads the book as a new 'diasporic realism': the London the migrants find is 'unreal' because it does not match the England of their schooling, and the despised newcomer becomes the anthropologist who explains the natives' customs, with a mobility that gives 'the boys' a view of the whole city. Schwarz also finds its vision of human reciprocity compromised by the narrative's relentless objectification of white women. Helon Habila stressed that, though a book of exile and alienation, it is not sad: Selvon finds the humour in the direst tribulations, and its message of a shared humanity mattered more in 2007 than in the 1950s. David Dabydeen has noted that Moses was conceived as an Indian but that Selvon kept the ethnic divisions of the Caribbean out of his London community.",
  structure="Episodic and loosely chronological across roughly three years and their seasons, held together by Moses as host, adviser and witness; minor characters receive self-contained sketches. The opening journey to Waterloo and the closing scene on the Embankment frame the book, and Schwarz argues that Moses grows more reflective until he emerges as the author of his own tale. Dawes describes the whole as told like a ballad or calypso, and the summer section is a single stream-of-consciousness passage (pp. 92-102 in the edition Wikipedia cites).",
  style="A third-person narrator speaks the creolised English of the characters. Selvon told Michel Fabre that he began with narrative in standard English and dialogue in dialect, could not 'really move', and then wrote both in dialect, after which 'the novel just shot along'. The idiom includes the boys' names for places ('the Water' for Bayswater, 'the Gate' for Notting Hill), 'liming' and 'oldtalk', 'spades' for themselves and a string of slang for white women. Wikipedia links the stream-of-consciousness summer passage to modernism, and Schwarz notes that Selvon confirmed T. S. Eliot's influence, visible in the shared 'unreal' London of The Waste Land; the geography of the city, down to the bus route, is exact.",
  ctx="Selvon arrived from Trinidad in 1950 and, like his characters, stayed in a hostel near Earl's Court, did menial work and came to know the Bayswater and Harrow Road district, while reading for the BBC's Caribbean Voices. The novel belongs to the first decade of post-war Caribbean migration after the Windrush, when the run-down rooming houses of Notting Hill were packed with migrant tenants by landlords such as Peter Rachman. Two years after publication the area saw the white riots of 1958, and in 1959 the murder of the Antiguan Kelso Cochrane; the first Caribbean carnival in London, held in St Pancras Town Hall in January 1959, was one response (Schwarz).",
  sig="South Asian Britain calls it Selvon's most acclaimed and widely known novel. Susheila Nasta's introduction to the Penguin edition describes it as 'a major step forward in the process of linguistic and cultural decolonization', and Wikipedia, citing the British Library, presents it as a precursor of Zadie Smith's White Teeth (2000) and Hanif Kureishi's The Buddha of Suburbia (1990). For Dawes it confirmed that West Indian idiom could carry not only comic character but deep emotion and philosophical introspection. Its success led to two sequels, Moses Ascending (1975) and Moses Migrating (1983), and Selvon adapted its characters for radio in the plays of Eldorado West One (1988).",
  crit="The criticism consulted centres on language and form. Christian Mair (Journal of Commonwealth Literature, 1989) compared its use of Caribbean creole with V. S. Naipaul's in Miguel Street; Nasta reads its narrative voice as decolonising the London novel; Habila praised its humour. Schwarz relates its picaresque, 'atomized' London to Defoe's Moll Flanders and criticises its sexual politics. Dawes, in EBSCO's reference article, calls it a sophisticatedly constructed series of episodes and places it at the head of the comic Moses trilogy.",
  chars="Moses Aloetta, a Trinidadian long settled in London; Henry Oliver, called Sir Galahad, a newcomer from Trinidad; Tolroy, a Jamaican, his mother and his aunt Tanty Bessy; Lewis and his wife Agnes; Cap, a Nigerian who came to study law; Bart and his English girlfriend Beatrice; Big City; Harris; Five Past Twelve; Daniel",
  canon="Major canon",
  biblio="First edition: Allan Wingate, London, 1956, cover designed by Charles Mozley (Schwarz); first US edition by St Martin's Press, New York (Wikipedia). Reissued by Longman, Harlow, 1985, with an introduction by Kenneth Ramchand (Toronto Metropolitan University Library), and by Penguin, London, 2006, with an introduction by Susheila Nasta (Wikipedia).",
  notes="Not read. The summary combines Wikipedia's article, Schwarz's essay (which quotes the opening and closing passages) and GradeSaver's plot summary, used for the order of episodes and for minor characters; Dawes, South Asian Britain and Britannica supply publication facts and assessments. GradeSaver calls Lewis Tolroy's brother, other accounts his brother-in-law, so the record does not state the relationship; GradeSaver's section summary places the pigeon in Hyde Park, which the record leaves as 'a park'. Wikipedia says Moses has been in London more than ten years; the record does not give a figure.",
  ver="verified", sources=[WIKI_TLL, SCHWARZ, GS, WIKI_SS, DAWES, SAB, BRIT, TMU]),

W10("Ways of Sunlight", SS, "1957", "Short-story collection", "minor",
  genres=G("Short-Story Collection"),
  themes=T(LAND, MIGR, CLASS),
  movements=M(CAR, WIN),
  overview="Selvon's only collection of short stories, published by MacGibbon & Kee in London in 1957 (1958 in Britannica), sets stories of rural Trinidad beside stories of hard times among West Indians in London.",
  content="Short stories of village life in Trinidad, with its washerwomen, cane-cutters and the superstitious Ma Procop, and of West Indians in the cold basements of London.",
  summary="In the Trinidad stories, according to the publisher's synopsis, village washerwomen gossip and quarrel, cane-cutters toil for a meagre harvest, and old Ma Procop protects the fruit of her mango tree with magic. The London stories turn to the depression of hard times in the city, where people live in cold, damp basements and hustle for survival. Dawes finds in the collection Selvon's wit, his trickery as a writer and his poetic sensibility.",
  themes_text="Village rivalry and superstition, the labour of the cane fields, and the poverty and improvisation of migrant life in London: the two worlds of Selvon's fiction in a single book.",
  structure="Separate stories set in Trinidad and in London; the number and order of the stories were not checked.",
  style="Dawes stresses wit, trickery and poetic sensibility, and Selvon's complete immersion in telling a story for its entertainment.",
  ctx="Published the year after The Lonely Londoners; South Asian Britain counts it, with The Housing Lark, as an extension of Selvon's writing on migrant life in Britain.",
  sig="Reissued by Longman in 1987 with a critical introduction by Jane Grant; Britannica lists it among Selvon's later works.",
  canon="Minor canon",
  biblio="First edition: MacGibbon & Kee, London, 1957 (South Asian Britain; Wikipedia; Dawes); Britannica gives 1958. Reissued by Longman, Harlow, 1987, with a critical introduction by Jane Grant (Toronto Metropolitan University Library).",
  notes="Not read; the contents were not examined, so the individual stories are not recorded. The account rests on the publisher's synopsis reprinted by Toronto Metropolitan University Library and on Dawes.",
  ver="partially verified", sources=[TMU, DAWES, SAB, BRIT, WIKI_SS]),

W10("Turn Again Tiger", SS, "1958", "Novel", "minor",
  genres=G("Social Novel", "Literary Novel"),
  themes=T(LAND, RACE, IDENT, CLASS),
  movements=M(CAR),
  overview="The sequel to A Brighter Sun, published by MacGibbon & Kee in London in 1958 (1959 in Wikipedia's list and Caribbean Beat), takes Tiger back to the sugar-cane country of his childhood for a year. Britannica calls it perhaps Selvon's best novel and singles out its extensive and striking use of dialect.",
  content="Tiger's year in the cane-growing village of Five Rivers, where his father lives, among the cane workers and the white overseer's household.",
  summary="Tiger leaves Barataria to return for a year to the sugar-cane country of his childhood and help his father, and after several misadventures learns more about life and himself (Caribbean Beat). At Five Rivers he is ashamed of his sexual response to Mrs Robinson, a white woman of the estate, but is saved, in the reading of the Northern Arizona University essay, by his peasant values; after the Robinsons have left, a cane worker tells him, 'You is one of we, Tiger', though near the end another reproaches him for boasting that he could read and write while helping nobody. In the radio play Selvon made from the novel, Tiger learns that he cannot turn his back on his Indian past if he is to lay its ghosts to rest and face the future whole (Peepal Tree).",
  themes_text="The pull of the cane fields and of the Indian past on a man who has left them, race and sex across the hierarchy of the estate, and the duty an educated man owes his community; Dawes reads the novel as Selvon's closer look at creolisation.",
  structure="Organised around a single year's stay in the cane country, continuing the protagonist of A Brighter Sun.",
  style="Britannica singles out its extensive and striking use of dialect.",
  ctx="Published two years after The Lonely Londoners, it returns to the Indo-Trinidadian countryside; South Asian Britain groups it with A Brighter Sun and The Plains of Caroni as Selvon's fiction of South Asian life in Trinidad.",
  sig="Britannica's 'perhaps his best'. Reissued by Heinemann in 1979 with an introduction and study questions by Sandra Pouchet Paquet, and adapted by Selvon for the BBC as one of the plays later collected in Highway in the Sun (1991).",
  chars="Tiger; Urmilla; Tiger's father; Mr and Mrs Robinson, a white couple on the estate; cane workers of Five Rivers",
  canon="Minor canon",
  biblio="First edition: MacGibbon & Kee, London, 1958 (South Asian Britain; Dawes; Britannica); Wikipedia's list and Caribbean Beat give 1959. Reissued by Heinemann, London, 1979, with an introduction by Sandra Pouchet Paquet (Toronto Metropolitan University Library).",
  notes="Not read. The account rests on search-result extracts from Caribbean Beat and the Northern Arizona University essay, with Peepal Tree's description of the radio adaptation; the name Five Rivers and the Robinsons come from the essay alone. The synopsis printed under this title in the Toronto Metropolitan University guide describes A Brighter Sun.",
  ver="partially verified", sources=[CBEAT, NAU, BRIT, DAWES, SAB, TMU, PT_HIGH, WIKI_SS]),

W10("I Hear Thunder", SS, "1963", "Novel", "minor",
  genres=G("Social Novel"),
  themes=T(CLASS, RACE, "Nationhood and national identity"),
  movements=M(CAR),
  overview="A novel of the Trinidadian middle class, published by MacGibbon & Kee in London in 1963 (1962 in Britannica), built on one young man's vow of chastity, in which Carnival stands for a society without racial barriers.",
  content="Adrian's year-long vow of celibacy, his temptation by his best friend's white wife, and Carnival.",
  summary="Adrian, a middle-class Indo-Trinidadian 'fete-boy' disgusted by the sexual looseness around him, vows to remain chaste for a year, and is tempted by the white wife of his best friend, Mark (Caribbean Beat; Northern Arizona University essay). Carnival, in the essay's reading, is Selvon's image of a society without racial barriers, 'Black, white, brown and yellow, rich and poor ... all were out on the streets jumping up in the bands', but one that cannot last: an exhausted Mark is determined to carry on to the 'Last Lap'.",
  themes_text="Sexual morality and self-discipline (the essay likens Adrian's experiment to Gandhi's brahmacharya), race and class among the Trinidadian middle class, and Carnival as a brief vision of a nonracial nation.",
  structure="Built around the year of Adrian's vow, with an episode of Carnival.",
  style="Caribbean Beat calls it a story of middle-class foibles; the Northern Arizona University essay finds it more cynical than compassionate.",
  ctx="Published in 1963, the year after Trinidad and Tobago's independence; with Those Who Eat the Cascadura it brings Selvon's concern with race back to Trinidad, in the essay's account.",
  sig="One of the least discussed of Selvon's novels; Britannica lists it among his later works.",
  chars="Adrian; Mark, his best friend; Mark's white wife",
  canon="Minor canon",
  biblio="First edition: MacGibbon & Kee, London, 1963 (South Asian Britain; Dawes; Wikipedia); Britannica gives 1962.",
  notes="Not read. The account rests on search-result extracts from Caribbean Beat and the Northern Arizona University essay.",
  ver="partially verified", sources=[CBEAT, NAU, SAB, DAWES, BRIT, WIKI_SS]),

W10("The Housing Lark", SS, "1965", "Novel", "minor",
  genres=G("Comic Novel", "Social Novel"),
  themes=T(MIGR, RACE, "The city, the suburb and modern space"),
  movements=M(CAR, WIN),
  overview="A comic novel of West Indian London, published by MacGibbon & Kee in 1965, in which Battersby and his friends try to pool their savings to buy a house. The Lynne Rienner synopsis calls it Selvon's fifth novel; by the dates of the first editions it is his sixth.",
  content="A scheme to buy a house together, and the gatherings, outings and quarrels of the West Indians drawn into it.",
  summary="Faced with unscrupulous and racist landlords, Battersby, a West Indian exile in London, and his rakish friends hatch a scheme to pool their money for a place of their own, but it does not go as planned (Caribbean Beat). The search for decent, affordable shelter brings hardships and comic situations and shows the exiles' dealings with English women, with the British in general and with one another (Lynne Rienner synopsis). The Northern Arizona University essay notes that the lark remains a lark to Battersby but becomes a grim commitment for Jean, and that at a community fete the Indo-Trinidadian Syl, asked why he does not go back to India, answers, 'Brit'n is my country'.",
  themes_text="Housing and racism in 1960s London, a migrant community forming out of separate struggles (the essay contrasts it with the 'lonely' struggles of the earlier novel), the price of assimilation, and the claim to belong.",
  structure="An ensemble comedy organised around the house-buying scheme.",
  style="Caribbean Beat calls it a cheeky comedy of a West Indian exile's search for shelter.",
  ctx="Set in London in the early 1960s, when West Indian migrants met discrimination from landlords; published in 1965.",
  sig="Selvon's second novel of West Indian London; reissued by Lynne Rienner, Boulder, in 1990.",
  chars="Battersby ('Bat'), who devises the scheme; Syl, an Indo-Trinidadian; Jean",
  canon="Minor canon",
  biblio="First edition: MacGibbon & Kee, London, 1965 (South Asian Britain). Reissued by Lynne Rienner, Boulder, 1990 (Toronto Metropolitan University Library).",
  notes="Not read. The account rests on the publisher's synopsis reprinted by Toronto Metropolitan University Library and on search-result extracts from Caribbean Beat and the Northern Arizona University essay; Jean's relation to Battersby is not stated in them.",
  ver="partially verified", sources=[TMU, CBEAT, NAU, SAB, WIKI_SS]),

W10("The Plains of Caroni", SS, "1970", "Novel", "minor",
  genres=G("Social Novel"),
  themes=T("Technology, media and consumer society", CLASS, LAND, "Family, marriage and domestic life"),
  movements=M(CAR),
  overview="Published by MacGibbon & Kee in London in 1970, the novel grew out of research on Trinidad's sugar industry sponsored by Tate and Lyle, which financed Selvon's return visit in 1969 (Journal of West Indian Literature, citing Michel Fabre). It turns on the trial of a mechanical cane harvester on a sugar estate.",
  content="An Indo-Trinidadian cane-cutting family and the trial of a mechanical harvester on a fictionalised Caroni estate, ending with an old cutter's fight against the machine.",
  summary="Romesh, a university-educated agricultural scientist working for the management of a fictionalised Caroni Ltd., oversees the testing of a new harvesting machine on the estate where his family cuts cane. The labourers fear, rightly, that it will cost them their jobs, and suspect it of being a 'metal Trojan horse'. The old cutter Balgobin, whose love for Seeta was thwarted by her arranged marriage to his brother, has given his life to the craft of cutting, and he resists the harvester with his cutlass. As he is dying, he is saved from arrest by the revelation that Romesh, raised as his nephew, is his son. Romesh leaves for London with his white girlfriend, while Balgobin is venerated as a hero.",
  themes_text="Mechanisation and the decline of sugar (the Journal of West Indian Literature essay reads the novel as foreshadowing oil's triumph over sugar in Trinidad), the dignity and skill of manual labour, hidden paternity, and the gulf between an educated, creolised generation and the cane-cutters.",
  structure="Centred on the harvester trial and its consequences, ending with Balgobin's death and Romesh's departure.",
  style="The journal essay quotes the rhythm of Balgobin's cutting ('his arm arcing the air ... in a grace of movement') and the villagers' images for the harvester: 'magic machine', 'space machine', 'giant monster'.",
  ctx="Tate and Lyle was preparing to leave Trinidad: in 1970 it sold a majority share in Caroni Ltd. to the PNM government, and it ended its involvement in 1976. Romesh cites the figures Selvon gathered, 1.94 man-days to produce a ton of sugar in Hawaii against 15.21 in Trinidad.",
  sig="Selvon turned it into the radio play Harvest in Wilderness (collected in Highway in the Sun, 1991). Its readers include a 1995 study of its idea of heroism, Supriya Agarwal's 'Conflict and Resolution' (2008), the ecocritical issue of the Journal of West Indian Literature (2016) and Kris Singh's essay on cane in Anthurium (2025).",
  chars="Balgobin, an old cane-cutter; Romesh, an agricultural scientist, raised as his nephew; Teeka, Romesh's brother, a cane-cutter; Seeta, whom Balgobin loved",
  canon="Minor canon",
  biblio="First edition: MacGibbon & Kee, London, 1970 (South Asian Britain; Journal of West Indian Literature). Reissued by Williams-Wallace, Toronto, 1985 (Anthurium's references).",
  notes="Not read. The plot rests on two independent scholarly discussions seen as search-result extracts (the Journal of West Indian Literature essay and 'The Novel since 1970'), which agree, except that the second calls Romesh a plantation manager and the first an agricultural scientist working for the management.",
  ver="partially verified", sources=[JWIL, NOV70, SAB, PT_HIGH, TMU, ANTH, WIKI_SS]),

W10("Those Who Eat the Cascadura", SS, "1972", "Novel", "minor",
  genres=G("Social Novel"),
  themes=T(RACE, "Love, intimacy and loss", "Myth, folklore and the supernatural"),
  movements=M(CAR),
  overview="Published in London by Davis Poynter in 1972, a novel of interracial love on a Trinidad plantation, framed by an obeahman's prophecy.",
  content="An Englishman's stay on a friend's Trinidad estate, his love for a young Indian woman and the prophecy of the village obeahman.",
  summary="Manko, the village obeahman, predicts trouble when an Englishman, Garry, comes to stay, and the prophecy is fulfilled when Garry falls in love with a local Indian woman, Sarojini (Caribbean Beat; Northern Arizona University essay). The essay reads the outcome as racism proving stronger than love, since Garry feels she cannot be transplanted from the world that made her, and notes the discovery that Roger Franklin, the plantation owner, secretly visits Indian women at night and is probably Sarojini's father.",
  themes_text="Interracial love and the sexual history of the plantation, which the essay calls a practice as old as slavery; obeah and prophecy; and the outsider's romantic idea of the island.",
  structure="Framed by Manko's prophecy and by its fulfilment in Garry's love affair.",
  style="Caribbean Beat calls it a story of interracial romance and the chaos it creates in a village; the essay sees the distant thunder of I Hear Thunder grown into a hurricane threatening the whole society.",
  ctx="Published in London in 1972, six years before Selvon left Britain; it was reissued in Toronto by TSAR in 1988.",
  sig="At his death Selvon was negotiating a film adaptation (Dawes).",
  chars="Manko, the village obeahman; Garry, an Englishman; Sarojini, a young Indian woman; Roger Franklin, the plantation owner",
  canon="Minor canon",
  biblio="First edition: Davis Poynter, London, 1972 (South Asian Britain). Reissued by TSAR, Toronto, 1988 (Toronto Metropolitan University Library).",
  notes="Not read. Garry, Sarojini and Roger Franklin are named only in the Northern Arizona University essay, seen as a search-result extract; the rest of the account comes from a Caribbean Beat extract.",
  ver="partially verified", sources=[CBEAT, NAU, SAB, TMU, DAWES, WIKI_SS]),

W10("Moses Ascending", SS, "1975", "Novel", "significant",
  genres=G("Comic Novel", "Satirical Fiction"),
  themes=T(MIGR, RACE, CLASS, "Language, writing and the limits of representation"),
  movements=M(CAR, WIN),
  overview="The second novel of the Moses trilogy, published in London by Davis Poynter in 1975, returns to Moses Aloetta of The Lonely Londoners, now the owner of a ramshackle house in Shepherd's Bush who means to write his memoirs while his handyman does the work. Wikipedia names it, with The Lonely Londoners, as the book for which Selvon is best known.",
  content="A comedy of Moses' rise from tenant to landlord and would-be memoirist, set in a house that fills with the politics and people of 1970s black London.",
  summary="Moses, once a poor Caribbean immigrant, has become the proud landlord of a ramshackle house in Shepherd's Bush. He sees himself as master of his own domain, writing his memoirs while his trusty sidekick and handyman, Bob, does all the work. His troubles are far from over. A Black Power group takes over the basement, headed by the indomitable Brenda; an illegal people-smuggling ring is discovered upstairs (an AbeBooks description of the first edition says Moses shelters Pakistani immigrants); and there is harassment by racist police, sheep-slaughtering in the back yard and a Black Panther on the loose. The publisher's description asks whether Moses' 'elaborately constructed castle in the air' will be demolished by these unruly forces, and presents the book as following the fortunes of characters from The Lonely Londoners.",
  themes_text="The comedy of upward mobility, as the former tenant becomes landlord and author; the Black Power politics of 1970s Britain, which invade the house Moses wants to keep for himself; police racism; and, in Dawes's reading of the trilogy, identity and belonging, as Moses discovers how English his values have become. Writing is itself a subject: the memoirs pursue the ambition with which The Lonely Londoners ends.",
  structure="Set largely in Moses' house, from the basement taken by the Black Power group to the upper floor where the smuggled immigrants are found; the episodes arise from its tenants and visitors.",
  style="Dawes counts the three Moses novels as a comic trilogy, and the publisher calls the book a hilarious and telling depiction of 1970s Britain.",
  ctx="Its Black Power group, people-smuggling and police harassment place it in the London of the early 1970s. It appeared in 1975, the year Selvon took up his fellowship at Dundee, three years before he left Britain for Canada.",
  sig="After The Lonely Londoners the best known of Selvon's books (Wikipedia). It continues the Moses saga, which Dawes takes as Selvon's most telling treatment of identity and belonging, and its characters reappear in the radio plays of Eldorado West One (1988). It has been reissued by Heinemann (1984) and Penguin (2008, and in Penguin Modern Classics).",
  chars="Moses Aloetta, landlord and would-be memoirist; Bob, his handyman; Brenda, leader of the Black Power group",
  canon="Secondary canon",
  biblio="First edition: Davis Poynter, London, 1975 (South Asian Britain; an AbeBooks listing of the first edition spells the publisher 'David-Poynter', ISBN 0706701887). Heinemann, London, 1984 (cited by Wikipedia); Penguin, London, 2008 (Toronto Metropolitan University Library); Penguin Modern Classics, ISBN 9780241504390.",
  notes="Not read. The summary rests on the Penguin Modern Classics description, seen in several booksellers' copies as search-result extracts, and on an AbeBooks listing; the record is therefore partially verified. Bob's background, the narrative voice and the ending are not described in the sources consulted and are not stated.",
  ver="partially verified", sources=[PENG_MA, WIKI_SS, DAWES, SAB, TMU, PT_ELD]),

W10("Moses Migrating", SS, "1983", "Novel", "minor",
  genres=G("Comic Novel"),
  themes=T(MIGR, IDENT, "Nationhood and national identity"),
  movements=M(CAR, WIN),
  overview="The last of the Moses novels, published by Longman in Harlow in 1983, five years after Selvon moved to Canada. It won the Georges Bugnet Award for the novel at the Alberta Literary Awards in 1984.",
  content="Moses, more than twenty-five years after The Lonely Londoners, goes back from London to Trinidad.",
  summary="More than twenty-five years after he became one of the 'Lonely Londoners', Moses Aloetta, though an avowed Anglophile, hankers for Trinidad, for sunshine, Carnival and rum punch, and the novel tells of his re-encounter with his native land (Lynne Rienner synopsis). In Dawes's account he at last musters the courage to return and must cope with recognising that he has become thoroughly and yet peculiarly English in his values, his sense of the world and his perception of himself.",
  themes_text="Return migration, Anglophilia and the colonial's divided loyalties, and the migrant seeing his homeland as a stranger.",
  structure="Framed by the return journey; the events in Trinidad are not described in the sources consulted.",
  style="The publisher speaks of Selvon's characteristic irony and delicacy of touch; Dawes includes it in the comic trilogy.",
  ctx="Published in 1983, after Selvon himself had left London for Calgary; the trilogy's homecoming came from a writer who had already left Britain for Canada.",
  sig="Georges Bugnet Award (1984). Reissued by Lynne Rienner, Boulder, in 2009 with an introduction by Susheila Nasta.",
  chars="Moses Aloetta",
  canon="Minor canon",
  biblio="First edition: Longman, Harlow, 1983 (South Asian Britain; Toronto Metropolitan University Library). Reissued by Lynne Rienner, Boulder, 2009, with an introduction by Susheila Nasta.",
  notes="Not read. The account rests on the publisher's synopsis reprinted by Toronto Metropolitan University Library and on Dawes; the plot in Trinidad is not described in either.",
  ver="partially verified", sources=[TMU, DAWES, SAB, WIKI_SS]),

W10("Eldorado West One", SS, "1988", "Plays (seven one-act radio plays, edited by Susheila Nasta)", "minor",
  genres=G("Radio Drama", "One-Act Play"),
  themes=T(MIGR, "The city, the suburb and modern space"),
  movements=M(CAR, WIN),
  overview="Seven one-act plays, published by Peepal Tree Press in Leeds in 1988 and edited with an introduction and notes by Susheila Nasta. Selvon turned several of his novels and stories into scripts for the BBC, and these plays bring to dramatic life characters first seen in The Lonely Londoners and Moses Ascending.",
  content="Seven one-act radio plays about Moses Aloetta and his friends Sir Galahad, Cap and Harris in London.",
  summary="The publisher's description asks whether Moses Aloetta, after long hard years in 'the Old Brit'n', will ever save enough money to go home to Trinidad, and answers that he will not if 'those damn vagabonds and reprobates', Sir Galahad, Cap and Harris, his so-called friends, have anything to do with it. The plays stage dreams and schemes, summer gaiety and winter disappointments, the experience of the parents and grandparents of today's Black British children, with Selvon's humour and poignancy.",
  themes_text="Migrant life in London, the dream of return and the friendships and small exploitations among 'the boys'.",
  structure="Seven separate one-act plays for radio; their titles and order were not checked.",
  style="Louis James, reviewing the book in Wasafiri, called them vivid radio plays that teachers wishing to dramatise Selvon's colourful stories would welcome.",
  ctx="Wikipedia dates Selvon's conversion of novels and stories into BBC radio scripts to the 1960s and 1970s; the collection appeared in 1988, ten years after he left Britain.",
  sig="One of two books that preserve some of Selvon's work for radio, of which South Asian Britain counts more than twenty plays.",
  canon="Minor canon",
  biblio="Peepal Tree Press, Leeds, 1988 (South Asian Britain; Toronto Metropolitan University Library; Dawes; Wikipedia's text), ISBN 9780948833069, 156 pp. Wikipedia's list gives 1989; the publisher's page gives 6 January 1998, presumably a reprint.",
  notes="Not read. The account rests on the publisher's description; the titles and broadcast dates of the plays are not recorded.",
  ver="partially verified", sources=[PT_ELD, SAB, TMU, DAWES, WIKI_SS]),

W10("Foreday Morning: Selected Prose 1946-1986", SS, "1989", "Selected prose (edited by Kenneth Ramchand and Susheila Nasta)", "minor",
  genres=G("Short Story", "Literary Journalism"),
  themes=T(LAND, MIGR),
  movements=M(CAR),
  overview="A selection of Selvon's prose from 1946 to 1986, edited by Kenneth Ramchand and Susheila Nasta and published by Longman in London in 1989. Wikipedia notes that much of the writing he did in Trinidad between 1945 and 1950 is found in it.",
  content="Stories, sketches and other prose from forty years, beginning with Selvon's newspaper writing in Trinidad.",
  summary="The book gathers prose from four decades of Selvon's career. Its earliest pieces belong to his years on the Trinidad Guardian, when he wrote stories and descriptive pieces under the names Michael Wentworth, Esses, Ack-Ack and Big Buffer; Dawes classes the book as nonfiction. The individual contents were not examined.",
  themes_text="As a retrospective selection it spans Selvon's subjects from Trinidad in the 1940s to life abroad; its themes are not analysed because the contents were not seen.",
  structure="A selection covering 1946-1986, made by two editors; its arrangement was not examined.",
  style="Not examined; the earliest pieces were journalism and short fiction written for a Trinidad newspaper.",
  ctx="Published in 1989, a year after Susheila Nasta's Critical Perspectives on Sam Selvon (1988) and in the year Warwick gave Selvon an honorary doctorate.",
  sig="The principal printed source for Selvon's early Trinidad writing, according to Wikipedia.",
  canon="Minor canon",
  biblio="Longman, London, 1989, edited by Kenneth Ramchand and Susheila Nasta (South Asian Britain; Wikipedia; Dawes).",
  notes="Contents not examined; the individual pieces are not recorded.",
  ver="partially verified", sources=[SAB, WIKI_SS, DAWES]),

W10("Highway in the Sun and Other Plays", SS, "1991", "Plays (four plays first broadcast by the BBC)", "minor",
  genres=G("Radio Drama", "Television Drama"),
  themes=T(IDENT, "Family, marriage and domestic life", MIGR),
  movements=M(CAR),
  overview="Four plays that Selvon wrote for BBC broadcast in the 1970s, published by Peepal Tree Press in Leeds in December 1991. The publisher presents them as his most focused treatment of the choice Indians in the Caribbean must make between tradition and creolisation; three adapt his Trinidad novels.",
  content="Highway in the Sun, Home Sweet India, Turn Again Tiger and Harvest in Wilderness.",
  summary="Highway in the Sun tells of Tiger and Urmilla's first year of marriage away from their extended family and of their dealings with Joe and Rita, their Afro-Creole neighbours, the matter of A Brighter Sun. In Home Sweet India Johnny, dismayed by his family's loss of culture, plans to return to India. In Turn Again Tiger, Tiger learns that he cannot turn his back on the Indian past if he is to lay its ghosts to rest and face the future whole. In Harvest in Wilderness the traditional cane-cutting world of Balgobin confronts the new technology of his creolised nephew Romesh, the conflict of The Plains of Caroni, 'but the past continues to spring surprises'.",
  themes_text="Tradition against creolisation among Indo-Trinidadians, return to India as a dream of recovered culture, marriage and friendship across ethnic lines, and the cane fields facing mechanisation.",
  structure="Four separate plays; three adapt the novels A Brighter Sun, Turn Again Tiger and The Plains of Caroni, while Home Sweet India has no novel behind it in the sources consulted.",
  style="Written for broadcast by the BBC, according to the publisher; their language and dramatic form were not examined.",
  ctx="The Anthurium special issue dates the BBC production of Home Sweet India to 1970, and Wikipedia and South Asian Britain list it among Selvon's television scripts; the book appeared in 1991, when he lived in Calgary.",
  sig="It gathers Selvon's drama of Indo-Trinidadian life as Eldorado West One gathers his London plays; Dawes cites it as the compilation of his dramatic works.",
  canon="Minor canon",
  biblio="Peepal Tree Press, Leeds, 1 December 1991 (publisher), ISBN 9780948833076, 215 pp.; reprinted 2008 (Toronto Metropolitan University Library).",
  notes="Not read. The account rests on the publisher's description. Which plays were made for radio and which for television is not stated; Wikipedia describes both books of plays as radio scripts but names Home Sweet India as a television script, hence the two genres.",
  ver="partially verified", sources=[PT_HIGH, SAB, DAWES, WIKI_SS, ANTH, TMU]),
]
