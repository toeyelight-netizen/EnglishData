"""Installment 10, wave 25: John Barth, Joan Didion, James Baldwin, Flannery O'Connor, Allen Ginsberg.

Five new authors and nine works, one record per Norton selection.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

JB = "John Barth"
JD = "Joan Didion"
JBA = "James Baldwin"
FOC = "Flannery O'Connor"
AG = "Allen Ginsberg"

SOG = "Southern Gothic"
POST = "Postmodernism and Postmodern Fiction"
BEAT = "The Beat Generation"
BAM = "Black Arts Movement"

W_JB = "John Barth (Wikipedia)"
W_LITF = "Lost in the Funhouse (Wikipedia)"
W_JD = "The White Album (Wikipedia)"
W_JBA = "James Baldwin (Wikipedia)"
W_GMM = "Going to Meet the Man (Wikipedia)"
W_GMMS = "Going to Meet the Man, short story (Wikipedia)"
W_SB = "Sonny's Blues (Wikipedia)"
W_FOC = "Flannery O'Connor (Wikipedia)"
W_GMHF = "A Good Man Is Hard to Find (Wikipedia)"
W_GCP = "Good Country People (Wikipedia)"
W_ETR = "Everything That Rises Must Converge (Wikipedia)"
W_HOWL = "Howl (poem) (Wikipedia)"
W_PROG = "A Letter to My Nephew (The Progressive, via course reading)"
W_BIB = "James Baldwin bibliography (baldwinbibliography.com)"

AUTHORS = [
A10(JBA, MAJ, "1924", "1987", "New York City, New York, United States",
  "American; novelist, essayist, playwright and short-story writer writing in English",
  "American writer and civil rights orator whose novels and essays on race, sexuality and the church - Go Tell "
  "It on the Mountain, Notes of a Native Son, The Fire Next Time - made him the conscience of American "
  "prose in the 1950s and 1960s",
  "James Arthur Jones was born in Harlem Hospital, New York, on 2 August 1924, the son of Emma Berdis Jones; "
  "in 1927 his mother married David Baldwin, a Baptist preacher from Louisiana, whose name he took and "
  "against whose religion he defined himself. He was a preacher himself as a teenager at the Fireside "
  "Pentecostal Church, left home in 1943, worked in New Jersey and New York, and in 1948 left the United "
  "States for Paris with forty dollars and a manuscript, where he wrote Go Tell It on the Mountain (1953) "
  "and the essays of Notes of a Native Son (1955); Giovanni's Room (1956) was a novel about white gay "
  "expatriates, and Nobody Knows My Name (1961), Another Country (1962), The Fire Next Time (1963), "
  "Blues for Mister Charlie (1964, a play), Going to Meet the Man (1965), Tell Me How Long the Train's "
  "Been Gone (1968), No Name in the Street (1972), If Beale Street Could Talk (1974) and Just Above My "
  "Head (1979) followed. He was a public speaker for the civil rights movement, debated William F. Buckley "
  "at Cambridge in 1965, lived for years at Saint-Paul-de-Vence in the south of France, and died there on "
  "1 December 1987.",
  "Novels: Go Tell It on the Mountain (1953), Giovanni's Room (1956), Another Country (1962), Tell Me How "
  "Long the Train's Been Gone (1968), If Beale Street Could Talk (1974) and Just Above My Head (1979), with "
  "the unfinished Remember This House. Essays: Notes of a Native Son (1955), Nobody Knows My Name (1961), "
  "The Fire Next Time (1963), No Name in the Street (1972), The Devil Finds Work (1976) and The Price of "
  "the Ticket (1985). Stories: Going to Meet the Man (1965). Plays: The Amen Corner (1954) and Blues for "
  "Mister Charlie (1964).",
  "Long, cadenced sentences that move from the colloquial to the biblical within a paragraph; the preacher's "
  "rhetoric - direct address, repetition, antithesis - turned to secular argument; an essayistic first "
  "person that makes the writer's own history the evidence; dialogue that catches the music and the "
  "evasions of Harlem and of the South.",
  "Race, racism and the struggle for civil rights; the Black church, sin and salvation; sexuality, desire "
  "and the closet; family, fathers and sons; exile, Paris and the American abroad; the uses of history and "
  "the refusal of American innocence; suffering and the possibility of love.",
  "Baldwin is the central American essayist of the civil rights era and one of the most quoted American "
  "writers of the century; his novels made Black Harlem and gay experience the matter of literary fiction, "
  "his essays are standard texts in American literature, history and law, and the 2016 film I Am Not Your "
  "Negro renewed his public presence a generation after his death.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Baldwin and from the bibliography "
           "pages consulted, read directly; they were not checked against a printed bibliography. "
           "Installment 10 records only the three Norton selections - 'Sonny's Blues' (Partisan Review, "
           "Summer 1957), 'Going to Meet the Man' (Status, October 1965; collected 1965) and 'A Letter to My "
           "Nephew' (The Progressive, December 1962; collected as 'My Dungeon Shook' in The Fire Next Time, "
           "1963) - so the novels, the other essays and the plays have no records and the bibliography is "
           "incomplete.",
  ver="partially verified", sources=[W_JBA, W_GMM, W_SB, W_PROG, W_BIB, NAAL]),
]

AUTHORS += [
A10(FOC, MAJ, "1925", "1964", "Savannah, Georgia, United States",
  "American; short-story writer and novelist writing in English",
  "American short-story writer of the Georgia backcountry, a Roman Catholic whose comic and violent stories of "
  "the action of grace - 'A Good Man Is Hard to Find', 'Good Country People' - are among the most admired in "
  "the language",
  "Mary Flannery O'Connor was born in Savannah, Georgia, on 25 March 1925, the only child of Edward Francis "
  "O'Connor and Regina Cline; the family moved to Milledgeville in 1940, her father died of lupus in 1941, "
  "and she took her degree at Georgia State College for Women in 1945 and studied at the Iowa Writers' "
  "Workshop, where she took her MFA in 1947. She wrote Wise Blood (1952) and The Violent Bear It Away "
  "(1960), the stories of A Good Man Is Hard to Find and Other Stories (1955) and Everything That Rises "
  "Must Converge (1965, posthumous), the essays and lectures of Mystery and Manners (1969) and the letters "
  "of The Habit of Being (1979). In 1950 she was diagnosed with disseminated lupus, the disease that had "
  "killed her father, and lived for the rest of her life at her mother's farm at Andalusia, near "
  "Milledgeville, raising peacocks and writing in the mornings; she died on 3 August 1964, at 39, and "
  "The Complete Stories won the National Book Award in 1972.",
  "Novels: Wise Blood (1952) and The Violent Bear It Away (1960). Stories: A Good Man Is Hard to Find and "
  "Other Stories (1955), Everything That Rises Must Converge (1965) and The Complete Stories (1971). "
  "Non-fiction: Mystery and Manners: Occasional Prose (1969) and The Habit of Being: Letters (1979), with "
  "the early stories in The Geranium: A Collection of Short Stories (1975).",
  "A comic, exact and mercilessly flat style in which grotesque events are reported without comment; "
  "dialogue that reproduces the idiom of the rural South with great precision; a habit of ending a story "
  "with a single turn that reverses everything before it; violent imagery used as the instrument of "
  "revelation rather than of sensation.",
  "Grace and the resistance to it, in explicitly Catholic terms; sin, redemption and judgement; the "
  "grotesque body and the disabled body; race and the American South in the years of desegregation; "
  "mothers and daughters, and the family as a field of violence; the pretensions of the educated and the "
  "secular.",
  "O'Connor is one of the great American short-story writers of the century and the central figure of the "
  "Southern Gothic after Faulkner; her stories are standard anthology texts, The Complete Stories won the "
  "National Book Award, and her essays on the writing of fiction, collected in Mystery and Manners, are "
  "among the most cited by American writers on craft.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on O'Connor and from its pages on the "
           "individual stories, read directly; they were not checked against a printed bibliography. "
           "Installment 10 records only the three Norton selections - 'Good Country People' (Harper's "
           "Bazaar, June 1955), 'A Good Man Is Hard to Find' (Modern Writing I, 1953) and 'Everything That "
           "Rises Must Converge' (New World Writing, October 1961) - so the two novels, the other stories "
           "and the letters have no records and the bibliography is incomplete.",
  ver="partially verified", sources=[W_FOC, W_GMHF, W_GCP, W_ETR, NAAL]),
A10(AG, MAJ, "1926", "1997", "Newark, New Jersey, United States",
  "American; poet, essayist and activist writing in English",
  "American poet of the Beat Generation whose long breath-lines and candour about sexuality, madness and "
  "empire made 'Howl' the founding poem of the postwar American counterculture",
  "Irwin Allen Ginsberg was born in Newark, New Jersey, on 3 June 1926, the son of Louis Ginsberg, a poet "
  "and high-school teacher, and Naomi Levy Ginsberg, whose mental illness and early death marked his life "
  "and his work. He entered Columbia University in 1943, met Jack Kerouac, William Burroughs and Neal "
  "Cassady there, was suspended and later arrested in connection with a stolen car, spent eight months in "
  "a psychiatric institute in 1949 at his own request, and moved to San Francisco in 1954, where he read "
  "'Howl' at the Six Gallery in October 1955 and saw it published by City Lights in 1956. Howl and Other "
  "Poems was the subject of an obscenity trial in 1957, which it won; Kaddish and Other Poems (1961), "
  "Reality Sandwiches (1963), Planet News (1968), The Fall of America (1972, National Book Award), Mind "
  "Breaths (1977), Plutonian Ode (1982), White Shroud (1986) and Cosmopolitan Greetings (1994) followed, "
  "with the essays of Deliberate Prose and the photographs and songs. He was a public figure of the "
  "anti-war and gay liberation movements, studied with Buddhist teachers from the 1970s, and died in New "
  "York on 5 April 1997.",
  "Poetry: Howl and Other Poems (1956), Kaddish and Other Poems (1961), Reality Sandwiches (1963), Planet "
  "News (1968), The Fall of America (1972), Mind Breaths (1977), Plutonian Ode (1982), White Shroud "
  "(1986), Cosmopolitan Greetings (1994) and Death and Fame (1999), with Collected Poems 1947-1997 (2006). "
  "Prose: Deliberate Prose: Selected Essays (2000), Journals: Mid-Fifties (1995) and the letters with "
  "Kerouac and Cassady.",
  "The long breath-line: a line measured by the length of a single exhalation rather than by the foot, "
  "with parataxis in place of subordinate clauses; catalogues of people and things; a diction that mixes "
  "the prophetic, the obscene and the documentary; repetition and incantation derived from Hebrew liturgy "
  "and from jazz.",
  "Madness, confinement and the destruction of the gifted by American society; sexuality and the closet; "
  "war, empire and the military-industrial state; the sacred in the ordinary and in the body; friendship "
  "and the Beat community; Buddhism, chant and the discipline of attention; testimony, and the poet as "
  "witness.",
  "Ginsberg is the most public poet of the American postwar avant-garde and 'Howl' the poem through which "
  "the Beat Generation is defined; the 1957 obscenity trial became a landmark of American free expression, "
  "the poem is a standard anthology and course text, and Ginsberg's readings, recordings and activism made "
  "him one of the best-known poets of the century.",
  bib_status="incomplete",
  bib_note="The biography and the list of books above come from Wikipedia's article on Ginsberg and on "
           "'Howl', read directly; they were not checked against a printed bibliography. Installment 10 "
           "records only the Norton selection, 'Howl' (written 1954-55; Howl and Other Poems, City Lights, "
           "1956); the other collections, the essays and the journals have no records, so the bibliography "
           "is incomplete.",
  ver="partially verified", sources=[W_HOWL, NAAL]),
]

AUTHORS += [
A10(JB, SEC, "1930", "2024", "Cambridge, Maryland, United States",
  "American; novelist and short-story writer writing in English",
  "American novelist and theorist of the exhausted mode, the most programmatic of the American postmodernists, "
  "whose Lost in the Funhouse (1968) turned the short story into an essay on its own making",
  "John Simmons Barth was born in Cambridge, Maryland, on 27 May 1930, the son of a candy-store owner; he "
  "studied briefly at the Juilliard School, took his BA and MA at Johns Hopkins University, and taught at "
  "Pennsylvania State University from 1953 to 1965 and then at the State University of New York at Buffalo, "
  "before returning to Johns Hopkins in 1973 as Alumni Centennial Professor, retiring in 1995. The Floating "
  "Opera (1956) and The End of the Road (1958) are realist novels, The Sot-Weed Factor (1960) and Giles "
  "Goat-Boy (1966) mock-epic ones; Lost in the Funhouse (1968) followed his essay 'The Literature of "
  "Exhaustion' (1967) and made him the leading theorist of American metafiction, and Chimera (1972) won the "
  "National Book Award in 1973. LETTERS (1979), Sabbatical (1982), The Tidewater Tales (1987), The Last "
  "Voyage of Somebody the Sailor (1991), Once Upon a Time (1994) and Coming Soon!!! (2001) followed, with "
  "the non-fiction of The Friday Book (1984) and Further Fridays (1995). He died at Bonita Springs, "
  "Florida, on 2 April 2024.",
  "Novels: The Floating Opera (1956), The End of the Road (1958), The Sot-Weed Factor (1960), Giles "
  "Goat-Boy (1966), Chimera (1972), LETTERS (1979), Sabbatical (1982), The Tidewater Tales (1987), The Last "
  "Voyage of Somebody the Sailor (1991), Once Upon a Time (1994), Coming Soon!!! (2001) and Every Third "
  "Thought (2015). Stories: Lost in the Funhouse (1968), On with the Story (1996) and The Development "
  "(2008). Non-fiction: The Friday Book (1984) and Further Fridays (1995).",
  "Stories that interrupt themselves to discuss their own construction, with footnotes, diagrams, blank "
  "pages and alternative endings; pastiche of earlier genres from the eighteenth-century novel to the "
  "detective story; a prose of great rhetorical energy and comic pedantry; the repeated figure of the "
  "author as a character in his own text.",
  "The exhaustion of literary forms and the possibility of writing after them; storytelling as a subject in "
  "itself; myth, epic and the oldest stories reused; identity as performance and as quotation; the artist's "
  "career and the relation of a writer to his own earlier books; the comic and the cosmic.",
  "Barth is the figure through which American postmodernism and metafiction are usually taught, and 'The "
  "Literature of Exhaustion' is one of the most cited critical essays of the postwar decades; Lost in the "
  "Funhouse is a standard text in courses on the American short story and on experimental fiction, and his "
  "influence on the writers who followed him - from Barth's own students to the metafiction of the 1970s "
  "and 1980s - is widely acknowledged.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Barth and on Lost in the Funhouse, "
           "read directly; they were not checked against a printed bibliography. Installment 10 records only "
           "the Norton selections of the title story, 'Lost in the Funhouse' (The Atlantic Monthly, November "
           "1967; collected 1968); the novels, the other stories and the criticism have no records, so the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_JB, W_LITF, NAAL]),
A10(JD, MAJ, "1934", "2021", "Sacramento, California, United States",
  "American; essayist, novelist and screenwriter writing in English",
  "American essayist and novelist whose cool, fragmentary reports on California and on American politics - "
  "Slouching Towards Bethlehem, The White Album - made her the most imitated prose stylist of American "
  "non-fiction",
  "Joan Didion was born in Sacramento, California, on 5 December 1934, into a family of California "
  "pioneers; she took her degree in English at the University of California, Berkeley, in 1956, won a "
  "Prize from Vogue for an essay and worked at the magazine in New York for eight years, and married the "
  "writer John Gregory Dunne in 1964, with whom she wrote screenplays and adopted a daughter, Quintana. "
  "Run River (1963) was her first novel; Slouching Towards Bethlehem (1968) made her reputation as an "
  "essayist, and Play It As It Lays (1970), A Book of Common Prayer (1977), Democracy (1984) and The Last "
  "Thing He Wanted (1996) are the later novels. The White Album (1979) collected the essays of the 1970s, "
  "followed by Salvador (1983), Miami (1987), After Henry (1992), Political Fictions (2001) and Where I Was "
  "From (2003); The Year of Magical Thinking (2005), written after Dunne's death in 2003, won the National "
  "Book Award, and Blue Nights (2011) followed the death of her daughter. She died in New York on 23 "
  "December 2021.",
  "Non-fiction: Slouching Towards Bethlehem (1968), The White Album (1979), Salvador (1983), Miami (1987), "
  "After Henry (1992), Political Fictions (2001), Where I Was From (2003), The Year of Magical Thinking "
  "(2005), We Tell Ourselves Stories in Order to Live (2006) and Blue Nights (2011). Novels: Run River "
  "(1963), Play It As It Lays (1970), A Book of Common Prayer (1977), Democracy (1984) and The Last Thing "
  "He Wanted (1996). Screenplays, with John Gregory Dunne, include Panic in Needle Park (1971) and A Star Is "
  "Born (1976).",
  "Short declarative sentences and a deliberately flat rhythm; the repeated phrase and the returning "
  "motif as structure; juxtaposition of reportage and private recollection without transition; quotation "
  "of documents, testimony and song lyrics; a first person that is present but withheld, and an irony "
  "that never quite becomes judgement.",
  "California as a place and a state of mind; the 1960s and their aftermath, above all in Los Angeles; "
  "narrative itself and the stories people tell to survive; women's lives and the pressure of feminine "
  "roles; politics, media and the manipulation of images; grief, illness and memory.",
  "Didion is the most influential American essayist of the last half-century and the model for the "
  "personal, reportorial non-fiction that followed her; The White Album was named by Publishers Weekly "
  "among the ten most important essays since 1950, The Year of Magical Thinking won the National Book "
  "Award, and her sentences are among the most quoted in modern American prose.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on The White Album and from general "
           "knowledge, checked against the article's publication details; they were not checked against a "
           "printed bibliography. Installment 10 records only the Norton selection, 'The White Album' (New "
           "West, 1979; collected 1979); the other collections and the novels have no records, so the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_JD, NAAL]),
]

WORKS = [
W10("Lost in the Funhouse", JB, "1967", "Short story (metafiction)", "significant",
  genres=G("Experimental Fiction", "Metafictional Novel", "Short Story"),
  themes=T("Art, the artist and the creative life", "Language, writing and the limits of representation", "Childhood, adolescence and coming of age"),
  movements=M(POST),
  overview="A story first printed in The Atlantic Monthly in November 1967 and collected as the title piece of "
           "Lost in the Funhouse (1968): a young boy's visit to a boardwalk funhouse at Ocean City, told by a "
           "narrator who keeps interrupting to discuss how the story is being told and how it might end.",
  content="A story of twenty-odd numbered sections in which Ambrose, thirteen, goes to a seaside funhouse with "
          "his family and the girl he loves, and in which the narration constantly breaks off to consider "
          "beginnings, middles, endings and the impossibility of the task it has set itself.",
  summary="The story is set in 1962 at Ocean City, Maryland, where Ambrose - the same boy who appears in the "
          "other Ambrose stories of the collection - has come with his family for the summer. He is "
          "thirteen, self-conscious, in love with his brother Peter's girl Magda, and he finds himself "
          "inside the funhouse, a maze of mirrors, a hall of illusions, a spiral staircase and a 'sliding "
          "board into the Atlantic'. Around this small adventure the narrator builds an essay: he "
          "discusses where a story should begin, how a personage should be introduced, what a plot is, "
          "why the reader's desire for an ending is itself a subject, and whether the story we are "
          "reading can have an end at all. Sections are numbered and interrupted; the narrator addresses "
          "the reader and himself ('you'); alternative versions of a sentence are offered and rejected. "
          "Ambrose gets lost, as the title says, and at the end he is on the sliding board or in the "
          "water, and the story has done what it said it could not do.",
  themes_text="The story's subject is storytelling. Everything the narrator says about plot, beginning and "
              "ending is enacted in the story itself, and the boy's loss of himself in the funhouse is the "
              "image of the reader's and the writer's situation inside a fiction. Around that are the "
              "themes of adolescence - sexual shame, the discovery of being observed, the pain of not "
              "being chosen - and of the relation between life and the forms through which it is told. "
              "The funhouse is also a figure of art itself: a structure built to deceive the senses, "
              "which is exactly what a story is, and the story's narrator is aware that this makes him a "
              "maker of illusions rather than a witness.",
  structure="Numbered sections, some of them lines long, which break off, restart and comment on themselves; "
            "the narrative of Ambrose's afternoon and the essay on narration alternate; the story ends "
            "with several possible endings offered and one of them performed, so that the reader cannot "
            "tell whether the story has closed or merely stopped.",
  style="A deliberately literary, oral-sounding narrator with a taste for lists, rhetorical questions and "
        "essayistic commentary; parodies of nineteenth-century fictional address and of the conventions "
        "of the magazine story; long sentences that mimic the pace of a child's afternoon and short "
        "apophthegms about the art of fiction; typographic devices, including dotted lines and italics.",
  ctx="Written in 1966-67 and printed in The Atlantic Monthly in November 1967, where it took third prize in "
      "the O. Henry Awards; collected as the title story of Lost in the Funhouse: Fiction for Print, Tape, "
      "Live Voice (New York: Doubleday, 1968). The collection followed Barth's essay 'The Literature of "
      "Exhaustion' (1967) and became, with the work of Barthelme and Coover, the standard instance of "
      "American metafiction.",
  sig="One of the most anthologised American short stories of the postwar decades and the standard text "
      "through which metafiction is taught; the collection it names is a landmark of American postmodernism, "
      "and the story's devices passed into the common vocabulary of American fiction writing.",
  canon="Major canon",
  crit="Criticism reads the story as a demonstration of Barth's theory of exhaustion, as a parody of the "
       "bildungsroman and of the reader's expectations, and as a story about the loss of the self that "
       "postmodern fiction is often accused of enacting; its use of the funhouse as an image of fiction, "
       "and its relation to the earlier Ambrose stories, are the recurring topics.",
  biblio="First published in The Atlantic Monthly, November 1967; collected in Lost in the Funhouse: Fiction "
         "for Print, Tape, Live Voice (New York: Doubleday, 1968). A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows published descriptions of the story and the "
        "passages quoted in the sources consulted, and the record says so rather than implying a full "
        "reading.",
  ver="partially verified", sources=[W_LITF, W_JB, NAAL]),
]

WORKS += [
W10("The White Album", JD, "1979", "Essay (personal essay)", "major",
  genres=G("Personal Essay", "Cultural Criticism", "Nonfiction Prose (1946–2000)"),
  themes=T("Language, writing and the limits of representation", "The city, the suburb and modern space", "Technology, media and consumer society"),
  movements=M(POST),
  overview="The long title essay of The White Album (Simon & Schuster, 1979), published complete in New West in "
           "1979 from reporting done in 1968-69: a fragmentary account of Los Angeles at the end of the "
           "1960s, opening with the sentence 'We tell ourselves stories in order to live'.",
  content="An essay in numbered fragments, moving between reportage - a Doors recording session, Black Panther "
          "meetings, a prison interview with Linda Kasabian, a murder trial, a psychiatric examination - and "
          "the narrator's own account of a breakdown she experienced in the summer of 1968.",
  summary="The essay opens with the sentence that has become Didion's signature - 'We tell ourselves stories "
          "in order to live' - and immediately complicates it: the stories we tell are 'the imposition of a "
          "narrative line upon disparate images', and when that line fails, the images are all that is "
          "left. What follows is a sequence of such images, most of them drawn from the Los Angeles of "
          "1968-69: the empty house on Franklin Avenue with its 'particular vanity' of black-and-white "
          "tiles; the recording studio where the Doors are at work; meetings with the Black Panthers; a "
          "prison interview with Linda Kasabian, who is testifying against Charles Manson, and the trial "
          "itself; a visit from a man with a gun. Between these scenes Didion places her own case history: "
          "the nausea, the spells of vertigo she began to have in the summer of 1968, the psychiatrist's "
          "report, the outpatient clinic in Santa Monica, the chemotherapy she was told she might need. "
          "The essay's movement is associational; it quotes song lyrics, newspaper clippings, police "
          "reports, the psychiatrist's report, and its refrain is the impossibility of the narrative it "
          "is nevertheless performing. It ends in a hospital, with Didion looking out at the city and "
          "acknowledging that the story she has told is one of many that could have been told.",
  themes_text="The essay's central subject is the relation between narrative and survival: people tell "
              "themselves stories in order to live, and the failure of narrative is a kind of breakdown. "
              "Didion's own illness is presented as exactly that failure, so that the essay's form - "
              "fragments, quotations, abrupt transitions - enacts the condition it describes. Around this "
              "are its subjects of California and the 1960s: the Manson murders and the end of the dream "
              "of the decade, media and image-making, the Black Panthers and the politics of the period, "
              "and the culture's habit of replacing events with stories about them.",
  structure="An essay in a series of untitled fragments, varying from a paragraph to several pages, with "
            "reportage, quotation, personal history and reflection interleaved; there is no argumentative "
            "progression and no resolution, and the essay's unity is tonal and thematic rather than "
            "narrative.",
  style="Short declarative sentences with a falling rhythm; the present tense used for scenes and the past "
        "for reflection; documents and testimony quoted at length and without comment; a repeated first "
        "person that is reserved to the point of impersonality; the phrase set in italics or repeated as "
        "a refrain.",
  ctx="The complete essay was published in New West in 1979, from reporting done in 1968-69, and became the "
      "first and title essay of The White Album (New York: Simon & Schuster, 1979); portions of the "
      "material had appeared earlier in magazines, and the Los Angeles of the essay is the city of the "
      "Manson trial, the Black Panthers, the Doors and the aftermath of the 1965 Watts rebellion.",
  sig="One of the most influential American essays of the second half of the century and a standard text in "
      "courses on the essay, on New Journalism and on California; Publishers Weekly named it one of the ten "
      "most important essays since 1950, and its first sentence is among the most quoted in modern American "
      "prose.",
  canon="Major canon",
  crit="Criticism reads the essay as a formal breakthrough in American non-fiction - the subject as fragmentation, "
       "the writer as a camera rather than a narrator - and as a document of the end of the 1960s; its "
       "treatment of illness, of the Manson trial and of media culture has been widely discussed, and it "
       "is often set beside the New Journalism of Tom Wolfe and Hunter S. Thompson as a distinctively "
       "female and self-effacing alternative.",
  biblio="First published complete in New West, 1979, from material reported in 1968-69; collected as the "
         "first essay of The White Album (New York: Simon & Schuster, 1979) and reprinted in We Tell "
         "Ourselves Stories in Order to Live (2006). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The essay was not read complete; the summary follows published descriptions and the passages quoted "
        "in the sources consulted, and the record says so.",
  ver="partially verified", sources=[W_JD, NAAL]),
]

WORKS += [
W10("Sonny's Blues", JBA, "1957", "Short story", "major",
  genres=G("Short Story", "Realist Fiction", "Autobiographical Novel"),
  themes=T("Race, racism and the struggle for civil rights", "Art, the artist and the creative life", "Family, marriage and domestic life"),
  movements=M(BAM),
  overview="A story published in Partisan Review in the summer of 1957 and collected in Going to Meet the Man "
           "(1965): a Harlem schoolteacher discovers that his younger brother, a jazz pianist and a heroin "
           "addict, has been arrested, and the two brothers slowly find their way back to one another.",
  content="A first-person story in two movements, from the narrator's reading of the news in the subway and "
          "his memories of their childhood, through the death of his small daughter and his letter to "
          "Sonny in prison, to the night in a Greenwich Village jazz club when he finally hears his "
          "brother play.",
  summary="The story opens with the narrator, a teacher of algebra in a Harlem high school, reading in the "
          "subway that his younger brother Sonny has been arrested for possession of heroin. He remembers "
          "their childhood - the father's bitterness and early death, the mother's request that he look "
          "after Sonny, the boy's early obsession with the piano, his truancy and his wish to join the "
          "army - and then meets Sonny's friend, who warns him that the addiction will not end with the "
          "prison sentence. For a long time the brothers do not speak. The narrator's small daughter Grace "
          "dies of polio while he is away, and he writes to Sonny in prison; when Sonny is released the "
          "two meet in New York in an awkward, careful reunion, and Sonny explains what music means to "
          "him - that heroin was a way of feeling in control, and that playing is a way of making the "
          "suffering bearable. In the story's final movement the narrator goes to a jazz club in Greenwich "
          "Village where Sonny is playing with a group led by Creole; the music begins as something the "
          "narrator cannot follow and becomes, in the last pages, a blues in which the whole history of "
          "the family and of the people is audible, and the narrator sends a drink to his brother and "
          "understands at last what he has been listening to.",
  themes_text="The story's argument is that suffering can be borne and partly redeemed by being made into "
              "music, and that the blues are the form in which a particular American history has been "
              "carried. It is also a story about brothers: the narrator's respectability and his fear are "
              "set against Sonny's risk, and the story refuses to choose between them, since the "
              "respectable brother is the one who needs to learn to listen. Race is present everywhere - "
              "in the housing projects, in the police, in the fear of the dark - but Baldwin never makes "
              "the story a tract; the political argument is carried by the music and by the family, and "
              "the story's famous last image connects the singer's cup of trembling to the brother's "
              "drink.",
  structure="A first-person narrative in two large movements divided by a period of silence and a letter, "
            "with a long embedded recollection of childhood and a closing scene in the club; the story "
            "moves from the news of the arrest to the performance, and the two are joined thematically "
            "rather than chronologically.",
  style="A measured, cadenced prose in the narrator's voice, with long sentences that reproduce the "
        "rhythms of thinking; dialogue in the idiom of Harlem and of musicians; the language of music used "
        "with technical precision; a final passage of great rhetorical power that describes a "
        "performance without quoting it.",
  ctx="Published in Partisan Review, vol. 24, no. 3, in the summer of 1957, when Baldwin was already known "
      "for Go Tell It on the Mountain and Notes of a Native Son; collected in Going to Meet the Man (Dial "
      "Press, 1965). It belongs to the great period of American jazz writing and to the literature of "
      "Harlem at the beginning of the civil rights movement, and it is Baldwin's most widely anthologised "
      "short story.",
  sig="One of the finest American short stories of the century and Baldwin's most widely taught fiction; it "
      "is a standard anthology text and a set text in courses on the American short story, on African "
      "American literature and on the literature of music, and its last pages are among the most discussed "
      "in American fiction.",
  canon="Major canon",
  crit="Criticism reads the story as a study in the ethics of listening, as a blues narrative whose form "
       "imitates the music it describes, and as Baldwin's most successful attempt to hold the private and "
       "the political in a single story; the figure of Creole, the function of Grace's death and the "
       "relation of the story to Baldwin's own Harlem childhood have all been discussed at length.",
  biblio="First published in Partisan Review, vol. 24, no. 3 (Summer 1957); collected in Going to Meet the Man "
         "(New York: Dial Press, 1965) and in Early Novels and Stories (Library of America, 1998). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows published descriptions and the passages quoted "
        "in the sources consulted, and the record says so.",
  ver="partially verified", sources=[W_SB, W_JBA, NAAL]),
W10("Going to Meet the Man", JBA, "1965", "Short story", "significant",
  genres=G("Short Story", "Gothic Fiction", "Realist Fiction"),
  themes=T("Race, racism and the struggle for civil rights", "Violence, crime and justice", "Sexuality, desire and the closet"),
  movements=M(BAM, SOG),
  overview="A story published in Status in October 1965 and collected as the title story of Going to Meet the "
           "Man (1965): a white Southern deputy sheriff, impotent in bed, remembers his father taking him to "
           "a lynching when he was eight years old and finds himself excited by the memory.",
  content="A story that moves between a white sheriff's bedroom in the present and two memories - an assault "
          "on a young civil rights worker in his cell that day, and the lynching he was taken to watch as "
          "a child - and ends with the violence and the sexual excitement joined together.",
  summary="Jesse, a deputy sheriff in a small Southern town, lies in bed with his wife Grace and cannot make "
          "love to her; his mind wanders to the black women he has known and to the day's work, when he "
          "and another officer arrested a young civil rights worker and Jesse beat him in his cell with "
          "a hose and a cattle prod. The prisoner, half conscious, asks him if he remembers 'Old Julia', "
          "and Jesse realizes that the young man is the grandson of a woman he once cheated in his "
          "mail-order business, and that he had known him as a boy. The beating resumes, and Jesse feels "
          "himself sexually aroused by it. The story then moves back to his childhood: the family car, a "
          "black neighbourhood singing 'Wade in the Water', his father's reassurances, and then the "
          "morning when the white people of the town gather to watch a black man burned and mutilated, "
          "with Jesse on his father's shoulders. In the last pages he comes back to the bedroom and finds "
          "that the memory has given him an erection, and the story ends with him turning to his wife.",
  themes_text="The story is Baldwin's most direct treatment of the sexual logic of American racism: Jesse's "
              "impotence and his excitement are produced by the same system, and the lynching is presented "
              "as the scene in which white masculinity is formed. Its method is to stay inside Jesse's "
              "consciousness, so that the reader experiences the banality of his racism - his "
              "self-justification, his nostalgia, his ordinary marital tenderness - before the "
              "atrocity, and then understands that the atrocity is not an exception to his life but its "
              "foundation. The title's 'going to meet the man' is both the boy's initiation and the "
              "sexual act the memory enables.",
  structure="A single continuous present-tense night interrupted by two flashbacks, one recent and one from "
            "childhood, with the second flashback occupying the centre of the story; the return to the "
            "bedroom in the last paragraph completes the frame and delivers the story's judgement without "
            "comment.",
  style="A third-person narrative confined to Jesse's consciousness, in a flat demotic Southern idiom; the "
        "childhood memory is rendered with the sensory immediacy of a child's perception and without "
        "explanation; the violence is described in exact physical detail, and the story's refusal of "
        "authorial comment is itself the moral instrument.",
  ctx="Published in the magazine Status in October 1965, one month before the collection, and collected as "
      "the title story of Going to Meet the Man (Dial Press, 1965), Baldwin's only collection of short "
      "stories; it appeared at the height of the civil rights movement, two years after The Fire Next Time "
      "and a year after the murders of Chaney, Goodman and Schwerner, and it is one of the few works by a "
      "major Black writer of the period to enter the mind of a white racist.",
  sig="One of the most discussed American short stories of the 1960s and the story through which Baldwin's "
      "treatment of white consciousness is usually taught; it is a standard anthology text on the "
      "literature of lynching and of American racism, and its narrative technique - full sympathetic "
      "access to a perpetrator - is regularly analysed in courses on point of view and on the ethics of "
      "representation.",
  canon="Major canon",
  crit="Criticism reads the story as an anatomy of the psychosexual structure of white supremacy, and debates "
       "the risks of Baldwin's decision to occupy Jesse's point of view; its relation to the Gothic "
       "tradition of the South, to the literature of lynching and to Baldwin's essays of the same years is "
       "the usual frame, and the final paragraph is one of the most discussed endings in American fiction.",
  biblio="First published in Status, October 1965; collected in Going to Meet the Man (New York: Dial Press, "
         "1965). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows published descriptions of the plot and the "
        "passages quoted in the sources consulted.",
  ver="partially verified", sources=[W_GMMS, W_GMM, W_BIB, NAAL]),
]

WORKS += [
W10("Letter to My Nephew", JBA, "1962", "Essay (open letter)", "major",
  genres=G("Personal Essay", "Political Essay", "Nonfiction Prose (1946–2000)"),
  themes=T("Race, racism and the struggle for civil rights", "Family, marriage and domestic life", "History, truth and the uses of the past"),
  movements=M(BAM),
  overview="An open letter published in The Progressive in December 1962, on the hundredth anniversary of the "
           "Emancipation Proclamation, and collected as 'My Dungeon Shook' at the head of The Fire Next Time "
           "(1963): Baldwin writes to his fourteen-year-old nephew about what America has done to him and "
           "what he must refuse.",
  content="A short letter in the second person, in which Baldwin addresses his nephew James by name on the "
          "centenary of emancipation, tells him that the country has set limits on his life before he was "
          "born, refuses both the hatred and the false innocence that the situation offers, and ends by "
          "asking him to accept his own history without accepting the definitions imposed on it.",
  summary="The letter is addressed to Baldwin's nephew and namesake, James, on the hundredth anniversary of "
          "the Emancipation Proclamation, and it begins by acknowledging that the occasion offers no "
          "comfort: 'you were born into a society which spelled out with brutal clarity, and in as many "
          "ways as possible, that you were a worthless human being'. Baldwin tells his nephew what the "
          "country has done to his father and his grandfather, and what it is doing to him, and then "
          "makes the turn that the letter exists for: he must not believe it, and he must not hate, "
          "because the hatred would be a second submission to the same lie. He explains that the white "
          "American is also trapped, in a dream of innocence that requires the Black American to carry "
          "the burden of the history he refuses to know, and he asks his nephew to accept his own "
          "humanity and his own history without accepting the definitions offered to him. The letter ends "
          "with an exhortation to love and to persist, and with the famous sentence about the country's "
          "future being in the hands of those who can say 'we'. Its argument is conducted almost entirely "
          "through the second person: the uncle's authority comes from his love, and the letter's diagnosis "
          "of white innocence is delivered not as theory but as something the boy will need to know in "
          "order to live, which is why the letter reads as both a private gift and a public document.",
  themes_text="The letter's central argument is that American racism damages white Americans as well as Black "
              "ones, because it requires them to believe in an innocence that their history contradicts; "
              "the famous formulation is that the white man's 'innocence' is his crime. Against that, "
              "Baldwin sets the nephew's task: to know his own history, to refuse both self-hatred and "
              "hatred of the other, and to insist on a humanity that is not granted by the country. The "
              "letter is also a family document - the tone of an uncle speaking to a beloved nephew - and "
              "its intimacy is what makes its politics persuasive: the general argument is made through a "
              "particular relationship, and the 'you' of the letter is at once one boy and a generation.",
  structure="A single letter of a few pages, with no sections; it moves from the occasion and the diagnosis, "
            "through the history of the family, to the reversal in which the nephew is told what he must "
            "do, and ends with an exhortation; the second person is maintained throughout, so that the "
            "argument is always addressed to someone.",
  style="Direct address in the second person, with the cadences of the pulpit - repetition, antithesis, "
        "long periodic sentences that resolve into short declaratives; the diction moves between the "
        "colloquial and the prophetic, and the letter's most famous sentences are short and absolute.",
  ctx="Published in The Progressive in December 1962 and collected, slightly revised and retitled 'My Dungeon "
      "Shook: Letter to My Nephew on the One Hundredth Anniversary of the Emancipation', as the first of "
      "the two essays in The Fire Next Time (New York: Dial Press, 1963), which became a bestseller and one "
      "of the defining books of the civil rights movement; the letter was written at the height of the "
      "movement, after the Birmingham campaign and before the March on Washington.",
  sig="One of the most quoted American essays of the century and the standard introduction to Baldwin's "
      "political thought; it is a set text in American literature, history and civics courses, the essay "
      "through which The Fire Next Time is usually taught, and the source of the phrases about innocence "
      "and about the 'we' that recur in American public argument.",
  canon="Major canon",
  crit="Criticism reads the letter as a founding document of the literature of the civil rights movement and "
       "as a masterpiece of the epistolary essay; its argument about white innocence has been enormously "
       "influential in American studies, and its relation to the longer essay that follows it in The Fire "
       "Next Time, and to Baldwin's later writing on the same themes, is the standard critical frame.",
  biblio="First published as 'A Letter to My Nephew' in The Progressive, December 1962; collected as 'My "
         "Dungeon Shook: Letter to My Nephew on the One Hundredth Anniversary of the Emancipation' in The "
         "Fire Next Time (New York: Dial Press, 1963) and in Collected Essays (Library of America, 1998). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The letter was read through the text reprinted by The Progressive and quoted in the sources "
        "consulted; the title used by the anthology, 'Letter to My Nephew', is the periodical title, and "
        "the record gives both.",
  ver="partially verified", sources=[W_PROG, W_JBA, NAAL]),
W10("Good Country People", FOC, "1955", "Short story", "major",
  genres=G("Short Story", "Gothic Fiction", "Satirical Fiction"),
  themes=T("Faith, doubt and the sacred", "Identity, authenticity and the divided self", "Class, labour and social mobility"),
  movements=M(SOG),
  overview="A story published in Harper's Bazaar in June 1955 and collected in A Good Man Is Hard to Find and "
           "Other Stories the same year: a one-legged philosophy doctor who calls herself Hulga is seduced "
           "and robbed of her wooden leg by a Bible salesman who turns out to be a collector of other "
           "people's prostheses.",
  content="A comic and violent story set on a Georgia tenant farm, in which Mrs. Hopewell's educated, angry "
          "daughter Hulga goes walking with a travelling Bible salesman, is seduced into removing her "
          "artificial leg, and is left stranded in a hayloft while he makes off with it.",
  summary="Mrs. Hopewell owns a farm in rural Georgia and employs the tenants Mr. and Mrs. Freeman, whom she "
          "condescends to call 'good country people'. Her daughter Joy, thirty-two, unmarried and "
          "overweight, lost a leg in a shooting accident as a child, has a doctorate in philosophy, and "
          "has changed her name to Hulga in order to spite her mother; she is an atheist who believes in "
          "nothing and treats everyone with contempt. A young Bible salesman, Manley Pointer, arrives at "
          "the door, charms Mrs. Hopewell with his humility and his talk of missionary work, and is "
          "invited to stay for dinner; he mentions a heart condition and shows an interest in Hulga, who "
          "decides to seduce him in order to humiliate his faith. They arrange to meet, and he takes her "
          "into a hayloft, where he asks her to remove her wooden leg and then opens his Bible case to "
          "reveal whiskey, condoms and obscene playing cards. He tells her that he has been collecting "
          "such things for years, takes her leg, mocks her belief in nothing, and leaves her stranded in "
          "the loft. The story ends with Mrs. Hopewell and Mrs. Freeman watching Pointer walk away down "
          "the road and remarking on how simple and good the country people are. The story's ending is a "
          "judgement on them rather than on him: the salesman has taken the leg that stood for Hulga's "
          "self-sufficiency, and her mother and the tenant have seen nothing.",
  themes_text="The story is about the pride of the intellect and the pride of the respectable, and about the "
              "way both are exposed by a young man who is neither honest nor simple. O'Connor's own gloss "
              "- that Hulga 'believes in nothing but her own belief in nothing', and that the wooden leg "
              "is a figure of the wooden part of her soul - is the key to its theology: the leg is both a "
              "literal disability and the symbol of a spiritual deficiency, and it must work as both. The "
              "story's comedy is very dark, and its target is not the Bible salesman, who is a kind of "
              "devil, but the complacency of the women who think they can classify him.",
  structure="A story in three movements - the household and its classifications, the arrival of the salesman "
            "and the dinner, and the date in the hayloft - with a short coda on the road; the point of "
            "view is omniscient and shifts between the women and into Hulga's consciousness for the "
            "seduction, and the reversal comes in a single gesture when the case is opened.",
  style="Comic and exact, with an eye for the absurd detail (the name Hulga, the 'nice girl' with a "
        "doctorate, the obscene cards in a Bible case); dialogue that reproduces the idiom of the rural "
        "South and the pretensions of the educated; a plain narrative voice that never comments on the "
        "atrocity it reports.",
  ctx="First published in Harper's Bazaar in June 1955 and collected in A Good Man Is Hard to Find and Other "
      "Stories (New York: Harcourt, Brace, 1955); O'Connor was living at Andalusia, her mother's farm near "
      "Milledgeville, and the story's tenant farm, its peacocks and its Bible salesmen belong to that "
      "world.",
  sig="One of O'Connor's best-known stories and a standard anthology text; its handling of disability, "
      "gender and belief has made it one of the most discussed American short stories of the 1950s, and "
      "the figure of Hulga is central to the critical literature on O'Connor and on the Southern grotesque.",
  canon="Major canon",
  crit="Criticism reads the story as a comic anatomy of intellectual pride, as a study in the grotesque body "
       "and as one of O'Connor's most successful treatments of grace arriving through violence; feminist "
       "and disability criticism has paid particular attention to Hulga's leg, to the story's treatment of "
       "ugliness as a strategy of refusal, and to the way the narrative uses her body against her.",
  biblio="First published in Harper's Bazaar, June 1955; collected in A Good Man Is Hard to Find and Other "
         "Stories (New York: Harcourt, Brace, 1955) and in The Complete Stories (1971). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows published descriptions and the passages quoted "
        "in the sources consulted, including O'Connor's own commentary on the wooden leg.",
  ver="partially verified", sources=[W_GCP, W_FOC, NAAL]),
]

WORKS += [
W10("A Good Man Is Hard to Find", FOC, "1953", "Short story", "major",
  genres=G("Short Story", "Gothic Fiction", "Realist Fiction"),
  themes=T("Faith, doubt and the sacred", "Violence, crime and justice", "Family, marriage and domestic life"),
  movements=M(SOG),
  overview="A story first printed in the anthology Modern Writing I (Avon, 1953) and collected in A Good Man Is "
           "Hard to Find and Other Stories (1955): a family driving to Florida is murdered by an escaped "
           "convict called the Misfit, and the grandmother's last gesture is one of recognition.",
  content="A story in a single day, from an Atlanta breakfast table through a car journey across Georgia and "
          "a dirt road, to a car accident and a clearing in the woods where a family of six is taken away "
          "and shot by three escaped convicts while the grandmother talks to their leader about Jesus.",
  summary="The grandmother does not want to go to Florida, where a convict called the Misfit is at large, and "
          "would rather visit relatives in east Tennessee; her son Bailey ignores her, and the family sets "
          "out the next morning with the grandmother in the back seat, dressed as a lady in case anyone "
          "should find her body, and with her cat hidden in a basket. On the way she tells the children "
          "stories, complains about their manners, remembers a plantation she once visited, and suddenly "
          "insists that the house with its secret panel is on the road they are taking; Bailey turns off "
          "onto a dirt road, the grandmother realizes that she has remembered the wrong state, and the cat "
          "leaps onto Bailey's neck and the car overturns in a ditch. Three men in a car arrive: the "
          "Misfit, in a black hat and with no shirt, and two boys. While the others are taken into the "
          "woods and shot one by one, the grandmother talks to the Misfit about Jesus and about prayer, "
          "and he explains his own theology - that if Christ raised the dead there is nothing to do but "
          "follow him, and if he did not, there is nothing to do but enjoy the time you have. The "
          "grandmother, hearing the shots, calls him 'one of my own babies' and touches him, and he shoots "
          "her; the story closes with his remark that she would have been a good woman if there had been "
          "somebody there to shoot her every minute of her life.",
  themes_text="The story is about grace arriving at the moment of death, and about the difference between "
              "the grandmother's conventional religion - respectability, manners, the past - and the "
              "Misfit's terrifyingly coherent theology. Its central event is the grandmother's gesture of "
              "recognition: in calling the Misfit one of her own children she does what her whole life of "
              "petty judgement has unfitted her for, and the story gives that moment all the weight of a "
              "conversion. Around it are the story's comic and satirical subjects - the family, the "
              "grandmother's nostalgia for the plantation South, the child June Star's rudeness - which "
              "make the violence at the end both shocking and inevitable.",
  structure="A single linear narrative in unbroken time, moving from the house to the road to the clearing; "
            "the story is full of foreshadowing (the Misfit in the newspaper, the grandmother's dress for "
            "burial, the hidden cat) and the reversal is prepared by the grandmother's own error; the "
            "final sentences are given to the Misfit.",
  style="Comic and exact in its rendering of the family, then suddenly bare; dialogue that reproduces the "
        "idiom of the Georgia family and, in the Misfit, a flatness that is more frightening than any "
        "rhetoric; the violence is reported at a distance and without comment, in the manner of a "
        "newspaper report.",
  ctx="First published in Modern Writing I (New York: Avon, 1953), a multi-author anthology, and collected in "
      "A Good Man Is Hard to Find and Other Stories (Harcourt, Brace, 1955); it is O'Connor's most "
      "anthologised story and one of the most anthologised American stories of the century, and it belongs "
      "to the Southern Gothic tradition of Flannery O'Connor, Carson McCullers and Faulkner.",
  sig="O'Connor's most famous story and one of the most widely anthologised American short stories; it is a "
      "standard course text on the short story, on the Southern Gothic and on the literature of grace, and "
      "its last paragraph is one of the most frequently quoted endings in American fiction.",
  canon="Major canon",
  crit="Criticism reads the story as a theological comedy in which grace comes through violence, and debates "
       "whether the grandmother's final gesture is genuine redemption or a final self-deception; the "
       "Misfit's speech about Christ, the story's treatment of race and class in the Georgia the family "
       "drives through, and O'Connor's own account of the story in Mystery and Manners are all central to "
       "the literature.",
  biblio="First published in Modern Writing I, ed. Willard Maas and Philip Rahv (New York: Avon, 1953); "
         "collected in A Good Man Is Hard to Find and Other Stories (New York: Harcourt, Brace, 1955) and "
         "in The Complete Stories (1971). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The story was not read complete; the summary follows published descriptions of the plot and the "
        "passages quoted in the sources consulted.",
  ver="partially verified", sources=[W_GMHF, W_FOC, NAAL]),
W10("Everything That Rises Must Converge", FOC, "1961", "Short story", "significant",
  genres=G("Short Story", "Realist Fiction", "Social Criticism"),
  themes=T("Race, racism and the struggle for civil rights", "Family, marriage and domestic life", "Class, labour and social mobility"),
  movements=M(SOG),
  overview="A story published in New World Writing in October 1961 and collected as the title story of "
           "Everything That Rises Must Converge (1965): a young man escorts his mother on a newly integrated "
           "bus in a Southern city, and his resentment of her racism ends in her death.",
  content="A single bus journey and the walk that follows it, in which Julian and his mother argue about "
          "race, manners and the family's lost status, a Black woman and her small son board the bus, and "
          "the mother's condescending gesture to the child ends in violence.",
  summary="Julian, a would-be writer in his early twenties, lives with his widowed mother in a Southern city "
          "and takes her to her weight-reducing class at the YMCA every Wednesday evening; because the "
          "buses have been integrated, she will not ride alone, and he escorts her with a mixture of duty "
          "and resentment. On the bus he reflects on his own liberal enlightenment and on his mother's "
          "nostalgia for the family's plantation past - 'they should rise, yes, but on their own side of "
          "the fence' - and he tries, unsuccessfully, to make friends with a well-dressed Black man in "
          "order to annoy her. A large Black woman in an identical hat to his mother's gets on with her "
          "small son, Carver; Julian's mother, delighted, gives the child a penny, and the woman strikes "
          "her with her handbag and walks off. Julian, triumphant, lectures his mother on the lesson she "
          "has received, and she walks faster and faster, then sits down on the kerb and dies of a stroke. "
          "The story ends with Julian running for help, calling her 'Mamma' and entering 'the world of "
          "guilt and sorrow'.",
  themes_text="The title comes from Teilhard de Chardin: everything that rises must converge, and the story "
              "tests that proposition on a Southern city at the beginning of desegregation. Its targets "
              "are double: the mother's genteel racism, which treats Black people as children to be "
              "patted, and Julian's liberal self-congratulation, which is a way of despising his mother "
              "without understanding her. The story's judgement falls on Julian, since his mother's "
              "gesture, for all its condescension, is a gesture of love, and his own response to her "
              "death is the beginning of the knowledge he has pretended to have. The identical hats are "
              "the story's central image: the two women are bound together by class and by a shared "
              "world whether they like it or not.",
  structure="A single continuous scene, from the house to the bus to the kerb, with the story's action "
            "carried almost entirely by dialogue and by Julian's interior commentary; the climax is a "
            "physical gesture rather than an event, and the story closes in the last sentence with a "
            "reversal of its protagonist's whole position.",
  style="Third-person narrative confined to Julian's consciousness, with an irony that turns against him; "
        "long stretches of dialogue in the idiom of the Southern middle class; the story's symbols (the "
        "hats, the penny, the family house) are placed without comment, and the last sentence is long and "
        "rhetorically weighted.",
  ctx="First published in New World Writing in October 1961 and won the O. Henry Award in 1963; collected as "
      "the title story of Everything That Rises Must Converge (New York: Farrar, Straus and Giroux, 1965), "
      "published after O'Connor's death. It is one of the few stories in which O'Connor addresses the "
      "civil rights movement directly, and it was written in the years of the Montgomery bus boycott and "
      "the sit-ins.",
  sig="One of O'Connor's most taught stories and the one through which her treatment of race is usually "
      "discussed; it is a standard anthology text on the Southern Gothic, on the short story and on the "
      "literature of the civil rights era, and its relation to the Teilhard de Chardin title is a set "
      "topic in courses on O'Connor.",
  canon="Major canon",
  crit="Criticism reads the story as O'Connor's most direct engagement with desegregation, and debates "
       "whether its irony is directed at the mother, at Julian, or at the liberal reader; the story's use "
       "of the doubled hats, its treatment of the Black woman (who is given no interiority) and the "
       "theological meaning of the ending have all been contested, and it is central to the discussion of "
       "race in O'Connor's work.",
  biblio="First published in New World Writing, October 1961; collected in Everything That Rises Must "
         "Converge (New York: Farrar, Straus and Giroux, 1965) and in The Complete Stories (1971). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows published descriptions of the plot and the "
        "passages quoted in the sources consulted.",
  ver="partially verified", sources=[W_ETR, W_FOC, NAAL]),
]

WORKS += [
W10("Howl", AG, "1956", "Poem (free verse, three parts)", "major",
  genres=G("Free Verse", "Political Poetry", "Confessional Poetry"),
  themes=T("Alienation, absurdity and existential freedom", "Madness, breakdown and confinement", "Sexuality, desire and the closet"),
  movements=M(BEAT),
  overview="Written in 1954-55, read at the Six Gallery in San Francisco in October 1955 and published in Howl "
           "and Other Poems (City Lights, 1956): a long poem in three parts and a footnote that names the "
           "generation destroyed by madness, denounces the god Moloch, and ends in the Rockland asylum with "
           "Carl Solomon.",
  content="A long poem in three parts plus a footnote: a catalogue of the 'best minds' of the postwar "
          "generation and their destruction in the cities, the prisons and the asylums; a litany of the god "
          "Moloch who consumes them; an address to Carl Solomon in the Rockland asylum; and a final "
          "declaration that everything is holy.",
  summary="Part I is a long catalogue of the people Ginsberg knew or had heard of in the postwar American "
          "underground - 'I saw the best minds of my generation destroyed by madness, starving hysterical "
          "naked' - and it follows them through the cities, the colleges, the prisons, the psychiatric "
          "wards, the jazz clubs and the beds of the late 1940s and early 1950s: those who 'dragged "
          "themselves through the negro streets at dawn looking for an angry fix', who 'poverty and "
          "obscurity and sixty-five-dollar-a-week jobs', who took drugs, were arrested, were "
          "institutionalized, were lovers, were poets. Part II turns on Moloch, the god of the "
          "mechanical civilization, in an incantatory litany that names the buildings, the factories, the "
          "universities, the Pentagon, the prisons and the human sacrifice they require. Part III "
          "addresses Carl Solomon directly - 'Carl Solomon! I'm with you in Rockland' - and answers each "
          "of Solomon's statements with a declaration of solidarity that has the structure of a "
          "liturgy. The 'Footnote to Howl' adds a final litany in which everything - 'the world is holy! "
          "the soul is holy! the skin is holy! the nose is holy!' - is declared holy, ending the poem in "
          "affirmation rather than denunciation.",
  themes_text="The poem's central subject is the destruction of the gifted by a society that institutionalizes, "
              "criminalizes and commodifies them, and its method is testimony: the catalogue form means "
              "that the poem does not argue but names, and the accumulation of specific lives gives it "
              "its authority. Part II shifts from persons to the system that consumes them, and the "
              "figure of Moloch gathers capitalism, war, psychiatry, sexuality and the city into a "
              "single image. Part III turns the poem into an act of solidarity, and the Footnote turns it "
              "into a blessing: the movement from indictment to sanctification is the poem's argument "
              "about what poetry can do, and its treatment of sexuality and of the body as holy was "
              "scandalous in 1956 in a way that later readings have sometimes obscured.",
  structure="Three numbered parts and a footnote: Part I is a single sentence of some seventy-eight long "
            "lines with anaphora ('who...') as its organizing device; Part II is a shorter litany built on "
            "'Moloch'; Part III is a dialogue-address to Solomon in the asylum, with the refrain 'I'm "
            "with you in Rockland'; the Footnote returns to the litany form and closes with 'Holy! "
            "Holy! Holy!' in a deliberate echo of religious chant.",
  style="The long breath-line, measured by the length of one exhalation rather than by foot or syllable; "
        "parataxis and catalogue; anaphora and repetition taken from Hebrew liturgy and from jazz; a "
        "diction that includes slang, obscenity, technical terms and the names of real people and places; "
        "spontaneity of composition (Ginsberg typed the first draft in a single session) with heavy "
        "subsequent revision.",
  ctx="Begun in the autumn of 1954 and read in public for the first time at the Six Gallery in San Francisco on "
      "7 October 1955, a reading now regarded as the founding event of the Beat movement; published by "
      "Lawrence Ferlinghetti's City Lights Books in Howl and Other Poems (1956), which was seized and "
      "prosecuted for obscenity, and cleared by Judge Clayton Horn on 3 October 1957 in a ruling that "
      "became a landmark of American free expression. The poem was written at the height of McCarthyism "
      "and of the conformity of the Eisenhower years, and it is dedicated to Carl Solomon, whom Ginsberg "
      "had met in the Columbia Presbyterian psychiatric institute in 1949.",
  sig="The founding poem of the Beat Generation and one of the most influential American poems of the "
      "century; the obscenity trial made it a cause and its publication a turning point in American "
      "literary censorship, it is a standard anthology and course text, and its first line is among the "
      "most recognisable in modern poetry.",
  canon="Major canon",
  crit="Criticism reads the poem as prophecy, as elegy for a generation, as a gay manifesto, as a "
       "document of American psychiatry and as a formal revolution in the American line; its relation to "
       "Whitman's catalogues, to Williams's variable foot and to Hebrew liturgical poetry has been "
       "extensively discussed, and the obscenity trial is a standard case in the history of American "
       "censorship.",
  biblio="Written 1954-55; first read at the Six Gallery, San Francisco, 7 October 1955; published in Howl and "
         "Other Poems (San Francisco: City Lights Books, Pocket Poets Series no. 4, 1956); collected in "
         "Collected Poems 1947-1997 (2006). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The poem was read in the published text; quotations are short and confined to the lines for which "
        "it is universally known. The date of the Six Gallery reading (7 October 1955) follows the sources "
        "consulted; some accounts give only the month.",
  ver="partially verified", sources=[W_HOWL, NAAL]),
]
