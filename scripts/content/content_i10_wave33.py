"""Installment 10, wave 33: Brathwaite's last English row, and three American poets.

Four authors, nine works. Kamau Brathwaite's "[On Sycorax Video Style]" is the last
outstanding row of the English anthology (96 in-scope, 94 recorded before this wave).
Bob Dylan, Simon J. Ortiz and Louise Glueck are new to the database, with two, three
and three works.

The wave also settles the last two provisional dates in the American list: Ortiz's
"Passing through Little Rock" is from A Good Journey (Turtle Island Foundation, 1977)
and "Earth and Rain, the Plants & Sun" from Going for the Rain (Harper & Row, 1976),
both established from the contents of Woven Stone (1992), which reprints the three
collections in full. With this wave no selection in either list carries an unverified
date.

First printings used here:

    Brathwaite, "[On Sycorax Video Style]"  conVERSations with Nathaniel Mackey (We Press, 1999)
    Bob Dylan, "It's Alright, Ma"           Bringing It All Back Home (Columbia, 22 March 1965)
    Bob Dylan, "Like a Rolling Stone"       Columbia single 4-43346, 20 July 1965
    Ortiz, "Earth and Rain, the Plants & Sun"  Going for the Rain (1976)
    Ortiz, "Passing through Little Rock"    A Good Journey (1977), p. 98 in Woven Stone
    Ortiz, From Sand Creek                   Thunder's Mouth Press, 1981
    Glueck, "The Drowned Children"          Descending Figure (Ecco, 1980)
    Glueck, "Descending Figure"             Descending Figure (1980)
    Glueck, "Vespers"                       The Wild Iris (Ecco, 1992)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL, NAAL  # noqa: E402

KB = "Kamau Brathwaite"
BD = "Bob Dylan"
SJO = "Simon J. Ortiz"
LG = "Louise Glück"

CAR = "Caribbean Literature in English"
POSTCOL = "Postcolonial Literature"
NAR = "Native American Renaissance"
BEAT = "The Beat Generation"
CONF = "Confessional Poetry"

W_KB = "Kamau Brathwaite (Wikipedia)"
CONV = "Sycorax video style and conVERSations with Nathaniel Mackey"
MACK = "CONVERSATIONS WITH NATHANIEL MACKEY (Rain Taxi review)"
W_BD = "Bob Dylan (Wikipedia)"
BIABH = "Bringing It All Back Home"
LARS = "Like a Rolling Stone (single)"
W_SJO = "Simon J. Ortiz (Wikipedia) and the Poetry Foundation author page"
GFR = "Going for the Rain"
AGJ = "A Good Journey"
WOVEN = "Woven Stone"
FIGHT = "Fight Back: For the Sake of the People, for the Sake of the Land"
ORTIZ_LIT = "Simon J. Ortiz, Native American Poet and Storyteller (nativeamericanlit.com survey)"
W_LG = "Louise Glück (Wikipedia) and the Nobel Prize citation"
DESC = "Descending Figure"
WILD = "The Wild Iris"

AUTHORS = [
A10(BD, MAJ, "1941", None, "Duluth, Minnesota, United States",
  "American; singer-songwriter and poet writing in English",
  "American songwriter who carried the literary ambitions of the folk revival into rock and made the "
  "song lyric a subject of academic study; Nobel Laureate in Literature 2016",
  "Bob Dylan was born Robert Allen Zimmerman in Duluth, Minnesota, on 24 May 1941 and grew up in "
  "Hibbing, on the Mesabi Iron Range; he took the name Dylan in 1962, the year his first album "
  "appeared. He moved to New York in January 1961, played the folk clubs of Greenwich Village, and "
  "released The Freewheelin' Bob Dylan (1963), which made him the leading songwriter of the American "
  "folk revival with 'Blowin' in the Wind' and 'A Hard Rain's a-Gonna Fall'. Another Side of Bob "
  "Dylan (1964) began the turn away from protest, and Bringing It All Back Home (March 1965) split "
  "its sides between acoustic and electric music; the single 'Like a Rolling Stone' (July 1965) and "
  "the album Highway 61 Revisited followed, and the electric set at the Newport Folk Festival in July "
  "1965 became the symbolic break between folk and rock. Blonde on Blonde (1966), John Wesley Harding "
  "(1967), Nashville Skyline (1969), Blood on the Tracks (1975), Desire (1976), Infidels (1983), Oh "
  "Mercy (1989), Time Out of Mind (1997), 'Love and Theft' (2001), Modern Times (2006), Tempest "
  "(2012) and Rough and Rowdy Ways (2020) followed across six decades. His prose includes Tarantula "
  "(1971) and the memoir Chronicles: Volume One (2004). He was awarded the Nobel Prize in Literature "
  "in 2016 'for having created new poetic expressions within the great American song tradition', the "
  "first such prize for a songwriter, and delivered his Nobel lecture in 2017.",
  "Studio albums: Bob Dylan (1962), The Freewheelin' Bob Dylan (1963), The Times They Are a-Changin' "
  "(1964), Another Side of Bob Dylan (1964), Bringing It All Back Home (1965), Highway 61 Revisited "
  "(1965), Blonde on Blonde (1966), John Wesley Harding (1967), Nashville Skyline (1969), Self "
  "Portrait (1970), New Morning (1970), Pat Garrett and Billy the Kid (1973), Dylan (1973), Planet "
  "Waves (1974), Blood on the Tracks (1975), The Basement Tapes (1975), Desire (1976), Street-Legal "
  "(1978), Slow Train Coming (1979), Saved (1980), Shot of Love (1981), Infidels (1983), Empire "
  "Burlesque (1985), Knocked Out Loaded (1986), Down in the Groove (1988), Oh Mercy (1989), Under "
  "the Red Sky (1990), Good as I Been to You (1992), World Gone Wrong (1993), Time Out of Mind "
  "(1997), 'Love and Theft' (2001), Modern Times (2006), Together Through Life (2009), Christmas in "
  "the Heart (2009), Tempest (2012), Shadows in the Night (2015), Fallen Angels (2016), Triplicate "
  "(2017), Rough and Rowdy Ways (2020) and Shadow Kingdom (2023). Books: Tarantula (1971), Writings "
  "and Drawings (1973), Lyrics 1962-1985 (1985), Chronicles: Volume One (2004), The Philosophy of "
  "Modern Song (2022).",
  "Long, accumulating stanzas built from short end-stopped phrases; surreal and collaged imagery "
  "drawn from the newspaper, the Bible, the blues and the folk song; a voice pitched between the "
  "preacher and the street hustler; refrain and repetition used as musical rather than logical "
  "structure; and a habit of addressing a 'you' whose identity shifts within the song.",
  "The individual against a society that has made a fool of him; the mutability of fortune; love and "
  "its betrayals; the American past and its myths, from the Civil War to the Depression; the "
  "prophetic and the biblical; and, after 1979, an explicit religious vocabulary that has divided "
  "his critics ever since.",
  "Dylan's Nobel Prize in 2016 settled, at least officially, a question the academy had argued for "
  "fifty years: whether the song lyric belongs to literature. The award cited 'new poetic "
  "expressions within the great American song tradition', and the two songs the Norton Anthology of "
  "American Literature prints - 'Like a Rolling Stone' and 'It's Alright, Ma (I'm Only Bleeding)' - "
  "are the pair on which that claim most often rests, both from 1965, the year he moved from acoustic "
  "protest to electric poetry.",
  bib_status="incomplete",
  bib_note="The albums and books above come from Wikipedia's article on Dylan, checked against "
           "album discographies and the Nobel citation; they were not checked against a printed "
           "bibliography, and the many singles, outtakes, live releases and Bootleg Series volumes "
           "are not listed. Installment 10 records two Norton selections, both songs from 1965; every "
           "other song and album has no record, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_BD, BIABH, LARS, NAAL]),
A10(SJO, SEC, "1941", None, "Albuquerque, New Mexico, United States",
  "American; poet, short-story writer and essayist of Acoma Pueblo writing in English",
  "Acoma Pueblo poet and storyteller, a central figure of the Native American Renaissance, whose "
  "sequence-poems of journey, rain and continuance made the oral tradition of his people a form of "
  "American poetry",
  "Simon Joseph Ortiz was born in Albuquerque, New Mexico, on 27 May 1941 and was raised in the Acoma "
  "Pueblo village of McCarty, in an Acoma-speaking family; his father was a stonemason, carpenter and "
  "woodcarver, and Ortiz has described how the older people's stories and songs formed his sense of "
  "language. He was educated at Fort Lewis College and the University of New Mexico, where he took an "
  "MFA in 1981, and worked in various jobs before teaching. His first chapbook, Naked in the Wind, "
  "appeared in 1971; a long manuscript was then divided into Going for the Rain (Harper & Row, 1976) "
  "and A Good Journey (Turtle Island Foundation, 1977), the two books that made him, with Leslie "
  "Marmon Silko and James Welch, one of the founders of the Native American Renaissance. Fight Back: "
  "For the Sake of the People, for the Sake of the Land (1980) turned to the uranium belt of New "
  "Mexico and the tercentenary of the Pueblo Revolt; From Sand Creek (1981) is his best-known single "
  "book, a sequence on the 1864 massacre of Cheyenne and Arapaho people and on the condition of the "
  "Native American veteran. Woven Stone (1992) collected the three earlier books with a long preface, "
  "and After and Before the Lightning (1994) followed a winter on the Rosebud Sioux reservation. He "
  "has taught at the University of New Mexico, the University of Toronto and Arizona State "
  "University, edited the journal Puerto del Sol, and served as lieutenant governor of the Pueblo of "
  "Acoma.",
  "Poetry: Naked in the Wind (1971), Going for the Rain (1976), A Good Journey (1977), Fight Back: "
  "For the Sake of the People, for the Sake of the Land (1980), From Sand Creek (1981), Woven Stone "
  "(1992, collecting the three previous books), After and Before the Lightning (1994) and Out There "
  "Somewhere (2002). Prose: Song, Poetry and Language (1977), A Poem Is a Journey (1982), the stories "
  "in Men on the Moon (1999) and the essay collections Speaking for the Generations (1998) and The "
  "Good Rainbow Road (2002).",
  "A plain, spoken line, often very short, with almost no punctuation; repetition and refrain carried "
  "over from song and prayer; narrative sequences rather than single lyrics, organised as journeys; "
  "direct address to a child, a listener or a place; and a vocabulary that keeps Acoma words and "
  "place-names untranslated.",
  "Journey and return, and the land as a source of identity; rain, drought and the shiwana, the "
  "rainmakers of Pueblo religion; fatherhood and the teaching of children; the survival of the Pueblo "
  "peoples since the Spanish conquest; the uranium mines and the exploitation of Indian labour; the "
  "massacres of the nineteenth century, especially Sand Creek; and language itself as the means by "
  "which a people continues.",
  "Ortiz is one of the three or four writers by whom the Native American Renaissance is dated, and "
  "the Norton Anthology of American Literature prints five of his poems, of which three fall inside "
  "the period. His insistence that the poem is a form of continuance rather than a private "
  "artefact - 'the only way to continue is to tell a story' - made him the theorist as well as the "
  "practitioner of a literature written for a community, and his influence runs through the Native "
  "writing of the following decades.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia, the Poetry Foundation and Gale author "
           "pages and a survey of his career at nativeamericanlit.com, checked against the contents "
           "of Woven Stone (1992); they were not checked against a printed bibliography, and the "
           "essays, chapbooks and edited volumes are not all listed. Installment 10 records three "
           "Norton selections - 'Earth and Rain, the Plants & Sun', 'Passing through Little Rock' and "
           "the excerpt from From Sand Creek - so the other collections, the stories and the essays "
           "have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_SJO, GFR, AGJ, WOVEN, ORTIZ_LIT, NAAL]),
A10(LG, MAJ, "1943", "2023", "New York City, United States",
  "American; poet and essayist writing in English",
  "American poet whose spare, myth-haunted lyrics of family, grief and the divine won the Nobel Prize "
  "in Literature in 2020, the first American poet to be so honoured since 1993",
  "Louise Elisabeth Glück was born in New York City on 22 April 1943, the daughter of a businessman "
  "who had wanted to be a writer, and grew up on Long Island; she has said that her childhood was "
  "dominated by the death of an older sister before she was born and by a period of anorexia in her "
  "teens, during which she began psychoanalysis and, at seventeen, left school for it. She studied at "
  "Sarah Lawrence College and Columbia University, published Firstborn in 1968, and then wrote almost "
  "nothing for several years while teaching; The House on Marshland (1975) established the voice, and "
  "Descending Figure (1980), The Triumph of Achilles (1985, the National Book Critics Circle Award), "
  "Ararat (1990), The Wild Iris (1992, the Pulitzer Prize), Meadowlands (1996), Vita Nova (1999), The "
  "Seven Ages (2001), Averno (2006), A Village Life (2009), Faithful and Virtuous Night (2014, the "
  "National Book Award) and Winter Recipes from the Collective (2021) followed. Her essays are "
  "collected in Proofs and Theories (1994) and American Originality (2017). She taught at Williams "
  "College, was Poet Laureate of the United States from 2003 to 2004, and was awarded the Nobel Prize "
  "in Literature in 2020 'for her unmistakable poetic voice that with austere beauty makes individual "
  "existence universal'. She died in Cambridge, Massachusetts, on 13 October 2023.",
  "Poetry: Firstborn (1968), The House on Marshland (1975), Descending Figure (1980), The Triumph of "
  "Achilles (1985), Ararat (1990), The Wild Iris (1992), Meadowlands (1996), Vita Nova (1999), The "
  "Seven Ages (2001), Averno (2006), A Village Life (2009), Poems 1962-2012 (2012), Faithful and "
  "Virtuous Night (2014) and Winter Recipes from the Collective (2021). Essays: Proofs and Theories "
  "(1994), American Originality (2017).",
  "Short, unrhymed and usually unpunctuated lines; a plain declarative syntax that turns, without "
  "warning, into myth; the first person used as a mask rather than a confession; sequences and "
  "recurring personae (the flowers and the gardener in The Wild Iris, the family of Ararat); and an "
  "ending that is usually a single hard sentence with no hedge in it.",
  "Family and its injuries, especially the father and the sister; grief and the work of mourning; the "
  "mythological and biblical stories that give private loss a public shape - Persephone, Orpheus and "
  "Eurydice, Abraham and Isaac; the garden and the seasons as a language for the divine; and, in the "
  "later books, old age, memory and the approach of death.",
  "Glück is the central American lyric poet of the last half-century and the only American poet to "
  "have received the Nobel Prize since Toni Morrison's fiction was honoured in 1993. The Wild Iris is "
  "the book by which that award was most often justified, and it is the volume from which the Norton "
  "Anthology of American Literature takes 'Vespers'; Descending Figure, from a decade earlier, is the "
  "book in which the mythic method of her maturity first appears.",
  bib_status="substantially complete",
  bib_note="The collections above come from Wikipedia's article on Glück, checked against the Nobel "
           "Prize citation and the contents of Poems 1962-2012; they were not checked against a "
           "printed bibliography, but the poetry collections are believed complete. Installment 10 "
           "records three Norton selections - 'The Drowned Children' and 'Descending Figure' from "
           "Descending Figure (1980) and 'Vespers' from The Wild Iris (1992) - so the essays and the "
           "later collections have no records.",
  ver="verified", sources=[W_LG, DESC, WILD, NAAL]),
]

WORKS = [
W10("[On Sycorax Video Style]", KB, "1999", "Prose statement on poetics (extract from a book of conversations)", "minor",
  genres=G("Literary Manifesto", "Prose Poetry", "Cultural Criticism"), themes=T("Language, writing and the limits of representation",
           "Art, the artist and the creative life", "Decolonisation, the end of empire and the new nation"),
  movements=M(CAR, POSTCOL),
  overview="The eleventh edition of the Norton Anthology of English Literature prints this passage in its "
           "'Born-Digital Literature' cluster, where it is the first item and the oldest, and it is there "
           "as a statement of poetics rather than as a poem: Brathwaite explaining what he calls the "
           "Sycorax video style, the practice of composing on a computer so that the page shows what the "
           "voice is doing. The passage comes from conVERSations with Nathaniel Mackey (Staten Island: We "
           "Press, 1999), the book in which Brathwaite's 1993 public conversation with Mackey at Poet's "
           "House is broken up and reset in the typography it describes.",
  content="The passage sets out the practice and its origin. Brathwaite says that by the time he came to "
          "DreamStories he had developed another technique within his writing, which he calls the Sycorax "
          "video style, in which he tries to visualise hearing: instead of a purely auditory experience of "
          "the poem, he tries to put on the page what sound looks like, using the computer to make things "
          "happen to the words. The style is named for Sycorax, Caliban's mother in The Tempest, the witch "
          "whose magic Prospero takes with the island, and Brathwaite sets it against what he calls "
          "Prospero's book - the printed page of the colonial literary tradition. It emerged after a "
          "sequence of disasters he describes elsewhere in the same book: the death of his wife Doris in "
          "1986, the hurricane and mudslide that destroyed his home, library and archive in Irish Town in "
          "1988, and the armed robbery in Kingston in 1990 after which he could no longer write by hand.",
  summary="The passage is a poetics in miniature, and its argument is that typography is not decoration "
          "but a way of recovering the oral. Brathwaite had spent twenty years arguing, in History of the "
          "Voice and elsewhere, that Caribbean writing in English had been forced into a print system "
          "built for a different language and a different metre, and that nation language carried its "
          "meaning in sound - in stress, in pitch, in the drum. The Sycorax video style is the "
          "technological answer to that argument: if the page cannot carry the voice, then change the "
          "page. Fonts of different sizes, irregular spacing, drawings, symbols and the 'x' of Sycorax "
          "itself are used to make the text perform the sound it describes, so that reading becomes a "
          "kind of hearing. The name is a political choice as well as a literary one. Sycorax never "
          "appears in The Tempest and never speaks; she is the powerful woman whose magic is taken and "
          "whose story is told by her captor, and Brathwaite's style claims her voice back through the "
          "machine that, in his account, her son's descendants now use. The passage's historical honesty "
          "is the part that most criticism now stresses: the style was not a playful experiment but a "
          "response to trauma, developed when Brathwaite could no longer hold a pen, and the computer "
          "became both prosthesis and medium.",
  themes_text="The first subject is the relation between writing and speech, which the passage treats as "
              "a technical problem with a technical solution. The second is colonial literacy: Prospero's "
              "book stands for the whole apparatus by which the colonised were taught to read and were "
              "silenced in the act, and Sycorax stands for the excluded alternative. The third is "
              "disaster and survival, since the style's origin is a sequence of losses and the practice "
              "is a way of writing after them. The fourth is the page itself, treated here as a visual "
              "and political space rather than a neutral container.",
  structure="An extract from a much longer book of conversations: a first-person explanation, moving from "
            "the technical description of the technique to its origin in catastrophe and its naming, "
            "without stanza breaks or a closing cadence.",
  style="The passage is in Brathwaite's own voice, with the characteristics of the late work: "
        "idiosyncratic spelling and capitalisation, the 'x' of Sycorax, sentences that run on and break "
        "off, and a mixture of the technical and the confessional. In the source book the whole passage "
        "is itself set in the video style, which no quotation of it can reproduce.",
  ctx="The practice dates from 1990 and was developed through the 1990s; conVERSations with Nathaniel "
      "Mackey appeared in 1999 from We Press and XCP: Cross-Cultural Poetics, and the earlier DreamStories "
      "(1994), The Zea Mexican Diary (1993) and the revised Middle Passages (Bloodaxe, 1992) are its first "
      "printed instances. The Norton's 'Born-Digital Literature' cluster places the passage at the head of "
      "a line that runs through digital and internet writing of the 2000s, which is a canonising claim "
      "about where electronic literature begins.",
  sig="The passage is the clearest short statement Brathwaite made of the Sycorax video style, and the "
      "eleventh edition's decision to open its 'Born-Digital Literature' cluster with it is the first time "
      "the Norton Anthology of English Literature has treated a Caribbean poet's typographic practice as "
      "the origin of digital literature in English. It is the latest addition to the English volume's "
      "period, and the one this installment records after it was recovered from a wrong date.",
  canon="Minor canon",
  crit="Criticism of the video style is extensive - Stewart Brown's 'Writin in Light' (1995), Nicholas "
       "Laughlin's 'Notes on videolectics' (2007) and the work of Elaine Savory - and it is generally read "
       "as a continuation of the nation language argument by technological means rather than as a break "
       "with it. The passage itself has attracted no separate criticism, since it is one extract from a "
       "book.",
  biblio="First published in conVERSations with Nathaniel Mackey (Staten Island: We Press, 1999); the "
         "Norton extracts it under the title '[On Sycorax Video Style]' in the 'Born-Digital Literature' "
         "cluster at p. 1101. A selection of The Norton Anthology of English Literature, 11th edition, "
         "vol. F.",
  notes="The exact pages of the extract in the source book, and the anthology's precise wording, were not "
        "verified; the record dates the selection to 1999 as its first publication in the nearest "
        "documented form and says so. An earlier pass had dated it after 2000 on the strength of MR/1 "
        "(1998), a date inside the period.",
  ver="partially verified", sources=[CONV, MACK, W_KB, NAEL]),
W10("It's Alright, Ma (I'm Only Bleeding)", BD, "1965", "Song lyric (long stanzas, refrain)", "significant",
  genres=G("Lyric Poetry", "Political Poetry", "Performance Poetry"),
  themes=T("Alienation, absurdity and existential freedom", "Technology, media and consumer society",
           "Violence, crime and justice"),
  movements=M(BEAT),
  overview="'It's Alright, Ma (I'm Only Bleeding)' is the third song of the acoustic second side of Bringing "
           "It All Back Home, released by Columbia on 22 March 1965, and it is the song in which Dylan's "
           "writing leaves the protest song behind. Its long stanzas are a catalogue of what American society does to the "
           "people in it, delivered without a chorus until the refrain arrives at the end of each stanza, "
           "and it is the densest lyric he had written.",
  content="The song opens with 'Darkness at the break of noon' and a sequence of images in which nothing "
          "is what it should be: shadows, the handmade blade, the child's balloon, the sun and moon "
          "eclipsed, and the flat statement that to understand you know too soon, there is no sense in "
          "trying. Its stanzas go on to take in advertising and the salesman's pitch, the preacher, the "
          "judge and the congressman, the poverty that is down the street and the war that is across the "
          "sea, the old who are despised and the young who are bought, and the American habit of dressing "
          "up the same bargain in new language. The refrain states the position: it is all right, ma, he "
          "is only bleeding - the singer is wounded but not dying, and the world that wounds him is not "
          "going to be reformed by the song. The middle stanzas turn on the masks people wear, the false "
          "gods and the masters of war of the earlier songs now generalised into a whole social order, and "
          "the last stanza addresses a 'you' who may be the listener, the singer's own generation, or the "
          "country itself.",
  summary="The song is usually read as Dylan's farewell to protest music, and the reading is right but "
          "crude. What changes in it is not the anger but its target and its tone: the earlier songs had "
          "named men and policies, and this one names a condition. The catalogue method - stanza after "
          "stanza of examples with no narrative and no argument - is borrowed from the folk and blues "
          "songs Dylan had been singing for years, and especially from the talking blues, but its "
          "ambition is literary: the statements are epigrams, and many of them have detached themselves "
          "from the song and become proverbs of the 1960s, 'he not busy being born is busy dying' among "
          "them. The organised religion of the middle stanzas gets the hardest treatment, and the song's "
          "anti-clericalism is the place where its later Christian phase looks most surprising. Formally, "
          "the song's achievement is to make a lyric of seven and a half minutes with no chorus hold a listening audience, "
          "and to do it with an acoustic guitar and a harmonica: the refrain is the only thing repeated, "
          "and it refuses consolation. 'It's alright, ma' is the voice of someone reassuring a mother "
          "while telling her that nothing is alright at all, and that double register - the intimate and "
          "the apocalyptic in one line - is what Dylan's 1965 writing is made of.",
  themes_text="The first subject is the gap between American promises and American arrangements, which "
              "the song records as a series of swindles rather than as a political programme. The second "
              "is the media and advertising that make the swindle acceptable. The third is mortality - "
              "the bleeding of the refrain - and the sense that a life is spent being managed by others. "
              "The fourth is language itself, since the song distrusts every sentence it uses and turns "
              "the distrust into its method.",
  structure="Long stanzas of irregular short lines, each ending with the refrain 'But it's all right, ma, "
            "I'm only bleeding', with no bridge and no chorus proper; a catalogue structure that "
            "accumulates rather than argues.",
  style="Dense, allusive, epigrammatic; internal rhyme and assonance rather than end-rhyme; a nasal, "
        "half-spoken delivery that pushes the lines toward speech; imagery drawn from the Bible, the "
        "fairground, the courtroom and the advertisement; and a refrain whose plainness is its point.",
  ctx="Bringing It All Back Home was released on 22 March 1965, with an electric first side and a "
      "largely acoustic second; the song belongs to the months in which Dylan was breaking with the folk "
      "revival. It was written in the summer of 1964, first performed at a concert in New York on 10 "
      "October 1964, and recorded on 15 January 1965. The escalation of the Vietnam War, the "
      "assassination of Kennedy two years earlier and the civil rights movement's turn to the North form "
      "its public context; the folk revival's argument about what a political song should be is its "
      "immediate literary one.",
  sig="The song is one of the two or three by which Dylan's literary reputation was made, and its lines "
      "are among the most quoted in American popular song. The Norton Anthology of American Literature "
      "prints it with 'Like a Rolling Stone' as the pair that establishes Dylan's claim on the canon, "
      "and the Nobel citation of 2016 is the institutional recognition of that claim.",
  canon="Secondary canon",
  crit="Critics read the song as the pivot from the topical song to the apocalyptic one, and the "
       "talking-blues catalogue as its formal model; Christopher Ricks's close reading in Dylan's Visions "
       "of Sin treats its metaphors as a sustained argument about the value of persons. The song's "
       "anti-clerical stanzas are usually discussed with the Christian albums of 1979-81.",
  biblio="Released on Bringing It All Back Home (Columbia, 22 March 1965), track three of the acoustic "
         "side two; collected in Lyrics 1962-1985 (1985) and every subsequent collection. A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The recording date, first performance and release date are given consistently by contemporary "
        "trade advertising and sessionography summaries; the lyric was not transcribed from a first "
        "pressing for this record.",
  ver="partially verified", sources=[BIABH, W_BD, NAAL]),
W10("Like a Rolling Stone", BD, "1965", "Song lyric (six-minute single, verse and refrain)", "major",
  genres=G("Lyric Poetry", "Narrative Poetry", "Performance Poetry"),
  themes=T("Class, labour and social mobility", "Alienation, absurdity and existential freedom",
           "Identity, authenticity and the divided self"),
  movements=M(BEAT),
  overview="'Like a Rolling Stone' was released as a single by Columbia on 20 July 1965, at six minutes "
           "and a half, at a time when radio would not play a record that long; it is the song on "
           "which Dylan's move to electric music and to a new kind of lyric both became public, and it is "
           "regularly called the greatest record in the history of rock music. It opens Highway 61 "
           "Revisited, released the following month.",
  content="The song addresses a woman who once had everything - she dressed so fine, threw the bums a "
          "dime, laughed at everyone who warned her - and who has now lost it all. Each verse supplies "
          "another scene of her fall: the people she once despised now offer her a place, she is on the "
          "street with nowhere to call home, she is asked to be a mystery tramp or a nobody. The chorus "
          "turns on the question 'How does it feel?' - to be without a home, a complete unknown, like a "
          "rolling stone - and it is asked not as sympathy but as an insistent, almost gloating demand "
          "that she recognise what has happened to her. The last verse describes her being offered a deal "
          "by someone who wants to use her, and the closing lines return to the question with the answer "
          "withheld.",
  summary="The song's originality is usually placed in three things, and all three are literary. The "
          "first is the address: the second person is used with the force of an indictment, and the "
          "singer's position - outside the woman, superior to her fall, and implicated in it - is "
          "unstable enough that listeners have read the song as a portrait of a society and not of a "
          "person. The second is the length and structure: six minutes of verse with no bridge, in which "
          "the chorus does not resolve but escalates, and the band - Al Kooper's organ, Mike Bloomfield's "
          "guitar, the session musicians of the Highway 61 sessions - builds behind a spoken, hectoring "
          "vocal that is closer to a speech than to a song. The third is the language, which is flat and "
          "idiomatic on the surface and full of rolled-up metaphors - the chrome horse with its diplomat, "
          "the princess on the steeple - and which refuses the folk song's clear moral. The song was "
          "recorded on 16 June 1965 in New York, after Dylan had written a long piece of prose that "
          "became the lyric, and it was issued only because a promotional play at the Arthur club in "
          "Manhattan produced enough demand to overrule Columbia's resistance. Its success made the "
          "six-minute single possible and, more importantly, ended the assumption that a pop lyric had to "
          "be about love.",
  themes_text="The first subject is social downfall, treated with an honesty that has no mercy in it and "
              "no moral either: the woman is not a victim and not a villain, and the song refuses both "
              "readings. The second is class and the pretence of bohemian freedom, since the woman's "
              "fall is from a position she thought was free and turns out to have been a loan. The third "
              "is the gaze of the singer, which is the song's real subject: who has the right to ask how "
              "it feels, and what does the asking do to the asker. The fourth is anonymity, the complete "
              "unknown of the chorus, which turns a social fall into a metaphysical one.",
  structure="Five verses and a chorus, with the chorus repeated after each verse and worded almost "
            "identically each time; a six-minute single with no bridge, built on a repeated harmonic "
            "pattern and an escalating arrangement.",
  style="A narrative lyric in the second person with a spoken-sung delivery; colloquial diction with "
        "compressed, surreal images; the rhetorical question as the structural spine; and a studio "
        "arrangement that grows from a snare shot to a full band behind a voice that never becomes "
        "melodic in the conventional sense.",
  ctx="Recorded 16 June 1965 and released on 20 July 1965, five days before the electric set at Newport "
      "that became the symbolic break with the folk revival; it was written in Woodstock in the spring of "
      "1965 and appeared on Highway 61 Revisited in August. Its commercial success - a top-ten single in "
      "the United States, Britain and Australia despite its length - changed what a single could be, and "
      "its reception is the moment the idea of the singer-songwriter as an artist rather than an "
      "entertainer became general.",
  sig="'Like a Rolling Stone' is the most frequently cited record in the history of rock criticism, and "
      "the one by which Dylan's claim on literary study was argued long before the Nobel Prize. It is "
      "printed in the Norton Anthology of American Literature, whose selection of him begins with it, and "
      "the Nobel citation's phrase about new poetic expressions within the great American song tradition "
      "is generally taken to refer to it first.",
  canon="Major canon",
  crit="The critical literature is enormous. Greil Marcus's Like a Rolling Stone: Bob Dylan at the "
       "Crossroads (2005) devotes a book to the record; Christopher Ricks reads it with the English "
       "canon in Dylan's Visions of Sin (2003); and the standard view - that it broke the three-minute "
       "single and the love-song monopoly at once - is shared even by critics who dislike the song's "
       "cruelty. The identification of the woman has been attempted for sixty years and remains "
       "unsettled.",
  biblio="Released as Columbia single 4-43346 on 20 July 1965; the opening track of Highway 61 Revisited "
         "(Columbia, 1965); collected in Lyrics 1962-1985 (1985). A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="Recording and release dates are from sessionography summaries and contemporary trade "
        "advertising; the lyric was not transcribed from a first pressing for this record, and the "
        "identity of the woman addressed has never been established and is not asserted here.",
  ver="partially verified", sources=[LARS, BIABH, W_BD, NAAL]),
W10("Earth and Rain, the Plants & Sun", SJO, "1976", "Poem (short free-verse lines, narrative)", "significant",
  genres=G("Lyric Poetry", "Nature Poetry", "Narrative Poetry"),
  themes=T("Land, place and regional belonging", "Nature, ecology and environmental crisis",
           "Family, marriage and domestic life"),
  movements=M(NAR),
  overview="'Earth and Rain, the Plants & Sun' is in Going for the Rain (New York: Harper & Row, 1976), "
           "Ortiz's first full-length collection, in its closing section 'The Rain Falls'. It is a short "
           "narrative poem about a drive to Colorado with his son Raho, and it is the poem most often "
           "anthologised as an example of how Ortiz makes the Pueblo relationship to land into a lyric.",
  content="The poem begins 'Once near San Ysidro / on the way to Colorado, / I stopped and looked'. The "
          "speaker hears a meadowlark through the smell of fresh-cut alfalfa; his son, Raho, says 'Look, "
          "dad', and a hawk is sweeping its wings through the blue of the wind and the sky. The hawk is "
          "writhing overhead and is addressed as the Bringer, the Thunderer; sunlight falls through cloud "
          "curtains in a straight bright shaft and comes down to earth, to a green plant. The poem ends "
          "with the father's instruction to the child: 'Listen, son, hold my hand'.",
  summary="The poem is short and its method is attention. What happens in it is almost nothing - a car "
          "stops, a bird is seen, rain is coming - and the whole weight of the poem is carried by the "
          "quality of the looking and by the presence of the child. Ortiz's line is very short and almost "
          "unpunctuated, so that the poem reads as a series of perceptions arriving one at a time rather "
          "than as a description organised in advance, and the effect is close to the oral storytelling he "
          "insisted was the source of his work. The hawk is the poem's centre: it is described physically "
          "and then named as the Bringer and the Thunderer, which are attributes of the shiwana, the "
          "rain-bringing spirits of Pueblo religion, and the naming is offered without explanation or "
          "italics. The last movement - the shaft of sunlight falling to a green plant, and the father "
          "telling the son to listen and hold his hand - turns the poem into a transmission: what is being "
          "passed on is not a belief but a way of seeing, and the poem's own short lines are the form that "
          "transmission takes. It is also, quietly, a poem about drought: the rain has not yet fallen, and "
          "the whole poem is tilted towards it.",
  themes_text="The first subject is land and belonging, in the specific sense Ortiz gives them - not "
              "scenery but a relationship of obligation between people, plants, animals and the rain. The "
              "second is fatherhood and instruction, since the poem's addressee is a child and its action "
              "is teaching him to look. The third is the sacred in the ordinary, which Ortiz refuses to "
              "separate from the sensory: the hawk is both a bird and a bringer of rain. The fourth is "
              "ecology, in the precise sense of the interdependence the poem enacts.",
  structure="A single short free-verse poem in a narrative sequence of perceptions, with a turn from "
            "description to invocation (the Bringer, the Thunderer) and a closing address to the child.",
  style="Very short lines, minimal punctuation, lower-case beginnings; a plain vocabulary with a few "
        "Acoma-derived names; repetition of 'it falls'; direct speech from the child; and an ending in "
        "the imperative.",
  ctx="Going for the Rain (1976) was written after the chapbook Naked in the Wind (1971) and came out of "
      "the manuscript Ortiz divided into two books; Harper & Row published it after a delay, and it was "
      "one of the first Native American poetry collections to reach a general trade readership, in the "
      "years following Momaday's House Made of Dawn (1968) and the occupation of Wounded Knee (1973).",
  sig="The poem is among the most anthologised of Ortiz's short lyrics and is regularly taught as an "
      "introduction to the Native American Renaissance's poetics of place; it is a Norton selection. The "
      "record's dating of it to 1976 fills the provisional blank in the Norton list, which carried no date "
      "until wave 33.",
  canon="Secondary canon",
  crit="Critics read the poem with the prologue to Going for the Rain, which invokes the shiwana, and "
       "treat its naming of the hawk as Ortiz's characteristic move - the sacred asserted inside the "
       "descriptive sentence rather than alongside it. The standard survey of his career describes the "
       "book as structured as a journey in four parts with a prologue, and places this poem in the "
       "closing section where the rain arrives.",
  biblio="First published in Going for the Rain (New York: Harper & Row, 1976); reprinted in Woven Stone "
         "(Tucson: University of Arizona Press, 1992). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The text was read for this record from the poem as printed in the anthology and quoted in "
        "teaching material. The page in Woven Stone was not established; the 1976 date rests on the "
        "collection's contents and the reviews of it.",
  ver="partially verified", sources=[GFR, WOVEN, ORTIZ_LIT, W_SJO, NAAL]),
W10("Passing through Little Rock", SJO, "1977", "Poem (free verse, short lines)", "significant",
  genres=G("Lyric Poetry", "Social Poetry", "Political Poetry"),
  themes=T("History, truth and the uses of the past", "Race, racism and the struggle for civil rights",
           "Land, place and regional belonging"),
  movements=M(NAR),
  overview="'Passing through Little Rock' is in A Good Journey (Berkeley: Turtle Island Foundation, "
           "1977), Ortiz's second collection; Woven Stone's contents place it at page 98. It is a poem "
           "about driving through an American city that has buried the Indian peoples who lived there, "
           "and it is the sharpest of his short political lyrics.",
  content="The poem opens with the old Indian ghosts - 'Quapaw', 'Waccamaw' - which are 'just billboard "
          "words in this crummy town'. It goes on to describe the speaker passing through Little Rock, "
          "Arkansas, and the poem's closing movement is a wish for escape: 'I just want to cross the next "
          "hill, / through that clump of trees / and come out on the other side / and see a clean river, "
          "/ the whole earth new / and hear the noise it makes / at birth.'",
  summary="The poem's argument is made by the collision of two kinds of name. Quapaw and Waccamaw are the "
          "peoples of the region through which the speaker is driving - the Quapaw gave Arkansas its name "
          "by a chain of French transliterations - and the poem finds them surviving only as words on "
          "billboards, which is to say as tourist signage, while the town itself is crummy, ordinary, and "
          "indifferent. Ortiz's short flat lines refuse the elegiac register that the material would "
          "invite; the anger is in the adjective and in the quotation marks around the tribal names, which "
          "mark them as someone else's speech. The turn at the end is not to lament but to a wish for "
          "birth - a clean river, a new earth, the noise it makes being born - and the wish is placed "
          "beyond the next hill, which means it is not available where the speaker is. That structure, in "
          "which the poem's hope is located outside the poem's own landscape, is characteristic of Ortiz's "
          "political writing, and it is why the poem can be read both as a critique and as a prayer. Its "
          "anger is understated and its formal means are very small: a handful of short lines, one "
          "quotation, one wish.",
  themes_text="The first subject is the erasure of Native peoples from the American landscape and their "
              "survival as brand names, which the poem renders as a fact of the roadside. The second is "
              "the American town as an ordinary place of forgetting, crummy rather than monstrous. The "
              "third is hope figured as geography, since what the speaker wants lies over the next hill. "
              "The fourth is naming and history, because the poem's whole charge depends on the reader "
              "knowing that the billboard words are the names of nations.",
  structure="A short free-verse poem in two movements: the description of the town and its billboard "
            "names, then the wish to cross the next hill, ending on the image of the earth being born.",
  style="Short unpunctuated lines; flat, deliberate colloquialism ('crummy town'); tribal names in "
        "quotation marks; a turn from statement to wish; and an ending in sensory immediacy.",
  ctx="A Good Journey appeared in 1977, the year of Silko's Ceremony, and belongs to the decade in which "
      "Native American writing entered the American literary mainstream; the poem's occasion is a road "
      "trip through the South, and its subject is the relation between the places Native people were "
      "removed from and the places they are driven through. Little Rock carries its own history of "
      "segregation, which the poem leaves implicit.",
  sig="The poem is a frequent anthology choice for the political side of Ortiz's work and is one of the "
      "three Ortiz selections in the Norton's period. Its record is also one of the two in which the "
      "last American dates were settled, from the contents of Woven Stone.",
  canon="Secondary canon",
  crit="Kenneth Lincoln's early survey of Ortiz reads the poem within the A Good Journey sequence as one "
       "of its encounters with the non-Indian world; critics of the anthology have used it to make the "
       "point that the Norton's own annotation of the Quapaw and Waccamaw as tribes of Arizona is wrong, "
       "since both are peoples of Arkansas. The error is the anthology's, not the poem's.",
  biblio="First published in A Good Journey (Berkeley: Turtle Island Foundation, 1977); reprinted in "
         "Woven Stone (Tucson: University of Arizona Press, 1992), p. 98. A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem's date and its place in A Good Journey rest on Woven Stone's contents list; the "
        "reading above is of the portions of the text quoted in reviews and criticism, not of a complete "
        "transcription.",
  ver="partially verified", sources=[AGJ, WOVEN, ORTIZ_LIT, W_SJO, NAAL]),
W10("From Sand Creek", SJO, "1981", "Poem sequence (book-length, mixed forms)", "major",
  genres=G("Elegiac Poetry", "Political Poetry", "Long Poem"),
  themes=T("History, truth and the uses of the past", "Violence, crime and justice",
           "Memory, trauma and testimony", "War, combat and its aftermath"),
  movements=M(NAR),
  overview="From Sand Creek (New York: Thunder's Mouth Press, 1981) is Ortiz's best-known book: a sequence "
           "that takes the massacre of Cheyenne and Arapaho people at Sand Creek, Colorado, in 1864 and "
           "sets it against the condition of Native American veterans in the 1970s, when Ortiz was working "
           "with patients at a Veterans Administration hospital. The Norton prints an excerpt, and it is "
           "the one book-length work of his in the anthology.",
  content="The sequence is in three parts. The first and third are lyrics in Ortiz's short unpunctuated "
          "lines, many of them spoken by a veteran or by the poet in the hospital, and they record ordinary "
          "American life - the ward, the bus, the town, the television - alongside the aftermaths of the "
          "war in Vietnam. The middle part is a prose history of the Sand Creek massacre of 29 November "
          "1864, in which a Colorado volunteer regiment under John Chivington attacked a camp of Cheyenne "
          "and Arapaho under Black Kettle, who had been told they were under army protection, and killed "
          "some two hundred people, most of them women, children and old men. Across the sequence, lines "
          "recur as refrains - 'it is not a story' among them - and the book's spacing and typography put "
          "the historical prose and the contemporary lyric on the same page.",
  summary="From Sand Creek is the book in which Ortiz's two subjects, the survival of Native peoples and "
          "the damage done to individual Native men, become one argument. The massacre is presented as "
          "documentary - the sequence quotes and paraphrases the record, and in an afterword Ortiz names "
          "his sources - and the lyrics around it are what the documentary cannot hold: the boredom of the "
          "hospital, the drinking, the ordinary tenderness of a friend, the speaker's sense that the "
          "history he is writing down is happening in his own body. The refrains do the structural work, "
          "returning the reader to the same few sentences so that they acquire the force of a liturgy, and "
          "the effect is closer to a memorial service than to a history. Ortiz has said that the book grew "
          "out of his time at the Fort Lyon Veterans Administration Hospital in Colorado, where he came to "
          "see the veterans he met as casualties of the same long war, and that intention is what makes "
          "the book's politics more than topical: the Sand Creek of 1864 and the Vietnam of the 1970s are "
          "treated as one event with two dates. Its formal innovation, which later Native writing has "
          "often followed, is the combination of verse and document without hierarchy, so that the archive "
          "and the poem are given equal weight and neither is allowed to explain the other.",
  themes_text="The first subject is the Sand Creek massacre itself, recorded as fact and refused as "
              "spectacle. The second is the continuity of violence against Indigenous peoples from the "
              "nineteenth-century frontier to the twentieth-century war, which the structure of the book "
              "asserts by juxtaposition. The third is trauma and testimony, since the veterans of the "
              "1970s speak in the same book as the survivors of 1864. The fourth is survival and "
              "continuance, which Ortiz's work never abandons: the book is a memorial, but it is also an "
              "argument that the people are still here.",
  structure="A three-part sequence, with lyrics enclosing a prose historical middle section, recurring "
            "refrains across the parts, and a typography that leaves space on the page as part of the "
            "form; an afterword documents the sources.",
  style="Short unpunctuated lyric lines and plain declarative prose; repetition of a small number of "
        "sentences as refrains; documentary quotation; no ironic distance; and a flatness of tone that "
        "refuses both outrage and consolation.",
  ctx="Published in 1981, in a period of renewed Native American political organisation and of public "
      "argument about the Vietnam veteran; Ortiz was working at the Fort Lyon VA hospital in Colorado "
      "when the book was conceived, and its publication by Thunder's Mouth Press put it in the small "
      "press circuit that carried much Native writing of the 1970s and 1980s.",
  sig="From Sand Creek is the most studied single book by an Acoma writer and one of the central texts of "
      "the Native American Renaissance; it won the Pushcart Prize for poetry and is the reason Ortiz is "
      "often described as the poet of continuance. The Norton Anthology of American Literature prints an "
      "excerpt, and the book is a standard presence on American literature syllabi.",
  canon="Major canon",
  crit="Criticism reads the book's mixing of genres as its main achievement and its refrains as the device "
       "that holds the two histories together; it is usually discussed with Silko's Ceremony and with the "
       "documentary poetics of the 1970s. The comparison with Whitman - a long American poem that includes "
       "everything - is common and usually qualified by the observation that Ortiz's inclusiveness is "
       "forensic rather than celebratory.",
  biblio="First published as From Sand Creek (New York: Thunder's Mouth Press, 1981); reissued by the "
         "University of Arizona Press in 2000. The Norton prints an excerpt. A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The sequence was not read in full for this record; the description rests on the published "
        "accounts of its structure, its three parts and its refrains. The details of the massacre are "
        "given as the book and the standard histories give them.",
  ver="partially verified", sources=[FIGHT, WOVEN, ORTIZ_LIT, W_SJO, NAAL]),
W10("The Drowned Children", LG, "1980", "Poem (short unrhymed lyric)", "significant",
  genres=G("Lyric Poetry", "Elegiac Poetry"), themes=T("Death, illness and mourning",
           "Family, marriage and domestic life", "Childhood, adolescence and coming of age"),
  movements=M(CONF),
  overview="'The Drowned Children' is the first poem of Descending Figure (New York: Ecco Press, 1980), "
           "Glück's third collection, where it opens the section called 'The Garden'. It is a short "
           "unrhymed lyric spoken over the bodies of children who have drowned, and it is one of the "
           "poems in which the mythic and the domestic first come together in her work.",
  content="The poem addresses the drowned children directly, describing them as lying in the water, and "
          "it holds the scene at a distance rather than dramatising it: the water, the light, the bodies, "
          "and a speaker who looks at them without being able to intervene. Its tone is flat and its "
          "sentences are short, and the poem refuses the consolations - of memory, of mourning, of meaning "
          "- that an elegy would normally offer. The children are not named and their parents are not "
          "present; what the poem keeps is the fact of the death and the uselessness of looking at it.",
  summary="The poem is a test case for Glück's early manner. It takes the most sentimental subject in "
          "nineteenth-century verse - drowned children - and writes about it with a coldness that is "
          "deliberately unbearable, refusing both the Victorian consolation and the modern ironising that "
          "would be the easy alternative. The effect is produced by two things: the second person, which "
          "addresses the dead as though they could hear, and the flatness of the declarative sentences, "
          "which do not rise into grief. The poem belongs with the Persephone material that dominates "
          "Descending Figure - the daughter taken down into the underworld, the mother left above - and "
          "reading it that way makes its refusal of consolation a mythological argument: the descent is "
          "real, and the poem will not pretend that the return cancels it. Its brevity matters. Glück's "
          "poems of this period are short because she cuts the connective tissue that would explain the "
          "emotion, so that the reader is left with the image and the statement and has to supply the "
          "grief, which is the effect she spent her career refining.",
  themes_text="The first subject is death, and specifically the death of children, which the poem treats "
              "as an event without compensation. The second is the failure of mourning, since the poem "
              "describes a grief that cannot be converted into meaning. The third is the mythological "
              "underworld that Descending Figure keeps invoking, which gives the drowned children a "
              "genealogy. The fourth is the gaze, since the poem is about looking at something one cannot "
              "help, which is also Glück's account of what a lyric does.",
  structure="A single short lyric in unrhymed free verse, in a series of statements addressed to the dead, "
            "with no narrative development and an ending that refuses to close the scene.",
  style="Short declarative lines with almost no punctuation; a flat, unemphatic tone; concrete nouns and "
        "almost no adjectives of feeling; the second person used as address to the dead; and an absence of "
        "simile, so that the poem never converts the bodies into symbols.",
  ctx="Descending Figure (1980) was Glück's third book, five years after The House on Marshland, and the "
      "one in which she began the sequence of biblical and classical narratives that would structure "
      "Ararat, The Wild Iris and Meadowlands. It appeared in the year of her marriage to John Dranow, "
      "whose name recurs in the later poems, and it is the book in which the family material of her mature "
      "work first becomes explicit.",
  sig="The poem is the standard introduction to Glück's early manner and one of the poems by which the "
      "Descending Figure volume is known; it is a Norton selection. Its presence in the anthology places "
      "her 1980 work beside the confessional poetry of the 1960s and the mythic poetry of the 1980s, "
      "which is where the criticism usually puts it.",
  canon="Secondary canon",
  crit="Criticism reads the poem with the Persephone poems of the same volume and treats its coldness as "
       "a deliberate refusal of the elegiac tradition; the standard account of Glück's development calls "
       "Descending Figure the book in which her mythic method appears. It is less discussed than the title "
       "poem, which is the volume's statement.",
  biblio="First published in Descending Figure (New York: Ecco Press, 1980), the opening poem of the "
         "section 'The Garden'; collected in The First Four Books of Poems (1995) and Poems 1962-2012 "
         "(2012). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The description rests on the poem's placement in the collection and on the critical accounts of "
        "the volume; the text was not transcribed in full for this record.",
  ver="partially verified", sources=[DESC, W_LG, NAAL]),
W10("Descending Figure", LG, "1980", "Poem (title poem of the collection, unrhymed lyric)", "significant",
  genres=G("Lyric Poetry", "Religious Poetry"), themes=T("Death, illness and mourning",
           "Faith, doubt and the sacred", "Art, the artist and the creative life"),
  movements=M(CONF),
  overview="'Descending Figure' is the title poem of Glück's third collection (New York: Ecco Press, "
           "1980), where it closes the first section after the poems of 'The Garden'. It is the poem that "
           "states the volume's governing image - the descent - and it is the one in which the "
           "mythological method of her later books is first fully visible.",
  content="The poem works the idea of descent as both a physical and a spiritual movement: the figure that "
          "comes down, the light that falls, the body that declines. It holds several scales at once - the "
          "religious descent of the divine into the world, the aging and deterioration of a body, and the "
          "artist's own going-down into the material he or she works with - and it does not settle which "
          "is primary. The tone is austere and the sentences are short, and the poem ends without "
          "resolving the descent into an ascent.",
  summary="The title poem is where the volume's argument becomes explicit. Glück's earlier books had "
          "worked through the family and through the imagery of the garden, and Descending Figure adds the "
          "vertical axis: what comes down, and what it costs to come down. The religious vocabulary is "
          "present but undoctrinal - the descent is not named as incarnation, and the poem keeps the "
          "theological reading available without requiring it - and the poem's power comes from its "
          "refusal to say whether the descent is a fall or a gift. That ambiguity is what the later books, "
          "and especially The Wild Iris, would build on: in The Wild Iris the divine speaks from the "
          "garden and the human answers, and the relation between them is exactly the descent this poem "
          "describes without a speaker to receive it. Read as an ars poetica, the poem also states Glück's "
          "method: the poem goes down into loss because that is where the material is, and it does not "
          "come back up with a consolation.",
  themes_text="The first subject is descent itself, in its religious, physical and artistic senses, held "
              "together without being reconciled. The second is mortality and the decline of the body, "
              "which the poem treats as a fact rather than a tragedy. The third is the sacred, invoked in "
              "a vocabulary that refuses to commit to a doctrine. The fourth is the work of art, which the "
              "poem presents as a going-down into the material rather than a rising above it.",
  structure="A short unrhymed lyric in the title position of its volume, organised as a series of "
            "statements about descent in different registers, ending without resolution.",
  style="Austere, short-lined free verse; abstract nouns used with concrete force; an almost complete "
        "absence of simile; a tone of statement rather than address; and an ending that stops rather than "
        "concludes.",
  ctx="Descending Figure appeared in 1980 from Ecco Press, the small press that published most of Glück's "
      "books and that gave her work its characteristic austere presentation. The volume's mythological and "
      "biblical material belongs to the years in which American poetry was turning back to narrative and "
      "to myth after the confessional 1960s, and Glück's version of that turn was to keep the first person "
      "while emptying it of autobiography.",
  sig="The poem gives the volume its title and its argument, and it is the clearest short statement of the "
      "mythic method that would produce Ararat and The Wild Iris. It is a Norton selection, and the "
      "pairing of it with 'The Drowned Children' is how the anthology represents the 1980 book.",
  canon="Secondary canon",
  crit="The standard critical account treats the title poem as the volume's thesis and reads it with the "
       "Persephone material; the descent is usually glossed as the descent into the underworld that "
       "structures the whole book. Later criticism reads it as anticipating the theological sequences of "
       "the 1990s.",
  biblio="First published in Descending Figure (New York: Ecco Press, 1980); collected in The First Four "
         "Books of Poems (1995) and Poems 1962-2012 (2012). A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The description rests on the poem's position in the volume and on the critical accounts of it; "
        "the text was not transcribed in full for this record.",
  ver="partially verified", sources=[DESC, W_LG, NAAL]),
W10("Vespers", LG, "1992", "Poem (evening prayer, unrhymed lyric)", "major",
  genres=G("Lyric Poetry", "Religious Poetry"), themes=T("Faith, doubt and the sacred",
           "Nature, ecology and environmental crisis", "Family, marriage and domestic life"),
  movements=M(CONF),
  overview="'Vespers' is one of the ten evening prayers in The Wild Iris (New York: Ecco Press, 1992), the "
           "collection for which Glück won the Pulitzer Prize in 1993; the Norton's selection is the "
           "fourth of them, which begins 'I don't wonder where you are anymore'. The book is built on the "
           "monastic hours - seven Matins and ten Vespers - and alternates the voices of flowers, a "
           "gardener-poet and the divine.",
  content="The poem begins by saying that the speaker no longer wonders where God is: 'You're in the "
          "garden; you're where John is, / in the dirt, abstracted, holding his green trowel.' It "
          "describes John's way of gardening - fifteen minutes of intense effort, fifteen minutes of "
          "ecstatic contemplation - and the speaker's relation to it: sometimes she works beside him, "
          "weeding and thinning the lettuces, and sometimes she watches from the porch near the upper "
          "garden until twilight makes lamps of the first lilies. The poem turns in its last lines: peace "
          "never leaves John, but it rushes through the speaker not as sustenance the flower holds but "
          "'like bright light through the bare tree'.",
  summary="The poem is a prayer addressed to a God who has been relocated into a gardener, and its "
          "theology is worked out through the difference between two people in the same garden. John has "
          "peace as a possession; the speaker has it only as a passage, a light that goes through and is "
          "not held. The image the poem ends on - bright light through the bare tree - is exactly the "
          "difference it has been describing: the bare tree is not fed by the light, it is only lit by it, "
          "and the light leaves. The first line's 'anymore' carries the poem's history in a word: the "
          "speaker used to look for God and has stopped, and what replaces the search is not faith but "
          "accuracy - she knows where God is, and it is with someone else. Glück's handling of the "
          "sequence is what makes the poem more than a domestic vignette: because 'Vespers' is the name of "
          "a liturgical hour, the poem is formally an evening prayer, and its complaint is delivered "
          "inside the form of devotion, which never breaks. The garden, the trowel, the lettuces and the "
          "lilies are literal, and they are also the whole apparatus of the book's theology - creation "
          "speaking back to its creator - so that a poem about weeding is a poem about the relation "
          "between the human and the divine. It is the most anthologised of the Vespers poems and the one "
          "by which the collection is usually taught.",
  themes_text="The first subject is the presence and absence of God, handled not as doubt but as "
              "relocation: the divine is in the garden and in another person, not in the speaker's "
              "experience. The second is the unequal distribution of peace, which the poem records without "
              "self-pity and without explaining. The third is work and attention, since the garden's "
              "labour is the poem's medium for contemplation. The fourth is transience, carried by "
              "twilight, the first lilies, the bare tree and the light that passes through.",
  structure="A single unrhymed lyric in the sequence's Vespers form, moving from a statement of God's "
            "location through a description of John's gardening to a closing simile that states the "
            "speaker's own condition; roughly sixteen short lines.",
  style="Plain declarative sentences in the second person, addressed to God; domestic and horticultural "
        "vocabulary held without irony; a single long simile at the end that carries the whole emotional "
        "weight; no punctuation of emphasis and no rhetorical heightening.",
  ctx="The Wild Iris was written, by Glück's own account, in about ten weeks in the summer of 1992 and "
      "published by Ecco that year; it won the Pulitzer Prize in 1993. Its structure follows the monastic "
      "hours, and the sequence's theology is worked out across the flowers' speeches, the gardener's "
      "prayers and the divine's replies, in a garden on a property in Vermont.",
  sig="'Vespers' is the poem by which The Wild Iris is most often represented in anthologies and courses, "
      "and the collection is the book on which Glück's Nobel Prize was most often justified. It is a "
      "Norton selection and the latest of her three poems in the anthology's period.",
  canon="Major canon",
  crit="Critics read the Vespers poems as the human half of the book's dialogue and treat the sequence as "
       "a whole as a modern book of hours; the fourth Vespers is regularly discussed for its simile of "
       "light through the bare tree, which is taken as the collection's image of the difference between "
       "revelation and possession. The Nobel citation's phrase about austere beauty is usually illustrated "
       "from this book.",
  biblio="First published in The Wild Iris (New York: Ecco Press, 1992); collected in Poems 1962-2012 "
         "(2012). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The text of this Vespers was read for this record from a published transcription; the Norton's "
        "own page reference was not established, and the anthology may print a different Vespers under "
        "the same title, since the book contains ten poems so named. The record identifies the poem by its "
        "first line.",
  ver="partially verified", sources=[WILD, W_LG, NAAL]),
]
