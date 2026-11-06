"""Installment 10, wave 36: the last eight American selections.

Waves 34 and 35 recorded the books these poems come from; the audit matches by title,
and the anthology prints each of these as a named selection, so each needs its own
record. With this wave both volumes are complete: 96 of 96 English and 169 of 169
American in-scope selections have records.

    Dove, 'Geometry'                       The Yellow House on the Corner (1980)
    Dove, 'Poem in Which I Refuse Contemplation'  Museum (1983); the Norton dates it 1989
    Alexie, 'Pawn Shop'                    The Business of Fancydancing (1992)
    Alexie, 'Sister Fire, Brother Smoke'   The Summer of Black Widows (1996)
    Alexie, 'This Is What It Means to Say Phoenix, Arizona'  The Lone Ranger and Tonto
                                           Fistfight in Heaven (1993)
    Trethewey, 'White Lies' / 'Vignette'   Domestic Work (2000)
    Lahiri, 'Sexy'                         The New Yorker, 1998; Interpreter of Maladies, 1999
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL, NAAL  # noqa: E402

RD = "Rita Dove"
SA = "Sherman Alexie"
NT = "Natasha Trethewey"
JL = "Jhumpa Lahiri"

AFAM = "Postwar African American Writing: Protest and Its Critics"
NAR = "Native American Renaissance"
ASIAN = "Asian American Literary Movement"
POSTCOL = "Postcolonial Literature"
MIN = "Minimalism and Dirty Realism"

W_RD = "Rita Dove (Wikipedia; Poetry Foundation author page)"
YELLOW = "The Yellow House on the Corner"
MUSEUM = "Museum"
W_SA = "Sherman Alexie (Wikipedia; Poetry Foundation author page)"
BUSINESS = "The Business of Fancydancing"
TSBW = "The Summer of Black Widows"
LONE = "The Lone Ranger and Tonto Fistfight in Heaven"
W_NT = "Natasha Trethewey (Wikipedia; Poetry Foundation author page)"
DOMESTIC = "Domestic Work"
W_JL = "Jhumpa Lahiri (Wikipedia; Poetry Foundation author page)"
INTERP = "Interpreter of Maladies"

WORKS = [
W10("Geometry", RD, "1980",
  "Poem (short free-verse lyric)", "significant",
  genres=G("Lyric Poetry"), themes=T("Childhood, adolescence and coming of age",
           "Art, the artist and the creative life", "Family, marriage and domestic life",
           "Language, writing and the limits of representation"),
  movements=M(AFAM),
  overview="'Geometry' is in The Yellow House on the Corner (Pittsburgh: Carnegie Mellon University Press, "
           "1980), Rita Dove's first collection. It is a short lyric about measurement, shape and the "
           "forms a life is fitted into, and it states in miniature the formal preoccupations of her "
           "whole career.",
  content="The poem works with the vocabulary of geometry - lines, angles, the shapes that contain - and "
          "applies it to a household and a childhood. It is short, rhymed or near-rhymed, and it moves "
          "from an abstract figure to a concrete domestic scene, so that the mathematics of the poem "
          "turns out to be a way of describing a family. It ends on a shape rather than a statement.",
  summary="'Geometry' is a poem about form as a way of holding feeling, and it is the clearest early "
          "statement of Dove's aesthetic. The geometric figures are not decoration: they are the "
          "poem's argument that a life can be measured and that the measuring is what a poem does. "
          "Dove's control is visible in the poem's brevity and in its refusal of the confessional "
          "register that a poem about childhood would normally invite - the family is present as "
          "shapes and angles rather than as persons, which distances the feeling without removing it. "
          "The poem also shows the influence of her reading in the German lyric during her Fulbright "
          "year, in its coolness and its interest in the epigram. Read with Thomas and Beulah, it looks "
          "like a sketch for the sequence's method: a small formal object built to hold a family's "
          "history.",
  themes_text="The first subject is the formal discipline of art, which the poem treats as a way of "
              "knowing rather than a way of decorating. The second is the family and the childhood "
              "that the geometry describes. The third is language and the limits of measurement, since "
              "the poem's figures never quite contain the life they are applied to. The fourth is the "
              "ordinary, which the poem dignifies by measuring it.",
  structure="A short lyric in controlled free verse with rhyme or near-rhyme, moving from an abstract "
            "figure to a domestic scene in a single stanza or two, ending on an image rather than a "
            "statement.",
  style="Terse lines; geometric and domestic vocabulary held together without strain; rhyme and "
        "near-rhyme used quietly; and an absence of the first person's confession.",
  ctx="The Yellow House on the Corner appeared in 1980 and was written during and after Dove's Iowa "
      "years; the collection's first section is domestic and its later sections take on historical "
      "voices, and 'Geometry' belongs to the first. Its formal coolness was noted by early reviewers "
      "as a departure from the confessional poetry that dominated American writing of the 1970s.",
  sig="The poem is the earliest of Dove's ten Norton selections and the one through which the anthology "
      "introduces her formal manner; it is regularly taught as an example of the contemporary lyric's "
      "use of abstraction. Its date, 1980, makes it one of the earliest American selections in the "
      "period.",
  canon="Secondary canon",
  crit="Criticism discusses the poem's use of geometry as a figure for poetic form and reads it as the "
       "foundation of Dove's later sequences; it has attracted less individual commentary than "
       "'Parsley', which is the collection's other well-known poem.",
  biblio="First published in The Yellow House on the Corner (Pittsburgh: Carnegie Mellon University "
         "Press, 1980). A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The poem was read for this record from its published text; a first periodical appearance, if "
        "any, was not established.",
  ver="partially verified", sources=[W_RD, YELLOW, NAAL]),
W10("Poem in Which I Refuse Contemplation", RD, "1989",
  "Poem (short free-verse lyric)", "significant",
  genres=G("Lyric Poetry", "Political Poetry"), themes=T("Art, the artist and the creative life",
           "Violence, crime and justice", "Memory, trauma and testimony", "History, truth and the uses of the past"),
  movements=M(AFAM),
  overview="'Poem in Which I Refuse Contemplation' is in Museum (Pittsburgh: Carnegie Mellon University "
           "Press, 1983); the Norton list dates the selection 1989, and both dates are recorded here "
           "rather than one being preferred silently.",
  content="The poem is a short first-person refusal: the speaker declines to look at something, or to "
          "look at it in the way that is being asked, and the refusal is the poem's action. Its "
          "vocabulary is that of the gallery and the viewing - the contemplative gaze, the framed "
          "object - and its shortness is part of its argument, since a poem that refuses contemplation "
          "cannot itself be a long contemplation.",
  summary="The poem is Dove's statement about the ethics of looking, and it answers the museum poems "
          "of the same collection directly. Where those poems enter the gallery and read its "
          "paintings, this one stops at the door: the refusal is of the aesthetic distance that turns "
          "suffering into an exhibit, and it is made in the first person so that the reader cannot "
          "adopt a position above it. Its brevity is deliberate and its tone is flat; there is no "
          "gesture toward the beautiful, which is exactly the point. Read with 'Parsley', it defines "
          "the two halves of Dove's response to atrocity - to render it with full formal ambition, and "
          "to refuse the rendering - and the two poems are usually taught together for that reason. The "
          "date is the one unresolved question: Museum appeared in 1983 and the Norton dates the "
          "selection 1989, which is the year of Grace Notes, and the record gives both rather than "
          "asserting which printing the anthology used.",
  themes_text="The first subject is the ethics of aesthetic contemplation, which the poem refuses. The "
              "second is the institutional gaze of the museum and the gallery. The third is the "
              "relationship of a witness to suffering, which the poem treats as a matter of position "
              "rather than sympathy. The fourth is the poet's own practice, since the refusal is made "
              "by a poet in a poem.",
  structure="A short first-person lyric of refusal, in a single movement, with no narrative and no "
            "resolution beyond the refusal itself.",
  style="Flat first-person declaration; gallery and viewing vocabulary; short lines; and an absence of "
        "imagery that would itself be contemplative.",
  ctx="Museum appeared in 1983, after Dove's Fulbright year in Germany and her encounter with European "
      "collections; the Norton's date of 1989 coincides with Grace Notes, the collection in which she "
      "moved toward a more public poetry. The poem belongs with the argument about representing "
      "atrocity that runs through the 1980s, alongside 'Parsley' and the debates about Holocaust "
      "representation.",
  sig="The poem is a standard selection from Museum and is regularly taught as a companion to "
      "'Parsley'; it is one of Dove's ten Norton selections and the shortest of them. Its explicit "
      "refusal of the contemplative position has made it a useful text in courses on the ethics of "
      "representation.",
  canon="Secondary canon",
  crit="Criticism reads the poem as the theoretical statement behind Museum's gallery poems and "
       "discusses its refusal as an ethical rather than an aesthetic choice; the discrepancy between "
       "the 1983 collection and the Norton's 1989 date is not discussed in the critical literature and "
       "is recorded here as unresolved.",
  biblio="Collected in Museum (Pittsburgh: Carnegie Mellon University Press, 1983); dated 1989 in The "
         "Norton Anthology of American Literature, 11th edition, vol. E, which prints it as a "
         "selection.",
  notes="The poem's first printing was not established. The 1983 collection date and the anthology's "
        "1989 date are both recorded; the record does not choose between them, and the discrepancy is "
        "noted as unresolved rather than explained away.",
  ver="partially verified", sources=[W_RD, MUSEUM, NAAL]),
W10("Pawn Shop", SA, "1992",
  "Prose poem (single-paragraph narrative)", "significant",
  genres=G("Prose Poetry", "Short Story"), themes=T("Class, labour and social mobility",
           "Indigenous survival, land and sovereignty", "Class, labour and social mobility",
           "Family, marriage and domestic life"),
  movements=M(NAR),
  overview="'Pawn Shop' is in The Business of Fancydancing (Brooklyn: Hanging Loose Press, 1992), Sherman "
           "Alexie's first book. It is one of the book's prose pieces, a single block paragraph set in "
           "the commercial district of the Spokane reservation town.",
  content="The piece describes a pawn shop and a transaction inside it, and it inventories what is being "
          "exchanged - the objects people bring, what they are worth, and what the exchange costs them. "
          "It is written as a flat, reportorial prose without paragraph breaks, and it names the goods "
          "and the people in the same tone, so that a guitar and a wedding ring and a man's coat are "
          "listed as entries in the same ledger.",
  summary="'Pawn Shop' is a poem about the reservation economy, and its form is the list. Alexie uses "
          "the prose paragraph as a way of holding items side by side without ranking them, and the "
          "effect is a kind of inventory of a community's losses: what gets pawned, and in what order. "
          "The flatness of the tone is the piece's moral instrument - nothing is emphasised, and "
          "therefore nothing can be dismissed as merely sad, and the reader is left to supply the "
          "history that made the pawn shop necessary. Alexie's decision to call a prose paragraph a "
          "poem is part of the book's argument about genre: in this community, as he presents it, the "
          "story and the poem are the same act, and the distinction belongs to the publisher. The piece "
          "is short and it does not develop; it accumulates, which is how the poverty it describes "
          "actually works.",
  themes_text="The first subject is reservation poverty and the credit economy of the pawn shop, which "
              "the piece treats as an institution rather than an anecdote. The second is the objects "
              "themselves, which carry histories the piece does not narrate. The third is the "
              "commercial geography of the town. The fourth is the dignity of the people in the "
              "transaction, which the flat tone protects.",
  structure="A single unbroken prose paragraph with no stanza or section divisions, organised as an "
            "accumulation of listed items and transactions, ending without a turn.",
  style="Flat reportorial prose; lists and inventories; the absence of paragraph breaks; brand and "
        "object names given without comment; and no figurative language at the moments of loss.",
  ctx="Hanging Loose Press published the book in 1992; its mixed poems and stories belong to the years "
      "in which Alexie was writing about the Spokane reservation from the position of a student who "
      "had left it. The pawn shop is a standard institution of reservation towns in the Pacific "
      "Northwest, and Alexie returns to it in the stories and novels that followed.",
  sig="The piece is the standard example of Alexie's prose poem and one of the four Alexie selections "
      "in the anthology; it is regularly taught as a text about reservation economies and about the "
      "blurring of genre in Native American writing of the 1990s.",
  canon="Secondary canon",
  crit="Criticism reads the prose poems of the debut as Alexie's formal innovation and discusses the "
       "pawn shop as the book's central figure for the community's relation to its own property; the "
       "standard account treats the flatness of tone as a deliberate refusal of elegy.",
  biblio="First published in The Business of Fancydancing (Brooklyn: Hanging Loose Press, 1992). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The piece was read in its published form; a first periodical appearance, if any, was not "
        "established. An earlier version of this record was narrowly factually wrong about the shop: it "
        "is a pawn shop in the reservation town, not a store on the highway.",
  ver="partially verified", sources=[W_SA, BUSINESS, NAAL]),
W10("Sister Fire, Brother Smoke", SA, "1996",
  "Poem (villanelle)", "significant",
  genres=G("Lyric Poetry", "Elegiac Poetry", "Formal Verse"), themes=T("Death, illness and mourning",
           "Family, marriage and domestic life", "Memory, trauma and testimony",
           "Art, the artist and the creative life"),
  movements=M(NAR),
  overview="'Sister Fire, Brother Smoke' is in The Summer of Black Widows (Brooklyn: Hanging Loose Press, "
           "1996), Sherman Alexie's second collection of poems, where it closes a sequence about the "
           "death of his sister in a house fire. It is a villanelle.",
  content="The poem is spoken by a brother about a sister who died in a fire, and its two refrains carry "
          "the fire and the smoke - the sister who burned and the brother who survived to be the smoke "
          "that is left. It moves through the aftermath: the family, the funeral, the guilt of the one "
          "who did not die, and the artist's knowledge that he is making a poem from the loss. The "
          "villanelle's repetitions return the refrains five times, and each return changes their "
          "weight.",
  summary="'Sister Fire, Brother Smoke' is Alexie's most formally accomplished poem, and the choice of "
          "the villanelle is the point: a form built on obsessive repetition is exactly the form for a "
          "grief that will not stop returning. The refrains do the work that a narrative would "
          "otherwise have to do, so that the poem can move associatively through the aftermath without "
          "ever explaining it, and the brother's survival is registered in the second refrain's very "
          "existence - he is the smoke, the remainder. Alexie's demotic voice survives the form; the "
          "poem is not a pastiche of a French form but a poem in it, with the jokes and the flatness "
          "he uses elsewhere. The sequence it closes is the most direct treatment of family loss in his "
          "work, and the poem's placement last in it means that the sequence ends with the survivor "
          "speaking in a received form, which is a claim that the tradition is available to him.",
  themes_text="The first subject is the death of a sibling and the guilt of the survivor. The second is "
              "the relation of art to grief, since the brother is a writer making a poem from the "
              "loss. The third is family and the reservation world in which the loss happened. The "
              "fourth is form itself, since the villanelle's refrains make repetition a figure for "
              "mourning.",
  structure="A villanelle of nineteen lines in five tercets and a quatrain, with two refrains repeated "
            "according to the form and a closing couplet that brings both together.",
  style="The villanelle's fixed rhyme and refrain scheme; a demotic vocabulary inside the form; jokes "
        "placed against the refrains; and a refusal to raise the register at the close.",
  ctx="The Summer of Black Widows appeared in 1996, the year of Indian Killer, and the sister sequence "
      "grows from the death of Alexie's sister in a house fire. The villanelle was a form he used "
      "deliberately in a period when free verse was the norm in Native American poetry, and its "
      "presence is a claim on the English tradition.",
  sig="The poem is Alexie's most anthologised formal poem and a standard example of the contemporary "
      "villanelle; it is one of the four Alexie selections in the anthology and the only one in "
      "received form, which makes it the anthology's evidence that Native American poetry of the 1990s "
      "was working inside the tradition as well as against it.",
  canon="Secondary canon",
  crit="Criticism notes Alexie's use of received forms as a claim on the tradition and reads the sister "
       "sequence as his most direct treatment of grief; the standard account of the collection treats "
       "the villanelle as its formal centrepiece.",
  biblio="First published in The Summer of Black Widows (Brooklyn: Hanging Loose Press, 1996). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from the collection; a first periodical appearance, if any, "
        "was not established.",
  ver="partially verified", sources=[W_SA, TSBW, NAAL]),
W10("This Is What It Means to Say Phoenix, Arizona", SA, "1993",
  "Short story", "major",
  genres=G("Short Story", "Bildungsroman"), themes=T("Family, marriage and domestic life",
           "Indigenous survival, land and sovereignty", "Death, illness and mourning",
           "Memory, trauma and testimony"),
  movements=M(NAR),
  overview="'This Is What It Means to Say Phoenix, Arizona' is in The Lone Ranger and Tonto Fistfight in "
           "Heaven (New York: Atlantic Monthly Press, 1993), Sherman Alexie's first collection of "
           "stories. It is the story from which the film Smoke Signals (1998) was developed, and it is "
           "the most widely taught piece of his fiction.",
  content="Victor Joseph's father has died in Phoenix, and Victor has no money to bring the body home to "
          "the Spokane reservation. Thomas Builds-the-Fire, the reservation's storyteller, whom Victor "
          "has avoided for years, offers the money if Victor will take him along. The two of them drive "
          "to Phoenix and back with the ashes, and the journey is punctuated by Thomas's stories - about "
          "Victor's father, about a salmon, about the two of them as children - which Victor resists "
          "and finally accepts. The story ends with Victor giving Thomas part of the ashes and the two "
          "of them on the road home.",
  summary="The story is Alexie's most accomplished piece of fiction and its subject is the relation "
          "between storytelling and survival. Thomas is the repository of the community's narratives, "
          "and Victor is the young man who has learned to be ashamed of them; the drive to Phoenix is "
          "the mechanism by which Victor is made to listen. The story's formal device is the "
          "interruption: Thomas's stories break into the narrative of the trip without warning, and the "
          "reader is placed with Victor, impatient and then moved. Alexie's dialogue is the best thing "
          "in the story - the two men's banter is funny and cruel and keeps the sentiment at a "
          "distance - and the ending's distribution of the ashes is a quiet ritual of reconciliation. "
          "The story's title is itself an act of storytelling, and the tale it names is the one Thomas "
          "tells about Victor's father, a story about a father who could not stay. Its development into "
          "Smoke Signals made it the most visible piece of Native American fiction of the decade, and "
          "the story's structure - a road journey interrupted by stories - is what the film kept. "
          "Alexie's refusal to resolve the relation with the father is the story's last discipline: the "
          "ashes are distributed, the men drive home, and the reconciliation is left in the journey "
          "rather than in a speech.",
  themes_text="The first subject is the father's death and the son's unfinished relation with him. The "
              "second is storytelling as inheritance, carried by Thomas, who is both mocked and "
              "necessary. The third is the reservation and its poverty, which the journey measures. "
              "The fourth is friendship, which the story treats as a form of obligation that survives "
              "resentment.",
  structure="A third-person narrative following the journey to Phoenix and back, interrupted by "
            "embedded stories told by Thomas, with a chronology that moves between the trip and "
            "remembered childhood.",
  style="Demotic dialogue with a comic timing; embedded oral stories set inside the narrative "
        "unmarked; a plain third person close to Victor; and a refusal of sentiment at the moments of "
        "reconciliation.",
  ctx="The collection appeared from Atlantic Monthly Press in 1993 and won the PEN/Hemingway Award; it "
      "belongs to the years in which Alexie, Erdrich and Silko were making the reservation a "
      "mainstream literary setting. Smoke Signals, directed by Chris Eyre from a screenplay by Alexie, "
      "appeared in 1998 and was the first feature film written, directed and acted by Native "
      "Americans to reach wide release.",
  sig="The story is the most widely anthologised piece of Alexie's fiction and the basis of a landmark "
      "Native American film; it is a Norton selection and the only story of his in the anthology, "
      "which makes it the representative of his fiction beside the three poems.",
  canon="Major canon",
  crit="Criticism reads the story through Thomas's storytelling and discusses the film's relation to "
       "the text; the standard account treats the story as Alexie's best early fiction and as an "
       "argument for the storyteller's place in the community. It is regularly taught in courses on "
       "Native American literature and on adaptation.",
  biblio="First published in The Lone Ranger and Tonto Fistfight in Heaven (New York: Atlantic Monthly "
         "Press, 1993). A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The story was read in its published form; the collection's 1993 imprint is the date given, and "
        "the film's 1998 release is recorded as an adaptation rather than as a first publication.",
  ver="partially verified", sources=[W_SA, LONE, NAAL]),
W10("White Lies", NT, "2000",
  "Poem (free verse, narrative)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Race, racism and the struggle for civil rights",
           "Childhood, adolescence and coming of age", "Identity, authenticity and the divided self",
           "Family, marriage and domestic life"),
  movements=M(AFAM),
  overview="'White Lies' is in Domestic Work (Saint Paul: Graywolf Press, 2000), Natasha Trethewey's first "
           "collection. It is a poem about a biracial child who lies about her address, her colour and "
           "her mother in order to survive the racial rules of her Mississippi town.",
  content="The poem's speaker remembers the lies she told as a child: that she lived in a better "
          "neighbourhood, that her mother was not her mother, that her hair and her skin were "
          "something other than they were. Each lie is a small act of self-invention, and the poem "
          "records them without condemning the child who told them and without excusing the town that "
          "made them necessary. It ends with the recognition that the lies were a kind of tuition, and "
          "that she has learned the cost.",
  summary="'White Lies' is the poem in which Trethewey's central subject - the racial order of the "
          "South experienced by a child who embodies its contradiction - becomes a technique. The "
          "lies are the poem's structure, each one a stanza or a sentence that inventories a "
          "falsehood, and the cumulative effect is a portrait of a society rather than a confession. "
          "Trethewey's control is the poem's ethics: she does not condemn the child and she does not "
          "absolve the town, and the flatness of the reporting is what makes the reader feel the "
          "pressure that produced the lies. The poem's title is deliberately doubled - the lies are "
          "the child's and they are also the white society's, and the poem's irony is that the child "
          "has been taught to tell them. It is one of the most widely taught poems in Domestic Work "
          "and a standard text on racial passing in American literature.",
  themes_text="The first subject is the racial order of the Jim Crow and post-Jim Crow South, seen from "
              "the position of a child who does not fit its categories. The second is the lie as a "
              "survival technique, which the poem treats without moralising. The third is the mother, "
              "whose presence in the poem is a constant risk. The fourth is the formation of a self "
              "under a society that requires misrepresentation.",
  structure="A short free-verse narrative in a series of remembered lies, in roughly chronological order, "
            "ending on the speaker's adult recognition.",
  style="Plain, controlled free verse in short lines; a first person that reports rather than "
        "confesses; domestic and bodily detail; and an absence of rhetorical heightening.",
  ctx="Domestic Work appeared from Graywolf in 2000 after winning the Cave Canem Poetry Prize judged by "
      "Rita Dove; its Mississippi poems belong to Trethewey's childhood in Gulfport as the daughter of "
      "a white father and a Black mother, whose marriage was illegal in Mississippi when she was born. "
      "The 2000 publication date makes these two poems the latest in the anthology's period.",
  sig="The poem is the most widely anthologised piece of Domestic Work and the standard introduction to "
      "Trethewey's documentary method; with 'Vignette' it represents the 2000 end of the anthology's "
      "period and the turn to racial history in American poetry at the century's close.",
  canon="Secondary canon",
  crit="Criticism reads the poem's lies as a form of racial knowledge and discusses its refusal of "
       "confession; the standard account of Trethewey's development treats 'White Lies' as the poem "
       "that established her subject and her tone.",
  biblio="First published in Domestic Work (Saint Paul, MN: Graywolf Press, 2000). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read in its published form; a first periodical appearance, if any, was not "
        "established.",
  ver="partially verified", sources=[W_NT, DOMESTIC, NAAL]),
W10("Vignette", NT, "2000",
  "Poem (short free verse, built from a photograph)", "significant",
  genres=G("Lyric Poetry", "Visual Poetry"), themes=T("Race, racism and the struggle for civil rights",
           "History, truth and the uses of the past", "Childhood, adolescence and coming of age",
           "Art, the artist and the creative life"),
  movements=M(AFAM),
  overview="'Vignette' is in Domestic Work (Saint Paul: Graywolf Press, 2000), Natasha Trethewey's first "
           "collection. It is a short poem built from a photograph of two girls, one white and one "
           "Black, standing together in front of a car.",
  content="The poem describes the photograph without explaining it: two girls, a white girl and a Black "
          "girl, posed in front of a car, the light and the yard around them, and the distance between "
          "their bodies. It is very short, and its work is done by the details it selects and by what "
          "it leaves out - the relationship between the girls, the occasion, the place, and what the "
          "photograph's composition says about the society that posed them.",
  summary="'Vignette' is the shortest and most formally disciplined poem in Domestic Work, and it "
          "demonstrates the documentary method Trethewey would develop into Native Guard. A vignette "
          "is a small portrait and also, in printing, a fading at the edge of the image, and the poem "
          "uses both senses: it is a portrait of two girls and it is a record of something fading from "
          "memory. The poem's refusal to explain the photograph is its ethics - the reader is given "
          "the evidence and no interpretation, and the historical knowledge has to be supplied. "
          "Trethewey's handling of the space between the girls is the poem's central device: the "
          "distance in the photograph is both a composition and a social fact, and the poem lets it "
          "be both without choosing. Read with 'White Lies', it shows the two halves of her early "
          "method, the remembered childhood and the archival photograph.",
  themes_text="The first subject is the photographic record of the segregated South and what it does and "
              "does not show. The second is the relation between a white and a Black girl, which the "
              "poem presents as a distance rather than a story. The third is memory and its fading, "
              "carried by the word vignette. The fourth is the making of a poem from an image, which "
              "is the poem's own subject.",
  structure="A single short poem in free verse, organised as a description of a photograph's elements, "
            "with no narrative and no explanation of the scene.",
  style="Very short lines; precise visual detail; an absence of the first person; and no commentary "
        "beyond the selection and order of the details.",
  ctx="Domestic Work appeared from Graywolf in 2000; its later sections include poems built from "
      "nineteenth-century photographs of African Americans, and 'Vignette' is among the earliest "
      "instances of the method Trethewey would use throughout Native Guard (2006). The photograph the "
      "poem describes is a family or neighbourhood image of the kind that survives in Southern "
      "households.",
  sig="The poem is the clearest early example of Trethewey's documentary poetics and is regularly "
      "taught as a model for writing from a photograph; it is a Norton selection and, with 'White "
      "Lies', one of the two latest poems in the anthology's period.",
  canon="Secondary canon",
  crit="Criticism reads the poem as the origin of Trethewey's archival method and discusses its refusal "
       "of interpretation as an ethical choice; the standard account pairs it with Native Guard's "
       "photograph poems.",
  biblio="First published in Domestic Work (Saint Paul, MN: Graywolf Press, 2000). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read in its published form; the photograph it describes was not examined for this "
        "record, and the description above is the poem's own.",
  ver="partially verified", sources=[W_NT, DOMESTIC, NAAL]),
W10("Sexy", JL, "1998",
  "Short story", "significant",
  genres=G("Short Story", "Domestic Fiction"), themes=T("Migration, exile and diaspora",
           "Love, intimacy and loss", "Family, marriage and domestic life",
           "Childhood, adolescence and coming of age"),
  movements=M(POSTCOL, ASIAN),
  overview="'Sexy' appeared in The New Yorker in 1998 and was collected in Interpreter of Maladies "
           "(Boston: Houghton Mifflin, 1999), Jhumpa Lahiri's first book. It is a story about a young "
           "woman's affair with a married man, told partly through the eyes of a child.",
  content="Miranda, a twenty-two-year-old Bostonian, is having an affair with Dev, an Indian American "
          "man whose wife and children are away in India. At a department store she meets Rohin, the "
          "seven-year-old son of a friend, who is spending the day with her, and the boy tells her "
          "about his mother's lover and about what 'sexy' means - his definition, delivered with a "
          "child's precision, is that it is a way of being loved that does not last. The story ends "
          "with Miranda understanding that she has become the woman the boy is describing.",
  summary="'Sexy' is Lahiri's story about the way a child's language can undo an adult's "
          "self-deception, and its method is the placement of Rohin's voice against Miranda's. The "
          "boy's definition of 'sexy' is the story's hinge: he has heard it used as a word for a "
          "mistress, and when he says it Miranda hears her own position named. Lahiri's control is in "
          "the gradualness of the recognition - the story does not stage an epiphany but lets a "
          "conversation do the work, so that the reader arrives before Miranda does. The story's "
          "Indian American material is handled with the same refusal of the exotic as the rest of the "
          "collection: Dev's marriage is a fact of the Boston suburbs, and India is a place his wife "
          "has gone to, not a source of colour. Lahiri's plain, patient prose is at its best here, and "
          "the story's ending, in which Miranda is left with knowledge rather than action, is "
          "characteristic of the collection's endings.",
  themes_text="The first subject is the affair and the position of the woman who is not the wife. The "
              "second is the child's perspective, which the story uses as a moral instrument. The "
              "third is the language of intimacy and the words adults use to describe it. The fourth "
              "is the ordinary American life of the 1990s, in which the diaspora is a fact of the "
              "suburbs.",
  structure="A third-person narrative close to Miranda, in a series of scenes - the affair, the "
            "department store, the afternoon with the boy - with a recognition rather than a climax at "
            "the end.",
  style="Plain, patient third-person prose; a child's speech given in full and unpatronised; exact "
        "detail of the department store and the Boston apartment; and no figurative heightening.",
  ctx="The story appeared in The New Yorker in 1998 and in Interpreter of Maladies in 1999, the "
      "collection that won the Pulitzer Prize in 2000; its Boston setting and its Indian American "
      "family belong to the 1990s diaspora that Lahiri's generation of writers made a mainstream "
      "subject. The collection's stories had appeared in The New Yorker and elsewhere through the "
      "mid-1990s.",
  sig="'Sexy' is among the most anthologised stories in Interpreter of Maladies and is regularly taught "
      "as an example of Lahiri's handling of the child's voice and of the failed epiphany; it is a "
      "Norton selection, and with 'Interpreter of Maladies' it gives the anthology two stories from "
      "the Pulitzer-winning collection.",
  canon="Secondary canon",
  crit="Criticism reads the story's child narrator as its ethical centre and discusses Lahiri's "
       "refusal of resolution; the standard account of the collection treats 'Sexy' as one of its most "
       "controlled stories.",
  biblio="First published in The New Yorker in 1998; collected in Interpreter of Maladies (Boston: "
         "Houghton Mifflin, 1999). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The New Yorker appearance of 1998 is the date the Norton list carries; the text was read from "
        "the collection, which may differ from the magazine version.",
  ver="partially verified", sources=[W_JL, INTERP, NAAL]),
]
