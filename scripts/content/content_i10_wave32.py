"""Installment 10, wave 32: the seven selections wave 31 brought into the period.

Four authors, seven works. Two of the authors (Simon Armitage, Juan Felipe
Herrera) are new; two (Stevie Smith, Louise Bennett) already have records and
gain a work each or three.

Why they are here at all: all seven rows carried "date to verify" until wave 31,
and five of them were nearly lost. A first pass dated Herrera's poems from Half of
the World in Light (2008), a new-and-selected volume, and dropped them; "Exiles"
opens Exiles of Desire (1983) and "Literary Asylums" is placed in the same book by
the 2008 volume's own contents. Bennett's "Jamaica Language" was mis-dated to
Jamaica Labrish (1966) by the same pass; it is a radio monologue first printed in
Aunty Roachy Seh (1993). All seven are inside 1946-2000 on the corrected dates.

First printings used here:

    Stevie Smith, "Pretty"              Scorpion and Other Poems (Longman, 1972), posthumous
    Louise Bennett, "Dry-Foot Bwoy"     Jamaica Labrish (Sangster's, 1966), pp. 275-6
    Louise Bennett, "Jamaica Oman"      Jamaica Labrish (1966)
    Louise Bennett, "Jamaica Language"  Aunty Roachy Seh (Sangster's, 1993), p. 1
    Simon Armitage, "The Tyre"          Cloudcuckooland (Faber and Faber, 1997)
    J. F. Herrera, "Exiles"             Exiles of Desire (Lalo Press, 1983)
    J. F. Herrera, "Literary Asylums"   Exiles of Desire (1983)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, SEC, MIN, NAEL, NAAL  # noqa: E402

SMITH = "Stevie Smith"
LB = "Louise Bennett"
SA = "Simon Armitage"
JFH = "Juan Felipe Herrera"

CAR = "Caribbean Literature in English"
POSTCOL = "Postcolonial Literature"
CHIC = "Chicano Movement Literature"
BPR = "The British Poetry Revival"
SWF = "Second-Wave Feminist Writing"

W_SMITH = "Stevie Smith (Wikipedia)"
W_SCORPION = "Scorpion and Other Poems"
W_LB = "Louise Bennett-Coverley (Wikipedia)"
W_LABRISH = "Jamaica Labrish"
W_ROACHY = "Aunty Roachy Seh"
MORRIS_NLJ = "Miss Lou Matters (Mervyn Morris, National Library of Jamaica lecture, 2016)"
W_SA = "Simon Armitage"
W_CCL = "Cloudcuckooland"
MAGFIELD = "Magnetic Field: The Marsden Poems, context and critical discussion"
POETRYFOUND = "The Shout Heard across the Atlantic (Poetry Foundation profile of Simon Armitage)"
W_JFH = "Juan Felipe Herrera"
W_EOD = "Exiles of Desire"
W_HWL = "Half of the World in Light: New and Selected Poems"
W_NORTON_AUDIO = "The Norton Anthology of American Literature, 11th edition, vol. E: publisher's audio and contents pages"

AUTHORS = [
A10(SA, SEC, "1963", None, "Huddersfield, West Riding of Yorkshire, England",
  "English; poet, playwright, novelist and translator writing in English",
  "English poet of the West Yorkshire Pennines whose plain, wry, often violent narratives in "
  "contemporary speech made him the most widely read British poet of his generation, and the "
  "Poet Laureate since 2019",
  "Simon Robert Armitage was born in Huddersfield on 26 May 1963 and grew up in the village of "
  "Marsden, on the edge of the Pennines, where his family still lived and where most of his poems "
  "are set; his father wrote pantomimes for a local all-male troupe. He read geography at "
  "Portsmouth Polytechnic and took a master's degree in social work at the University of "
  "Manchester, and worked for several years as a probation officer, an experience that later "
  "underpins poems such as 'Remains' and the television work he did with soldiers. Zoom! (Bloodaxe, "
  "1989) was his first collection; Kid (1992) won the Forward Prize for Best First Collection's "
  "successor, Book of Matches (1993) and The Dead Sea Poems (1995) established him, and "
  "Cloudcuckooland (1997) was shortlisted for the Whitbread Prize. The millennium poem Killing "
  "Time, broadcast and printed in 1999, made him a public figure, and the sequence of prose poems "
  "in Seeing Stars (2010) and the translations of Sir Gawain and the Green Knight (2007), the "
  "Alliterative Morte Arthure (2012) and Pearl (2016) extended his range. He was Professor of "
  "Poetry at Oxford from 2015 to 2019, has been Professor of Poetry at Leeds since 2017, and was "
  "appointed Poet Laureate on 10 May 2019; he was awarded the CBE in 2010 and the Queen's Gold "
  "Medal for Poetry in 2018. His prose includes All Points North (1998), the Pennine Way account "
  "Walking Home (2012) and its sequel Walking Away, and the novels Little Green Man (2001) and "
  "The White Stuff (2004).",
  "Collections: Zoom! (1989), Kid (1992), Book of Matches (1993), The Dead Sea Poems (1995), "
  "Cloudcuckooland (1997), Killing Time (1999), Selected Poems (2001), The Universal Home Doctor "
  "(2002), Travelling Songs (2002), The Shout: Selected Poems (2005), Tyrannosaurus Rex Versus "
  "the Corduroy Kid (2006), Seeing Stars (2010), The Death of King Arthur (2012), Paper Aeroplane: "
  "Selected Poems 1989-2014 (2014), The Unaccompanied (2017), Sandettie Light Vessel Automatic "
  "(2019), Magnetic Field: The Marsden Poems (2020) and Blossomise (2024). Translations: Sir "
  "Gawain and the Green Knight (2007), The Alliterative Morte Arthure (2012), Pearl (2016), The "
  "Odyssey (2016). Prose: All Points North (1998), Walking Home (2012), Walking Away (2015). "
  "Novels: Little Green Man (2001), The White Stuff (2004).",
  "A conversational, usually first-person line that sounds like speech but is metrically exact; "
  "short sentences; a Yorkshire vocabulary kept without ornament; sudden shifts of register from "
  "the demotic to the literary; narrative poems that withhold their moral; and endings that turn "
  "on a plain statement or a single image rather than a summary.",
  "Adolescence and the remembered places of a northern childhood; class, work and the probation "
  "service; the borderland between town and moor; violence, often casual and domestic; the body "
  "and its failures; the First World War and its commemorations; and, in the later work, the "
  "environment and the public poem.",
  "Armitage is the most widely taught British poet of his generation and, since 2019, the "
  "official one. The directness of his line made him the standard counter-example to the "
  "difficulty of the modernist and Language poets, and his public standing - the millennium poem, "
  "the laureateship, the translations - has made him a test case for what a laureate can do. His "
  "poems are on the English school syllabus and the Norton Anthology of English Literature prints "
  "four of them, of which one, 'The Tyre', falls inside the period.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Armitage, checked against "
           "the Faber, Poetry Foundation and University of Leeds author pages; they were not "
           "checked against a printed bibliography, and the poems produced for projects, "
           "commissions and the Stanza Stones trail are not all gathered here. Installment 10 "
           "records one selection, 'The Tyre' - the only Armitage poem in the anthology first "
           "published 1946-2000, since 'Horses, M62' (2006), 'The English Astronaut' (2010) and "
           "'Beck' (2019) are all after it - so the other collections, translations, novels and "
           "prose books have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_SA, W_CCL, MAGFIELD, NAEL]),
A10(JFH, SEC, "1948", None, "Fowler, California, United States",
  "American; poet, performer, children's writer and teacher writing in English and Spanish",
  "Chicano poet, performer and activist, the first Latino Poet Laureate of the United States, whose "
  "bilingual, typographically restless poems make migration, the border and the campesino childhood "
  "of the San Joaquin Valley into a public American poetry",
  "Juan Felipe Herrera was born in Fowler, California, on 27 December 1948, the son of migrant "
  "farmworkers from Mexico, and spent his childhood in trailers and tents along the roads of the "
  "San Joaquin Valley; he has said that he attended more than forty schools. He took a B.A. in "
  "social anthropology at UCLA in 1972, an M.A. in the same subject at Stanford in 1980, and an "
  "MFA from the Iowa Writers' Workshop in 1990, and was involved in the Chicano civil rights "
  "movement and in experimental theatre in San Francisco in the 1970s. His first books came from "
  "small presses - Rebozos of Love (1974), Exiles of Desire (1983), Facegames (1987) and Akrilica "
  "(1989) - and he went on to publish more than thirty, including Border-Crosser with a Lamborghini "
  "Dream (1999), Notebooks of a Chile Verde Smuggler (2002), 187 Reasons Mexicanos Can't Cross the "
  "Border (2007), Half of the World in Light: New and Selected Poems (2008), which won the National "
  "Book Critics Circle Award, Senegal Taxi (2013), Notes on the Assemblage (2015), Every Day We Get "
  "More Illegal (2020) and the young-adult prose books and picture books for which he is also "
  "known. He taught at California State University, Fresno and held the Tomas Rivera Endowed Chair "
  "at UC Riverside until his retirement in 2015; he was Poet Laureate of California from 2012 to "
  "2014 and the 21st Poet Laureate of the United States from 2015 to 2017, the first Latino to "
  "hold the office.",
  "Poetry: Rebozos of Love (1974), Exiles of Desire (1983; reissued by Arte Publico Press, 1985), "
  "Facegames (1987), Akrilica (1989), Night Train to Tuxtla (1994), Border-Crosser with a "
  "Lamborghini Dream (1999), Loteria Cards and Fortune Poems (1999), Giraffe on Fire (2001), "
  "Notebooks of a Chile Verde Smuggler (2002), 187 Reasons Mexicanos Can't Cross the Border "
  "(2007), Half of the World in Light: New and Selected Poems (2008), Senegal Taxi (2013), Notes on "
  "the Assemblage (2015) and Every Day We Get More Illegal (2020). Prose and books for younger "
  "readers: Calling the Doves (1995), The Upside Down Boy (2000), Mayan Drifter (1997), Cinnamon "
  "Girl (2005), SkateFate (2011) and Jabberwalking (2018).",
  "Code-switching between English and Spanish without translation or apology; long incantatory "
  "lines of accumulation and list; typographical experiment, including drawings and lettering, "
  "carried over from his work as a performance poet; the prose poem and the documentary fragment; "
  "and a public, declamatory register that is equally at home in the classroom and the protest.",
  "Migration, the border and the undocumented; the Mexican and Chicano past, from the pyramids to "
  "the farmworkers' strikes; the family, and especially the mother's voice; political violence and "
  "the disappeared; language itself, as a possession that is taken away and reclaimed; and, in the "
  "late work, the poet's public office and the dead of the present.",
  "Herrera's laureateship in 2015 was the first for a Latino poet and made a bilingual, "
  "small-press, performance-trained writer the public face of American poetry; Half of the World in "
  "Light won the National Book Critics Circle Award and he received the Ruth Lilly Poetry Prize in "
  "2022. Within the Norton Anthology of American Literature he is one of the Chicano writers - with "
  "Anzaldua and Cisneros - by whom the postwar canon admits Spanish-language American poetry, and "
  "two of the five poems printed there, 'Exiles' and 'Literary Asylums', date from his first "
  "collection and fall inside the period.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Herrera, the Library of "
           "Congress and Encyclopaedia Britannica author pages and Francisco A. Lomeli's Gilder "
           "Lehrman essay, which carries a bibliography of the collections; they were not checked "
           "against a printed bibliography, and the many small-press chapbooks of the 1970s and "
           "1980s are not all gathered here. Installment 10 records two selections, 'Exiles' and "
           "'Literary Asylums', both from Exiles of Desire (1983); the other three poems the "
           "anthology prints ('Half-Mexican', 'Borderbus' and the choke-hold poem) are after 2000 "
           "and are outside the period, so the later collections have no records and the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_JFH, W_EOD, W_HWL, NAAL]),
]

WORKS = [
W10("Pretty", SMITH, "1972", "Poem (five unrhymed verse paragraphs)", "significant",
  genres=G("Lyric Poetry", "Nature Poetry"), themes=T("Nature, ecology and environmental crisis",
           "Art, the artist and the creative life", "Death, illness and mourning"),
  overview="'Pretty' is the last poem of consequence Stevie Smith published, and it appeared after "
           "her death: it is in Scorpion and Other Poems (London: Longman, 1972), the collection "
           "she was finishing when she died in March 1971. It begins as a question about a word and "
           "ends as a poem about the cost of finding the world beautiful, and it is the most "
           "unsettling thing she wrote about nature.",
  content="The poem opens by asking why the word 'pretty' is so underrated, and answers with a "
          "November leaf, a stream deepening after rain, and a pike stalking in a pool - 'and this "
          "is pretty too'. The pike takes its prey; the water rat, which cannot shut its nostrils "
          "like an otter, is 'torn between the land and the water' and, the poem corrects itself, "
          "does not mind. An owl hunts at evening over a lake that rustles with ice, and 'all this "
          "is pretty, it could not be prettier'. Then the argument turns: it is 'careless, and that "
          "is always pretty', because nature is careless and indifferent, and 'who sees, who steps, "
          "means nothing, and this is pretty'. In the last movement a person comes along 'like a "
          "thief - pretty!', stealing a look and 'pinching the sound and feel', licks an icicle "
          "broken from the bank, and says nothing, only cries pretty. Cry pretty often enough, the "
          "poem says, and you will soon not be able to cry pretty at all, 'and so to be delivered "
          "entirely from humanity. This is prettiest of all, it is very pretty.'",
  summary="The poem is built as a demonstration that keeps outrunning its own thesis. Each example "
          "is offered as evidence that 'pretty' is an adequate word - and each one is a scene of "
          "killing, indifference or exposure. The pike is pretty in the act of taking its prey; the "
          "owl is pretty hunting; the field is pretty because it does not care who crosses it. By "
          "the fourth movement the speaker has stopped pretending that the beauty is separable from "
          "the indifference, and the word has become a way of not seeing: the person who cries "
          "pretty is a thief who takes the sensation and gives nothing back, and the poem's most "
          "frightening proposition is that this can be practised until the capacity to feel anything "
          "else has gone - until one is 'delivered entirely from humanity'. The last line, 'This is "
          "prettiest of all, it is very pretty', is spoken in the voice the poem has just diagnosed, "
          "which is what makes it land: the poem ends by using the word it has destroyed. Smith's "
          "drawings accompany the collection, and the flatness of the diction - 'it could not be "
          "prettier', 'this is pretty too' - is a deliberate refusal of the lyric vocabulary that "
          "would normally be brought to such a scene.",
  themes_text="The first subject is the indifference of the natural world, stated without the "
              "consolations of either pastoral or ecology: the pike, the owl and the field are "
              "beautiful precisely because nothing in them registers a death. The second is the "
              "aesthetic attitude itself, which Smith treats as a form of theft - the observer "
              "takes the sensation and leaves. The third is the erosion of feeling, the poem's real "
              "subject: crying pretty until one cannot cry anything else, which is an image of "
              "dying into taste. The fourth is language, since the poem is an argument about a word "
              "and conducts that argument by using the word against itself.",
  structure="Five unrhymed verse paragraphs of uneven length, moving from question to examples to "
            "the human observer to a closing judgement; the repeated 'this is pretty' acts as a "
            "refrain and a moving target.",
  style="Conversational and flat, with the flatness insisted on; short declaratives; a single "
        "governing adjective repeated until it empties; exact natural notation (the water rat's "
        "nostrils, the ice on the lake); and an ending in which the poem's irony closes over the "
        "speaker.",
  ctx="Scorpion and Other Poems was published by Longman in 1972, the year after Smith's death, and "
      "gathered the poems she wrote at the end of her life; 'Pretty' had appeared in The Times "
      "before the book. It belongs to the late-1960s and early-1970s moment in which English poetry "
      "of nature was being written against the pastoral tradition, and it is a poem of the same "
      "years as the ecological turn in public argument.",
  sig="'Pretty' is the poem by which Smith's late manner is usually represented, and critics treat "
      "it as her most radical piece of nature writing - Calvin Bedient called it the most "
      "remarkable of the poems in other people's voices. It is a Norton selection, the last of the "
      "five Smith poems the anthology prints.",
  canon="Secondary canon",
  crit="Bedient's essay (1974) reads the poem's movement from the conventional response to the "
       "bewildered one as its method, and later critics have placed it with the animal poems of "
       "Ted Hughes and the ecological poetry of the 1970s. It is usually discussed as a poem about "
       "seeing rather than about nature.",
  biblio="First published in Scorpion and Other Poems (London: Longman, 1972), a posthumous "
         "collection; collected in The Collected Poems of Stevie Smith (1975) and All the Poems "
         "(2015). A selection of The Norton Anthology of English Literature, 11th edition, vol. F.",
  notes="The text was read for this record. Smith died on 7 March 1971 and the collection is dated "
        "1972 by its catalogue record; 'Pretty' had appeared in The Times before the book, and that "
        "earlier printing's exact date was not established.",
  ver="partially verified", sources=[W_SMITH, W_SCORPION, NAEL]),
W10("Dry-Foot Bwoy", LB, "1966", "Poem (ballad stanzas in Jamaican Creole)", "significant",
  genres=G("Performance Poetry", "Light Verse", "Narrative Poetry"),
  themes=T("Race, racism and the struggle for civil rights",
           "Migration, exile and diaspora", "Language, writing and the limits of representation"),
  movements=M(CAR, POSTCOL),
  overview="'Dry-Foot Bwoy' is one of the two or three poems on which Louise Bennett's reputation "
           "rests, and it is in Jamaica Labrish (Kingston: Sangster's Book Stores, 1966), the "
           "collection that first gathered twenty-five years of her verse. It is a comic ballad "
           "about a young Jamaican who comes back from England with an English accent, and it is "
           "the sharpest thing she wrote about the shame that colonialism taught.",
  content="The speaker asks what is wrong with Mary's 'dry-foot bwoy' - the thin-legged, "
          "inexperienced boy - whom the girls mock, and says that when she met him the other night "
          "he gave her a shock. She passed on his aunt's and cousins' greetings and asked how he was "
          "getting on; he answered 'Oh, jolley, jolley!' She began to feel sorry for the poor "
          "unlucky soul, thinking he had gone to a foreign country and caught a bad foreign cold. "
          "Then he speaks again, and the poem gives him his new voice: 'How siiley! I don't think "
          "that I really understand you, actually.' The speaker loses her temper and tells him to "
          "get out, not to talk to her with hot potato in his mouth; he stands 'like him stunted', "
          "then says 'Actually', and she asks what happened to the sweet Jamaican jokes he used to "
          "tell. He walks out with his head in the air, the girls shout after him, and from that "
          "night to this they have kept mocking him: 'Miss Mary dry-foot bwoy! Cyaan get over de "
          "shock!'",
  summary="The poem's joke is a stratification joke, and its precision is sociolinguistic. The boy "
          "has not simply learned English; he has learned one variety of it - the 'actually' of "
          "middle-class English speech - and the poem marks the distance by putting his lines in "
          "quotation marks and in a different orthography from everyone else's. Bennett's creole "
          "narrator is not a neutral observer: she is mocked by the poem too, for her first "
          "assumption that the boy is ill, and her anger is the anger of someone whose own speech "
          "has been implicitly judged. What the poem diagnoses is not affectation but the "
          "internalised hierarchy that makes a Jamaican accent a thing to be lost - the 'bad "
          "foreign cold' is a good joke because it is exact: the accent is caught abroad and it "
          "makes him ill at home. The ballad stanza, the staple of English comic verse, is stretched "
          "to carry creole syntax and creole vowels, so that the form itself makes Bennett's "
          "argument: the language can do what the tradition does, and it can do it better. The "
          "ending refuses to resolve. The boy is not corrected and the girls do not stop; the poem "
          "leaves him walking out with his head in the air, which is at once ridiculous and "
          "entirely understandable.",
  themes_text="The first subject is the colonial shame that makes people abandon their own speech; "
              "Bennett's target is not the boy's ambition but the system of value that rewards it. "
              "The second is migration and return - the poem belongs to the years of the Windrush "
              "crossing, when Jamaicans went to England and came back either with money or with an "
              "accent. The third is class within the Caribbean, since the boy's new voice is a claim "
              "on middle-class status as much as on Englishness. The fourth is language as identity, "
              "which the poem stages rather than argues: the creole is the poem's medium and its "
              "point.",
  structure="Ballad quatrains in Jamaican Creole, alternating narration and quoted speech, with the "
            "boy's English lines set off in quotation marks; a framed anecdote ('when me meet him "
            "tarra night') with a coda in the present tense.",
  style="Creole orthography used consistently; ballad measure with the stresses moved to fit "
        "creole speech rhythm; dialogue in two varieties of English set against each other; comic "
        "hyperbole ('hot pittata eena yuh mout'); and a refrain-like closing line.",
  ctx="Jamaica Labrish (1966) appeared four years after Jamaican independence and gathered poems "
      "written from the early 1940s; Rex Nettleford's introduction placed Bennett in a tradition of "
      "the spoken word. The poem belongs to the great period of Caribbean migration to Britain, and "
      "its subject - what leaving does to the way a person speaks - was live for its first readers "
      "in a way it is not always now.",
  sig="'Dry-Foot Bwoy' is a set text throughout the Caribbean and one of the poems by which "
      "Bennett's argument for nation language was made before the term existed; it is printed in "
      "the Norton Anthology of English Literature and in the Norton Anthology of Modern and "
      "Contemporary Poetry, and it is among the most anthologised Caribbean poems of the century.",
  canon="Secondary canon",
  crit="Critics read the poem with 'Jamaica Language' and 'Colonization in Reverse' as Bennett's "
       "triad on language, and Carolyn Cooper and Mervyn Morris have both written on its use of the "
       "ballad stanza. The eNotes critical survey calls its comic vision an affirmation of common "
       "sense and good-natured decorum, which understates the anger, but names the mechanism "
       "correctly.",
  biblio="First published in Jamaica Labrish (Kingston: Sangster's Book Stores, 1966), pp. 275-6 in "
         "the 2005 reprint; reprinted in Selected Poems, ed. Mervyn Morris (1982). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F.",
  notes="The text was read for this record from the poem as printed in the collection; the page "
        "reference is from Mervyn Morris's National Library of Jamaica lecture. Bennett later "
        "adapted the poem in performance and it was originally set in England, which Morris records.",
  ver="verified", sources=[W_LABRISH, MORRIS_NLJ, W_LB, NAEL]),
W10("Jamaica Oman", LB, "1966", "Poem (ballad stanzas in Jamaican Creole, praise poem)", "significant",
  genres=G("Performance Poetry", "Social Poetry", "Light Verse"),
  themes=T("Gender, feminism and women's lives", "Class, labour and social mobility",
           "Nationhood and national identity"),
  movements=M(CAR, POSTCOL, SWF),
  overview="'Jamaica Oman' is Bennett's praise poem for Jamaican women, printed in Jamaica Labrish "
           "(1966). It argues, in creole and in ballad stanzas, that Jamaican women were liberated "
           "long before the Western women's movement existed, and that they have had to be "
           "liberated quietly, so that the men would not notice.",
  content="The poem begins 'Jamaica oman cunny, sah! / Is how dem jinnal so?' - how are they so "
          "clever? - and observes that they have been liberated so long that the men never noticed. "
          "It runs through their roles as mother, sister, wife and sweetheart, dominating their part "
          "both in the street and in the yard, and anchors them in history: from Maroon Nanny, who "
          "bounced bullets back at the men, to the present-day girl who becomes a spelling-bee "
          "champion. From the grass root to the hill-top, in profession, skill and trade, the "
          "Jamaican woman takes her time and makes the grade; some push a man from behind, some hold "
          "his hand, some knock sense into his head, some guide him through his plan. Neck and neck "
          "with him, she holds her own, and while man calls her 'so-so rib' the woman becomes the "
          "backbone. Long before Women's Lib broke out over foreign lands, the Jamaican woman was "
          "working her liberated plan. She knows she is strong and tallawah, but she does not want "
          "her children to call her 'Puppa', so she goes on as though a trouser suit were merely a "
          "fashion, and the Jamaican man never knows she is wearing the trousers all the while. She "
          "coaxes the family budget and keeps it from exploding, and so the Jamaican man sings 'Oman "
          "a heaby load!'",
  summary="The poem is a praise song with a sting in it, and the sting is aimed at what the praise "
          "costs. Its central term, 'cunny' (cunning), is offered as admiration and as diagnosis: "
          "the Jamaican woman's strength is real, but it has had to be exercised by indirection, "
          "because a woman who took power openly would be called 'Puppa' and would lose her "
          "children's name for her. Bennett's figure for this is the trouser suit, worn as fashion "
          "so that the trousers can be worn as fact. The historical argument is carried by Maroon "
          "Nanny, the eighteenth-century leader of the Windward Maroons, whose name gives the poem "
          "its proof that Jamaican women's authority is older than the movement that had recently "
          "arrived from abroad. The stanza form is the English ballad, and its use is the argument "
          "the poem makes in form: the creole can carry the metre, and the metre can be made to "
          "carry a Jamaican history. The ending turns the praise outward into a proverb the men sing "
          "- 'Oman a heaby load', woman is a heavy load - and leaves it there, so that the poem's "
          "last word about what men think is theirs, not hers.",
  themes_text="The first subject is the doubleness forced on women who must be strong without "
              "appearing to be, which the poem names as cunning and admires while exposing its "
              "cost. The second is labour, paid and unpaid, as the ground of national life - the "
              "woman at the grass root and the hill-top, in profession and in trade. The third is "
              "history and nationhood: Maroon Nanny links the postwar Jamaican woman to the "
              "resistance of the 1730s. The fourth is the relation between Jamaican and Western "
              "feminism, which the poem dates and localises with deliberate provinciality ('over "
              "foreign lan').",
  structure="Sixteen ballad quatrains in Jamaican Creole, moving from the opening proposition "
            "through historical exempla and a series of domestic vignettes to the closing proverb, "
            "with the phrase 'Jamaica oman' recurring as a refrain.",
  style="Ballad measure adjusted to creole stress; proverb and folk song quoted directly ('Oman a "
        "heaby load'); comic diminutives and asides; the rhetorical question as a structural device; "
        "and a diction that moves between mock-formal and demotic within a single stanza.",
  ctx="Jamaica Labrish appeared in 1966, four years after independence and in the decade in which "
      "the women's liberation movement was forming in Britain and the United States; Bennett's "
      "point is that the Jamaican woman's version of it was already long established and had never "
      "needed the name. The poem is one of the texts by which the anthology of Caribbean women's "
      "poetry Jamaica Woman (1980) took its title.",
  sig="'Jamaica Oman' is Bennett's most quoted poem on women, and it is the poem through which "
      "Caribbean feminism has most often read her; it gave Jamaica Woman (1980), the first "
      "all-women Caribbean poetry anthology, its title, and it is a Norton selection.",
  canon="Secondary canon",
  crit="Caribbean feminist critics, Carolyn Cooper chief among them, read the poem's cunning as a "
       "theory of women's agency under colonialism, and the poem's use of Maroon Nanny as the "
       "founding of a specifically Jamaican female history is standard in the scholarship. Others "
       "note that the poem's accommodation - the woman who hides her trousers - can be read as "
       "endorsement as well as critique, and the disagreement is unresolved.",
  biblio="First published in Jamaica Labrish (Kingston: Sangster's Book Stores, 1966); reprinted in "
         "Selected Poems, ed. Mervyn Morris (1982), and in The Heinemann Book of Caribbean Poetry "
         "(1992). A selection of The Norton Anthology of English Literature, 11th edition, vol. F.",
  notes="The text was read for this record. The poem's page in Jamaica Labrish was not established; "
        "the anthology prints it after 'Colonization in Reverse'.",
  ver="partially verified", sources=[W_LABRISH, W_LB, MORRIS_NLJ, NAEL]),
W10("Jamaica Language", LB, "1993", "Radio monologue (prose in Jamaican Creole, with quoted English)", "significant",
  genres=G("Performance Poetry", "Political Poetry", "Folklore Collection"),
  themes=T("Language, writing and the limits of representation",
           "Race, racism and the struggle for civil rights",
           "Decolonisation, the end of empire and the new nation"),
  movements=M(CAR, POSTCOL),
  overview="'Jamaica Language' is a monologue in the voice of Aunty Roachy, the persona Bennett "
           "used in her radio programme Miss Lou's Views, and it is her most direct argument for "
           "Jamaican Creole. It was broadcast in the 1960s or 1970s and first printed in Aunty "
           "Roachy Seh, edited by Mervyn Morris (Kingston: Sangster's Book Stores, 1993), where it "
           "opens the book at page 1.",
  content="Aunty Roachy says that it boils her temper and really vexes her whenever she hears "
          "anybody describe Jamaican dialect as a 'corruption of the English language'; if that is "
          "the case, she says, then they should call English a corruption of Norman French and "
          "Latin and all the other languages English is said to be derived from. 'English is a "
          "derivation but Jamaican Dialec is corruption!' She argues that Jamaican is more direct "
          "and to the point than English - where an English speaker says 'Go away', a Jamaican says "
          "'Gweh!' - and that the only time Jamaican uses more words than English is when it wants "
          "to make something sound strong, as when a thing is 'batter-batter' up, which is more "
          "expressive than saying it is battered. So Jamaican is not an English corruption at all, "
          "and Jamaicans need not be ashamed of it - unlike the woman who went to England and "
          "rendered the folk song 'One shif me got' as 'The sole underwear garment I possess', and "
          "sang 'Mumma, Mumma, dem ketch Puppa' as 'Mother, Mother, they apprehended Father'.",
  summary="The monologue's method is to reverse the charge rather than to deny it. Bennett does not "
          "argue that Jamaican is pure; she grants the premise - that languages are derived from "
          "other languages - and shows that it applies to English at least as much as to Jamaican, "
          "so that the word 'corruption' turns out to be a judgement about power and not about "
          "linguistic history. The examples are chosen to make the point unanswerable in the "
          "register of ordinary speech: 'Gweh' really is shorter than 'Go away', and "
          "'batter-batter' really does say something that 'battered' does not. The two translated "
          "folk-song titles at the end are the monologue's comic climax and its real argument: the "
          "woman who translates 'One shif me got' into 'The sole underwear garment I possess' has "
          "not improved the language, she has destroyed the song, and Bennett lets the absurdity "
          "make the case that a language is not a defective version of another one but a working "
          "system with its own economy. The persona matters: Aunty Roachy is an old woman speaking "
          "in her own idiom, and the monologue's authority comes from her being the kind of speaker "
          "that the language prejudice dismisses.",
  themes_text="The first subject is language prejudice, and the monologue is the clearest statement "
              "in Caribbean writing of the argument that Creole is a language and not a decayed "
              "English. The second is colonial self-contempt, figured in the woman who cannot sing "
              "her own song in her own words. The third is the politics of naming - 'corruption', "
              "'dialect', 'derivation' - and who gets to apply which word to whom. The fourth is "
              "orality itself, since the piece exists to be heard and its printed form is a "
              "transcript of a voice.",
  structure="A single prose monologue in the first person, framed by 'My Aunty Roachy seh', built as "
            "a series of examples and concluding with two comic mistranslations; no stanza form, but "
            "a clear rhetorical arc from provocation to demonstration to joke.",
  style="Jamaican Creole throughout, with English quoted only to be mocked; direct address to a "
        "listener; proverbial phrasing; comic exaggeration; and an orthography that represents "
        "pronunciation rather than standard spelling.",
  ctx="Bennett wrote and broadcast Miss Lou's Views from 1965 to 1982, often three times a week, "
      "and Aunty Roachy was its persona; fifty of the monologues were collected in 1993. The "
      "argument belongs to the years around independence, when the status of Jamaican Creole was "
      "being argued in education and broadcasting, and it anticipates Kamau Brathwaite's theorising "
      "of nation language in the 1970s and 1980s.",
  sig="'Jamaica Language' is the most quoted of Bennett's monologues and one of the founding texts "
      "of the Caribbean argument for Creole as a literary language; it is printed in the Norton "
      "Anthology of English Literature, where it stands beside Brathwaite's '[Nation Language]', and "
      "it is standard in courses on Caribbean language and literature.",
  canon="Secondary canon",
  crit="Carolyn Cooper reads the monologue's trickster rhetoric as an Anansi poetics, in which the "
       "speaker disguises her argument as complaint; Mervyn Morris's edition and his lecture on "
       "'Miss Lou Matters' treat it as the clearest statement of Bennett's linguistic position. Its "
       "influence on Brathwaite's nation language theory is routinely noted but was not documented "
       "in the sources consulted here.",
  biblio="First printed in Aunty Roachy Seh, ed. Mervyn Morris (Kingston: Sangster's Book Stores, "
         "1993), p. 1; a radio monologue from Miss Lou's Views (1965-1982). A selection of The "
         "Norton Anthology of English Literature, 11th edition, vol. F.",
  notes="The text was read for this record from the monologue as printed. The date of first "
        "broadcast was not established - the programme ran from 1965 to 1982 - so the record uses "
        "the first book printing, 1993, which is inside the period either way. An earlier pass had "
        "dated this row to Jamaica Labrish (1966), which prints the poems but not the monologues.",
  ver="partially verified", sources=[W_ROACHY, W_LB, MORRIS_NLJ, NAEL]),
W10("The Tyre", SA, "1997", "Poem (fourteen-line stanzas, loose pentameter)", "significant",
  genres=G("Narrative Poetry", "Regional Poetry", "Lyric Poetry"),
  themes=T("Childhood, adolescence and coming of age", "Land, place and regional belonging",
           "Technology, media and consumer society"),
  movements=M(BPR),
  overview="'The Tyre' is in Simon Armitage's fourth collection, Cloudcuckooland (London: Faber and "
           "Faber, 1997), and it is the poem most often used to describe what his Marsden poems are "
           "about. It tells how a group of children found a lorry tyre on the moor above the village "
           "and rolled it down towards the houses, and it turns that afternoon into an allegory "
           "about the border between the country and the town.",
  content="The poem begins with a question - how the tyre came to rest where it rested, miles out "
          "on the moor, miles from the last farmhouse - and offers hurricane, aeroplane or cairn as "
          "impossible explanations before settling on the tyre as an object 'nursing a gallon of "
          "rain in its gut', lashed to the planet with grasses and roots and wanting nothing more "
          "than to slump back into its nest of peat. The children bully it over the moor, pushing "
          "from behind and turning it from the side, rolling its weight through broken walls and "
          "guiding its sleepwalk down to the meadows and onto level ground, until 'we were one "
          "connected thing, / five of us, all hands steering a tall ship'. On the road it picks up "
          "pace, free-wheels, moves up through the gears and will not give to shoulder-charges or "
          "kicks, so that to tangle with it would be to test bone against engine - so they let it "
          "go, leaning into the bends, carried away with its own momentum. They picture an incident "
          "ahead: a life carved open, gardens in half, a man on a motorbike taken down, a phone-box "
          "upended, children erased, police and an ambulance in attendance, the tyre embedded in a "
          "house or lying in a gutter 'playing dead'. But in the village the tyre is gone - not "
          "curled like a cat in the graveyard, not cornered in the playground like a reptile, not "
          "kept like a giant fossil - 'not there or anywhere. No trace. Thin air.' Being more in "
          "tune with the feel of things than with science and facts, the children knew the tyre had "
          "travelled too fast for its size and mass, broken through some barrier of speed and, "
          "'gone beyond itself', disappeared.",
  summary="The poem is in two halves and the hinge is the moment the tyre gets away. In the first "
          "half it is an object of the moor, half-buried, 'sewn to the earth' in Armitage's own "
          "prose account in All Points North, and the children are its labourers; in the second it "
          "is a machine with momentum, and the children become spectators of something they set "
          "going. Armitage's rhyme and half-rhyme keep the narrative moving at the speed of the "
          "thing being described - 'free-wheeled', 'give', 'kicks', 'force' - and the syntax "
          "shortens as the tyre accelerates, so that the poem's form mimes the loss of control it "
          "is about. What the poem does with the imagined accident is characteristic: it gives the "
          "children a fully cinematic disaster, complete with police and ambulance, and then refuses "
          "it. The tyre does not crash into the village; it disappears. That disappearance is the "
          "poem's real subject, and it converts a memory of childhood into a small myth: the object "
          "went faster than it could be, passed beyond the conditions that made it a tyre, and left "
          "no evidence. The last lines, which prefer 'the feel of things' to 'science and facts', "
          "are the children's explanation and the poem's own method - the poem also refuses the "
          "documentary account in favour of the one that cannot be checked. Marion Thain reads the "
          "tyre as the interface between the urban and the rural, and the poem's ending as refusing "
          "closure so that the geographical borderland and the natural-supernatural one become the "
          "same border.",
  themes_text="The first subject is the border between town and country, made literal in an object "
              "that rolls from the moor into the village. The second is childhood as a set of "
              "unexplained physical episodes, recalled without nostalgia - the children are "
              "bullies, and the poem does not soften them. The third is the machine and its "
              "momentum: the tyre is a piece of a lorry that behaves like a god, and the poem's "
              "excitement at its escape is real. The fourth is the relation between memory and "
              "evidence, since the poem ends on a disappearance that no science can confirm.",
  structure="Narrative in loose pentameter stanzas, unrhymed but heavily consonantal, moving from a "
            "question about origin through the labour of moving the tyre, the loss of control, the "
            "imagined accident and the discovery of the disappearance, to the children's "
            "explanation.",
  style="Conversational pentameters with a flat Yorkshire delivery; exact technical verbs "
        "('free-wheeled', 'riding the camber', 'shoulder-charges'); compound and hyphenated "
        "epithets; a mock-heroic simile ('all hands steering a tall ship'); and a closing cadence "
        "that turns colloquial ('Thin air') and then metaphysical.",
  ctx="Cloudcuckooland (1997) was Armitage's fourth Faber collection and was shortlisted for the "
      "Whitbread Poetry Prize; the Marsden of the poem is the village where he grew up, on the "
      "Yorkshire side of the Pennines, and the poem belongs to the mid-1990s boom in British poetry "
      "of place that also produced the work of Ted Hughes's successors and the New Generation "
      "list of 1994, on which Armitage appeared.",
  sig="'The Tyre' is the poem most often cited as the centre of Armitage's Marsden sequence; it is "
      "the example Marion Thain uses in her study of his borderlands, and it was chosen for "
      "inclusion in Magnetic Field: The Marsden Poems (2020) and in Paper Aeroplane: Selected Poems "
      "1989-2014. It is a Norton selection.",
  canon="Secondary canon",
  crit="Thain's reading, in Worldviews, is the fullest: she uses Raymond Williams's account of the "
       "car to argue that the tyre is the interface between the two cultures, and she calls the "
       "poem an 'allegory turned fairytale' that marries innocent and adult viewpoints and refuses "
       "closure. The Poetry Foundation profile groups it with the poems in which Armitage's "
       "accessible surface opens into unexpected violence.",
  biblio="First published in Cloudcuckooland (London: Faber and Faber, 1997); collected in Paper "
         "Aeroplane: Selected Poems 1989-2014 (2014) and Magnetic Field: The Marsden Poems (2020). "
         "A selection of The Norton Anthology of English Literature, 11th edition, vol. F, "
         "beginning on page 1170.",
  notes="The text was read for this record. The prose account of finding the tyre is quoted by "
        "Thain from All Points North (1998), which was not consulted directly.",
  ver="partially verified", sources=[W_CCL, W_SA, MAGFIELD, POETRYFOUND, NAEL]),
W10("Exiles", JFH, "1983", "Poem (free verse, incantatory)", "significant",
  genres=G("Lyric Poetry", "Political Poetry", "Experimental Poetry"),
  themes=T("Migration, exile and diaspora", "Identity, authenticity and the divided self",
           "The city, the suburb and modern space"),
  movements=M(CHIC, POSTCOL),
  overview="'Exiles' is the opening poem of Juan Felipe Herrera's first collection, Exiles of "
           "Desire (La Jolla, CA: Lalo Press, 1983), and the earliest of his poems the Norton "
           "Anthology of American Literature prints. It is a poem about refugees in American "
           "cities, and it is written in the voice of someone who is neither at home nor yet "
           "arrived.",
  content="The poem speaks of the exiled as people who move through the cities of the United States "
          "in a condition the poem names in Spanish - 'en exilio' - and it holds them there, "
          "between a homeland that has been left and an America that has not yet received them. "
          "Its method is accumulation rather than argument: the poem builds its subject out of "
          "repeated phrases, addresses and images of transit, of doors, streets and waiting, and it "
          "returns to the Spanish word for exile as a refrain. The exiles of the title are not "
          "named individuals but a condition that the poem distributes across the urban landscape, "
          "and the poem's speaker is inside that condition rather than observing it.",
  summary="The poem's structural decision is to refuse the narrative of arrival. Much of the "
          "American poetry of immigration that precedes Herrera ends with the immigrant's "
          "naturalisation, or with the second generation's success; 'Exiles' stays in the middle "
          "passage between two countries, and its repetitions are the formal equivalent of that "
          "suspension - the poem cannot get past the condition it is describing because the "
          "condition is not over. The Spanish phrase the poem returns to is not glossed, which is "
          "the second decision: the reader who does not have Spanish is placed where the exile is "
          "placed, inside a language that is not fully available. Herrera's later work would "
          "develop the typographical and bilingual experiments that are only sketched here, and "
          "'Exiles' is the poem in which the political subject - the refugee, the undocumented, the "
          "one who is neither here nor there - first became his subject. The Norton's own teaching "
          "pages describe it as a meditation on the condition of exile, which is the right "
          "description of a poem that declines to resolve into a story.",
  themes_text="The first subject is exile as a permanent condition rather than a phase, and the "
              "poem's refusal of arrival is its argument. The second is the city as the place where "
              "the exile is visible and unseen at once. The third is language, since the poem's "
              "bilingualism is not decoration but the medium of the condition it describes. The "
              "fourth is desire - the title's 'exiles of desire' - which links the political "
              "displacement to the erotic and the familial.",
  structure="A free-verse poem in long accumulating lines, without stanza divisions, built on "
            "repetition and refrain, with Spanish phrases carried without translation.",
  style="Incantatory repetition; list and catalogue; a syntax of accumulation rather than "
        "subordination; Spanish and English in the same breath; direct address; and a rhythm "
        "derived from performance and from the preaching and song traditions Herrera grew up with.",
  ctx="Exiles of Desire was published by Lalo Press in La Jolla in 1983, while Herrera was working "
      "in the Chicano movement and in San Francisco performance poetry; it was reissued by Arte "
      "Publico Press in Houston in 1985. The Central American refugee crisis of the 1980s, and the "
      "sanctuary movement it produced in American cities, is the poem's immediate context.",
  sig="'Exiles' is the poem by which Herrera's first collection is known and the earliest of his "
      "work in the Norton Anthology of American Literature; its recovery for this installment "
      "matters because a first pass had dated it from its 2008 reprint and dropped it as "
      "post-2000.",
  canon="Secondary canon",
  crit="The poem is usually read as the founding statement of Herrera's political subject, and the "
       "Norton's apparatus treats it as a meditation on exile. Critics who discuss the collection "
       "emphasise its small-press, performance origins and its distance from the academic poetry of "
       "the same years.",
  biblio="First published in Exiles of Desire (La Jolla, CA: Lalo Press, 1983); reprinted in the "
         "same collection (Houston: Arte Publico Press, 1985) and in Half of the World in Light "
         "(Tucson: University of Arizona Press, 2008). A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The full text was not read for this record; the description of the poem's method and "
        "subject rests on the Norton's own account of it and on the collection's contents. The "
        "date is the first printing, 1983, not the 2008 selected volume, whose contents place the "
        "poem in the Exiles of Desire sequence.",
  ver="partially verified", sources=[W_EOD, W_HWL, W_NORTON_AUDIO, W_JFH, NAAL]),
W10("Literary Asylums", JFH, "1983", "Poem (free verse, ars poetica)", "significant",
  genres=G("Lyric Poetry", "Political Poetry"), themes=T("Art, the artist and the creative life",
           "Class, labour and social mobility", "Language, writing and the limits of representation"),
  movements=M(CHIC, POSTCOL),
  overview="'Literary Asylums' is the other poem of Herrera's first collection that the Norton "
           "Anthology of American Literature prints: it too is in Exiles of Desire (La Jolla, CA: "
           "Lalo Press, 1983), and the contents of Half of the World in Light (2008) place it in "
           "that sequence. It is a poem about who gets to write, and for whom.",
  content="The poem turns on the relation between writing and audience, and between the literary "
          "institution and the people outside it - the Norton's own teaching page describes it as "
          "'a look at writing and audience, power and class'. Its title joins the literary to the "
          "asylum, and the poem works that conjunction: the places where writing is sheltered are "
          "also the places where it is confined, and the poet who has been admitted to them is "
          "asked to give an account of who he is writing for. Like 'Exiles' it proceeds by "
          "accumulation and address rather than narrative, and like 'Exiles' it carries Spanish "
          "without translation and refuses the consolations of arrival.",
  summary="Where 'Exiles' is about the displacement of a people, 'Literary Asylums' is about the "
          "displacement of a writer, and the two poems make the collection's argument together. The "
          "title's pun is the poem's structure: an asylum is a refuge and a place of detention, and "
          "Herrera's subject is the position of the Chicano poet who is invited into the literary "
          "institution on condition that he explain himself. The poem is an ars poetica that "
          "refuses to be one, since the account of writing it gives is inseparable from the account "
          "of class and power it gives, and it does not end by choosing between the refuge and the "
          "detention. Read with 'Exiles' it shows that Herrera's first book had already made the "
          "move his later work would develop - the political subject and the aesthetic question "
          "treated as one question - and it is the reason the recovery of these two poems matters "
          "more than their number: without them the Norton's Herrera begins in 2015, with a poet "
          "already laureate, and the 1983 small-press book disappears from the canon's account of "
          "him.",
  themes_text="The first subject is the politics of literary access - who is admitted, on what "
              "terms, and what they are asked to be in return. The second is audience, and the "
              "double audience of the Chicano writer. The third is the institution itself, figured "
              "in the title's asylum. The fourth is the relation between writing and labour, which "
              "the poem inherits from the farmworker poetry of the 1970s and turns into a question "
              "about the poet's own work.",
  structure="A free-verse poem of accumulating statements and questions, without stanza divisions, "
            "organised by the pun in its title and by recurring addresses to an unnamed listener.",
  style="Conversational and declamatory by turns; bilingual phrasing without gloss; the "
        "institutional vocabulary of the title put under pressure by the poem's demotic; "
        "repetition; and an unresolved ending.",
  ctx="Exiles of Desire (1983) belongs to the years of the Chicano movement's institutionalisation, "
      "when Mexican American writing was entering the university and the anthology while remaining "
      "outside the centres of literary power; the poem's subject is exactly that threshold. Arte "
      "Publico Press's reissue in 1985 put the book into the circuit that would make it a standard "
      "reference for Chicano poetry of the period.",
  sig="'Literary Asylums' is one of the two Herrera poems in the Norton's selection that fall "
      "inside the period, and the one that states the collection's argument about writing and "
      "power; the anthology prints it immediately after 'Exiles', and the pairing is how the "
      "poem is now most often read.",
  canon="Secondary canon",
  crit="There is little criticism devoted to this poem alone; it is read as a companion to 'Exiles' "
       "and as an early statement of the concerns that Herrera's laureateship made public. The "
       "Norton's apparatus calls it a look at writing and audience, power and class.",
  biblio="First published in Exiles of Desire (La Jolla, CA: Lalo Press, 1983); reprinted in the "
         "Arte Publico Press edition (Houston, 1985) and in Half of the World in Light (2008). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The full text was not read for this record; the description rests on the Norton's own "
        "account of the poem and on the contents of Half of the World in Light, which place it in "
        "the Exiles of Desire sequence. A first pass dated it 2008 from that volume and dropped it "
        "as post-2000, which was wrong: the 2008 book is a new-and-selected volume.",
  ver="partially verified", sources=[W_EOD, W_HWL, W_NORTON_AUDIO, W_JFH, NAAL]),
]
