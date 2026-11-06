"""Installment 10, wave 29: Amiri Baraka, N. Scott Momaday, Mary Oliver and
Lucille Clifton, with two poems restored to authors recorded earlier.

Five new authors and fifteen works, plus two poems for Audre Lorde and Allen
Ginsberg, whose author records exist and who were recorded in wave 24 and wave
25 with only some of their Norton selections.

First printings settled here:

    Amiri Baraka, "An Agony. As Now."           The Dead Lecturer (Grove Press, 1964)
    Amiri Baraka, "A Poem for Willie Best"      The Dead Lecturer (Grove Press, 1964)
    Amiri Baraka, "Black Art"                   The Liberator, January 1966
    Amiri Baraka, "Will They Cry When You're
        Gone, You Bet"                          Black Magic (Bobbs-Merrill, 1969)
    N. Scott Momaday, "Headwaters"              The Way to Rainy Mountain (UNM Press, 1969)
    N. Scott Momaday, The Way to Rainy Mountain  University of New Mexico Press, 1969
    Mary Oliver, "The Summer Day"               House of Light (Beacon Press, 1990)
    Lucille Clifton, "miss rosie"               Good Times (Random House, 1969)
    Lucille Clifton, "the lost baby poem"       Good News About the Earth (Random House, 1972)
    Lucille Clifton, "homage to my hips"        Two-Headed Woman (Massachusetts, 1980)
    Lucille Clifton, "wishes for sons"          Quilting (BOA Editions, 1991)
    Lucille Clifton, "blessing the boats"       Quilting (BOA Editions, 1991)
    Lucille Clifton, "to my last period"        Quilting (BOA Editions, 1991)
    Lucille Clifton, "wild blessings"           Quilting (BOA Editions, 1991)
    Audre Lorde, "Poetry Is Not a Luxury"       Chrysalis, 1977; Sister Outsider (1984)
    Allen Ginsberg, "Footnote to Howl"          Howl and Other Poems (City Lights, 1956)
    Allen Ginsberg, "A Supermarket in California" Howl and Other Poems (City Lights, 1956)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

AB = "Amiri Baraka"
NSM = "N. Scott Momaday"
MO = "Mary Oliver"
LC = "Lucille Clifton"

BAM = "Black Arts Movement"
AAW = "Postwar African American Writing: Protest and Its Critics"
NAR = "Native American Renaissance"
SWF = "Second-Wave Feminist Writing"
BEAT = "The Beat Generation"
CONF = "Confessional Poetry"

W_AB = "Amiri Baraka (Wikipedia)"
W_AB_PF = "Amiri Baraka, Poetry Foundation author page and poem notes"
W_DEAD = "The Dead Lecturer (Grove Press, 1964), library catalogue record with contents"
W_BLACKART = "Black Art (poem) (Wikipedia), with the Liberator and Sonny's Time Now first appearances"
W_BLACKMAGIC = "Black Magic: Sabotage, Target Study, Black Art; Collected Poetry 1961-1967 (Bobbs-Merrill, 1969), catalogue record"
W_NSM = "N. Scott Momaday (Wikipedia)"
W_RAINY = "The Way to Rainy Mountain (University of New Mexico Press, 1969), bibliographic and contents record"
W_MO = "Mary Oliver (Wikipedia)"
W_HOL = "House of Light (Beacon Press, 1990), publisher's note on 'The Summer Day'"
W_LC = "Lucille Clifton (Wikipedia)"
W_LC_EBSCO = "Lucille Clifton, EBSCO Research Starters and Poetry Foundation author page"
W_GOODTIMES = "Good Times (Random House, 1969) and Two-Headed Woman (University of Massachusetts Press, 1980), catalogue records"
W_QUILT = "Quilting: Poems 1987-1990 (BOA Editions, 1991), contents and the collected-poems table of contents"

AUTHORS = [
A10(AB, MAJ, "1934", "2014", "Newark, New Jersey, United States",
  "American; poet, playwright, essayist, music critic and activist writing in English",
  "American poet and playwright, the central theorist and most visible figure of the Black Arts Movement, whose Dutchman and The Dead Lecturer turned the anger of the early 1960s into a poetry of public address and whose later work moved through Black nationalism to Marxism",
  "Amiri Baraka was born Everett LeRoi Jones in Newark, New Jersey, on 7 October 1934, the son of a postal supervisor and a social worker; he grew up in the city's predominantly Black Central Ward, which he would write about for sixty years. He took a BA in English at Howard University in 1954, served in the US Air Force as a meteorologist and gunner from 1954 to 1957 - a period he described as the beginning of his political education, and which ended with a discharge after his annotated copy of Lenin was found - and settled in Greenwich Village, where he co-edited the little magazines Yugen and Kulchur and ran Totem Press, publishing Frank O'Hara, Diane di Prima and Jack Kerouac. Preface to a Twenty Volume Suicide Note (1961) was his first book of poems; Blues People: Negro Music in White America (1963) was the first full-length history of Black music by a Black American writer; The Dead Lecturer (1964) and the plays Dutchman and The Slave (1964) made him, at thirty, the most discussed Black writer in the country. After the assassination of Malcolm X in February 1965 he left Greenwich Village for Harlem, founded the Black Arts Repertory Theatre/School, and published the essays of Home: Social Essays (1966); he took the name Imamu Amiri Baraka in 1967, returned to Newark after the riots of that year, and was arrested and beaten by police during the disturbances, an experience recorded in his play and in his testimony. Black Magic (1969) collected the nationalist poetry; from the early 1970s he moved towards Marxism-Leninism and organised in Newark through the Congress of Afrikan People and later the League of Revolutionary Struggle, writing Hard Facts (1975) and Poetry for the Advanced (1979). He taught at the State University of New York at Stony Brook from 1985 until his retirement in 2013, was appointed New Jersey's second poet laureate in 2002 and held the post for sixteen months before it was abolished, and died in Newark on 9 January 2014.",
  "Poetry: Preface to a Twenty Volume Suicide Note (1961), The Dead Lecturer (1964), Black Art (1966), Black Magic: Sabotage; Target Study; Black Art (1969), It's Nation Time (1970), Spirit Reach (1972), Hard Facts (1975), Poetry for the Advanced (1979), Reggae or Not! (1981), Transbluesency: The Selected Poems 1961-1995 (1995) and Somebody Blew Up America and Other Poems (2003). Drama: Dutchman and The Slave (1964), The Baptism and The Toilet (1966), The Slave Ship (1969), Four Black Revolutionary Plays (1969) and The Motion of History (1978). Prose: Blues People (1963), Home: Social Essays (1966), Black Music (1968), Raise Race Rays Raze (1971), The Autobiography of LeRoi Jones (1984) and Digging: The Afro-American Soul of American Classical Music (2009).",
  "A poetry built for the voice, with the line broken wherever the breath or the argument breaks; the vernacular and the obscene used as instruments of refusal; the names of the dead spoken aloud; a jazz-derived rhythm that repeats a phrase until it becomes a demand; and, in the later work, the flat declarative sentence of the political pamphlet set inside the lyric.",
  "Race and the refusal of assimilation; the Black artist's obligation to the community; Malcolm X, Newark and the memory of the 1967 rebellion; the relation of Black music - blues, bebop, free jazz - to Black writing; the American state as a machine of violence; and, in the late work, class and empire alongside race.",
  "Baraka is the founder and the most influential figure of the Black Arts Movement, and the writer through whom the American avant-garde of the 1950s became the Black nationalism of the 1960s. Dutchman is a set text and a standing part of the American repertoire; 'Black Art' is the poem most often reprinted to define the movement's aesthetic; Blues People remains the founding work of Black music criticism; and his influence on the poets of the Black Arts generation is acknowledged on every side.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Baraka, the Poetry Foundation's author page, and library catalogue records of The Dead Lecturer and Black Magic; they were not checked against a printed bibliography. Installment 10 records four Norton selections - 'An Agony. As Now.', 'A Poem for Willie Best', 'Black Art' and 'Will They Cry When You're Gone, You Bet' - so the other books of poems, the plays, the essays and the music criticism have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_AB, W_AB_PF, W_DEAD, W_BLACKART, NAAL]),
A10(NSM, MAJ, "1934", "2024", "Lawton, Oklahoma, United States",
  "American; Kiowa novelist, poet, essayist and scholar writing in English",
  "Kiowa American novelist, poet and scholar whose House Made of Dawn won the Pulitzer Prize in 1969 and opened the Native American Renaissance, and whose The Way to Rainy Mountain remade the essay and the poem as instruments of tribal history",
  "Navarre Scott Momaday was born in Lawton, Oklahoma, on 27 February 1934, of Kiowa descent through his father, the painter Al Momaday, and English and Cherokee descent through his mother, Natachee Scott Momaday, a writer and teacher; he spent his childhood on reservations in the Southwest, principally at Jemez Pueblo in New Mexico, and drew on that upbringing in everything he wrote. He took a BA in political science at the University of New Mexico in 1958, an MA and a PhD in English at Stanford, where he studied with Yvor Winters, and taught at the University of California at Santa Barbara, Berkeley, Stanford and, from 1982, the University of Arizona, where he was Regents Professor of English and founded the poetry centre that now bears his name. House Made of Dawn (1968), his first novel, won the Pulitzer Prize for Fiction in 1969 and is generally taken as the beginning of the Native American Renaissance; The Way to Rainy Mountain (1969), illustrated by his father, retraced the Kiowa migration from the Yellowstone headwaters to the Wichita Mountains through legend, historical commentary and memoir. Angle of Geese and Other Poems (1974), The Gourd Dancer (1976), The Names: A Memoir (1976), The Ancient Child (1989), In the Presence of the Sun (1992) and The Man Made of Words (1997) followed. He was awarded the National Medal of Arts in 2007 and a Pulitzer Prize for Poetry in 2024 for the posthumous collection The Earth in Our Hands, delivered the first Native American inaugural benediction in 2021, and died in Santa Fe, New Mexico, on 24 January 2024.",
  "Fiction: House Made of Dawn (1968), The Ancient Child (1989) and the children's book Circle of Wonder (1994). Poetry: Angle of Geese and Other Poems (1974), The Gourd Dancer (1976), In the Presence of the Sun: Stories and Poems 1961-1991 (1992), Again the Far Morning: New and Selected Poems (2011) and The Earth in Our Hands (2024). Prose: The Journey of Tai-me (1967), The Way to Rainy Mountain (1969), The Names: A Memoir (1976), The Man Made of Words (1997) and Three Plays (2007).",
  "A prose that moves between three registers without warning - the oracular, the documentary and the anecdotal - and sets them side by side rather than blending them; a syntax that takes the cadence of oral narrative and slows it to the pace of writing; the landscape as a participant rather than a setting; and a habit of ending a passage on a sentence that sounds like a proverb without being one.",
  "The land and the memory of a people's migration; the oral tradition as a form of history; the relation of the individual to the tribe and of the tribe to the American state; the Kiowa and Jemez sacred landscape of Oklahoma and New Mexico; loss, survival and the continuity of language; and the act of bearing witness as the writer's office.",
  "Momaday is the founding figure of the Native American Renaissance and the writer most responsible for the presence of Native American literature in the American canon. House Made of Dawn's Pulitzer Prize in 1969 is the event that criticism dates the beginning of that renaissance from, The Way to Rainy Mountain is a standard text in courses on American autobiography and on the essay, and his 2024 Pulitzer for poetry made him one of the few writers honoured in two genres by that prize.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Momaday and from the bibliographic record of The Way to Rainy Mountain; they were not checked against a printed bibliography. Installment 10 records two Norton selections - 'Headwaters' and the selections from The Way to Rainy Mountain, which share one record - so the novels, the other poems and the plays have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_NSM, W_RAINY, NAAL]),
A10(MO, MAJ, "1935", "2019", "Maple Heights, Ohio, United States",
  "American; poet and essayist writing in English",
  "American poet, the best-selling poet in the United States in the last quarter of the twentieth century, whose close attention to the ordinary natural world - the grasshopper, the pond, the owl - made a devotional poetry of observation that a mass readership took to its own",
  "Mary Jane Oliver was born in Maple Heights, Ohio, on 10 September 1935 and grew up in a house she later described as unhappy; she began writing poems at fourteen, and at seventeen visited Edna St. Vincent Millay's house in Austerlitz, New York, and stayed to help the family sort Millay's papers, a stay that she said decided her life. She attended Ohio State University and Vassar College without taking a degree, moved to Provincetown, Massachusetts, in the late 1950s, and lived there for the rest of her life with the photographer Molly Malone Cook, running a small bookshop and later working as an editor at the Provincetown house of the publisher Houghton Mifflin. No Voyage and Other Poems (1963) was her first book; she published it at twenty-eight. She wrote at first in the formal metres she had learned from Millay and from her reading of the English Romantics, then, from the late 1960s, in a stripped free verse of short lines and single images. American Primitive (1983) won the Pulitzer Prize for Poetry; New and Selected Poems (1992) won the National Book Award; House of Light (1990), from which 'The Summer Day' comes, won the Christopher Award and the L. L. Winship/PEN New England Award; Why I Wake Early (2004), Thirst (2006), Evidence (2009), Swan (2010), A Thousand Mornings (2012), Dog Songs (2013), Blue Horses (2014) and Felicity (2015) followed. She gave very few interviews and readings and refused most public appearances, and died at her home in Hobe Sound, Florida, on 17 January 2019.",
  "Poetry: No Voyage and Other Poems (1963), The River Styx, Ohio and Other Poems (1972), The Night Traveler (1978), Sleeping in the Forest (1979), Twelve Moons (1979), American Primitive (1983), Dream Work (1986), Provincetown (1987), House of Light (1990), New and Selected Poems (1992), White Pine (1994), West Wind (1997), The Leaf and the Cloud (2000), What Do We Know (2002), Owls and Other Fantasies (2003), Why I Wake Early (2004), Blue Iris (2004), Thirst (2006), Red Bird (2008), Evidence (2009), Swan (2010), A Thousand Mornings (2012), Dog Songs (2013), Blue Horses (2014), Felicity (2015) and Devotions (2017). Prose: A Poetry Handbook (1994), Rules for the Dance (1998), Winter Hours (1999), Long Life (2004) and Upstream (2016).",
  "Short free-verse lines, often unpunctuated or lightly punctuated, each carrying one image; a repeated question addressed to the world rather than to a person; a vocabulary of ordinary things - grass, pond, heron, blackberries - used without ornament; and an ending that turns the observation into a direct address to the reader, which is the move her critics hold against her and her readers love her for.",
  "Attention as a discipline and a form of praise; the natural world as a place where the sacred is available without doctrine; mortality, and the ordinary fact of being alive in a body; solitude, walking and the deliberate narrowness of a life; and, in the later books, grief, and the death of the companion she lived with for forty years.",
  "Oliver is the most widely read American poet of the last forty years and the one whose work has done most to keep a general readership for poetry in the United States: New and Selected Poems sold more than a million copies, and 'The Summer Day', with its closing question about 'your one wild and precious life', is among the most quoted American poems of the period. Her Pulitzer Prize and National Book Award make her the most decorated popular poet of her generation; academic criticism has been slower than the public, and the argument about her is now a standard part of the discussion of American poetry's readership.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Oliver and the Poetry Foundation's author page; they were not checked against a printed bibliography. Installment 10 records one Norton selection - 'The Summer Day' - so the twenty-odd other collections, the essays and the handbooks have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_MO, W_HOL, NAAL]),
A10(LC, MAJ, "1936", "2010", "Depew, New York, United States",
  "American; poet, memoirist and children's writer writing in English",
  "American poet whose short, unpunctuated, lower-case poems of family, body and history made a vernacular lyric of Black American womanhood, and whose eleven collections and twenty-one children's books carried that voice to a readership far beyond the poetry world",
  "Lucille Clifton was born Thelma Lucille Sayles in Depew, New York, on 27 June 1936, the daughter of a steelworker and a laundress, and grew up in Buffalo; she was the first person in her family to finish high school, took a scholarship to Howard University in 1953, and left after two years for Fredonia State Teachers College, where she acted in a production of a play by the poet Ishmael Reed, who became a friend and sent her poems to Langston Hughes. She married Fred Clifton, a philosophy teacher and sculptor, in 1959, and they had six children; his death in 1984 is the subject of much of her later work. Her first collection, Good Times (1969), was chosen by The New York Times as one of the ten best books of the year, and she published it while raising the children and working as a clerk and as a literature assistant at the US Department of Education. Good News About the Earth (1972), An Ordinary Woman (1974), Two-Headed Woman (1980, the Juniper Prize), Next (1987), Quilting: Poems 1987-1990 (1991), The Book of Light (1993), The Terrible Stories (1996), Blessing the Boats: New and Selected Poems 1988-2000 (2000, the National Book Award), Mercy (2004) and Voices (2008) followed. She taught at Columbia, George Washington University and St. Mary's College of Maryland, served as poet laureate of Maryland from 1979 to 1985, read at the first and second inaugurations of Bill Clinton, and died in Baltimore on 13 February 2010.",
  "Poetry: Good Times (1969), Good News About the Earth (1972), An Ordinary Woman (1974), Two-Headed Woman (1980), Next (1987), Quilting: Poems 1987-1990 (1991), The Book of Light (1993), The Terrible Stories (1996), Blessing the Boats: New and Selected Poems 1988-2000 (2000), Mercy (2004) and Voices (2008); collected in The Collected Poems of Lucille Clifton 1965-2010 (2012). Memoir: Generations (1976). Children's books: twenty-one titles, including the Everett Anderson series (1970-1983) and The Lucky Stone (1979).",
  "Very short free-verse poems in lower case, without punctuation, so that a line break does the work a comma would do; a plain vocabulary and a syntax close to speech; the single image held for a whole poem; a repeated name or phrase as a refrain; and an ending that is usually a flat declarative sentence, which is where the poem's emotional weight lands.",
  "Family and ancestry, especially the mother and the Dahomey women she claimed as forebears; the Black female body, its appetites and its changes; motherhood and the loss of children; death, and the deaths of her husband and her parents; the Black American past, from slavery to the civil rights movement; and the ordinary dignity of people the society has set aside.",
  "Clifton is one of the central American poets of the postwar period and the one whose formal economy did most to show that a poem of twenty short lines could carry a history. Blessing the Boats won the National Book Award in 2000, she held the Maryland laureateship for six years, and her influence runs through the Black Arts and feminist poetry of the 1970s into the work of the poets who came after; 'homage to my hips' and 'miss rosie' are among the most anthologised American poems of the period.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Clifton, the EBSCO and Poetry Foundation author pages, and catalogue records of Good Times, Two-Headed Woman and Quilting; they were not checked against a printed bibliography. Installment 10 records seven Norton selections - 'miss rosie', 'the lost baby poem', 'homage to my hips', 'wishes for sons', 'blessing the boats', 'to my last period' and 'wild blessings' - so the other collections, the memoir and the twenty-one children's books have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_LC, W_LC_EBSCO, W_GOODTIMES, W_QUILT, NAAL]),
]

WORKS = [
W10("An Agony. As Now.", AB, "1964", "Poem (free verse)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Confessional Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Identity, authenticity and the divided self",
           "Alienation, absurdity and existential freedom"),
  movements=M(BEAT, BAM),
  overview="'An Agony. As Now.' is the sixth poem in The Dead Lecturer (New York: Grove Press, 1964), the "
           "collection Baraka published under the name LeRoi Jones a year before the assassination of "
           "Malcolm X and two years before he left Greenwich Village for Harlem. It is a first-person "
           "poem about being housed in a body that hates the person living in it, and it is the clearest "
           "statement in the book of the separation between the poet's public position and his inner "
           "life that the whole collection is about.",
  content="The poem begins 'I am inside someone / who hates me.' The speaker looks out through the eyes "
          "of that other, watches him eat and drink and move through the world, and describes the "
          "humiliation of being carried around by a self that is not his own. The imagery is of "
          "enclosure and infection: the body as a room, as a machine, as something the speaker has been "
          "put inside rather than something he is. In the middle of the poem the speaker addresses the "
          "person he is inside and asks what the arrangement is for; then the poem turns outward, to "
          "love, to the woman in the room, to the world of the city, and the private agony becomes a "
          "general condition. The poem ends not with resolution but with the speaker still inside, still "
          "watching, having discovered that the self he would like to be cannot be reached from where he "
          "is standing.",
  summary="The poem is built on a single conceit - the self as a dwelling occupied by someone else - and "
          "it tests that conceit until it yields a political meaning. The 'someone who hates me' is at "
          "first a psychological double, the mask the poet wears in the white bohemia of the early "
          "1960s; by the end of the poem it is also the American arrangement in which a Black writer is "
          "permitted to be present only as a performance. Baraka's line here is short, flat and "
          "unornamented, and the flatness is the point: the poem refuses the lyric consolations that "
          "have been available to it and stays with the description of a self divided against itself. "
          "The Dead Lecturer is the book in which Baraka breaks with the Beats, and 'An Agony. As Now.' "
          "is the poem that states why: the alienation the Beats had made into a style was, for him, "
          "not a style but a condition with a history. Read against 'Black Art', written two years later, "
          "the poem marks the moment before the turn, when the split could still be recorded as an agony "
          "rather than resolved into a programme.",
  themes_text="The first subject is the divided self, and the poem's peculiar force comes from refusing to "
              "allegorise it: the speaker really is inside someone who hates him, and the description is "
              "literal before it is symbolic. The second is race as an inner partition, the experience of "
              "inhabiting a self that the surrounding society has designed. The third is the failure of "
              "love and art as exits: the poem turns towards a woman and towards the city and finds that "
              "neither offers a way out of the enclosure. The fourth is the anticipation of the turn "
              "Baraka would take - the sense that the agony is a stage to be passed through rather than a "
              "condition to be analysed.",
  structure="A single unbroken free-verse lyric of about forty short lines, without stanza divisions in "
            "the printed text, moving from the initial statement of enclosure through a middle passage "
            "of address to the 'someone' and closing on the body still occupied.",
  style="Short lines, hard enjambment and very little metaphor of the ornamental kind; a spoken, almost "
        "conversational register interrupted by sudden abstraction; repetition of the pronouns 'I' and "
        "'you' until the two become interchangeable; and a refusal of the cadence that would let the "
        "poem close on a consolation.",
  ctx="Written in the last years of Baraka's Greenwich Village period and published in The Dead Lecturer "
      "(Grove Press, 1964), the collection that marked his break with the Beats and with the white "
      "avant-garde. Richard Howard, reviewing the book in The Nation, called the poems 'the agonized "
      "poems of a man writing to save his skin'. Within two years of its publication Baraka had left "
      "the Village, founded the Black Arts Repertory Theatre/School in Harlem and written 'Black Art'.",
  sig="'An Agony. As Now.' is one of the two or three poems by which The Dead Lecturer is known and the "
      "standard anthology text for the transition in Baraka's work from Beat-adjacent experiment to "
      "Black Arts statement; it is taught as the poem that records the moment before the turn, and it "
      "opens the Norton selection of his poetry.",
  canon="Secondary canon",
  crit="Criticism reads the poem as the psychological hinge of Baraka's career, the point at which the "
       "Beat vocabulary of alienation is revealed to have a racial content; the poem's refusal of "
       "consolation has been discussed as a formal strategy rather than a failure of resolution, and it "
       "is regularly compared with 'Black Dada Nihilismus' from the same volume.",
  biblio="First published in The Dead Lecturer (New York: Grove Press, 1964), where it is the sixth poem; "
         "collected in Transbluesency: The Selected Poems of Amiri Baraka/LeRoi Jones 1961-1995 (1995). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The volume, publisher and year are from the library catalogue record of the first edition and "
        "its contents list; the poem's position in the volume is from that contents list. The date of "
        "composition is not established from the sources consulted, so the record gives the date of "
        "first book publication.",
  ver="partially verified", sources=[W_AB, W_AB_PF, W_DEAD, NAAL]),
W10("A Poem for Willie Best", AB, "1964", "Poem (free verse, extended)", "major",
  genres=G("Narrative Poetry", "Free Verse", "Political Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Art, the artist and the creative life",
           "Power, the state and surveillance"),
  movements=M(BEAT, BAM),
  overview="'A Poem for Willie Best' is the longest and most ambitious poem in The Dead Lecturer (Grove "
           "Press, 1964). Willie Best was a Black American actor who appeared in more than a hundred "
           "Hollywood films from the 1930s to the 1950s, usually as a servant or a comic sidekick, "
           "credited for years as 'Sleep 'n' Eat'; Baraka's poem takes the fact of that career - a man "
           "paid to perform a caricature of himself - and makes it the model of what American culture "
           "does to the Black artist. It is written in numbered sections of varying length and mixes "
           "narration, quotation, hallucination and direct address.",
  content="The poem opens with a scene of performance: a face singing alone, a man on a screen doing what "
          "he has been hired to do. Baraka describes Best's face, his voice and his routines, and the "
          "description keeps sliding from the actor to the audience and back, so that the reader is never "
          "sure whether the poem is about the man, the role or the people watching. The middle sections "
          "move into a hallucinatory landscape of American images - films, advertisements, lynchings, "
          "churches - in which Best's face recurs, and the poem's speaker begins to address him "
          "directly, asking what it cost to make the face that the country wanted. The last sections "
          "turn to the speaker's own position: the poet who has also been performing, who has also been "
          "paid, and who is now trying to write a poem that will not be a performance. The poem ends on "
          "an address to the reader - a demand to hear - rather than on an image.",
  summary="What makes 'A Poem for Willie Best' the central poem of The Dead Lecturer is that it refuses to "
          "let the reader stand outside the machine it describes. Best is not presented as a victim to be "
          "pitied but as a worker with a craft, and the poem's anger is directed less at him than at the "
          "economy that made his craft into a caricature and at the audience that paid for it. Baraka "
          "built the poem out of the materials of American mass culture - the film, the advertisement, "
          "the minstrel routine - and set them in a verse that is itself cinematic, cutting between "
          "close-up and panorama without transition. The numbered sections keep the poem from settling "
          "into a single argument, and the recurring face holds it together as a refrain. The poem's "
          "formal risk is its length: Baraka allows the hallucination to run on past the point where a "
          "shorter poem would have made its point, so that the reader experiences something of the "
          "exhaustion the poem is about. In the last movement the poem turns on its own speaker and asks "
          "whether this poem, too, is a performance - which is the question that the whole of Baraka's "
          "later work, from 'Black Art' to the Marxist poems, would try to answer, and which none of "
          "them would settle. That is why the poem still reads as a threshold rather than a "
          "conclusion.",
  themes_text="The first subject is the manufacture of the Black performer: the poem is a study of how a "
              "caricature is produced, cast, paid for and consumed, and it insists on the labour involved "
              "rather than the stereotype alone. The second is spectatorship - the audience's share in "
              "the arrangement - which is why the poem keeps turning to address the reader. The third is "
              "the artist's complicity: Baraka writes about Best while asking what he himself has done "
              "for a living, and the question gives the poem its moral pressure. The fourth is the "
              "American image-world of the 1950s and early 1960s, the films and advertisements through "
              "which a nation learned what a Black face was for. Baraka does not step outside that "
              "image-world to judge it; he works inside it, cutting from one piece of it to another, so "
              "that the poem reproduces the very condition it is complaining about.",
  structure="An extended poem in numbered sections, twenty pages in the first edition, moving between "
            "third-person description of Best, hallucinatory catalogue and direct address; the sections "
            "vary in length and are not organised by argument, and the poem's coherence is carried by "
            "the recurring face and by the speaker's voice.",
  style="Long unrhymed free-verse lines that sometimes run to prose; abrupt shifts of register between "
        "the demotic and the literary; a montage technique borrowed from film and from jazz; the "
        "repetition of a name or phrase as a refrain; and an ending that turns to the second person and "
        "raises its voice.",
  ctx="Published in The Dead Lecturer (Grove Press, 1964), the collection that marked Baraka's break with "
      "the Beats. Willie Best (1916-1962) had died two years before the book appeared, and his career - "
      "more than a hundred films, the degrading credit 'Sleep 'n' Eat', a late life of poverty and "
      "illness - was recent public knowledge. The poem belongs to the moment just before the Black Arts "
      "Movement, when Baraka was working out in verse the argument about the Black artist's relation to "
      "the American audience that he would make explicitly in 'The Myth of a Negro Literature' (1962) and "
      "in Home: Social Essays (1966).",
  sig="'A Poem for Willie Best' is the poem most often cited as the achievement of The Dead Lecturer and "
      "as the first full statement of the aesthetic that the Black Arts Movement would adopt; it is "
      "widely anthologised, it gave its title to a generation's argument about the Black performer, and "
      "criticism treats it as the bridge between Baraka's Beat years and his nationalist work.",
  canon="Major canon",
  crit="Critics have read the poem as a study of minstrelsy and its wage, as a precursor of the Black Arts "
       "aesthetic, and as an experiment in cinematic form; Adrienne Rich called The Dead Lecturer a "
       "book rather than an assemblage of occasional poems, and singled out its 'faultless phrasing', "
       "while later criticism has attended to the poem's ambivalence about its own spectatorship.",
  biblio="First published in The Dead Lecturer (New York: Grove Press, 1964); collected in Transbluesency "
         "(1995). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first edition's contents list gives the poem in the volume; the page extent described above "
        "is from the catalogue record of the Grove edition and was not checked against a copy. No "
        "printed bibliography of Baraka was consulted.",
  ver="partially verified", sources=[W_AB, W_AB_PF, W_DEAD, NAAL]),
W10("Black Art", AB, "1966", "Poem (free verse, incantatory)", "major",
  genres=G("Political Poetry", "Free Verse", "Black Arts Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Art, the artist and the creative life",
           "Violence, crime and justice"),
  movements=M(BAM),
  overview="'Black Art' was written in 1965, after the assassination of Malcolm X, and first published in "
           "The Liberator for January 1966, before being collected in Black Magic (Bobbs-Merrill, 1969). "
           "It is the manifesto poem of the Black Arts Movement: a demand that poems be useful, that "
           "they be weapons, that they stop describing the world and start changing it, delivered in a "
           "voice that alternates between incantation and threat. Its opening - 'Poems are bullshit "
           "unless they are / teeth or trees or lemons piled / on a step' - is among the most quoted "
           "openings in postwar American poetry.",
  content="The poem begins by clearing the ground: most poems are worthless, and the test of a poem is "
          "whether it is a thing in the world - teeth, a tree, lemons on a step - rather than a "
          "refinement of feeling. From there it moves into a catalogue of what a Black poem should do: "
          "it should be able to kill, it should assassinate, it should 'shoot guns' and 'make our own "
          "world'. Baraka names the enemies in the poem's own vocabulary - the 'negroleader', the "
          "'liberal', the 'jewlady', the 'owner-jews' - and the naming is deliberately offensive, part "
          "of the poem's argument that a poetry of politeness is a poetry of submission. The middle of "
          "the poem turns to sound: 'rrrrrrrrrrrr / tuhtuhtuhtuhtuhtuh', onomatopoeia that turns the "
          "poem into the noise of gunfire and of a voice refusing to be grammatical. It ends with a "
          "demand rather than an image: 'We want a black poem. And a / Black World.'",
  summary="'Black Art' is a poem that argues against poetry, and its force depends on the contradiction it "
          "cannot resolve. Baraka calls for a writing that would stop being writing - that would be "
          "action, a bullet, a tree - and he makes the call in an elaborately crafted poem whose rhythms "
          "are borrowed from jazz and from the sermon. The poem's obscenity and its anti-Semitic naming "
          "have been the centre of its reception: they are inseparable from its historical moment, when "
          "the language of Black nationalism was being forged in reaction to the murder of Malcolm X, "
          "and they have been the reason it is taught as a document as much as a poem. Baraka himself "
          "later repudiated the anti-Semitic strain as a 'reactionary thing' while continuing to defend "
          "the poem's central demand. Its formal achievement is the ending, which refuses the lyric "
          "turn: there is no image to hold, only a slogan that the poem has spent all its energy making "
          "feel like an inevitability. Read beside 'An Agony. As Now.' from two years earlier, it marks "
          "the distance Baraka travelled - from a self divided and unable to act to a voice that has "
          "decided that the poem is the act, and the shorter distance between that voice and the "
          "speaker of the Marxist poems of the 1970s, who would demand the same thing of a different "
          "politics.",
  themes_text="The first subject is the function of art: the poem is an ars poetica that defines the poem "
              "by what it can do rather than by what it says. The second is violence, both the violence "
              "the poem calls for and the violence it answers, which the poem refuses to separate. The "
              "third is naming as a political act - the poem's enemies are named in the language of the "
              "street rather than analysed, and the naming is itself the argument. The fourth is the "
              "Black world the poem wants, which exists in the poem only as a demand, and which the "
              "poem's rhythm makes momentarily present. The poem is therefore a document of the moment in "
              "which American poetry was asked to choose between craft and use, and it answers by "
              "refusing to see the two as alternatives.",
  structure="A single free-verse poem of about seventy lines, without stanza divisions in the printed "
            "text, built as a series of escalating imperatives and catalogues, with an onomatopoeic "
            "passage at the centre and a two-line demand at the end.",
  style="Incantatory repetition, hard consonants and a rhythm driven by stress rather than metre; "
        "obscenity and racial epithets used as instruments; onomatopoeia and non-semantic sound; a "
        "vocabulary drawn from street speech, jazz and the slogan; and an absence of simile, so that "
        "the poem's images are asserted as facts.",
  ctx="Written in 1965 after the assassination of Malcolm X and first published in The Liberator for "
      "January 1966. The poem had already circulated in 1965 as a recorded performance on the drummer "
      "Sunny Murray's album Sonny's Time Now, with Albert Ayler, Don Cherry, Lewis Worrell and Henry "
      "Grimes, which is why its rhythms sound like the free jazz of the period. Between 1968 and 1973 it "
      "was reprinted in more than fifteen anthologies, and it became the founding text of the Black Arts "
      "Movement's poetics alongside Larry Neal's essay 'The Black Arts Movement' (1968).",
  sig="'Black Art' is the manifesto poem of the Black Arts Movement and one of the most consequential "
      "American poems of the 1960s: its opening lines are among the most quoted in postwar poetry, its "
      "recorded performance is an early instance of the poem as an audio work, and its demand for a "
      "usable art set the terms of the argument about Black aesthetics for a decade.",
  canon="Major canon",
  crit="Criticism treats the poem as the ars poetica of the Black Arts Movement and as the clearest "
       "instance of its refusal of the Western lyric; the anti-Semitic passages have been the subject of "
       "a substantial literature, including Baraka's own later repudiation, and the poem's relation to "
       "the jazz of Albert Ayler and Sunny Murray has been studied as a model of cross-media influence. "
       "William J. Harris and Houston Baker read it as the point at which Baraka's modernism becomes a "
       "political programme.",
  biblio="First published in The Liberator, January 1966; collected in Black Magic: Sabotage; Target "
         "Study; Black Art (Bobbs-Merrill, 1969) and in Transbluesency (1995). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The Liberator printing of January 1966 and the 1965 recording on Sonny's Time Now are recorded "
        "from the sources read, which agree on both; the poem's page extent in Black Magic is not "
        "established from the sources consulted.",
  ver="partially verified", sources=[W_AB, W_AB_PF, W_BLACKART, W_BLACKMAGIC, NAAL]),
W10("Will They Cry When You're Gone, You Bet", AB, "1969", "Poem (free verse, elegiac)", "significant",
  genres=G("Elegiac Poetry", "Free Verse", "Political Poetry"),
  themes=T("Death, illness and mourning", "Race, racism and the struggle for civil rights",
           "Migration, exile and diaspora"),
  movements=M(BAM),
  overview="'Will They Cry When You're Gone, You Bet' is a poem of the Black nationalist period, collected "
           "in Black Magic: Sabotage; Target Study; Black Art (Indianapolis: Bobbs-Merrill, 1969), the "
           "volume that gathered the poems Baraka wrote between 1961 and 1967. It is an elegy for the "
           "dead of the movement and a rebuke to those who survived them, built on a desert landscape in "
           "which the speaker's friends lie unburied while the living drift away from them.",
  content="The poem opens with the dead: 'You leave dead friends in a desert.' The speaker addresses "
          "those who have walked away from the bodies, describing them as deserted by the living and by "
          "themselves, 'leaving themselves, in the foot paths of madmen and saints'. The desert is the "
          "poem's central landscape - dry, white, without water - and the people in it are dying of "
          "thirst while 'white women serenade them in mystic deviousness', figures of the culture that "
          "has distracted them from the struggle. The poem's argument is that the dead are better off "
          "than the living who have abandoned them, and that an oasis, even a bitter one, is better than "
          "'white drifting fairies, muses, singing to us, in calm tones, about how it is better to die'. "
          "The poem ends by refusing the consolation of art: the muses' song is exactly what the speaker "
          "will not accept.",
  summary="The poem is Baraka's elegy for the movement's dead, written in the voice of a survivor who has "
          "decided that mourning is not enough. Its images are taken from Exodus and from the desert "
          "narratives of American preaching - a people in flight, a wilderness, an oasis that recedes - "
          "and Baraka turns that inheritance against the liberal culture that, in his account, offers "
          "Black Americans a beautiful death instead of a liveable life. The 'white drifting fairies, "
          "muses' are the poem's most revealing figure: they are the aesthetic tradition itself, singing "
          "in calm tones about transcendence, and the poem's refusal of them is a refusal of the whole "
          "idea of a poetry that consoles. The ending is deliberately unresolved - the speaker is still "
          "in the desert, the friends are still dead, and the only thing the poem has established is "
          "that it will not lie about either fact. It is one of the clearest statements in Black Magic of "
          "the position Baraka had reached: that the elegy, like every other form, had to be rebuilt for "
          "the use of the living.",
  themes_text="The first subject is mourning under political pressure - the dead of the movement, and the "
              "question of what the survivors owe them. The second is desertion, both the literal "
              "abandonment of the bodies and the cultural abandonment of the struggle by those who took "
              "up the consolations of art. The third is the desert as a figure for America, a place of "
              "white heat and no water, which the poem sets against the oasis it refuses to promise. The "
              "fourth is the refusal of the muse, which makes the poem an argument about what poetry is "
              "for, conducted inside an elegy.",
  structure="A single free-verse poem, in one movement, of about sixty lines, built as an address to the "
            "survivors that keeps returning to the image of the desert and closes on the refusal of the "
            "muses' song.",
  style="Long, unpunctuated free-verse lines close to the cadence of a sermon; direct address in the "
        "second person plural; a landscape described in flat declaratives; and a vocabulary that mixes "
        "the biblical ('oasis', 'muses', 'saints') with the colloquial ('you bet', 'etcetera').",
  ctx="Collected in Black Magic: Sabotage; Target Study; Black Art (Bobbs-Merrill, 1969), which gathered "
      "the poems of 1961-1967 and which Baraka published at the height of his Black nationalist period, "
      "the year of Black Fire (edited with Larry Neal) and of the founding of the Congress of Afrikan "
      "People. The poem's dead are those of the movement's first years - the poem is contemporaneous with "
      "the elegies for Malcolm X and with the Newark rebellion of 1967.",
  sig="'Will They Cry When You're Gone, You Bet' is one of the poems by which the Black Magic volume is "
      "known and has been anthologised in the Norton Anthology of American Literature since the 1990s, "
      "where it stands beside 'An Agony. As Now.' and 'A Poem for Willie Best' as the third face of "
      "Baraka's poetry: the elegiac, public voice of the nationalist years.",
  canon="Secondary canon",
  crit="Criticism reads the poem as the elegiac counterpart to 'Black Art' - the same programme, in the "
       "mode of mourning rather than demand - and discusses its use of the Exodus narrative and its "
       "refusal of the pastoral consolation that the Western elegy traditionally offers; it is also read "
       "as evidence of how quickly Baraka's poetry absorbed the deaths of the mid-1960s into a political "
       "form.",
  biblio="Collected in Black Magic: Sabotage; Target Study; Black Art (Indianapolis: Bobbs-Merrill, 1969); "
         "reprinted in Transbluesency (1995). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The first printing of the poem in a periodical was not established from the sources consulted; "
        "the record therefore gives the date of first book collection, 1969, and does not claim an "
        "earlier magazine appearance. The volume and publisher are from the catalogue record of Black "
        "Magic.",
  ver="partially verified", sources=[W_AB, W_AB_PF, W_BLACKMAGIC, NAAL]),
W10("Headwaters", NSM, "1969", "Poem (free verse, lyric)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Nature Poetry"),
  themes=T("Land, place and regional belonging", "Myth, folklore and the supernatural",
           "Memory, trauma and testimony"),
  movements=M(NAR),
  overview="'Headwaters' is the framing poem of The Way to Rainy Mountain (Albuquerque: University of New "
           "Mexico Press, 1969), Momaday's account of the Kiowa migration from the headwaters of the "
           "Yellowstone to the Wichita Mountains. It stands at the front of the book, before the "
           "historical introduction and the twenty-four three-part episodes, and sets the terms on which "
           "everything after it is read: a people, a migration, a landscape and the act of remembering.",
  content="The poem opens on the high country where the Kiowas began, 'the headwaters of the Yellowstone', "
          "and follows them east and south as they come down out of the mountains into the plains, "
          "acquiring horses, the sun dance and the Tai-me, and becoming a Plains people. Its images are "
          "of descent and arrival: the meadow, the river, the buffalo, the sacred doll. In the closing "
          "movement the poem turns from the migration to the present, and to the speaker's own relation "
          "to the journey - the story is now his to carry - and the poem ends on a note of continuance "
          "rather than loss, with the landscape still holding what the people left in it.",
  summary="'Headwaters' does the work of a preface in verse: it establishes the geography, the timeframe "
          "and the tone of the book that follows, and it does so without explaining anything. Momaday "
          "writes the migration as a movement through a landscape whose names are Kiowa, so that the "
          "reader learns the country and the history at the same time. The poem's syntax is unhurried and "
          "its images are held rather than developed, which is the technique Momaday takes from oral "
          "narrative: a thing is named, allowed to stand, and then the poem moves on. The turn at the end "
          "- from the ancestors to the speaker - makes the poem a genealogy rather than a travelogue, and "
          "it is that turn that licenses the rest of The Way to Rainy Mountain, in which Momaday "
          "interleaves Kiowa legend, historical commentary and his own memoir. The poem is short, and "
          "its shortness is part of its argument: the origin of a people can be told in a page, if the "
          "page is right.",
  themes_text="The first subject is origin and migration - the journey from the headwaters to the plains, "
              "which is both a historical event and the founding story of the Kiowa as a people. The "
              "second is the land as the carrier of memory, since the poem's geography is the argument "
              "that the Kiowas' history is locatable. The third is inheritance: the speaker receives the "
              "story and becomes its teller, which makes the poem a statement about what a poet does with "
              "a tribal past. The fourth is the sacred - the Tai-me and the sun dance - present in the "
              "poem without being explained, which is Momaday's way of writing a religious culture "
              "without translating it for outsiders.",
  structure="A short free-verse poem of about twenty-five lines in four movements: the high country, the "
            "descent into the plains, the acquisition of the Kiowa way of life, and the turn to the "
            "speaker's present.",
  style="Spare free verse with long, balanced sentences and very few adjectives; proper names used "
        "without gloss; a rhythm close to spoken narration; and an ending that resolves on a statement "
        "of continuance rather than an image.",
  ctx="Published as the opening poem of The Way to Rainy Mountain (University of New Mexico Press, 1969), "
      "illustrated by the author's father, the Kiowa painter Al Momaday, and written after Momaday had "
      "retraced his ancestors' route from Montana to Oklahoma. The book appeared in the year House Made "
      "of Dawn won the Pulitzer Prize, and the two together are the founding documents of the Native "
      "American Renaissance.",
  sig="'Headwaters' is the poem that opens one of the central books of Native American literature and is "
      "the standard anthology selection from Momaday's poetry; it appears in the Norton Anthology with "
      "the prose selections from the same book, and it is taught as a model of how a poem can carry a "
      "people's history.",
  canon="Secondary canon",
  crit="Criticism reads the poem as the frame that makes The Way to Rainy Mountain legible, and as an "
       "instance of Momaday's 'land ethic' - the proposition that a people's identity is inseparable from "
       "the country it moved through; it is usually discussed together with the 'Rainy Mountain Cemetery' "
       "poem that closes the book, and with the book's three-voice structure.",
  biblio="First published in The Way to Rainy Mountain (Albuquerque: University of New Mexico Press, "
         "1969), where it opens the volume; reprinted in In the Presence of the Sun: Stories and Poems "
         "1961-1991 (1992). A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The bibliographic details are from the record of the University of New Mexico Press edition and "
        "from the scholarship on the book, which describes 'Headwaters' as the framing poem that follows "
        "the preface and precedes the introduction. The poem was not read in a printed copy for this "
        "record.",
  ver="partially verified", sources=[W_NSM, W_RAINY, NAAL]),
W10("The Way to Rainy Mountain", NSM, "1969", "Prose memoir with poems (three-voice narrative)", "major",
  genres=G("Nonfiction Prose (1946–2000)", "Memoir", "Mythological Retelling"),
  themes=T("Land, place and regional belonging", "Myth, folklore and the supernatural",
           "Memory, trauma and testimony"),
  movements=M(NAR),
  overview="The Way to Rainy Mountain was published by the University of New Mexico Press in 1969, "
           "illustrated with eleven drawings by the author's father, the Kiowa painter Al Momaday. It "
           "retraces the Kiowa migration from the headwaters of the Yellowstone to the Wichita Mountains "
           "of Oklahoma and ends at Rainy Mountain, where Momaday's grandmother Aho lived and is buried. "
           "The book is built in three voices on facing pages: a Kiowa legend, a passage of historical "
           "commentary, and a fragment of Momaday's own memory, each set in a different typeface.",
  content="The book opens with a preface and an introduction, framed by two poems, 'Headwaters' and "
          "'Rainy Mountain Cemetery', and then divides into three sections - 'The Setting Out', 'The "
          "Going On' and 'The Closing In' - each containing eight episodes. Every episode is a triptych: "
          "on the left-hand page a Kiowa myth or story, in the words of the oral tradition; on the "
          "right, a paragraph of historical and anthropological commentary on the same subject; and below "
          "it, in italic, a passage of Momaday's own recollection, usually of his childhood at Jemez or "
          "of his grandmother. The episodes trace the migration, the acquisition of the horse and the "
          "sun dance, the Tai-me, the wars with the United States, the surrender at Fort Sill in 1875 and "
          "the settlement near Rainy Mountain. The book closes with the grandmother's death and with the "
          "poem 'Rainy Mountain Cemetery', and with Momaday's account of returning to the mountain.",
  summary="The Way to Rainy Mountain is the book in which Momaday solved the formal problem that Native "
          "American writing faced in the 1960s: how to write the history of an oral people without "
          "turning their stories into anthropology or into memoir. His answer is the three-voice page, "
          "which refuses to subordinate legend to commentary or commentary to memory, and which makes the "
          "reader hold all three at once. The effect is cumulative rather than narrative: no single "
          "episode explains the migration, but the sequence of them, each with its myth and its fact and "
          "its remembered detail, builds a history that is neither the anthropologist's nor the "
          "novelist's. The grandmother, Aho, is the book's centre - a woman born in the shadow of the "
          "Kiowas' last free years, who told Momaday the stories, and whose death at Rainy Mountain gives "
          "the book its destination. The prose is spare and deliberate, with a cadence that Momaday took "
          "from Kiowa speech as he had heard it, and the book's most quoted passage, about looking upon "
          "the landscape in the early morning 'with the sun at your back', is the clearest statement of "
          "its method: the land is not scenery but an instrument of knowledge. It is one of the small "
          "number of American books of the period that changed what a book of nonfiction prose could be, "
          "and it has been in print continuously since 1969.",
  themes_text="The first subject is the migration itself, as event and as the shaping story of a people. "
              "The second is the relation of oral tradition to written history: the book puts the two "
              "side by side, in different typefaces, and refuses to arbitrate between them. The third is "
              "the grandmother and the family - Aho, the Tai-me keeper's descendant, and Momaday's own "
              "childhood among the Kiowa and Jemez - through whom the abstract history becomes personal. "
              "The fourth is dispossession and survival: the surrender at Fort Sill, the confinement to "
              "the reservation near Rainy Mountain, and the continuity of the stories afterwards. The "
              "fifth is the landscape as a site of knowledge, an idea the book states in its most famous "
              "passage and enacts on every page.",
  structure="A preface, an introduction, two framing poems and three sections of eight episodes each; "
            "every episode is a triptych of legend, commentary and memoir printed in three typefaces on "
            "the page, and the book's argument is carried by the arrangement rather than by a continuous "
            "narrative.",
  style="Restrained, cadenced prose with long periodic sentences and a deliberately archaic formality in "
        "the legendary passages; the commentary in a plainer documentary register; the memoir passages in "
        "a quieter first person; and an overall design - typeface, illustration, page layout - that is part "
        "of the book's meaning.",
  ctx="Written after Momaday retraced the Kiowa migration from Montana to Oklahoma in the mid-1960s, and "
      "based on an earlier privately printed booklet, The Journey of Tai-me (1967). It was published by "
      "the University of New Mexico Press in 1969, the year House Made of Dawn won the Pulitzer Prize, "
      "and it is one of the two or three books that opened the Native American Renaissance. Its "
      "three-voice form has been widely imitated and is taught as a model of cross-genre writing.",
  sig="The Way to Rainy Mountain is the central work of Native American nonfiction prose and one of the "
      "most influential American books of the period: it has never been out of print, it is a standard "
      "text in courses on American autobiography, the essay and Native American literature, and its "
      "three-voice form changed the way American writers could put oral tradition on the page.",
  canon="Major canon",
  crit="Criticism has read the book as the founding example of 'tribal autobiography', as a critique of "
       "anthropological appropriation, and as a formal experiment in the juxtaposition of oral and "
       "written history; the typeface and layout have been discussed as constitutive of its meaning "
       "rather than decorative, and the book's relation to The Journey of Tai-me (1967) has been studied "
       "as an instance of a writer revising his own materials.",
  biblio="First published in Albuquerque by the University of New Mexico Press in 1969, with drawings by "
         "Al Momaday; based on The Journey of Tai-me (1967); reissued in a twenty-fifth anniversary "
         "edition in 1994 and in later editions. A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E, which prints the introduction and the episodes IV, XIII, "
         "XVII, XXIV and the epilogue.",
  notes="The book's structure, illustrations and publisher are recorded from the bibliographic and "
        "scholarly sources read, not from a copy of the first edition. The Norton selection is an "
        "excerpt, recorded here as one work with its parts named in the bibliography statement.",
  ver="partially verified", sources=[W_NSM, W_RAINY, NAAL]),
W10("The Summer Day", MO, "1990", "Poem (free verse, lyric)", "major",
  genres=G("Lyric Poetry", "Free Verse", "Nature Poetry"),
  themes=T("Nature, ecology and environmental crisis", "Faith, doubt and the sacred",
           "Death, illness and mourning"),
  movements=M(),
  overview="'The Summer Day' was first published in House of Light (Boston: Beacon Press, 1990) and is the "
           "most quoted American poem of the last thirty years. It begins with a question about who made "
           "the world, passes through the observation of a grasshopper, and ends with a question "
           "addressed to the reader about what they intend to do with their life. It is a poem of "
           "attention that turns, in its last line, into a demand.",
  content="The poem opens with four questions: 'Who made the world? / Who made the swan, and the black "
          "bear? / Who made the grasshopper?' The speaker then describes the grasshopper - this one, in "
          "the grass, not the species - eating sugar out of her hand, moving her jaws back and forth "
          "'instead of up and down', and looking around 'with her enormous and complicated eyes'. The "
          "poem then widens: the speaker says she does not know exactly what a prayer is, but she knows "
          "how to pay attention, how to fall down into the grass, how to be idle and blessed, and how to "
          "walk through the fields, which is what she has been doing all day. The last lines turn to the "
          "reader: 'Tell me, what else should I have done? / Doesn't everything die at last, and too "
          "soon? / Tell me, what is it you plan to do / with your one wild and precious life?'",
  summary="'The Summer Day' is a poem about attention, and it earns its famous ending by refusing to "
          "hurry towards it. The first half is almost entirely questions and observation: the grasshopper "
          "is described with a naturalist's precision - the jaws, the eyes, the sugar - and the speaker "
          "does not interpret it. The turn comes with the word 'prayer', which the poem introduces "
          "tentatively, as something the speaker cannot define but can enact through attention. From "
          "there the poem moves outward into the fields, into idleness, into the idea of being 'blessed', "
          "and the movement is deliberately undramatic: nothing happens except that the speaker spends a "
          "day looking. The ending's power comes from the shift of address. For thirteen lines the poem "
          "has been spoken to no one, and in the last four it turns on the reader and asks a question "
          "that the rest of the poem has been quietly making possible - if attention is all we have, what "
          "are you doing with your life? The poem's simplicity is its risk and its achievement: Oliver's "
          "critics have called it prose with line breaks, and her readers have taken it as a credo, which "
          "is a fate few poems of the period have had. The question is unanswerable inside the poem, and "
          "the poem knows it: it offers no model of a good life, only the demand that the reader notice "
          "the one they are already living.",
  themes_text="The first subject is attention as a form of prayer, stated explicitly in the poem's middle "
              "lines and enacted in its first half. The second is the particularity of the natural world: "
              "the grasshopper is not a symbol but a creature with jaws and eyes, and the poem's "
              "insistence on that is what keeps it from being a greeting card. The third is mortality, "
              "raised in the penultimate question and left to stand. The fourth is the reader, who is "
              "addressed directly at the end and made responsible for the poem's question, which is why "
              "the poem is so often quoted out of context as an injunction.",
  structure="A single free-verse lyric of nineteen lines in one stanza, unrhymed, moving from question to "
            "observation to reflection to a closing address, with no section breaks and an ending that "
            "turns from the first person to the second, so that the poem's last movement is also its only "
            "moment of direct speech.",
  style="Short free-verse lines with heavy enjambment; almost no metaphor, and where figures appear they "
        "are homely ('fall down into the grass'); a conversational register carried by rhetorical "
        "questions; and a closing quatrain of direct address that is deliberately plain.",
  ctx="Published in House of Light (Beacon Press, 1990), the collection that won the Christopher Award and "
      "the L. L. Winship/PEN New England Award, and reprinted in New and Selected Poems (1992). By 1990 "
      "Oliver was the best-selling poet in the United States, and 'The Summer Day' became - through "
      "readings, quotations and its use in commencement addresses and in the 'grasshopper' name by which "
      "many readers know it - the most widely circulated American poem of its period.",
  sig="'The Summer Day' is the most quoted American poem of the last three decades and the one most often "
      "used to introduce readers to poetry; its closing question is part of the common American "
      "vocabulary, and it is a set text in schools and in courses on nature writing. Its critical "
      "reception is a case study in the relation between a poet's popular readership and the academy.",
  canon="Major canon",
  crit="Critics divide over the poem: some read it as a genuine devotional lyric in the tradition of "
       "Whitman and Hopkins, others as a sentimental simplification of that tradition, and the argument "
       "has become a standard topic in discussions of American poetry's public. Its formal plainness has "
       "been defended as a deliberate poetics of attention and attacked as prose arranged on the page; "
       "feminist and ecocritical readings have emphasised the poem's refusal of mastery over the natural "
       "world it describes.",
  biblio="First published in House of Light (Boston: Beacon Press, 1990); reprinted in New and Selected "
         "Poems (1992) and The Truro Bear and Other Adventures (2008). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The first printing in House of Light is recorded from the publisher's own note on the poem and "
        "from the Poetry Foundation's page; no earlier periodical appearance was established, and the "
        "record therefore dates the poem 1990.",
  ver="partially verified", sources=[W_MO, W_HOL, NAAL]),
W10("miss rosie", LC, "1969", "Poem (free verse, portrait)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Social Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Death, illness and mourning",
           "The city, the suburb and modern space"),
  movements=M(AAW),
  overview="'miss rosie' was published in Lucille Clifton's first collection, Good Times (New York: Random "
           "House, 1969). It is a portrait of an old woman the speaker has known since childhood, seen "
           "now sitting with her bag among the garbage cans of an American city, and it is the poem that "
           "established the voice - lower case, unpunctuated, plain, unsparing and tender at once - that "
           "Clifton would use for the rest of her life.",
  content="The poem addresses miss rosie directly and describes her: a woman who was once 'the best "
          "looking gal in town', now wrapped in an old coat, sitting 'through your destruction' with her "
          "bag beside her. The speaker says she has watched miss rosie for years - 'I have watched you / "
          "through your destruction / I have stood on the corner and watched you' - and then makes the "
          "declaration on which the poem turns: 'through your destruction / i stand up'. The poem ends "
          "with the speaker asserting that she is the same as miss rosie, or that she stands in the same "
          "place, and that the old woman's survival is her own.",
  summary="'miss rosie' is a poem of twenty short lines that does the work of a short story, and its "
          "economy is the point: Clifton gives the woman's whole history in a phrase - 'the best looking "
          "gal in town' - and her present in three details: the coat, the bag, the corner. The poem's "
          "grammar is doing something careful. The speaker 'watches' miss rosie, which is the position of "
          "a spectator, and then refuses that position by standing up; the final lines collapse the "
          "distance between the two women, so that the poem becomes an act of identification rather than "
          "of observation. That movement - from seeing to standing with - is the ethical core of "
          "Clifton's early work, and it is why the poem is taught as an example of a portrait that "
          "refuses to sentimentalise the person it honours. The lower-case spelling and the absence of "
          "punctuation, which Clifton adopted from the start, give the poem the sound of a voice speaking "
          "rather than a text being read, and the line breaks fall where a breath would.",
  themes_text="The first subject is the destruction that poverty and age work on a person, recorded "
              "without euphemism. The second is the gaze: the poem is about who is looked at and who is "
              "looking, and its ethical turn is the speaker's refusal to remain a spectator. The third is "
              "the city - the corner, the garbage cans, the bag - as the place where such lives are "
              "lived and seen. The fourth is solidarity, stated in the last line as a fact of the "
              "speaker's own standing, which is also the poem's tacit claim about what a poem can do.",
  structure="One short free-verse poem of about twenty lines, unpunctuated and in lower case, addressed in "
            "the second person to miss rosie and closing with a first-person declaration.",
  style="Lower case throughout, no punctuation, line breaks at the breath; a plain vocabulary with a few "
        "startling phrases ('through your destruction'); repetition of the word 'watched' as a refrain; "
        "and an ending that is a short declarative sentence.",
  ctx="Published in Good Times (Random House, 1969), Clifton's first collection, which The New York Times "
      "named one of the ten best books of the year. The book appeared at the end of the decade in which "
      "the civil rights movement had turned to the urban North, and its portraits of Buffalo and of "
      "people like miss rosie belong to that moment. It is the earliest poem in the Norton selection of "
      "Clifton's work.",
  sig="'miss rosie' is one of the two or three poems by which Clifton is best known and the standard "
      "introduction to her work; it is anthologised throughout American school and university "
      "literature, and it established the portrait poem of urban Black life that she would return to "
      "for forty years.",
  canon="Secondary canon",
  crit="Critics read the poem as a study in the ethics of the gaze and as an early instance of Clifton's "
       "identification with the marginalised figures of her childhood; it is usually discussed with "
       "'the lost baby poem' and 'homage to my hips' as the three faces of her early work - witness, "
       "grief and celebration.",
  biblio="First published in Good Times (New York: Random House, 1969); collected in Good Woman: Poems and "
         "a Memoir 1969-1980 (1987) and The Collected Poems of Lucille Clifton 1965-2010 (2012). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The 1969 first publication in Good Times is recorded from the EBSCO and Poetry for Students "
        "accounts and from the collection's contents; the poem was not read in a copy of the first "
        "edition.",
  ver="partially verified", sources=[W_LC, W_LC_EBSCO, W_GOODTIMES, NAAL]),
W10("the lost baby poem", LC, "1972", "Poem (free verse, elegy)", "major",
  genres=G("Elegiac Poetry", "Free Verse", "Confessional Poetry"),
  themes=T("Death, illness and mourning", "Family, marriage and domestic life",
           "Faith, doubt and the sacred"),
  movements=M(AAW, SWF),
  overview="'the lost baby poem' was published in Good News About the Earth (New York: Random House, 1972), "
           "Clifton's second collection. It is an elegy for a pregnancy that was ended, spoken by a woman "
           "who is also the mother of living children, and it moves through guilt, address and a final "
           "blessing without ever settling into a single attitude towards what happened.",
  content="The poem begins with the 'almost body' that was lost and with the speaker's account of the "
          "circumstances: the winter, the poverty, the other children who needed what there was. She "
          "addresses the lost child directly and imagines it in the water - the sewage, the sea, the ice "
          "- and the imagery moves from pollution to baptism as the poem proceeds. In the middle the "
          "speaker makes a promise: if she had let the child be born, she says, she would have done "
          "certain things, or would not have; the grammar of the promise is deliberately tangled, since "
          "the child was not born and the promise can only be conditional. The poem ends by committing "
          "the child to the care of something larger than the speaker - the rivers, the sea, the natural "
          "world that the poem has been moving towards - and by asking forgiveness, or granting it.",
  summary="'the lost baby poem' is the most discussed of Clifton's early poems because it refuses every "
          "position its subject offers. It is not a poem of simple grief, because the speaker explains "
          "the decision and does not repent it; it is not a poem of justification, because the guilt is "
          "present in every line; and it is not a religious poem in any settled sense, although it ends "
          "by committing the child to the rivers and the sea in a gesture that borrows the language of "
          "baptism. Clifton's technique here is the one she would use for forty years: short unpunctuated "
          "lines, a plain vocabulary, a repeated word or phrase to hold the poem together, and an ending "
          "that is a single flat sentence carrying an enormous weight. The water imagery, which the "
          "EBSCO reading traces from sewage through ice to the rivers of the last stanza, is the poem's "
          "structural device: the child moves through it from pollution to consecration, and the reader "
          "is carried along by the imagery rather than argued into a judgement. It is a poem about "
          "poverty as much as about loss - the decision is presented as an economic one - and that is why "
          "it has been central to the feminist and Black feminist reading of Clifton's work. The poem "
          "has also been read as an elegy that refuses the elegy's consolations, since its committal "
          "of the child to the rivers is a letting-go rather than a promise of reunion, and that "
          "refusal is what keeps it from being a poem about forgiveness.",
  themes_text="The first subject is abortion, treated without either the pro-life or the pro-choice "
              "vocabulary of the period: the poem's terms are the winter, the money, the other children, "
              "and the decision is a fact to be mourned rather than a position to be defended. The second "
              "is poverty as a condition of motherhood, which the poem states plainly and without "
              "indignation. The third is the religious imagination - the water, the blessing, the "
              "committal - which the poem uses without adopting a doctrine. The fourth is address: the "
              "poem speaks to the child, which makes it an elegy that cannot be sure it has the right to "
              "mourn, and that uncertainty is its emotional engine.",
  structure="A free-verse elegy in three stanzas, unpunctuated and in lower case, addressed to the lost "
            "child, moving from the circumstances of the loss through a conditional promise to a final "
            "committal; the lines are short enough that the poem reads as a single held breath, and the "
            "three stanzas mark the only structural division Clifton allows.",
  style="Short unpunctuated lines in lower case; a plain and often monosyllabic vocabulary; repetition of "
        "the water imagery through the three stanzas; and an ending that resolves into a single "
        "declarative sentence.",
  ctx="Published in Good News About the Earth (Random House, 1972), the collection that followed Good "
      "Times and that also contains Clifton's poems on the Kent State shootings and her sequence on "
      "Biblical figures. The poem belongs to the early 1970s, when Black feminist writing was beginning "
      "to make the conditions of Black motherhood a public literary subject, and it has become a "
      "standard text in that discussion.",
  sig="'the lost baby poem' is among the most anthologised and most discussed American poems of the "
      "period on abortion and motherhood; it is a set text in courses on American poetry, on Black "
      "women's writing and on feminist literature, and it is usually taken as the poem in which "
      "Clifton's characteristic voice fully arrives.",
  canon="Major canon",
  crit="Feminist and Black feminist criticism has read the poem as a refusal of the sentimental "
       "motherhood of the era and as an insistence on the material conditions of reproductive choice; "
       "formal criticism has attended to its unpunctuated syntax and to the water imagery that carries "
       "the poem from pollution to blessing, and the poem's relation to the elegy has been widely "
       "discussed.",
  biblio="First published in Good News About the Earth (New York: Random House, 1972); collected in Good "
         "Woman (1987) and The Collected Poems (2012). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The 1972 first publication is recorded from the EBSCO Research Starters entry, which gives the "
        "collection and the year, and from the University of Arizona's Voca catalogue citation of the "
        "Random House edition; the poem was not read in a copy of the first edition.",
  ver="partially verified", sources=[W_LC, W_LC_EBSCO, W_GOODTIMES, NAAL]),
W10("homage to my hips", LC, "1980", "Poem (free verse, lyric)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Social Poetry"),
  themes=T("Gender, feminism and women's lives", "Race, racism and the struggle for civil rights",
           "Identity, authenticity and the divided self"),
  movements=M(SWF, AAW),
  overview="'homage to my hips' was published in Two-Headed Woman (Amherst: University of Massachusetts "
           "Press, 1980), which won the Juniper Prize. It is a short poem of celebration in which the "
           "speaker's hips are described as big, free, mighty and magic, and it is among the most "
           "anthologised American poems of the period - a body poem that is also a poem about Black "
           "women's refusal of the shapes the culture has prescribed for them.",
  content="The poem begins 'these hips are big hips' and proceeds by a series of assertions: they need "
          "space, they do not fit into 'little pretty places', they are free, they have never been "
          "enslaved, they go where they want to go. In the second movement the speaker says she has known "
          "them to 'put a spell on a man and / spin him like a top', and the poem ends with the hips "
          "declared mighty and magic. The vocabulary is deliberately simple and the repetition of 'hips' "
          "at the end of each line gives the poem the structure of a chant.",
  summary="'homage to my hips' works by taking a part of the body that the culture has made into an object "
          "of shame or fetish and making it the subject of a declaration. The poem is funny, and the "
          "humour is part of its politics: 'they don't fit into little pretty places' is a joke about "
          "small chairs and a statement about a whole aesthetic. Clifton's formal decision is to keep the "
          "poem short and the lines almost identical in length, so that the repetition accumulates force "
          "rather than variety. The word 'enslaved' in the middle of the poem is the hinge: it moves the "
          "poem from body pride to history, and it claims for the speaker's body a lineage of resistance "
          "rather than of victimhood. The ending's 'magic' is not a retreat into fantasy but a claim on "
          "the power the poem has spent its lines establishing, and it is why the poem reads as a "
          "blessing rather than a boast.",
  themes_text="The first subject is the female body as a site of both social discipline and self-"
              "possession. The second is race: the poem's speaker is a Black woman, the body described "
              "is the one the culture has caricatured, and the word 'enslaved' makes the connection "
              "explicit. The third is speech itself - the lower case, the repetition, the chant - which "
              "the poem uses to make a claim that would sound merely assertive in a different register. "
              "The fourth is joy, which the poem treats as a political achievement rather than a private "
              "mood.",
  structure="A single short free-verse poem of about twenty lines, unpunctuated and in lower case, built "
            "as a series of parallel assertions with 'hips' recurring as a refrain, and closing on a "
            "two-line declaration.",
  style="Lower case, no punctuation, very short lines; a plain vocabulary and a syntax close to speech; "
        "anaphora and refrain; and a tone that moves between comedy and celebration without breaking.",
  ctx="Published in Two-Headed Woman (Amherst: University of Massachusetts Press, 1980), which won the "
      "Juniper Prize and which is divided into three sequences, 'homage to mine', 'two-headed woman' and "
      "'the light that came to lucille clifton'. The poem belongs to the flourishing of Black feminist "
      "writing at the end of the 1970s, alongside the work of Audre Lorde and Toni Cade Bambara, and it "
      "has become one of the most quoted American poems on the body.",
  sig="'homage to my hips' is the most widely circulated of Clifton's poems after 'miss rosie' and the one "
      "most often taught as an example of Black feminist body poetics; it is anthologised in school and "
      "university texts and in collections of American poetry, and it has become a fixture of readings "
      "and of the public performance of her work.",
  canon="Secondary canon",
  crit="Criticism reads the poem as a Black feminist reclamation of the body and as an instance of "
       "Clifton's use of the chant and the refrain; it is frequently discussed alongside Lorde's 'Uses of "
       "the Erotic' and with the body poems of the 1970s, and its humour has been read as a deliberate "
       "strategy for making a political claim without adopting a political register.",
  biblio="First published in Two-Headed Woman (Amherst: University of Massachusetts Press, 1980); "
         "collected in Good Woman (1987), Blessing the Boats (2000) and The Collected Poems (2012). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The collection, publisher and prize are recorded from the catalogue and reference records read; "
        "the poem's place in the volume's first sequence is from the collection's contents as recorded by "
        "those sources.",
  ver="partially verified", sources=[W_LC, W_GOODTIMES, W_QUILT, NAAL]),
W10("wishes for sons", LC, "1991", "Poem (free verse, curse-blessing)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Social Poetry"),
  themes=T("Gender, feminism and women's lives", "Family, marriage and domestic life",
           "Death, illness and mourning"),
  movements=M(SWF),
  overview="'wishes for sons' was published in Quilting: Poems 1987-1990 (Brockport, New York: BOA "
           "Editions, 1991). It is a poem of comic revenge in which a mother wishes on her sons the "
           "physical indignities of menstruation and menopause, so that they might know what women's "
           "bodies endure, and it is one of the most quoted poems in Clifton's later work.",
  content="The poem begins 'i wish them cramps' and proceeds through a list of wishes: a strange town, the "
          "last tampon, no 7-11, one week early in a white skirt, one week late. The second movement "
          "moves forward in time to menopause - hot flashes, clots 'like you wouldn't believe' - and asks "
          "that the flashes come when they meet someone special and the clots when they want to. The "
          "poem ends with the wish that they be brought to 'gynecologists / not unlike themselves', which "
          "is the poem's joke and its judgement: the sons will meet the medical profession as women meet "
          "it, and will be understood by men who resemble them.",
  summary="'wishes for sons' is a curse poem, and its comedy is exact. Clifton takes the register of the "
          "maternal blessing - the thing a mother is supposed to give a son - and fills it with the "
          "physiological facts that sons are not supposed to know about their mothers and sisters. The "
          "list structure is the poem's engine: each wish is a small, specific humiliation, and the "
          "accumulation of them turns the poem from a joke into an argument about whose experience counts "
          "as real. The final turn to the gynecologists is the sharpest move in the poem, because it "
          "shifts the target from the sons' ignorance to the institutions that share it. Clifton's line "
          "here is almost entirely without metaphor - the poem is a list of things that happen to "
          "bodies - and the flatness is what makes the last line land. It is a poem that has been read as "
          "merely funny and as a precise piece of feminist argument, and it is both.",
  themes_text="The first subject is the asymmetry of bodily knowledge between men and women, stated as a "
              "list of things sons do not know. The second is the maternal voice turned against its own "
              "convention: the blessing becomes a curse that is also a lesson. The third is the medical "
              "profession, which the last line makes the poem's real addressee. The fourth is time, since "
              "the poem moves from menstruation to menopause and asks the sons to age as women age, which "
              "is the poem's most serious wish.",
  structure="A single free-verse poem of about twenty lines, unpunctuated and in lower case, built as a "
            "list of wishes in two movements - the menstrual and the menopausal - and closing on a "
            "single line about the gynecologists.",
  style="Lower case, no punctuation, very short lines; a plain and bodily vocabulary ('cramps', 'tampon', "
        "'clots', 'hot flashes'); a list structure carried by anaphora ('i wish them'); and a tone that "
        "is comic on the surface and entirely serious underneath.",
  ctx="Published in Quilting: Poems 1987-1990 (BOA Editions, 1991), the volume in which Clifton arranged "
      "her poems of the late 1980s in four sequences named after quilt patterns. The poem belongs to the "
      "period of her widest recognition as a feminist poet, after the death of her husband in 1984 and "
      "alongside The Book of Light (1993).",
  sig="'wishes for sons' is one of the most widely quoted poems in Clifton's later work and a standard "
      "anthology piece in courses on American poetry and on women's writing; its closing line is among "
      "the most cited in her work, and it is regularly read as a compact statement of the feminist "
      "argument about embodied knowledge.",
  canon="Secondary canon",
  crit="Feminist criticism reads the poem as a comic inversion of the maternal blessing and as an "
       "argument about the epistemology of the body; it is usually discussed with 'to my last period' and "
       "'poem to my uterus' as Clifton's sequence on the female body across a lifetime, and its humour "
       "has been analysed as a mode of political statement.",
  biblio="First published in Quilting: Poems 1987-1990 (Brockport, NY: BOA Editions, 1991); collected in "
         "Blessing the Boats (2000) and The Collected Poems (2012). A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E.",
  notes="The first publication in Quilting is recorded from the contents lists of the volume and of the "
        "collected poems; the poem was not read in a copy of the first edition.",
  ver="partially verified", sources=[W_LC, W_QUILT, NAAL]),
W10("blessing the boats", LC, "1991", "Poem (free verse, blessing)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Religious Poetry"),
  themes=T("Faith, doubt and the sacred", "Love, intimacy and loss", "Death, illness and mourning"),
  movements=M(SWF),
  overview="'blessing the boats' was published in Quilting: Poems 1987-1990 (BOA Editions, 1991), where it "
           "gives its name to the last of the volume's four sequences, and it later became the title poem "
           "of Blessing the Boats: New and Selected Poems 1988-2000 (2000), which won the National Book "
           "Award. It is a poem of farewell and safe passage, addressed to someone setting out on water, "
           "and it is one of the most quoted American blessings of the period.",
  content="The poem consists of a series of wishes for a voyage: 'may the tide / that is entering even now "
          "/ the lip of our understanding / carry you out / beyond the face of fear'; may you kiss the "
          "wind and turn from it, certain that it will love your back; may you open your eyes to water, "
          "'water waving forever'; and may you, 'in your innocence', sail through 'this to that'. The "
          "address is to a 'you' who is departing, and the poem never specifies whether the voyage is a "
          "journey, a death or a life; the ambiguity is deliberate and is what makes the poem usable at "
          "weddings, funerals and readings of every kind.",
  summary="'blessing the boats' is a poem built entirely of subjunctive wishes, and its power comes from "
          "the fact that it asks for almost nothing except safe passage. Clifton's images are drawn from "
          "the sea - the tide, the wind, the water - and they are handled without ornament: the tide "
          "'entering the lip of our understanding' is the poem's one elaborate figure, and after it the "
          "wishes become plainer and shorter, as though the poem were learning to speak. The word "
          "'innocence' near the end is the most surprising in the poem, since Clifton's work is rarely "
          "innocent about anything; here it names the condition of the person setting out, who does not "
          "know what the water holds. The final phrase, 'sail through this to that', is the poem's "
          "achievement: it declines to name either shore, so that the blessing can be said over any "
          "crossing, and it does so in four monosyllables. It is a religious poem without a doctrine and "
          "a love poem without a beloved, and that is why it has become one of the most used poems in "
          "American public life.",
  themes_text="The first subject is passage - the crossing from one condition to another, left "
              "unspecified so that it can be a journey, a life or a death. The second is fear, which the "
              "poem names once and then moves past, since the blessing is designed to carry the traveller "
              "out beyond 'the face of fear'. The third is innocence as a condition of setting out, which "
              "the poem values without admiring. The fourth is the water itself, which Clifton uses as "
              "her standing figure for what cannot be controlled and what can nonetheless be blessed.",
  structure="A single free-verse poem of about eighteen very short lines, unpunctuated and in lower case, "
            "built as a sequence of 'may' clauses addressed to a departing 'you', and closing on a "
            "four-word phrase.",
  style="Extremely short lines and minimal punctuation; a vocabulary of sea and weather used plainly; "
        "anaphora on 'may'; and an ending that reduces to monosyllables.",
  ctx="Published in Quilting: Poems 1987-1990 (BOA Editions, 1991) and used as the title poem of Blessing "
      "the Boats: New and Selected Poems 1988-2000 (2000), which won the National Book Award in 2000. "
      "The poem was read at Clifton's public appearances throughout the last decade of her life and has "
      "become a standard text at memorial services, which is a fate the poem's own refusal to specify "
      "its crossing made possible.",
  sig="'blessing the boats' is the poem that gave its title to the collection that won Clifton the "
      "National Book Award, and it is one of the most widely used American poems of the period at public "
      "occasions; it is a standard anthology selection and the poem most often chosen to represent "
      "Clifton's late manner.",
  canon="Secondary canon",
  crit="Criticism reads the poem as a secular blessing and as an instance of Clifton's late style, in "
       "which the short line and the subjunctive carry the whole weight; it is discussed with the poems "
       "of The Book of Light and The Terrible Stories as the mature form of the religious imagination "
       "that runs through her work from Good News About the Earth onwards.",
  biblio="First published in Quilting: Poems 1987-1990 (Brockport, NY: BOA Editions, 1991); the title poem "
         "of Blessing the Boats: New and Selected Poems 1988-2000 (Rochester, NY: BOA Editions, 2000). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The first publication in Quilting is recorded from the volume's contents lists; the National "
        "Book Award for Blessing the Boats is from the award records. The poem was not read in a copy of "
        "the first edition.",
  ver="partially verified", sources=[W_LC, W_QUILT, NAAL]),
W10("to my last period", LC, "1991", "Poem (free verse, address)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Confessional Poetry"),
  themes=T("Gender, feminism and women's lives", "Death, illness and mourning",
           "Family, marriage and domestic life"),
  movements=M(SWF),
  overview="'to my last period' was published in Quilting: Poems 1987-1990 (BOA Editions, 1991). It "
           "addresses the speaker's final menstrual period as 'girl', a companion of thirty-eight years "
           "who is now leaving, and it turns the end of fertility into a poem of friendship, irritation "
           "and farewell.",
  content="The poem opens 'well, girl, goodbye, / after thirty-eight years', and establishes at once the "
          "intimacy of the address: the period is a girl, an old companion, someone the speaker has "
          "lived with for nearly four decades. The speaker recalls that she 'never arrived / splendid in "
          "your red dress / without trouble for me / somewhere, somehow', which is both a complaint and "
          "an affectionate one. The poem then turns to the present and to what the ending means, and it "
          "refuses both the cultural narrative of loss and the counter-narrative of liberation. It ends "
          "with a goodbye that is neither relieved nor grieving, and the evenness of tone is the poem's "
          "achievement.",
  summary="'to my last period' is a poem about an ending that the culture has no good language for, and "
          "Clifton's solution is to treat the ending as a relationship. The address to 'girl' does the "
          "work: it makes the period a person with a long history, and it lets the speaker be ambivalent "
          "without being either ungrateful or sentimental. The 'red dress' is the poem's one flourish, and "
          "it is a good one, since it turns the menstrual blood into a garment and the arrival into a "
          "social occasion. What follows is deliberately flat - 'without trouble for me / somewhere, "
          "somehow' - and the flatness is the point, since the poem is refusing the lyric intensities "
          "that the subject invites. The ending's even tone is the hardest thing in the poem to achieve, "
          "and it is what makes the poem usable: it gives a reader a way of saying goodbye to a bodily "
          "era without having to choose between mourning and relief. It is one of the poems that has made "
          "Clifton central to the feminist writing of the body in the 1980s and 1990s.",
  themes_text="The first subject is the end of fertility, treated as a relationship ending rather than as "
              "a loss of function. The second is time, counted in the poem's 'thirty-eight years' and "
              "felt in the difference between the opening 'goodbye' and the poem's even tone. The third is "
              "the body's ordinary trouble, which the poem records without dramatising. The fourth is "
              "the refusal of the available narratives - the medical, the nostalgic and the liberatory - "
              "which the poem acknowledges and declines.",
  structure="A short free-verse poem of about fourteen lines, unpunctuated and in lower case, addressed in "
            "the second person to the period and framed as a goodbye.",
  style="Lower case, minimal punctuation, very short lines; a conversational register with one striking "
        "image ('splendid in your red dress'); and an ending that refuses emphasis.",
  ctx="Published in Quilting: Poems 1987-1990 (BOA Editions, 1991); Clifton was in her early fifties when "
      "the poems of the volume were written, and the collection's sequences move through the body, "
      "family and history. The poem belongs with 'wishes for sons' and 'poem to my uterus' to a group of "
      "poems on menstruation and menopause that were unusual in American poetry of the period for their "
      "frankness and their lack of either shame or triumph.",
  sig="'to my last period' is one of the most quoted poems in Clifton's later work and a standard "
      "anthology selection on the body and ageing; it is regularly cited as an example of how her plain "
      "style can carry a subject that American poetry had largely avoided.",
  canon="Secondary canon",
  crit="Feminist criticism reads the poem as a reclamation of menopause from the medical and cultural "
       "narratives that frame it as decline; formal criticism attends to the address and to the "
       "deliberate flatness of the ending, and the poem is usually discussed with 'wishes for sons' as "
       "the comic and the elegiac faces of the same subject.",
  biblio="First published in Quilting: Poems 1987-1990 (Brockport, NY: BOA Editions, 1991); collected in "
         "Blessing the Boats (2000) and The Collected Poems (2012). A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E.",
  notes="The first publication in Quilting is recorded from the contents lists of the volume; the poem "
        "was not read in a copy of the first edition.",
  ver="partially verified", sources=[W_LC, W_QUILT, NAAL]),
W10("wild blessings", LC, "1991", "Poem (free verse, lyric)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Nature Poetry"),
  themes=T("Faith, doubt and the sacred", "Nature, ecology and environmental crisis",
           "Memory, trauma and testimony"),
  movements=M(SWF),
  overview="'wild blessings' was published in Quilting: Poems 1987-1990 (BOA Editions, 1991), in the "
           "volume's first sequence. It is a short poem of thanks for the ungovernable parts of a life - "
           "the wild, the unasked-for, the things that arrive without being sent for - and it is one of "
           "the clearest statements of the religious imagination that runs through Clifton's later work.",
  content="The poem gives thanks for what has not been planned: for the 'wild' blessings that come "
          "unbidden, for the parts of a life that were not arranged by the self. Its images are of "
          "weather, growth and animals, and its grammar is that of the blessing or the grace before a "
          "meal - a list of what is being thanked for, offered without explanation. The poem closes by "
          "accepting the wildness rather than trying to bring it under control, and the acceptance is the "
          "poem's argument.",
  summary="'wild blessings' is a poem of gratitude that refuses to be pious. Clifton's subject is the "
          "difference between the life one plans and the life one gets, and her formal choice is to make "
          "the poem a list rather than an argument, so that the reader receives the blessings in the same "
          "unordered way the speaker did. The word 'wild' is doing a lot of work: it names what is not "
          "domesticated, not chosen and not controlled, and it associates the sacred with the "
          "unmanageable rather than with the orderly. That association is characteristic of Clifton's "
          "late work, in which God is more often found in the ungovernable than in the institution. The "
          "poem's shortness is part of its meaning: a blessing is not an essay, and Clifton's decision to "
          "let the poem be as brief as a grace note is what keeps it from becoming a sermon. It is a "
          "useful companion to 'blessing the boats', which makes the same move with a voyage rather than "
          "a life.",
  themes_text="The first subject is gratitude for what was not asked for, which the poem treats as the "
              "shape of a real life. The second is the sacred, located in the wild rather than the "
              "institutional. The third is the refusal of control - the poem does not ask for the wild "
              "things to be tamed, and its acceptance is its ethics. The fourth is memory, since the "
              "blessings are recollected rather than anticipated, which gives the poem its backward look.",
  structure="A short free-verse poem, unpunctuated and in lower case, built as a list of thanks with a "
            "closing acceptance; about a dozen lines.",
  style="Lower case, minimal punctuation, short lines; a plain vocabulary with a few words of weather and "
        "growth; and an incantatory repetition of the gesture of thanks.",
  ctx="Published in Quilting: Poems 1987-1990 (BOA Editions, 1991), whose four sequences are named after "
      "quilt patterns and which gathers Clifton's poems of the late 1980s, a period that followed the "
      "death of her husband and in which her work turned increasingly towards blessing and elegy.",
  sig="'wild blessings' is one of the poems by which the late manner of Clifton's work is known, and it "
      "is anthologised as an example of her religious writing; it is less widely quoted than 'blessing "
      "the boats' but belongs to the same group, and it is used in courses on American poetry and on "
      "spirituality in literature.",
  canon="Secondary canon",
  crit="Criticism reads the poem as an instance of Clifton's theology of the ungovernable, and discusses "
       "it with the blessings and thanksgivings of Blessing the Boats and Mercy; the poem's brevity has "
       "been read as a formal expression of the grace-note rather than as a limitation.",
  biblio="First published in Quilting: Poems 1987-1990 (Brockport, NY: BOA Editions, 1991); collected in "
         "Blessing the Boats (2000) and The Collected Poems (2012). A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E.",
  notes="The volume attribution and sequence are from the contents lists of Quilting and of the collected "
        "poems; the poem was not read in a copy of the first edition for this record.",
  ver="partially verified", sources=[W_LC, W_QUILT, NAAL]),
W10("Poetry Is Not a Luxury", "Audre Lorde", "1977", "Essay (prose)", "significant",
  genres=G("Literary Essay", "Political Essay", "Feminist Criticism"),
  themes=T("Gender, feminism and women's lives", "Language, writing and the limits of representation",
           "Race, racism and the struggle for civil rights"),
  movements=M(SWF, AAW),
  overview="'Poetry Is Not a Luxury' was first published in Chrysalis: A Magazine of Women's Culture in "
           "1977 and collected in Sister Outsider: Essays and Speeches (Trumansburg, New York: The "
           "Crossing Press, 1984). It is Lorde's statement of a poetics: poetry, she argues, is not an "
           "ornament added to political struggle but the means by which women - and Black women in "
           "particular - discover what they know, and therefore the precondition of any action they "
           "might take.",
  content="The essay begins from the distinction between poetry as 'the way we help give name to the "
          "nameless so it can be thought' and the 'luxury' of the title, which is a word Lorde takes from "
          "the culture's own condescension towards art and turns against it. She argues that for women "
          "the poem is not a refinement but a necessity, because the feelings that precede thought have "
          "to be given form before they can become ideas, and because the language available to women "
          "has been made by others. The middle of the essay turns on the 'Black mother' and on the "
          "daughters who must learn to hear their own knowledge, and it insists on the difference "
          "between the 'yes' that is a genuine assent and the 'yes' that is compliance. It closes with "
          "the claim that poetry lays 'the foundations for a future of change' and that it is the task of "
          "women to make it.",
  summary="'Poetry Is Not a Luxury' is a short essay that does the work of a manifesto, and its argument "
          "is more exact than its title suggests. Lorde is not claiming that poetry is pleasant or "
          "useful; she is claiming that it is epistemological - that the poem is the instrument by which "
          "a feeling is converted into a thought, and that without that conversion the thought cannot be "
          "acted on. The essay's political force comes from its insistence that this is especially true "
          "for Black women, whose knowledge has been systematically refused a form. The 'Black mother' "
          "passage, which is also a passage about her own mother, gives the argument its ground: the "
          "daughters have to learn to recognise their own feeling as knowledge, and the poems that do "
          "that are not luxuries but the first acts of a politics. The essay's rhetoric is deliberately "
          "plain and its sentences are short, and its closing claim - that poetry 'is not a luxury' but "
          "'a vital necessity of our existence' - has become one of the most quoted sentences in "
          "twentieth-century feminist criticism.",
  themes_text="The first subject is poetry as a mode of knowledge rather than a decoration, which the "
              "essay argues by locating thought in feeling. The second is the refusal of the language "
              "women have been given, and the work of naming what has been 'nameless'. The third is "
              "race and gender together: the essay's argument is made for women in general and for Black "
              "women in particular, and it refuses to separate the two. The fourth is the future, which "
              "the essay treats as something the poem makes possible rather than merely imagines.",
  structure="A short prose essay of about fifteen hundred words in five or six unnumbered sections, moving "
            "from the definition of poetry, through the argument about feeling and thought, to the Black "
            "mother passage, to a closing statement about change.",
  style="Short declarative sentences with occasional incantatory repetition; a first-person plural that "
        "includes the reader; a vocabulary drawn from both the poetic and the political; and a closing "
        "that raises the register without becoming rhetorical.",
  ctx="First published in Chrysalis: A Magazine of Women's Culture in 1977 and collected in Sister "
      "Outsider (1984). It belongs to the flourishing of Black feminist theory at the end of the 1970s "
      "and is a companion piece to 'Uses of the Erotic: The Erotic as Power' (1978), delivered as a "
      "paper at the Fourth Berkshire Conference on the History of Women in 1978 and published the same "
      "year.",
  sig="'Poetry Is Not a Luxury' is one of the founding texts of Black feminist criticism and among the "
      "most cited essays in twentieth-century American letters; it is a set text in courses on feminist "
      "theory, on poetics and on African American literature, and its title has become a common phrase "
      "in discussions of art and politics.",
  canon="Secondary canon",
  crit="Criticism treats the essay as a foundational statement of Black feminist poetics, and reads its "
       "argument about feeling and thought alongside Lorde's 'Uses of the Erotic' and the essays of "
       "Sister Outsider; it has been central to the theorisation of what is now called 'poethics' and to "
       "discussions of the relation between aesthetics and political practice.",
  biblio="First published in Chrysalis: A Magazine of Women's Culture, no. 1 (1977); collected in Sister "
         "Outsider: Essays and Speeches (Trumansburg, NY: The Crossing Press, 1984). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The Chrysalis first printing of 1977 and the collection in Sister Outsider (1984) are recorded "
        "from the sources read; the number of the Chrysalis issue was not established from those sources.",
  ver="partially verified", sources=["Audre Lorde (Wikipedia)", "Sister Outsider (The Crossing Press, 1984), contents and publication records", NAAL]),
W10("Footnote to Howl", "Allen Ginsberg", "1956", "Poem (free verse, litany)", "major",
  genres=G("Beat Poetry", "Free Verse", "Religious Poetry"),
  themes=T("Faith, doubt and the sacred", "Counterculture, drugs and rebellion",
           "Sexuality, desire and the closet"),
  movements=M(BEAT),
  overview="'Footnote to Howl' closes Howl and Other Poems (San Francisco: City Lights Books, 1956), the "
           "collection that made Ginsberg the central poet of the Beat Generation and that was the "
           "subject of the 1957 obscenity trial in San Francisco. It is a litany of the word 'holy' - "
           "fifteen lines of it, applied to everything the culture had declared unholy - and it is the "
           "poem in which Ginsberg's prophetic voice is fully established.",
  content="Every line of the poem begins with the word 'Holy', and the list runs through body parts, "
          "people, places and conditions: holy the groin, holy the bum, holy the cock and the cunt, holy "
          "the grandmother, holy the screaming infants, holy the indifference of the sidewalks, holy the "
          "grinning meat-eaters, holy the solitary apparitions, holy the sea, holy the desert, holy the "
          "tongues and the cock and the cunt and the bum and the wombs and the sperm and the "
          "spirit. The litany is spoken in the voice of the angel in the first section of Howl, and its "
          "function is to declare that everything exists, including the despised and the obscene, and "
          "that the whole of it is holy. The poem ends with a fourfold refrain: 'Holy holy holy holy / "
          "Holy holy holy holy / Holy holy holy holy / Holy holy holy holy'.",
  summary="'Footnote to Howl' is a poem of pure assertion, and its form is the oldest one available: the "
          "litany. Ginsberg takes the word that the religious tradition reserves for the sacred and "
          "applies it to the body, and the repetition is the argument - by the time the reader reaches "
          "the fourth 'holy the', the distinction between the sacred and the obscene has been destroyed "
          "by accumulation rather than by reasoning. The poem's openness to everything is its politics: "
          "in 1956, when the book was published by City Lights and seized by the customs, a list that "
          "includes 'holy the cock and holy the cunt' alongside 'holy the grandmother' was an act of "
          "defiance. The final fourfold refrain is a formal decision - the litany is not closed with a "
          "statement but with a repetition, so that the poem does not so much end as stop, which keeps "
          "its assertion from becoming a conclusion. Read as the last part of Howl, it answers the "
          "despair of the poem's opening: if all is holy, then 'Moloch' is included too, and the "
          "prophetic denunciation becomes a universal affirmation. The litany has been imitated ever "
          "since, by poets and by preachers, and it is the source of the poem's continuing life in "
          "performance: it is almost impossible to read aloud without beginning to chant.",
  themes_text="The first subject is holiness - what it is, who confers it and on what - and the poem's "
              "answer is everything and everyone, without exception. The second is the body, named "
              "explicitly and without euphemism, in a period when that was a legal risk. The third is "
              "the Beat generation's counter-theology, which takes the vocabulary of the Catholic "
              "upbringing Ginsberg had left and uses it against the institution. The fourth is "
              "affirmation as a political act: the poem's 'yes' to everything is a refusal of the "
              "American moral order that had made the poem's own subjects criminal.",
  structure="A single litany of fifteen long lines in free verse, unrhymed, every line beginning with "
            "'Holy', followed by a four-line coda of 'Holy holy holy holy'.",
  style="Long free-verse lines with extensive parallelism and anaphora; capitalization used "
        "emphatically; a vocabulary that mixes the liturgical with the obscene; and an incantatory "
        "repetition designed for oral delivery, since Ginsberg composed the poem for the reading room "
        "rather than the page and its effect depends on the accumulation of the word in the ear.",
  ctx="Published as the closing poem of Howl and Other Poems (City Lights Books, 1956), in a first run of "
      "four thousand copies and in the 'Pocket Poets' series; copies were seized by the US Customs "
      "Service in 1957 and the publisher Lawrence Ferlinghetti was tried for obscenity in San Francisco, "
      "and the acquittal that followed became a landmark in post-war American free expression. The poem "
      "was written in Berkeley in the summer of 1955, in the burst of composition that also produced "
      "'Howl' and 'A Supermarket in California'.",
  sig="'Footnote to Howl' is the poem that completes the most famous poem of the Beat Generation and one "
      "of the most reprinted American poems of the period; its litany of 'holy' is part of the common "
      "vocabulary of post-war American poetry, and it is a standard anthology text for the Beats and for "
      "the literature of the 1950s.",
  canon="Major canon",
  crit="Critics read the poem as the theological counterpart to 'Howl', as a Blakean affirmation in the "
       "tradition of the prophetic books Ginsberg had been reading, and as an instance of the oral, "
       "performance-based poetics of the Beats; its place in the obscenity trial and in the "
       "liberalisation of American publishing law is part of its critical history.",
  biblio="First published in Howl and Other Poems (San Francisco: City Lights Books, 1956); collected in "
         "Collected Poems 1947-1980 (1984). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The 1956 City Lights first edition and the poem's position as the closing poem of the book are "
        "recorded from the records of the collection and its history; the exact date of composition is "
        "given as the summer of 1955 in the accounts consulted.",
  ver="partially verified", sources=["Allen Ginsberg (Wikipedia)", "Howl and Other Poems (City Lights Books, 1956), publication and trial records", NAAL]),
W10("A Supermarket in California", "Allen Ginsberg", "1956", "Poem (free verse, elegy)", "significant",
  genres=G("Beat Poetry", "Free Verse", "Elegiac Poetry"),
  themes=T("Art, the artist and the creative life", "The city, the suburb and modern space",
           "Sexuality, desire and the closet"),
  movements=M(BEAT),
  overview="'A Supermarket in California' is one of the shorter poems in Howl and Other Poems (City "
           "Lights, 1956), and it is the most personal of the collection's poems about poetry. It "
           "describes the poet walking at night in a supermarket in California, thinking of Walt "
           "Whitman, and finding him - or imagining him - among the shoppers and the fruit.",
  content="The speaker walks 'down the sidestreets under the trees with a headache self-conscious "
          "looking at the full moon' and enters a 'neon fruit supermarket' in 'my hungry fatigues'. He "
          "wonders where Whitman is, and the poem imagines him: 'I saw you, Walt Whitman, childless, "
          "lonely old grubber, poking among the meats in the refrigerator and eyeing the grocery boys.' "
          "The two poets wander the aisles together; Whitman asks about the prices and the family, and "
          "the speaker asks him where the lost America has gone. The poem turns at the end to García "
          "Lorca, another poet of desire, and closes with the image of the two of them on the road, "
          "the speaker following Whitman's 'abandoned' road.",
  summary="'A Supermarket in California' is an elegy for a poet and for a country, written in the middle "
          "of the consumer abundance of the 1950s. Ginsberg's method is to make Whitman a physical "
          "presence in the poem - 'childless, lonely old grubber, poking among the meats' - and to let "
          "the reader feel the pathos of the great American poet reduced to a shopper, which is also "
          "Ginsberg's joke about what America has done with its own tradition. The poem's question, "
          "'Where are we going, Walt Whitman?', is asked in a supermarket, and the answer is that the "
          "doors of the supermarket close at dusk and the poets walk out into the night. Ginsberg's "
          "Whitman is openly a poet of same-sex desire - the 'grocery boys' are eyed as the poem's "
          "speaker eyes them - and the poem's act of inheritance is therefore also an act of outing the "
          "tradition, which is the political move the poem makes under its elegiac surface. The closing "
          "image of the road, and of García Lorca, extends the lineage beyond the national tradition and "
          "makes the poem's company a set of poets who were all, in different ways, outsiders.",
  themes_text="The first subject is poetic inheritance - what a young poet can take from a dead one, and "
              "what the dead one's America has become. The second is the supermarket as the emblem of a "
              "consumer society that has replaced the world Whitman wrote about. The third is same-sex "
              "desire, present in the poem's looking and in the company it keeps. The fourth is "
              "loneliness, which the poem's ending states without consolation: the poets walk out into "
              "the night and the poem cannot say where they are going.",
  structure="A single free-verse poem of about twenty-five lines in one stanza, moving from the street to "
            "the supermarket to the imagined conversation and out into the night.",
  style="Long free-verse lines with colloquial diction and occasional formal address; direct apostrophe "
        "to Whitman; a mixture of the specific and the visionary ('neon fruit supermarket', 'the doors "
        "close at dusk'); and an ending on an image rather than a statement.",
  ctx="Written in Berkeley in 1955 and published in Howl and Other Poems (City Lights, 1956). The poem "
      "belongs to the moment when Ginsberg, having left New York and his earlier formal apprenticeship, "
      "was writing the poems that made him famous; its address to Whitman places the Beats in a national "
      "lineage that the poem simultaneously claims and mourns.",
  sig="'A Supermarket in California' is one of the best-known poems of the Beat Generation and a standard "
      "anthology text for the period; it is taught as Ginsberg's statement about poetic tradition and as "
      "an example of the Beat use of the long line and the direct address.",
  canon="Secondary canon",
  crit="Criticism reads the poem as Ginsberg's negotiation with the American poetic tradition, and "
       "discusses the supermarket as a figure for a consumer capitalism that had absorbed the America "
       "Whitman wrote; the poem's treatment of Whitman's sexuality has been central to gay and lesbian "
       "readings of the period and of Ginsberg's work.",
  biblio="First published in Howl and Other Poems (San Francisco: City Lights Books, 1956); collected in "
         "Collected Poems 1947-1980 (1984). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The 1956 City Lights first edition is recorded from the records of the collection; the poem's "
        "composition date of 1955 is from the accounts of the period, and the exact date was not "
        "established from the sources consulted.",
  ver="partially verified", sources=["Allen Ginsberg (Wikipedia)", "Howl and Other Poems (City Lights Books, 1956), publication and trial records", NAAL]),
]
