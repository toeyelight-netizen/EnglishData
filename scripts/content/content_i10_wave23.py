"""Installment 10, wave 24: Frank O'Hara, Audre Lorde and Susan Sontag.

Three new authors and eight works, one record per Norton selection.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

FO = "Frank O'Hara"
AL = "Audre Lorde"
SS = "Susan Sontag"

NYS = "The New York School"
BAM = "Black Arts Movement"
FEM2 = "Second-Wave Feminist Writing"

W_FO = "Frank O'Hara (Wikipedia)"
W_MP = "Lunch Poems (Wikipedia)"
W_MIE = "Meditations in an Emergency (Wikipedia)"
W_CITE = "Having a Coke with You (Encyclopedia.com, Poetry for Students)"
W_PF_FO = "Frank O'Hara (Poetry Foundation)"
W_EV = "Evergreen Review, index 1957-1967"
W_AL = "Audre Lorde (Wikipedia)"
W_SO = "Sister Outsider (Wikipedia)"
W_LOC = "Chrysalis and 'Poetry Is Not a Luxury' (Library of Congress blog)"
W_CP = "The Collected Poems of Audre Lorde (library catalogue contents)"

AUTHORS = [
A10(FO, SEC, "1926", "1966", "Baltimore, Maryland, United States",
  "American; poet, art curator and critic writing in English",
  "American poet and Museum of Modern Art curator, the liveliest of the New York School poets, whose 'I do this, "
  "I do that' lunch poems made the ordinary afternoon the subject of American lyric verse",
  "Francis Russell O'Hara was born in Baltimore on 27 March 1926 and grew up in Grafton, Massachusetts; he "
  "studied piano at the New England Conservatory, served as a sonarman in the US Navy in the Pacific, and took "
  "his degree at Harvard in 1950, where he met John Ashbery and began publishing in the Harvard Advocate. He "
  "took an MA at the University of Michigan, where he won a Hopwood Award, moved to New York in 1951, worked "
  "at the front desk of the Museum of Modern Art and rose there to associate curator of painting and "
  "sculpture, writing the catalogues of Jackson Pollock and Robert Motherwell and reviews for ArtNews. His "
  "books in his lifetime were small gallery and press editions - A City Winter and Other Poems (1952), "
  "Oranges: 12 pastorals (1953), Meditations in an Emergency (1957), Odes (1960), Lunch Poems (1964) and "
  "Love Poems (Tentative Title) (1965) - and his poetry was assembled after his death in The Collected "
  "Poems, edited by Donald Allen (1971), which shared the National Book Award in 1972. He was struck by a "
  "jeep on the beach at Fire Island on 24 July 1966 and died the next day at Mastic Beach, Long Island.",
  "Poetry: A City Winter and Other Poems (1952), Oranges: 12 pastorals (1953), Meditations in an Emergency "
  "(1957), Odes (1960), Lunch Poems (1964) and Love Poems (Tentative Title) (1965), collected in The "
  "Collected Poems of Frank O'Hara, ed. Donald Allen (1971), and in the posthumous selection In Memory of My "
  "Feelings (1967). Prose: Jackson Pollock (1959), Art Chronicles 1954-1966 (1975) and the mock manifesto "
  "'Personism' (written 1959, published in Yugen, 1961).",
  "Free verse that keeps the cadences of talk: the poem as a record of the afternoon that produced it, with "
  "street names, shop windows, film stars and friends' names left in; the 'I do this, I do that' structure; "
  "surreal turns, camp jokes and sudden tenderness; an insistence that the poem is 'between two persons "
  "instead of two pages'.",
  "The city, the lunch hour and the ordinary day; friendship, love and gay desire; painting, music and the "
  "other arts, with painters as recurring heroes; the death of friends and of the famous, faced without "
  "ceremony; the belief that immediacy and speed are themselves values.",
  "O'Hara is the central poet of the New York School and the model for the conversational, city-written "
  "American poem of the last half-century; the posthumous Collected Poems won the National Book Award, "
  "'The Day Lady Died' and 'Why I Am Not a Painter' are among the most anthologised American poems of the "
  "period, and his manner - casual, fast, intimate, funny - is one of the dominant idioms of American "
  "poetry since 1960.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on O'Hara and its pages on Lunch Poems "
           "and Meditations in an Emergency, and from the Poetry Foundation's author page, read directly; "
           "they were not checked against a bibliography. Installment 10 records only the five Norton "
           "selections, 'Personism: A Manifesto' and four poems: the prose books and the contents of the "
           "posthumous volumes have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_FO, W_MP, W_MIE, W_PF_FO, NAAL]),
A10(AL, MAJ, "1934", "1992", "New York City, New York, United States",
  "American; poet, essayist and activist writing in English",
  "American poet, essayist and self-described 'Black, lesbian, feminist, socialist, mother, warrior, poet', "
  "whose poems and essays on race, sexuality and the uses of anger and of the erotic made her a founding "
  "voice of Black feminist thought",
  "Audrey Geraldine Lorde was born in Harlem, New York, on 18 February 1934, the youngest of three "
  "daughters of immigrants from Barbados and Carriacou; she dropped the 'y' from her name as a child, "
  "learned to read at four and wrote her first poems at school, published a poem in Seventeen while still "
  "at Hunter High School, and took her BA at Hunter College and her MLS at Columbia. She worked as a "
  "librarian in New York and as a teacher, married the lawyer Edwin Rollins in 1962 and divorced in 1970, "
  "and had two children; she was active in the civil rights, anti-war, lesbian and feminist movements and "
  "was a founding member of Kitchen Table: Women of Color Press. The First Cities (1968), Cables to Rage "
  "(1970), From a Land Where Other People Live (1973, National Book Award finalist), New York Head Shop "
  "and Museum (1974), Coal (1976), The Black Unicorn (1978), Chosen Poems - Old and New (1982), Our Dead "
  "Behind Us (1986) and The Marvelous Arithmetics of Distance (1993) are the poetry; The Cancer Journals "
  "(1980), Zami: A New Spelling of My Name (1982), Sister Outsider (1984) and A Burst of Light (1988) the "
  "prose. She was Poet Laureate of New York State in 1991 and died at St Croix in the US Virgin Islands on "
  "17 November 1992.",
  "Poetry: The First Cities (1968), Cables to Rage (1970), From a Land Where Other People Live (1973), New "
  "York Head Shop and Museum (1974), Coal (1976), The Black Unicorn (1978), Chosen Poems - Old and New "
  "(1982), Our Dead Behind Us (1986) and The Marvelous Arithmetics of Distance (1993), gathered in The "
  "Collected Poems of Audre Lorde (1997). Prose: The Cancer Journals (1980), Zami: A New Spelling of My "
  "Name (1982), Sister Outsider: Essays and Speeches (1984), A Burst of Light (1988) and I Am Your Sister "
  "(2009).",
  "A poetry of plain statement and long breath, often in loose free verse with biblical and incantatory "
  "repetition; anger and tenderness held in the same sentence; the first person used as a public voice; in "
  "the essays, a prose of direct address, short declarative paragraphs and aphorism ('the master's tools "
  "will never dismantle the master's house') that is meant to be spoken aloud.",
  "Race, racism and the struggle for civil rights, and the difference between them; sexuality, desire and "
  "the closet; gender, feminism and women's lives, above all the lives of Black women; the erotic as "
  "knowledge and power; illness, cancer and mortality; the uses of anger; poetry itself as a necessity "
  "rather than a luxury; the refusal of any hierarchy of oppressions.",
  "Lorde is the central theoretician of intersectionality in Black feminist writing and one of the most "
  "widely quoted American essayists of the century; 'The Master's Tools Will Never Dismantle the Master's "
  "House' and 'Uses of the Erotic' are standard texts in women's, gender and Black studies, her Collected "
  "Poems is a landmark of American poetry, and her name is attached to institutions, prizes and reading "
  "rooms on several continents.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Lorde and on Sister Outsider, from "
           "the Library of Congress blog post on Chrysalis and from the contents listing of The Collected "
           "Poems in library catalogues, read directly; they were not checked against a bibliography. "
           "Installment 10 records only the five Norton selections - three poems, 'Coal', 'The Woman Thing' "
           "and 'Black Mother Woman', and two essays, 'Uses of the Erotic' and 'The Master's Tools'; the "
           "other books have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_AL, W_SO, W_LOC, W_CP, NAAL]),
]

AUTHORS.append(
A10(SS, MAJ, "1933", "2004", "New York City, New York, United States",
  "American; essayist, novelist, playwright and film-maker writing in English",
  "American essayist and public intellectual whose essays on interpretation, photography, illness and war - "
  "beginning with 'Against Interpretation' - made criticism itself a literary form and the critic a public "
  "figure",
  "Susan Sontag was born in New York on 16 January 1933, grew up on Long Island, in Tucson and in the San "
  "Fernando Valley, graduated from North Hollywood High School at fifteen, studied at Berkeley and at the "
  "University of Chicago and took an MA in philosophy at Harvard; she taught at Columbia and at City "
  "College, and her marriage to the sociologist Philip Rieff ended in 1959. 'Notes on \"Camp\"' in 1964 and "
  "the collection Against Interpretation (1966) made her famous as the critic who argued for the sensuous "
  "surface of art against the hunt for hidden meaning; Styles of Radical Will (1969), On Photography "
  "(1977), Illness as Metaphor (1978), Under the Sign of Saturn (1980), AIDS and Its Metaphors (1989), "
  "Regarding the Pain of Others (2003) and At the Same Time (2007) followed, with the novels The Benefactor "
  "(1963), Death Kit (1967), The Volcano Lover (1992) and In America (1999), the stories of I, etcetera "
  "(1978), the play Alice in Bed (1993) and the films Duet for Cannibals (1969) and Brother Carl (1971). "
  "She directed stage productions in besieged Sarajevo in 1993 and was awarded the Jerusalem Prize in "
  "2001; she died in New York on 28 December 2004.",
  "Non-fiction: Against Interpretation (1966), Styles of Radical Will (1969), On Photography (1977), Illness "
  "as Metaphor (1978), Under the Sign of Saturn (1980), AIDS and Its Metaphors (1989), Where the Stress "
  "Falls (2001) and Regarding the Pain of Others (2003), with the journals Reborn (2008) and As "
  "Consciousness Is Harnessed to Flesh (2012). Fiction: The Benefactor (1963), Death Kit (1967), I, "
  "etcetera (1978), The Volcano Lover (1992) and In America (1999). Plays and films: A Parsifal (1991), "
  "Alice in Bed (1993), Duet for Cannibals (1969) and Brother Carl (1971).",
  "Aphoristic, declarative sentences in short numbered paragraphs; the essay built as a series of "
  "propositions rather than an argument with footnotes; a taste for lists, definitions and the imperative "
  "('In place of a hermeneutics we need an erotics of art'); high and popular culture discussed in the same "
  "vocabulary; an authoritative first-person plural that speaks for the age.",
  "Interpretation and the critic's task; form against content; photography, images and the modern world; "
  "illness as metaphor and the metaphors we think with; war, atrocity and the ethics of looking at other "
  "people's suffering; camp, style and sensibility; the intellectual as a public figure.",
  "Sontag is the most widely read American critic of the second half of the century and the writer who "
  "made the essay a public form; 'Against Interpretation' and 'Notes on \"Camp\"' are standard texts in "
  "criticism and cultural studies, On Photography and Illness as Metaphor shaped whole fields, and her "
  "name is a byword for the intellectual life of postwar New York.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Sontag and on Against "
           "Interpretation, read directly; they were not checked against a bibliography. Installment 10 "
           "records only the Norton selection, 'Against Interpretation' (Evergreen Review, December 1964; "
           "collected 1966); the other collections, the novels, the plays and the films have no records, so "
           "the bibliography is incomplete.",
  ver="partially verified", sources=["Susan Sontag (Wikipedia)", "Against Interpretation (Wikipedia)", NAAL]))

WORKS = [
W10("Personism: A Manifesto", FO, "1961", "Essay (literary manifesto)", "significant",
  genres=G("Literary Manifesto", "Literary Criticism and Theory (1946–2000)", "Experimental Fiction"),
  themes=T("Art, the artist and the creative life", "Language, writing and the limits of representation"),
  movements=M(NYS),
  overview="A short comic manifesto written in 1959 and published in the magazine Yugen in 1961: O'Hara "
           "announces a movement invented 'after lunch with LeRoi Jones on August 27, 1959' and argues that a "
           "poem should be 'between two persons instead of two pages'.",
  content="Some five hundred words of mock programme, in which O'Hara names his movement, dates its founding "
          "to a lunch with a friend, refuses metre, assonance and 'all that stuff', and reduces poetics to "
          "one instruction: go on your nerve.",
  summary="The essay opens by declaring that everything written since 1949 about poetry has been 'in the "
          "public domain, practically' and announces a new movement, Personism, founded - the joke is the "
          "precision - 'after lunch with LeRoi Jones on August 27, 1959'. O'Hara explains that he has "
          "taken the name from 'Personalism' after hearing that the great problem of the age was 'Personal "
          "ism' and that the movement 'has nothing to do with personality or intimacy, far from it!'. He "
          "then gives the argument: a poem should be written as if addressed to one person, as if the "
          "telephone had replaced the printing press, so that the poem is 'at last between two persons "
          "instead of two pages'. He dismisses metre, assonance and 'all that stuff' ('You just go on your "
          "nerve'), admits that the movement has already been attacked and that he intends to keep it "
          "'in the family', and ends by imagining the poem in the hands of its single reader and by "
          "proposing, half-seriously, to abolish the audience. The manifesto's tone is the argument: it is "
          "a joke that makes a real claim about scale, intimacy and the death of the public reader.",
  themes_text="The essay's argument is that the scale of modern communication - the telephone rather than "
              "the printing press - should change the scale of the poem, and that a poem addressed to one "
              "person is more honest than a poem addressed to posterity. Around that sit O'Hara's other "
              "convictions: that formal technique ('metre, assonance, all that stuff') is less important "
              "than nerve, that a movement is a social fact made at lunch rather than a doctrine, and that "
              "the avant-garde's own institutions and manifestos are material for comedy. The manifesto is "
              "also, as its critics have noted, a love poem in disguise: it was written during O'Hara's "
              "affair with the dancer Vincent Warren, and the 'two persons' of its poetics are the poet and "
              "the beloved.",
  structure="A single short prose piece in three movements: the founding joke, the definition and the "
            "consequences; it borrows the shape of the modernist manifesto (Marinetti, Breton, the "
            "Imagists) and deflates it, offering a founding date, a name, a doctrine and a schism within "
            "one page.",
  style="Comic, chatty, first-person prose with exclamation marks and abrupt asides; short paragraphs; "
        "deliberate name-dropping (LeRoi Jones, 'the great problem of the age'); the vocabulary of "
        "bureaucracy and publicity ('public domain', 'movement', 'the family') applied to poetry; a single "
        "memorable aphorism, 'The poem is at last between two persons instead of two pages'.",
  ctx="Written in 1959 for a projected anthology of statements on poetics (Donald Allen's The New American "
      "Poetry, 1945-1960, where it was not in the end printed) and published in Yugen, the little magazine "
      "edited by LeRoi Jones and Hettie Cohen, in 1961; it belongs to the run of New York School statements "
      "about poetry and to the longer tradition of the avant-garde manifesto, and it was taken up in the "
      "1960s as a name for O'Hara's whole manner.",
  sig="The best-known statement of poetics by any of the New York School poets and one of the few "
      "twentieth-century American manifestos still quoted whole; the phrase 'between two persons instead "
      "of two pages' is the standard shorthand for O'Hara's conversational poetics, and the piece is a "
      "standard anthology text on American avant-garde poetics and on the manifesto as a genre.",
  canon="Secondary canon",
  crit="Critics read the manifesto as a serious poetics in comic dress - a claim about intimacy, scale and "
       "address rather than a rejection of craft - and as a document of the gay social world in which the "
       "New York School poems were written; its relation to modernist manifestos, to the Black Arts "
       "movement that LeRoi Jones went on to found, and to O'Hara's own practice in the love poems has "
       "all been discussed.",
  biblio="Written in 1959 and published in Yugen in 1961; collected in Donald Allen's edition of The "
         "Collected Poems of Frank O'Hara (New York: Knopf, 1971) and reprinted in the standard O'Hara "
         "prose selections. A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The essay was quoted from the published text through the sources consulted rather than read in a "
        "complete authorised edition; the founding date and the Yugen publication are given as the sources "
        "state them. The anthology of statements for which it was written did not print it.",
  ver="partially verified", sources=[W_FO, W_PF_FO, NAAL]),
W10("Why I Am Not a Painter", FO, "1957", "Poem (free verse)", "major",
  genres=G("Free Verse", "Lyric Poetry", "Experimental Fiction"),
  themes=T("Art, the artist and the creative life", "Language, writing and the limits of representation"),
  movements=M(NYS),
  overview="A poem of the mid-1950s, printed in Meditations in an Emergency (1957), in which O'Hara compares "
           "the painting of his friend Mike Goldberg - which begins with sardines and ends without them - "
           "with his own poem about oranges, which ends without once saying the word.",
  content="A single anecdote in short free-verse lines: the poet drops in on the painter Mike Goldberg, "
          "watches him begin a canvas with the word SARDINES in it, returns over the following days, and "
          "finds the painting finished with no sardines in it - and then describes the twelve poems about "
          "orange that he wrote and called ORANGES, none of which mentions orange.",
  summary="The poem begins with a flat declaration - 'I am not a painter, I am a poet' - and a joke about "
          "wanting to be a painter. It then tells two parallel stories. In the first, O'Hara drops in on "
          "Mike Goldberg as he starts a painting, is offered a drink, looks up and sees that 'SARDINES' has "
          "been written into the canvas, and is told 'it needed something there'; he comes back over "
          "several days, watches the painting change, and when it is finished asks where the sardines have "
          "gone - they are gone, and the painting is still called SARDINES. In the second, O'Hara thinks "
          "of a colour, orange, writes a line about it, and in a few days has a page, then another page, "
          "then twelve poems that are not about orange at all; he calls the sequence ORANGES, and the poem "
          "ends with him seeing Mike's painting in a gallery 'called SARDINES'. The comparison is the "
          "argument: both artists begin with a word or a colour, both let the work move away from its "
          "starting point, and both name the finished thing after the trace that survives in it. The "
          "poem's joke is that the titles are the only surviving evidence of the original intention, and "
          "its deeper point is that this is not a loss: the painting and the poem are better for having "
          "travelled away from their subjects, and the trace in the title records the journey rather "
          "than a failure to arrive.",
  themes_text="The poem is about process, and about the relation between a title, a subject and a work. Its "
              "claim is that a painting and a poem are records of the act that produced them rather than "
              "statements about their nominal subjects - Ashbery called this O'Hara's 'concept of the poem "
              "as the chronicle of the creative act that produces it', and the critical literature on "
              "O'Hara returns to the poem for exactly that reason. Beneath the joke is a serious argument "
              "about abstraction: Goldberg's painting is an abstract expressionist canvas, and O'Hara's "
              "poem is a demonstration that writing can work the same way, starting from a concrete word "
              "and ending somewhere the word cannot reach.",
  structure="Free-verse lines of two to eight words, in a single unbroken anecdote with two halves that "
            "mirror each other; no stanza divisions; the parallel is made by repetition ('days go by', "
            "'I drop in') rather than by statement, and the poem ends on the rhyme of the two titles, "
            "SARDINES and ORANGES.",
  style="Conversational and apparently artless: short lines, plain diction, direct speech, no metaphor and "
        "almost no adjectives; the rhythm is that of a man telling a story about his afternoon; the "
        "poem's art is in the symmetry of the two anecdotes and in the flat finality of the last line.",
  ctx="Written in the mid-1950s (the Poetry Foundation dates it to 1956) and printed in Meditations in an "
      "Emergency (Grove Press, 1957), O'Hara's second collection; Mike Goldberg was a painter friend of "
      "the New York School circle, and the poem belongs to the moment when O'Hara was writing most closely "
      "about the visual arts he was also curating and reviewing.",
  sig="One of O'Hara's two or three most anthologised poems and a standard text in courses on modern "
      "poetry, on the New York School and on poetry and the visual arts; its comparison of the two "
      "arts is one of the most quoted passages in postwar American writing about poetry, and it is "
      "regularly used to explain how abstract expressionism changed American poetry.",
  canon="Major canon",
  crit="Criticism reads the poem as a statement of O'Hara's compositional theory, as a comic meditation on "
       "abstraction and as a portrait of the New York art world as a social institution; its parallel "
       "structure and its refusal of metaphor have been much discussed, and it is regularly set beside "
       "'Personism' as the practical demonstration of the poetics announced there.",
  biblio="Printed in Meditations in an Emergency (New York: Grove Press, 1957); written in the mid-1950s "
         "(1956 by the Poetry Foundation's dating). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The poem was read in the text printed by the Poetry Foundation and other anthologies; no "
        "first-periodical appearance has been identified, and the record does not assert one.",
  ver="partially verified", sources=[W_MIE, W_FO, W_PF_FO, NAAL]),
]

WORKS += [
W10("A Step Away from Them", FO, "1956", "Poem (free verse)", "significant",
  genres=G("Free Verse", "Elegiac Poetry", "Lyric Poetry"),
  themes=T("The city, the suburb and modern space", "Death, illness and mourning", "Art, the artist and the creative life"),
  movements=M(NYS),
  overview="Written on 16 August 1956, the day after Jackson Pollock's funeral, and printed in Lunch Poems "
           "(1964): a walk through midtown Manhattan at lunch hour that becomes an elegy for three friends "
           "who have died.",
  content="A single lunch-hour walk in short free-verse lines, from the sidewalk and the construction "
          "workers to the avenue, a hat check, a shoeshine and a hamburger, ending with the thought of "
          "Jackson Pollock, Bunny Lang and John La Touche, dead within a year of one another.",
  summary="The poem begins with its most quoted line - 'It's my lunch hour, so I go / for a walk among the "
          "hum-colored / cabs' - and follows the poet down the sidewalk past labourers eating sandwiches, "
          "past skirts, past a Puerto Rican family, into a shoeshine stand and then a place for a "
          "hamburger and a malted, with the newspaper, the advertisements and the store windows all "
          "recorded at the pace of walking. The middle of the poem pauses on a glass of papaya juice in a "
          "store where a woman is looking at a poster of a film, and on the thought of the poet's "
          "friends; at the end of the walk he remembers 'a blonde child' and then, in the last lines, the "
          "three dead - 'Bunny' (Violet Ranney Lang), John La Touche and Jackson Pollock, all of whom had "
          "died in 1955-56 - and asks, 'Is the earth as full as life was full, of them?' The poem closes "
          "with the return to the street and to the ordinary present, the death of the friends held inside "
          "the afternoon rather than announced as its subject.",
  themes_text="The poem's subject is the coexistence of the ordinary and the dead: the city goes on being "
              "vivid and specific (cabs, chewing gum, papaya juice, a Dior display) at the same moment "
              "that the poet's friends have stopped, and the elegy is made out of the sheer pressure of "
              "the details rather than out of mourning language. The title states the poem's argument - "
              "that the dead are only a step away, in the same street - and the question at the centre, "
              "'Is the earth as full as life was full, of them?', is one of the few directly rhetorical "
              "lines O'Hara ever wrote. It is also a poem about the lunch hour itself, and about the "
              "possibility of writing a serious poem in the middle of a working day.",
  structure="One unbroken free-verse sequence of some sixty lines, in a single present-tense walk with no "
            "stanza divisions; the movement is spatial (sidewalk, street, store, restaurant, street) and "
            "the elegy arrives without a transition, so that the reader experiences the deaths as the "
            "poet does - as an interruption of the afternoon.",
  style="Long conversational lines broken at the phrase rather than the foot, in a diction that includes "
        "brand names, advertisements, brand-new slang and the names of the dead; paratactic syntax joined "
        "by 'and' and 'then'; almost no figurative language except the compound 'hum-colored', which has "
        "become the poem's signature.",
  ctx="Composed on 16 August 1956, the day after Jackson Pollock's funeral at Springs, Long Island, where "
      "O'Hara had been one of the mourners; printed in Lunch Poems (City Lights, 1964), the collection "
      "that took its name from poems written in O'Hara's lunch hours at the Museum of Modern Art. It is "
      "the first of the lunch poems and the poem in which O'Hara's mature manner - elegy inside the "
      "daily, the city as an elegiac machine - is fully present.",
  sig="The poem that established the 'lunch poem' and one of the central American elegies of the century; it "
      "is a standard anthology text for the New York School, for the relations between poetry and the "
      "visual arts, and for the elegy, and its opening line is one of the best known in postwar American "
      "poetry.",
  canon="Major canon",
  crit="Criticism reads the poem as an elegy that refuses elegiac convention, as a document of the New York "
       "art world of the mid-1950s, and as an experiment in representing urban perception at walking pace; "
       "the deaths of Pollock, Lang and La Touche, the poem's treatment of Puerto Rican New York and its "
       "relation to Whitman's catalogues have all been discussed.",
  biblio="Printed in Lunch Poems (San Francisco: City Lights Books, Pocket Poets Series no. 19, 1964); "
         "composed 16 August 1956. A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="No first periodical printing was identified; the record gives the collection as the first "
        "appearance rather than asserting an earlier one.",
  ver="partially verified", sources=[W_MP, W_FO, W_PF_FO, NAAL]),
W10("The Day Lady Died", FO, "1959", "Poem (free verse)", "major",
  genres=G("Free Verse", "Elegiac Poetry", "Lyric Poetry"),
  themes=T("Death, illness and mourning", "The city, the suburb and modern space", "Art, the artist and the creative life"),
  movements=M(NYS),
  overview="Written on 17 July 1959, the day Billie Holiday's death was reported, and printed in Lunch "
           "Poems (1964): the poem records a lunch hour of errands in Manhattan - a shoeshine, a bank, a "
           "gift, a bottle of Strega, a book of Genet's plays - and then, in its last lines, the news of "
           "her death and the memory of hearing her sing.",
  content="A single afternoon in short free-verse lines, with exact times, a shoeshine, a bank, a "
          "haberdasher, a bookshop and a bar, and with the news of Billie Holiday's death arriving at the "
          "end - not as an event in the poem but as the thing that stops it, so that the last line is a "
          "memory of her singing and of a room falling silent.",
  summary="The poem opens with its characteristic precision - 'It is 12:20 in New York a Friday / three "
          "days after Bastille day, yes / it is 1959' - and then follows the poet through an ordinary "
          "sequence of errands: a shoeshine, a bank, a walk up to a store to buy a gift, a stop at the "
          "Golden Griffin to buy a bottle of Strega for a friend, a look at the New World Writing "
          "paperback and a purchase of Genet's plays at the Eighth Street Bookshop. The details are "
          "specific and unsentimental - the names of streets, the price of things, the cashier's name - "
          "and the poem's rhythm is the rhythm of an afternoon with nothing in it. Then, in the last "
          "lines, the poet sees a sign or a headline, learns that Billie Holiday has died, and goes into "
          "a bar where a woman is singing; the poem ends with the memory of hearing Lady sing at the "
          "Five Spot, '#and everyone and I stopped breathing', the 'and' carrying the shock and the "
          "grammar breaking under it. The poem's structure is an errand list with a hole at the end: "
          "nothing in the afternoon prepares for the death, and the flatness of the earlier lines is "
          "what makes the last four unbearable. The poem's dates and prices have been read as an "
          "indictment of the culture that produced both the singer and the shoebox city, but their "
          "first function is structural: they establish a world so thoroughly ordinary that death "
          "cannot be prepared for in it.",
  themes_text="The poem is an elegy that refuses to announce itself as one: death arrives at the end of an "
              "errand list, and the effect depends on the flatness of everything before it. Its subject "
              "is the way public news enters a private afternoon, and the way a great artist's death is "
              "registered not by mourning but by the body's memory of her voice. The exact times and "
              "prices - what critics call its 'consumer' detail - are both the poem's realism and its "
              "irony: the world of goods continues, and the singer who made everyone stop breathing is "
              "dead.",
  structure="One continuous free-verse sequence of about forty lines, with no stanza breaks, organised by "
            "the sequence of errands and by the clock; the single turn comes in the last six lines, when "
            "the poem shifts from the street to the memory of the performance, and the poem ends in the "
            "middle of a breath.",
  style="Conversational free verse with exact times, dates, place names, brand names and prices; line "
        "breaks at the phrase; the last line's '#and everyone and I stopped breathing' uses the hash sign "
        "as a stage direction for a gasp and reverses the natural word order, producing the most "
        "discussed single line in O'Hara's work.",
  ctx="Written on 17 July 1959, the day the newspapers reported Billie Holiday's death, and printed in "
      "Lunch Poems (City Lights, 1964); O'Hara had heard Holiday sing at the Five Spot in the 1950s. The "
      "poem belongs to the small group of American elegies for jazz musicians, with Frank O'Hara's own "
      "tributes to Pollock and to Bunny Lang, and it is the poem through which the New York School's "
      "relation to jazz and to the recording of a single day is usually taught.",
  sig="One of the most admired American short poems of the century and O'Hara's best-known work; it is a "
      "standard anthology piece, a set text on the elegy, on the New York School and on the poetry of the "
      "city, and its final line is among the most frequently quoted in postwar American poetry.",
  canon="Major canon",
  crit="Criticism has read the poem as an anti-elegy, as a poem about consumer culture and the media, as a "
       "gay elegy for a singer who was also a gay icon, and as a formal experiment in which the "
       "line-break does the work of grief; the relationship between the errand list and the death, and "
       "between the poem's casualness and its mourning, is the central interpretive question.",
  biblio="Printed in Lunch Poems (San Francisco: City Lights Books, Pocket Poets Series no. 19, 1964); "
         "written 17 July 1959. A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The poem is quoted in the summary from the text printed in Lunch Poems and in the sources "
        "consulted; the exact punctuation of the final line follows the printed edition used by the "
        "sources.",
  ver="partially verified", sources=[W_MP, W_FO, W_PF_FO, NAAL]),
]

WORKS += [
W10("Having a Coke with You", FO, "1960", "Poem (free verse)", "major",
  genres=G("Free Verse", "Lyric Poetry", "Confessional Poetry"),
  themes=T("Love, intimacy and loss", "Art, the artist and the creative life", "The city, the suburb and modern space"),
  movements=M(NYS),
  overview="Written in April 1960 and printed in Love Poems (Tentative Title) (1965): a love poem in long "
           "free-verse lines that compares the beloved with the paintings in the world and with a recent "
           "trip to Spain, chooses the afternoon and the Coke with him, and makes the comparison itself "
           "the declaration.",
  content="A single address in long free-verse lines, in which the poet lists what he would rather do "
          "than sit with the beloved - travel, look at paintings, visit Spain - and finds that the list "
          "keeps turning into reasons for preferring the afternoon they are having, with its Coke, its "
          "orange shirt and its talk.",
  summary="The poem begins by preferring the beloved's company to a whole itinerary - 'Having a coke with "
          "you / is even more fun than going to San Sebastian, Irun, Hendaye, Biarritz, Bayonne' - and "
          "then, in a rush of clauses, says why: because of the orange shirt, because of the lover's "
          "yoghurt, because of the tulips, because of the secrecy of their smiles, because he would "
          "rather look at him 'than all the portraits in the world', with one exception, the 'Polish "
          "Rider' of Rembrandt, which is in the Frick and which they can go to see together for the "
          "first time. The poem keeps its balance between the grand and the small - Spanish cities, "
          "Rembrandt, the Frick - and the ordinary: a Coke, a shirt, a smile, a day off. It ends not "
          "with a declaration but with the present-tense fact of the afternoon, the poem having argued "
          "that this is enough. The comparisons are the argument: the beloved is not measured against "
          "art and found equal to it but preferred to it, and the preference is stated in the terms of "
          "a shopping list and a holiday itinerary, in the voice of someone who cannot quite believe his "
          "luck. Its form is one long sentence of clauses held together by 'because', so that the "
          "grammar itself keeps finding new reasons, and the poem's happiness is the happiness of a "
          "syntax that will not stop.",
  themes_text="The poem is a defence of the ordinary present against the prestige of art and travel: the "
              "beloved is set beside the Prado and wins, and the one painting that survives the comparison "
              "survives because it can be seen together, that is, because it can be turned into an "
              "experience shared rather than an object admired. Its tone is the argument - the "
              "exuberance of the list, the jokes, the willingness to be embarrassing - and its model is "
              "'Personism': a poem addressed to one person, in which the 'two persons' of the address "
              "are the whole point.",
  structure="A single sentence-like movement in long free-verse lines, with no stanza breaks, held together "
            "by anaphora ('partly because', 'it is hard to believe') and by the accumulation of clauses; "
            "the ending returns to the opening situation - the Coke - so that the poem closes where it "
            "began.",
  style="Long breathless lines of talk, with lists, exclamations, questions and parenthetical asides; "
        "proper names left in (Biarritz, the Frick, the Polish Rider, yoghurt); no regular metre; the "
        "rhythm of a man speaking quickly because he is happy.",
  ctx="Written on 21 April 1960, four days after O'Hara returned from a trip to Spain, and addressed to "
      "the Canadian ballet dancer Vincent Warren, whom he had met in the summer of 1959; printed in Love "
      "Poems (Tentative Title) (Tibor de Nagy, 1965), the last collection published in his lifetime. It "
      "belongs to the sequence of love poems of 1959-61, his most productive period, and to the gay "
      "love poetry of the period, which had few public models.",
  sig="One of the most loved and most anthologised American love poems of the second half of the century; "
      "it is a standard text in courses on modern love poetry, on the New York School and on gay "
      "literature, it has been widely quoted in popular culture from films to songs, and it is the poem "
      "through which O'Hara's 'Personism' is most often explained.",
  canon="Major canon",
  crit="Criticism reads the poem as a democratic love poem, as a deliberate refusal of the rhetoric of "
       "courtly and Romantic love, and as a document of gay life in 1960 written in a period when such "
       "declarations were dangerous; the list form, the treatment of the Polish Rider and the relation "
       "of the poem to Personism are the recurring topics, and its reception has made it one of "
       "O'Hara's most popular works after his death.",
  biblio="Printed in Love Poems (Tentative Title) (New York: Tibor de Nagy Gallery Editions, 1965); "
         "written 21 April 1960 and first published in a little magazine before the collection. A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first magazine printing is reported by the reference sources as a small-press magazine; the "
        "record does not name it, since only secondary descriptions were available.",
  ver="partially verified", sources=[W_CITE, W_FO, W_PF_FO, NAAL]),
W10("In Memory of My Feelings", FO, "1956", "Poem (free verse sequence)", "significant",
  genres=G("Free Verse", "Confessional Poetry", "Experimental Fiction"),
  themes=T("Identity, authenticity and the divided self", "Art, the artist and the creative life", "Sexuality, desire and the closet"),
  movements=M(NYS),
  overview="A long poem of 1956, printed in the Evergreen Review in 1958 and reprinted in The New American "
           "Poetry in 1960: a sequence in which the poet tries on and discards a series of selves, from a "
           "serpent to a stag to a film star, and arrives at the moving 'scene of my selves'.",
  content="A poem in numbered sections, mixing narrative, dialogue, list and lyric, in which the speaker "
          "assumes and refuses a series of identities and ends by accepting that the self is a scene "
          "rather than a thing.",
  summary="The poem is in sections and moves between several kinds of writing: a narrative of a stag hunt "
          "and a serpent, a passage of film-star glamour, a sequence of lists and exclamations, and a "
          "meditative close. Its governing action is the assumption and rejection of selves - the poet "
          "tries on the roles of lover, hunter, animal, woman, star and corpse - and the poem's most "
          "quoted formulation is that the self is 'the scene of my selves', a place in which identities "
          "arrive and depart rather than a substance that persists. The dedication names Grace Hartigan, "
          "the painter, and the poem's imagery is full of her canvases; the emotional movement is from "
          "the wish to be fixed to the acceptance of change, and the last sections turn to love and to "
          "the possibility of being 'reborn' in the ordinary.",
  themes_text="The poem is O'Hara's most sustained treatment of identity: the self is not a single thing "
              "but a scene or a staging, and the poem's energy comes from the pleasure of changing masks "
              "and its gravity from the fear that there is nothing underneath them. Critics have read "
              "the poem as a gay text - the masks include those of Hollywood women and the language of "
              "camp - and as a response to Whitman's 'Song of Myself', whose catalogue of selves it "
              "rewrites a century later. Its relation to painting, and to Hartigan's work in "
              "particular, makes it one of the central documents of the interaction between the New York "
              "School poets and the abstract expressionist painters.",
  structure="A sequence in numbered sections, moving without transition between narrative, dialogue, list "
            "and lyric; the poem's coherence is thematic rather than syntactic, and its returns and "
            "repetitions enact the movement between selves that it describes.",
  style="Dense, surreal and rhetorical rather than conversational - the least 'lunch poem' of O'Hara's "
        "major works - with long cascading lines, exclamations, invented images and sudden plain "
        "statements; the diction ranges from the archaic to the camp, and the poem's rhythms are closer "
        "to music than to talk.",
  ctx="Dated in manuscript 27 June to 1 July 1956 and first published in the Evergreen Review in 1958; "
      "reprinted in Donald Allen's The New American Poetry, 1945-1960 (1960), the anthology that made "
      "the New York School a public fact. It was the poem that gave its title to the Museum of Modern "
      "Art's memorial volume of 1967 and to Jasper Johns's painting of 1961, and it belongs to the "
      "moment of O'Hara's closest engagement with the painters of his circle.",
  sig="O'Hara's most ambitious long poem and, with 'Second Avenue' and 'Rhapsody', the work on which his "
      "claim to be a major poet rather than a charming occasional one rests; it is a standard text for "
      "the New York School, for the poetry of identity and for the relation between American poetry and "
      "abstract expressionism, and its 'scene of my selves' is one of the period's defining phrases.",
  canon="Major canon",
  crit="Criticism reads the poem as a Whitmanian self-portrait, as a camp performance of identity and as a "
       "poem about painting; Perloff's account of it as a transition from 'Second Avenue' to the 'Odes', "
       "and the reading of its elegiac structure, are the starting points of the later literature.",
  biblio="Written June-July 1956; first published in the Evergreen Review, vol. 2, no. 6 (Autumn 1958); "
         "reprinted in The New American Poetry, 1945-1960, ed. Donald Allen (1960) and in The Collected "
         "Poems of Frank O'Hara (1971). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The poem was not read complete; the summary follows the published descriptions of its structure "
        "and the passages quoted in the sources consulted.",
  ver="partially verified", sources=[W_EV, W_FO, W_PF_FO, NAAL]),
]

WORKS += [
W10("Coal", AL, "1968", "Poem (free verse)", "significant",
  genres=G("Free Verse", "Political Poetry", "Lyric Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Identity, authenticity and the divided self", "The city, the suburb and modern space"),
  movements=M(BAM, FEM2),
  overview="A poem collected in Lorde's first book, The First Cities (1968) and used as the title poem of Coal "
           "(1976): a short lyric in which the blackness of coal is turned from a metaphor of injury into an "
           "image of value, heat and art.",
  content="A short poem in open form, in which coal - black, buried, flammable, precious - is set beside the "
          "poet's own blackness, and the poem ends by claiming the jewel that the miners' labour produces.",
  summary="The poem is short and concentrated, and works by turning a single image. Coal is black, is dug "
          "out of the earth, is dirty to handle and is the source of heat and light; the poet takes that "
          "image and puts it beside the blackness of her own body and her own people, so that the "
          "centuries of association of blackness with dirt, night and death are reversed into an image of "
          "concentrated value and energy. The poem moves from the mineral to the human and from the "
          "labour of mining to the labour of making a poem, and its imagery of pressure and transformation "
          "- the earth compressing what is buried into something hard and precious - becomes a way of "
          "describing the history of Black Americans. The close of the poem turns the image outward, from "
          "the stone to the person, and the poem's argument is complete in a few lines: what has been "
          "treated as base material is in fact the source of light.",
  themes_text="The poem's central work is the revaluation of blackness. Lorde takes a word that carries "
              "centuries of contempt and makes it the vehicle of beauty and power, a strategy she shared "
              "with the Black Arts movement but handled with her own economy: there is no rhetoric in the "
              "poem, only the image, and the reader is asked to see rather than to agree. Its second "
              "subject is art - coal is what diamonds are made of, and the poem's own compression is part "
              "of the claim - and its third is the earth itself, the buried and the mined, which connects "
              "it to the poems of place in Lorde's later work.",
  structure="A short open-form poem of some twenty lines in a single movement, without stanza divisions, "
            "built around one developing image rather than around narrative or argument; the poem's turn "
            "comes late, when the mineral image is applied to the speaker, and the last lines are "
            "declarative and short.",
  style="Spare free verse with very little punctuation and a syntax close to speech; the images are held "
        "apart from one another rather than joined by connectives; repetition of the key word as "
        "insistence rather than decoration; no regular metre, but a strong rhythm of short breaths.",
  ctx="Collected in The First Cities (1968), Lorde's first book, published by the Poet's Press, and made the "
      "title poem of Coal (1976), the selection from her first three books published by Norton; it belongs "
      "to the Black Arts movement of the later 1960s and to the first wave of Black feminist poetry, and "
      "it is the poem through which her early manner is usually introduced.",
  sig="One of Lorde's most anthologised poems and the source of the title of her best-known selection; it is "
      "a standard text in courses on Black American poetry and on the literature of the 1960s, and its "
      "handling of the blackness metaphor is regularly contrasted with the more programmatic poetry of "
      "the Black Arts movement.",
  canon="Major canon",
  crit="Criticism reads the poem as an early instance of Lorde's revaluation of blackness and as a response "
       "to the pejorative uses of 'coal' and 'black' in the American literary tradition; its brevity and "
       "its refusal of rhetoric have been discussed as a deliberate contrast with the public style of the "
       "Black Arts poets, and it is often read alongside 'The Woman Thing' and the later 'Black Mother "
       "Woman'.",
  biblio="Collected in The First Cities (New York: The Poet's Press, 1968); reprinted as the title poem of "
         "Coal (New York: W. W. Norton, 1976) and in The Collected Poems of Audre Lorde (1997). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was not read complete in an authorised edition; the account follows the published "
        "descriptions of the poem and the passages quoted in the sources consulted.",
  ver="partially verified", sources=[W_CP, W_AL, NAAL]),
W10("The Woman Thing", AL, "1970", "Poem (free verse)", "significant",
  genres=G("Free Verse", "Political Poetry", "Confessional Poetry"),
  themes=T("Gender, feminism and women's lives", "Sexuality, desire and the closet", "Race, racism and the struggle for civil rights"),
  movements=M(BAM, FEM2),
  overview="A poem printed in Cables to Rage (1970) and reprinted in Coal (1976): a first-person poem about "
           "the body, desire and the naming of a woman's experience, in which the poet refuses the "
           "language offered to her and makes her own.",
  content="A short poem in free verse, spoken in the first person, moving between the body, the memory of a "
          "girlhood and the wish to speak plainly about what a woman is and wants.",
  summary="The poem is short, first-person and direct, and its project is to name 'the woman thing' - the "
          "experience that the available vocabulary either sentimentalises or refuses to name at all. It "
          "moves between recollection and present statement, from a girlhood in which the body was a "
          "source of shame or secrecy to an adult claim on pleasure, work and speech, and its imagery is "
          "domestic and bodily rather than mythological. The poem's repetitions act as insistence: what "
          "the culture will not name, the poem names twice. Its tone is not confessional in the mode of "
          "the period's poetry of private suffering but public and declarative, and the 'I' of the poem "
          "speaks for a 'we' by the end.",
  themes_text="The poem's subject is the relation between a woman's body and her language: the 'woman "
              "thing' is both sexuality and the whole range of experience that patriarchy has treated as "
              "unspeakable, and the poem's act is to say it. It belongs to the early second wave's "
              "insistence that the personal is political, and to Lorde's distinctive version of that "
              "insistence, in which the naming of desire is inseparable from the naming of race: the "
              "woman of the poem is Black, and the poem's argument is that the two cannot be separated.",
  structure="A short poem in open form, without stanza divisions or regular metre, organised by repetition "
            "and by the alternation of memory and statement; the movement is from the private past to "
            "the public present, and the poem ends on a declaration rather than an image.",
  style="Plain free verse with short lines and sparse punctuation; conversational syntax and direct "
        "address; the diction deliberately avoids the ornamental, and the poem's force comes from the "
        "refusal of euphemism.",
  ctx="Printed in Cables to Rage (1970), Lorde's second collection, published by Broadside Press, and "
      "reprinted in Coal (1976) and in The Collected Poems; the dating of the poem to 1973 in the "
      "anthology's table of contents is presumably the date of a later printing, since the contents of "
      "Cables to Rage include it. It belongs to the poetry of Black women's sexuality of the early "
      "1970s, a subject almost unwritten in American verse before it.",
  sig="One of the poems through which Lorde's early treatment of Black female sexuality is taught; it is a "
      "standard text in courses on African American poetry and on feminist poetry of the 1970s, and it "
      "prepares the arguments of 'Uses of the Erotic' a decade later.",
  canon="Secondary canon",
  crit="Criticism reads the poem as an early and unusually explicit treatment of Black women's desire in "
       "American poetry, and as a poem that negotiates between the Black Arts movement's public rhetoric "
       "and the women's movement's private idiom; its place in Lorde's development towards the essays of "
       "the 1970s and 1980s is the usual frame.",
  biblio="Printed in Cables to Rage (Detroit: Broadside Press, 1970); reprinted in Coal (1976) and in The "
         "Collected Poems of Audre Lorde (1997). The anthology's list dates it 1973; the record follows "
         "the collection's contents. A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The poem's first book appearance is given as Cables to Rage on the evidence of the collection's "
        "contents as listed in library catalogues; no periodical printing was identified.",
  ver="partially verified", sources=[W_CP, W_AL, NAAL]),
]

WORKS += [
W10("Black Mother Woman", AL, "1973", "Poem (free verse)", "significant",
  genres=G("Free Verse", "Confessional Poetry", "Political Poetry"),
  themes=T("Family, marriage and domestic life", "Gender, feminism and women's lives", "Race, racism and the struggle for civil rights"),
  movements=M(FEM2, BAM),
  overview="A poem printed in From a Land Where Other People Live (1973): a daughter addresses the mother who "
           "taught her silence and endurance, and the poem holds love and reproach in the same breath as "
           "Lorde names the inheritance she means to change.",
  content="A first-person poem of address, in which the speaker, herself a mother, speaks to her own mother "
          "about what was handed down - silence, work, the care of others - and about what she means to do "
          "differently with her children.",
  summary="The poem is spoken by a daughter who is also a mother, and it moves between the two positions: "
          "the child who learned from her mother how to work, how to keep silence and how to survive, and "
          "the mother who looks at her own children and wants to hand on something other than silence. "
          "The address to the 'black mother woman' is tender and accusing at once: the mother's strength "
          "is recognised and celebrated, and so is the cost of it, both to the mother and to the "
          "daughter. The poem's images are domestic - hands, kitchens, the body's labour - and its "
          "rhythms are those of speech held under pressure. Towards the end the speaker turns from the "
          "past to the future and the poem becomes a promise: the inheritance will be altered, and the "
          "silence will not be passed on.",
  themes_text="The poem is about inheritance between women: what a mother gives a daughter, what it costs "
              "her to give it, and whether a daughter can both honour it and refuse part of it. Lorde "
              "writes the poem without sentimentality in either direction - the mother's endurance is "
              "real and so is the damage - and the figure of the 'black mother woman' gathers the "
              "specific history of Black American motherhood (labour, loss, the care of other people's "
              "children) with the general history of women. The poem's turn towards the daughter's own "
              "children makes it a poem about change rather than complaint, and it belongs with the "
              "essays on silence and anger that made Lorde's prose famous.",
  structure="A poem of address in open form, without stanza divisions, organised by the alternation "
            "between past and present and between the mother and the speaker's own children; repetition "
            "of the address at intervals gives the poem its shape, and the ending turns from memory to "
            "promise.",
  style="Plain free verse with short lines, sparse punctuation and a syntax close to speech at its most "
        "pressured; the repetition of the key address works as refrain; the diction refuses ornament, "
        "and the poem's emotion is carried by rhythm and repetition rather than by metaphor.",
  ctx="Printed in From a Land Where Other People Live (Detroit: Broadside Press, 1973), a National Book "
      "Award finalist, and reprinted in The Collected Poems; it belongs to the early 1970s literature of "
      "Black motherhood and to the poetry of the women's movement, and it is one of a group of Lorde "
      "poems - with 'The Woman Thing' and 'Coal' - in which her themes of race, gender and family are "
      "held together.",
  sig="One of Lorde's most frequently taught poems and a standard text on Black motherhood and on the "
      "mother-daughter poem in American literature; it is regularly set beside the work of Lucille "
      "Clifton and Gwendolyn Brooks, and it is the poem through which the autobiographical basis of "
      "Lorde's writing is usually introduced.",
  canon="Secondary canon",
  crit="Criticism reads the poem as a meditation on the reproduction of silence between Black women, and as "
       "a poem that complicates the celebration of maternal strength by naming its cost; the relation "
       "between the poem and Lorde's essays on silence ('The Transformation of Silence into Language and "
       "Action') is the usual critical frame.",
  biblio="Printed in From a Land Where Other People Live (Detroit: Broadside Press, 1973); reprinted in The "
         "Collected Poems of Audre Lorde (1997). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The poem's first appearance in book form is given from the collection's contents as listed in "
        "library catalogues; no periodical printing was identified, and the poem was not read complete.",
  ver="partially verified", sources=[W_CP, W_AL, NAAL]),
W10("Uses of the Erotic: The Erotic as Power", AL, "1978", "Essay (address)", "major",
  genres=G("Literary Essay", "Feminist Criticism", "Political Essay"),
  themes=T("Gender, feminism and women's lives", "Sexuality, desire and the closet", "Art, the artist and the creative life"),
  movements=M(FEM2),
  overview="An address delivered at the Fourth Berkshire Conference on the History of Women at Mount Holyoke "
           "on 25 August 1978, published first as a pamphlet and collected in Sister Outsider (1984): Lorde "
           "defines the erotic as a source of knowledge and power and distinguishes it from the "
           "pornographic.",
  content="A prose address in numbered sections in which Lorde argues that the erotic is a resource of "
          "deep knowledge and satisfaction that women have been taught to distrust, that it is not the "
          "same as the sexual and not the same as the pornographic, and that claiming it is a political "
          "act with consequences for work, friendship and love.",
  summary="Lorde begins by naming the erotic as a resource 'within each of us' that lies 'in a deeply "
          "female and spiritual plane' and that has been made suspect: women have been taught that the "
          "erotic is a sign of the inferior, the animal or the merely sexual, and the result is that the "
          "power attached to it has been surrendered. She distinguishes the erotic from the pornographic "
          "with the neat formula that pornography is 'sensation without feeling' while the erotic is "
          "'feeling without sensation' - that is, the erotic is a mode of attention and knowledge that "
          "informs everything a woman does, from the making of a poem to the making of a bed. She "
          "illustrates with the difference between the demanding and the merely adequate in work, in "
          "friendship and in love; argues that the erotic is a measure of what we can ask of ourselves "
          "and others; and concludes that the erotic is a source of political power, because a woman who "
          "knows what satisfies her cannot be persuaded that she deserves less. The address is "
          "interrupted, in printed form, by its circumstances - it was delivered to an audience of "
          "historians of women - and its tone is the tone of the platform rather than the study. Its "
          "last movement turns from definition to obligation: to feel the erotic is to know what one can "
          "demand of oneself, and that knowledge is what makes political action possible.",
  themes_text="The essay's central claim is that the erotic is a form of knowledge rather than a form of "
              "pleasure, and that the distinction between the erotic and the pornographic is the "
              "distinction between attention and consumption. From that follow its political claims: that "
              "women's distrust of their own satisfaction is a form of internalised oppression; that the "
              "energy of the erotic can be carried into work and politics; that the 'false belief that "
              "only the sexual is a proper source of power' keeps women divided from one another. The "
              "essay is also a link between the feminist and Black liberation arguments that Lorde made "
              "throughout Sister Outsider: the erotic is one of the resources with which difference can "
              "be lived rather than feared.",
  structure="A spoken address in numbered sections, opening with a definition, moving through the "
            "distinction between the erotic and the pornographic, the account of what the erotic "
            "supplies to work and relationship, and the political conclusion; the paragraphs are short "
            "and declarative, and the argument advances by assertion and illustration rather than by "
            "citation.",
  style="Direct address in the second person and the first person plural; short paragraphs with "
        "aphoristic closing sentences; a vocabulary that mixes the spiritual ('a deeply female and "
        "spiritual plane') with the political ('the erotic as power'); repetition and antithesis used as "
        "oral devices, as in the phrase that became its summary, 'pornography is sensation without "
        "feeling'.",
  ctx="Delivered at the Fourth Berkshire Conference on the History of Women at Mount Holyoke College on 25 "
      "August 1978 and first published as a pamphlet by Out & Out Books; collected as the second essay in "
      "Sister Outsider: Essays and Speeches (Trumansburg, NY: Crossing Press, 1984). It belongs to the "
      "second wave's debates about sexuality and to the Black feminist critique of a feminism organised "
      "around white women's experience.",
  sig="One of the founding documents of Black feminist thought and one of the most cited American essays of "
      "the period; it is a standard text in women's, gender and sexuality studies, it named the erotic as "
      "a political category, and it is the essay through which Lorde's thought is most often taught "
      "alongside 'The Master's Tools'.",
  canon="Major canon",
  crit="Criticism reads the essay as a revaluation of a category that Western thought had placed below "
       "reason, as a contribution to the feminist ethics of pleasure, and as a text that complicates the "
       "period's debates between feminist anti-pornography and sex-radical positions; its relation to "
       "Audre Lorde's poetry of the same years, and to the tradition of Black women's writing about the "
       "body, has been widely discussed.",
  biblio="Delivered 25 August 1978; published as a pamphlet by Out & Out Books (1978) and later by Kore "
         "Press; collected in Sister Outsider: Essays and Speeches (1984) and in I Am Your Sister (2009). "
         "A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The essay was read through the printed text in Sister Outsider as quoted in the sources consulted; "
        "the pamphlet's exact place and date of publication are given as the second-hand descriptions "
        "state them.",
  ver="partially verified", sources=[W_SO, W_AL, NAAL]),
W10("The Master's Tools Will Never Dismantle the Master's House", AL, "1979", "Essay (address)", "major",
  genres=G("Literary Essay", "Feminist Criticism", "Political Essay"),
  themes=T("Gender, feminism and women's lives", "Race, racism and the struggle for civil rights", "Power, the state and surveillance"),
  movements=M(FEM2, BAM),
  overview="Comments delivered at the Second Sex Conference in New York on 29 September 1979 and printed in "
           "This Bridge Called My Back (1981) and in Sister Outsider (1984): an attack on a feminism that "
           "invites Black and lesbian women as tokens and a demand that difference be made the ground of "
           "political work.",
  content="A short address in which Lorde answers the organisers of a conference on Simone de Beauvoir, "
          "names the absence of Black and lesbian women from its programme, and argues that a movement "
          "cannot be liberated with the instruments of the system it opposes.",
  summary="Lorde speaks as a panellist at a conference marking thirty years of The Second Sex, and her "
          "remarks begin with the fact that the programme she has been invited to join has almost no "
          "Black women in it: the absence is the argument. She refuses the position of the token, "
          "describes the ways in which Black women and lesbians are asked to be present without being "
          "heard, and turns the conference's own subject - Beauvoir's account of woman as other - "
          "against it, pointing out that a feminism which makes the experience of white, middle-class, "
          "heterosexual women the measure of womanhood reproduces the structure it claims to oppose. "
          "Her central formulation is that the master's tools will never dismantle the master's house: "
          "the methods of a system cannot be used to end it. The address ends with a call to recognise "
          "difference - of race, sexuality, class and age - not as an obstacle to solidarity but as the "
          "material of it, and with the warning that a movement which cannot hear the difference within "
          "it will fail. The address is short - a few pages - and its force comes from the collision "
          "between the courtesy of the panel and the anger of the intervention: Lorde thanks the "
          "organisers and then tells them that their conference has reproduced the exclusions it "
          "denounces, and her own presence on the platform becomes the evidence for her argument.",
  themes_text="The essay's argument is about the difference between inclusion and transformation: a "
              "conference, a movement or a theory that adds Black and lesbian women to an unchanged "
              "structure has not changed the structure. Lorde's terms are interlocking - race, class, "
              "sexuality and age are not separate oppressions to be ranked but a single complex reality - "
              "and her target is a white feminism that treats its own experience as universal. The essay "
              "is also a document of its occasion: the anger in it is directed at a particular room, and "
              "Lorde's insistence that anger is a source of information rather than a failure of "
              "civility became one of the most quoted arguments of Black feminist writing.",
  structure="A short address in a handful of paragraphs, opening with the fact of exclusion, moving to the "
            "critique of the conference's theory, then to the general claim about tools and the house, "
            "and ending with a demand; the paragraphs are built as a sequence of assertions, and the last "
            "sentences are a warning and a promise.",
  style="Direct, first-person, spoken prose with short declarative sentences and a few memorable "
        "formulations; anger held in formal syntax; the second person used to address the audience "
        "directly ('those of us who stand outside the circle of this society's definition of acceptable "
        "women'); no footnotes and no hedging.",
  ctx="Delivered as comments at the 'Personal and the Political' panel of the Second Sex Conference at New "
      "York University on 29 September 1979, the conference marking the thirtieth anniversary of "
      "Beauvoir's The Second Sex; printed in This Bridge Called My Back: Writings by Radical Women of "
      "Color, ed. Cherrie Moraga and Gloria Anzaldua (1981), and in Sister Outsider (1984). It is one of "
      "the founding texts of intersectional feminism and of the Black feminist critique of the second "
      "wave.",
  sig="One of the most quoted American essays of the twentieth century and a founding text of "
      "intersectionality; the sentence that gives it its title has become a proverb of political "
      "organising, the essay is a standard text in women's, gender and Black studies, and its argument "
      "about difference as the ground of solidarity shaped a generation of feminist theory.",
  canon="Major canon",
  crit="Criticism reads the essay as the clearest statement of Lorde's theory of interlocking oppressions "
       "and as a key document in the history of the second wave's internal conflicts; its rhetoric, its "
       "use of the conference as a scene and its argument about anger have been widely analysed, and it "
       "is routinely taught with This Bridge Called My Back and with Kimberle Crenshaw's later work on "
       "intersectionality.",
  biblio="Delivered 29 September 1979; first printed in This Bridge Called My Back: Writings by Radical "
         "Women of Color, ed. Cherrie Moraga and Gloria Anzaldua (Watertown, MA: Persephone Press, 1981); "
         "collected in Sister Outsider: Essays and Speeches (1984). A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The address was read through its printed text in the sources consulted; the date of delivery is "
        "given as the sources state it (29 September 1979), and the collection's own dating to 1979 in the "
        "anthology's list is consistent with it.",
  ver="partially verified", sources=[W_SO, W_AL, NAAL]),
]

WORKS += [
W10("Against Interpretation", SS, "1964", "Essay (critical essay)", "major",
  genres=G("Cultural Criticism", "Literary Criticism and Theory (1946–2000)", "Literary Essay"),
  themes=T("Art, the artist and the creative life", "Language, writing and the limits of representation", "Technology, media and consumer society"),
  movements=M("Postmodernism and Postmodern Fiction"),
  overview="An essay published in the Evergreen Review in December 1964 and collected as the title essay of "
           "Against Interpretation (1966): Sontag argues that modern criticism has substituted the hunt for "
           "hidden meaning for the experience of art, and calls for an 'erotics' of art in place of a "
           "hermeneutics.",
  content="A prose essay in which Sontag describes the modern habit of interpretation, traces its history "
          "from the Greeks through Freud and Marx, argues that it has become a way of taming and "
          "diminishing art, and ends with a set of proposals for a criticism that would attend to the "
          "surface of works.",
  summary="Sontag begins from a fact about the modern reader: that the first question asked of a work of "
          "art is what it means, and that interpretation - the translation of the visible into a hidden "
          "content - has become the dominant activity of criticism. She distinguishes two historical "
          "kinds of interpretation: the pre-modern kind, which sought to bring old texts up to date by "
          "allegory, and the modern kind, which she describes as 'excavating' and destroying, treating "
          "the work as a symptom of something the critic already knows (the Oedipal, the economic, the "
          "ideological). She argues that the modern style of interpretation has become a defensive "
          "response to the difficulty of modern art, a way of making it manageable; that it separates "
          "form from content, and that the separation is false; that the flight from interpretation is at "
          "the root of much of modern art's own difficulty; and that what is needed instead is a "
          "criticism that attends to the surface of works - to their descriptions, their textures, their "
          "ways of doing whatever they do. The essay's last sentences give the famous formula: 'In place "
          "of a hermeneutics we need an erotics of art.' The essay's method is to describe a habit of "
          "reading, give it a history, show what it costs, and propose a discipline in its place; its "
          "confidence comes from the assumption that criticism is a form of writing with its own "
          "pleasures, and its polemical edge from the conviction that most contemporary criticism had "
          "stopped looking at works of art altogether.",
  themes_text="The essay's argument is about attention: to interpret a work in the modern manner is to "
              "replace it with a meaning that the critic already possessed, and so to lose the work's "
              "particularity. Sontag's alternative is descriptive rather than doctrinal - a criticism of "
              "form, of surface, of the sensuous life of works - and she connects it to the experience of "
              "contemporary art (abstract painting, the New Novel, the films of Bresson and Godard) in "
              "which the surface is not a veil over a meaning but the whole thing. The essay is also a "
              "document of the 1960s' argument with the New Criticism and with psychological and Marxist "
              "criticism, and of a moment when high and popular art began to be discussed in the same "
              "vocabulary.",
  structure="An essay of some twenty pages in numbered sections, moving from description to history to "
            "polemic to prescription; the argument is carried by antithesis (form and content, depth and "
            "surface, hermeneutics and erotics) and ends with a compressed statement of aims rather than "
            "a conclusion.",
  style="Aphoristic, confident, declarative prose with short paragraphs and frequent italicised terms; "
        "sentences built as definitions and reversals; a taste for lists and for the imperative; a first "
        "person plural that speaks for the age ('our culture', 'we are taught'), balanced by a critic's "
        "willingness to praise and blame particular works.",
  ctx="First published in the Evergreen Review, vol. 8, no. 34 (December 1964), and collected as the "
      "opening essay of Against Interpretation and Other Essays (New York: Farrar, Straus and Giroux, "
      "1966), a finalist for the National Book Award; it belongs to Sontag's early New York period, when "
      "she was writing for the little magazines and the Partisan Review circle, and to the 1960s "
      "rethinking of criticism that produced the New Sensibility and the study of popular culture.",
  sig="Among the most influential American essays of the century: it named a whole critical disposition, "
      "gave a generation its formula for describing works of art, and opened the way for the cultural "
      "studies and postcritique that followed; the essay is a standard text in courses on criticism and "
      "theory, and its closing phrase, 'an erotics of art', is one of the most quoted in modern "
      "criticism.",
  canon="Major canon",
  crit="Criticism has read the essay as the founding statement of a formalist and aestheticist criticism, "
       "as a transitional moment between the New Criticism and poststructuralism, and as a text whose "
       "influence on the 'postcritique' of the 2000s and 2010s has been acknowledged by its own "
       "originators; its relation to Robbe-Grillet's arguments for a 'poetics of presence', to camp and "
       "to the New Sensibility has all been discussed.",
  biblio="First published in the Evergreen Review, vol. 8, no. 34 (December 1964); collected in Against "
         "Interpretation and Other Essays (New York: Farrar, Straus and Giroux, 1966). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The essay was read through the printed text and the sources consulted; quotations are short and "
        "confined to the sentences for which the essay is known.",
  ver="partially verified", sources=["Against Interpretation (Wikipedia)", "Susan Sontag (Wikipedia)", W_EV, NAAL]),
]
