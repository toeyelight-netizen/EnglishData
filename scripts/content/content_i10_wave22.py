"""Installment 10, wave 23: J. D. Salinger, Jack Kerouac, Kurt Vonnegut and Grace Paley.

Four new authors and six works, one record per Norton selection.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

JS = "J. D. Salinger"
JK = "Jack Kerouac"
KV = "Kurt Vonnegut"
GP = "Grace Paley"

BEAT = "The Beat Generation"
POSTMOD = "Postmodernism and Postmodern Fiction"
FEM2 = "Second-Wave Feminist Writing"
BLACKHUM = "Black Humour and the Absurdist Novel"

W_SAL = "J. D. Salinger (Wikipedia)"
W_ESME = "For Esmé—with Love and Squalor (Wikipedia)"
W_KER = "Jack Kerouac (Wikipedia)"
W_OTR = "On the Road (Wikipedia)"
W_VON = "Kurt Vonnegut (Wikipedia)"
W_HB = "Harrison Bergeron (Wikipedia)"
W_S5 = "Slaughterhouse-Five (Wikipedia)"
W_PAL = "Grace Paley (Wikipedia)"
W_LSD = "Later the Same Day (Wikipedia)"
W_CONV = "A Conversation with My Father (Encyclopedia.com, Short Stories for Students)"

AUTHORS = [
A10(JS, MAJ, "1919", "2010", "New York City, New York, United States",
  "American; novelist and short-story writer writing in English",
  "American writer whose stories of adolescent alienation and of the Glass family - above all The Catcher in "
  "the Rye - made him the most influential and most reclusive American writer of the postwar decades",
  "Jerome David Salinger was born in Manhattan on 1 January 1919, the son of a Jewish importer of cheese and "
  "ham and a mother of Scots-Irish descent; he was educated at the McBurney School and at Valley Forge "
  "Military Academy, spent a year at New York University and studied briefly at Ursinus College and "
  "Columbia, where Whit Burnett's short-story course led to his first sale, 'The Young Folks', to Story in "
  "1940. He served in the US Army from 1942 to 1945, landed in Normandy on D-Day and was present at the "
  "liberation of a subcamp of Dachau, and his war experience is behind much of his fiction. 'A Perfect Day "
  "for Bananafish' (The New Yorker, 1948) began the Glass family sequence; The Catcher in the Rye (1951) "
  "made him famous; Nine Stories (1953), Franny and Zooey (1961) and Raise High the Roof Beam, Carpenters "
  "and Seymour: An Introduction (1963) followed, and 'Hapworth 16, 1924' (The New Yorker, 1965) was the "
  "last thing he published. He withdrew to Cornish, New Hampshire, avoided publicity for the rest of his "
  "life and died there on 27 January 2010.",
  "Fiction: The Catcher in the Rye (1951), Nine Stories (1953), Franny and Zooey (1961), Raise High the Roof "
  "Beam, Carpenters and Seymour: An Introduction (1963) and the uncollected 'Hapworth 16, 1924' (1965). "
  "Stories of the 1940s, some uncollected in his lifetime, are gathered in Three Early Stories (2014).",
  "A colloquial, idiomatic first-person voice that catches adolescent speech exactly; dialogue that carries "
  "almost all of the action; a habit of sudden religious or mystical intensity inside ordinary conversation; "
  "irony that turns to tenderness without warning; the recurring device of the child who is wiser than the "
  "adults around her.",
  "Adolescent alienation and the loss of innocence; the phoniness of adult society and the longing for "
  "authenticity; war, trauma and what Salinger called 'squalor'; the family as a religious community, above "
  "all in the Glass stories; Zen, Vedanta and Christian mysticism; the holiness of the child.",
  "Salinger is the writer through whom the American postwar adolescent found a voice, and The Catcher in the "
  "Rye is one of the most widely read and most frequently taught American novels of the century; his "
  "stories, particularly 'For Esmé' and the Glass sequence, are central to the criticism of the American "
  "short story, and his reclusiveness made him a cultural figure as well as a literary one.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Salinger and on 'For Esmé', read "
           "directly; they were not checked against a bibliography. Installment 10 records only the Norton "
           "selection, 'For Esmé—with Love and Squalor' (The New Yorker, 8 April 1950; Nine Stories, 1953); "
           "The Catcher in the Rye and the other books have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_SAL, W_ESME, NAAL]),
A10(JK, MAJ, "1922", "1969", "Lowell, Massachusetts, United States",
  "American; novelist, poet and diarist writing in English",
  "American novelist of the Beat Generation, whose spontaneous prose and road narratives - above all On the "
  "Road - made the cross-country journey the founding myth of postwar American counterculture",
  "Jean-Louis Lebris de Kérouac was born in Lowell, Massachusetts, on 12 March 1922 to French Canadian "
  "parents and grew up speaking joual, learning English at about six. He won a football scholarship to "
  "Columbia University, injured his leg, left without a degree, served in the merchant marine and the navy, "
  "and met Allen Ginsberg, William Burroughs and Neal Cassady in New York in the mid-1940s. The Town and "
  "the City (1950) was his first novel; On the Road, written in 1951 on a continuous roll of paper and "
  "published by Viking on 5 September 1957, made him famous. The Subterraneans (1958), The Dharma Bums "
  "(1958), Doctor Sax (1959), Maggie Cassidy (1959), Tristessa (1960), Lonesome Traveler (1960), Big Sur "
  "(1962), Visions of Gerard (1963), Desolation Angels (1965) and Vanity of Duluoz (1968) followed, with "
  "the poetry of Mexico City Blues (1959) and The Scripture of the Golden Eternity (1960). He drank "
  "heavily in his last years, lived with his mother and his third wife Stella Sampas, and died at St "
  "Petersburg, Florida, on 21 October 1969.",
  "Novels: The Town and the City (1950), On the Road (1957), The Subterraneans (1958), The Dharma Bums "
  "(1958), Doctor Sax (1959), Maggie Cassidy (1959), Tristessa (1960), Big Sur (1962), Visions of Gerard "
  "(1963), Desolation Angels (1965) and Vanity of Duluoz (1968), with the posthumous Visions of Cody (1972), "
  "The Sea Is My Brother (2011) and others. Poetry: Mexico City Blues (1959), The Scripture of the Golden "
  "Eternity (1960) and Book of Blues (1995).",
  "Spontaneous prose: long, paratactic sentences driven by breath and jazz rhythm, with dashes and colons "
  "instead of full stops; the deliberate refusal of revision in the manuscripts; a diction that mixes slang, "
  "Catholic devotional language, Buddhist terminology and French Canadian speech; the road, the car and the "
  "jazz club as recurring settings.",
  "The road, movement and the refusal of settled life; jazz, sex and intoxication as forms of ecstasy; "
  "friendship and the search for a father or a brother; Catholic and Buddhist mysticism; the American "
  "landscape, its small towns and its dispossessed; the sadness and exhaustion that follow the ecstasy.",
  "Kerouac is the central novelist of the Beat Generation and the writer who gave postwar American prose its "
  "most imitated style; On the Road is one of the defining American books of the 1950s, it has been "
  "continuously in print and taught as a document of the counterculture, and its manuscript roll is among "
  "the best-known objects in American literary history.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Kerouac and on On the Road, read "
           "directly, and from general knowledge; they were not checked against a bibliography. Installment "
           "10 records only the Norton selection, On the Road (Viking, 5 September 1957); the other novels "
           "and the poetry have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_KER, W_OTR, NAAL]),
]

AUTHORS += [
A10(KV, MAJ, "1922", "2007", "Indianapolis, Indiana, United States",
  "American; novelist, short-story writer and essayist writing in English",
  "American novelist and satirist whose dark comedies of technology, war and American optimism - Cat's "
  "Cradle, Slaughterhouse-Five - made him the most widely read counter-cultural novelist of the 1960s",
  "Kurt Vonnegut Jr. was born in Indianapolis on 11 November 1922, the son of an architect; he studied "
  "chemistry at Cornell, enlisted in the US Army in 1943, was captured in the Battle of the Bulge and was "
  "a prisoner of war in Dresden, where he survived the firebombing in February 1945 in an underground meat "
  "locker of a slaughterhouse - the experience behind Slaughterhouse-Five. He took an MA in anthropology at "
  "the University of Chicago, worked as a police reporter for the City News Bureau of Chicago and as a "
  "public-relations writer for General Electric, and began publishing stories in the Saturday Evening Post "
  "and the Magazine of Fantasy and Science Fiction. Player Piano (1952), The Sirens of Titan (1959), "
  "Mother Night (1961), Cat's Cradle (1963), God Bless You, Mr. Rosewater (1965), Slaughterhouse-Five "
  "(1969), Breakfast of Champions (1973), Slapstick (1976), Jailbird (1979), Deadeye Dick (1982), Galápagos "
  "(1985), Bluebeard (1987), Hocus Pocus (1990) and Timequake (1997) are the novels, with the stories of "
  "Canary in a Cathouse (1961) and Welcome to the Monkey House (1968), the play Happy Birthday, Wanda June "
  "(1970) and the essays of Palm Sunday (1981) and A Man Without a Country (2005). He died in New York on "
  "11 April 2007.",
  "Novels: Player Piano (1952), The Sirens of Titan (1959), Mother Night (1961), Cat's Cradle (1963), God "
  "Bless You, Mr. Rosewater (1965), Slaughterhouse-Five (1969), Breakfast of Champions (1973), Slapstick "
  "(1976), Jailbird (1979), Deadeye Dick (1982), Galápagos (1985), Bluebeard (1987), Hocus Pocus (1990) and "
  "Timequake (1997). Stories: Canary in a Cathouse (1961), Welcome to the Monkey House (1968), Bagombo Snuff "
  "Box (1999) and Complete Stories (2017). Non-fiction: Palm Sunday (1981), Fates Worse Than Death (1991), "
  "A Man Without a Country (2005) and Armageddon in Retrospect (2008).",
  "Short, flat, deadpan sentences and very short paragraphs, often of one line; a naive or helpless "
  "protagonist moved through events he cannot control; science-fiction devices (time travel, aliens, "
  "apocalypse) used as satire; recurring catchphrases ('So it goes'); diagrams, lists and drawings "
  "incorporated into the printed text; a sentimental and moralising voice underneath the irony.",
  "War and massacre, above all the bombing of Dresden; technology, automation and the degradation of work; "
  "American optimism, consumerism and the religion of success; free will and fatalism; religion invented and "
  "institutionalised (Bokononism); loneliness, family and the search for community; death, treated with "
  "irony and tenderness at once.",
  "Vonnegut is the most widely read American satirist of the postwar decades and, with Heller and Pynchon, "
  "one of the writers through whom the American postmodern novel is taught; Slaughterhouse-Five is a "
  "standard text of the anti-war literature of Vietnam-era America, has been adapted for film and stage and "
  "has never been out of print, and 'Harrison Bergeron' is one of the most widely anthologised American "
  "short stories, a set text in schools for the critique of enforced equality.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Vonnegut, 'Harrison Bergeron' and "
           "Slaughterhouse-Five, read directly; they were not checked against a bibliography. Installment 10 "
           "records only the two Norton selections - 'Harrison Bergeron' (The Magazine of Fantasy and Science "
           "Fiction, October 1961; Welcome to the Monkey House, 1968) and Slaughterhouse-Five (Delacorte, 31 "
           "March 1969); the other novels and the essays have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_VON, W_HB, W_S5, NAAL]),
A10(GP, MAJ, "1922", "2007", "New York City, New York, United States",
  "American; short-story writer, poet and political activist writing in English",
  "American short-story writer of the Bronx and Greenwich Village, whose talky, digressive, funny stories of "
  "mothers, fathers, neighbours and radicals made her the great miniaturist of American city life",
  "Grace Goodside was born in the Bronx, New York, on 11 December 1922, the daughter of Ukrainian Jewish "
  "immigrants who had come to the United States in 1906 and who spoke Russian and Yiddish at home; her "
  "father, Isaac Goodside, became a doctor. She dropped out of high school at sixteen, attended Hunter "
  "College for a year and studied poetry briefly with W. H. Auden at the New School, married the film "
  "cameraman Jess Paley in 1942 and had two children, and was active for the rest of her life in the "
  "feminist, anti-war and peace movements - she was a member of the War Resisters League and one of the "
  "founding members of the Greenwich Village Peace Center. The Little Disturbances of Man (1959), Enormous "
  "Changes at the Last Minute (1974) and Later the Same Day (1985) are the three collections, gathered as "
  "The Collected Stories (1994), which was a finalist for the Pulitzer Prize and the National Book Award; "
  "the poems are collected in Leaning Forward (1985) and Begin Again (2000), and the essays in Just As I "
  "Thought (1998). She taught at Columbia, Syracuse and the City College of New York, was Poet Laureate of "
  "Vermont from 2003, and died at Thetford, Vermont, on 22 August 2007.",
  "Stories: The Little Disturbances of Man (1959), Enormous Changes at the Last Minute (1974), Later the Same "
  "Day (1985) and The Collected Stories (1994). Poetry: Leaning Forward (1985) and Begin Again: Collected "
  "Poems (2000). Essays and interviews: Just As I Thought (1998) and Conversations with Grace Paley (1997).",
  "A talky, digressive, first-person or free indirect voice that reproduces the rhythms of New York speech; "
  "very short paragraphs and abrupt transitions; jokes, repetitions and direct addresses to the reader; "
  "stories that refuse conventional closure and often end in the middle of a conversation; a mixture of "
  "realism and metafictional experiment.",
  "Mothers, fathers, children and the ordinary labour of family life; the Bronx, Greenwich Village and the "
  "street as a community; Jewish immigrant inheritance; feminism, abortion, friendship between women; "
  "politics and activism, above all the anti-war and peace movements; storytelling itself, and the ethics "
  "of the stories we tell about other people.",
  "Paley is one of the most admired American short-story writers of the century and the model for a whole "
  "school of voice-driven American fiction; her three collections are small in number and enormous in "
  "influence, 'A Conversation with My Father' is among the most discussed American stories of the 1970s, "
  "and her combination of formal experiment with political commitment made her a central figure for "
  "feminist criticism.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Paley and on Later the Same Day, "
           "read directly, and from the Encyclopedia.com entry on 'A Conversation with My Father'. They were "
           "not checked against a bibliography. Installment 10 records only the two Norton selections - 'A "
           "Conversation with My Father' (New American Review, 1972; Enormous Changes at the Last Minute, "
           "1974) and 'Zagrowsky Tells' (Mother Jones, May 1985; Later the Same Day, 1985); the other "
           "collections, the poems and the essays have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_PAL, W_LSD, W_CONV, NAAL]),
]

WORKS = [
W10("For Esmé—with Love and Squalor", JS, "1950", "Short story", "major",
  genres=G("Short Story", "War Novel", "Realist Fiction"),
  themes=T("War, combat and its aftermath", "Childhood, adolescence and coming of age", "Memory, trauma and testimony"),
  movements=M("Late Modernism"),
  overview="A story published in The New Yorker on 8 April 1950 and collected in Nine Stories (1953): an "
           "American sergeant in Devon before D-Day meets a thirteen-year-old girl and her small brother, "
           "and a second episode in occupied Bavaria shows him recovering from a breakdown with her letter "
           "in his hands.",
  content="Two episodes joined by a frame: the narrator's refusal of a wedding invitation and his written "
          "notes on the bride, then the rainy afternoon in Devon in 1944 with Esmé and Charles, and then "
          "the scene in Bavaria after V-E Day in which Sergeant X, shattered by the war, opens a parcel "
          "posted almost a year earlier.",
  summary="The story opens with a wedding invitation the narrator cannot accept and his decision to send 'a "
          "few written notes' about the bride, whom he met nearly six years before. The first episode is "
          "Devon in 1944, on a stormy afternoon during the last weeks of training for the invasion: the "
          "narrator, a sergeant, walks into town, listens to a children's choir rehearsal in a church, and "
          "is struck by the 'melodious and unsentimental' singing of one girl of about thirteen. He takes "
          "shelter in a tearoom and finds her there with her little brother Charles and their governess. "
          "Esmé - orphaned, her father killed in North Africa, her mother dead - wears her father's "
          "oversized military wristwatch and talks to the lonely American with a composure beyond her "
          "years, asking him to write to her and telling him that she wants to be a 'cold person' and is "
          "trying to be 'more compassionate'. The second episode moves to Bavaria after V-E Day and shifts "
          "to the third person: Sergeant X has returned from a field hospital after a nervous breakdown, "
          "cannot sleep, cannot read, and is visited by 'Corporal Z' (Clay), who lectures him on the "
          "lessons of the war - 'God, I love a good soldier' - and shows no feeling for what X has been "
          "through. After Clay leaves, X opens his unopened mail and finds a small package from Devon "
          "posted nearly a year before: Esmé's letter, written in her careful hand, and her father's "
          "wristwatch - 'a talisman' - which she asks him to wear for the duration of the war. The story "
          "ends there, with X's hands trembling, and the last line of the story is the only comment on "
          "it.",
  themes_text="The story is about the damage war does to the capacity for feeling, and about the possibility "
              "of being brought back: Sergeant X's breakdown is described as a failure of the 'faculties' "
              "- he cannot sleep, read, feel or pray - and Esmé's gift works because it is disinterested, "
              "unsentimental and addressed to him as a person rather than as a soldier. The two episodes "
              "are also a study in the difference between 'love' and 'squalor': the title's terms are the "
              "story's argument, and the wedding-narrator's voice is the voice of a man who has recovered "
              "enough to be ironic. Salinger's decision to make the girl the moral centre, and to let her "
              "be neither saintly nor sentimental, is the story's most distinctive choice, and it belongs "
              "to his lifelong interest in the wisdom of children.",
  structure="A frame and two episodes: the invitation, the Devon afternoon and the Bavarian evening, with a "
            "deliberate shift from the first person to the third person and a change of the narrator's "
            "name to 'Sergeant X' between the episodes; the story withholds the union of the two until "
            "the parcel is opened, and its ending is a 'happy' ending that is also a diagnosis.",
  style="A precise, artfully casual first-person style in the framing sections, with long sentences that "
        "shift between irony and tenderness; dialogue that catches Esmé's careful, slightly formal speech "
        "and Charles's chatter; the third-person episode in Bavaria written in a flatter, more withdrawn "
        "register; the letter reproduced at the end in Esmé's own idiom, which is the story's emotional "
        "climax.",
  ctx="Published in The New Yorker on 8 April 1950, after being returned once and cut by six pages, and "
      "collected in Nine Stories (Little, Brown, 1953); Salinger had served in the 4th Infantry Division "
      "and landed on Utah Beach on D-Day, and the story was conceived as a tribute to veterans still "
      "suffering from what was then called battle fatigue. It is one of the earliest and most influential "
      "American treatments of combat trauma in fiction, and it belongs to the postwar American short story "
      "of the war, with the stories of Irwin Shaw and James Jones.",
  sig="Salinger's most admired story and one of the finest American short stories of the century; it is the "
      "story through which his war experience is usually discussed, it is a standard anthology text and a "
      "frequent set text on the literature of trauma, and its two-part structure and its shift of narrative "
      "person are regularly taught as a model of the modern short story's technique.",
  canon="Major canon",
  crit="Criticism reads the story as Salinger's most successful treatment of the war, as a study in the "
       "ethics of the gift and of the letter, and as a story about the possibility of recovery; its shift "
       "from 'I' to 'Sergeant X' has been much discussed as a way of dramatising dissociation, and its "
       "portrait of Esmé has divided critics between those who see a sentimental idealisation of the child "
       "and those who see a carefully unsentimental portrait. It is regularly compared with 'A Perfect Day "
       "for Bananafish', its companion in Nine Stories.",
  biblio="First published in The New Yorker, 8 April 1950; collected in Nine Stories (Boston: Little, Brown, "
         "1953), published in the United Kingdom as For Esmé—with Love and Squalor and Other Stories. A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows the published text as described in the "
        "sources consulted, and the quotations are short and were checked against more than one "
        "transcription.",
  ver="partially verified", sources=[W_ESME, W_SAL, NAAL]),
]

WORKS += [
W10("On the Road", JK, "1957", "Novel", "major",
  genres=G("Bildungsroman", "Autobiographical Novel", "Experimental Fiction"),
  themes=T("Counterculture, drugs and rebellion", "Land, place and regional belonging", "Identity, authenticity and the divided self"),
  movements=M(BEAT),
  overview="Published by Viking on 5 September 1957: Sal Paradise's account of his journeys across America in "
           "1947-50 with Dean Moriarty, a young ex-convict and car thief, in a book that made the road, the "
           "car and the jazz club the images of postwar American freedom.",
  content="Five parts, three of them road trips with Dean, moving from Paterson, New Jersey, to Denver, San "
          "Francisco, Los Angeles and Mexico City, and filled with the people Sal and Dean meet on the way - "
          "hitch-hikers, waitresses, farm workers, musicians, junkies and friends.",
  summary="Sal Paradise, a young writer living with his aunt in Paterson, New Jersey, has just finished a "
          "book and is recovering from a divorce when he meets Dean Moriarty, a wild, handsome, fast-talking "
          "young man from Denver who has spent time in reformatories and is newly married to a girl called "
          "Marylou. Part One follows Sal's first journey west in July 1947 - the buses and the "
          "hitch-hiking, the nights in Denver with Dean and their friend Carlo Marx, the ghost town of "
          "Central City, the job as a night watchman near San Francisco, the affair with Terry, a Mexican "
          "girl, and the cotton fields of California - and his return to New York. Part Two is the winter "
          "of 1948-49, when Dean arrives at Christmas with Marylou and the Dodge, and Sal, Dean and Marylou "
          "drive to New Orleans and on to San Francisco, where Dean abandons Sal for his wife Camille. Part "
          "Three is the spring of 1949: Sal in Denver, a trip to Mexico City, and Dean's arrival to take "
          "him to New York, where Sal meets the woman he calls 'the girl' and Dean leaves. Part Four is "
          "1950, the great journey to Mexico with Dean, Sal and the poet Remi Boncoeur, and Part Five is "
          "the return to New York and Dean's last, brief appearance before he goes back west. The book's "
          "famous scenes - the drive to the Mexican border, the jazz clubs of San Francisco and New York, "
          "the 'mad ones' speech - are held together by Dean's energy and by Sal's growing awareness that "
          "the freedom he admires is also a form of irresponsibility.",
  themes_text="The novel's subject is the pursuit of 'it' - ecstasy, authenticity, the next party, the next "
              "saxophone solo - and its discovery that the pursuit destroys the people who follow it. Dean "
              "is both the novel's hero and its casualty: he leaves wives and children behind, steals cars "
              "and ends the book in rags, and Sal's love for him does not prevent the reader from seeing "
              "the damage. The road is the novel's image of American possibility and of American "
              "restlessness, and its landscape - the plains, the Denver mountains, the Mexican desert - is "
              "described with a lyricism that gives the book its lasting power. Behind the freedom is a "
              "melancholy, Catholic and Buddhist at once, that becomes explicit in Kerouac's later books.",
  structure="Five parts of very unequal length, each corresponding to a journey or a period in Sal's life; "
            "the narrative is episodic and picaresque, held together by the recurrence of Dean and by the "
            "first-person voice; the prose is spontaneous, paratactic and run on with dashes and colons, "
            "and the book's chronology is deliberately approximate.",
  style="Kerouac's 'spontaneous bop prosody': long breathless sentences, strings of present participles, "
        "improvised lists of names and places, jazz-derived rhythms and repetitions; slang, profanity and "
        "Catholic devotional language side by side; a first-person narrator who is both inside and "
        "observing the action.",
  ctx="Written in April 1951 on a continuous roll of taped-together paper in a three-week burst, then "
      "revised for years and heavily edited by Viking's editors before publication on 5 September 1957; "
      "the book's characters are portraits of Kerouac, Neal Cassady, Allen Ginsberg, William Burroughs and "
      "others, and its publication made Kerouac the spokesman of the Beat Generation and was received as "
      "a scandal and a manifesto at once.",
  sig="The central novel of the Beat Generation and one of the defining American books of the 1950s; it "
      "named a youth culture, gave American prose a new speed and sound, has been continuously in print "
      "and widely taught since, and its manuscript roll is a canonical object of American literary history; "
      "it is the work through which the postwar counterculture and the road narrative are studied.",
  canon="Major canon",
  crit="Criticism has read the novel as a picaresque, as a spiritual autobiography, as a document of "
       "postwar masculinity and of the Beats' marginalisation of women, and as a formal experiment in "
       "spontaneous prose. Its portraits of Cassady and Ginsberg and its treatment of race, class and "
       "sexuality have been much discussed, and the relation of the published text to the 1951 manuscript "
       "roll (published as On the Road: The Original Scroll in 2007) has become a subject of its own.",
  biblio="Published by Viking Press (New York) on 5 September 1957; the original 1951 manuscript roll was "
         "published as On the Road: The Original Scroll (New York: Viking, 2007). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The novel was not read complete; the summary follows the published text as described in the "
        "sources consulted, and quotations are limited to well-known phrases. The Norton selection is "
        "printed as an extract, and the record is the whole novel.",
  ver="partially verified", sources=[W_OTR, W_KER, NAAL]),
W10("Harrison Bergeron", KV, "1961", "Short story", "significant",
  genres=G("Dystopian Fiction", "Satirical Fiction", "Science Fiction"),
  themes=T("Utopia, dystopia and imagined futures", "Power, the state and surveillance", "Identity, authenticity and the divided self"),
  movements=M(POSTMOD, "New Wave Science Fiction"),
  overview="A story published in The Magazine of Fantasy and Science Fiction in October 1961 and collected in "
           "Welcome to the Monkey House (1968): in 2081 the United States has made everyone equal by law, "
           "and a fourteen-year-old boy who refuses his handicaps is shot dead on live television.",
  content="A short story of some twelve hundred words set in 2081, in which George and Hazel Bergeron watch a "
          "television ballet, their son Harrison escapes from prison, seizes a studio and is killed by the "
          "Handicapper General, and his parents cannot remember what they have seen.",
  summary="The story opens with the sentence that has become its signature: 'The year was 2081, and everybody "
          "was finally equal.' The equality is enforced by constitutional amendment and by the Handicapper "
          "General, Diana Moon Glampers, whose agents fit the strong with weights, the beautiful with "
          "masks and the intelligent with radios that broadcast noises into their ears every twenty "
          "seconds. George Bergeron, who is intelligent and strong, wears a forty-seven-pound bag of "
          "birdshot around his neck and a radio in his ear; his wife Hazel is of perfectly average "
          "intelligence and needs no handicap. They are watching a ballet on television - the ballerinas "
          "are masked and weighted - when a bulletin announces that their son Harrison, fourteen years "
          "old, seven feet tall and burdened with three hundred pounds of handicaps, has escaped from "
          "prison. Harrison storms the studio, tears off his handicaps and the ballerina's, declares "
          "himself emperor, chooses the ballerina as his empress and dances with her to the musicians' "
          "'best' music. Diana Moon Glampers enters with a double-barrelled shotgun and kills them both; "
          "the television goes dark. George, who has left the room to get a beer, returns and asks Hazel "
          "why she has been crying; she says something sad happened on television but she cannot remember "
          "what it was.",
  themes_text="The story is a reductio ad absurdum of one reading of equality: a society that levels down "
              "every excellence to the lowest common denominator produces not justice but a numb, "
              "supervised mediocrity in which no one can think, feel or remember. Its satire is aimed at "
              "bureaucratic egalitarianism, and the story is regularly taught - and regularly contested - "
              "as an argument about equality and excellence; Vonnegut's own politics were egalitarian, and "
              "the story's target is more precisely the deadening of individuality by the state than "
              "equality as such. The ending, in which Hazel cannot remember her son's death, is the "
              "story's real horror: the handicaps have done their work on memory itself.",
  structure="A single continuous scene of a few pages, with no chapters or breaks, in which the television "
            "broadcast, the parents' conversation and Harrison's irruption are intercut; the story's time "
            "is compressed into an evening and its exposition is delivered through the broadcast and the "
            "narrator's flat commentary.",
  style="Short declarative sentences and very short paragraphs; a deadpan, faux-naive narrator who reports "
        "atrocity as ordinary fact; repeated phrases ('everybody was finally equal', 'that was the law') "
        "used as a refrain; dialogue in the flat idiom of television and bureaucracy; almost no metaphor, "
        "so that the few images (the birdshot bag, the shotgun) carry great weight.",
  ctx="Published in The Magazine of Fantasy and Science Fiction in October 1961 and collected in Welcome to "
      "the Monkey House (Delacorte, 1968); it belongs to Vonnegut's early period of magazine science "
      "fiction, written while he was working for General Electric and publishing in the slicks and the "
      "pulps, and it was adapted for television and film several times, most notably in the 1995 Showtime "
      "film.",
  sig="One of the most widely anthologised American short stories of the century and a standard school text "
      "on dystopia, equality and the state; its opening sentence is one of the best known in American "
      "fiction, and the story is a frequent point of reference in political argument about merit and "
      "levelling, which has made it both unusually influential and unusually contested.",
  canon="Major canon",
  crit="The story has been read as a satire of enforced egalitarianism, as a Cold War parable about "
       "conformity and as a metafictional joke about the reader's own desire for a level playing field; "
       "critics have debated whether its target is equality itself (a reading Vonnegut resisted) or the "
       "bureaucratic administration of equality, and its portrait of Hazel and of the ballerinas has been "
       "central to feminist and disability readings of the story.",
  biblio="First published in The Magazine of Fantasy and Science Fiction, October 1961; collected in Welcome "
         "to the Monkey House (New York: Delacorte Press, 1968). A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="Read through the text reproduced in anthologies and in the sources consulted; the quotations are "
        "short and were checked against more than one transcription.",
  ver="partially verified", sources=[W_HB, W_VON, NAAL]),
]

WORKS += [
W10("Slaughterhouse-Five", KV, "1969", "Novel", "major",
  genres=G("Postmodern Fiction", "Science Fiction", "War Novel"),
  themes=T("War, combat and its aftermath", "Death, illness and mourning", "Memory, trauma and testimony"),
  movements=M(POSTMOD, "Black Humour and the Absurdist Novel"),
  overview="Published by Delacorte on 31 March 1969, subtitled 'The Children's Crusade: A Duty-Dance with "
           "Death': the life of Billy Pilgrim, a prisoner of war in Dresden during the firebombing of 1945, "
           "who becomes 'unstuck in time' and is exhibited in a zoo on another planet, told in fragments by "
           "a narrator who is also a character.",
  content="Ten chapters and a first chapter about the writing of the book, moving without transition between "
          "Billy's childhood, his war, his optometry practice in Ilium, New York, his abduction by the "
          "Tralfamadorians, the death of his wife, the death of his son in Vietnam and the Dresden "
          "firestorm, with the phrase 'So it goes' following every death.",
  summary="The novel opens with a chapter in which 'I' - a narrator closely identified with Vonnegut - "
          "describes returning to Dresden in 1967 with his old war friend Bernard O'Hare, trying and "
          "failing for years to write a book about the firebombing, and beginning the book with the "
          "Children's Crusade and the famous first line 'All this happened, more or less.' The second "
          "chapter introduces Billy Pilgrim, an optometrist from Ilium, New York, who has come unstuck in "
          "time: he travels without warning between moments of his life, and the novel follows him through "
          "them. As a chaplain's assistant in 1944 he is captured in Luxembourg, survives the cattle cars, "
          "arrives in Dresden as a prisoner of war, and is working in a malt-syrup factory when the city "
          "is destroyed in February 1945; with the other prisoners he is put to work clearing the bodies. "
          "Later, abducted by the Tralfamadorians, he is kept in a zoo with the film star Montana "
          "Wildhack and learns their philosophy - that all moments exist simultaneously, that the dead "
          "are always alive in their own moments, and that the appropriate response to death is 'So it "
          "goes'. In the present of the novel's 1960s, Billy survives a plane crash, is nursed by his "
          "daughter, goes on television to tell the world about Tralfamadore, and is murdered in 1976 by "
          "Paul Lazzaro. The novel ends with the prisoners in Dresden and with the birdsong that follows "
          "the bombing, and with the narrator's acknowledgement that the book he has written is a failure "
          "and his son's war in Vietnam is not over.",
  themes_text="The novel's central subject is the firebombing of Dresden and the impossibility of writing "
              "about it: the first chapter is an essay on that impossibility, and the rest of the book "
              "answers it with a form that refuses chronology, causation and moral summary. Tralfamadorian "
              "time is the novel's device for expressing trauma - if all moments exist at once, then "
              "nothing is lost and nothing can be changed, and 'So it goes' is both consolation and "
              "evasion. The novel is also about the American war in Vietnam, about the slaughter of "
              "civilians in the name of the state, and about the 'children's crusade' that sends "
              "adolescents to die; its deadpan treatment of death has been read as a way of holding grief "
              "at arm's length and as a way of insisting on continuing to feel it.",
  structure="Ten chapters moving non-chronologically through Billy's life, with the narrator's own voice "
            "intruding in the first and last chapters and briefly in between; the Tralfamadorian "
            "episodes, the war, the optometrist's family life and the Dresden material are interleaved in "
            "short sections, so that the reader experiences time as Billy does. The book's fragments are "
            "held together by repeated phrases, by the refrain 'So it goes' and by the recurring image of "
            "the blue and ivory feet of the dead and dying.",
  style="Short, flat sentences and very short paragraphs; deadpan irony and a naively precise notation of "
        "detail; refrain and repetition used as structure; lists, songs and doggerel poems embedded in the "
        "text; a tone that moves from slapstick to sorrow within a paragraph, and a narrator whose "
        "sentimentality is offered without embarrassment.",
  ctx="Published by Delacorte Press on 31 March 1969 and dedicated to Mary O'Hare and Bernard V. O'Hare; "
      "Vonnegut had been a prisoner of war in Dresden and had worked for years on a book about it, visiting "
      "the city in 1967 with O'Hare. The novel appeared during the Vietnam War, was burned in a school "
      "board furnace in Drake, North Dakota, in 1973, and became one of the defining anti-war books of the "
      "American 1960s and 1970s; it was filmed by George Roy Hill in 1972.",
  sig="Vonnegut's masterpiece and one of the central American novels of the postwar period; it is a standard "
      "text on the literature of war and of trauma, on postmodern narrative and on the 1960s, it has never "
      "been out of print, and its first chapter is often taught as an essay on the ethics of writing "
      "history.",
  canon="Major canon",
  crit="Criticism reads the novel as a postmodern war narrative, as a trauma narrative whose form imitates "
       "dissociation, and as a satire of American optimism and of the conventions of science fiction; the "
       "function of Tralfamadore, the meaning of 'So it goes' and the relation of the narrator to Vonnegut "
       "are the central debates. Its censorship history, from the Drake school board to later challenges, is "
       "a standard case study in American book banning.",
  biblio="Published by Delacorte Press (New York) on 31 March 1969. A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The novel was not read complete; the summary follows the published text as described in the sources "
        "consulted, and quotations are limited to the best-known phrases. The Norton selection is printed "
        "as an extract, and the record is the whole novel.",
  ver="partially verified", sources=[W_S5, W_VON, NAAL]),
]

WORKS += [
W10("A Conversation with My Father", GP, "1972", "Short story", "major",
  genres=G("Short Story", "Metafictional Novel", "Domestic Fiction"),
  themes=T("Family, marriage and domestic life", "Art, the artist and the creative life", "Death, illness and mourning"),
  movements=M(FEM2, POSTMOD),
  overview="A story published in New American Review in 1972 and collected in Enormous Changes at the Last "
           "Minute (1974): a writer visits her dying father, who asks her to write a simple story, and the "
           "two versions she produces - one tragic, one open - become an argument about how fiction should "
           "end.",
  content="A short story in two movements, in which the unnamed daughter sits by her bedridden father's side "
          "and tells him the story of a woman and her drug-addicted son, twice: first as a conventional "
          "tragedy that the father approves of, and then as a story that refuses to end in tragedy, which "
          "the father rejects.",
  summary="The story begins with the father's request: 'I would like you to write a simple story just once "
          "more, the kind you used to write when you were a little girl.' He is old, ill with heart "
          "disease, and knows that he is dying; he lies in bed in his apartment with the curtains drawn, "
          "and his daughter, a writer in middle age, comes to sit with him and agrees. She invents a neighbour, a woman with a son who becomes a drug addict, and "
          "tells the story with the ending the father wants - the son dies, the woman is destroyed, "
          "everything is tragic and complete. The father is pleased. But the narrator is not satisfied, "
          "and she tells the story again: this time the son survives, the mother learns to live with him, "
          "and the story ends not with a death but with a possibility. The father rejects the second "
          "version as 'not a story' - it does not end, it does not conclude, it does not tell the truth "
          "about life. Their conversation moves between the two versions and between their two ideas of "
          "what a story is for: the father holds that a story must acknowledge tragedy, face death and "
          "end, while the daughter holds that a story may leave its people alive and its ending open, and "
          "that a life is not improved by being made into a conclusion. The father's illness is present "
          "throughout, since the story's occasion is the fact that he is dying, and the argument about "
          "fiction is also an argument about how to face that. The story ends with the father's reproach "
          "and the daughter's unresolved reply.",
  themes_text="The story is about the difference between two kinds of truth: the father's, which demands "
              "that art acknowledge tragedy and conclude, and the daughter's, which refuses to close "
              "experience off and insists that a story may leave its people alive. Around that argument "
              "gathers the story's other subjects - the relation of a daughter to a dying father, the "
              "ethics of using real people in fiction (the narrator's story is invented, but the "
              "conversation is not), and the feminist critique of narrative form, since the closed, "
              "tragic ending is associated with the father and the open one with the daughter. Paley's "
              "preface to Enormous Changes - 'Everyone in this book is imagined into life except the "
              "father. No matter what story he has to live in, he's my father' - is the story's own "
              "frame.",
  structure="A frame conversation with two embedded narratives: the father's request, the first version of the "
            "story, the father's approval, the second version, and the father's rejection, with the "
            "narrator's commentary between them; the story's movement is dialectical rather than "
            "plot-driven, and it ends in disagreement rather than resolution.",
  style="A talky, conversational first-person voice with short paragraphs and abrupt transitions; dialogue "
        "in which the father's old-world idiom and the daughter's modern one are sharply distinguished; "
        "direct address and repetition; the embedded stories told in a plainer style than the frame, so "
        "that the difference between them is audible.",
  ctx="Published in New American Review in 1972 and collected in Enormous Changes at the Last Minute "
      "(Farrar, Straus and Giroux, 1974); the father is Paley's own father, Isaac Goodside, a doctor, and "
      "the story belongs to the feminist experimental fiction of the early 1970s and to the tradition of "
      "metafictional stories about storytelling that runs from Sterne through Borges to Barth.",
  sig="Paley's most discussed story and one of the central American short stories of the 1970s; it is a "
      "standard text in courses on metafiction, on the short story and on American women's writing, and it "
      "is one of the clearest statements in postwar American fiction of the argument that narrative form is "
      "a political and ethical choice.",
  canon="Major canon",
  crit="Criticism has read the story as metafiction, as a feminist critique of closure, as a study in "
       "mourning and as Paley's ars poetica; the two versions of the story-within-the-story are regularly "
       "analysed as models of the tragic and the open ending, and the father's demand for a simple story "
       "has been discussed in relation to the immigrant parent's relation to American realism.",
  biblio="First published in New American Review in 1972; collected in Enormous Changes at the Last Minute "
         "(New York: Farrar, Straus and Giroux, 1974) and in The Collected Stories (New York: Farrar, Straus "
         "and Giroux, 1994). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows the published text as described in the "
        "sources consulted, and the quotations are the best-known lines.",
  ver="partially verified", sources=[W_CONV, W_PAL, NAAL]),
W10("Zagrowsky Tells", GP, "1985", "Short story", "significant",
  genres=G("Short Story", "Domestic Fiction", "Metafictional Novel"),
  themes=T("Race, racism and the struggle for civil rights", "Family, marriage and domestic life", "Memory, trauma and testimony"),
  movements=M(FEM2),
  overview="A story published in Mother Jones in May 1985 and collected in Later the Same Day the same year: "
           "an elderly Jewish pharmacist in the Bronx, talking to the narrator on a park bench, defends "
           "himself against the charge of racism by telling the story of his daughter, his grandson and "
           "the Black woman who bore him.",
  content="A single monologue - Zagrowsky's account, punctuated by the narrator's brief questions and "
          "corrections - in which the pharmacist remembers his daughter's breakdown, the child she had "
          "with a Black man, the family's refusal of the child, and his own late, grudging love for his "
          "grandson.",
  summary="The story is spoken almost entirely by Mr. Zagrowsky, a retired pharmacist who runs into the "
          "narrator, Faith, in a park and begins to talk. He is aggrieved: he has been accused of racism "
          "by the Black and Puerto Rican customers of his pharmacy, and he wants to explain himself. His "
          "explanation is a family history - his daughter Eileen, who had a breakdown and spent years in "
          "and out of hospitals; the child she had with a Black man, who was left to her parents to raise; "
          "his wife's refusal to accept the child; and his own slow, unwilling, and finally absolute love "
          "for the boy, whom he calls his grandson and whose name he says with pride. The story's action "
          "is entirely in the telling: Zagrowsky reveals, without ever admitting it, that his own life "
          "has been changed by exactly the people he thinks he is defending himself against, and the "
          "narrator's few interjections show that she is hearing something other than what he means to "
          "say. The story ends with him still talking, unrepentant and, in spite of himself, moving.",
  themes_text="The story is about the gap between a man's opinions and his life: Zagrowsky's talk is full of "
              "racial insult and self-pity, and his actions - taking in his mixed-race grandson, raising "
              "him, loving him - contradict everything he says. Paley's method is to let him condemn "
              "himself out of his own mouth and then to let the reader see what he cannot see: that he "
              "has already been changed. The story is also about the ethics of the storyteller, since "
              "the narrator is a writer listening for material, and about the Bronx as a place where "
              "ethnic and racial groups live close together and talk past one another.",
  structure="A dramatic monologue with a thin frame: Zagrowsky speaks for almost the whole story, and the "
            "narrator's presence is registered in brief questions, reported gestures and occasional "
            "corrections; the story has no plot in the conventional sense, only the gradual unfolding of "
            "a family history through the speaker's resistance to it.",
  style="Paley's reproduced Bronx speech: run-on sentences, repetitions, self-interruptions, insults, "
        "direct address ('You know what I'm saying?'), and sudden turns into tenderness; the narrator's "
        "voice is much quieter, so that the contrast between the two is part of the story's meaning.",
  ctx="Published in Mother Jones in May 1985 and collected in Later the Same Day (Farrar, Straus and Giroux, "
      "1985); Zagrowsky had appeared in Paley's earlier story 'The Used-Boy Raisers' and Faith Darwin is "
      "the semi-autobiographical character who recurs across her collections; the story belongs to the "
      "New York Jewish fiction of the 1980s and to the feminist short story of the same years.",
  sig="One of Paley's most admired late stories and a standard example of the American dramatic monologue in "
      "fiction; it is the story through which her late style and her treatment of race and ethnicity are "
      "usually discussed, and its method - letting a bigoted speaker reveal his own transformation - is "
      "frequently taught as a model of indirect characterisation.",
  canon="Secondary canon",
  crit="Criticism reads the story as a study in the ethics of letting a character speak, and as one of the "
       "few American stories of its period to treat a white ethnic character's racism through his own "
       "family history; the relation between Zagrowsky's speech and his actions is the central topic, and "
       "the story is often compared with Paley's earlier 'The Used-Boy Raisers' and with the Faith Darwin "
       "stories around it.",
  biblio="First published in Mother Jones, May 1985; collected in Later the Same Day (New York: Farrar, "
         "Straus and Giroux, 1985) and in The Collected Stories (1994). A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows the published text as described in the sources "
        "consulted, and the quotations are limited to characteristic phrases rather than exact lines.",
  ver="partially verified", sources=[W_LSD, W_PAL, NAAL]),
]
