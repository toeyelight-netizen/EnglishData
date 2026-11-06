"""Installment 10, wave 10: Cyprian Ekwensi's 1946-2000 bibliography (African writing in English).

The third African author of installment 10 and the first Nigerian novelist of the popular
urban tradition. Ekwensi published from 1947, when the Onitsha novella When Love Whispers and
the folk tales of Ikolo the Wrestler appeared, to the 1990s. The bibliography was taken from
Gale's Contemporary Authors (the fullest list, with publishers) and checked against The
Writers Directory, Contemporary Black Biography, the Encyclopedia of World Biography, Gale's
Contextual Encyclopedia of World Literature, Wikipedia and the African Writers Series list.

Sixteen works whose contents are described in the sources consulted are recorded: the
novellas and folk tales of 1947-1962, the eight adult novels from People of the City (1954)
to For a Roll of Parchment (1986), Lokotown and Other Stories (1966) and the children's
parable King Forever! (1992). About twenty further books for young readers, two story
collections and an edited anthology are listed in the bibliography note, because no source
consulted describes what they contain. None of the books was read, except the front matter
and first chapter of Beautiful Feathers in the African Writers Series text.

The plot of Jagua Nana follows Donald Cosentino's profile in World Literature and Its Times;
People of the City follows Emmanuel Iduma's 2020 essay; Burning Grass and An African Night's
Entertainment follow Wikipedia; Iska, Survive the Peace and Divided We Stand rest on critical
essays and a review seen only as search extracts, and are labelled so. Sources disagree on
several dates (Burning Grass 1961 or 1962; Jagua Nana's Daughter 1986, 1987 or 1993; the Dag
Hammarskjold prize 1968 or 1969) and on how long People of the City took to write (ten or
fourteen days); each record states the disagreement. Every work is linked to "African
Literature in English", whose taxonomy entry names Ekwensi; no other movement is assigned.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ  # noqa: E402

CA = "Ekwensi, Cyprian (Odiatu Duaka) 1921- (Contemporary Authors, New Revision Series, via Encyclopedia.com)"
CBB = "Ekwensi, Cyprian 1921-, by Jeanne Lesinski (Contemporary Black Biography, vol. 37, via Encyclopedia.com)"
EWB = "Cyprian Ekwensi (Encyclopedia of World Biography, via Encyclopedia.com)"
GCE = "Ekwensi, Cyprian (Gale Contextual Encyclopedia of World Literature, via Encyclopedia.com)"
WD = "Ekwensi, Chief Cyprian D. (The Writers Directory, via Encyclopedia.com)"
WIKI_CE = "Cyprian Ekwensi (Wikipedia)"
WIKI_BOOKS = ("Wikipedia articles on People of the City, Jagua Nana, Burning Grass, An African Night's "
              "Entertainment and Lokotown and Other Stories")
LIT = "Jagua Nana, by Donald Cosentino (World Literature and Its Times, via Encyclopedia.com)"
IDUMA = ("Emmanuel Iduma, \"Cyprian Ekwensi's Lagos Noir\" (NYR Daily, The New York Review of Books, "
         "2 June 2020)")
BF_TEXT = "Cyprian Ekwensi, Beautiful Feathers (African Writers Series text, Eswatini Heritage Digital Library)"
ISKA_X = ("Iska: critical extracts (Virginia U. Ola, \"Cyprian Ekwensi's Iska Revisited\", Utafiti; Ulf "
          "Hannerz, \"The City, According to Ekwensi... and Onuzo\", Afropolitan, Berghahn)")
IFR = "Review of Survive the Peace (The International Fiction Review, University of New Brunswick)"
SMITH = ("Arthur E. E. Smith, \"Social Consciousness in the Writings of Cyprian Ekwensi\" (ChickenBones: "
         "A Journal, 2007)")
LOKO_CAT = ("Lokotown and Other Stories: contents (Tokyo Metropolitan Library catalogue; Jarndyce catalogue "
            "282, African Literature in English)")
ISR = "\"The Urban/Rural Conflict in African Literature\" (Igbo Studies Review, no. 8, 2020)"
VANGUARD = "\"The passport of Mallam Ilia's animation movie underway\" (Vanguard, Lagos, 16 January 2019)"
WARLIT = ("\"The masquerade of death macabre in the North: strange revolutionary aesthetics in Nigeria\" "
          "(Free Online Library)")
AWS = 'Heinemann African Writers Series (Wikipedia), section "Bibliography"'

CE = "Cyprian Ekwensi"
AFR = "African Literature in English"
CITY = "The city, the suburb and modern space"
DECOL = "Decolonisation, the end of empire and the new nation"
LOVE = "Love, intimacy and loss"
FAMILY = "Family, marriage and domestic life"
MYTH = "Myth, folklore and the supernatural"
LAND = "Land, place and regional belonging"
VIOLENCE = "Violence, crime and justice"
GENDER = "Gender, feminism and women's lives"
POWER = "Power, the state and surveillance"
NATION = "Nationhood and national identity"
WAR = "War, combat and its aftermath"
MIGR = "Migration, exile and diaspora"

AUTHORS = [
A10(CE, MAJ, "1921", "2007", "Minna, Northern Nigeria",
  "Nigerian; Igbo novelist, short-story writer and children's author, born and raised in Northern Nigeria, "
  "who chaired Biafra's Bureau for External Publicity during the civil war",
  "Nigerian novelist and pioneer of the popular urban novel, whose People of the City (1954) was among the "
  "first West African novels in English and whose Jagua Nana (1961) became the best-known Nigerian popular "
  "novel; also a prolific writer of folk tales, novellas and books for young readers from 1947 to the 1990s.",
  "Cyprian Odiatu Duaka Ekwensi was born on 26 September 1921 at Minna in Northern Nigeria, to Igbo parents "
  "from Nkwelle Ezunaka, in present-day Anambra State (Wikipedia). Contemporary Black Biography says that he "
  "grew up speaking Hausa as well as Igbo, and that his father, David Duaka, a storyteller and elephant "
  "hunter, told him the Igbo tales he later published. He was educated at Government College, Ibadan, at "
  "Achimota College in the Gold Coast and at the School of Forestry, worked for two years as a forestry "
  "officer, and taught biology, chemistry and English at Igbobi College, Lagos, from 1947 to 1949, the years "
  "of his first books. Trained as a pharmacist, he lectured at the School of Pharmacy in Lagos (1949-1956), "
  "and in 1951 a government scholarship took him to the Chelsea School of Pharmacy in London; he wrote People "
  "of the City on the voyage. Gale dates his first work for the Nigerian Broadcasting Corporation to 1951; "
  "Contemporary Authors makes him head of features there from 1957 to 1961, when he became federal director "
  "of information. He read his stories on the radio, where he was known as 'Your Favourite Story Teller'. In "
  "1966 he resigned and moved his family to Enugu; during the civil war he chaired Biafra's Bureau for "
  "External Publicity and directed its radio service, and travelled to the United States to raise money for "
  "Biafra. After the war he ran newspaper and publishing companies in the East (managing director of the "
  "Daily Star, 1975-1979), chaired the East Central State Library Board (1972-1975) and, according to Gale, "
  "the Federal Radio Corporation of Nigeria from 1991; Contemporary Black Biography says he wrote full time "
  "from 1984. He received the Dag Hammarskjold International Prize for Literary Merit (1969 in Gale's "
  "entries, 1968 in Wikipedia), was made a Member of the Order of the Federal Republic in 2001 and a fellow "
  "of the Nigerian Academy of Letters in 2006, and died at Enugu on 4 November 2007. He married Eunice "
  "Anyiwo; they had five children.",
  "Ekwensi's books of the period run from When Love Whispers and Ikolo the Wrestler (both 1947) to King "
  "Forever! and Masquerade Time (1992) and The Red Flag (1993). His adult novels are People of the City "
  "(1954), Jagua Nana (1961), Burning Grass (1962), Beautiful Feathers (1963), Iska (1966), Survive the Peace "
  "(1976), Divided We Stand (1980), and Jagua Nana's Daughter and For a Roll of Parchment (both 1986 or "
  "1987). His collections of stories include The Rainmaker (1965), Lokotown (1966) and Restless City and "
  "Christmas Gold (1975), and Contemporary Authors lists twenty-one juvenile titles, among them The Leopard's "
  "Claw (1950), The Drummer Boy and The Passport of Mallam Ilia (1960) and An African Night's Entertainment "
  "(1962). He also wrote hundreds of stories for newspapers, magazines and radio, and radio and television "
  "scripts for the BBC and Radio Nigeria. Emmanuel Iduma puts his output at nearly forty novels by his death; "
  "Cosentino notes that the U.S. edition of Jagua Nana (1969) already listed seven novellas, four works of "
  "folklore, two collections of stories and six novels.",
  "Ekwensi called himself 'a writer for the masses', more interested in 'the heart of the truth which the man "
  "in the street can recognize' than in style (interview with Lewis Nkosi, 1972, quoted in Contemporary "
  "Black Biography). His novels are episodic, a habit the Encyclopedia of World Biography traces to his "
  "beginnings as a pamphleteer and Contemporary Black Biography to the radio stories out of which People of "
  "the City grew. Juliet Okonkwo compares his naturalistic technique with Zola's; John Povey sees behind it a "
  "reading of American popular fiction and crime paperbacks. Dialogue moves between Pidgin, broken English "
  "and standard Nigerian English, sometimes within one paragraph, and his descriptions of dress borrow the "
  "language of advertising in Drum magazine (Cosentino).",
  "The modern West African city, above all Lagos, as a place of opportunity, corruption and moral danger for "
  "migrants from the countryside; women's independence and its price (Jagua Nana, Iska, Jagua Nana's "
  "Daughter); party politics and corruption at the end of colonial rule and after independence; Pan-African "
  "solidarity set against domestic failure (Beautiful Feathers); ethnic hostility, civil war and the "
  "hardships of the peace (Iska, Survive the Peace, Divided We Stand); colour prejudice met by African "
  "students in England (For a Roll of Parchment); and, in the folk tales and children's books, vengeance, "
  "heroism, adventure and moral instruction.",
  "Gale's Contextual Encyclopedia calls him the father of the modern Nigerian novel, and Martin Tucker the "
  "earliest and most prolific of the socially realistic Nigerian novelists (quoted in Contemporary Authors). "
  "People of the City preceded Achebe's Things Fall Apart by four years, and Charles Larson thought him "
  "probably the most widely read novelist in Nigeria. His standing with critics has been lower: Bernth "
  "Lindfors found none of his works free of 'amateurish blots and blunders', while his biographer Ernest "
  "Emenyonu saw in them 'a literature of social awareness and commitment'. He links the Onitsha market "
  "pamphlets, where he began, with the novel published in London, and the St. James Guide to Children's "
  "Writers calls him an acknowledged pioneer of Nigerian writing for young readers.",
  bib_status="substantially complete",
  bib_note="Bibliography status, 1946-2000: substantially complete for books; uncollected work is not "
  "listed. Recorded as works (16): When Love Whispers (1947); Ikolo the Wrestler and Other Ibo Tales (1947); "
  "People of the City (1954); The Drummer Boy (1960); The Passport of Mallam Ilia (1960); Jagua Nana (1961); "
  "Burning Grass (1962); An African Night's Entertainment (1962); Beautiful Feathers (1963); Iska (1966); "
  "Lokotown and Other Stories (1966); Survive the Peace (1976); Divided We Stand (1980); Jagua Nana's "
  "Daughter (1986); For a Roll of Parchment (1986); King Forever! (1992). Listed but not recorded as works, "
  "because no source consulted describes their contents: The Leopard's Claw (Nelson, 1950); Yaba Roundabout "
  "Murder (Tortoise Series, Lagos, 1962); The Rainmaker and Other Short Stories (African Universities Press, "
  "1965; revised 1971); The Great Elephant-Bird (Nelson, 1965; Wikipedia lists an Evans edition of 1990); "
  "Juju Rock (African Universities Press, 1966); The Boa Suitor (Nelson, 1966; Wikipedia gives 1949); "
  "Trouble in Form Six (Cambridge University Press, 1966); Coal Camp Boy (Longman Nigeria, 1971); Samankwe "
  "in the Strange Forest (Longman Nigeria, 1973; 1975 in Contemporary Black Biography); The Rainbow-Tinted "
  "Scarf and Other Stories (Evans, 1975; 1979 in Contemporary Black Biography); Samankwe and the Highway "
  "Robbers (Evans, 1975; 1979 in Contemporary Black Biography); The Restless City and Christmas Gold, with "
  "Other Stories (Heinemann, 1975; African Writers Series no. 172); Motherless Baby (novella, Fourth "
  "Dimension, 1980); Behind the Convent Wall (Evans, 1990; 1987 in The Writers Directory and Wikipedia); "
  "Murder Mile Two (Evans, 1990); Gone to Mecca (Heinemann, Ibadan, 1991); Masquerade Time (Heinemann, 1992); "
  "The Red Flag (Heinemann, 1993). Edited: Festac Anthology of Nigerian New Writing (1977). Contributions: "
  "'Law of the Grazing Field' in Langston Hughes's An African Treasury (1960); a story in Modern African "
  "Prose, edited by Richard Rive (African Writers Series no. 9, 1964). Also: hundreds of stories, articles "
  "and reviews in periodicals (West African Review, Black Orpheus, Flamingo and others), radio and television "
  "scripts for the BBC and Radio Nigeria, sound recordings (Voice of America, 1975-1979; Archive of World "
  "Literature on Tape, 1988), and 'No Escape from S.A.P.', published on the Internet. After 2000: Cash on "
  "Delivery (stories, 2007, according to Wikipedia). Dates that differ between sources are given in the work "
  "records.",
  ver="verified", sources=[CA, CBB, EWB, GCE, WD, WIKI_CE, AWS, LIT, IDUMA],
  infl=["H. Rider Haggard", "Robert Louis Stevenson"],
  alt=["Cyprian Odiatu Duaka Ekwensi", "C. O. D. Ekwensi"]),
]

WORKS = [
W10("When Love Whispers", CE, "1947", "Novella (romance)", "minor",
  genres=G("Novella", "Popular Romance Fiction"),
  themes=T(LOVE, FAMILY),
  movements=M(AFR),
  overview="Ekwensi's first published work, a short romance printed in Onitsha in 1947 under the name C. O. D. "
  "Ekwensi, and an early example of the Onitsha market literature that flourished between the Second World "
  "War and the civil war.",
  content="A short romance: a beautiful young woman with several suitors believes she has won the man she "
  "loves, while her father means her to marry an older man.",
  summary="According to Arthur Smith, the story, like Jagua Nana later, turns on a very attractive woman with "
  "several suitors; just as she believes she has won the love of her life, her father expects her to marry "
  "an older man in an arranged marriage. Donald Cosentino describes the novella as urban, erotic and "
  "picaresque, written in a popular idiom and devoted to the dilemmas of romantic love, a subject that "
  "university-educated Nigerian writers then avoided. How the conflict ends is not stated in the sources "
  "consulted.",
  themes_text="Romantic love against the arranged marriage: the conflict Cosentino names as the staple of "
  "Onitsha romance, 'true love' set against the mores of traditional marriage.",
  structure="A novella of pamphlet length, the format of the Onitsha presses; its chapter division was not "
  "examined.",
  style="Light and colloquial: Contemporary Black Biography calls it a short, light romance, and Cosentino "
  "speaks of its popular idiom.",
  ctx="Contemporary Black Biography says Ekwensi wrote it out of sorrow at a failed courtship of a young woman "
  "whose father insisted on a marriage of convenience. It appeared in Onitsha in 1947, while Ekwensi was "
  "teaching at Igbobi College, early in the market-literature boom that Cosentino dates from the end of the war.",
  sig="Its success encouraged Ekwensi to go on writing in the same vein (Contemporary Black Biography), and it "
  "ties him to the Onitsha market literature as well as to the Nigerian novel in English.",
  canon="Minor canon",
  biblio="Onitsha: Tabansi Bookshop, 1947, as C. O. D. Ekwensi (Contemporary Authors); Tabansi Press, 1947 "
  "(Contemporary Black Biography). Wikipedia dates it 1948 and cites a Tabansi Press edition of 1959.",
  notes="Not seen. The premise is known only from Smith's description, seen as a search extract, and the "
  "ending was not found.",
  ver="partially verified", sources=[CBB, LIT, SMITH, CA, WIKI_CE]),

W10("Ikolo the Wrestler and Other Ibo Tales", CE, "1947", "Folk tales and stories", "minor",
  genres=G("Folklore Collection", "Children's Fiction"),
  themes=T(MYTH, LAND),
  movements=M(AFR),
  overview="Ekwensi's first collection, published in London by Thomas Nelson in 1947 under the name C. O. D. "
  "Ekwensi: Igbo folk tales, many of them learned from his father, together with three of his own early "
  "stories.",
  content="Igbo folk tales and legends, with the short stories 'Banana Peel', 'The Tinted Scarf' and 'Land of "
  "Sani', according to Contemporary Authors.",
  summary="Contemporary Authors names among Ekwensi's early works the short stories 'Banana Peel', 'The "
  "Tinted Scarf' and 'Land of Sani', which he published together with a collection of Igbo folk tales under "
  "this title, after the years in the forest service when, Emenyonu says, he decided to become a writer. Contemporary Black Biography says that the "
  "tales were the Igbo stories and legends his father told him, and Gale's Contextual Encyclopedia that his "
  "first stories eulogised his father as an elephant hunter of unequalled bravery and a skilled carpenter. "
  "The title tale was not described in the sources consulted.",
  themes_text="Igbo heritage handed from father to son through storytelling, and the forest settings of "
  "Ekwensi's first adventure stories.",
  structure="A mixed book of retold folk tales and original stories; the number and order of the pieces were "
  "not established.",
  style="Retellings of oral tales for young readers; Contemporary Authors lists the book among his juvenile "
  "works.",
  ctx="Published in the same year as When Love Whispers, after two years as a forestry officer; Emenyonu dates "
  "Ekwensi's decision to become a writer to his solitary time in the forest reserves.",
  sig="His first book with a London publisher, and the first sign of the folk material he returned to in An "
  "African Night's Entertainment and The Great Elephant-Bird.",
  canon="Minor canon",
  biblio="London: Thomas Nelson, 1947, as C. O. D. Ekwensi (Contemporary Authors; Contemporary Black "
  "Biography). Gale's Contextual Encyclopedia calls it his first collection of short stories.",
  notes="Not seen. Whether 'The Tinted Scarf' is the title story of The Rainbow-Tinted Scarf and Other Stories "
  "(1975) was not established.",
  ver="partially verified", sources=[CA, CBB, GCE]),

W10("People of the City", CE, "1954", "Novel", "major",
  genres=G("Social Novel", "Naturalist Fiction", "Bildungsroman"),
  themes=T(CITY, DECOL, LOVE, VIOLENCE, "Class, labour and social mobility"),
  movements=M(AFR),
  comp=("1951", "1951"),
  overview="Ekwensi's first full-length novel, published in London by Andrew Dakers in 1954, and one of the "
  "first West African novels in English: among Nigerian books only Tutuola's The Palm-Wine Drinkard preceded "
  "it in Britain (Iduma), and Gale calls it the first West African English novel written in a modern style. "
  "Assembled from stories Ekwensi had broadcast on the radio, it follows a young crime reporter and "
  "dance-band leader through the overcrowded, corrupt and exhilarating life of an unnamed city recognisable "
  "as Lagos at the end of colonial rule. A revised edition appeared as no. 5 of Heinemann's African Writers "
  "Series in 1963, and American editions followed in 1967 and 1969.",
  content="Amusa Sango, twenty-six, reports crime for the West African Sensation and leads a highlife band. "
  "The novel follows his work and his entanglements with women: Aina, who pursues him; Elina, a convent girl "
  "to whom he is engaged; and Beatrice the Second, whom he finally marries. It also follows his reverses, "
  "eviction after a friend's scheme brings the police to his room and dismissal after he writes a story that "
  "favours that friend, while the city's crimes and deaths pass through the book as news.",
  summary="Amusa Sango has come to the city to make his fortune and is doing well when the novel opens: a "
  "crime reporter for the West African Sensation who knows 'the smell of news', and the leader of a highlife "
  "band, he is 'a most colourful and eligible young bachelor', and most girls in the city have his address "
  "(Iduma). His reports bring the city's violence into the book: a woman and her child killed by the men to "
  "whom she had lent her husband's gramophone; a man murdered by a society he had joined to better his "
  "fortunes, after he refused to hand over his first-born son. 'What is the secret of getting ahead in the "
  "city?' he asks. His private life is crowded. He is engaged to Elina, who is in a convent, but from the "
  "start he is pursued by Aina, whom he sleeps with and feels conflicted about but will not make happy; the "
  "people of the city, men and women alike, are shown as restless sexual beings. Then his fortunes turn. His "
  "friend Bayo uses Sango's room for a risky scheme, and the C.I.D. raids it and takes him away (Arthur "
  "Smith); after the uproar Sango is evicted. When he writes a story favouring the same friend, the paper "
  "dismisses him, and he is left without job or home. At his first meeting with Beatrice the Second, the "
  "woman he will marry, he calls himself one of the people overcrowding the city, 'only a musician, and a bad "
  "one at that. A hack writer, smearing the pages of the Sensation with blood and grime.' Her father gives "
  "the marriage a reluctant blessing, and the novel closes on the prospect of happiness, with Beatrice's "
  "'let's snatch happiness from life now'; nothing is said about work or recovery (Iduma). Along the way, as "
  "Gale's encyclopedia notes, Ekwensi disposes of characters he no longer needs by killing them and leaves "
  "subplots unresolved, and the city itself emerges as the villain: 'The city eats many an innocent life "
  "every year.'",
  themes_text="The city as moral hazard: Gale's encyclopedia sees in the novel a picture of 'squalor, bribery, "
  "corruption, and mercenary values', with the city as villain, and Iduma finds in it the setting Ekwensi "
  "kept returning to, the city as a 'hill' of wrongdoing. Ambition and survival: Sango's question about "
  "getting ahead, and his fall, show how a young man's idea of fortune becomes entangled with the city's "
  "promise. Love and marriage as the arc of a young man's life, the match that confirms his standing, which "
  "Iduma calls as prominent a theme as the vagaries of the city. The end of empire: written on the way to "
  "London in 1951, when West Africans were taking over the civil service, the press and the police, the book, "
  "in Iduma's reading, shows impatience with colonial dithering, and Wikipedia's article says it challenges "
  "European dominance. Ekwensi's didacticism and sense of retribution (Gale) give the episodes a moral frame.",
  structure="An episodic third-person narrative built from radio stories, which Gale says Ekwensi united into "
  "one long story in fourteen days on the voyage of 1951 (Contemporary Black Biography says ten). Gale finds "
  "the subplots loosely joined, like 'day-to-day records of events', and the episodic form drew most of the "
  "early criticism. The city is never named, though Yoruba speech and the lagoon point to Lagos (Iduma).",
  style="Fast, colloquial and journalistic, with the vocabulary of crime reporting and dance-hall nights. "
  "Chidi Okonkwo traces its manner to Westerns, detective thrillers, the Arabian Nights, Rider Haggard's "
  "'European-hero-in-Africa' tales, Stevenson's adventures and Indian films (cited by Wikipedia), and "
  "Wikipedia calls its tone didactic. Iduma, who copied whole paragraphs as a teenager, quotes its excited, "
  "cinematic sentences: 'The madness communicated itself to him'.",
  ctx="Written in 1951 on the ship that took Ekwensi to the Chelsea School of Pharmacy, after he had broadcast "
  "many of its episodes on Nigerian radio. It was first called Lajide of Lagos (Gale), was serialised in the "
  "Daily Times before book publication (Contemporary Black Biography) and came out in London in 1954, four "
  "years before Achebe's Things Fall Apart. It is set in the late 1940s and early 1950s, when the West African "
  "colonies were moving towards self-government; Cosentino calls it a kind of prequel to Jagua Nana.",
  sig="The first of Ekwensi's city novels and, in the Encyclopedia of World Biography's words, the first major "
  "novel published by a Nigerian; Gale calls it the first modern West African novel in English. It set the "
  "pattern of his later urban fiction and began a line of Lagos novels: Iduma says that any Nigerian writer "
  "who has tried to write about Lagos 'as a city with feeling' descends from Ekwensi, and names Sefi Atta's "
  "Everything Good Will Come and Teju Cole's Every Day Is for the Thief among the books that followed. It "
  "entered the African Writers Series as no. 5 in 1963, was published in the United States from 1967, and was "
  "reissued by New York Review Books Classics in 2020 with Iduma's introduction.",
  crit="Early reception in Britain was generally positive and dwelt on the urban setting (Wikipedia). Later "
  "critics were harsher about its construction: Gale's encyclopedia faults its careless plotting and its "
  "'disregard for the humanity of some of its characters, who are often unceremoniously and unnecessarily "
  "killed', and finds Ekwensi acting as 'both the plaintiff and jury', while still holding it of major "
  "importance for its picture of Lagos. Contemporary Black Biography notes that the criticism of its episodic "
  "form followed his reputation thereafter. Iduma, in 2020, explains its neglect beside Achebe by its "
  "'undisguisedly didactic and moralizing character' and reads it as Lagos noir.",
  chars="Amusa Sango; Aina; Elina; Beatrice the Second; Bayo",
  canon="Major canon",
  biblio="London: Andrew Dakers, 1954 (Contemporary Authors; Wikipedia). Revised edition, Heinemann African "
  "Writers Series no. 5, 1963 (series list); Evanston: Northwestern University Press, 1967; revised edition, "
  "New York: Fawcett, 1969 (Contemporary Authors); New York Review Books Classics, 2020, with an introduction "
  "by Emmanuel Iduma. Serialised in the Daily Times, Lagos, before book publication (Contemporary Black "
  "Biography); working title Lajide of Lagos (Gale).",
  notes="Not read. Sources differ on the time the writing took (ten days in Contemporary Black Biography, "
  "fourteen in Gale's Contextual Encyclopedia) and on where it was written (on the voyage, or while studying "
  "in London, as Wikipedia's article says). The friend's name, Bayo, comes from Arthur Smith's essay, seen as "
  "a search extract; names of other characters found only in reader summaries are not used. The ending beyond "
  "the marriage was not checked.",
  ver="partially verified", sources=[IDUMA, GCE, CBB, CA, EWB, WIKI_BOOKS, SMITH, LIT, AWS]),

W10("The Drummer Boy", CE, "1960", "Novella for young readers", "minor",
  genres=G("Novella", "Juvenile Fiction"),
  themes=T("Art, the artist and the creative life", "Class, labour and social mobility"),
  movements=M(AFR),
  comp=("1947", "1949"),
  overview="A novella for young readers published by Cambridge University Press in 1960, based, according to "
  "Wikipedia, on the life of the Nigerian street musician Benjamin 'Kokoro' Aderounmu.",
  content="The wandering, homeless and poverty-stricken life of a street musician, in Wikipedia's "
  "description.",
  summary="Wikipedia, citing a 2009 report in the Nigerian Compass, describes the book as a perceptive and "
  "powerful account of the wandering, homeless and poverty-stricken life of a street artist, modelled on "
  "Kokoro. The Encyclopedia of World Biography counts it, with The Passport of Mallam Ilia, among 'exercises in "
  "blending traditional themes with undisguised romanticism'. The names of its characters and the course of "
  "the story were not found in the sources consulted.",
  themes_text="Poverty, homelessness and the life of a wandering artist, treated with the romanticism the "
  "Encyclopedia of World Biography notes.",
  structure="A short novella published as a supplementary school reader; its chapter structure was not "
  "examined.",
  style="Written for young readers; Contemporary Authors notes that his novellas were used chiefly as "
  "supplementary readers in schools.",
  ctx="One of the children's manuscripts that Ekwensi read aloud to his pupils at Igbobi College in the late "
  "1940s (Contemporary Black Biography), published in the year of Nigerian independence alongside The "
  "Passport of Mallam Ilia.",
  sig="A minor book, recorded because it is one of his earliest works for children and because of its link "
  "with a real Lagos musician.",
  canon="Minor canon",
  biblio="Cambridge: Cambridge University Press, 1960 (Contemporary Authors; Contemporary Black Biography); "
  "Wikipedia cites ISBN 978-0-521-04882-8.",
  notes="Not seen. The composition dates are inferred from Contemporary Black Biography's statement that he "
  "read the manuscript to his Igbobi classes, where Contemporary Authors dates his teaching to 1947-1949.",
  ver="partially verified", sources=[WIKI_CE, CBB, EWB, CA]),

W10("The Passport of Mallam Ilia", CE, "1960", "Novella", "minor",
  genres=G("Novella", "Historical Adventure"),
  themes=T(VIOLENCE, LOVE),
  movements=M(AFR),
  comp=("1948", "1948"),
  overview="A novella of love and revenge set in Northern Nigeria, written in 1948 and published by Cambridge "
  "University Press in 1960; it became a school reader in Nigeria and the basis of an animated film announced "
  "in 2019.",
  content="Mallam Ilia spends most of his life seeking vengeance on Mallam Usman (or Usuman) for the death of "
  "his wife, Zarah.",
  summary="According to a 2019 report in Vanguard, the story takes place mainly in Kano in colonial Northern "
  "Nigeria and follows a fiery young warrior, Ilia, who spends the rest of his life seeking vengeance for the "
  "death of his wife, Zarah, at the hands of Mallam Usman; the paper calls it a story of love, loss and "
  "revenge. A 2025 report on the same film adaptation also sets it in colonial Kano. The meaning of the "
  "passport in the title and the manner of the final reckoning were not described in the sources consulted.",
  themes_text="Vengeance pursued over a lifetime and what it costs the avenger; love and loss; the social "
  "world of colonial Kano.",
  structure="A short novella that Ekwensi first read in manuscript to his Igbobi pupils (Contemporary Black "
  "Biography); its internal division was not examined.",
  style="Romantic adventure for young readers, which the Encyclopedia of World Biography counts among his "
  "blends of traditional themes and romanticism.",
  ctx="Written in 1948 (Wikipedia; Vanguard) and published twelve years later by Cambridge University Press, "
  "in the same year as The Drummer Boy; Wikipedia cites a reprint of 2023.",
  sig="Vanguard's report quotes the view that it was one of the most widely read young-adult novels of the "
  "late 1990s in Nigeria; Magic Carpet Studios of Lagos announced an animated feature in 2019 and showed a first "
  "look in 2025.",
  canon="Minor canon",
  biblio="Cambridge: Cambridge University Press, 1960 (Contemporary Authors; Contemporary Black Biography, as "
  "Passport of Mallam Ilia). Written 1948 (Wikipedia).",
  notes="Not seen. The plot outline comes from news reports of the film adaptation, seen as search extracts; "
  "fuller summaries in reader reviews were not used.",
  ver="partially verified", sources=[VANGUARD, WIKI_CE, CA, CBB, EWB]),

W10("Jagua Nana", CE, "1961", "Novel", "major",
  genres=G("Social Novel", "Political Novel", "Naturalist Fiction"),
  themes=T(CITY, GENDER, DECOL, POWER, LAND),
  movements=M(AFR),
  overview="Ekwensi's best-known novel, published in London by Hutchinson in 1961, a year after Nigerian "
  "independence: the affairs and adventures of Jagua, an ageing Igbo courtesan of the Tropicana club in "
  "Lagos, set against the party politics of the last colonial decade, and her return to her home village of "
  "Ogabu. Donald Cosentino calls it 'the best realized novel' to come out of the tradition of Onitsha market "
  "literature and Ekwensi's widely acknowledged masterpiece. It was published in the United States by Fawcett "
  "in 1969 and in Heinemann's African Writers Series (no. 146) in 1975, and Ekwensi later wrote a sequel, "
  "Jagua Nana's Daughter.",
  content="Jagua, forty-five, earns her living at the Tropicana and pays for her young lover Freddie Namme, a "
  "poor teacher, to study law in England, hoping to marry him. While he is away she campaigns for the "
  "politician Uncle Taiwo and settles a chieftaincy dispute in Freddie's home town. Freddie returns, marries "
  "a younger woman and stands against Taiwo; Taiwo's thugs beat him to death, Taiwo and his henchman are "
  "killed in turn, and Jagua goes home to Ogabu, where her newborn child dies and a briefcase of stolen party "
  "money gives her the means to become a merchant princess in Onitsha.",
  summary="Jagua is a forty-five-year-old 'good time girl' whose income comes from men she meets at the "
  "Tropicana, a Lagos bar of businessmen, politicians and hustlers. Her name evokes the Jaguar car: "
  "Contemporary Authors quotes the novel, 'They called her Jagua because of her good looks and stunning "
  "fashions.' Afraid of losing her beauty, she clings to Freddie Namme, a young and poor schoolteacher, and "
  "arranges to send him to England to study law, bribing the right people for his passport, on the "
  "understanding that he will marry her and keep her in old age: 'You mus' go train yousself to be a proper "
  "man.' Freddie, who despises her trade but takes what it pays for, is unfaithful in turn. During his "
  "eighteen months away Jagua throws herself into the arms and the campaigns of Uncle Taiwo, the most "
  "charismatic politician in Lagos, of the party called OP2, and wins over the Lagos market women with her speeches. "
  "Visiting Freddie's home town of Bagana, she ends a long chieftaincy dispute that threatened war with a "
  "neighbouring village and has a brief affair with its chief, Ofubara; a visit to Onitsha shows her that she "
  "lacks the capital to set up as a cloth merchant, the life that her brother Fonso, a merchant prince, holds "
  "out to her. Freddie comes back from England, marries a younger woman and stands against Taiwo for the "
  "Lagos City Council. Taiwo's thugs beat him to death, the outcry costs Taiwo the election, and Taiwo, his "
  "henchman Dennis Odoma (another of Jagua's lovers) and Dennis's girlfriend Sabrina are killed in the "
  "violence that follows. Fonso arrives with the news that their father is dying, and Jagua leaves Lagos for "
  "Ogabu. There, nearly fifty, she conceives a child by an anonymous lover near the river shrine of the "
  "fertility deity; the baby dies a few days after its birth. Then she opens the briefcase Taiwo left with "
  "her on the night of his defeat, finds thousands of pounds stolen from the party treasury, and resolves: "
  "'I goin' to Onitsha. I wan' to become proper merchant princess.' (Plot after Cosentino, World Literature "
  "and Its Times, with page references to the Panther edition.)",
  themes_text="Money and the city: Cosentino shows that money arbitrates everything in Ekwensi's Lagos, from "
  "love to politics, and the murders that end the Lagos chapters read as a judgement on the high life. "
  "Women's independence: Jagua's choice lies between the Tropicana and the life of the Onitsha merchant "
  "princesses, 'independent women' in Fonso's words, and Cosentino reads her return east as a "
  "transformation from harlot to heroine. Politics before independence: Uncle Taiwo's party has no programme "
  "beyond money, thuggery and patronage, which Gale counts among the first fictional exposures of political "
  "corruption in Nigeria. Village and city: Ogabu is drawn as a paradise set aside rather than lost, and "
  "Cosentino argues that Jagua's return anticipates the flight of the Igbo from Lagos to their villages in "
  "1966-1967. The Encyclopedia of World Biography adds that her life personalises the conflict between "
  "traditional and modern urban Africa.",
  structure="About two-thirds of the novel follow Jagua's picaresque adventures in Lagos, broken by journeys "
  "east to Bagana and Onitsha; an accelerating series of murders closes the Lagos action, and the last "
  "chapters, in Ogabu, bring loss and a final reversal of fortune (Cosentino). The Encyclopedia of World "
  "Biography finds the plot much more cohesive than that of People of the City, because it is centred on a "
  "single heroine.",
  style="Dialogue moves between Pidgin, broken English and standard Nigerian English, sometimes within one "
  "paragraph, which Ekwensi defended as part of the African writer's effort to 'Africanise the English "
  "language' (quoted by Cosentino from Larson). Descriptions of Jagua's body and clothes borrow, Cosentino "
  "shows, the visual language of advertising in Drum magazine, giving the book a cinematic surface; J. O. J. "
  "Nwachukwu-Agbada called it a 'Rabelaisian jeu d'esprit' (Contemporary Authors).",
  ctx="Published in 1961, the year Ekwensi became federal director of information, and set in the decade "
  "before independence, when the three regional parties competed for the posts left by departing British "
  "officials and Igbo migrants crowded into Lagos (Cosentino). Its heroine descends from the Onitsha "
  "pamphlets' stock figure of the 'Highlife queen', whom Cosentino had studied in Ba Shiru. Church groups and "
  "women's organisations attacked the novel, some schools banned it, and Parliament refused an Italian "
  "studio's request to film it in Nigeria (Contemporary Authors; Gale).",
  sig="Ekwensi's most successful and most widely read novel, which, Gale says, many consider his most "
  "lasting contribution to the art of the African novel, and which, Cosentino says, has held the Nigerian imagination "
  "as no other fictional character has, down to the bumper sticker 'I Love Jagua Nana and her Daughter too'. "
  "It is the book through which the Onitsha market heroine entered the London novel, and an early fiction of "
  "political corruption in Nigeria. The campaign against it and the parliamentary debates over the proposed "
  "Italian film made it a test case for frank sexual writing in West Africa. Wikipedia notes comparisons "
  "with Dickens's moral view of the city and with Zola's Nana, and criticism in the 1980s of its stereotyped "
  "women.",
  crit="The first British reviews were favourable: the Times Literary Supplement called it 'a very good novel "
  "indeed' and one of the first authoritative pictures of the 'High-life' of the towns, and Bernard Bergonzi, "
  "in The Spectator, thought 'the West African novel is growing up fast' (Cosentino). African academic "
  "critics were divided. Eustace Palmer found no consistent moral attitude and judged it a failure 'by any "
  "standards'; Chinweizu, Jemie and Madubuike answered him by invoking Shakespeare's refusal to moralise. "
  "Robert July thought the return to the village the weakest part of the book, while Austin Shelton read it "
  "as an 'ontological recoil' from the Westernised city. Later studies include Cosentino's 'Jagua Nana: "
  "Culture Heroine' (1977) and Loretta Hawkins's 'The Free Spirit of Ekwensi's Jagua Nana' (African "
  "Literature Today, 1979).",
  chars="Jagua Nana; Freddie Namme; Uncle Taiwo; Fonso; Chief Ofubara; Dennis Odoma; Sabrina",
  canon="Major canon",
  biblio="London: Hutchinson, 1961 (Contemporary Authors); London: Panther, 1963 (the edition Cosentino "
  "cites); New York: Fawcett, 1969 (Contemporary Authors); Heinemann African Writers Series no. 146, 1975 "
  "(series list; Wikipedia).",
  notes="Not read. The plot follows Cosentino's summary. Contemporary Authors differs in placing Freddie's "
  "affair with a younger woman before he leaves for England and in having Jagua flee Lagos; Contemporary "
  "Black Biography says she is allowed happiness after suffering; Wikipedia says she gives birth to a son but "
  "does not mention his death, which the Igbo Studies Review also records. Iduma says the novel won the Dag "
  "Hammarskjold Prize; Gale's entries record the prize as Ekwensi's (1969) and Wikipedia under 1968, without "
  "naming the book.",
  ver="partially verified", sources=[LIT, CA, CBB, EWB, GCE, WIKI_BOOKS, IDUMA, ISR, AWS]),

W10("Burning Grass", CE, "1962", "Novel", "significant",
  genres=G("Regional Fiction", "Adventure Fiction"),
  themes=T(LAND, MYTH, FAMILY),
  movements=M(AFR),
  overview="A novel of the Fulani cattle-herders of Northern Nigeria, published by Heinemann in 1962 as the "
  "second title of the African Writers Series and the first novel written for the series. Its wandering "
  "hero, Mai Sunsaye, is driven by a spell of wanderlust across the grasslands while his family tries to "
  "bring him home.",
  content="Mai Sunsaye, head of the Sunsaye family and chief of Dokan Toro, frees a slave girl, Fatimeh, sets "
  "off a run of misfortunes and falls under a rival's spell, the sokugo or wandering sickness; his "
  "adventures and his sons' searches lead through deserted and resettled villages to a reunion at Dokan Toro "
  "and his death.",
  summary="Mai Sunsaye, a Fulani cattleman, head of his household and chief of the settlement of Dokan Toro, "
  "rescues a slave girl, Fatimeh, from the servant of a rough man named Shehu. Her arrival brings misfortune "
  "and leads his wife Shaitu to think her unlucky: the youngest son, Rikku, falls in love with her, but his "
  "brother Hodio runs away with her. At the same time Ardo, Mai Sunsaye's rival for the chieftaincy, casts on "
  "him the sokugo, a charm bound to the leg of a Senegal dove, the 'wandering sickness' that 'turned studious "
  "men into wanderers, that led husbands to desert their wives, Chiefs their people, and sane men their "
  "reason'. Driven across the country, Mai Sunsaye meets his eldest son Jalla; Baba, an old man who refuses "
  "to leave the deserted village of Old Chanka, evacuated by the colonial authorities because of the tsetse "
  "fly; and Ligu, a legendary herdswoman known as 'the champion cattle-herder'. Rikku is helped by a Kanuri "
  "woman, Kantuma, who dies near the end. At the close most of the family is reunited at Dokan Toro, and Mai "
  "Sunsaye dies from the strain of his adventures (Wikipedia).",
  themes_text="The pastoral life of the Mbororo Fulani, their values and their attachment to the grasslands, "
  "which Francis Nyamnjoh (cited by Wikipedia) finds convincingly rendered by an outsider; the pull of "
  "wandering against settled duty, embodied in the sokugo; family loyalty in the search for the lost father; "
  "rivalry for a chief's power; and the colonial state's intrusion on the herders' world through "
  "resettlement.",
  structure="A picaresque sequence of episodes, which the Encyclopedia of World Biography calls basically a "
  "collection of vignettes; the narrative moves between the wandering father and the members of his family "
  "who follow him.",
  style="Margaret Laurence found in it 'many of the qualities of the traditional African tales, magical "
  "occurrences, mysterious and seductive women, acts of phenomenal heroism, swift-paced adventure'; Umar "
  "Abdurrahman notes that the arid landscape is central to its characterisation (both cited by Wikipedia).",
  ctx="Accounts of its origin differ. Wikipedia, after Abdurrahman, says it rests on a short visit recorded in "
  "'Three Weeks among the Fulani' (Nigeria Magazine, October 1960); Contemporary Black Biography speaks of "
  "several months spent with the nomadic Fulani, and the Encyclopedia of World Biography of a real family he "
  "had lived with. Heinemann cut the manuscript from 80,000 to 40,000 words.",
  sig="With Survive the Peace, one of the two novels that Gale and Contemporary Authors single out as "
  "exceptions to his city fiction, and regarded by Contemporary Black Biography as one of his more serious "
  "books. Heinemann expected a school readership, but the first printing of 2,500 sold out quickly; the book "
  "has been reprinted many times, translated into German as Der Wanderzauber (Bejjit, cited by Wikipedia) "
  "and reissued by East African Educational Publishers in 1998.",
  chars="Mai Sunsaye; Shaitu; Jalla; Hodio; Rikku; Leibe; Fatimeh; Ardo; Shehu; Ligu; Kantuma; Baba",
  canon="Secondary canon",
  biblio="London: Heinemann, 1962, African Writers Series no. 2, as Burning Grass: A Story of the Fulani of "
  "Northern Nigeria (series list; Contemporary Authors); Nairobi: East African Educational Publishers, 1998. "
  "The Encyclopedia of World Biography, Gale's Contextual Encyclopedia and Wikipedia's article on Ekwensi date "
  "it 1961.",
  notes="Not read. The plot follows Wikipedia's article, which carries an 'all plot' warning; the reference "
  "entries confirm the hero, the sokugo and the Fulani setting.",
  ver="partially verified", sources=[WIKI_BOOKS, CBB, EWB, CA, GCE, AWS]),

W10("An African Night's Entertainment", CE, "1962", "Folk tale (novella)", "minor",
  genres=G("Novella", "Retelling and Adaptation"),
  themes=T(VIOLENCE, MYTH, LOVE),
  movements=M(AFR),
  overview="A tale of vengeance set in Northern Nigeria and told by an old storyteller, published as folklore "
  "by African Universities Press in Lagos in 1962 and revised in 1986.",
  content="Abu Bakir's long revenge on the merchant who married the girl betrothed to him, carried out through "
  "a charm worked on the merchant's son.",
  summary="Narrated by an old storyteller, the tale follows Abu Bakir, whose betrothed, Zainobe, the love of "
  "his life, is married instead to Mallam Shehu, a wealthy merchant in need of a child. When they have a son, "
  "Kyauta, Abu swears vengeance and roams from town to town, losing an eye and an ear, to gather what he needs "
  "for a charm that will make the boy worthless. The charm turns Kyauta into a violent thug who kills his own "
  "father; later, when its power has worn off, Kyauta kills Abu (Wikipedia).",
  themes_text="Desire, vengeance and child marriage, the themes Wikipedia lists, together with the cost of "
  "revenge to the avenger.",
  structure="A frame narrative in which an old storyteller tells the tale, as the title's night of "
  "entertainment suggests; the book runs to about 96 pages.",
  style="Folk-tale narration for young readers; Contemporary Authors classes it as folklore among his juvenile "
  "works, and The Writers Directory gives the subtitle A Tale of Vengeance.",
  ctx="Ekwensi was accused of plagiarising the Hausa novel Jikin Magayi (1934) by Rupert East and John Tafida "
  "Umaru; he answered that his book retold a folktale an old Hausa mallam had told him (Wikipedia).",
  sig="A minor work, notable for the dispute over its relation to Jikin Magayi and for its long life as a "
  "school text: it was revised in 1986 and published in London by John Murray in 1996.",
  chars="Abu Bakir; Zainobe; Mallam Shehu; Kyauta",
  canon="Minor canon",
  biblio="Lagos: African Universities Press, 1962; revised edition, 1986 (Contemporary Authors); London: John "
  "Murray, 1996 (Wikipedia). Wikipedia's article on Ekwensi also lists the title under 1948, which no other "
  "source supports.",
  notes="Not seen. The plot follows Wikipedia's article, a stub that cites the 1996 edition.",
  ver="partially verified", sources=[WIKI_BOOKS, CA, WD, WIKI_CE]),

W10("Beautiful Feathers", CE, "1963", "Novel", "significant",
  genres=G("Political Novel", "Domestic Fiction"),
  themes=T(FAMILY, DECOL, CITY),
  movements=M(AFR),
  overview="A novel of Lagos in the first years of independence, published by Hutchinson in London in 1963 "
  "and in the African Writers Series (no. 84) in 1971: the public success and private failure of Wilson "
  "Iyari, a pharmacist who leads the Nigerian Movement for African and Malagasy Solidarity.",
  content="Wilson Iyari is respected by the crowds and by African leaders, but his wife Yaniya disregards "
  "him at home and finally deserts him, while his movement and his pharmacy suffer; the novel follows both "
  "crises until Yaniya comes to sit beside him in public on the movement's last day.",
  summary="The title comes from an Ibo proverb printed on the jacket: 'However famous a man is outside, if he "
  "is not respected inside his own home he is like a bird with beautiful feathers, wonderful on the outside "
  "but ordinary within.' Wilson Iyari, thirty, the light-skinned son of a Calabar father and a Fulani mother, "
  "runs the Independence Pharmacy in a Lagos suburb and has lately become leader of the Nigerian Movement for "
  "African and Malagasy Solidarity (NMFAMS) after a crisis in its ranks. Strangers greet him in the street "
  "and his patients' respect comforts him, but at home 'he was nothing'. His wife Yaniya, a glamorous "
  "nineteen-year-old from Benin when he married her, feels neglected; she disregards him and then deserts "
  "him, taking refuge with the children Jomo and Pandhit in a forest village near Benin, where his image "
  "changes in her mind to that of 'the man who had been wronged'. Meanwhile his cause and his business "
  "suffer. The publisher's description says that Wilson does not come to terms with himself 'until he "
  "discovers that unity is a complex of the judicious and proper, the overlooked and forgotten, the "
  "tolerated and rejected'; in chapter 19 Yaniya cancels a flight in order to sit beside him in public on "
  "the last day of the NMFAMS.",
  themes_text="Public reputation against private authority, the proverb's subject; Pan-African unity, which "
  "Gale sees as the hope of the first optimistic years of independence, tested against the disunity of a "
  "marriage; the neglected wife's grievances, which the novel presents from her side as well as his; and the "
  "bustle and disorder of suburban Lagos, from the quarrelsome bole-kaja buses to the schoolgirls who come to "
  "the pharmacy.",
  structure="Third-person narration in numbered chapters, mostly following Wilson but moving to Yaniya during "
  "her flight (chapter 11); the publisher's description frames the story as a test of the proverb.",
  style="Brisk, comic and observant in the opening chapter: the improvised bus stop of the bole-kaja drivers, "
  "the heavily made-up schoolgirl, the waiting patients. John Povey, reviewing it in Critique, saw in its "
  "professionalism 'a new and perhaps important phenomenon in African writing' (Contemporary Authors).",
  ctx="Published in 1963, when Ekwensi was director of information in Lagos, and dedicated to Leopold Sedar "
  "Senghor 'of Negritude Fame' and to Sir Abubakar Tafawa Balewa, the federal prime minister, as patron of "
  "the Society of Nigerian Authors. Its movement for African and Malagasy solidarity places it in the "
  "Pan-African politics of the years after independence.",
  sig="The novel in Gale's chronological sequence of his Lagos fiction that reflects 'the first optimistic "
  "years of independence with its concern for Pan-Africanism'; the Encyclopedia of World Biography names it "
  "and Iska as the most important novels he published between 1961 and 1966. Its subject, a public man undone "
  "at home, carries his city fiction from the underworld of Jagua Nana to the new professional and political "
  "elite.",
  chars="Wilson Iyari; Yaniya; Chini Moka; Jomo; Pandhit",
  canon="Secondary canon",
  biblio="London: Hutchinson, 1963 (Contemporary Authors; Wikipedia); Heinemann African Writers Series no. 84, "
  "1971, 'first published London: Hutchinson, 1963' (series list). The Igbo Studies Review cites a Heinemann "
  "printing of 1966.",
  notes="Partly read: the front matter and the opening of chapter 1 in the African Writers Series text; "
  "passages of chapters 3, 4, 5, 11, 16 and 19 only in search extracts. Yaniya's refuge, the village of 'Ol' "
  "Man Forest, Emorwen' near Benin, is named in the Igbo Studies Review. The ending beyond Yaniya's "
  "appearance at Wilson's side was not seen.",
  ver="partially verified", sources=[BF_TEXT, GCE, CA, EWB, ISR, AWS, WIKI_CE]),

W10("Iska", CE, "1966", "Novel", "significant",
  genres=G("Social Novel", "Political Novel"),
  themes=T(CITY, GENDER, NATION, VIOLENCE),
  movements=M(AFR),
  overview="A novel published by Hutchinson in London in 1966, the year of the two coups, that follows Filia, "
  "a young Igbo woman raised in Northern Nigeria, from Kaduna to Lagos; Gale says that it exposed the ethnic "
  "divisions that erupted in the civil war. Its title is the Hausa word for wind (general knowledge), and "
  "Virginia Ola calls Filia 'a true child of the wind'.",
  content="Filia, convent-educated and the daughter of an Igbo family in Kaduna, marries a Northerner, Dan "
  "Kaybi, against his family's wishes; after his death in an ethnic brawl she goes to Lagos, seeks a career "
  "as a model, drifts through relationships and a stay with a prayer sect, and dies young.",
  summary="Filia grows up in Kaduna in a protected home and a convent. She marries Dan Kaybi, a Northerner, "
  "against stiff opposition from his father, in a courtship carried on by letter (Ola). Dan Kaybi, quick to "
  "violence, dies after intervening in a brawl between Hausa and Igbo men in his favourite bar (Hannerz); her "
  "brother has already been killed in a riot, and her father, embittered, has returned to the village and "
  "died (Ola). Filia tries the family's home village and rejects a mature Igbo suitor there, then goes to "
  "Lagos to stay with her elder sister and brother-in-law, hoping to become a model (Hannerz). Lagos brings "
  "parties, job-seeking, fast cars and cannabis; after an illness she finds some peace among the Prayer "
  "People of the preacher Piska Dabra, who later wades into the lagoon and drowns (Ola; Hannerz). She grows "
  "close to Dapo Ladele, a political correspondent of the West African Sensation whose British wife has gone "
  "home. But Dapo writes in praise of his new patron, the corrupt suitor she had rejected, now a "
  "parliamentarian in Lagos who pursues her again, and she is deeply disappointed in him. She thinks of "
  "modelling abroad, but dies young, with her mother beside her, in what Ola calls a mysterious death; "
  "Hannerz says she is 'gone with the wind'.",
  themes_text="Ethnic hatred as the sickness of the nation: Ola reads Ekwensi's central concern as the "
  "'destructive and divisive tribalism which inevitably led to the Nigerian Civil War', anchored in Filia's "
  "marriage across the line between North and East; the city's glamour as a cover for pain, seen in the "
  "troubled congregation of the Prayer People; a search for peace and happiness through fashion, love and "
  "religion that ends in the discovery of corruption even in religion; and the journalist's compromise with "
  "power in Dapo Ladele.",
  structure="Divided into sections named after four characters who shape Filia's life, among them Dan Kaybi, "
  "Remi and Piska Dabra (Ola); the riot in which her brother died is told in flashback.",
  style="Ola finds the riot passages restrained, avoiding 'over statement and over description', and compares "
  "Dan Kaybi with Achebe's Okonkwo as a man prone to violence who dies by it; the Lagos chapters use the "
  "vocabulary of fashion and nightlife familiar from Jagua Nana.",
  ctx="Published in 1966, the year of the coups and of the killings of Igbo in the North that preceded the "
  "civil war; Gale says that the novel forecast the war. It was his last novel before the war; the next, "
  "Survive the Peace, appeared ten years later.",
  sig="Gale places it fourth in the sequence of his Lagos novels, the book that exposes 'the tribal and "
  "factional divisions and animosities that finally erupted in the Nigerian civil war'; the Encyclopedia of "
  "World Biography counts it, with Beautiful Feathers, among his most important works of the 1960s. "
  "Contemporary Black Biography notes that it never rivalled Jagua Nana in popularity; Spectrum Books of "
  "Ibadan reissued it in 1981.",
  chars="Filia; Dan Kaybi; Dapo Ladele; Piska Dabra; Remi; Gadson Salifas",
  canon="Secondary canon",
  biblio="London: Hutchinson, 1966; Ibadan: Spectrum Books, 1981 (Contemporary Authors; Contemporary Black "
  "Biography). Hannerz mentions a paperback of 1968.",
  notes="Not read. Sources differ on whether Dan Kaybi was Filia's husband (Contemporary Black Biography, Ola) "
  "or her fiancé (Hannerz). The summary combines extracts from Ola's and Hannerz's essays, seen only in search "
  "results; Gadson Salifas is named by Ola without his part being clear.",
  ver="partially verified", sources=[ISKA_X, CBB, GCE, CA, EWB]),

W10("Lokotown and Other Stories", CE, "1966", "Short-story collection", "minor",
  genres=G("Short-Story Collection"),
  themes=T(CITY, FAMILY),
  movements=M(AFR),
  overview="A collection of nine stories of city life, published by Heinemann in 1966 as no. 19 of the African "
  "Writers Series.",
  content="The nine stories are 'Lokotown', 'A Stranger from Lagos', 'The Ivory Dancer', 'Timber Money', "
  "'Under the Almond Tree', 'Coin-Diver', 'Spider's Web', 'Fashion Girl' and 'Glittering City' (library "
  "catalogue contents).",
  summary="Wikipedia describes the stories as looking at Nigerian city life and showing its excitement and "
  "dissolution, and the guide to African literature by Zell, Bundy and Coulon, quoted in a bookseller's "
  "catalogue, as short stories of urban life. In the title story, according to an essay in the Igbo Studies "
  "Review, Nwuke and his wife lose their child, and he sends his grieving wife home to her mother. The other "
  "eight stories were not described in the sources consulted.",
  themes_text="The excitement and dissolution of city life, in Wikipedia's words; in 'Lokotown', grief and "
  "the village as refuge from the city.",
  structure="Nine stories, opening with the title story and ending with 'Glittering City' (catalogue "
  "contents).",
  style="Short popular stories in the episodic manner of his novels; the prose itself was not seen.",
  ctx="Published in the same year as Iska; the Encyclopedia of World Biography names it, with The Rainmaker "
  "(1965), as one of the two important story collections among the works he published each year from 1961 to "
  "1966.",
  sig="The first of his story collections in the African Writers Series; the second, Restless City and "
  "Christmas Gold, followed as no. 172 in 1975.",
  canon="Minor canon",
  biblio="London: Heinemann, 1966, African Writers Series no. 19 (series list; Contemporary Authors); "
  "reprinted 1981 (library catalogue).",
  notes="Not seen. The contents come from a library catalogue record seen as a search extract, which "
  "misspells two titles ('Locotown', 'Spider's wed').",
  ver="partially verified", sources=[LOKO_CAT, WIKI_BOOKS, ISR, CA, EWB, AWS]),

W10("Survive the Peace", CE, "1976", "Novel", "significant",
  genres=G("War Novel", "Social Novel"),
  themes=T(WAR, "Memory, trauma and testimony", FAMILY),
  movements=M(AFR),
  overview="A novel of the first months after the Nigerian civil war, published by Heinemann in 1976 as no. "
  "185 of the African Writers Series: a Biafran radio journalist, James Odugo, tries to gather his scattered "
  "family and rebuild his life, and is killed by armed robbers.",
  content="James Odugo, who left his family to follow Biafra Radio, sets out at the war's end to reunite his "
  "family and to find his place in a reunited Nigeria; amid shortages, banditry, refugees and relief work he "
  "faces the lessons of defeat, and he is killed on the road by armed robbers.",
  summary="James Okonkwo Odugo, a radio journalist on the Biafran side, has left his family and parents to "
  "work for Biafra Radio wherever it is located. When the war ends he sets about returning to normal family "
  "life, but his wife Juliette has gone off to the city, leaving their three children in Ogene village, and "
  "he faces what a reviewer in The International Fiction Review calls the 'ugly revelations and lessons of "
  "defeat' and the brazen immorality of wartime: he knows that he has fought 'on the losing side of the "
  "no-victors, no-vanquished civil war'. He has himself had affairs, with the radio announcer Vic Ezenta, "
  "with Benne and with Gladys Nwike. Contemporary Black Biography describes his journey through violence, "
  "destruction, refugees and relief operations, with flashbacks to the war. He is killed by armed robbers, "
  "and Gladys gives birth to his child soon afterwards; for the reviewer, the robbers 'make an irony of his "
  "efforts to survive in peace time'.",
  themes_text="The cost of peace after civil war: refugees, scattered families and the fragility of peace, "
  "the subjects Gale says the novel brought to timely attention; defeat and the moral disorder war leaves "
  "behind; the journalist as witness; and the irony of the title, since James survives the war only to die "
  "in the peace. Peter Nazareth's essay 'Survive the Peace: Cyprian Ekwensi as a Political Novelist' (in "
  "Marxism and African Literature, edited by Georg M. Gugelberger, 1986) treats it as political fiction.",
  structure="A picaresque journey narrative, in Contemporary Black Biography's term, that begins at the end of "
  "the war and reaches back to it in flashbacks; with Burning Grass it is one of the two novels Gale names as "
  "not set in Lagos.",
  style="Realistic, documentary narration drawn from Ekwensi's own experience of Biafran radio; the reviewer "
  "found 'more fact than fiction' in it and judged that its incidents were given little imaginative "
  "treatment.",
  ctx="Written from Ekwensi's experience as chair of Biafra's Bureau for External Publicity and director of "
  "its radio service (1967-1970), and published six years after the war ended in January 1970.",
  sig="The last novel in the chronological sequence of his fiction that Gale traces, from late colonial Lagos "
  "to the end of the war. With Divided We Stand it is one of his two novels of the civil war, and the "
  "reviewer in The International Fiction Review set its documentary realism against Kole Omotoso's "
  "allegorical war novel The Combat.",
  chars="James Odugo; Juliette; Vic Ezenta; Gladys Nwike; Benne",
  canon="Secondary canon",
  biblio="London: Heinemann, 1976, African Writers Series no. 185 (series list; Contemporary Authors; "
  "Contemporary Black Biography).",
  notes="Not read. Contemporary Authors spells the hero's name Oduga; the review spells it Odugo. The summary "
  "rests on the review, seen only in search extracts, and on the reference entries.",
  ver="partially verified", sources=[IFR, CA, CBB, GCE, AWS]),

W10("Divided We Stand", CE, "1980", "Novel", "minor",
  genres=G("War Novel", "Political Novel"),
  themes=T(WAR, NATION, POWER),
  movements=M(AFR),
  overview="A novel of the Nigerian civil war, subtitled A Novel of the Nigerian Civil War, written during the "
  "war and published by Fourth Dimension Publishers in Enugu in 1980.",
  content="The war seen through Chika, a correspondent, intellectual and nationalist, and its effect on the "
  "people of the East, according to the critical accounts seen.",
  summary="Gale's Contextual Encyclopedia calls it one of the first fictional documentaries of the war and "
  "its aftermath. An essay on Nigerian war fiction, reprinted by the Free Online Library, says that it "
  "follows individual rather than collective heroism, centred on Chika, a correspondent of courage and "
  "forthrightness and a nationalist at heart, who wants to expose the forces in Nigerian society behind the "
  "war and holds that 'the real enemies are the politicians who robbed the country blind'. Arthur Smith "
  "writes that it reverses the received idea that unity is strength, showing how ethnicity, division and "
  "hatred bring about distrust, displacement and war itself.",
  themes_text="Ethnic division as the cause of war, in an ironic reversal of the slogan 'united we stand'; "
  "the responsibility of politicians; individual courage amid communal disaster.",
  structure="A full-length novel; its narrative organisation was not examined, and the sources describe its "
  "content only in outline.",
  style="Documentary realism, in Gale's description of it as a fictional documentary of the war.",
  ctx="Written in the heat of the war (Smith) but published only in 1980; Contemporary Black Biography says "
  "that in the 1980s Ekwensi drew on manuscripts from his 'archive' for this and other novels.",
  sig="With Survive the Peace, one of Ekwensi's two novels of the civil war, written while he was serving "
  "Biafra's information service.",
  canon="Minor canon",
  biblio="Enugu: Fourth Dimension Publishers, 1980 (Contemporary Authors; Wikipedia, which gives the "
  "subtitle). Gale's Contextual Encyclopedia dates it 1981.",
  notes="Not read. The protagonist's name and role come from a single essay seen as a search extract.",
  ver="partially verified", sources=[GCE, WARLIT, SMITH, CA, CBB, WIKI_CE]),

W10("Jagua Nana's Daughter", CE, "1986", "Novel", "minor",
  genres=G("Social Novel"),
  themes=T(FAMILY, GENDER, MIGR),
  movements=M(AFR),
  overview="The sequel to Jagua Nana, published by Spectrum Books in Ibadan (1986 or 1987): the search of "
  "Jagua's daughter Lizza for her mother, and of Jagua for her daughter.",
  content="Lizza, born of Jagua's teenage affair and raised in Jagua's home town, searches for her mother, "
  "who has been told that Lizza died; the 'dual search' widens into an account of border clashes and migrant "
  "labour.",
  summary="In Ernest Emenyonu's account (Concise Dictionary of World Literary Biography, quoted in "
  "Contemporary Authors), Lizza is the child of an illicit union of Jagua's teenage years, raised in Jagua's "
  "home town while her mother pursued her life in Lagos. When Jagua returns at the end of the events of Jagua "
  "Nana to look for her, 'she is led to believe that Lizza has since died'; later events reveal that Lizza "
  "is alive and prosperous. Emenyonu calls the book 'the story of a dual search—daughter for mother, and "
  "mother for daughter', which 'later develops into a moving account of international border clashes and "
  "migrant labor'.",
  themes_text="Mother and daughter, separation and search; sexual frankness in a more permissive Nigeria; "
  "migrant labour and conflict at the borders.",
  structure="A search narrative with two seekers, in Emenyonu's description; the book's organisation was not "
  "examined.",
  style="J. O. J. Nwachukwu-Agbada (World Literature Today, quoted in Contemporary Authors) found its "
  "bawdiness undiminished twenty-five years after Jagua Nana, though it caused less outrage.",
  ctx="Published in the last years of the oil boom, when, Cosentino says, it caused 'a cultural mania' and "
  "inspired the bumper sticker 'I Love Jagua Nana and her Daughter too'; Contemporary Black Biography says "
  "that it reworked earlier material from Ekwensi's archive.",
  sig="Ekwensi's one sequel, which kept Jagua's name alive in Nigerian popular culture.",
  chars="Lizza; Jagua Nana",
  canon="Minor canon",
  biblio="Ibadan: Spectrum Books, 1986 (Contemporary Black Biography; Cosentino) or 1987 (Contemporary "
  "Authors; the Encyclopedia of World Biography); Gale's Contextual Encyclopedia gives 1993, and Wikipedia "
  "lists both 1987 and 1993.",
  notes="Not seen. Recorded under 1986, the date given by the two sources that name the publisher's year "
  "without qualification.",
  ver="partially verified", sources=[CA, LIT, CBB, EWB, GCE, WIKI_CE]),

W10("For a Roll of Parchment", CE, "1986", "Novel", "minor",
  genres=G("Autobiographical Novel", "Social Novel"),
  themes=T("Race, racism and the struggle for civil rights", MIGR, "Education, institutions and the academy"),
  movements=M(AFR),
  overview="A novel based on Ekwensi's years as a pharmacy student in London in the 1950s, published by "
  "Heinemann (1986 or 1987), about a Nigerian student of law who meets humiliation and colour prejudice in "
  "Britain.",
  content="A young Nigerian goes to England for a law degree and suffers mental torture, disorientation, "
  "unrequited love and racial degradation, in Emenyonu's summary.",
  summary="According to Contemporary Authors, the novel draws on Ekwensi's own experience as a pharmacy "
  "student in London in the 1950s, though its protagonist seeks a law degree. Emenyonu writes that 'the plot "
  "tells of mental torture, disorientation, unrequited love, and the degradation to which the hero is "
  "subjected in the British social and political environment because of his skin color', and calls the book "
  "'a revealing imaginative documentary of race relations and color prejudice in England during the 1950s'. "
  "Contemporary Black Biography says that it recounts the voyage from Nigeria to England.",
  themes_text="Race and colour prejudice in 1950s Britain; the African student's isolation and humiliation; "
  "the pursuit of a qualification, the 'roll of parchment' of the title.",
  structure="A narrative of departure and life abroad; its organisation was not examined.",
  style="Nwachukwu-Agbada found 'considerable artistic development, particularly in language and descriptive "
  "power', and called Ekwensi the 'Nigerian Defoe' (World Literature Today, quoted in Contemporary Authors); "
  "Emenyonu notes its pathos, candour and acrimonious undertones.",
  ctx="One of the novels that Contemporary Black Biography says Ekwensi made from older manuscripts after he "
  "turned to full-time writing in 1984; Gale calls it one of the earliest exposés of the indignities suffered "
  "by African students in England.",
  sig="A late work that returns to the London of Ekwensi's student years; Gale counts it among the topical "
  "subjects that sustained his popularity.",
  canon="Minor canon",
  biblio="Ibadan: Heinemann Educational Books, 1986 (Wikipedia, citing Open Library; Contemporary Black "
  "Biography); Contemporary Authors gives Heinemann, London, 1987.",
  notes="Not seen. Recorded under 1986, the date of the Ibadan edition in the catalogue record Wikipedia "
  "cites.",
  ver="partially verified", sources=[CA, CBB, GCE, WIKI_CE]),

W10("King Forever!", CE, "1992", "Children's story (parable)", "minor",
  genres=G("Children's Fiction"),
  themes=T(POWER, VIOLENCE),
  movements=M(AFR),
  alt=["King for Ever!"],
  overview="A parable for young readers about tyranny, published by Heinemann Educational Books in 1992, "
  "which Emenyonu calls 'a well-crafted parable on the nature and fate of military dictators and "
  "self-proclaimed absolute rulers for life'.",
  content="Sinanda seizes power from a legitimate king and, to keep it, kills almost everyone he once loved, "
  "but is deposed and killed in turn.",
  summary="In Emenyonu's account, quoted by Contemporary Authors, the tale centres on Sinanda, a man who "
  "wrests power from a legitimate king but is in turn deposed and killed, despite killing almost everyone he "
  "once loved in his effort to hold on to the throne. Emenyonu reads it as a parable on military dictators "
  "and on rulers who proclaim themselves absolute for life.",
  themes_text="Usurpation, tyranny and its self-destruction, within the moral education (truth, integrity, "
  "justice) that Emenyonu finds in Ekwensi's later books for children.",
  structure="A short parable of rise and fall; its organisation was not examined.",
  style="Written for young readers in the manner of what Emenyonu calls a 'grandfather-artist' concerned with "
  "shaping the future of his readers.",
  ctx="Published in 1992, during military rule in Nigeria, as one of his late books for Heinemann, with "
  "Gone to Mecca (1991), Masquerade Time (1992) and The Red Flag (1993).",
  sig="A minor book, singled out by Emenyonu among Ekwensi's works for children.",
  canon="Minor canon",
  biblio="London: Heinemann Educational Books, 1992 (Contemporary Authors, as King Forever!; Emenyonu's title "
  "is King for Ever!). The Writers Directory and the Encyclopedia of World Biography also list it under 1992.",
  notes="Not seen. Only Emenyonu's description, quoted by Contemporary Authors, was found.",
  ver="partially verified", sources=[CA, WD, EWB]),
]
