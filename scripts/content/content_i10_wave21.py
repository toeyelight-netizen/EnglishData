"""Installment 10, wave 22: Saul Bellow, Arthur Miller and Robert Lowell.

Three new authors and eight works. Lowell's "The Quaker Graveyard in Nantucket" was first printed in
the Partisan Review for Spring 1945, so it is before the period and is not recorded; the other seven
Norton selections are recorded one by one.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

SB = "Saul Bellow"
AM = "Arthur Miller"
RL = "Robert Lowell"

CONF = "Confessional Poetry"
LATE = "Late Modernism"
JEWAM = "Jewish American Fiction"
DEATHOF = "Death and the afterlife"

W_BEL = "Saul Bellow (Wikipedia)"
W_BELBIB = "Bibliography of Saul Bellow (Wikipedia)"
W_BELGREEN = "Analysis of Saul Bellow's Looking for Mr Green (Literary Theory and Criticism)"
W_MIL = "Arthur Miller (Wikipedia)"
W_DOS = "Death of a Salesman (Wikipedia)"
W_LOW = "Robert Lowell (Wikipedia)"
W_LIFE = "Life Studies (Wikipedia)"
W_SKUNK = "Skunk Hour (Wikipedia)"
W_FUD = "For the Union Dead (Wikipedia)"
W_QG = "The Quaker Graveyard in Nantucket (Wikipedia)"
W_LWC = "Lord Weary's Castle (Wikipedia)"
W_PR45 = "Partisan Review, Vol. XII, No. 2 (Spring 1945), table of contents (Boston University)"

AUTHORS = [
A10(SB, MAJ, "1915", "2005", "Lachine, Quebec, Canada",
  "Canadian-born American; novelist, short-story writer, essayist and playwright writing in English",
  "Canadian-born American novelist and Nobel laureate whose picaresque, intellectually restless fiction - "
  "Augie March, Herzog, Humboldt's Gift - made the immigrant city and the arguing mind the subject of "
  "postwar American prose",
  "Saul Bellow was born Solomon Bellows at Lachine, Quebec, on 10 June 1915, the son of Russian Jewish "
  "immigrants from Saint Petersburg, and grew up in the Humboldt Park district of Chicago after the family "
  "moved there in 1924. He studied at the University of Chicago and took a BA in anthropology at "
  "Northwestern University in 1937, worked briefly as a teacher and editor, served in the merchant marine "
  "in the Second World War, and taught at the University of Minnesota, Boston University, the University of "
  "Chicago and elsewhere. Dangling Man (1944), The Victim (1947), The Adventures of Augie March (1953, "
  "National Book Award), Seize the Day (1956), Henderson the Rain King (1959), Herzog (1964, National Book "
  "Award), Mr. Sammler's Planet (1970, National Book Award), Humboldt's Gift (1975, Pulitzer Prize) and "
  "The Dean's December (1982) are the novels, with the stories of Mosby's Memoirs (1968), Him with His Foot "
  "in His Mouth (1984) and Collected Stories (2001). He was awarded the Nobel Prize in Literature in 1976, "
  "the only writer to win the National Book Award for Fiction three times, and died at Brookline, "
  "Massachusetts, on 5 April 2005.",
  "Novels: Dangling Man (1944), The Victim (1947), The Adventures of Augie March (1953), Seize the Day "
  "(1956), Henderson the Rain King (1959), Herzog (1964), Mr. Sammler's Planet (1970), Humboldt's Gift "
  "(1975), The Dean's December (1982), More Die of Heartbreak (1987), A Theft (1989), The Bellarosa "
  "Connection (1989), Ravelstein (2000). Stories: Mosby's Memoirs and Other Stories (1968), Him with His "
  "Foot in His Mouth (1984), Something to Remember Me By (1991) and Collected Stories (2001). "
  "Non-fiction: To Jerusalem and Back (1976) and It All Adds Up (1994).",
  "A voluble, energetic, digressive prose that mixes high argument with the slang of the Chicago streets; "
  "first-person narrators who talk their way through experience; long sentences with a comic and "
  "rhapsodic swell; sudden shifts from philosophy to farce; a gift for the monologue of the self-educated "
  "immigrant.",
  "The immigrant city and the American promise; the argument between the intellectual and the practical "
  "life; Jewish identity, the Holocaust and the moral inheritance of the diaspora; love, marriage and the "
  "comedy of sexual entanglement; money, ambition and the illusions of success; death and the search for "
  "transcendence in a secular age.",
  "Bellow is the central American novelist of the postwar decades and the writer through whom the Jewish "
  "American novel became a national literature; his Nobel Prize in 1976 confirmed a reputation built on "
  "Augie March and Herzog, and his prose - its energy, its learning and its emotional range - is the "
  "standard against which Philip Roth, Malamud, Ozick and a generation of successors are measured.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Bellow and on his bibliography, read "
           "directly, and from general knowledge; they were not checked against a bibliography. Installment "
           "10 records only the Norton selection, 'Looking for Mr. Green' (Commentary, March 1951; collected "
           "in Mosby's Memoirs and Other Stories, 1968); the novels and the other stories have no records, so "
           "the bibliography is incomplete.",
  ver="partially verified", sources=[W_BEL, W_BELBIB, NAAL]),
A10(AM, MAJ, "1915", "2005", "New York City, New York, United States",
  "American; playwright, essayist and screenwriter writing in English",
  "American playwright whose tragedies of the ordinary man - above all Death of a Salesman, All My Sons and "
  "The Crucible - made him, with Tennessee Williams, the defining dramatist of the postwar American stage",
  "Arthur Asher Miller was born in Harlem, New York, on 17 October 1915, the son of a Polish Jewish "
  "manufacturer; the family lost its business in the crash of 1929 and moved to Brooklyn, and Miller worked "
  "in a warehouse and for a radio station before taking a BA at the University of Michigan in 1938, where "
  "he won the Hopwood Award twice. The Man Who Had All the Luck (1944) failed on Broadway; All My Sons "
  "(1947) established him, and Death of a Salesman opened at the Morosco Theatre on 10 February 1949, ran "
  "for 742 performances and won the Pulitzer Prize for Drama. The Crucible (1953), a play about the Salem "
  "witch trials written against McCarthyism, A View from the Bridge (1955), A Memory of Two Mondays (1955), "
  "After the Fall (1964), Incident at Vichy (1964), The Price (1968), The Creation of the World and Other "
  "Business (1972) and Playing for Time (1980) followed, with the screenplays of The Misfits (1961) and "
  "others, the reportage of Situation Normal (1944) and the essays and memoir Timebends (1987). He refused "
  "to name names before the House Un-American Activities Committee in 1956 and was convicted of contempt of "
  "Congress, a conviction overturned in 1958; he was married to Marilyn Monroe from 1956 to 1961. He died "
  "at Roxbury, Connecticut, on 10 February 2005, the fifty-sixth anniversary of the premiere of Death of a "
  "Salesman.",
  "Plays: The Man Who Had All the Luck (1944), All My Sons (1947), Death of a Salesman (1949), An Enemy of "
  "the People (1950, adaptation of Ibsen), The Crucible (1953), A View from the Bridge (1955), A Memory of "
  "Two Mondays (1955), After the Fall (1964), Incident at Vichy (1964), The Price (1968), The Creation of "
  "the World and Other Business (1972), The Archbishop's Ceiling (1977), The American Clock (1980), Playing "
  "for Time (1980), Broken Glass (1994) and Resurrection Blues (2002). Screenplays: The Misfits (1961) and "
  "Everybody Wins (1990). Prose: Situation Normal (1944), Focus (1945, novel), The Misfits (1961, novella), "
  "In Russia (1969), In the Country (1977), 'Salesman' in Beijing (1984) and Timebends (1987, memoir).",
  "Plain, muscular, colloquial dialogue that rises to a rhetorical and sometimes lyrical intensity; "
  "monologues and confessional arias set against short, hard exchanges; a dramaturgy of memory in which "
  "past and present occupy the same stage; realistic sets used as memory-spaces; the language of the "
  "salesman, the immigrant and the working man made tragic.",
  "The American Dream and its collapse; the failure of fathers and the disappointment of sons; the ordinary "
  "man as tragic hero; guilt, betrayal and the corruption of the past; McCarthyism, informers and the "
  "tyranny of the community; the immigrant family and social mobility; time, memory and the refusal to "
  "accept one's own life.",
  "Miller is, with Williams, the major American dramatist of the postwar decades, and Death of a Salesman is "
  "the play through which American tragedy after 1945 is usually taught: it won the Pulitzer Prize, ran for "
  "742 performances, has been revived on Broadway repeatedly, has been filmed ten times and has sold some "
  "eleven million copies, and its Willy Loman became the representative figure of the ordinary man in "
  "modern drama.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Miller, read directly, and from "
           "general knowledge; they were not checked against a bibliography. Installment 10 records only the "
           "Norton selection, Death of a Salesman (1949); the other plays, the screenplays and the prose have "
           "no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_MIL, W_DOS, NAAL]),
A10(RL, MAJ, "1917", "1977", "Boston, Massachusetts, United States",
  "American; poet, translator, playwright and teacher writing in English",
  "American poet and the central figure of confessional poetry, whose formal Catholic verse of the 1940s gave "
  "way to the autobiographical free verse of Life Studies and to a public poetry of history and civil "
  "rights",
  "Robert Traill Spence Lowell IV was born in Boston on 1 March 1917 into a Boston Brahmin family descended "
  "from the Mayflower; his father was a naval commander and his mother a Winslow. He studied at Harvard, "
  "left to study with Allen Tate and John Crowe Ransom, and took a BA at Kenyon College in 1940, "
  "converting to Catholicism in 1941 and refusing military service in the Second World War - he served "
  "five months in prison as a conscientious objector in 1943. Land of Unlikeness (1944), Lord Weary's "
  "Castle (1946, Pulitzer Prize), The Mills of the Kavanaughs (1951), Life Studies (1959, National Book "
  "Award), Imitations (1961), For the Union Dead (1964), Near the Ocean (1967), Notebook 1967-68 (1969), "
  "The Dolphin (1973, Pulitzer Prize), History (1973) and Day by Day (1977) are the books, with the "
  "verse translations and the plays of The Old Glory (1965). He taught at Boston University, where his "
  "students included Sylvia Plath and Anne Sexton, was Consultant in Poetry to the Library of Congress in "
  "1947-48, and died in New York on 12 September 1977.",
  "Poetry: Land of Unlikeness (1944), Lord Weary's Castle (1946), The Mills of the Kavanaughs (1951), Life "
  "Studies (1959), Imitations (1961), For the Union Dead (1964), Near the Ocean (1967), Notebook 1967-68 "
  "(1969), Notebook (1970), The Dolphin (1973), History (1973) and Day by Day (1977), with Collected Poems "
  "(2003, ed. Frank Bidart and David Gewanter). Plays: The Old Glory (1965). Prose: Collected Prose (1987). "
  "Translations: Phaedra (1961), Imitations (1961) and Prometheus Bound (1969).",
  "A dense, allusive, heavily stressed formal verse in the early books, with violent imagery, enjambment "
  "and an unusual mixture of pentameter and trimeter; from Life Studies a loose, conversational free verse "
  "and irregular stanza that keeps the rhythm of speech; rhyme used sparingly and often ironically; a "
  "rhetoric that moves between the private and the public within a single poem.",
  "History and the American past, above all the Puritan inheritance, the Civil War and the Second World "
  "War; family, ancestry and the decline of the Boston Brahmins; mental illness, hospital and "
  "confinement; marriage, divorce and the betrayals of the intimate life; Catholicism, guilt and the "
  "possibility of grace; the modern city, civil rights and the corruption of public memory.",
  "Lowell is the most influential American poet of the postwar era: Life Studies changed what American "
  "poetry was permitted to say about the self, and his teaching at Boston University made him the centre of "
  "the confessional generation; his public poems of the 1960s, above all 'For the Union Dead', are the "
  "central American examples of the poetry of history, and his letters and drafts are among the most "
  "studied documents of modern poetry.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Lowell, Life Studies, For the Union "
           "Dead and Lord Weary's Castle, read directly, and from general knowledge; they were not checked "
           "against a bibliography. Installment 10 records six Norton selections - 'Mr. Edwards and the "
           "Spider' (Poetry, 1946; Lord Weary's Castle, 1946), 'Skunk Hour' and 'Memories of West Street and "
           "Lepke' (Partisan Review, January 1958; Life Studies, 1959), 'Night Sweat' and 'For the Union "
           "Dead' (For the Union Dead, 1964) and 'The Quaker Graveyard in Nantucket' is excluded because its "
           "first printing was in the Partisan Review for Spring 1945. The other books have no records, so "
           "the bibliography is incomplete.",
  ver="partially verified", sources=[W_LOW, W_LIFE, W_SKUNK, W_FUD, W_QG, W_LWC, W_PR45, NAAL]),
]

WORKS = [
W10("Looking for Mr. Green", SB, "1951", "Short story", "significant",
  genres=G("Short Story", "Realist Fiction", "Social Criticism"),
  themes=T("The city, the suburb and modern space", "Race, racism and the struggle for civil rights", "Class, labour and social mobility"),
  movements=M(LATE, JEWAM),
  overview="A story first published in Commentary in March 1951 and collected in Mosby's Memoirs and Other "
           "Stories (1968): George Grebe, a classics graduate reduced to relief work in Depression Chicago, "
           "spends a day trying to deliver a welfare cheque to a man named Tulliver Green in a Black "
           "neighbourhood he does not know.",
  content="A single day's narrative in which Grebe takes over a colleague's caseload, walks the South Side "
          "streets with a list of names, is mocked, threatened and befriended by the people he asks, and "
          "ends the day without having found his man, having learned something about the limits of his own "
          "competence.",
  summary="George Grebe is a slight, scholarly man of about thirty-five who has a degree in classics, no job "
          "to match it, and a temporary post with the relief administration; he is given a district he has "
          "never worked and a batch of cheques, among them one for Tulliver Green, who cannot be found. The "
          "story follows him through one day in a poor Black neighbourhood of Chicago: he climbs tenement "
          "stairs, knocks on doors, consults a janitor, is directed to a basement church, is taken for a "
          "policeman or a rent collector, and meets a series of people - a woman who wants to sell him "
          "something, a man who lectures him on the race question, a preacher, a boy who offers to guide "
          "him - each of whom has his own relation to the missing man and to the money. Grebe, whose "
          "classical education and good manners are both useless and a kind of protection, keeps trying to "
          "do his job properly and keeps being told that he cannot understand the place he is in. By the "
          "end of the day he has not found Green, and the cheque goes back into his pocket; the story's "
          "last movement is his recognition that the city has defeated his methods and that the man he was "
          "looking for may not want to be found.",
  themes_text="The story is about the collision between bureaucratic good will and a world it cannot see: "
              "Grebe's decency is real and his competence is not, and Bellow uses the delivery of a relief "
              "cheque to expose the distance between the welfare state's categories and the lives it "
              "administers. Its treatment of race is of its moment and has been criticised since: the "
              "neighbourhood is rendered as a labyrinth of unfamiliar speech and evasion, and the story "
              "does not give its Black characters the interiority it gives Grebe. What remains powerful is "
              "the portrait of a man whose education has not prepared him for anything and whose work "
              "requires a knowledge of the city that no book supplies.",
  structure="A single continuous narrative, close to Grebe's point of view and ordered by the sequence of "
            "addresses and encounters rather than by plot; the day's structure is picaresque, one door "
            "after another, and the story withholds the meeting its title promises, ending on an "
            "unresolved errand.",
  style="Bellow's early realism: exact notation of streets, stairs, smells and accents; dialogue rendered in "
        "the cadences of the neighbourhood; a third person that stays close to Grebe's educated, slightly "
        "fastidious consciousness; an epigraph from Ecclesiastes set against the day's futility.",
  ctx="Published in Commentary in March 1951, in the years when Bellow was teaching at the University of "
      "Minnesota and writing The Adventures of Augie March, and collected in Mosby's Memoirs and Other "
      "Stories (Viking, 1968); its Depression Chicago, the relief administration and the South Side belong "
      "to the city of Bellow's childhood and to his first attempts at the picaresque novel of American "
      "urban life.",
  sig="One of Bellow's best early stories and the one most often anthologised from his first phase; it is a "
      "standard text for the study of the American urban story of the 1950s and of Bellow's Chicago, and it "
      "anticipates the energetic first-person narration that Augie March would make his signature.",
  canon="Secondary canon",
  crit="Criticism reads the story as a study in the ethics of help and as an early treatment of race in "
       "Bellow's work; readers have been divided over whether its rendering of the Black neighbourhood is "
       "an honest record of a white observer's blindness or a limitation of the story itself, and the "
       "Ecclesiastes epigraph has been central to accounts of its argument about work and futility.",
  biblio="First published in Commentary, March 1951; collected in Mosby's Memoirs and Other Stories (New "
         "York: Viking Press, 1968) and in Collected Stories (New York: Viking, 2001). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows the published text as described in the "
        "critical account cited and in Bellow's bibliography, and the quotations are limited to the "
        "epigraph and to well-known phrases.",
  ver="partially verified", sources=[W_BELGREEN, W_BELBIB, NAAL]),
W10("Death of a Salesman", AM, "1949", "Play (two acts and a requiem)", "major",
  genres=G("Modern Tragedy", "Domestic Drama", "Full-Length Play"),
  themes=T("Class, labour and social mobility", "Family, marriage and domestic life", "Identity, authenticity and the divided self"),
  movements=M(LATE),
  overview="The play that opened on Broadway on 10 February 1949: Willy Loman, a sixty-year-old travelling "
           "salesman who has spent his life believing in the American Dream, is fired, quarrels with his "
           "sons, revisits his memories and kills himself so that his family can collect the insurance.",
  content="Two acts and a requiem, set in the Lomans' Brooklyn house and in Willy's memories of Boston and "
          "of the road, in which the failure of a salesman's career and the failure of his sons' lives "
          "unfold through a montage of present scenes, flashbacks and hallucinations.",
  summary="Willy Loman comes home late at night with his suitcases, having failed to drive to New England; his "
          "wife Linda persuades him to ask his boss Howard for a job in New York, and the couple talk about "
          "their sons, Biff, thirty-four, who has drifted through the West doing farm work, and Happy, who "
          "has a job and an apartment and no satisfaction. In the boys' bedroom Biff and Happy remember "
          "their father's ambitions for them and Biff's high-school glory as a football player, ended when "
          "he failed mathematics and did not graduate; Willy, overhearing, is angry and then hopeful when "
          "Biff says he will see a former employer, Bill Oliver, about a business loan. The second act "
          "takes Willy to Howard's office, where he is humiliated, told to take a rest and fired; Biff's "
          "interview with Oliver fails and he steals a fountain pen; at Charley's office Willy meets "
          "Bernard, the swot of Biff's schooldays, now a successful lawyer, and Charley offers him a job "
          "that Willy refuses. In the restaurant where the family meet, Biff tries to tell the truth about "
          "himself and Willy, unable to bear it, retreats into the memory of the day in Boston when Biff "
          "found him with a woman and called him a fake - the moment that broke the boy's belief in him. "
          "At home the quarrel ends with Biff's tearful admission that they are ordinary men and Willy's "
          "sudden conviction that his son loves him; then Willy, talking to the ghost of his brother Ben, "
          "decides that his life insurance, twenty thousand dollars, is worth more than his life. He drives "
          "away and crashes the car. The requiem is the funeral, poorly attended; Linda, who has made the "
          "last payment on the house, cannot understand why Willy did it, and asks the empty air 'We're "
          "free'.",
  themes_text="The play's subject is the American Dream as a system of belief that destroys the man who keeps "
              "faith with it: Willy's conviction that being 'well liked' is the key to success, his "
              "investment in his sons' popularity and athletic glory, and his inability to accept that he "
              "has failed all belong together, and Miller makes the salesman's vocabulary - being "
              "well-liked, being a big man, having contacts - into a tragic idiom. Its second subject is "
              "fatherhood and inheritance: Biff's theft, his drift and his final refusal to lie are a "
              "judgment on his father's values, and Happy's decision to follow Willy's path completes the "
              "cycle. The play's third subject is memory: Willy's flashbacks are not nostalgia but an "
              "effort to live in a past where his sons still promised something, and the staging, which "
              "lets past and present occupy the same set, makes that effort the play's form.",
  structure="Two acts and a requiem, played without scene changes on a single set of the frame house, with "
            "the actors' movement into and out of the lit areas making the transitions; time is not "
            "linear, since Willy's memories and hallucinations invade the present action; the play's "
            "climax is internal, a decision made in solitude, and the requiem is a coda in which the "
            "survivors try to make sense of it.",
  style="A colloquial, rhythmical American speech - the salesman's patter, the immigrant's malapropism, the "
        "kitchen quarrel - that becomes lyrical in Willy's monologues; short exchanges and overlapping "
        "dialogue; the expressionist devices of light, music and half-transparent walls; a tone that "
        "moves between pathos and comedy without letting either settle.",
  ctx="First performed at the Morosco Theatre, New York, on 10 February 1949, directed by Elia Kazan, with "
      "Lee J. Cobb as Willy, Mildred Dunnock as Linda and Arthur Kennedy as Biff; it won the Pulitzer Prize "
      "for Drama and the Tony Award for Best Play, and was published by Viking Press in 1949. Miller wrote "
      "it out of the encounter with his uncle Manny Newman, a salesman, in Boston in 1947, and out of his "
      "interest in the simultaneity of past and present; the play belongs to the postwar American theatre "
      "of social criticism and to the debate about whether tragedy is possible for the common man.",
  sig="One of the two or three most important American plays of the twentieth century and the most "
      "influential American tragedy: it made the ordinary salesman a tragic protagonist, changed the "
      "American theatre's use of memory and stage time, has been revived repeatedly on Broadway and filmed "
      "ten times, and is a standard text in the study of American drama, of tragedy and of the critique of "
      "the American Dream.",
  canon="Major canon",
  crit="Criticism has argued over whether Willy is a tragic hero or a pathetic victim, with Miller's own "
       "essay 'Tragedy and the Common Man' (1949) the starting point; readings have examined the play's "
       "expressionist staging, its treatment of capitalism and its father-son psychology, and its reception "
       "in the United States and abroad, including the 1983 Beijing production that Miller described in "
       "'Salesman' in Beijing. Its place in the canon of American tragedy, beside O'Neill and Williams, is "
       "secure, and the play is central to discussions of masculinity and the family in postwar America.",
  chars="Willy Loman, a sixty-year-old travelling salesman in the Wagner Company, exhausted, deluded and "
        "proud; Linda Loman, his wife, loyal, practical and clear-sighted; Biff Loman, the elder son, a "
        "former high-school football star who has drifted and steals; Happy Loman, the younger son, "
        "superficially successful and morally adrift; Ben Loman, Willy's dead brother, who went to Alaska "
        "and made a fortune, appearing in Willy's memories; Charley, the neighbour whose success Willy "
        "cannot bear; Bernard, Charley's son, now a lawyer; Howard Wagner, Willy's employer; the Woman, "
        "with whom Willy had an affair in Boston; Miss Forsythe and Letta, the women Happy picks up; and "
        "Stanley, the waiter.",
  biblio="First published by Viking Press (New York, 1949) and premiered at the Morosco Theatre, New York, on "
         "10 February 1949. A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The play was not read complete; the summary follows the published play as described in the sources "
        "consulted, and the quotations are the best-known lines.",
  ver="partially verified", sources=[W_DOS, W_MIL, NAAL]),
]

WORKS += [
W10("Mr. Edwards and the Spider", RL, "1946", "Poem (six-line stanzas)", "significant",
  genres=G("Formal Verse", "Religious Poetry", "Dramatic Monologue"),
  themes=T("Faith, doubt and the sacred", "Death, illness and mourning", "Nature, ecology and environmental crisis"),
  movements=M(LATE),
  overview="A poem printed in Poetry in the winter of 1946 and collected in Lord Weary's Castle the same year: "
           "Jonathan Edwards, the New England theologian, watches spiders spin and considers the soul's "
           "precariousness, and the poem ends by asking that his own heart be 'not hardened'.",
  content="Six-line stanzas in rhymed iambic pentameter, in which the octogenarian Edwards observes a spider "
          "spinning its web, sees in it an image of the soul suspended over damnation, remembers the death of "
          "a young woman and prays for a heart that will not harden.",
  summary="'I saw the spiders marching through the air, / Swimming from tree to tree that mildewed day / In "
          "latter August when the hay / Came creaking to the barn.' The poem opens with Edwards's own "
          "natural observation - the 'flying spiders' of a late-summer afternoon - and turns it into "
          "theology: the spider hangs above the void as the soul hangs above damnation, and its 'thread' "
          "is the thin line of grace. The second stanza moves to the human case: 'And there's the man who "
          "fought the wilderness / Of his own heart, and tamed it to the yoke' - Edwards himself, the "
          "theologian of the will. The poem then remembers 'the widow' and a girl who died unregenerate, "
          "and the young man 'who was the wildest of us all' and drowned; the last stanza asks, in an "
          "old man's voice, for the one thing the preacher cannot give himself: 'Let me not lose / the "
          "memory of that first affliction, Lord, / and let my heart be broken by the Word, / not "
          "hardened.' The poem's power is in the way its Calvinist imagery - the spider, the web, the "
          "abyss, the 'thin thread' of the creature's spinning - is exact natural observation and exact "
          "theological figure at once.",
  themes_text="The poem is a study in Puritan theology as a way of seeing: Edwards's God is a God of absolute "
              "sovereignty, the soul hangs by a thread over the abyss, and the natural world is a system of "
              "signs of election and reprobation. Lowell, a Catholic convert writing a dramatic monologue "
              "in the voice of a Calvinist, uses the form both to inhabit and to judge that vision: the old "
              "man's prayer not to have his heart hardened is a recognition that the theology of the "
              "hardened heart is a danger to the heart itself. The poem's spiders, with their 'mulberry' "
              "bodies and their long threads, are among the most precisely observed images in the early "
              "Lowell, and their combination of delicacy and menace sets the tone of the whole book.",
  structure="Six-line stanzas of rhymed pentameter in a variety of rhyme schemes, with the argument moving "
            "from the spider to the soul, from the soul to particular sinners, and from them to the "
            "speaker's prayer; the poem's last stanza turns outward into petition, so that the monologue "
            "ends as a prayer.",
  style="Dense, allusive, heavily stressed pentameter with a knotty syntax that imitates the preacher's "
        "reasoning; violent and exact natural imagery ('mildewed day', 'mulberry spiders', 'the whited "
        "monster'); archaism and biblical phrasing used without irony; a tone of grim, controlled intensity.",
  ctx="Printed in Poetry in the winter of 1946 and collected in Lord Weary's Castle (Harcourt, Brace, 1946), "
      "the book that won the Pulitzer Prize in 1947; the poem belongs to Lowell's early Catholic phase, in "
      "which he wrote dramatic monologues and historical poems under the influence of Allen Tate, John "
      "Crowe Ransom and the New Critics, and it is one of the poems through which that phase is taught.",
  sig="One of the best-known poems in Lord Weary's Castle and a standard example of Lowell's early formal "
      "manner; it is anthologised as a study in the modern dramatic monologue and in the American Puritan "
      "inheritance, and it shows the historical and theological ambition that would reappear, transformed, "
      "in the public poems of the 1960s.",
  canon="Secondary canon",
  crit="Criticism reads the poem through its relation to Edwards's own writings - the 'Personal Narrative' "
       "and the sermons - and through Lowell's use of the monologue to stage a theology he had recently "
       "adopted and would soon leave; the prayer against a hardened heart is usually taken as the poem's "
       "centre, and the poem is often compared with 'The Quaker Graveyard in Nantucket' as an example of "
       "the historical imagination of the early Lowell.",
  biblio="First published in Poetry, Winter 1946, and collected in Lord Weary's Castle (New York: Harcourt, "
         "Brace, 1946). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was not read complete; the summary follows the text as reproduced in anthologies and in the "
        "critical sources consulted, and the quotations are short and were checked against more than one "
        "transcription. The exact month of the Poetry appearance was not verified.",
  ver="partially verified", sources=[W_LWC, W_LOW, NAAL]),
W10("Skunk Hour", RL, "1958", "Poem (eight six-line stanzas)", "major",
  genres=G("Confessional Poetry", "Free Verse", "Lyric Poetry"),
  themes=T("Madness, breakdown and confinement", "Land, place and regional belonging", "Alienation, absurdity and existential freedom"),
  movements=M(CONF, LATE),
  overview="The last poem of Life Studies, first printed in the Partisan Review in January 1958 and dedicated "
           "to Elizabeth Bishop: a portrait of a declining Maine sea town, a night of insomnia and despair, "
           "and a family of skunks that comes down the street to feed.",
  content="Eight six-line stanzas in loose rhymed verse, moving from the town's summer people and its decaying "
          "proprietors, through the poet's night drive and his confession of a mind 'not gracious', to the "
          "skunks who march up Main Street as the poem's strange, unsentimental consolation.",
  summary="'Nautilus Island's hermit / heiress still lives through winter in her Spartan cottage; / her sheep "
          "still graze the graveyard hill.' The first four stanzas are a social survey of a dying Maine "
          "resort: the heiress, the 'summer millionaire' and his 'ill-fated' marriage, the 'fairy "
          "decorator' and the 'graveyard' hill, the town's 'eyesores' and the 'thousand-threaded "
          "paintwork' peeling from the church. Then the poem turns inward and the tone changes: 'One dark "
          "night, / my Tudor Ford climbed the hill's skull; / I watched for love-cars. Lights turned "
          "down, / they lay together in their cars, / and I would see them, / a red-fox stain / in the "
          "back seat, then a love-crazed stare / and the shot of my love's... / My mind's not right.' "
          "The fifth and sixth stanzas are the poem's celebrated 'dark night' session: 'I hear my ill "
          "spirit sob in each blood cell, / as if my hand were at its throat... / I myself am hell; / "
          "nobody's here - '. The seventh stanza describes the skunks: 'only skunks, that search / in the "
          "moonlight for a bite / to eat. They march on their soles up Main Street... / I stand on top / "
          "of our back steps and breathe the rich air - / a mother skunk with her column of kittens "
          "swills / the garbage pail. / She jabs her wedge-head in a cup / of sour cream, drops her "
          "ostrich tail / and will not scare.' The poem's ending does not console and does not judge; the "
          "skunks are both ridiculous and heroic, and the poet's identification with them is the poem's "
          "final, unsentimental movement.",
  themes_text="The poem is a confessional lyric that turns the poet's mental illness into a landscape: the "
              "decline of the town is his own decline, the 'eyesores' and the 'graveyard' are the furniture "
              "of a mind, and the 'dark night' of the central stanzas is explicitly, as Lowell said, 'not "
              "gracious, but secular, puritan, and agnostical'. The skunks are the poem's answer to the "
              "consolations of the elegy: they are ugly, hungry, maternal and fearless, and the poet's "
              "last gesture is to stand and watch them rather than to interpret them. Its dedication to "
              "Elizabeth Bishop acknowledges the model of 'The Armadillo', and the two poems together "
              "are a dialogue about how much of the self a poem may display.",
  structure="Eight six-line stanzas with irregular but persistent rhyme and a loose iambic measure; the first "
            "four stanzas survey the town in a drifting, 'dawdling' manner, the fifth and sixth turn "
            "inward and intensively lyric, and the last two return to the street for the skunks, so that "
            "the poem's shape is a descent and a return.",
  style="A loose, conversational line that keeps the rhythm of speech while rhyming irregularly; a mixture of "
        "social satire ('fairy / decorator'), raw confession ('My mind's not right'), and dense "
        "alliteration ('a red-fox stain', 'the rich air'); the stanza is the poem's unit of attention, and "
        "the last stanza's short lines break the measure into something like observation itself.",
  ctx="First printed in the Partisan Review in January 1958, with 'Man and Wife' and 'Memories of West Street "
      "and Lepke', and collected as the last poem of Life Studies (Farrar, Straus and Cudahy, 1959), which "
      "won the National Book Award in 1960; Lowell began it in August 1957 and said that rereading "
      "Elizabeth Bishop showed him a way 'of breaking through the shell of my old manner'. It is dedicated "
      "to Bishop, whose 'The Armadillo' is dedicated to him.",
  sig="One of the most anthologised American poems of the postwar period and the poem through which "
      "confessional poetry and Life Studies are usually introduced; it is the first poem of the book to be "
      "completed and the last to be printed, it named a whole manner of American verse, and its 'I myself "
      "am hell' is among the defining lines of modern American poetry.",
  canon="Major canon",
  crit="Criticism has read the poem as the founding text of confessional poetry, as a political poem about "
       "the decay of New England, and as a poem about reading and influence - its relation to Bishop's "
       "'The Armadillo' and to St John of the Cross's 'dark night' is documented in Lowell's own essay "
       "'On Skunk Hour', which describes the poem's composition stanza by stanza. The skunks have been "
       "variously read as delightful and as terrifying, and Lowell, quoting Wilbur and Berryman, said both "
       "could be right.",
  biblio="First published in the Partisan Review, January 1958; collected in Life Studies (New York: Farrar, "
         "Straus and Cudahy, 1959). A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The poem was read through the text reproduced in anthologies and in the sources consulted; the "
        "quotations are short and were checked against more than one transcription. The Partisan Review "
        "date is from the poem's own critical record and agrees with the Norton list's book date of 1959.",
  ver="partially verified", sources=[W_SKUNK, W_LIFE, W_LOW, NAAL]),
]

WORKS += [
W10("Memories of West Street and Lepke", RL, "1958", "Poem (nine five-line stanzas)", "significant",
  genres=G("Confessional Poetry", "Free Verse", "Narrative Poetry"),
  themes=T("Memory, trauma and testimony", "Violence, crime and justice", "The city, the suburb and modern space"),
  movements=M(CONF, LATE),
  overview="A poem first printed in the Partisan Review in January 1958 and collected in Life Studies (1959): "
           "the poet, now a suburban father with a teaching job, remembers the winter of 1943-44 when he "
           "was a conscientious objector in a New York jail and shared a corridor with the murderer Lepke "
           "Buchalter.",
  content="Nine five-line stanzas of loose free verse in which the poet describes his present domestic life, "
          "recalls the West Street jail, the 'stain of the oldness' of the building, his fellow prisoners - "
          "the 'victims of murder' and the gangster Louis 'Lepke' Buchalter, waiting for electrocution - and "
          "admits the distance between the man he was and the man he has become.",
  summary="'Only teaching on Tuesdays, book-worming / in pajamas fresh from the washer each morning, / I hog a "
          "whole house on Marlborough Street.' The poem opens in the poet's comfortable present - a house "
          "in Boston, a teaching job, a wife and daughter, the Sunday papers - and its tone is wry and "
          "guilty: 'I feel like the prices of my poems are rising, / and I am a book-worming / Harvard "
          "man.' Then the poem goes back fifteen years: 'In the fun of the jail-yard... / I was a fire-"
          "breathing / Catholic convert'. He describes the West Street jail, 'the stain of the oldness' "
          "of its walls, the prisoners 'fresh from the courts', the 'muggers' and the 'victims of murder' "
          "he met there, and then the corridor's most famous occupant: 'Also, in the West Street Jail, "
          "'Lepke' Buchalter, / the only man in the ward who could tell us / the date of his death, / "
          "with his 'Biro' pen / writing his last letters.' Lepke is described with a strange tenderness "
          "- 'a psychopathic murderer, / the man in charge of Murder, Incorporated' - who 'was fly-"
          "weight, / bald and voluble, and looked like the theatre's idea / of a Jewish comedian'. The "
          "poem ends with a meditation on the difference between the 'fire-breathing' convert of 1943 and "
          "the 'book-worming Harvard man' of 1958, and with the thought that the age of the double "
          "agent is over - a line whose irony is that the poet's own life has been a series of "
          "transformations.",
  themes_text="The poem is about the betrayals of time and respectability: the radical convert and "
              "conscientious objector has become a Harvard bookworm with a house in the Back Bay, and the "
              "poem's self-mockery is also an accusation. Lepke, the murderer waiting to be executed, "
              "becomes an image of the poet's own death sentence - 'the only man in the ward who could "
              "tell us the date of his death' - and the poem's tenderness toward him is an acknowledgment "
              "of a brotherhood in confinement. The comparison of the poet's 'fire-breathing' faith with "
              "Lepke's calm is the poem's central irony: the convert has lost his fire, and the murderer "
              "has kept his dignity.",
  structure="Nine five-line stanzas of loose free verse, moving between the present and 1943-44 without "
            "transitions; the poem is a montage of scenes - the Marlborough Street house, the jail corridor, "
            "Lepke's cell - and its last stanza returns to the present with a judgment on the self that "
            "has survived.",
  style="Conversational, ironic, heavily enjambed free verse, with a diction that mixes the domestic and the "
        "journalistic ('book-worming', 'Biro pen', 'the man in charge of Murder, Incorporated'); a flat "
        "tone that makes the horror of the prison material more rather than less; the short five-line "
        "stanza gives each observation its own weight.",
  ctx="First printed in the Partisan Review in January 1958 with 'Skunk Hour' and 'Man and Wife', and "
      "collected in Life Studies (1959); Lowell's imprisonment at the West Street jail in 1943, his "
      "refusal of military service and his testimony at the trial of Lepke Buchalter belong to the war "
      "years, and the poem belongs to the sequence of autobiographical poems in Life Studies that made the "
      "book a landmark.",
  sig="One of the central poems of Life Studies and the one that most clearly connects Lowell's public and "
      "private histories; it is a standard anthology text and is much discussed for its treatment of "
      "imprisonment, capital punishment and the poet's own privilege, and its portrait of Lepke is among "
      "the most memorable in postwar American poetry.",
  canon="Secondary canon",
  crit="Criticism reads the poem as a study in the poet's changing politics and as a meditation on "
       "complicity: the poet who once shared a corridor with a murderer now lives on Marlborough Street, "
       "and the poem refuses to resolve the comparison. Its treatment of Lepke has been discussed in "
       "relation to the literature of capital punishment, and the poem is often placed beside 'Skunk "
       "Hour' as evidence of the range of Life Studies.",
  biblio="First published in the Partisan Review, January 1958; collected in Life Studies (New York: Farrar, "
         "Straus and Cudahy, 1959). A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The poem was not read complete; the summary follows the text as reproduced in anthologies and "
        "critical sources, and the quotations are short and were checked against more than one "
        "transcription.",
  ver="partially verified", sources=[W_LIFE, W_LOW, W_SKUNK, NAAL]),
W10("Night Sweat", RL, "1964", "Poem (twenty-eight lines in two parts)", "significant",
  genres=G("Confessional Poetry", "Formal Verse", "Lyric Poetry"),
  themes=T("Madness, breakdown and confinement", "Art, the artist and the creative life", "Love, intimacy and loss"),
  movements=M(CONF, LATE),
  overview="A poem collected in For the Union Dead (1964): a writer lies awake night after night in a "
           "sweat, unable to work, and is brought back to himself by the memory of his wife's presence - "
           "the poem's 'dear heart' - in the second half.",
  content="Twenty-eight lines in two parts, the first a nightmarish account of insomnia, night sweats and "
          "creative sterility, the second a turn toward the wife whose patience and warmth the poet "
          "invokes as the only thing that can 'bear' him.",
  summary="'Work-table, litter, books and standing lamp, / plain things, my stalled equipment, the old broom "
          "- / but I am lying in a tidied room, / for ten nights now I've felt the creeping damp / that "
          "seeps into the mattress...' The opening describes the poet's study as 'stalled equipment' and "
          "the bedroom as a place of nightly terror; the sweat is the body's symptom of a mind unable to "
          "write, and the poem's imagery is one of drowning, smothering and being 'worn ... to the bone'. "
          "The first part ends with the poet's recognition that 'I am tired. Everyone's tired of my "
          "turmoil' - a line that is also a confession of the burden he is on others. The second part "
          "turns to the wife: 'When I was troubled, you were my health, / and I was your fever; / you "
          "were the cool of the evening... / at the end of the day, / my dear heart, / you were the "
          "good of my life.' The poem's resolution is not a cure but a gratitude, and the address to 'my "
          "dear heart' - Elizabeth Hardwick, from whom Lowell was shortly to separate - gives the ending "
          "its pathos.",
  themes_text="The poem is about the relation between creative work and mental illness: the 'stalled "
              "equipment' of the study and the 'creeping damp' of the bedroom are the same condition, and "
              "the poet's inability to write is inseparable from his inability to sleep. Its second "
              "subject is marriage as care: the wife's 'health' and the poet's 'fever' form a contrast "
              "that is both tender and unequal, and the poem's gratitude is shadowed by the knowledge "
              "that the care is exhausting. The 'dear heart' of the last line belongs to the same woman "
              "whose patience the poem has just called into question, and the doubleness is the poem's "
              "achievement.",
  structure="Twenty-eight lines in two parts, the first twenty lines unbroken and the second eight; the "
            "division is marked by the turn from the bedroom to the wife, and the poem's only full stop "
            "falls at the halfway point, so that the syntax itself enacts the break between the night and "
            "the memory.",
  style="Loose rhymed verse with an irregular but audible pattern of rhyme and half-rhyme; a diction that "
        "mixes the domestic ('work-table, litter, books') with the medical ('sweat', 'damp', 'fever'); "
        "long sentences that imitate the insomnia they describe, and short lines at the end that "
        "slow into the address to the wife.",
  ctx="Collected in For the Union Dead (Farrar, Straus and Giroux, 1964), Lowell's sixth book, which "
      "followed Life Studies and in which he returned to stricter forms and to public themes; the poem "
      "belongs to the sequence of poems about his marriage to Elizabeth Hardwick, whom he was to leave "
      "for Caroline Blackwood in 1970, and it was later revised as a sonnet for Notebook (1970).",
  sig="One of the most anthologised poems of For the Union Dead and a standard text for the study of "
      "confessional poetry and of the literature of mental illness; its 'I am tired. Everyone's tired of "
      "my turmoil' is among the most quoted lines in Lowell's work, and the poem is central to accounts "
      "of his late style.",
  canon="Secondary canon",
  crit="Criticism reads the poem as an example of the confessional mode at its most controlled, with the "
       "formal regularity of the verse holding the material at a distance; the address to the wife has "
       "been discussed in relation to the ethics of using intimate life as material, and the poem's later "
       "revision as a sonnet in Notebook is often used to show how Lowell's late style compressed and "
       "hardened his early drafts.",
  biblio="Collected in For the Union Dead (New York: Farrar, Straus and Giroux, 1964); a revised sonnet "
         "version appeared in Notebook (1970). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The poem's first periodical appearance was not identified; the 1964 date is the book date given in "
        "the Norton list and confirmed by the volume's bibliography. The text quoted was read through "
        "anthologies and teaching reproductions rather than the first edition.",
  ver="partially verified", sources=[W_FUD, W_LOW, NAAL]),
]

WORKS += [
W10("For the Union Dead", RL, "1964", "Poem (eight eight-line stanzas)", "major",
  genres=G("Confessional Poetry", "Elegiac Poetry", "Formal Verse"),
  themes=T("History, truth and the uses of the past", "Race, racism and the struggle for civil rights", "War, combat and its aftermath"),
  movements=M(CONF, LATE),
  overview="The title poem of For the Union Dead (1964), first read at the Boston Arts Festival in 1960: "
           "standing on Boston Common beside Saint-Gaudens's monument to Colonel Shaw and the 54th "
           "Massachusetts, the poet remembers the Civil War, the demolished South Boston Aquarium of his "
           "childhood and the civil-rights struggle on television, and ends with the traffic.",
  content="Eight eight-line stanzas of loose rhymed verse in which the poet describes the excavation of the "
          "Common for an underground garage, the 'shaking' monument, the story of Shaw and his Black "
          "regiment, the loss of the Aquarium, a remembered childhood street, and the cars that 'nose "
          "forward like fish' at the end.",
  summary="'Relinquunt Omnia Servare Rem Publicam' reads the epigraph, the monument's inscription rewritten by "
          "Lowell to say that Shaw's soldiers gave up everything to serve the state. The poem opens on the "
          "Common, where 'the old South Boston Aquarium stands / in a Sahara of snow now' and where a "
          "'commercial photograph' shows the excavation for a garage; the poet watches the bronze relief "
          "of Shaw on his horse, 'He has an angry wrenlike vigilance, / a greyhound's gentle tautness', "
          "and remembers that 'on a thousand small-town New England greens' there are their stone "
          "statues of the abstract Union Soldier. The fourth and fifth stanzas retell the charge "
          "of the 54th on Fort Wagner, 'the bell-cheeked Negro infantry' who 'waded in the blood of "
          "their brothers', and the moment when 'Colonel Shaw / is riding on his bubble, / he waits / "
          "for the blessèd break.' Then the poem moves to the poet's childhood: the Aquarium, where 'my "
          "hand draws back from the fish', and the 'cowed, / loyal / and black' faces of the prisoners in "
          "the county jail. The seventh stanza turns to the present - 'The Aquarium is gone. Everywhere, "
          "/ giant finned cars nose forward like fish; / a savage servility / slides by on grease' - and "
          "the final image of the poem is the traffic on the new road, indifferent to the monument above "
          "it.",
  themes_text="The poem is about the relation between public memory and present indifference: the monument "
              "commemorates a sacrifice for racial justice, and the city that raised it is now building a "
              "garage beneath it and driving past it. Its second subject is the poet's own history, since "
              "the Aquarium and the Common belong to his Boston childhood and the monument to his family's "
              "ancestry on both sides of the Civil War; the sixth stanza's memory of the 'cowed' prisoners "
              "is the poem's acknowledgment that the poet's inheritance is compromised. The civil-rights "
              "images of the 1960s, which Lowell saw on television, belong to the poem's final movement "
              "and make it, with 'Skunk Hour' and the poems of Near the Ocean, one of the central "
              "American poems of the decade.",
  structure="Eight eight-line stanzas with irregular rhyme and a loose pentameter; the poem moves from the "
            "present scene to history, back to childhood, and forward to the traffic, and its stanzas are "
            "units of association rather than of argument; the epigraph's Latin and the monument's bronze "
            "are the poem's two fixed points, and the last stanza enforces a break between them and the "
            "modern street.",
  style="A formal but flexible verse - rhyme and metre present but irregular - with a diction that moves "
        "between the journalistic ('a commercial photograph'), the historical ('bell-cheeked Negro "
        "infantry') and the visionary ('the blessèd break'); short lines and heavy stresses in the "
        "climactic stanzas; the last three lines are among the most famous in postwar American poetry.",
  ctx="First read at the Boston Arts Festival in June 1960 and collected as the title poem of For the Union "
      "Dead (Farrar, Straus and Giroux, 1964); its occasion was the excavation of Boston Common for an "
      "underground garage and the demolition of the South Boston Aquarium in 1954, and its monument is "
      "Augustus Saint-Gaudens's bronze relief of Colonel Robert Gould Shaw and the 54th Massachusetts "
      "Volunteer Infantry, dedicated in 1897. The title echoes Allen Tate's 'Ode to the Confederate Dead', "
      "and the poem belongs to the civil-rights years in which Lowell marched in Washington and wrote "
      "against the war in Vietnam.",
  sig="Lowell's best-known public poem and one of the central American poems of the 1960s; it is a standard "
      "text in the study of the poetry of history and of civil rights, it gave its name to one of the "
      "defining books of his career, and its closing image of 'a savage servility' is among the most "
      "quoted endings in modern American verse.",
  canon="Major canon",
  crit="Criticism has read the poem as an elegy for a lost civic ideal, as a meditation on the poet's own "
       "family history and on the monument as an object of art, and as a civil-rights poem of the early "
       "1960s; the relation of the poem to Tate's 'Ode to the Confederate Dead' and to Saint-Gaudens's "
       "relief has been extensively discussed, and the epigraph's alteration of the Latin inscription is "
       "the standard example of Lowell's habit of revising public texts for his own purposes.",
  biblio="Collected in For the Union Dead (New York: Farrar, Straus and Giroux, 1964); first read at the "
         "Boston Arts Festival in 1960. A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The poem's first periodical publication was not identified; the 1964 date is the book date in the "
        "Norton list, and the 1960 first reading is documented. The Latin of the epigraph and the "
        "inscription on the monument differ, which the record states rather than resolves.",
  ver="partially verified", sources=[W_FUD, W_LOW, NAAL]),
]
