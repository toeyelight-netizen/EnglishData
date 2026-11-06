"""Installment 10, wave 27: Sylvia Plath, the eight selections of the American anthology.

One new author and eight works, one record per Norton selection. Wave 27 also
dates the whole Plath block: the list carried all eight as "written 1961-1963"
with no first-publication date, which left them outside the audit's dated set.

Dates settled here (see the record notes and the list rows for the basis):

    Morning Song        1961  book: Ariel (Faber, 1965)
    Blackberrying       1962  first printing: The New Yorker, 15 September 1962
    The Applicant       1963  first printing: The London Magazine, January 1963
    Lady Lazarus        1965  book: Ariel (Faber, 1965)
    Ariel               1965  book: Ariel (Faber, 1965)
    Daddy               1965  book: Ariel (Faber, 1965)
    Words               1965  book: Ariel (Faber, 1965)
    Child               1971  book: Winter Trees (Faber, 1971)

Composition dates, from the manuscripts at Smith College and the appendix to
Ariel: The Restored Edition: Morning Song 19 February 1961; Blackberrying
23 September 1961; The Applicant 11 October 1962; Daddy 12 October 1962; Ariel
27 October 1962; Lady Lazarus 23-29 October 1962; Child 28 January 1963; Words
1 February 1963.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

SP = "Sylvia Plath"

CONF = "Confessional Poetry"
SWF = "Second-Wave Feminist Writing"

W_SP = "Sylvia Plath (Wikipedia)"
W_SPB = "Sylvia Plath bibliography (Wikipedia)"
W_ARIEL = "Ariel, poetry collection (Wikipedia)"
W_COL = "The Colossus and Other Poems (Wikipedia)"
W_REST = "Ariel: The Restored Edition, appendix of composition dates"
W_PF_MS = "Morning Song (Poetry Foundation poem page)"
W_PF_BB = "Blackberrying (Poetry Foundation poem page)"
W_PF_APP = "The Applicant (Poetry Foundation poem page)"
W_PF_LL = "Lady Lazarus (Poetry Foundation poem page)"
W_PF_AR = "Ariel (Poetry Foundation poem page)"
W_PF_DA = "Daddy (Poetry Foundation poem page)"
W_NY_BB = "Blackberrying, The New Yorker, 15 September 1962 (newyorker.com archive)"
W_INDEX = "Index of Works by Sylvia Plath (sylviaplath.info)"
W_WT = "Winter Trees, first edition (Faber and Faber, 1971), bookseller records"
W_BRIT = "Ariel (Britannica entry)"

AUTHORS = [
A10(SP, MAJ, "1932", "1963", "Boston, Massachusetts, United States",
  "American; poet, novelist and short-story writer writing in English",
  "American poet whose posthumous Ariel (1965) and The Collected Poems (1981) made her the central "
  "confessional poet of the postwar period and the most discussed woman poet of the twentieth century",
  "Sylvia Plath was born in the Jamaica Plain district of Boston on 27 October 1932, the daughter of "
  "Otto Plath, a German-born professor of biology at Boston University, and Aurelia Schober Plath, a "
  "teacher of Austrian descent. Her father died in November 1940, when she was eight, and the grief and "
  "anger of that loss became the matter of her best-known poem nineteen years later. She grew up in "
  "Wellesley, wrote and published precociously, won a scholarship to Smith College, and in 1953, after a "
  "month in New York as a guest editor at Mademoiselle, suffered the first of the breakdowns and suicide "
  "attempts that The Bell Jar (1963) describes. She returned to Smith, graduated summa cum laude in 1955, "
  "and took a Fulbright to Newnham College, Cambridge, where she met the poet Ted Hughes; they married in "
  "June 1956. After two years teaching at Smith she and Hughes moved back to England, and in 1960, after "
  "the birth of their daughter Frieda, Heinemann published The Colossus and Other Poems, the only "
  "collection of her poetry to appear in her lifetime. In 1961 they settled at Court Green in North "
  "Tawton, Devon, where their son Nicholas was born; in the autumn of 1962, after Hughes's affair with "
  "Assia Wevill, the marriage broke up and Plath moved with the children to a flat in Fitzroy Road, "
  "London. In the last five months of her life she wrote at extraordinary speed - the poems of October "
  "and November 1962, including 'Daddy', 'Lady Lazarus', 'Ariel' and 'The Applicant', and the winter poems "
  "'Child' and 'Words' - and in January 1963 published The Bell Jar under the pseudonym Victoria Lucas. "
  "She died by suicide in London on 11 February 1963, aged thirty, and is buried at Heptonstall in West "
  "Yorkshire. Ariel appeared in 1965 in a text arranged by Hughes, who reordered the manuscript and added "
  "poems; Ariel: The Restored Edition (2004) printed her own selection and sequence for the first time. "
  "The Collected Poems (1981), also edited by Hughes, won the Pulitzer Prize for Poetry in 1982, the first "
  "awarded posthumously to a poet.",
  "Poetry: The Colossus and Other Poems (1960), Ariel (1965), Uncollected Poems (1965), Crossing the "
  "Water (1971), Winter Trees (1971), The Collected Poems (1981, Pulitzer Prize 1982), Selected Poems "
  "(1985) and Ariel: The Restored Edition (2004). Novel: The Bell Jar (1963, as Victoria Lucas). Prose "
  "and letters: Letters Home (1975), Johnny Panic and the Bible of Dreams (1977), The Journals of Sylvia "
  "Plath (1982), The Unabridged Journals (2000) and The Letters of Sylvia Plath (2 vols, 2017-2018). "
  "Children's books: The Bed Book (1976) and The It-Doesn't-Matter Suit (1996).",
  "Short stanzas, usually tercets, quintains or loose quatrains, with lines that run over the stanza "
  "break and a rhyme that is heard in the vowel rather than at the line end; a diction that moves without "
  "warning between the nursery and the clinic, the lyric and the obscene; a first person that is at once "
  "exhibitionistic and defensive; repetition and refrain used as a formal device, as in 'Daddy' and 'Lady "
  "Lazarus'; the homeliest domestic object - a watch, a shoe, a telephone, a paperweight - made to carry "
  "the whole weight of the poem.",
  "The father as the dead origin of speech; the wish to die and the theatrical refusal to stay dead; "
  "motherhood, childbirth and the body as the site of another's life; marriage, betrayal and the "
  "humiliation of dependence; the Holocaust and the concentration camp as figures for domestic power; "
  "the English and American landscape as an image of the mind; the materials of a woman's art - sewing, "
  "cooking, beekeeping, riding, drawing - turned into the machinery of vision.",
  "Plath is the poet through whom confessional poetry and the literature of the 1960s are taught, and "
  "'Daddy', 'Lady Lazarus' and 'Ariel' are among the most anthologised and most argued-over poems of the "
  "century. Her posthumous reputation - the Pulitzer of 1982, the biographies, the controversy over the "
  "editing of Ariel, the part she plays in feminist criticism from the 1970s onward - has made her a case "
  "study in the making of a literary reputation as well as a body of work, and her influence on later "
  "women poets in English is acknowledged almost everywhere it is discussed.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Sylvia Plath, on Ariel and on "
           "The Colossus and Other Poems, which agree with the contents list of The Collected Poems and "
           "with the dates of composition established from the manuscripts at Smith College and printed "
           "in the appendix to Ariel: The Restored Edition; they were not checked against a printed "
           "bibliography. Installment 10 records the eight Norton selections - 'Morning Song', 'Lady "
           "Lazarus', 'Ariel', 'Daddy', 'Words', 'Blackberrying', 'The Applicant' and 'Child' - so the "
           "other poems, the novel, the stories, the letters and the journals have no records, and the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_SP, W_SPB, W_ARIEL, W_COL, W_REST, W_PF_MS, NAAL]),
]

WORKS = [
W10("Morning Song", SP, "1961", "Poem (six tercet stanzas in free verse)", "major",
  genres=G("Confessional Poetry", "Lyric Poetry", "Free Verse"),
  themes=T("Family, marriage and domestic life", "Gender, feminism and women's lives",
           "Identity, authenticity and the divided self"),
  movements=M(CONF),
  overview="'Morning Song' is the poem with which Ariel opens, written on 19 February 1961, ten months "
           "after the birth of Plath's daughter Frieda, and first collected in Ariel (Faber and Faber, "
           "1965). Six tercets follow a mother through the first hours of a night with a new baby: the "
           "child's cry, the mother's stumbling from bed, the window whitening towards morning, and the "
           "infant's 'handful of notes' rising 'like balloons'. It is the tenderest poem in the book and "
           "the one that most exactly states the book's argument about the self, since the mother "
           "announces that she is 'no more your mother / Than the cloud that distills a mirror to reflect "
           "its own slow / Effacement at the wind's hand'.",
  content="The poem begins in the register of an address to the newborn: 'Love set you going like a fat "
          "gold watch. / The midwife slapped your footsoles, and your bald cry / Took its place among the "
          "elements.' The second tercet answers the birth with a museum: 'New statue', the child's "
          "nakedness in a drafty museum, the family standing 'round blankly as walls'. The third rejects "
          "the title of mother in the metaphor of the cloud and the mirror, and the fourth turns to the "
          "night feeding, the baby's 'moth-breath' flickering 'among the flat pink roses', the mother "
          "waking to listen and hearing 'a far sea'. The fifth is the physical comedy of the nursing "
          "mother: 'One cry, and I stumble from bed, cow-heavy and floral / In my Victorian nightgown'; "
          "the baby's mouth opens 'clean as a cat's', the window whitens and swallows its dull stars. The "
          "last tercet gives the child the poem's title and its closing image: 'And now you try / Your "
          "handful of notes; / The clear vowels rise like balloons.'",
  summary="'Morning Song' works by refusing the two obvious poems about a newborn - the lullaby and the "
          "confession of maternal inadequacy - and writing a third, in which the mother is a medium rather "
          "than an origin. Its movement is from sound to sound: the 'bald cry' of the first stanza, the "
          "echoing voices of the second, the 'moth-breath' and the 'far sea' of the fourth, and at last "
          "the child's own 'handful of notes'. Between them Plath places three images of detachment: the "
          "watch that love winds up, the statue in the museum, and the cloud that distils a mirror only to "
          "efface itself. The mother's body is then given back to her in the fifth stanza as something "
          "comic and animal - 'cow-heavy and floral' - and the poem's final gesture is generous because it "
          "is not sentimental: the child's vowels are balloons because they rise, and because they are "
          "loosed from the hand that made them. The tercets are unrhymed but not shapeless; the line "
          "breaks fall in the middle of phrases, so that each stanza ends on an image rather than a "
          "statement, and the whole poem has the even, forward tread of a song sung while walking. It is "
          "worth noticing how little the poem asks of the reader: there is no allusion to decode, no "
          "proper name, and the only difficulty is the emotional one of a mother who says she is not a "
          "mother. The three images of detachment do the work that a confessional poem would do with "
          "confession - the watch, the statue and the cloud - and each of them is an image of something "
          "made and then left behind, which is what the poem thinks a child is, and what it fears a poem "
          "is too.",
  themes_text="The poem's first subject is the making of a self: the mother is not the origin of the "
              "child but a reflecting surface that empties as the child fills, and the poem finds this "
              "neither tragic nor consoling but simply true. Its second subject is the ordinary labour of "
              "infancy - the night feeding, the stumble from bed, the milk-heavy body - recorded without "
              "either the idealisation of the Madonna or the self-pity that confessional writing is "
              "often accused of. The third is sound as the child's first act of ownership: the poem "
              "moves from the cry that 'took its place among the elements' to the clear vowels that rise, "
              "and in doing so it makes the baby's voice the poem's own medium. Read against the rest of "
              "Ariel, 'Morning Song' is the book's ground bass: the poems that follow - 'Lady Lazarus', "
              "'Daddy', 'Ariel' itself - are all songs sung by a voice that has learned, here, to be "
              "loosed from the body that made it.",
  structure="Six unrhymed tercets, each a complete sentence or a pair of sentences, with the line running "
            "on across the stanza break; the poem moves from birth (stanzas one to three) to night "
            "feeding (four and five) to dawn (six), and its last line is the shortest and the only one "
            "that names the child's utterance as the poem's subject.",
  style="Free verse tercets with a loose, predominantly iambic tread and occasional rhyme heard inside "
        "the line ('watch' / 'slapped', 'floral' / 'cat's'); a diction that mixes the nursery ('fat gold "
        "watch', 'balloons') with the laboratory and the museum ('elements', 'statue', 'distills a "
        "mirror'); similes drawn from animals and weather; and a syntax that keeps the mother's 'I' in "
        "subordinate clauses, so that the child's cry has the grammatical initiative.",
  ctx="Written on 19 February 1961 at Court Green, North Tawton, ten months after the birth of Frieda "
      "Plath on 1 April 1960, and two months after Plath had suffered a miscarriage (the subject of "
      "'Barren Woman', written two days later). It was first collected as the opening poem of Ariel "
      "(London: Faber and Faber, 1965), in the text arranged by Ted Hughes after her death; the restored "
      "edition of 2004 keeps it in first place, where Plath herself had put it. Plath had read Robert "
      "Lowell's Life Studies in 1959 and studied in his Boston University seminar with Anne Sexton; the "
      "domestic intimacies of 'Morning Song' belong to the moment when American confessional poetry and "
      "the English lyric of the 1960s met.",
  sig="'Morning Song' is the poem that opens the most influential posthumous collection in "
      "twentieth-century English poetry, and it is the standard counter-example to the idea that Plath's "
      "late work is only a literature of extremity: anthologies of motherhood, of the family and of "
      "women's writing place it beside Sexton's 'Little Girl, My String Bean' and Sylvia's own later "
      "poems, and its cloud-and-mirror stanza is one of the most quoted statements in postwar poetry "
      "about what it means to make another person.",
  canon="Major canon",
  crit="Critics have read the poem as Plath's revision of the Romantic birth ode, as a feminist "
       "rethinking of the mother as mirror rather than origin, and as the formal model for the tercet "
       "poems of October 1962; the 'fat gold watch' has been discussed as an image of the body as "
       "mechanism, and the poem's refusal of the Madonna has been set against the Marian imagery of "
       "'The Moon and the Yew Tree'. Its place in the argument about the editing of Ariel is secure: "
       "both the 1965 text and Plath's own manuscript open with it.",
  biblio="Written 19 February 1961; first collected as the opening poem of Ariel (London: Faber and "
         "Faber, 1965); reprinted in The Collected Poems (1981) and in Ariel: The Restored Edition "
         "(2004). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="No first periodical printing was established from the sources consulted; the poem is dated "
        "1961 from its composition and from its first book appearance in 1965. The British and American "
        "editions of Ariel differ in their contents and in their ordering, and the restored text of 2004 "
        "differs again from the 1965 text; the dates given here are those of the composition and of the "
        "first publication in book form.",
  ver="partially verified", sources=[W_SP, W_ARIEL, W_REST, W_PF_MS, W_BRIT, NAAL]),
W10("Blackberrying", SP, "1962", "Poem (three long free-verse stanzas)", "significant",
  genres=G("Lyric Poetry", "Free Verse", "Nature Poetry", "Pastoral and Rural Poetry"),
  themes=T("Nature, ecology and environmental crisis", "Death, illness and mourning",
           "Land, place and regional belonging"),
  movements=M(CONF),
  overview="'Blackberrying' was written on 23 September 1961 at Court Green and first published in The "
           "New Yorker of 15 September 1962, which makes it the one Norton selection of Plath's that "
           "appeared in a periodical in her lifetime and the only one with a first printing before the "
           "posthumous books. Three long unrhymed stanzas follow a walk down a lane between blackberry "
           "hedges towards a sea that may or may not appear; what begins as a nature poem about abundance "
           "turns, at the last hook of the lane, into a poem about nothing at all - 'a great space / Of "
           "white and pewter lights'.",
  content="The first stanza establishes the lane: 'Nobody in the lane, and nothing, nothing but "
          "blackberries', on either side, 'a blackberry alley, going down in hooks, and a sea / Somewhere "
          "at the end of it, heaving'. The berries are 'big as the ball of my thumb, and dumb as eyes', "
          "fat with 'blue-red juices' that squander themselves on the picker's fingers; the picker had "
          "not asked for 'such a blood sisterhood' and packs the fruit into a milk bottle. Overhead the "
          "choughs go 'in black, cacophonous flocks - / Bits of burnt paper wheeling in a blown sky', the "
          "only voice, 'protesting, protesting'; and the picker doubts the sea will appear at all. The "
          "second stanza reaches a bush so ripe it is 'a bush of flies', their blue-green bellies and wing "
          "panes hung 'in a Chinese screen', stunned by the honey of the berries into believing in "
          "heaven. The third: one more hook and the berries and bushes end; a wind funnels between two "
          "hills, slapping 'its phantom laundry' in the face; the hills are too green and sweet to have "
          "tasted salt; the sheep path leads to the hills' northern face, 'orange rock / That looks out on "
          "nothing, nothing but a great space / Of white and pewter lights, and a din like silversmiths / "
          "Beating and beating at an intractable metal'.",
  summary="The poem is built as a walk with three stages, and each stage is a different relation between "
          "the eye and what it sees. In the lane the world is all nearness and excess: the berries push "
          "themselves into the hand, stain it, and ask to be eaten or carried home, and the only sound is "
          "the picker's own; the choughs are the first warning, a voice that protests without saying what. "
          "At the flies' bush the abundance becomes a parody of communion - the insects drunk on the fruit, "
          "'they believe in heaven' - and the poem's irony is at its driest. Then the lane ends, and the "
          "third stage reverses everything: the hills are too sweet to have known the sea, the wind is a "
          "laundry slapped in the face, and the view from the northern face is not a prospect but a void. "
          "The famous last line gives that void a sound - a din 'like silversmiths / Beating and beating "
          "at an intractable metal' - which is the sound of work that will not be finished, and the poem "
          "ends there, without consolation, having travelled from plenitude to vacancy in twenty-seven "
          "lines.",
  themes_text="'Blackberrying' is a poem about appetite and its disappointment: the lane offers more than "
              "can be carried, the flies show what happens to those who take it all, and the sea that the "
              "whole walk has been aimed at is withheld. Its second subject is the English landscape as a "
              "state of mind, in which the green hills are 'too green and sweet to have tasted salt' and "
              "the only grandeur is a vacancy; Plath wrote it in Devon in the autumn after the move to "
              "Court Green, and it belongs with the garden and country poems of 1961 rather than with the "
              "Berlin and London poems of 1962. The third is sound as the trace of labour: the choughs "
              "protest, the wind slaps laundry, and the sea is not water but the noise of smiths beating "
              "an intractable metal, which is also a figure for the poem's own making.",
  structure="Three long unrhymed stanzas of nine, eight and ten lines, each a single sentence extended by "
            "commas and semicolons; the walk supplies the structure, and the repeated phrase 'nothing, "
            "nothing' at the opening and near the close marks the symmetry of the emptiness at either end.",
  style="Long free-verse lines with a heavy, list-like syntax and internal rhyming ('big as the ball of "
        "my thumb, and dumb as eyes'); a diction drawn from the kitchen, the market and the workshop; "
        "similes that turn the natural world into manufactured objects ('a Chinese screen', 'phantom "
        "laundry', 'an intractable metal'); and a refusal of the closing image that a nature poem is "
        "expected to supply.",
  ctx="Written on 23 September 1961 at Court Green, North Tawton, and published in The New Yorker for 15 "
      "September 1962, during Plath's lifetime and a few weeks before the poems of October 1962 changed "
      "her manner completely. It was not in the 1965 Ariel; it was collected in Crossing the Water (1971) "
      "and then in The Collected Poems (1981). The Devon lane, the blackberry hedges and the walk to the "
      "coast belong to the same landscape as 'Letter in November' and 'Winter Trees'.",
  sig="'Blackberrying' is the best known of Plath's English landscape poems and the one most often used "
      "to show that her gift was not confined to the confessional mode; it is a standing exhibit in "
      "discussions of postwar nature poetry, and its last line is among the most frequently quoted in her "
      "work.",
  canon="Secondary canon",
  crit="Readings have concentrated on the poem's reversal of the pastoral - the lane that leads not to a "
       "prospect but to vacancy - and on the flies' bush as a parody of the Eucharist; feminist critics "
       "have noted the 'blood sisterhood' of the berries and the milk bottle as images of the female body "
       "and of domestic labour, and ecocritical readings have placed the poem in the tradition of the "
       "English walk poem from Clare to Hughes.",
  biblio="Written 23 September 1961; first published in The New Yorker, 15 September 1962; collected in "
         "Crossing the Water (London: Faber and Faber, 1971) and reprinted in The Collected Poems (1981). "
         "A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="This is the only one of the eight Plath selections whose first printing is a periodical in her "
        "lifetime, and the 1962 date of the list is therefore the date of first publication rather than "
        "of composition.",
  ver="partially verified", sources=[W_SP, W_PF_BB, W_NY_BB, W_INDEX, NAAL]),
W10("The Applicant", SP, "1963", "Poem (eight quintains in free verse)", "major",
  genres=G("Confessional Poetry", "Dramatic Monologue", "Free Verse"),
  themes=T("Gender, feminism and women's lives", "Family, marriage and domestic life",
           "Technology, media and consumer society"),
  movements=M(CONF, SWF),
  overview="'The Applicant' was written on 11 October 1962, the day Ted Hughes left for London, and first "
           "published in The London Magazine in January 1963; it was collected in Ariel (1965). A "
           "salesman interviews a man who has come to be supplied with a wife, and the poem conducts the "
           "interview in the language of advertising and of the medical catalogue: 'Do you wear / A glass "
           "eye, false teeth or a crutch, / A brace or a hook, / Rubber breasts or a rubber crotch, / "
           "Stitches to show something's missing?' The wife, when she is produced, is 'a living doll' who "
           "'can sew, it can cook, / It can talk, talk, talk', and the poem ends with the salesman's "
           "refrain, 'Will you marry it, marry it, marry it.'",
  content="The poem is an interrogation. The first three quintains ask whether the applicant is 'our sort "
          "of a person', listing prostheses and surgical repairs in the flat tones of a form; the fourth "
          "turns to the empty hand, and the salesman fills it: 'Here is a hand / To fill it and willing / "
          "To bring teacups and roll away headaches / And do whatever you tell it. / Will you marry it?' "
          "The fifth advertises the suit the wife is compared to - 'Black and stiff, but not a bad fit', "
          "waterproof, shatterproof, 'proof / Against fire and bombs through the roof' - and promises, "
          "'Believe me, they'll bury you in it.' The sixth finds the applicant's head empty and produces "
          "'the ticket for that', then calls the wife out of the closet: 'Come here, sweetie, out of the "
          "closet.' The seventh answers the objection that she is new with the wedding anniversaries: "
          "'Naked as paper to start // But in twenty-five years she'll be silver, / In fifty, gold.' The "
          "eighth gives the catalogue of her functions - 'A living doll, everywhere you look. / It can sew, "
          "it can cook, / It can talk, talk, talk' - and the close: 'My boy, it's your last resort. / Will "
          "you marry it, marry it, marry it.'",
  summary="The poem's method is to let a commercial voice describe a marriage and never interrupt it. "
          "Everything the salesman says is true to the language of advertising - the guarantees, the "
          "materials, the anniversary schedule, the promise that the product will outlast the buyer - and "
          "the horror comes from the fit between that language and the institution it is selling. The "
          "applicant is described as damaged stock, his missing parts catalogued as disqualifications; the "
          "wife is described as stock, 'naked as paper to start', blank for the husband to fill in, and "
          "then as the ideal employee, sewing, cooking, talking, with 'nothing wrong with it'. The poem's "
          "repetitions do the work of the refrain in a ballad: 'Will you marry it' returns five times, "
          "and the closing line triples it into a threat. Plath said that she wrote the poem as light "
          "verse, and its jaunty, nursery-rhymed surface is exactly what makes it difficult to dismiss: "
          "the reader is placed in the position of the customer who is being sold the arrangement the "
          "poem is condemning. The catalogue is also a precise piece of social observation: the glass eye, the "
          "false teeth, the crutch and the rubber limbs are the stock of the postwar rehabilitation "
          "hospital, and the wife's guarantees - waterproof, shatterproof, proof against fire and bombs "
          "- are the language of the civil-defence advertisement. Plath wrote the poem the day Hughes "
          "left, and its coldest move is to give the abandoning husband no line at all: he is the "
          "customer, and the poem's satire is aimed at the market that supplies him rather than at the "
          "man who complains.",
  themes_text="The first subject is marriage as a commercial transaction, in which the wife is a "
              "manufactured object with a warranty and the husband a customer with a hole to be filled. "
              "The second is the construction of gender in the advertising of the postwar period: the poem "
              "quotes the language of the catalogue and the showroom so exactly that its satire needs no "
              "commentary. The third is the body - the glass eye, the false teeth, the rubber breasts, the "
              "stitches - which the poem treats as a set of parts that can be replaced or supplied, and "
              "which connects 'The Applicant' to the surgical imagery of 'Lady Lazarus' and 'Fever 103°'. "
              "Written the day Hughes left and a day before 'Daddy', it is also, unmistakably, a poem "
              "about the end of a marriage, though it never names one.",
  structure="Eight unrhymed quintains in the voice of the salesman, with the applicant and the wife given "
            "no speech at all; the questions of the first half ('Will you marry it?') are answered by the "
            "catalogue of the second, and the poem's only progression is the escalation of the sales "
            "pitch, from enquiry to guarantee to threat.",
  style="Short lines with a jaunty, heavily stressed rhythm close to doggerel; internal rhyme and "
        "alliteration ('Black and stiff, but not a bad fit'); diction lifted from advertising, insurance "
        "and medicine; the second person used as the salesman's instrument, so that the reader is "
        "addressed as the customer; and a refusal of metaphor in favour of the literal catalogue, which "
        "is the poem's central irony.",
  ctx="Written on 11 October 1962, the day Ted Hughes left Court Green for London, and a day before "
      "'Daddy'; first published in The London Magazine in January 1963, a month before Plath's death, and "
      "collected in Ariel (London: Faber and Faber, 1965). It belongs to the extraordinary sequence of "
      "October 1962 poems in which Plath's manner changed, and its subject - the wife as manufactured "
      "goods - belongs to the moment of Betty Friedan's The Feminine Mystique (1963) and of the postwar "
      "advertising boom that Friedan attacked.",
  sig="'The Applicant' is Plath's most sustained satire and one of the founding texts of the feminist "
      "critique of marriage in postwar poetry; it is a standard anthology piece and the poem most often "
      "taught beside 'Daddy' to show that Plath's anger could be directed outward, at an institution, "
      "rather than only inward at her own family.",
  canon="Major canon",
  crit="Critics have read the poem as a satire on the exchange of women, as a parody of the marriage "
       "plot of the women's magazines in which Plath had published, and as a verse experiment in the "
       "register of advertising; its relation to Friedan, to the 'feminine mystique' and to Plath's own "
       "marriage has been discussed at length, and its comic surface has been the subject of a running "
       "argument between readers who find it liberating and those who find it cruel.",
  biblio="Written 11 October 1962; first published in The London Magazine, January 1963; collected in "
         "Ariel (London: Faber and Faber, 1965) and reprinted in The Collected Poems (1981). A selection "
         "of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The Poetry Foundation's headnote gives the first publication as 1963 and the collection as Ariel "
        "(1965), which agrees with the London Magazine printing recorded here; the exact day of the "
        "magazine's appearance was not established from the sources consulted, and the record gives the "
        "month.",
  ver="partially verified", sources=[W_SP, W_PF_APP, W_ARIEL, W_INDEX, W_REST, NAAL]),
W10("Lady Lazarus", SP, "1965", "Poem (twenty-eight tercet stanzas in free verse)", "major",
  genres=G("Confessional Poetry", "Dramatic Monologue", "Free Verse"),
  themes=T("Death, illness and mourning", "Madness, breakdown and confinement",
           "The Holocaust, atrocity and historical memory"),
  movements=M(CONF, SWF),
  overview="'Lady Lazarus' was written between 23 and 29 October 1962 and first published in Ariel (Faber "
           "and Faber, 1965). It is a dramatic monologue spoken by a woman who has died and come back "
           "three times, addressing 'Herr Doktor', 'Herr Enemy' and finally 'Herr God, Herr Lucifer' from "
           "the stage of a public spectacle; its twenty-eight tercets end with the most quoted lines "
           "Plath wrote: 'Out of the ash / I rise with my red hair / And I eat men like air.' The poem "
           "fuses the biblical Lazarus who was raised from the dead with the myth of the phoenix and with "
           "the imagery of the concentration camp, and it is the boldest of the poems in which she made "
           "her own suffering into theatre.",
  content="The speaker begins by boasting that she has 'done it again', once every ten years, and "
          "describes herself as 'a sort of walking miracle' with skin 'bright as a Nazi lampshade' and a "
          "face 'a featureless, fine / Jew linen'. She invites the crowd to 'peel off the napkin', asks "
          "'Do I terrify?', and catalogues her body - nose, eye pits, teeth, sour breath - before "
          "promising that the flesh the grave ate will be at home on her again and she will be 'a smiling "
          "woman'. She is 'only thirty' and has, like a cat, nine times to die: 'This is Number Three.' "
          "The 'peanut-crunching crowd' shoves in to see her unwrapped 'hand and foot', the 'big strip "
          "tease'; she displays her hands and knees and insists that she is 'the same, identical woman'. "
          "The first death, at ten, was 'an accident'; the second she meant, rocking shut 'as a seashell' "
          "while they called and picked the worms off her 'like sticky pearls'. Then the poem's most "
          "famous turn: 'Dying / Is an art, like everything else. / I do it exceptionally well.' She "
          "does it 'so it feels like hell', 'so it feels real', and says, 'I guess you could say I've a "
          "call.' The comeback in broad day is 'the theatrical' - 'A miracle!' - and there is a charge "
          "for the eyeing of her scars, for the hearing of her heart, for 'a piece of my hair or my "
          "clothes'. The final movement addresses 'Herr Doktor' and 'Herr Enemy' - 'I am your opus, / I am "
          "your valuable, / The pure gold baby / That melts to a shriek' - and passes through ash and "
          "bone ('A cake of soap, / A wedding ring, / A gold filling') to the last three stanzas, in which "
          "she warns 'Herr God, Herr Lucifer' to beware and rises from the ash with her red hair to eat "
          "men like air.",
  summary="'Lady Lazarus' is a resurrection poem told from the wrong side of the miracle. Its speaker has "
          "not been restored to life but put back on display, and she understands that her deaths have "
          "made her valuable: the crowd pays to see the scars, the doctors own the case, and even God and "
          "Lucifer are addressed as rival proprietors of the exhibit. The poem's triple structure - the "
          "parade of the body, the history of three deaths, and the revenge - is held in tercets so short "
          "that each stanza lands like a beat, and the rhyme is carried by the vowel rather than by the "
          "line end, giving the whole a nursery-rhyme jauntiness that makes the horror harder to refuse. "
          "The Holocaust imagery is the most contested thing in it: the lampshade, the Jew linen, the "
          "soap and the gold filling are images of what the camps made of human bodies, and Plath uses "
          "them to describe what has been made of hers. The poem does not apologise for the comparison or "
          "explain it, and the last stanza refuses consolation altogether: the speaker does not rise into "
          "heaven but into appetite, 'and I eat men like air'. The poem's rhetoric is that of the stage, and "
          "it is worth being exact about the audience: the 'peanut-crunching crowd' is not a metaphor "
          "for readers but for the spectators of a miracle, and the speaker's complaint is that her "
          "suffering has been converted into a spectacle that pays. That is why the poem's revenge is "
          "also a claim about art: to 'eat men like air' is to become the thing that consumes rather "
          "than the thing consumed, and the closing image is deliberately less consoling than "
          "triumphant.",
  themes_text="The first subject is survival as a performance, in which the survivor is paid in attention "
              "and the audience is complicit in the death it comes to see. The second is the ownership of "
              "a body and of a case history, argued in the addresses to 'Herr Doktor' and 'Herr Enemy': "
              "the doctors, the husband and the god are versions of the same proprietor. The third is the "
              "use of the Holocaust as a figure for the woman's condition, which is the poem's most "
              "argued-over decision and the reason it is now taught as much for its politics as for its "
              "craft. The fourth is rebirth itself, drawn from the Gospel of John and from the phoenix, "
              "and deliberately parodic: what rises is not the soul but the body's appetite.",
  structure="Twenty-eight unrhymed tercets, mostly one sentence per stanza, with a refrain-like repetition "
            "of 'Herr' in the closing addresses and a movement from the public display of the first half "
            "to the private history of the second and the revenge of the last three stanzas; the poem "
            "has no stanza breaks beyond the tercet, so the escalation is continuous.",
  style="Very short lines, often of two or three words, with heavy internal rhyme and assonance ('Do I "
        "terrify?', 'the peanut-crunching crowd'); a diction that mixes the circus barker, the medical "
        "report and the nursery rhyme; direct address used as a weapon; and a use of proper names - "
        "Lazarus, God, Lucifer - that keeps the poem at the scale of myth even when it is most "
        "confessional.",
  ctx="Written between 23 and 29 October 1962 at Court Green, in the weeks after the break-up of Plath's "
      "marriage and in the middle of the sequence of poems, including 'Daddy' and 'Ariel', that made her "
      "late manner; first published in Ariel (London: Faber and Faber, 1965). Its 'Herr Doktor' belongs to "
      "the German and Austrian doctors of Plath's biography - her father Otto Plath's German origins and "
      "her own memories of the American hospital in which she was treated after her 1953 suicide attempt. "
      "The poem's Holocaust imagery was written in the knowledge of the Eichmann trial of 1961, and the "
      "argument about its propriety began almost as soon as the poem was published.",
  sig="'Lady Lazarus' is one of the two or three poems by which Plath is known, and its closing lines are "
      "among the most recognised in twentieth-century English poetry; it is central to the feminist "
      "criticism of the 1970s that made Plath a public figure, to the study of confessional writing, and "
      "to the continuing argument about the uses of Holocaust imagery in postwar literature.",
  canon="Major canon",
  crit="The criticism is divided between readings that take the poem as a triumphant assertion of female "
       "survival and readings that find in it a dangerous appropriation of the language of the camps; "
       "biographical critics have traced the 'three deaths' to the 1953 overdose and to the earlier "
       "accident and illness, and formal critics have read the tercets as a parody of the hymn. Seamus "
       "Heaney's charge that Plath's Holocaust imagery is 'a poetry of the will' and the defences of "
       "later feminist critics remain the terms of the argument.",
  biblio="Written 23-29 October 1962; first published in Ariel (London: Faber and Faber, 1965); reprinted "
         "in The Collected Poems (1981) and in Ariel: The Restored Edition (2004). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="No periodical printing before Ariel was established from the sources consulted; the 1965 date "
        "is the date of first publication in book form. The BBC recording of October 1962 includes lines "
        "omitted from the printed text, and the published version is the one recorded here.",
  ver="partially verified", sources=[W_SP, W_PF_LL, W_ARIEL, W_INDEX, W_REST, NAAL]),
W10("Ariel", SP, "1965", "Poem (ten tercets with a closing single line)", "major",
  genres=G("Confessional Poetry", "Lyric Poetry", "Free Verse"),
  themes=T("Identity, authenticity and the divided self", "Nature, ecology and environmental crisis",
           "Death, illness and mourning"),
  movements=M(CONF),
  overview="'Ariel' was written on 27 October 1962, Plath's thirtieth birthday, and first published in "
           "Ariel (Faber and Faber, 1965), the collection that took its title from it. Ten tercets and a "
           "single closing line describe a dawn horse ride: 'Stasis in darkness. / Then the substanceless "
           "blue / Pour of tor and distances.' The rider becomes one with the horse, then with the drive "
           "itself - 'God's lioness', 'White / Godiva', 'the arrow, / The dew that flies / Suicidal' - "
           "and the poem ends in 'the red / Eye, the cauldron of morning'. It is Plath's most concentrated "
           "lyric and the one that gives its name to the whole of her late work.",
  content="The poem opens in stillness and darkness, then in the 'substanceless blue' of distance and the "
          "'Pour of tor and distances' - the tors of Dartmoor. The rider and horse grow one: 'God's "
          "lioness, / How one we grow, / Pivot of heels and knees! - The furrow // Splits and passes, "
          "sister to / The brown arc / Of the neck I cannot catch'. Berries cast dark hooks, 'Black sweet "
          "blood mouthfuls'; something else 'hauls me through air - / Thighs, hair; / Flakes from my "
          "heels'. The rider becomes 'White / Godiva', unpeeling 'Dead hands, dead stringencies', then "
          "'Foam to wheat, a glitter of seas'; the child's cry 'melts in the wall'; and the last four "
          "stanzas give the poem its terrible speed: 'And I / Am the arrow, // The dew that flies / "
          "Suicidal, at one with the drive / Into the red // Eye, the cauldron of morning.'",
  summary="'Ariel' compresses the whole of Plath's late manner into thirty-one lines. It begins with a "
          "stasis that is also an unmaking - darkness, then a blue with no substance - and every stage of "
          "the ride is a further shedding: the rider loses the horse's neck, then her dead 'stringencies', "
          "then her body, until the only thing left is motion. The poem's pronouns matter: 'I cannot "
          "catch' and 'I unpeel' give way to 'And I / Am the arrow', a predication rather than an action, "
          "so that the self at the end is not a rider but the ride. The images are drawn from the stable, "
          "the harvest and the Christian martyrdom - God's lioness, Godiva, the dew, the red eye - and "
          "they are held in tercets whose line breaks keep interrupting the sentence at the point of "
          "greatest speed. The famous 'Suicidal' is both literal and descriptive of the drive: the poem "
          "was written on Plath's birthday, five months after her separation, and it is hard not to read "
          "the line biographically; but within the poem it names the impersonality the whole ride has "
          "been reaching for. The poem's extraordinary economy is worth stating plainly: in thirty-one "
          "lines it moves through five distinct states - stasis, the blue of distance, the merging with "
          "the horse, the shedding of the rider's body, and the final identification with the arrow - and "
          "it does so without a single connective to explain the transitions. Plath wrote it on her "
          "thirtieth birthday, and the coincidence of the birthday with the poem's theme of rebirth has "
          "governed its reception; but the poem's own logic is not the logic of an autobiography. It is "
          "the logic of a ride, in which the rider's will is progressively handed over to the animal's "
          "speed, and the last line arrives at a colour - red - that is also the colour of the sun and of "
          "blood, and a word, 'cauldron', that belongs to the kitchen and to witchcraft at once.",
  themes_text="The first subject is the dissolution of the self into pure motion, which the poem pursues "
              "through a series of metamorphoses from rider to lioness to Godiva to arrow to dew. The "
              "second is the landscape of Dartmoor as an image of that dissolution: the tors, the furrow, "
              "the berries, the 'cauldron of morning' are all forms of the same energy. The third is "
              "rebirth, and the poem is deliberately ambiguous about whether the rider's flight is a "
              "release or a death; 'the child's cry / Melts in the wall' is the one domestic sound in the "
              "poem and it is swallowed. Read with 'Lady Lazarus' and 'Daddy', 'Ariel' completes a trio in "
              "which the self is murdered, resurrected and finally dissolved, and it is the most "
              "impersonal of the three.",
  structure="Ten unrhymed tercets and a single closing line, each stanza a breath-length unit with the "
            "sentence running across the breaks; the movement is chronological (darkness to sunrise) but "
            "the stages are metamorphic rather than narrative, and the final line stands alone as the "
            "arrival the whole poem has been riding towards.",
  style="Extremely compressed free verse with a strong, almost chant-like rhythm; heavy alliteration and "
        "assonance ('substanceless blue', 'Pivot of heels and knees'); ellipsis and parataxis, with "
        "verbs often omitted; a diction that is archaic and liturgical ('God's lioness', 'Godiva', "
        "'stringencies') set against the physical detail of the ride; and a closing image of pure colour.",
  ctx="Written on 27 October 1962, Plath's thirtieth birthday, at Court Green; 'Ariel' was the name of "
      "the horse she rode at a riding school on Dartmoor, and Ted Hughes recorded that she had ridden a "
      "bolting horse as a student at Cambridge. The poem was first published in Ariel (London: Faber and "
      "Faber, 1965) and gives the collection its title; in the restored edition of 2004 it stands in the "
      "middle of Plath's own sequence, where she had placed it.",
  sig="'Ariel' is the poem that named the most influential posthumous collection in modern English "
      "poetry, and its title has become the shorthand for Plath's late manner; it is a set text in the "
      "teaching of twentieth-century lyric and the poem most often used to demonstrate her mastery of "
      "the short, driven stanza.",
  canon="Major canon",
  crit="Readings divide between the biographical - the birthday ride as a figure of rebirth or of "
       "suicide - and the formal, which attend to the tercets, the ellipses and the metamorphic series; "
       "feminist critics have read the poem's 'Godiva' and its dissolution of the female body as a "
       "critique of the spectacle of the woman, and the poem's relation to Hughes's own horse poems has "
       "been much discussed.",
  biblio="Written 27 October 1962; first published in Ariel (London: Faber and Faber, 1965); reprinted in "
         "The Collected Poems (1981) and in Ariel: The Restored Edition (2004). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem's title is also the title of the collection, which is why the record is for the poem "
        "and not the book; no periodical printing before Ariel was established from the sources "
        "consulted. 'Ariel' was a working title of the collection too, and Plath's manuscript is titled "
        "Ariel and other poems.",
  ver="partially verified", sources=[W_SP, W_PF_AR, W_ARIEL, W_INDEX, W_REST, NAAL]),
W10("Daddy", SP, "1965", "Poem (sixteen quintains with irregular rhyme)", "major",
  genres=G("Confessional Poetry", "Dramatic Monologue", "Formal Verse"),
  themes=T("Family, marriage and domestic life", "Death, illness and mourning",
           "The Holocaust, atrocity and historical memory"),
  movements=M(CONF),
  overview="'Daddy' was written on 12 October 1962, a day after 'The Applicant' and one month after "
           "Plath's separation from Ted Hughes, and first published in Ariel (Faber and Faber, 1965). Its "
           "sixteen quintains address the father who died when she was eight, and they move through "
           "idolatry, German and Polish memory, the Nazi and the Jew, the blackboard and the black "
           "telephone, to the vampire staked in the heart and the last line, 'Daddy, daddy, you bastard, "
           "I'm through.' The rhyme is carried by the long 'oo' vowel that closes most of the stanzas, so "
           "that the poem sounds like a nursery rhyme while it performs a symbolic murder.",
  content="The first quintain establishes the address and the image: 'You do not do, you do not do / Any "
          "more, black shoe / In which I have lived like a foot / For thirty years, poor and white, / "
          "Barely daring to breathe or Achoo.' The second: 'Daddy, I have had to kill you. / You died "
          "before I had time', and the father is a 'Marble-heavy, a bag full of God, / Ghastly statue with "
          "one gray toe / Big as a Frisco seal'. The poem goes to the German tongue and the Polish town "
          "'scraped flat by the roller / Of wars', to the father's 'Ach, du', and to the speaker's "
          "inability to speak: 'The tongue stuck in my jaw. / It stuck in a barb wire snare. / Ich, ich, "
          "ich, ich, / I could hardly speak.' Every German was the father, and the language 'an engine, an "
          "engine / Chuffing me off like a Jew', 'A Jew to Dachau, Auschwitz, Belsen'. The middle stanzas "
          "give the father as 'Panzer-man', 'Not God but a swastika', and the notorious line 'Every woman "
          "adores a Fascist'. Then the photograph on the blackboard, the cleft chin, the father as 'the "
          "black man who / Bit my pretty red heart in two'; the burial when she was ten, the attempted "
          "suicide at twenty ('And get back, back, back to you'), the glue that stuck her together; the "
          "model of the father made in a husband, 'A man in black with a Meinkampf look // And a love of "
          "the rack and the screw', and the marriage vow, 'And I said I do, I do.' The close cuts the "
          "black telephone off at the root, and ends: 'There's a stake in your fat black heart / And the "
          "villagers never liked you... Daddy, daddy, you bastard, I'm through.'",
  summary="'Daddy' is a poem of exorcism built on a child's chant. Its engine is the long 'oo' rhyme - "
          "shoe, do, Achoo, you, blue, two, through - which recurs in most of the sixteen quintains and "
          "gives the poem the momentum of a skipping game even at its most violent. Against that music "
          "Plath sets a sequence of increasingly extreme identifications: the father as black shoe, as "
          "statue, as Nazi, as vampire; the daughter as foot, as Jew, as the one who made a model of him "
          "and married it. The poem's controversial middle - the camps, the swastika, 'Every woman adores "
          "a Fascist' - is not decoration but the logic of the child's overestimation: if the father was "
          "everything, he was also the state, the army and the executioner, and the only way to be free of "
          "him is to make him a monster and then kill the monster. The last movement turns from the father "
          "to the husband who replaced him, and the closing 'I'm through' is at once a telephone "
          "disconnection and a declaration that the poem is finished and the mourning with it. The "
          "poem's formal signature is the vowel rhyme, and it is worth naming what it does: because the "
          "rhyme is carried by a single sound and not by a pattern of consonants, the stanzas feel both "
          "closed and endlessly repeatable, like the verses of a counting-out game, and the reader is "
          "carried from one enormity to the next on a rhythm that will not let them stop to object. That "
          "is the poem's ethical problem and its technical achievement at the same moment. The sixteen "
          "quintains are also a history in miniature: the father's death, the town in Poland, the train "
          "to the camps, the photograph on the blackboard, the suicide attempt at twenty, the husband "
          "made in the father's image, and the stake through the heart - each a scene the poem will not "
          "explain, arranged in the order a child might remember them rather than the order an analyst "
          "would reconstruct.",
  themes_text="The poem's first subject is the dead father as the origin of the speaker's speech: the "
              "'Ach, du', the stuck tongue and 'Ich, ich, ich, ich' are all about a language inherited "
              "from him and unusable without him. The second is the substitution of husband for father, "
              "which the poem presents not as a psychological thesis but as a deed - 'I made a model of "
              "you... And I said I do, I do.' The third is the Holocaust, used as the extreme vocabulary "
              "of absolute power, and the poem is now as often discussed for that decision as for its "
              "craft. The fourth is the nursery rhyme itself: 'Daddy' is a poem about the way a child's "
              "chant carries an adult's rage, and its formal genius is that the reader hears the chant "
              "before the rage.",
  structure="Sixteen unrhymed quintains (the first and last of five lines, with an extra section break "
            "before the final three stanzas), held together by a single vowel rhyme that returns at the "
            "end of most stanzas; the movement is from the father's death to the attempt to recover him "
            "to the husband who replaces him, and the last three stanzas stage the exorcism.",
  style="Short trimeter and dimeter lines in quintains, with a rhyme scheme carried by the 'oo' vowel "
        "rather than by exact rhyme; a diction that mixes the nursery ('Achoo', 'black shoe') with German "
        "and with the machinery of war; heavy repetition ('back, back, back', 'ich, ich, ich, ich'); and "
        "a tone that shifts without transition between the child's and the executioner's.",
  ctx="Written on 12 October 1962 at Court Green, a day after 'The Applicant' and a month after Hughes's "
      "departure; first published in Ariel (London: Faber and Faber, 1965). Otto Plath, born in Grabow in "
      "Prussia, died of undiagnosed diabetes in November 1940, when Plath was eight; the poem's Polish "
      "town and its German are his, and the 'gipsy ancestress' is a family story. Plath read 'Daddy' on "
      "the BBC in October 1962, and it is the poem most often cited in the argument about the editing of "
      "Ariel.",
  sig="'Daddy' is the most famous poem Plath wrote and one of the most anthologised poems in English of "
      "the twentieth century; it is a set text wherever confessional poetry is taught, and its use of "
      "Holocaust imagery has made it a permanent case in the ethics of poetic metaphor.",
  canon="Major canon",
  crit="The criticism is largely an argument about the Holocaust imagery: for some readers the swastika "
       "and the camps are the poem's justification, since they measure the child's absolutism; for others "
       "they are an appropriation that the poem never earns. Against that argument run the formal "
       "readings, which attend to the quintains and the vowel rhyme as a return of the nursery, and the "
       "biographical, which trace the black telephone and the 'model' to Plath's marriage. Robert "
       "Phillips's early reading of the poem as a metaphorical murder of the father's memory is still "
       "the starting point for most later accounts.",
  biblio="Written 12 October 1962; first published in Ariel (London: Faber and Faber, 1965); reprinted in "
         "The Collected Poems (1981) and in Ariel: The Restored Edition (2004). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="No periodical printing before Ariel was established from the sources consulted; the 1965 date is "
        "the date of first publication in book form. The poem's German and its Polish town are given in "
        "the text; the biographical facts of Otto Plath's birth and death are recorded here from the "
        "encyclopaedic sources, not from the poem.",
  ver="partially verified", sources=[W_SP, W_PF_DA, W_ARIEL, W_INDEX, W_REST, NAAL]),
W10("Words", SP, "1965", "Poem (six quatrains)", "significant",
  genres=G("Confessional Poetry", "Lyric Poetry", "Formal Verse"),
  themes=T("Language, writing and the limits of representation", "Art, the artist and the creative life",
           "Death, illness and mourning"),
  movements=M(CONF),
  overview="'Words' was written on 1 February 1963, ten days before Plath's death, and first published in "
           "Ariel (Faber and Faber, 1965) as the last poem in the 1965 text. Six quatrains compare words "
           "to the rings a stone makes in water, to the echo of hoof-beats, and finally to stars that are "
           "'fixed and moving' and govern a life without being asked; it is the shortest and the most "
           "impersonal of her late poems, and it stands as her ars poetica.",
  content="The first quatrain sets the comparison: 'Axes / After whose stroke the wood rings, / And the "
          "echoes / Travel outward like horses.' The second: 'Then the sap rises, / Weeping like tears, "
          "like water / Striving to re-cover / The rock that is the centre.' The third turns to the "
          "approach of a rider: 'More silent than the tramp of horses, / And more distant than the "
          "storm, / The words dry and riderless, / And the hoof-taps of horses.' The fourth has the "
          "stars, 'fixed and moving', and the fifth and sixth close the poem with the stars 'governing a "
          "life' and the lines 'From the bottom of the pool, fixed stars / Govern a life.'",
  summary="'Words' is a poem about what poems do after they are written, and it is unusually free of the "
          "confessional apparatus of Plath's other late work: there is no father, no husband and no "
          "hospital, only the axe, the sap, the horses and the stars. Its movement is a sequence of "
          "similes that get further away from the speaker - the axe-stroke is close and violent, the sap "
          "rises and weeps, the horses grow distant and silent, and the stars are fixed at the bottom of "
          "a pool. The last two quatrains abandon simile altogether and state the moral: words are "
          "'fixed and moving', they do not answer, and they govern a life. Read as the poem Plath put "
          "last in the 1965 Ariel, it is a leave-taking of poetry written by a poet ten days from death, "
          "and it has often been read as her most serene statement about her own art.",
  themes_text="The first subject is the autonomy of language: words, once written, are 'dry and riderless' "
              "and they act on the writer rather than for her. The second is the relation of the poem to "
              "the life that made it, which 'Words' figures as a pool in which the stars are both "
              "reflected and fixed. The third is silence, which the poem approaches through the dying "
              "fall of its images from axe to sap to hoof to stars. It is also, formally, a poem about "
              "form: the quatrains are so regular that the poem seems to have been found rather than "
              "made, which is exactly the condition it describes.",
  structure="Six unrhymed quatrains, largely in trimeter and tetrameter, with each stanza a complete "
            "sentence or a pair of sentences and a movement of withdrawal from the axe to the stars; the "
            "poem's last line falls at the very end of the sentence it completes.",
  style="Short, regular quatrains with an almost entirely end-stopped syntax; a diction drawn from "
        "woodwork, riding and astronomy rather than from the clinic; simile used as the poem's whole "
        "structure, then dropped for the last plain statements; and an absence of the first person that "
        "is unusual in Plath's late work.",
  ctx="Written on 1 February 1963 at Fitzroy Road, London, ten days before Plath's death, and placed last "
      "in the 1965 Ariel, where it closes the collection; reprinted in The Collected Poems (1981). It is "
      "one of the poems of the final week, with 'Edge', 'Balloons' and 'Contusion', and it belongs to the "
      "winter sequence in which the earlier, driven manner gives way to a sparer one.",
  sig="'Words' is Plath's most quoted statement about poetry and the poem that critics use to argue that "
      "her late work is not only confessional; it closes the 1965 Ariel and is therefore the last word of "
      "the collection that made her reputation, and it is a standard anthology poem in the teaching of "
      "twentieth-century poetics.",
  canon="Secondary canon",
  crit="Readings have treated 'Words' as an ars poetica, as a poem about the afterlife of the written "
       "text, and as a formal exercise in the plain style that Plath was moving towards in her last "
       "weeks; its position at the end of the 1965 Ariel has been read both as Hughes's elegiac framing "
       "and as a placing that Plath's own manuscript supports, since her restored sequence also ends "
       "with it.",
  biblio="Written 1 February 1963; first published in Ariel (London: Faber and Faber, 1965), where it "
         "stands as the last poem of the 1965 text; reprinted in The Collected Poems (1981) and in "
         "Ariel: The Restored Edition (2004). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="No periodical printing was established from the sources consulted; the 1965 date is the date of "
        "first publication in book form. Its place as the last poem of the 1965 Ariel is confirmed by the "
        "collection's contents list.",
  ver="partially verified", sources=[W_SP, W_ARIEL, W_REST, W_INDEX, NAAL]),
W10("Child", SP, "1971", "Poem (eight lines in two sentences)", "significant",
  genres=G("Confessional Poetry", "Lyric Poetry", "Free Verse"),
  themes=T("Family, marriage and domestic life", "Childhood, adolescence and coming of age",
           "Art, the artist and the creative life"),
  movements=M(CONF),
  overview="'Child' was written on 28 January 1963, two weeks before Plath's death, and was not printed in "
           "Ariel; it first appeared in Winter Trees (Faber and Faber, 1971). Eight lines address the "
           "child's 'clear eye' as 'the one absolutely beautiful thing', and the poem asks to fill it with "
           "'color and ducks, / The zoo of the new', before closing on the single word 'Wringing' and the "
           "line 'Your clear eye is the one absolutely beautiful thing.' It is the last of Plath's poems "
           "about her children and the shortest of the Norton selections.",
  content="The poem in full: 'Your clear eye is the one absolutely beautiful thing. / I want to fill it "
          "with color and ducks, / The zoo of the new // Whose name you meditate - / April snowdrop, "
          "Indian pipe, / Little // Stalk without wrinkle, / Pool in which images / Should be grand and "
          "classical, not this troublous // Wringing of hands, this dark / Ceiling without a star.' Its "
          "two sentences move from the child's eye as the one beautiful thing to the adult's 'troublous / "
          "Wringing of hands' and the 'dark / Ceiling without a star' that the child's eye is reflecting, "
          "and the poem's whole argument is carried by the contrast between the zoo of the new and the "
          "room in which it is being imagined.",
  summary="'Child' is a poem of two rooms. The first is the child's eye, which the mother wants to fill "
          "with the names of flowers and animals; the second is the room they are actually in, with its "
          "dark ceiling and the mother's wringing hands. The poem's movement is from the wish to the "
          "admission, and its brevity is the point: there is no time, and no room, for anything between "
          "them. Plath wrote it on 28 January 1963, a fortnight before her death, and it belongs with "
          "'Edge' and 'Words' to the last week's poems; the tenderness is undiminished and the despair is "
          "unargued, and the poem ends not on the child's eye but on the ceiling it is reflecting.",
  themes_text="The first subject is the failure of the imagination's gift: the mother wants to give the "
              "child a world of names and images, and what she has to give instead is her own 'troublous "
              "wringing of hands'. The second is infancy as an unmediated attention, the child as the "
              "only clear eye in the poem. The third is the relation of art to care - the mother's "
              "business is to fill the eye with 'the zoo of the new', and the poem is the record of her "
              "inability to do it. It is also, quietly, a poem about the material of poetry: the "
              "snowdrop, the Indian pipe and the 'little stalk' are the stock of a nature poem, and the "
              "poem is asking whether they can be given to a child or only written.",
  structure="Eight unrhymed short lines, run as two sentences across four and four, with the poem turning "
            "at 'not this troublous' and the last two lines falling into the dark ceiling; there is no "
            "stanza division, so the turn is carried entirely by syntax.",
  style="Extremely short free-verse lines with a high proportion of monosyllables; a diction of flowers "
        "and animals ('snowdrop', 'Indian pipe', 'ducks') set against a diction of the sickroom "
        "('troublous', 'Wringing', 'dark'); a single long sentence interrupted by a dash; and an "
        "almost entire absence of the figurative language that the rest of the late poems rely on.",
  ctx="Written on 28 January 1963 at Fitzroy Road, London, two weeks before Plath's death, and not "
      "included in the 1965 Ariel; first published in Winter Trees (London: Faber and Faber, 1971) and "
      "reprinted in The Collected Poems (1981). Its subject is Plath's son Nicholas, born in January "
      "1962, and it belongs to the last group of poems in which she wrote about her children.",
  sig="'Child' is the best known of Plath's poems about her children after 'Morning Song' and the one "
      "most often set beside it to show how far the two years between them had taken her; it is a "
      "standard anthology poem and its opening line is among the most quoted in her work.",
  canon="Secondary canon",
  crit="Critics have read 'Child' as a counterweight to the poems of maternal rage, as a poem about the "
       "impossibility of giving a child an unspoiled world, and as a late instance of Plath's turn to the "
       "plain style; its relation to 'Morning Song', written two years earlier about the same child, has "
       "been the starting point for most accounts of her late development.",
  biblio="Written 28 January 1963; first published in Winter Trees (London: Faber and Faber, 1971) and "
         "reprinted in The Collected Poems (1981). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The poem is not in the 1965 Ariel, which is why its first publication is 1971 and not 1965; the "
        "1971 date of the list is therefore the date of first publication in book form, not of "
        "composition. The Winter Trees first edition is recorded from bookseller and catalogue listings "
        "rather than from a printed bibliography.",
  ver="partially verified", sources=[W_SP, W_WT, W_REST, W_INDEX, NAAL]),
]
