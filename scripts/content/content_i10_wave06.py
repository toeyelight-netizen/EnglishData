"""Installment 10, wave 06: Amos Tutuola's 1946-2000 bibliography (Nigerian fiction in English).

The first author of installment 10 from outside the British and American traditions.
All eleven books (1952-1990) are recorded. They were checked against the Wikipedia articles
on Tutuola, The Palm-Wine Drinkard and My Life in the Bush of Ghosts; Encyclopaedia
Britannica; four Gale reference entries compiled on Encyclopedia.com (Contemporary Black
Biography, the Gale Contextual Encyclopedia of World Literature, the Encyclopedia of World
Biography and Contemporary Literary Criticism, the last including part of Chris Dunton's
2006 essay on the unpublished plays); ISFDB's bibliography and two of its contents listings;
and Faber's descriptions of four reissues, used only for plot outlines.

Sources disagree on the date of Simbi (1955 or 1956), on that of The Witch-Herbalist
(1981 or 1980), on the length of the narrator's stay in the Bush of Ghosts (twenty-four or
twenty years) and on the number of stories in The Village Witch Doctor (twelve or eighteen).
Each record states the disagreement. Every work is linked to "African Literature in
English", whose taxonomy entry dates the movement from The Palm-Wine Drinkard (1952). No
other movement is assigned: the magical-realism label that Wikipedia's categories give the
first novel is not supported by the sources consulted.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ  # noqa: E402

WIKI_AT = "Amos Tutuola (Wikipedia)"
BRIT = "Amos Tutuola (Encyclopaedia Britannica)"
CBB = "Amos Tutuola (Encyclopedia.com, compiling Gale's Contemporary Black Biography)"
GCE = "Amos Tutuola (Encyclopedia.com, compiling the Gale Contextual Encyclopedia of World Literature)"
EWB = "Amos Tutuola (Encyclopedia.com, compiling the Encyclopedia of World Biography)"
CLC = "Tutuola, Amos 1920-1997 (Encyclopedia.com, compiling Gale's Contemporary Literary Criticism)"
WIKI_PWD = "The Palm-Wine Drinkard (Wikipedia)"
WIKI_BUSH = "My Life in the Bush of Ghosts (novel) (Wikipedia)"
ISFDB = "Summary Bibliography: Amos Tutuola (ISFDB)"
ISFDB_YF = "Publication: Yoruba Folktales (ISFDB record 411186)"
ISFDB_VWD = "Publication: The Village Witch Doctor & Other Stories (ISFDB record 409845)"
FAB_HUN = "The Brave African Huntress (Faber and Faber product page)"
FAB_AJA = "Ajaiyi and His Inherited Poverty (Faber and Faber product page)"
FAB_FEA = "Feather Woman of the Jungle (Faber and Faber product page)"
FAB_PAU = "Pauper, Brawler and Slanderer (Faber and Faber product page)"
AT = "Amos Tutuola"
AFR = "African Literature in English"
MYTH = "Myth, folklore and the supernatural"

AUTHORS = [
A10(AT, MAJ, "1920", "1997", "Abeokuta, Nigeria",
  "Nigerian; Yoruba (Egba) novelist and short-story writer writing in English",
  "Novelist and storyteller whose The Palm-Wine Drinkard (1952) was the first Nigerian book to win international fame; author of eleven books (1952-1990) that rework Yoruba folktales as quest romances in an idiosyncratic West African English.",
  "Amos Olatubosun Tutuola was born on 20 June 1920 at or near Abeokuta, in the Egba country of Yorubaland, then under British rule; Wikipedia names the village of Wasinmi, Gale's Contemporary Black Biography the Ipose-Ake quarter of Abeokuta. His parents, Charles and Esther Tutuola, were Yoruba Christian cocoa farmers. He had about six years of schooling, including the Salvation Army primary school and the Anglican Central School in Abeokuta, which ended when his father died in 1939. He then trained as a smith and worked as a blacksmith (some accounts say coppersmith) for the Royal Air Force in Nigeria during the Second World War (1942-45 in Wikipedia, 1943-45 in the Gale entries). After failing to set up his own smithy, he became a messenger in the Department of Labour in Lagos in 1948, having married Victoria Alake in 1947. In the idle hours of that job he began writing English versions of Yoruba tales. His first manuscript, The Wild Hunter in the Bush of the Ghosts, was sent to the London photographic publisher Focal Press in the late 1940s and not printed until 1982. The Palm-Wine Drinkard, passed to Faber and Faber by the United Society for Christian Literature, appeared in London in 1952 and New York in 1953. From 1956 he worked as a storekeeper for the Nigerian Broadcasting Corporation in Ibadan. He was a founding member of the Mbari Club, a visiting research fellow at the University of Ife in 1979 and an associate of the International Writing Program at the University of Iowa in 1983. In retirement he lived between Ibadan and Ago-Odo. He died at Ibadan on 8 June 1997, of hypertension and diabetes. His papers are held by the Harry Ransom Center at the University of Texas at Austin.",
  "Tutuola's books retell and recombine Yoruba folktales as long episodic quests: a naive, idle or headstrong hero or heroine travels into the bush of spirits, survives monsters and captivities by cunning, magic or a protector's help, and comes home changed. Eight novels, an early manuscript published late (Contemporary Black Biography counts nine 'epic novels' in all), a school collection of traditional tales and a final book of stories make up the published output. He also wrote short stories for periodicals and anthologies and unpublished plays reworking the same material.",
  "First-person oral narration in the early books (Simbi, 1955, is the first in the third person), in an English shaped by Yoruba syntax and idiom, with coinages, irregular grammar and spelling, and objects of modern life set in a world of spirits. Episodes are loosely linked, and Tutuola himself declined to call his books novels. The register changes in Yoruba Folktales (1986), written for schools in standard English.",
  "Journeys to the land of the dead and the bush of ghosts; death, famine and poverty, including poverty inherited and apparently permanent; greed, betrayal and trickery; the testing and education of a weak or disobedient protagonist; parents who fail or are lost; the preservation and performance of Yoruba oral tradition.",
  "Tutuola was the first Nigerian writer to achieve international recognition. The reception of The Palm-Wine Drinkard became a test case for African writing in English: acclaim in Britain and the United States, hostility among educated Nigerians who thought its language and spirits shamed the country on the eve of independence, and later reassessment of his work as a creative transmission of oral tradition into print. The taxonomy of this database dates African literature in English from his first book.",
  bib_status="substantially complete",
  bib_note="Bibliography status, 1946-2000: substantially complete. All eleven books are recorded as works: The Palm-Wine Drinkard (1952), My Life in the Bush of Ghosts (1954), Simbi and the Satyr of the Dark Jungle (1955), The Brave African Huntress (1958), Feather Woman of the Jungle (1962), Ajaiyi and His Inherited Poverty (1967), The Witch-Herbalist of the Remote Town (1981), The Wild Hunter in the Bush of the Ghosts (written in the late 1940s, published 1982), Yoruba Folktales (1986), Pauper, Brawler and Slanderer (1987) and The Village Witch Doctor and Other Stories (1990). The list agrees across Wikipedia, Britannica (which omits The Wild Hunter), Gale's Contemporary Black Biography and ISFDB. Not recorded separately: short stories that ISFDB lists with years of first appearance in periodicals and anthologies. They are 'The Strange Fellows' Palm-Wine Tapster' and 'Tort and the Dancing Market-Women' (1952), 'My First Wedding Day in the Bush of Ghosts' (1954), 'The Elephant Woman' (1956; revised in Yoruba Folktales), 'Ajaiyi and the Witch Doctor' (1959), 'Ajantala, the Noxious Guest' and 'Don't Pay Bad for Bad' (1960), 'The Duckling Brothers and Their Disobedient Sister' (1961), 'The Town of Famine' (1962, from Feather Woman of the Jungle), 'Remember the Day After Tomorrow' (1969), 'Akanke and the Jealous Pawnbroker' (1974) and 'Tort's Bitter Marriage' (1984). Four of them were collected in The Village Witch Doctor; their first venues and texts were not consulted. Also not recorded: the unpublished plays Ajaiyi and the Witch Doctor, The Pupils of the Eyes and The Sword of Vengeance, known from Chris Dunton's study of the manuscripts at the Harry Ransom Center; a 1958 drama titled The Palm-Wine Drinkard listed by Gale's Contemporary Literary Criticism and not identified further; the radio tale 'Dola with her Colanut Tree' (BBC West Africa Service, 1954); and the posthumous collection Don't Pay Bad for Bad (2012), outside the period. Unresolved dates: Simbi (1955; 1956 in two Gale entries) and The Witch-Herbalist (1981; 1980 in the Encyclopedia of World Biography).",
  ver="verified", sources=[WIKI_AT, BRIT, CBB, GCE, EWB, CLC, ISFDB],
  infl=["D. O. Fagunwa", "John Bunyan"], alt=["Amos Olatubosun Tutuola"]),
]

WORKS = [
W10("The Palm-Wine Drinkard and His Dead Palm-Wine Tapster in the Deads' Town", AT, "1952", "Novel", "major",
  genres=G("Fantasy", "Mythological Retelling"),
  themes=T(MYTH, "Death, illness and mourning"),
  movements=M(AFR),
  overview="Amos Tutuola's first published book is a short novel of 125 pages, issued by Faber and Faber in London in 1952 and by Grove Press in New York in 1953. Told in the first person in an unconventional English shaped by Yoruba idiom, it is a quest tale assembled from Yoruba folktales: a drinker whose palm-wine tapster has died follows him to the town of the dead and comes home again. Britannica calls it the first Nigerian book to achieve international fame. Wikipedia describes it as the first African novel in English published outside Africa.",
  content="A continuous first-person narrative without numbered chapters, made of a chain of adventures. It opens with the narrator's life of drinking and his tapster's fatal fall from a palm tree, then follows his tests by an old man who is a god, including the capture of Death in a net. Next come the rescue of a town head's daughter from the Complete Gentleman in the forest, and the birth of the monstrous child Zurrjir and how the narrator deals with him. A long journey with his wife through bush and towns of spirits includes the Red Fish. After a stay in the Deads' Town and the gift of a magic egg, he returns home to a famine caused by a quarrel between Heaven and Land.",
  summary="The narrator, son of a rich man, is a drinker of palm wine whose father has hired an expert tapster to keep him supplied. When the tapster falls from a palm tree and dies, the supply stops, and no other tapster can match him. The narrator, who calls himself the 'Father of gods who could do anything in this world', sets out with his magical powers to find where the dead man has gone.\n\nSeven months after leaving home he meets an old man, in fact a god, who promises to tell him where the tapster is if he will perform a task: to bring Death from his house in a net. The narrator does so, in the episode anthologised as 'How I Brought Death into the World', and the terrified old man runs away without keeping his promise. Five months later another town head offers the same information if the narrator will rescue his daughter, who has followed a handsome stranger from the market into the forest. The stranger is the Complete Gentleman: a skull who had hired his limbs and body from their owners and returns each part on the way home until only a humming skull is left. The narrator rescues the girl and marries her, but her father withholds the information until the narrator has dealt with Zurrjir, the child she bears, who terrorises the town. Only then is he told that the tapster lives in the Deads' Town.\n\nHusband and wife travel together through forests and towns of spirits, some hostile and some hospitable, helping each other through trial after trial. Among them is the Red Fish, a monster with thirty horns and many eyes that open and shut 'as if a man was pressing a switch on and off'. In the Deads' Town they find the tapster, who is unable to leave it. He gives the narrator an egg that will provide whatever its owner asks for.\n\nAt home the narrator finds a famine: Heaven and Land have quarrelled, and Heaven is withholding rain. For a time the egg feeds his town and the country around with food and palm wine. Then the crowds break it in their excitement and turn on him when it can produce nothing more. He glues the egg together and uses it to punish them. Finally he settles the quarrel between Heaven and Land with a ritual, and the drought ends.",
  themes_text="The book is a journey to the land of the dead and back. Its hero goes in search of the one man who made his idle life possible and returns having to act for the whole community. Critics read the journey in different ways. Britannica sees a quest in which a lazy drinker gains wisdom and confronts death. Gale's Contemporary Literary Criticism describes the pattern common to Tutuola's books, a weak character transformed by a spiritual journey. E. N. Obiechina (1968) stressed the narrator's magical power, which defies even fate, unlike the helpless victims of Kafka. Death becomes a person who can be netted and led home, and the dead keep a town with its own rules. In the last episodes an inexhaustible gift is destroyed by the greed and carelessness of the people it feeds, and a quarrel between Heaven and Land has to be settled by ritual. These episodes add ingratitude and communal responsibility to the folktale material.",
  structure="An episodic quest. Departure, journey and return frame a chain of largely self-contained adventures, each built on a folktale motif and linked mainly by the narrator and his count of the months. Bernth Lindfors compared its episodes to the boxes of a freight train, 'independent units coupled with a minimum of apparatus'. Gale's Contextual Encyclopedia notes that Simbi (1955) was Tutuola's first book to use numbered chapters.",
  style="First-person storytelling in an English that Dylan Thomas called 'young English' and others called pidgin or broken English. Yoruba syntax and idiom are carried into English, adjectives serve as verbs ('I would jealous him more than that'), and words are coined or spelled anew. Modern things appear among the spirits, as in the Red Fish's switch-like eyes. Raymond Queneau's French translation, L'Ivrogne dans la brousse (1953), deliberately kept something of this irregularity.",
  ctx="Tutuola wrote the book as a messenger in the Labour Department in Lagos, after Focal Press had received but not published his first manuscript. Answering an advertisement, he sent it to the United Society for Christian Literature, which passed it to Faber and Faber. It appeared in 1952, near the end of colonial rule, while Nigerian nationalists were pressing for self-government. The Gale entries connect the hostility of educated Nigerians to that moment, when they were anxious about how Africa was seen abroad. Its material comes from Yoruba oral tradition and the Yoruba-language fantasies of D. O. Fagunwa. Bunyan's Pilgrim's Progress and the Arabian Nights, read at school, are possible models for the extended quest.",
  sig="The book made Tutuola the first Nigerian writer with an international reputation. It also opened the controversy that shaped the early reception of African writing in English: should an African author write standard English for foreign readers, or could the language and forms of oral tradition be carried into print? Its later standing depends on the second answer. Wikipedia counts it among the most important texts of the African literary canon. It has been translated into many languages (eleven in Britannica, fifteen in one Gale entry). E. K. Ogunmola's Yoruba folk-opera version (1963) was performed with great success across Nigeria. It appears on Time's list of the 100 best fantasy books (2020) and the BBC's Big Jubilee Read (2022).",
  crit="Dylan Thomas's review, 'Blithe Spirits' (The Observer, 6 July 1952), called it a 'brief, thronged, grisly and bewitching story' and set the tone for its British reception. V. S. Pritchett praised it in the New Statesman. Kingsley Amis, in The Spectator, found an 'unfathomable African myth' with a 'unique grotesque humour'. American reviewers treated Tutuola as a 'primitive', among them Selden Rodman (New York Times Book Review, 1953) and Anthony West (The New Yorker, 1953). Educated Nigerians objected that its English and its spirits gave foreigners a backward picture of Africa. Some Yoruba readers called it a copy of Fagunwa. Tutuola openly admitted the debt, and the Gale Contextual Encyclopedia explains it by the norms of oral storytelling. Reassessments by E. N. Obiechina (1968), Taban lo Liyong (1968), Omolara Ogundipe-Leslie (1970) and Wole Soyinka (1963) defended its imaginative unity and its fidelity to oral performance. Bernth Lindfors collected the reviews and criticism in Critical Perspectives on Amos Tutuola (1975), and Steven M. Tobias (1999) has read its anti-realism as a critique of colonialism.",
  chars="The narrator, the palm-wine drinkard ('Father of gods who could do anything in this world'); his dead palm-wine tapster; an old man who is a god; Death; the Complete Gentleman; a town head's daughter, who becomes the narrator's wife; Zurrjir, their child; the Red Fish",
  canon="Major canon", alt=["The Palm-Wine Drinkard", "The Palm-Wine Drinkard and His Dead Palm-Wine Tapster in the Dead's Town"],
  biblio="First edition: Faber and Faber, London, 1952 (125 pages). First US edition: Grove Press, New York, 1953. French translation by Raymond Queneau, L'Ivrogne dans la brousse (Paris, 1953); Italian translation, Il bevitore di vino di palma (1954, per ISFDB). Published with My Life in the Bush of Ghosts in one volume by Grove Press, 1994; Faber reissue, 2014.",
  notes="Unresolved: the form of the title ('Deads' Town' in Britannica and three Gale entries, 'Dead's Town' in Wikipedia's lead and Gale's Contemporary Literary Criticism); the number of translations (eleven, more than a dozen, fifteen); and whether the book is a novel at all, since Tutuola wrote in 1978 that he could not call his books novels. Gale's Contemporary Literary Criticism lists a 1958 drama called The Palm-Wine Drinkard that is not identified further. Faber's present-day author note says T. S. Eliot acquired the book; this was not corroborated and is not used. The newspaper reviews are cited from Wikipedia and the Gale entries and were not consulted.",
  ver="verified", sources=[WIKI_PWD, WIKI_AT, BRIT, CBB, GCE, EWB, CLC, ISFDB]),

W10("My Life in the Bush of Ghosts", AT, "1954", "Novel", "significant",
  genres=G("Fantasy", "Supernatural Fiction", "Mythological Retelling"),
  themes=T(MYTH, "Childhood, adolescence and coming of age", "Family, marriage and domestic life"),
  movements=M(AFR),
  overview="Tutuola's second book is a novel of 174 pages, published in 1954 by Faber and Faber in London and Grove Press in New York. Its unnamed narrator recalls how, as a small boy, he strayed into the Bush of Ghosts, the realm of the spirits. He spent twenty-four years wandering through its towns before he found his way home.",
  content="A first-person account in related episodes that do not always keep to chronological order. A small boy flees during a war and enters the Bush of Ghosts. He passes through its many towns, with their rulers, ceremonies and courts, undergoing trials and transformations, and marries in the bush. He stays with his dead cousin in the Tenth Town of Ghosts. A goddess sends him back to the human world, and the book closes with a moral on hatred.",
  summary="The narrator is seven years old when war and slave raiding reach his home. His stepmothers have mistreated him and his elder brother and abandon them, and the boys flee from the slave traders. Too young to understand the dangers the bush holds for mortals, the narrator runs in terror into the Bush of Ghosts. He spends twenty-four years there, in a spirit world that Bernth Lindfors describes as 'replete with towns, kings, civic ceremonies, festivals, law courts, and even his cousin's Methodist church'. Passing from one ghost town to the next, he undergoes trials and transformations, marries in the bush, and has experiences 'both harrowing and happy'. In the Tenth Town of Ghosts he finds his dead cousin and thinks of settling there for good. He cannot bring himself to do it, because he longs for his earthly home. At last a 'television-handed' goddess offers him a way back to an ordinary life with his mother and brother, and he accepts. The book ends with the narrator's reflection on hatred, the force that drove him out.",
  themes_text="Lindfors, quoted in Contemporary Black Biography, reads the book less as a quest than as an extended initiation rite. The Bush of Ghosts is at once a terrifying underworld and a mirror of human society, with kings, courts and even a church. The boy's long apprenticeship there begins with his stepmothers' cruelty and ends with his return to his mother, which makes the book a story of growing up. Its closing moral on hatred, noted by Gale's Contemporary Literary Criticism, ties the supernatural ordeal back to the jealousy inside his family.",
  structure="A retrospective first-person narrative of related episodes, not always in chronological order. The narrator reckons his progress through the bush town by town, up to the Tenth Town of Ghosts, and like The Palm-Wine Drinkard the book has no numbered chapters.",
  style="A naive young narrator tells his adventures in Tutuola's Yoruba-inflected English. Traditional spirit lore is mixed with the furniture of modern life, a Methodist church and a goddess with a television for a hand. The Gale Contextual Encyclopedia treats this mixture as Tutuola's characteristic way of updating ancestral tales.",
  ctx="Published two years after The Palm-Wine Drinkard by the same London and New York houses, it appeared while Tutuola was still a messenger in Lagos and while educated Nigerians were still attacking his first book. The slave raids that open the story have drawn scholarly attention, notably in Thomas Jay Lynn's essay on slavery's disruption in the novel (2016).",
  sig="With The Palm-Wine Drinkard it is one of the two books on which Tutuola's reputation chiefly rests. The two won second-place awards in a literary contest in Turin in 1985 and were reissued together by Grove Press in 1994. Time named it among the 100 best fantasy books (2020), and David Byrne and Brian Eno took its title for their album of 1981. Achille Mbembe's essay on life, sovereignty and terror in Tutuola's fiction (2003) is among later studies that return to it.",
  crit="Lindfors, in the Dictionary of Literary Biography, stressed the mixture of the harrowing and the happy in the narrator's twenty-four years. Gale's Contemporary Literary Criticism gives its closing lesson on hatred as an instance of Tutuola's folktale endings. Peter Kalliney (2013) has examined it among Tutuola's books in a study of his relationship with Faber and Faber.",
  chars="The unnamed narrator, a boy of seven at the start; his elder brother; his stepmothers; his mother; his dead cousin in the Tenth Town of Ghosts; the television-handed goddess",
  canon="Secondary canon",
  biblio="First published 1954 by Faber and Faber, London, and Grove Press, New York (174 pages). Italian translation, La mia vita nel bosco degli spiriti (1954, per ISFDB). An episode appeared separately as 'My First Wedding Day in the Bush of Ghosts' (1954, per ISFDB). Reissued with The Palm-Wine Drinkard by Grove Press, 1994.",
  notes="Sources differ on how the boy comes to the bush. Wikipedia and Britannica say he flees slave traders with his elder brother; the Gale entries say his stepmothers abuse and abandon him during a war. The summary combines the two. They also differ on the length of his stay: twenty-four years in Contemporary Black Biography and the Gale Contextual Encyclopedia, twenty in Contemporary Literary Criticism. The Gale Contextual Encyclopedia puts the television-handed goddess in this book in its plot summary but in The Palm-Wine Drinkard in a later paragraph; two Gale plot summaries place the goddess who sends the boy home here. Contemporary Black Biography lists the first edition as Grove, 1954, with a Faber reprint in 1978; Wikipedia shows a 1954 Faber first edition. Wikipedia records a 1984 Premio Grinzane Cavour nomination; Gale gives a second-place award in Turin in 1985.",
  ver="verified", sources=[WIKI_BUSH, WIKI_AT, BRIT, CBB, GCE, CLC, ISFDB]),

W10("Simbi and the Satyr of the Dark Jungle", AT, "1955", "Novel", "minor",
  genres=G("Fantasy", "Mythological Retelling"),
  themes=T(MYTH, "Childhood, adolescence and coming of age"),
  movements=M(AFR),
  overview="Tutuola's third book, published by Faber and Faber in London in 1955, and his first with a heroine. Simbi, a rich and pampered only child, leaves home against her parents' wishes to learn what poverty and punishment are.",
  content="A third-person quest narrative in numbered chapters. It follows Simbi from her parents' house through slavery and a long series of ordeals, in places such as the Town of the Multi-Coloured People and the Dark Jungle of the Satyr, and back to her village.",
  summary="Curious about how others live, Simbi resolves to experience the poverty and punishment she has never known, and leaves home in spite of her parents' warnings. In Bernth Lindfors's list she is 'kidnapped, sold into slavery, beaten, starved, almost beheaded, set afloat on a river in a sealed coffin, carried off by an eagle, imprisoned in a tree trunk, half-swallowed by a boa constrictor, attacked by a satyr, shrunk and put in a bottle, bombarded by a stone-carrying phoenix, and petrified into a rock'. She comes through by her wits and her voice, singing to summon the dead to her aid. When she reaches home she rests, then goes out to warn her playmates to heed their parents.",
  themes_text="A cautionary tale of disobedience told from the side of a resourceful heroine. Suffering sought out of curiosity becomes a real education, and the ending turns her experience into a lesson for other children.",
  structure="The Gale Contextual Encyclopedia notes that this was Tutuola's first book divided into numbered chapters and his first told in the third person. It takes both as signs of his wider reading and growing sense of himself as an author.",
  style="Tutuola's Yoruba-inflected English in third-person narration. Song is the heroine's means of calling on the dead for help.",
  ctx="Written in his spare time while Tutuola was still a Labour Department messenger, and published three years after The Palm-Wine Drinkard, when he was famous abroad and still under attack from educated Nigerian critics.",
  sig="The book marks the formal change, to chapters and third-person narration, that the Gale entries read as evidence of Tutuola's literary self-consciousness. It is also the first of his books with a female hero, a line continued in The Brave African Huntress.",
  chars="Simbi; her parents; the Satyr of the Dark Jungle",
  canon="Minor canon",
  biblio="First edition: Faber and Faber, London, 1955. US edition: City Lights Books, San Francisco, 1988 (cited by Wikipedia). Faber reissue, 2014.",
  notes="Dated 1955 by Wikipedia, Britannica, Contemporary Black Biography (Faber, 1955), the Gale Contextual Encyclopedia and ISFDB, and 1956 by the Encyclopedia of World Biography and Gale's Contemporary Literary Criticism; 1955 is recorded. The plot is taken from Lindfors's account as quoted in Contemporary Black Biography and from Gale's Contemporary Literary Criticism; the novel itself was not read.",
  ver="verified", sources=[CBB, GCE, CLC, BRIT, WIKI_AT, EWB, ISFDB]),

W10("The Brave African Huntress", AT, "1958", "Novel", "minor",
  genres=G("Fantasy", "Adventure Fiction"),
  themes=T(MYTH, "Family, marriage and domestic life"),
  movements=M(AFR),
  overview="Tutuola's fourth book, published in 1958 with illustrations by the Nigerian artist Ben Enwonwu. It is his second with a heroine: Adebisi, a huntress who goes into the Jungle of the Pigmies to rescue her four brothers.",
  content="The story of Adebisi's expedition into the Jungle of the Pigmies, with Ben Enwonwu's illustrations. It covers her victory over a giant, her service as barber to a king, her time in the pigmies' prison and the rescue of her brothers.",
  summary="Adebisi, a huntress, sets out for the Jungle of the Pigmies to rescue her four brothers. On the way she overcomes a giant, serves as barber to a king and suffers the horrors of the pigmies' prison, but she refuses to give up. Using both her strength and her intelligence, she finds a way to free her brothers and returns home to a hero's welcome.",
  themes_text="Adebisi takes the role of the hunter, one of the folktale hero types that the Gale Contextual Encyclopedia identifies in Tutuola's fiction. Loyalty to her family drives her quest, and persistence and intelligence decide its outcome.",
  structure="An outward journey into a hostile jungle and a return, marked by a series of trials (the giant, the king's court, the prison) in Tutuola's usual episodic manner.",
  style="Episodic adventure in Tutuola's Yoruba-inflected English. The first edition was illustrated by the Nigerian artist Ben Enwonwu.",
  ctx="Published in 1958, the year of Chinua Achebe's Things Fall Apart, two years after Tutuola moved to the Nigerian Broadcasting Corporation in Ibadan and two before Nigerian independence. The New York Times reviewed it on 2 November 1958 under the heading 'Adebisi's Odyssey'.",
  sig="With Simbi it forms the pair of Tutuola's books with female heroes. The Gale Contextual Encyclopedia observes that his later books were received less warmly in Britain and America than his first two.",
  chars="Adebisi, the huntress; her four brothers; a giant; a king; the pigmies",
  canon="Minor canon",
  biblio="First published 1958, with illustrations by Ben Enwonwu. Contemporary Black Biography gives Grove Press as publisher; Wikipedia cites a 1958 first edition from a rare-book dealer's listing, not consulted. Faber paperback reissue, 2014.",
  notes="The plot outline comes from Faber's description of the 2014 reissue; the novel was not read. The New York Times review of 2 November 1958 could not be retrieved (HTTP 403). Which of the 1958 London and New York editions came first was not established.",
  ver="partially verified", sources=[FAB_HUN, WIKI_AT, BRIT, CBB, GCE, ISFDB]),

W10("Feather Woman of the Jungle", AT, "1962", "Novel", "minor",
  genres=G("Fantasy", "Mythological Retelling"),
  themes=T(MYTH),
  movements=M(AFR),
  overview="A frame-tale novel published by Faber and Faber in London in 1962. In it an elderly chief entertains the people of his Yoruba village on ten nights with the story of his past adventures.",
  content="Ten nights of storytelling, in which the chief recounts adventures that include his meeting with the Jungle Witch and her ostrich, his visit to the town of the water people and his imprisonment by the Goddess of Diamonds.",
  summary="The people of a Yoruba village gather on ten nights to hear the stories and wisdom of their chief. Night after night he tells them of his adventures, among them his encounter with the Jungle Witch and her ostrich, his visit to the town of the water people and his imprisonment by the Goddess of Diamonds. Each evening the listeners return, eager to learn whether the story will end happily.",
  themes_text="The frame makes storytelling itself a subject. An elder's memories become the village's entertainment and instruction, and the adventures he relates turn on Tutuola's familiar trials of captivity and escape among supernatural beings.",
  structure="A frame narrative which, as the Gale Contextual Encyclopedia notes, is modelled on the Arabian Nights. The chief's tale is divided among ten nights of telling before an audience, a device taken from oral storytelling.",
  style="The Gale Contextual Encyclopedia calls it Tutuola's most stylised work. The chief's first-person tales are set inside the communal occasion of a storytelling performance.",
  ctx="Published in 1962, two years after Nigerian independence. According to the Gale Contextual Encyclopedia, this was the period in which Nigerian critics began to view Tutuola more favourably.",
  sig="Its frame of storyteller and audience makes visible the oral model behind all Tutuola's fiction. ISFDB records an excerpt published separately in 1962 as 'The Town of Famine (Feather Woman of a Jungle)'.",
  chars="The village chief, who tells the story; the Jungle Witch; the Goddess of Diamonds; the villagers who listen",
  canon="Minor canon", alt=["The Feather Woman of the Jungle"],
  biblio="First edition: Faber and Faber, London, 1962. Faber paperback reissue, 2015.",
  notes="Britannica and the Gale Contextual Encyclopedia give the title as The Feather Woman of the Jungle; Wikipedia, ISFDB and Faber's reissue as Feather Woman of the Jungle. The episodes come from Faber's description of the 2015 reissue and the frame from the Gale Contextual Encyclopedia; the novel and its reviews were not read.",
  ver="partially verified", sources=[FAB_FEA, GCE, CBB, BRIT, WIKI_AT, ISFDB]),

W10("Ajaiyi and His Inherited Poverty", AT, "1967", "Novel", "minor",
  genres=G("Fantasy", "Mythological Retelling"),
  themes=T(MYTH, "Class, labour and social mobility"),
  movements=M(AFR),
  overview="Ajaiyi and His Inherited Poverty, published by Faber and Faber in London in 1967, is the story of a man born into the poverty his parents leave him. He travels through supernatural lands in search of a way out of it.",
  content="The death of Ajaiyi's parents and the poverty they leave him; his pawning of his own labour; journeys through unfamiliar lands peopled by strange creatures such as the Spirit of Fire; help from a wizard and a unicorn; and a final reckoning, close to home, with the trickster who has kept the family poor.",
  summary="Ajaiyi is born into poverty, and when his parents die it is all they leave him. Determined to improve his lot, he pawns his labour and then travels through unfamiliar lands full of strange creatures. Among them is the Spirit of Fire, with its huge feathered head and flaming body, and he is helped by a wizard and a unicorn. In the end the answer to his troubles lies near home. Chris Dunton's account of the novel and its stage versions shows that a dishonest witch doctor has caused the family's poverty by trickery, taking the rams offered on the father's grave among other things. Ajaiyi discovers the deception and confronts him, and the story ends with forgiveness and communal reconciliation.",
  themes_text="Poverty as an inheritance that seems permanent is the book's subject. Dunton links its recurrence in Tutuola's work to the loss of his schooling at his father's death, and reads Ajaiyi as the darkest version of his concern with poverty, failing parents and the vulnerable individual. The resolution traces misery to human trickery rather than fate and ends in magnanimity.",
  structure="An episodic quest in Tutuola's usual form, assembled, as Dunton shows, from material written over thirteen years. A five-page story of 1959 supplied two major episodes, and a play, a story of 1960 and an earlier radio tale fed into others.",
  style="Tutuola's Yoruba-inflected English carries both the supernatural journeys and the everyday business of pawnbrokers and debts that frames them.",
  ctx="Published in 1967, the year the Nigerian civil war began, five years after Feather Woman of the Jungle. Fourteen years passed before Tutuola's next book, The Witch-Herbalist of the Remote Town (1981). Dunton notes how little critical attention the novel has received; Harold Collins's Twayne study (1969) could give it only a brief summary.",
  sig="It closes the first phase of Tutuola's career and shows his habit of recycling material across story, play and novel. He later drew on it for an unpublished play, The Sword of Vengeance, and for two pieces in The Village Witch Doctor and Other Stories (1990).",
  chars="Ajaiyi; the dishonest witch doctor; the Spirit of Fire; a wizard; a unicorn",
  canon="Minor canon",
  biblio="First edition: Faber and Faber, London, 1967. Faber paperback reissue, 2015.",
  notes="The witch doctor's role and the rams on the father's grave come from Chris Dunton's 2006 essay on Tutuola's unpublished plays, reprinted in Gale's Contemporary Literary Criticism. Part of that essay was seen only as a search-engine extract of the same page; the novel itself was not read. Dunton names its antecedents: the play and the 1959 story 'Ajaiyi and the Witch Doctor', the play The Pupils of the Eyes, and the story 'Don't Pay Bad for Bad' (1960), first broadcast as 'Dola with her Colanut Tree' by the BBC West Africa Service in 1954.",
  ver="partially verified", sources=[FAB_AJA, CLC, CBB, GCE, BRIT, WIKI_AT, ISFDB]),

W10("The Witch-Herbalist of the Remote Town", AT, "1981", "Novel", "minor",
  genres=G("Fantasy", "Mythological Retelling"),
  themes=T(MYTH, "Family, marriage and domestic life"),
  movements=M(AFR),
  overview="Tutuola's first book in fourteen years, published by Faber and Faber in London in 1981; Contemporary Black Biography counts it as his seventh novel. It tells of a hunter's six-year quest for a cure for his wife's childlessness.",
  content="A hunter's six-year journey through towns and jungles of fantastic beings, among them the Abnormal Squatting Man of the Jungle, to the Remote Town. The witch-herbalist there gives him a medicine, and the book follows what happens at home after he tastes it on the way back.",
  summary="A hunter and his wife cannot have a child. The husband sets out to find a cure, and after six years of bizarre and sometimes frightening encounters, among them the Abnormal Squatting Man of the Jungle, he reaches the Remote Town. There the witch-herbalist gives him a broth for his wife. Famished on the way home, he sips some of it himself. His wife drinks the rest and soon becomes pregnant. So does he, and he must undergo further trials and torments before he is cured.",
  themes_text="The longing for a child drives the quest. The husband's lapse, tasting the medicine meant for his wife, produces the comic reversal of a pregnant man, so that a story of marital devotion becomes a folktale about consequences.",
  structure="A single six-year journey to a distant town and back, with a sequence of encounters on the way and further trials after the homecoming. Tutuola's quest pattern is carried on past its goal.",
  style="Reviewing it in the Times Educational Supplement (26 February 1982), Edward Blishen described its language as 'a mixture of straight translation from Yoruba, and everyday modern Nigerian idiom, and grand epical English'.",
  ctx="Tutuola published it after his term as a visiting writer at the University of Ife in 1979, following a long silence since Ajaiyi (1967). The Gale Contextual Encyclopedia found that the gap had made no discernible difference to his methods.",
  sig="The book showed Tutuola's manner unchanged after fourteen years, and Western reviewers still admired it. Blishen wrote that 'the imagination at work is always astonishing'.",
  chars="The hunter; his wife; the witch-herbalist of the Remote Town; the Abnormal Squatting Man of the Jungle",
  canon="Minor canon",
  biblio="First edition: Faber and Faber, London, 1981. Reissued by Faber.",
  notes="Dated 1981 by Wikipedia, Britannica, Contemporary Black Biography (Faber, 1981), the Gale Contextual Encyclopedia, Gale's Contemporary Literary Criticism and ISFDB, and 1980 by the Encyclopedia of World Biography, as Contemporary Black Biography's narrative also implies; 1981 is recorded. Faber's reissue calls it Tutuola's final novel, although Pauper, Brawler and Slanderer followed in 1987. The novel was not read.",
  ver="verified", sources=[CBB, GCE, BRIT, WIKI_AT, EWB, CLC, ISFDB]),

W10("The Wild Hunter in the Bush of the Ghosts", AT, "1982", "Novel (facsimile of an early manuscript)", "minor",
  genres=G("Fantasy", "Mythological Retelling"),
  themes=T(MYTH),
  movements=M(AFR),
  overview="Tutuola's first book-length manuscript, written in the late 1940s and sent to the London photographic publisher Focal Press. It was published only in 1982, when Three Continents Press issued a facsimile edited by Bernth Lindfors.",
  content="A handwritten narrative of 76 pages, sent with photographic negatives of artists' drawings of the spirits it describes. It is reproduced in facsimile with Lindfors's introduction and postscript; a second edition followed in 1989.",
  summary="As Contemporary Black Biography outlines it, the hero sets out on a perilous epic journey, witnesses many ghastly events, and survives by his own intelligence or, when that fails, by the intervention of a protective spirit. This is the pattern of all Tutuola's later fiction. The Gale Contextual Encyclopedia calls it a mythological adventure story about spirits in the Nigerian bush.",
  themes_text="The themes of the later books are already here: a journey among spirits, survival by wit, and dependence on supernatural protection.",
  structure="A journey narrative of episodes. The Gale Contextual Encyclopedia calls it clearly the work of a novice, and Gale's Contemporary Literary Criticism lists it as short stories.",
  style="A handwritten English narrative illustrated with photographs of artists' drawings of the spirits, the device by which Tutuola hoped to interest a photographic publisher.",
  ctx="Tutuola wrote to Focal Press, a London publisher of photography books, asking whether it would consider a book of Nigerian bush tales with pictures of the spirits. An editor agreed to look, and the manuscript then lay unpublished for more than thirty years.",
  sig="Published thirty years after The Palm-Wine Drinkard, it documents the starting point of Tutuola's career. Nancy J. Schmidt reviewed it in Africa Today (1984) under the title 'The First Shall Be Last: Tutuola's Forgotten Story'.",
  comp=None, canon="Minor canon", alt=["The Wild Hunter in the Bush of Ghosts"],
  biblio="Facsimile of the manuscript, edited with an introduction and a postscript by Bernth Lindfors, Three Continents Press, 1982; second (revised) edition, 1989.",
  notes="Contemporary Black Biography and the Gale Contextual Encyclopedia describe a single narrative; Gale's Contemporary Literary Criticism classes it as short stories. Its composition is dated only to the late 1940s. Its content is known only from these summaries; the facsimile and Schmidt's review were not consulted. The Gale Contextual Encyclopedia spells the title The Wild Hunter in the Bush of Ghosts.",
  ver="partially verified", sources=[CBB, GCE, CLC, WIKI_AT, EWB, ISFDB]),

W10("Yoruba Folktales", AT, "1986", "Folktale collection", "minor",
  genres=G("Folklore Collection", "Children's Fiction"),
  themes=T(MYTH),
  movements=M(AFR),
  overview="A short collection of seven traditional Yoruba tales retold by Tutuola for Nigerian schoolchildren, published by Ibadan University Press in 1986. It was his first book to preserve the communal stories rather than build new fictions from them.",
  content="Seven tales in 57 pages, with interior illustrations by Kola Adesokan and a cover by Bayo Ogundele: 'Ajantala, the Noxious Guest, Is Born', 'Ajantala and the Three Brothers', 'Antere, the Child of the Goddess of the River', 'Too Much of Indulgence', 'The Elephant Woman and the Hunter' (a version of his story 'The Elephant Woman', 1956), 'Segi and the Boa Constrictor' and 'The Shell-Man and the Terror of the Bush'.",
  summary="The Gale Contextual Encyclopedia says the tales keep faithfully to tradition, with an occasional touch of 'zaniness' in character and plot. Going by their titles, two follow Ajantala, the 'noxious guest', from his birth to his dealings with three brothers. The others concern the child of a river goddess, over-indulgence, a hunter and an elephant woman, Segi and a boa constrictor, and the Shell-Man, Tortoise, facing a terror of the bush. In the Segi story a character cries, 'Ah, I am finished today!' (p. 38).",
  themes_text="These are traditional moral tales, presented as communal property to be handed on. Chris Dunton takes the cry 'Ah, I am finished today!' from this book as emblematic of how fragile the individual is in Tutuola's imagined world.",
  structure="Seven separate tales of six to about twelve pages each, arranged as a school reader rather than linked by a frame.",
  style="The Gale Contextual Encyclopedia notes that the grammatical irregularities and stylistic inventions of the earlier books are absent: the book was written for primary-school classrooms, in standard English.",
  ctx="Published in Ibadan, where Tutuola lived, for the Nigerian school market. It is the only one of his books recorded here that was first published in Nigeria.",
  sig="The book marks a shift from reworking folklore into extended fiction to preserving the tales themselves. It also shows Tutuola adapting his English to a school audience.",
  canon="Minor canon",
  biblio="Ibadan University Press, Ibadan, 1986; v + 57 pages; trade paperback, printed on demand (ISFDB). ISBN 978-121-186-5 (978-978-121-186-7); OCLC 16907864.",
  notes="The contents come from ISFDB's listing, whose data is taken from OCLC; the description comes from the Gale Contextual Encyclopedia. The tales themselves were not read, and their subjects are inferred from their titles. The Dunton quotation (p. 38) falls within 'Segi and the Boa Constrictor' (pp. 35-44) by ISFDB's page numbers.",
  ver="partially verified", sources=[ISFDB_YF, GCE, CLC, WIKI_AT, BRIT, ISFDB]),

W10("Pauper, Brawler and Slanderer", AT, "1987", "Novel", "minor",
  genres=G("Fantasy", "Mythological Retelling"),
  themes=T(MYTH),
  movements=M(AFR),
  overview="A late Tutuola romance, published by Faber and Faber in London and Boston in 1987. Its three title characters are forced to set out on journeys of no return.",
  content="The adventures of the three title characters on their journeys, including a ploughing competition for the hand of the beautiful Popondoro and a short-lived reign of Pauper and Slanderer over a town of women.",
  summary="Pauper, Brawler and Slanderer are each forced to set out on a journey from which there is no return, and their travels lead them through incidents and adventures in the manner of Tutuola's earlier romances. Among them is a ploughing competition for the hand of the beautiful Popondoro. Pauper and Slanderer also rule for a while over a town of women, a reign that does not last.",
  themes_text="Faber's description presents the book as drawing on Yoruba folk tradition to reflect on human vagaries. Poverty, quarrelsomeness and slander, embodied in its three heroes, set the adventures in motion.",
  structure="Three protagonists rather than one, whose journeys of no return form an episodic sequence on the pattern of Tutuola's earlier quest romances.",
  style="Folktale idiom in Tutuola's late English; the publisher's description stresses the humour of its episodes.",
  ctx="Published in 1987, six years after The Witch-Herbalist of the Remote Town and a year after Yoruba Folktales. Tutuola was then in his late sixties and living between Ibadan and Ago-Odo.",
  sig="The Encyclopedia of World Biography lists it among the 'similar romances' in which Tutuola kept to his established method. Faber reissued it in 2014 with the rest of his fiction.",
  chars="Pauper; Brawler; Slanderer; Popondoro",
  canon="Minor canon",
  biblio="First edition: Faber and Faber, London and Boston, 1987 (ISBN 0-571-14714-4, per Wikipedia's citation). Faber reissue, 2014.",
  notes="Its content is known only from Faber's description of the 2014 reissue; the book and its reviews were not read, and its ending is not recorded. The Encyclopedia of World Biography gives the title as Pauper, Brawler, Slanderer.",
  ver="partially verified", sources=[FAB_PAU, EWB, CBB, BRIT, WIKI_AT]),

W10("The Village Witch Doctor and Other Stories", AT, "1990", "Short-story collection", "minor",
  genres=G("Short-Story Collection", "Mythological Retelling"),
  themes=T(MYTH),
  movements=M(AFR),
  overview="Tutuola's last book, published by Faber and Faber in London in 1990. It collects short stories based on traditional Yoruba tales, four of them first published in periodicals or anthologies between 1960 and 1974.",
  content="ISFDB lists twelve stories in 90 pages. They are 'The Village Witch Doctor', 'A Short Biography of Tortoise', 'A Short Biography of Yanribo, Tortoise's Wife', 'Ajao and the Active Bone', 'Don't Pay Bad for Bad' (first published 1960), 'Akanke and the Jealous Pawnbroker' (1974), 'Remember the Day After Tomorrow' (1969), 'Ade, the Traitor', 'Rere, the Disobedient Son', 'The Duckling Brothers and Their Disobedient Sister' (1961), 'The Rich Husbandman and his Odd-looking Pawn' and 'The Greedy Tortoise and the Orisa-Oko'.",
  summary="The stories retell Yoruba fables of greed, betrayal and trickery. Three belong to what ISFDB groups as Tutuola's Tortoise stories, about Tortoise and his wife Yanribo. Others concern disobedient children, pawns and pawnbrokers, a traitor and a village witch doctor. According to Chris Dunton, the title story and 'Remember the Day After Tomorrow' rework material from Ajaiyi and His Inherited Poverty. 'Don't Pay Bad for Bad' descends from a tale broadcast by the BBC West Africa Service in 1954.",
  themes_text="Gale's Contemporary Literary Criticism and the Gale Contextual Encyclopedia both name greed, betrayal and tricksterism as the subjects of the collection. The stories of disobedient children carry a cautionary moral like Simbi's.",
  structure="Twelve self-contained tales of six to eleven pages each, closing with a Tortoise story, with no frame.",
  style="Lindfors, in the Dictionary of Literary Biography as quoted by Contemporary Black Biography, found in it 'the same buoyant imagination' and 'fascination with comically grotesque fantasy worlds' as in the first books. Richard Bauerle (World Literature Today, 1991) thought the style still 'fresh'.",
  ctx="Published seven years before Tutuola's death and his final publication, it gathers work from three decades, from stories of the early 1960s to new pieces.",
  sig="As his final book it confirms the continuity of Tutuola's practice over forty years, the reworking of Yoruba tales in his own English, and it gathers in book form stories first scattered in periodicals and anthologies.",
  crit="Richard Bauerle's review in World Literature Today 65.3 (summer 1991), p. 539, called the collection 'illuminating'. Lindfors concluded that Tutuola, 'after more than forty years of writing, remains a very resourceful raconteur'.",
  canon="Minor canon", alt=["The Village Witch Doctor & Other Stories"],
  biblio="First edition: Faber and Faber, London, 1990; 90 pages; paperback, £3.99 (US $7.95); ISBN 0-571-14215-X; cover by Henry Iles (ISFDB). Faber reissue, 2014.",
  notes="ISFDB's contents listing, which lacks a primary verification, gives twelve stories; the Gale Contextual Encyclopedia says eighteen. Not resolved, as the book itself was not consulted.",
  ver="partially verified", sources=[ISFDB_VWD, GCE, CLC, CBB, BRIT, WIKI_AT, ISFDB]),
]
