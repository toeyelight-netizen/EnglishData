"""Installment 10, wave 11: R. K. Narayan's novels and two story collections, 1947-1990.

The first South Asian author of installment 10. Narayan published from 1935 to 1993; his books
of the period run from An Astrologer's Day and Other Stories (1947) and Mr. Sampath (1949) to
Salt and Sawdust (1993). The bibliography was taken from Gale's Contemporary Authors (the fullest
list, with publishers) and checked against Gale's Contextual Encyclopedia of World Literature,
Wikipedia, the Sahitya Akademi list and the Post45 Playboy Fiction Index.

This wave records twelve works: the ten novels from Mr. Sampath (1949) to The World of Nagaraj
(1990) and the two story collections whose title stories Contemporary Authors summarises, An
Astrologer's Day and Other Stories (1947) and A Horse and Two Goats and Other Stories (1970).
The later story collections, the retellings of Indian myth and epic (Gods, Demons, and Others;
The Ramayana; The Mahabharata), the memoir My Days and the travel books and essays are listed
in the bibliography note and are the next wave's work. None of the books was read.

The novel plots follow Wikipedia's articles (two of them flagged, The Painter of Signs as
unreferenced and The Vendor of Sweets as needing citations), checked where possible against
Gale; The Guide is also checked against Paul Brians's study guide and Talkative Man against
Kirkus Reviews. Gale's one-sentence account of The Guide (Raju arriving in Malgudi, dying and
revered as a saint) conflicts with the fuller plot and is reported, not followed. Contemporary
Authors dates the Sahitya Akademi award 1961, the Akademi's list 1960. Every work is linked to
"South Asian Literature in English", whose taxonomy entry names Narayan; no other movement is
assigned.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ  # noqa: E402

CA = "Narayan, R.K. 1906-2001 (Contemporary Authors, via Encyclopedia.com)"
GCE = "Narayan, R. K. (Gale Contextual Encyclopedia of World Literature, via Encyclopedia.com)"
WIKI_RKN = "R. K. Narayan (Wikipedia)"
WIKI_NOVELS = ("Wikipedia articles on Mr. Sampath - The Printer of Malgudi, The Financial Expert, Waiting for "
               "the Mahatma, The Guide, The Man-Eater of Malgudi, The Vendor of Sweets, The Painter of Signs, A "
               "Tiger for Malgudi, Talkative Man and The World of Nagaraj")
BRIANS = ("Paul Brians, R. K. Narayan: The Guide: A Study Guide (Washington State University; Wayback "
          "Machine capture of 17 January 1999)")
KIRKUS = "Review of Talkative Man (Kirkus Reviews, 15 January 1986)"
ENOTES = ("R. K. Narayan criticism: extracts (eNotes; Contemporary Literary Criticism vols. 7 and 28, "
          "including V. S. Naipaul, 'An Old Equilibrium')")
JIWS = ("Singh et al., 'Subdued Voices and Marginalized Lives: Reading R. K. Narayan's Waiting for the "
        "Mahatma ...' (Journal of International Women's Studies, Bridgewater State University)")
MONDAL = "Subarna Mondal, 'R.K. Narayan' (Indian Writing in English, University of Hyderabad)"
SAHITYA = "List of Sahitya Akademi Award winners for English (Wikipedia)"
PLAYBOY = "Playboy Fiction Index (Post45 Data Collective)"

RKN = "R. K. Narayan"
SAL = "South Asian Literature in English"
FAITH = "Faith, doubt and the sacred"
FAMILY = "Family, marriage and domestic life"
LOVE = "Love, intimacy and loss"
ART = "Art, the artist and the creative life"
IDENT = "Identity, authenticity and the divided self"
MEDIA = "Technology, media and consumer society"
GENDER = "Gender, feminism and women's lives"
MYTH = "Myth, folklore and the supernatural"
VIOLENCE = "Violence, crime and justice"
NATURE = "Nature, ecology and environmental crisis"
CLASS = "Class, labour and social mobility"
LANG = "Language, writing and the limits of representation"

AUTHORS = [
A10(RKN, MAJ, "1906", "2001", "Madras, Madras Presidency, British India",
  "Indian; novelist, short-story writer and essayist writing in English, from a Tamil family of Madras, who "
  "lived in Mysore and set almost all his fiction in the imaginary South Indian town of Malgudi",
  "Indian novelist and short-story writer, with Mulk Raj Anand and Raja Rao a leading author of early Indian "
  "writing in English (Wikipedia); his fourteen novels, from Swami and Friends (1935) to The World of Nagaraj "
  "(1990), are almost all set in Malgudi, as are most of his stories, and The Guide (1958) won the first "
  "Sahitya Akademi Award for a book in English.",
  "Rasipuram Krishnaswami Narayanaswami was born in Madras on 10 October 1906 into a Tamil Brahmin family and "
  "spent part of his childhood in the care of his maternal grandmother, Parvati, while his father, a "
  "headmaster, was transferred from school to school (Wikipedia). In 1922 he joined the school in Mysore where "
  "his father was headmaster; he failed the entrance examination twice and took his BA at Maharaja's College, "
  "Mysore, in 1930 (Gale's Contextual Encyclopedia; Contemporary Authors). A brief spell as a schoolteacher "
  "proved distasteful, and he turned to writing: an article on Indian cinema in the Madras Mail (July 1930) was "
  "his first publication, and he later reported from Mysore for the newspaper Justice. Graham Greene, shown "
  "the manuscript by a friend, recommended Swami and Friends, which Hamish Hamilton published in 1935; "
  "Contemporary Authors says he shortened his surname to Narayan that year. He married Rajam in 1934; they had "
  "a daughter, Hema, and Rajam's death in 1939 stopped his writing for a time. He edited the journal Indian "
  "Thought from 1941 and owned Indian Thought Publications in Mysore, which issued many of his books in India. "
  "After The English Teacher (1945) came the novels of the period studied here, from Mr. Sampath (1949) to The "
  "World of Nagaraj (1990), together with stories, essays, travel writing, a memoir and prose versions of the "
  "Ramayana and the Mahabharata; My Dateless Diary records his first visit to the United States, in 1956. His "
  "honours include the Sahitya Akademi Award for The Guide (1960; Contemporary Authors gives 1961), the Padma "
  "Bhushan (1964), the English-Speaking Union Book Award for My Days (1975), the Royal Society of Literature's "
  "Benson Medal (1980), honorary membership of the American Academy and Institute of Arts and Letters (1981 in "
  "Wikipedia, 1982 in Contemporary Authors), the Sahitya Akademi Fellowship (1994) and the Padma Vibhushan "
  "(2000). He sat in the Rajya Sabha as a nominated member from 1986 to 1992. His brother R. K. Laxman, the "
  "cartoonist, illustrated some of his books. He died in Chennai on 13 May 2001; his manuscripts are in the "
  "Mugar Memorial Library at Boston University.",
  "Narayan's books of 1946-2000 comprise ten novels, from Mr. Sampath (1949) to The World of Nagaraj (1990); "
  "story collections from An Astrologer's Day and Other Stories (1947) and Lawley Road (1956) to Malgudi Days "
  "(1982), Under the Banyan Tree (1985), The Grandmother's Tale (1992) and Salt and Sawdust (1993); retellings "
  "of Indian myth in Gods, Demons, and Others (1964) and shortened prose versions of the Ramayana (1972) and "
  "the Mahabharata (1978); travel writing (My Dateless Diary, 1960; The Emerald Route, 1977, which includes the "
  "play The Watchman of the Lake); essays (Next Sunday, 1956; Reluctant Guru, 1974; A Writer's Nightmare, "
  "1988); and the memoir My Days (1974). He also wrote stories for magazines, among them the New Yorker "
  "(Contemporary Authors) and Playboy, which printed 'A Breath of Lucifer' in July 1969 and 'God and the "
  "Cobbler' in February 1976 (Post45 Playboy Fiction Index).",
  "Narayan told William Walsh that English 'is so transparent it can take on the tint of any country', and "
  "Walsh called his English 'limpid, simple, calm and unaffected, natural in its run and tone, and beautifully "
  "measured' (Contemporary Authors). Walsh also described the typical design of the novels as concentric "
  "circles, with the town outside, the family within and a modest, self-aware hero at the hub, and called them "
  "'comedies of sadness'. Melvin J. Friedman placed him, with Isaac Bashevis Singer, in an oral tradition in "
  "which the spoken triumphs over the written. Gale's Contextual Encyclopedia stresses the economy of his "
  "plotting, and notes that the stories of his early collections are slight and journalistic, those of the "
  "later ones longer and more intricately built.",
  "Middle-class life in a small South Indian town and the meeting of tradition and modernity there; money, "
  "ambition and the vanity of human wishes (The Financial Expert); imposture and sainthood (The Guide); the "
  "national movement and Gandhi (Waiting for the Mahatma); fathers and sons and the generation gap (The Vendor "
  "of Sweets); a bully's invasion of a quiet life, told through a Hindu myth (The Man-Eater of Malgudi); love "
  "set against a woman's vocation (The Painter of Signs); renunciation and detachment (A Tiger for Malgudi); "
  "the retelling of Hindu myth and epic; and the comedy of misunderstanding between India and the West ('A "
  "Horse and Two Goats', Talkative Man).",
  "Graham Greene called him 'the novelist I most admire in the English language' (Contemporary Authors), the "
  "poet Dom Moraes 'by far the best writer of English fiction that his country has ever produced' (Gale), and "
  "Shashi Tharoor wrote that in the West he was widely considered the quintessential Indian writer. Critics "
  "compare Malgudi with Faulkner's Yoknapatawpha County, and Walsh wrote that 'whatever happens in India "
  "happens in Malgudi, and whatever happens in Malgudi happens everywhere'. The Guide won the first Sahitya "
  "Akademi Award for English, and in 1994 he became the second Indian writer in English, after Anand, to be "
  "made a Fellow of the Akademi. V. S. Naipaul's reading of his novels as 'religious books ... intensely "
  "Hindu', prepared for withdrawal rather than action, is a political critique that later critics, Richard "
  "Cronin among them, have examined (eNotes).",
  bib_status="substantially complete",
  bib_note="Bibliography status, 1946-2000: substantially complete for books, following Contemporary Authors' "
  "list; uncollected magazine stories are not listed. Recorded as works in this wave (12): An Astrologer's Day "
  "and Other Stories (1947); Mr. Sampath (1949); The Financial Expert (1952); Waiting for the Mahatma (1955); "
  "The Guide (1958); The Man-Eater of Malgudi (1961); The Vendor of Sweets (1967); A Horse and Two Goats and "
  "Other Stories (1970); The Painter of Signs (1976); A Tiger for Malgudi (1983); Talkative Man (1986); The "
  "World of Nagaraj (1990). Listed and still to be recorded (wave 12): Lawley Road (stories, Indian Thought, "
  "Mysore, 1956); Next Sunday: Sketches and Essays (Indian Thought, 1956; Pearl, Bombay, 1960); My Dateless "
  "Diary: A Journal of a Trip to the United States in October 1956 (Indian Thought, 1960; Penguin, 1965); "
  "Gods, Demons, and Others (Viking, 1964; illustrated by R. K. Laxman, University of Chicago Press, 1993); The "
  "Ramayana: A Shortened Modern Prose Version of the Indian Epic (Viking, 1972); My Days: A Memoir (Viking, "
  "1974); Reluctant Guru (Hind Pocket Books, New Delhi, 1974); The Emerald Route, including the play The "
  "Watchman of the Lake (Government of Karnataka, 1977; Ind-US, 1980); The Mahabharata: A Shortened Prose "
  "Version of the Indian Epic (Viking, 1978); Old and New (stories, Indian Thought, 1981); Malgudi Days "
  "(Viking, 1982; a different book from the 1943 Malgudi Days); Under the Banyan Tree and Other Stories (Viking, 1985); "
  "Malgudi Days II (Viking, 1986); A Writer's Nightmare: Selected Essays, 1958-1988 (Penguin, 1988); A "
  "Story-Teller's World: Stories, Essays, Sketches (Penguin, 1989); The Grandmother's Tale (Indian Thought, "
  "1992; with selected stories, Viking, 1994); Salt and Sawdust: Stories and Table Talk (Penguin, New Delhi, "
  "1993); Indian Thought: A Miscellany (editor, Penguin, 1997). Omnibus volumes of earlier work: A Town Called "
  "Malgudi (1999), The Magic of Malgudi and The World of Malgudi (both 2000). Before the period, and not "
  "recorded by installment 9: Swami and Friends (1935), The Bachelor of Arts (1937), The Dark Room (1938), "
  "Mysore (1939), Malgudi Days (1943), Dodu and Other Stories (1943), Cyclone and Other Stories (1944) and The "
  "English Teacher (1945; in the United States as Grateful to Life and Death, 1953). After the period: The "
  "Writerly Life: Selected Non-Fiction (2001). Magazine stories seen in the Post45 Playboy index: 'A Breath of "
  "Lucifer' (July 1969) and 'God and the Cobbler' (February 1976).",
  ver="verified", sources=[CA, GCE, WIKI_RKN, SAHITYA, PLAYBOY],
  alt=["Rasipuram Krishnaswami Narayanaswami", "Rasipuram Krishnaswami Narayan", "R.K. Narayan"]),
]

WORKS = [
W10("An Astrologer's Day and Other Stories", RKN, "1947", "Short-story collection", "minor",
  genres=G("Short-Story Collection"),
  themes=T(VIOLENCE, FAITH, IDENT),
  movements=M(SAL),
  overview="A collection of short stories published in London by Eyre & Spottiswoode in 1947, the first of "
  "Narayan's collections to appear with a British publisher (his three earlier ones were issued in Mysore by "
  "Indian Thought), on Contemporary Authors' list. Its title story is among his most anthologised.",
  content="Stories of Malgudi life, led by 'An Astrologer's Day', in which a market-place astrologer "
  "recognises his last client of the evening as the man he once stabbed and left for dead.",
  summary="In the title story, as Contemporary Authors retells it, a village astrologer plying his trade in "
  "the market gives his last client of the day the usual platitudes until the man angrily demands the truth. "
  "The astrologer then tells him his past: that many years ago he was stabbed and thrown into a well, and has "
  "been hunting his attacker ever since; he even knows the client's name. He advises him to give up the "
  "search, because the attacker has long since died, and takes his fee. At home he tells his wife why he is "
  "late: the man he attacked years ago, and believed he had killed, is alive and well, and his mind is at last "
  "at rest. None of the sources consulted names the collection's other stories.",
  themes_text="Guilt and its release; fate, and the astrologer's performance of foreknowledge; the irony of a "
  "trickster whose 'prophecy' is really memory; the anonymity of the market-place crowd, in which a past can "
  "be hidden for years.",
  structure="The title story turns on a reversal disclosed only at the end, when the astrologer explains "
  "himself to his wife.",
  style="Compressed, ironic short fiction; Wikipedia notes that Narayan's stories have been compared with "
  "Maupassant's for their compressed narratives.",
  ctx="Published in 1947, the year of independence. Chelva Kanaganayakam, in Literature of Developing Nations "
  "for Students, says the title story 'first appeared in 1947' and has remained heavily anthologised for more "
  "than fifty years (quoted by Contemporary Authors). The earlier collections, Malgudi Days (1943), Dodu (1943) "
  "and Cyclone (1944), had been published in Mysore.",
  sig="'An Astrologer's Day' is, with 'A Horse and Two Goats', among Narayan's best-received stories "
  "(Contemporary Authors), and Kanaganayakam finds it significant that a story of 1947 should keep its appeal "
  "after more than fifty years.",
  canon="Minor canon",
  biblio="London: Eyre & Spottiswoode, 1947 (Contemporary Authors). Contents and later editions not checked.",
  notes="Not read. Kanaganayakam's date for the story's first appearance is reported as he gives it; whether "
  "the story had been printed earlier, in a newspaper or one of the Mysore collections, was not checked.",
  ver="partially verified", sources=[CA, WIKI_RKN]),

W10("Mr. Sampath", RKN, "1949", "Novel", "significant",
  genres=G("Comic Novel", "Social Novel"),
  themes=T(ART, MEDIA, LOVE, FAITH),
  movements=M(SAL),
  overview="Narayan's fifth novel, issued in London by "
  "Eyre & Spottiswoode in 1949 and in the United States as The Printer of Malgudi (Michigan State College "
  "Press, 1957). Wikipedia calls it a comic-realist novel of manners. In two parts, it follows Srinivas, the "
  "editor of a small Malgudi paper, and Sampath, his printer, first in journalism and then in a venture into "
  "film-making.",
  content="Srinivas, the idealistic editor of The Banner, depends on the resourceful printer Sampath; when the "
  "paper has to stop, the two join a film company, where Sampath falls for the actress Shanti and the same "
  "infatuation drives a young man, Ravi, mad.",
  summary="Wikipedia's account, following William Walsh, divides the novel in two. In the first part Srinivas, "
  "the editor of a journal called The Banner, and Sampath, its printer, must work together to bring it out; "
  "the two contrasting, good-hearted men form a partnership that makes the paper the centre of attention in "
  "Malgudi, until circumstances force them to suspend it. In the second part they join a company formed to "
  "make a film, where their paths diverge though their bond remains. Sampath, daring and over-ambitious, falls "
  "in love with the film's actress, Shanti; the women's studies article calls the book a 'rollicking tale of "
  "love that maddens a married person, Sampath', and adds that the same pursuit turns a young man, Ravi, into "
  "'a real madman in the end'. Srinivas, weighed down by his sense of responsibility, is driven out by "
  "unpleasant incidents in the studio and revives The Banner with another printer, which Sampath, absorbed in "
  "the actress, hardly notices. At the end Sampath comes back, having lost the woman, his wealth, his fame and "
  "his peace.",
  themes_text="V. S. Naipaul, rereading the novel during the Emergency, called Srinivas 'a contemplative idler' and read "
  "the book as a religious fable of a people 'philosophically prepared for defeat and withdrawal ... rather "
  "than independence and action' (Contemporary Literary Criticism extract). The sources also bring out the "
  "partnership of opposites, the reflective editor and the man of schemes; the film studio as a modern "
  "business that seduces and ruins; and infatuation as a kind of madness. S. C. Harrex's essay treats it as "
  "comedy.",
  structure="Two parts with different centres: the first, on the newspaper, centred on Sampath; the second, "
  "on film production, centred on Srinivas (Walsh, cited by Wikipedia). Walsh calls it the first of three "
  "novels with an external approach, attending to events outside the protagonist rather than to his inner "
  "life as the earlier novels had.",
  style="Comic realism and the manners of a small town; much of the comedy comes from setting the editor's "
  "scruples against the printer's improvisations, and from the glamour and confusion of the studio.",
  ctx="Written after the war and published in 1949, two years after independence; Wikipedia, citing "
  "Masterplots II, sets the action in 1938, under British rule. Its American edition, retitled The Printer of "
  "Malgudi in 1957, was one of several Narayan novels issued in the 1950s by Michigan State College Press "
  "(Contemporary Authors).",
  sig="Filmed twice, as the Hindi Mr. Sampat (1952) and the Tamil Mr. Sampath (1972) (Wikipedia). For "
  "Naipaul it became a key text: in the essay 'An Old Equilibrium' he argued from it that Narayan's novels are "
  "'less the purely social comedies I had once taken them to be than religious books', and, rereading it "
  "during the Emergency of 1975, saw in it 'a foreshadowing of the tensions that had to come to India'. Harrex's essay on its comedy was reprinted in "
  "Contemporary Literary Criticism.",
  chars="Srinivas; Sampath; Shanti; Ravi",
  alt=["The Printer of Malgudi", "Mr. Sampath - The Printer of Malgudi"],
  biblio="London: Eyre & Spottiswoode, 1949; as The Printer of Malgudi, East Lansing: Michigan State College "
  "Press, 1957 (Contemporary Authors). Wikipedia titles its article Mr. Sampath - The Printer of Malgudi.",
  notes="Not read. Shanti's and Ravi's parts come from the women's studies article, seen only as a search "
  "extract; character names found only in reader summaries are not used. The 1938 setting (Masterplots II, "
  "via Wikipedia) was not checked.",
  ver="partially verified", sources=[WIKI_NOVELS, CA, ENOTES, JIWS]),

W10("The Financial Expert", RKN, "1952", "Novel", "major",
  genres=G("Comic Novel", "Social Novel"),
  themes=T(CLASS, FAMILY, FAITH, "Power, the state and surveillance"),
  movements=M(SAL),
  overview="Narayan's sixth novel, published by Methuen in London in 1952 and by Michigan State College Press "
  "in 1953. It tells the rise and fall of Margayya, who begins as a petty money-lender under a banyan "
  "tree outside the Central Co-operative Land Mortgage Bank in Malgudi, grows rich first by publishing a sex "
  "manual and then by taking deposits at extravagant interest, and is ruined by a run on his business. Gale's "
  "Contextual Encyclopedia calls it arguably one of Narayan's best and most popular novels, and William Walsh "
  "praised its 'intricate and silken organization'.",
  content="Margayya helps the bank's shareholders borrow cheaply and relends the money at higher interest, "
  "until bank officials confiscate his forms and his spoilt son Balu throws his account book into a gutter. "
  "After forty days' worship of Lakshmi he buys from the shady Dr Pal a manuscript on 'Bed Life', which becomes "
  "the best-seller Domestic Harmony. He then grows rich on deposits brought in by Dr Pal from black "
  "marketeers, until his quarrel with Dr Pal over Balu's dissipation starts the run that bankrupts him and "
  "sends him back to the banyan tree.",
  summary="Margayya does business under a banyan tree in front of the Central Co-operative Land Mortgage Bank "
  "in Malgudi: he helps the bank's shareholders borrow at low interest and lends the money to the needy at a "
  "higher rate, keeping the difference. The bank's Secretary and its peon, Arul Doss, seize the loan forms from "
  "his box and threaten to proceed against him, which sets him on the way to improving his position. Then his spoilt son, Balu, "
  "throws the red account book holding all his transactions into the gutter, and the old business cannot go "
  "on. An astrologer assures him that good times will come if he worships Lakshmi, the goddess of wealth, and "
  "he performs the worship for forty days, with ash from a red lotus and ghee from the milk of a grey cow. Soon "
  "afterwards Dr Pal sells him, for whatever cash is in his purse, the manuscript of a book on 'Bed Life'; "
  "Madan Lal, 'a man from the North', publishes it on equal shares as Domestic Harmony, it sells in great "
  "numbers, and Margayya makes his fortune.\n\n"
  "His next ruin comes through Balu. Margayya enrols him in school in style, becomes secretary of the school "
  "committee and hires a tutor with orders to beat the boy when necessary, but Balu fails the school-leaving "
  "examination, tears up his certificate book, throws it into the same gutter and runs away. A letter from "
  "Madras reports him dead; Margayya, helped by a fellow traveller who is a plain-clothes police inspector, "
  "finds him alive and brings him home. He arranges Balu's marriage to Brinda, daughter of a tea-estate owner "
  "in the hills, dismissing an honest pundit who finds the horoscopes unmatched and paying another astrologer, "
  "found by Dr Pal, to certify that they agree, and he sets the couple up in Lawley Extension. To draw Dr Pal "
  "away from his son, he employs him to bring in deposits from black marketeers on the promise of high "
  "interest, paid out of the stream of new deposits. Margayya becomes rich, buys a car, stuffs every corner of "
  "his house with sacks of notes and gives to the War Fund when pressed.\n\n"
  "One day he visits Balu's house, where Brinda, with her child, tells him in tears of her husband's nights; "
  "Balu then drives up with Dr Pal and two women of the town. Margayya drags Dr Pal from the car, beats him "
  "and sends the women away. The next day the bandaged Dr Pal whispers that Margayya's affairs are unsound; "
  "depositors besiege him, his wealth is paid out, hundreds remain unpaid, and he files for insolvency. In the "
  "end he tells Balu to take his old place under the banyan tree with the box, and when the young man "
  "hesitates, ashamed of what people will say, Margayya offers to go back there himself.",
  themes_text="Money is the subject: Wikipedia calls the theme lust for money, and an excerpt reprinted in "
  "Contemporary Literary Criticism quotes Margayya's credo, 'Money alone is important in this world.' Gale's "
  "Contextual Encyclopedia reads the plot as a study of 'the vanity of human wishes', yet Margayya is no "
  "monster: Narayan keeps him human and able to hold the reader's sympathy (Wikipedia; Gale). Fathers and "
  "sons: the same excerpt pairs the book with The Vendor of Sweets as novels told from the father's side, and "
  "the spoilt, prodigal Balu, whom Margayya both indulges and has beaten, undoes him twice. Religion and "
  "fortune: worship of Lakshmi, horoscopes bought to order and astrology turned to business show piety "
  "entangled with greed. Society: Gale sets the rise and fall against wartime poverty, corruption, "
  "bureaucracy and the opportunism of businessmen and officials, while Dr Pal, 'the archetypal confidence "
  "man', embodies the town's appetite for easy money and illicit pleasure.",
  structure="A double cycle of rise and fall, each turn set off by Balu: the account book thrown into the "
  "gutter ends the first trade, and the certificate thrown into the same gutter begins the crisis that leads "
  "to the second. Gale observes that Narayan alternates the details of everyday Malgudi life with views into "
  "Margayya's mind, and Walsh praises 'a scheme of composition holding everything together in a vibrant and "
  "balanced union'. The ending returns Margayya to the banyan tree where he began.",
  style="Narration that is, in Gale's words, 'serious and comic throughout', moving between the bank steps, "
  "the household and Margayya's private calculations. The comedy is gentle rather than satirical: his "
  "schemes, his rituals for Lakshmi and Dr Pal's patter are treated with irony but without contempt, in the "
  "plain, measured English Walsh found 'limpid, simple, calm and unaffected' (Contemporary Authors).",
  ctx="Published in 1952 and set during the Second World War: Margayya gives to the War Fund, and his "
  "depositors are black marketeers, so the boom he exploits is the wartime economy of shortage and illicit "
  "profit (Wikipedia; Gale). The co-operative land-mortgage bank, an institution meant to give landholders "
  "cheap credit (general knowledge), supplies the margin he lives on. Methuen published it in London (as "
  "Mondal also notes), and the American edition of 1953 was one of several Narayan novels issued by Michigan "
  "State College Press in the 1950s.",
  sig="Often counted among Narayan's finest novels: Gale's Contextual Encyclopedia calls it arguably one of "
  "his best and most popular, and cites the praise for it and for The Guide as typical of the response to his "
  "work. Gale singles out its portraits of Margayya, Dr Pal, Margayya's long-suffering wife Meenakshi and the "
  "prodigal Balu. The excerpt in Contemporary Literary Criticism reads it with The Vendor of Sweets as one of "
  "the novels told from a father's point of view, and G. S. Amur's essay on symbolism reads it with The "
  "English Teacher and The Vendor of Sweets. It was filmed in Kannada as Banker Margayya (1983) (Wikipedia).",
  crit="Walsh: the novel 'has an intricate and silken organization, a scheme of composition holding "
  "everything together in a vibrant and balanced union' (quoted by Gale). Gale's encyclopedia praises "
  "Narayan's 'powerful handling of the central theme of the vanity of human wishes and his deft manipulation "
  "of plot', and finds Margayya 'deeply flawed but also capable of retaining the reader's sympathy'. Amur's "
  "essay, reprinted in Contemporary Literary Criticism, traces the lotus pond, the garden and the ruined "
  "temple as symbols in this novel and two others.",
  chars="Margayya; Meenakshi; Balu; Dr Pal; Madan Lal; Arul Doss; Brinda",
  canon="Major canon",
  biblio="London: Methuen, 1952; East Lansing: Michigan State College Press, 1953 (Contemporary Authors). "
  "Filmed in Kannada as Banker Margayya (1983).",
  notes="Not read. The plot follows Wikipedia's long summary, which is flagged as overlong but agrees with "
  "Gale's characterisation. Wikipedia puts the tea estate in the 'Memphis Hills', evidently Narayan's Mempi "
  "Hills, and gives a figure of 29 per cent for the promised interest; neither detail is used. Meenakshi's "
  "name comes from Gale.",
  ver="partially verified", sources=[WIKI_NOVELS, GCE, CA, ENOTES, MONDAL]),

W10("Waiting for the Mahatma", RKN, "1955", "Novel", "significant",
  genres=G("Political Novel", "Comic Novel"),
  themes=T("Decolonisation, the end of empire and the new nation", "Nationhood and national identity", LOVE,
           GENDER, FAMILY),
  movements=M(SAL),
  overview="Narayan's seventh novel, published in 1955 by Michigan State College Press (Contemporary "
  "Authors), with a London edition from Methuen (Mondal). Set in Malgudi in the last years of British rule, it "
  "follows Sriram, drawn into Gandhi's movement by his love for Bharati, and is unusual among Narayan's novels "
  "in bringing Gandhi on stage. Gale's Contextual Encyclopedia calls it his most political novel.",
  content="Sriram, a high-school graduate living with his grandmother, follows Bharati into the Quit India "
  "movement, drifts into the company of anti-British extremists, is jailed, and is finally engaged to Bharati "
  "amid partition and the death of Gandhi.",
  summary="Sriram, who has finished high school, lives with his grandmother in Malgudi. He is attracted to "
  "Bharati, a girl of his own age who is active in Gandhi's Quit India movement, and becomes an activist "
  "himself. He then falls in with anti-British extremists, to his grandmother's great grief. His underground "
  "work takes him into a countryside that is alien to him, and his misunderstandings with the villagers "
  "provide, in Wikipedia's judgement, the book's best comic moments. After a spell in jail he is reunited with "
  "Bharati, and the novel ends with their engagement amid the tragedy of partition in 1947 and Gandhi's death "
  "in 1948. Gandhi appears as a character, and his ideas and practices are set against the views of "
  "traditionalists such as the town's notables and Sriram's grandmother. The romance is unconventional and is "
  "concluded outside either family's circle (Wikipedia); the women's studies article sees Bharati as "
  "Narayan's exemplary modern woman, graceful, disciplined, devoted to her teacher and to the nation.",
  themes_text="Love and politics: Bharati draws Sriram into the national movement, and Cynthia vanden "
  "Driesen's essay traces his relationship to Gandhi (eNotes contents). Ambivalence towards nationalism: "
  "Satish Aikant (Journal of Commonwealth Literature, 2007) finds a 'colonial ambivalence', perhaps owed to "
  "Narayan's largely British readership, and Harveen Mann (ARIEL, 2000) a patriarchal nationalism (both cited "
  "by Wikipedia). Tradition against reform: Gandhi's practice against the grandmother and the notables. "
  "Women's agency: the women's studies article finds romantic and political purpose united in Bharati.",
  structure="A chronological narrative that moves from the town to the countryside and to jail and closes on "
  "partition and Gandhi's death; the political struggle serves as the background to the romance (Wikipedia).",
  style="Narayan's 'gentle comic style' (Wikipedia), in low-key storytelling behind which, in the same "
  "article's phrase, much happens; the comedy of Sriram's encounters with villagers sits beside the gravity of "
  "Gandhi's scenes.",
  ctx="Written in the early 1950s about the years from the Quit India movement, launched in August 1942, to "
  "independence and partition in 1947 and Gandhi's assassination in January 1948 (general historical dates). "
  "Michigan State College Press, which brought out Narayan's novels in America in the 1950s, published it in "
  "1955.",
  sig="Unusual among Narayan's novels in having Gandhi as a character and the independence struggle as its "
  "subject; Gale calls it his most political novel. Its politics have divided critics: vanden Driesen called "
  "it Narayan's neglected novel, and Richard Cronin's essay 'Quite Quiet India' uses it, with The Painter of "
  "Signs, to examine V. S. Naipaul's appraisal of the religious and the political in Narayan's work (eNotes).",
  chars="Sriram; Bharati; Sriram's grandmother; Mahatma Gandhi",
  biblio="East Lansing: Michigan State College Press, 1955 (Contemporary Authors; Wikipedia's infobox names "
  "Michigan State University Press, the same press under its later name); London: Methuen (Mondal; year not "
  "given there).",
  notes="Not read. The plot is Wikipedia's (a stub with two scholarly references). The names of the extremist "
  "leader and other characters, found only in reader summaries, are not used. The date of the London edition "
  "was not checked.",
  ver="partially verified", sources=[WIKI_NOVELS, CA, GCE, ENOTES, JIWS, MONDAL]),

W10("The Guide", RKN, "1958", "Novel", "major",
  genres=G("Philosophical Fiction", "Comic Novel"),
  themes=T(FAITH, IDENT, ART, LOVE, MEDIA),
  movements=M(SAL),
  overview="Narayan's best-known novel, published in New York by Viking and in London by Methuen in 1958. It "
  "tells how Raju, a tourist guide in Malgudi, becomes the lover and manager of a dancer, Rosie, goes to "
  "prison for forgery and, on his release, is taken for a holy man by villagers who expect him to fast to end "
  "a drought. It won the first Sahitya Akademi Award given to a book in English (1960), was filmed as Guide "
  "(1965) and staged in New York (1968), and Gale's Contextual Encyclopedia says it is usually considered "
  "Narayan's most accomplished novel.",
  content="Raju, a popular and unscrupulous guide nicknamed 'Railway Raju', falls in love with Rosie, wife of "
  "the archaeologist Marco, while the couple visit Malgudi. When Marco abandons her, Rosie moves in with Raju, "
  "whose mother leaves the house; Raju becomes her manager and makes her a famous dancer, then grows "
  "controlling and is jailed for two years for forgery. Released, he shelters in an abandoned temple near the "
  "village of Mangal, where the villager Velan takes him for a sadhu; when drought brings famine, the "
  "villagers expect him to fast for rain, and the fast becomes a public spectacle.",
  summary="The novel begins after Raju's release from prison, with a villager, Velan, consulting him as a holy "
  "man at an abandoned temple near the village of Mangal. Brians's study guide notes the abrupt turns of the "
  "opening chapter, into the past and forward to the time when Raju will tell Velan his life story; from then "
  "on the narrative alternates between the present at the temple and the story of how Raju came there.\n\n"
  "That story begins with 'Railway Raju', a popular and not very scrupulous guide to the sights around "
  "Malgudi. Among his clients are Marco, an archaeologist, and his wife Rosie, who longs to dance; Marco "
  "disapproves of her passion, but Raju encourages her to pursue it, and the two become close. When Marco "
  "learns of their relationship, he leaves Rosie in Malgudi and returns to Madras alone. Rosie takes refuge in "
  "Raju's home, and they live together; Raju's mother, who does not approve, leaves them. Raju becomes Rosie's "
  "stage manager, and through his promotion she wins recognition as a dancer. Success makes him overconfident; "
  "he asserts more and more control over her life for financial gain, becomes involved in a forgery case "
  "connected with Rosie's signature, and despite Rosie's defence is sentenced to two years in prison.\n\n"
  "After his sentence Raju passes through Mangal and, rather than return to Malgudi in disgrace, stays in the "
  "temple and accepts the part the villagers give him, delivering sermons and settling their quarrels. When "
  "drought brings famine, some of the villagers come to believe that the rains will come if he fasts. Raju "
  "confesses his whole past to Velan, but Velan's faith is unchanged, and Raju resolves to go on with the "
  "fast. As news of it spreads through the press, a large crowd gathers to watch, to his annoyance. On the "
  "morning of the eleventh day he goes down to the river for his daily ritual, senses rain falling in the "
  "distant hills, and collapses into the water. Whether it really rained, and whether Raju died, the novel "
  "does not say.",
  themes_text="Imposture and transformation: Raju is a guide in successive senses, to tourists, to Rosie's "
  "career and at last to the villagers, and the question the novel leaves open is whether the pretended holy "
  "man becomes a real one; Brians notes that the book begins as a comic look at a rogue's life and 'evolves "
  "into something quite different'. Faith and its uses: the villagers' belief creates Raju's role, Velan's "
  "faith survives his confession, and the fast can be read either as the culmination of a fraud or as a "
  "genuine sacrifice; Brians cautions that Narayan was not a devout Hindu and objected to Westerners' "
  "assumption that all Indians are deeply spiritual. Art and commerce: Rosie's dancing, scorned by her "
  "husband, becomes under Raju's management a business, and Brians points to the double standing of the "
  "traditional temple dancer, of whom the novel offers both negative and positive images. Publicity: the "
  "fast turns into a spectacle reported by the press. Gale's encyclopedia stresses that Raju is unable to "
  "convince the villagers that he is a fraud.",
  structure="Two interleaved time-lines, the present at the temple near Mangal and Raju's past, with blank "
  "lines marking the shifts (Brians). The present is narrated in the third person and the past largely in "
  "Raju's own voice as he recounts it (general knowledge, not checked in the sources). The past catches up "
  "with the present at the fast, and the ending, on the eleventh day, is left open.",
  style="Narayan's even, understated English carries both the comedy of Raju's opportunism and the gravity of "
  "the fast, and the ending refuses to decide between them. The vocabulary of South Indian daily life, from "
  "betel leaf to the pyol where neighbours sit and talk, is used without explanation, which is why Brians "
  "glosses it for American students. The irony is gentle: the holy man's authority is accidental, but the "
  "villagers' need is real.",
  ctx="Published in 1958, eleven years after independence, by Viking in New York and Methuen in London. "
  "Narayan said that the episode of the reluctant holy man came from a real incident he had read about in a "
  "newspaper (Brians). The Sahitya Akademi, India's national academy of letters, gave it the first of its "
  "awards for English in 1960 (the Akademi's list; Contemporary Authors dates Narayan's award 1961).",
  sig="The Narayan novel most widely read and adapted. Vijay Anand's Hindi film Guide (1965), with Dev Anand "
  "as Raju and Waheeda Rehman as Rosie, changed the ending; an English-language version written by Pearl S. "
  "Buck and directed by Tad Danielewski was screened at Cannes in 2007 (Wikipedia). Harvey Breit and Patricia "
  "Rinehart's stage adaptation was produced at the Hudson Theatre in New York in 1968 (Contemporary Authors), "
  "a production William Goldman profiled in The Season. In 2022 it was chosen for the Big Jubilee Read, a list "
  "of seventy books by Commonwealth authors.",
  crit="Anthony West, in the New Yorker in 1958, called it 'the best of R. K. Narayan's enchanting novels "
  "about the South Indian town of Malgudi and its people' and 'a profound statement of Indian realities' "
  "(quoted by Gale). Gale reports that it is usually considered his most accomplished novel, and Brians calls "
  "it 'one of his most interesting books'. Readers differ over the ending: Wikipedia stresses that Raju's fate "
  "is left to the reader, whereas Gale's summary has him die during the fast and be revered as a saint.",
  chars="Raju; Rosie; Marco; Velan; Raju's mother",
  canon="Major canon",
  biblio="New York: Viking, 1958 (Contemporary Authors; first American edition, 220 pp., per Wikipedia); "
  "London: Methuen, 1958 (Wikipedia; Mondal). Stage adaptation by Harvey Breit and Patricia Rinehart (Hudson "
  "Theatre, New York, 1968); film, Guide (1965).",
  notes="Not read. The plot follows Wikipedia; the first of the three parts of Brians's study guide confirms "
  "the opening at the temple and the alternation of present and past. Gale's one-sentence summary places "
  "Raju's arrival in Malgudi and has him die and become a saint; both conflict with Wikipedia's fuller account "
  "and are not followed. Contemporary Authors and the Akademi's list disagree on the year of the award (1961 "
  "and 1960), and Contemporary Authors calls the 1968 production Off-Broadway, although the Hudson is a "
  "Broadway house (general knowledge) and Goldman's book is about Broadway.",
  ver="partially verified", sources=[WIKI_NOVELS, BRIANS, GCE, CA, SAHITYA, MONDAL]),

W10("The Man-Eater of Malgudi", RKN, "1961", "Novel", "significant",
  genres=G("Comic Novel"),
  themes=T(MYTH, VIOLENCE, NATURE),
  movements=M(SAL),
  overview="A comic novel published by Viking in New York in 1961, in which Nataraj, a contented printer of "
  "Malgudi, has his press and his peace taken over by Vasu, a bullying taxidermist who moves into his attic. "
  "Wikipedia notes that Narayan draws on the myth of Bhasmasura, and Gale's Contextual Encyclopedia calls the "
  "novel 'another triumph' after The Guide.",
  content="Vasu, a strongman and taxidermist come to hunt in the Mempi Hills, installs himself in Nataraj's "
  "attic, drives away his friends and customers, shoots animals for stuffing and plans to shoot an elephant "
  "Nataraj has brought down from the hills; he is found dead, having struck his own head while killing a "
  "mosquito.",
  summary="Nataraj lives in a large ancestral house in Malgudi and runs a small printing press with one "
  "employee, Sastri; a poet and a journalist named Sen are among the friends who gather there. Vasu, a "
  "taxidermist come in search of the wildlife of the Mempi Hills, walks into the press demanding five hundred "
  "visiting cards, and soon installs himself in its attic, promising to stay only a few days. Nataraj and "
  "Sastri come to see him as a rakshasa, a demon. Vasu bullies away Nataraj's friends and customers, shoots a "
  "pet dog and many other animals and birds, poaches in the hills, fills the neighbourhood with the stench of "
  "his work and entertains women in the attic; when Nataraj questions him, Vasu complains to the rent "
  "controller as a harassed tenant. As Nataraj's poet friend prepares a celebration for the release of his "
  "book of verse on Krishna, Rangi, a temple dancer, tells Nataraj that Vasu means to kill Kumar, an elephant "
  "Nataraj has brought from the hills for treatment as a favour to a friend. Muthu, a tea-shop owner, agrees "
  "to help, but Nataraj fails to stop Vasu; resolving on a final confrontation, he finds him asleep, and next "
  "morning Vasu is dead. The autopsy finds a blow from a blunt weapon; the case is closed, but Nataraj's press "
  "is ruined and his friends avoid him. Later he learns through Sastri, who heard it from Rangi, that Vasu "
  "died when he brought his own powerful hand down on a mosquito sitting on his head. The story ends with the "
  "moral that demons bring about their own destruction.",
  themes_text="Good and evil in a comic key: Vasu is a modern rakshasa, and his death enacts the legend of "
  "Bhasmasura, the demon who could turn to ashes anyone on whose head he laid his hand and who was tricked "
  "into laying it on his own (Wikipedia names the myth; its content is general knowledge). Hospitality and its abuse: Nataraj's "
  "inability to refuse or expel his guest is both a virtue and a weakness. Exploitation of nature: the "
  "slaughter of the hills' wildlife and the threat to the elephant. Community: the circle of printer, poet and "
  "journalist stands for a gentle town life that the bully disrupts.",
  structure="A chronological narrative told by Nataraj (his first-person narration is general knowledge), "
  "building from Vasu's arrival to the night of the celebration and closing with the revelation of how he "
  "died.",
  style="A comedy of mounting exasperation; Vasu's brute vitality is set against Nataraj's timidity, and the "
  "climax turns a mythic pattern into farce.",
  ctx="Published by Viking in 1961, three years after The Guide, and set in Malgudi and the Mempi Hills. "
  "Narayan's own retellings of Indian myths, Gods, Demons, and Others, followed in 1964 (Contemporary "
  "Authors).",
  sig="Gale's Contextual Encyclopedia calls it 'another triumph' after The Guide and lists it among Narayan's "
  "major works. It sets a Hindu myth inside a realistic Malgudi story, as Wikipedia observes, and its cast of "
  "printer, poet, journalist, temple dancer and tea-shop owner shows the cross-section of the town that the "
  "novels assemble.",
  chars="Nataraj; Vasu; Sastri; Sen; the poet; Rangi; Muthu; Kumar (an elephant)",
  biblio="New York: Viking, 1961; 250 pp. (Contemporary Authors; Wikipedia). The London edition was not "
  "checked.",
  notes="Not read; the plot follows Wikipedia. Nataraj's first-person narration and the content of the "
  "Bhasmasura legend are general knowledge.",
  ver="partially verified", sources=[WIKI_NOVELS, GCE, CA]),

W10("The Vendor of Sweets", RKN, "1967", "Novel", "significant",
  genres=G("Domestic Fiction", "Comic Novel"),
  themes=T(FAMILY, FAITH, "Migration, exile and diaspora", MEDIA),
  movements=M(SAL),
  overview="A novel published by Viking in New York and, as The Sweet-Vendor, by the Bodley Head in London in "
  "1967. Jagan, a widowed sweet-seller of Malgudi and a lifelong Gandhian, struggles to understand his only "
  "son, Mali, who comes back from creative-writing studies in America with a companion, Grace, and a scheme "
  "to manufacture story-writing machines.",
  content="Jagan, fifty-five, prosperous and devoted to the Bhagavad Gita, naturopathy and hand-spun cloth, "
  "indulges his motherless son; Mali leaves college, goes to America with money taken from his father's "
  "hidden savings and returns with Grace and a business plan Jagan will not fund. Jagan drifts towards "
  "renunciation, and when Mali is arrested for drunken driving he leaves him to the law while paying towards "
  "his bail and offering Grace her fare home.",
  summary="Jagan, fifty-five, sells sweets in Malgudi and prospers. In his youth he left his studies to follow "
  "Gandhi in the freedom struggle, was commended by Gandhi for wearing hand-spun cloth, and he still lives by "
  "the Bhagavad Gita and by naturopathy, on which he has written a book that has lain at Nataraj's press for "
  "five years. His wife, Ambika, died of a brain tumour, leaving him to bring up their son, Mali, whom he "
  "spoils. In college Mali announces that he wants to be a writer and, without telling his father, arranges "
  "to go to America to study creative writing, using money from the cash Jagan has hidden from the tax "
  "collector. Jagan accepts this and proudly shows Mali's letters to everyone. Years later Mali returns, "
  "Westernised, with Grace, half-American and half-Korean, whom he calls his wife; Jagan grows fond of her and "
  "feels that Mali neglects her. Mali's grand scheme, a factory for story-writing machines with unnamed "
  "American partners, needs his father's money, and Jagan's refusal deepens the rift. Troubled, Jagan "
  "withdraws from the shop; a meeting with an eccentric 'bearded man', whose eloquence makes him reflect on "
  "his monotonous life, stirs a longing for renunciation and memories of his married years. When Mali is "
  "arrested for drunken driving and deserts Grace, Jagan tells his cousin that a dose of prison life will do "
  "him no harm, but writes a cheque for the preliminary costs of his bail and offers to buy Grace a ticket "
  "home if she wants one.",
  themes_text="Fathers and sons and the generation gap, which Wikipedia calls the main theme, and which the "
  "excerpt in Contemporary Literary Criticism pairs with The Financial Expert as novels told from the father's "
  "side. Tradition and the West: Jagan's Gandhian austerity, his Gita and his naturopathy against Mali's "
  "American ambitions and his claim that Grace is his wife. Money and conscience: Jagan's hidden, untaxed "
  "cash sits uneasily with his Gandhian virtue, and Wikipedia's character note says he uses religion to quiet "
  "his agitation. Renunciation: the ending turns to the Hindu ideal of withdrawal from worldly life.",
  structure="A third-person narrative centred on Jagan, moving between the present and his memories of youth, "
  "marriage and Gandhi; Wikipedia calls the book the 'biography' of its fictional sweet-vendor.",
  style="Gentle irony at Jagan's expense: his maxim 'Conquer taste, and you will have conquered the self' "
  "(Wikipedia) sits beside his trade in sweets, and his piety beside his concealed cash.",
  ctx="Published in 1967, with the British edition retitled The Sweet-Vendor (Contemporary Authors). Its "
  "contrast between a Gandhian of the freedom-struggle generation and a son formed by America sets the clash "
  "of generations in post-independence India. It was adapted as 'Mithaivalla' for the Hindi television series "
  "Malgudi Days (Wikipedia).",
  sig="Wikipedia makes the generation gap its main theme and the clash of Indian and Western culture another. "
  "Critics have read it beside The Financial Expert as a novel of fathers (Contemporary Literary Criticism "
  "extract) and with The English Teacher and The Financial Expert for its symbols (G. S. Amur, via eNotes).",
  chars="Jagan; Mali; Grace; Ambika; Jagan's cousin; the bearded man",
  alt=["The Sweet-Vendor"],
  biblio="New York: Viking, 1967; London: Bodley Head, 1967, as The Sweet-Vendor (Contemporary Authors).",
  notes="Not read. The plot follows Wikipedia, whose article is flagged for more citations and cites a "
  "SuperSummary page for the paragraph on Jagan's background. Its description of the bearded man as a "
  "'hairdryer' looks like a slip and is not used. Gale's Contextual Encyclopedia mentions 'two less popular "
  "works' between The Man-Eater of Malgudi and A Tiger for Malgudi without naming them; by Contemporary "
  "Authors' list they would be this novel and The Painter of Signs.",
  ver="partially verified", sources=[WIKI_NOVELS, CA, ENOTES, GCE]),

W10("A Horse and Two Goats and Other Stories", RKN, "1970", "Short-story collection", "minor",
  genres=G("Short-Story Collection"),
  themes=T(CLASS, LANG, ART),
  movements=M(SAL),
  overview="A collection of short stories published by Viking in New York in 1970, named after one of "
  "Narayan's best-known stories, a comedy of misunderstanding between a poor old goatherd and an American "
  "visitor.",
  content="Headed by 'A Horse and Two Goats', in which Muni, an old goatherd, and an American businessman who "
  "wants to buy the clay horse beside which Muni rests bargain without a common language.",
  summary="In the title story, as Contemporary Authors summarises it, Muni, a poor goatherd, rests in the "
  "shade of a statue of a horse made of clay while his goats graze. An American businessman passing by wants "
  "to buy the statue for his house in New York. Neither speaks the other's language, so the American assumes "
  "he is negotiating for the horse while Muni believes he is selling his goats. When the American hands him a "
  "hundred rupees, a vast sum for the old man, Muni runs home to tell his wife; the American hires a truck "
  "and carts the statue away, the goats wander home by themselves, and Muni is left to explain as best he can "
  "how he came by so much money. The sources consulted do not list the other stories in the volume.",
  themes_text="Cross-cultural incomprehension; poverty and value, since each man prizes the clay horse "
  "differently; humour without judgement. Ralph J. Crane locates the irony in 'the total benign "
  "incomprehension that exists between the two' (Contemporary Authors).",
  structure="Built on a double dialogue in which each speaker develops 'his own hermetically-sealed "
  "interpretation of the other's words and gestures' (Crane).",
  style="Comic irony and what Crane calls a 'wonderful double discourse'; the story's charm, he adds, lies in "
  "Narayan's refusal to pass judgment.",
  ctx="Published in 1970 by Viking, Narayan's American publisher since The Guide. Narayan had described his "
  "own first journey to America, in 1956, in My Dateless Diary (1960); the title story reverses the direction, "
  "bringing an American to an Indian village.",
  sig="With 'An Astrologer's Day', the title story is among Narayan's best-received (Contemporary Authors), "
  "and Crane's entry in the Reference Guide to Short Fiction treats it as a model comedy of cultural "
  "misunderstanding.",
  canon="Minor canon",
  biblio="New York: Viking, 1970 (Contemporary Authors). Contents and the London edition not checked.",
  notes="Not read; contents other than the title story not identified.",
  ver="partially verified", sources=[CA]),

W10("The Painter of Signs", RKN, "1976", "Novel", "significant",
  genres=G("Comic Novel", "Social Novel"),
  themes=T(LOVE, GENDER, ART, FAITH, "Power, the state and surveillance"),
  movements=M(SAL),
  overview="A short novel published by Viking in New York in 1976, with a London edition from Heinemann, in "
  "which Raman, a rationalist sign-painter of Malgudi, falls in love with Daisy, a young woman who runs the "
  "town's family-planning campaign, and loses her to her vocation.",
  content="Raman, who lives with his pious aunt and prides himself on his lettering, paints boards for "
  "Daisy's family-planning office and tours the villages with her; they become lovers and plan a simple "
  "marriage, his aunt leaves for Benares rather than see him marry outside his caste, and on the day Daisy is "
  "to move in she leaves for a three-year campaign elsewhere in India.",
  summary="Raman takes the craft of lettering seriously: his signboards, made of the best rosewood from the "
  "Mempi mountains, are better, he believes, than his rival Jayaraj's. He lives on Ellaman Street with his "
  "aunt, a conservative old woman fond of mythological stories and family gossip, whose interest in his doings "
  "irritates him and whom he feels guilty for neglecting. Not orthodox himself, he despises superstition and "
  "caste and reads old books on science and history, though he is given to quoting scripture. Daisy, an "
  "intense young woman working in family planning, hires him to make a signboard for her office; he is "
  "captivated by her precision, authority and devotion to her work, and accompanies her on a three-week tour "
  "of the villages around Malgudi to find sites for messages on population control. His resolve never to "
  "marry weakens. Daisy tells him about her complicated past and admits that she is attracted to him; they "
  "spend nights together and decide on a Gandharva marriage, the simplest form of union, on her terms: she "
  "will not change her name or keep house for him. His aunt, upset above all by his marrying outside his "
  "caste, asks him to arrange a one-way journey to Benares and goes despite his pleas. On the morning Daisy "
  "is to move into his house she changes her mind, fearing that married life will compromise her purpose and "
  "independence, and leaves Malgudi for a three-year family-planning project in villages across India, while "
  "Raman tells her that his house will be open to her whenever she returns.",
  themes_text="Love against vocation: Daisy, who in the women's studies article asserts her autonomy by "
  "refusing motherhood along with other conditions, chooses her work over marriage. Modernity and tradition: "
  "Raman's rationalism and his love across caste set against his aunt's orthodoxy and her retreat to Benares. "
  "The state in the village: Daisy's campaign brings the government's population policy into Malgudi's "
  "countryside. Art as craft: Raman's pride in his lettering.",
  structure="A narrative that follows Raman's point of view in Wikipedia's account, with Daisy's past told "
  "when she confides in him, ending without reconciliation.",
  style="Comic irony at the expense of a rationalist who keeps quoting the scriptures, and of his infatuation "
  "with a woman who shuns every comfort (Wikipedia's account of the characters).",
  ctx="Published in 1976. India's family-planning programme, which Daisy serves, became notorious for "
  "coercive sterilisation during the Emergency of 1975-1977 (general historical knowledge). Richard Cronin's "
  "essay reads the novel with Waiting for the Mahatma to examine V. S. Naipaul's view of the religious and the "
  "political in Narayan (eNotes).",
  sig="Daisy belongs with Narayan's independent women, whom the women's studies article groups with Rosie of "
  "The Guide and Shanti of Mr. Sampath. It was reprinted in The World of Malgudi (2000), an omnibus of four "
  "novels (Contemporary Authors).",
  chars="Raman; Daisy; Raman's aunt; Jayaraj",
  biblio="New York: Viking, 1976 (Contemporary Authors); London: Heinemann (Wikipedia; year not checked). The "
  "American jacket is by Abner Graboff (Wikipedia).",
  notes="Not read. Wikipedia's plot section is flagged as unreferenced; it agrees with the women's studies "
  "article (a search extract) on Daisy's refusals. Gale's 'two less popular works' (see The Vendor of Sweets) "
  "would include this novel.",
  ver="partially verified", sources=[WIKI_NOVELS, CA, JIWS, ENOTES]),

W10("A Tiger for Malgudi", RKN, "1983", "Novel", "significant",
  genres=G("Philosophical Fiction"),
  themes=T(NATURE, FAITH, VIOLENCE),
  movements=M(SAL),
  overview="A novel narrated by a tiger, published in 1983 by Viking in New York and Heinemann in London. "
  "Raja, old and in a zoo, tells of his life in the jungle, his capture and training in a Malgudi circus, his "
  "rampage, and his taming by a holy man, the Master, with whom he finds peace. Narayan's introduction traces "
  "the idea to a report he read of a monk moving about with a pet tiger at the Kumbh Mela in Allahabad.",
  content="Raja loses his tigress and cubs to hunters, raids village livestock, is caught by poachers and "
  "sold to a circus in Malgudi, where the Captain starves and trains him; he kills the Captain and runs loose "
  "in the town until the Master calms him and takes him to the hills, later giving him to the zoo.",
  summary="Raja, an old tiger in a zoo, tells his own story. Young and free in the jungle, he mated with a "
  "tigress and raised a litter until hunters killed his whole family. He took revenge on the cattle and "
  "livestock of nearby villages until poachers caught him and sent him to a circus in Malgudi, where a harsh "
  "trainer known only as the Captain, owner of the Grand Malgudi Circus, starved him and forced him to perform. "
  "He lived in captivity for some time, but his wild instincts overcame him and he mauled and killed the "
  "Captain. After a long rampage through the town he was taken, this time willingly, by a monk, the Master, "
  "who befriended him and with whom he found peace in the hills. Sensing his own end approaching, the Master "
  "gave the ageing tiger to the zoo, where he is cared for and admired, and where, watched by children, he "
  "realises that he has done something to make people happy. Wikipedia's cast list adds the Captain's wife, "
  "Rita; Madan, a film producer and director; Jaggu, an actor; Alphonso, a hunter and poacher; and Jayaraj, a "
  "frame-maker.",
  themes_text="Captivity and freedom; the bond between a wild creature and a renunciant, which Wikipedia "
  "singles out as the book's moving centre; violence and its taming; and detachment, which Wikipedia relates "
  "to the teaching of the Buddha's enlightenment. Human cruelty, in the hunters, poachers and the Captain, is "
  "seen from the animal's side.",
  structure="A retrospective first-person narrative by the tiger, preceded by Narayan's introduction on its "
  "origins; it moves from jungle to circus, town and hermitage and ends in the zoo.",
  style="Narayan's plain style adapted to an animal narrator, whose view of human customs produces irony; "
  "Wikipedia says he consulted the tiger expert K. Ullas Karanth (an unreferenced statement).",
  ctx="Published in 1983, when Narayan was in his late seventies. His introduction names three prompts: a report of a "
  "monk moving around with a pet tiger at the Kumbh Mela, accounts of lasting friendships between tigers and "
  "people, and a bookmark showing a tiger with the words 'I'd love to get into a good book' (Wikipedia, citing "
  "S. R. Ramteke, 1998, and the 1995 Allied edition).",
  sig="Gale's Contextual Encyclopedia says that, with a tiger as its protagonist, it 'made yet another "
  "impression', but that it was the last Narayan novel to receive wide critical attention, with mixed "
  "reviews and a few critics' disappointment. It was reviewed by Phoebe-Lou Adams in the Atlantic and in "
  "People (Contemporary Authors), and later reprinted in The World of Malgudi (2000).",
  chars="Raja (the tiger); the Captain; Rita; Madan; Jaggu; Alphonso; the Master; Jayaraj",
  biblio="New York: Viking, 1983 (Contemporary Authors); London: Heinemann, 1983 (Wikipedia); 175 pp.",
  notes="Not read; the plot follows Wikipedia. Karanth's part is unreferenced there. Gale calls it Narayan's "
  "twelfth novel, which matches Contemporary Authors' list.",
  ver="partially verified", sources=[WIKI_NOVELS, GCE, CA]),

W10("Talkative Man", RKN, "1986", "Novel", "minor",
  genres=G("Comic Novel"),
  themes=T(IDENT, FAMILY, LANG),
  movements=M(SAL),
  overview="A short novel narrated by a Malgudi man known as the Talkative Man, published by Heinemann in "
  "London in 1986 and by Viking in New York in 1987; Kirkus called it 'really a long short story'.",
  content="The narrator's dealings with Dr. Rann, a smartly dressed stranger 'from Timbuctoo' who says he is "
  "working on a project for the United Nations, whose deserted wife comes looking for him, and whose courtship "
  "of the librarian's granddaughter the narrator tries to stop.",
  summary="The Talkative Man, a comfortable Malgudi resident who sends reports to the newspapers and earned "
  "his name, he says, because he 'cannot contain' himself, tells his story in a corner of the Boardless Hotel "
  "(Kirkus). In the library he meets an imposing stranger in a full suit, Dr. Rann, who says he comes from "
  "Timbuctoo and is engaged on a 'vital project' for the United Nations, and who eventually reveals that his work concerns a little weed that will eat up the world by the year 3000. "
  "Meanwhile a very large lady, an officer of the Home Guard in Delhi who carries a small pistol, holds the "
  "narrator for hours at the station with her story of faithless love: she is Rann's wife. The narrator must "
  "keep husband and wife apart and also prevent Rann's seduction of the librarian's granddaughter; after the "
  "tumult of Rann's public lecture a solution is found, and months later Mme Rann has the last word. A "
  "postscript by Narayan explains why he did not expand the story (Kirkus; Wikipedia).",
  themes_text="Imposture and the glamour of the foreign expert and his United Nations project; gossip and the "
  "compulsion to tell stories, embodied in the narrator; and the deserted wife's pursuit of her husband.",
  structure="First-person narration by the Talkative Man, told in the Boardless Hotel (Kirkus), followed by an "
  "author's postscript.",
  style="Garrulous, comic storytelling; Kirkus compared it with Isaac Bashevis Singer's shtetl tales.",
  ctx="The Talkative Man had narrated earlier Narayan stories (general knowledge); here he lives in Kabir "
  "Street, like the hero of the next novel, The World of Nagaraj (Mondal). Kirkus counted the book as the "
  "fifteenth Malgudi work.",
  sig="A late, slight novel, but its narrator reappears in the cast of The World of Nagaraj (Wikipedia), and "
  "the women's studies article counts its Sarasa among Narayan's women who choose a career for themselves.",
  chars="The Talkative Man; Dr. Rann; Rann's wife; the librarian; the librarian's granddaughter",
  canon="Minor canon",
  biblio="London: Heinemann, 1986; New York: Viking, 1987 (Contemporary Authors; Wikipedia gives the 1987 "
  "Library of Congress call number). Wikipedia's infobox also shows an Indian edition from Indian Thought "
  "Publications. Kirkus gives Viking and 1 February 1986.",
  notes="Not read. Contemporary Authors (Viking, 1987) and Kirkus (Viking, 1 February 1986) disagree on the "
  "American date; a Los Angeles Daily News review of 15 March 1987 (cited by Wikipedia) supports 1987. Plot "
  "details found only in reader reviews and blogs are not used.",
  ver="partially verified", sources=[KIRKUS, WIKI_NOVELS, CA, MONDAL, JIWS]),

W10("The World of Nagaraj", RKN, "1990", "Novel", "significant",
  genres=G("Comic Novel", "Domestic Fiction"),
  themes=T(FAMILY, LANG, MYTH),
  movements=M(SAL),
  overview="Narayan's fourteenth and last novel, published by Viking in New York in 1990. Nagaraj, a gentle, "
  "childless man of Kabir Street in Malgudi who keeps the books for a sari shop and has long planned a book on "
  "the sage Narada, finds his quiet life disturbed when his brother's wayward son, Tim, comes to live with "
  "him.",
  content="Nagaraj lives with his wife Sita and widowed mother in the family house, keeps accounts for "
  "Coomar's Boeing Sari Company and plans his book on Narada; Tim, son of his ambitious brother Gopu, leaves "
  "home and moves in, and his late nights and the smell of spirits about him bring turmoil into the house.",
  summary="Nagaraj's world is comfortable. He lives in his family's spacious house in Kabir Street with his "
  "wife, Sita, and his widowed mother, fills his day with letter-writing, coffee and keeping the books for his "
  "friend Coomar's Boeing Sari Company, and sits on his verandah planning the book he means to write on the "
  "life of the sage Narada. A mild man from a well-to-do family, he has no children and has grown fond of his "
  "elder brother Gopu's son, christened Krishnaji but known as Tim. When Tim leaves his ambitious, "
  "land-owning father and comes to live with his uncle, Nagaraj is forced to take responsibility for him; "
  "puzzled by the young man's secret late-night activities and by the strong smell of spirits that lingers "
  "behind him, he finds his days filled with unwelcome complications that threaten the calm of his world "
  "(Wikipedia, paraphrasing a publisher's description). Malgudi figures pass through: Jayaraj the "
  "photographer, who sleeps on a bench outside his shop at the Market archway for fear his lens will be stolen "
  "and is woken every day by Nagaraj; Kanni the betel-seller; an old, absent-minded priest; Bari the "
  "stationer; a drunken engineer; and the Talkative Man. Contemporary Authors calls it the tale of an "
  "easygoing townsman bedevilled by 'the dual trials of caring for his wayward nephew and trying to write a "
  "book about an obscure Indian saint'.",
  themes_text="Ambition and inertia: Nagaraj's unwritten book on Narada is a comic image of the unrealised "
  "life, and Mondal links the mythical Narada, compelled to pass on tales and news, to the storyteller of "
  "these late novels. Family duty: the childless uncle's responsibility for a rebellious nephew, and the "
  "strain between brothers. Settled habit and the young: Tim's nights and drinking disturb a household of "
  "fixed routines. Community: the gallery of Kabir Street and market characters.",
  structure="A comic narrative of domestic routine and its disruption; Mondal notes that it shares its "
  "pattern with Talkative Man, in which a comfortable Kabir Street man with literary ambitions has his peace "
  "disturbed by an outsider.",
  style="Gentle comedy and irony; Hanif Kureishi praised its superb irony and said Narayan was 'in control of "
  "all his subtle effects' (Contemporary Authors).",
  ctx="Published in 1990, when Narayan was eighty-three, as his last novel; Julian Moynahan's New York Times "
  "review called it his fourteenth. Narada, the wandering sage of Hindu myth who carries news between gods and "
  "men (general knowledge), gives Nagaraj his never-written subject.",
  sig="In Moynahan's phrase, the latest building block in 'a shining edifice', it closes the sequence of "
  "Malgudi novels Narayan began in 1935. Kureishi, reviewing it in the Observer, called Narayan 'a master' "
  "and urged readers of 'long, tediously clever' novels to think of 'the wisdom and humour Narayan gently "
  "slips into his small but luminous masterpieces'; Publishers Weekly found the Malgudi residents "
  "'talkative, philosophical and able to confront events with wonder and humor' (Contemporary Authors).",
  chars="Nagaraj; Sita; Nagaraj's mother; Gopu; Tim (Krishnaji); Coomar; Jayaraj; Kanni; the Talkative Man",
  biblio="New York: Viking, 1990 (Contemporary Authors). A London edition was reviewed in the Observer on 25 "
  "March 1990 but not identified; Penguin's paperback followed in 1991 (Wikipedia).",
  notes="Not read. Wikipedia's article is a stub whose plot paraphrases a publisher's description; Contemporary "
  "Authors' one-sentence summary agrees. Tim's fate and the ending were not checked.",
  ver="partially verified", sources=[WIKI_NOVELS, CA, MONDAL]),
]
