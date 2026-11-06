"""Installment 10, wave 13: the Norton selections of authors already recorded.

The first wave under the third scope decision (2026-11-06), which makes the selections of
The Norton Anthology of English Literature (11th edition, vol. F) and The Norton Anthology
of American Literature (vol. E) the measure of the installment. These are the selections
of 1946-2000 by authors whose records already exist: nine poems by Philip Larkin (wave 02),
George Orwell's 'Politics and the English Language' (Orwell's author record belongs to
installment 9; see wave 05) and Samuel Selvon's story 'Waiting for Aunty to Cough' (wave 08).
Larkin's 'Aubade' was recorded in wave 02.

Each record names the collection the piece belongs to. Completion dates of the poems come
from Wikipedia's list of Larkin's poems and its article on High Windows; first periodical
printings are recorded only where a consulted source gives them. The poem 'High Windows'
is recorded as 'High Windows (poem)' because the collection has the bare title.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import W10, G, T, M, NAEL  # noqa: E402

LARKIN = "Philip Larkin"
GO = "George Orwell"
SS = "Samuel Selvon"
MOVE = "The Movement"
CAR = "Caribbean Literature in English"
WIN = "Black British Writing and the Windrush Generation"

W_LIST = "List of poems by Philip Larkin (Wikipedia)"
W_CG = "Church Going (Wikipedia)"
W_MCM = "MCMXIV (Wikipedia)"
W_TWW = "The Whitsun Weddings (Wikipedia)"
W_HW = "High Windows (Wikipedia)"
W_HWP = "High Windows (poem) (Wikipedia)"
W_TBTV = "This Be the Verse (Wikipedia)"
EBSCO_EXP = "The Explosion by Philip Larkin (EBSCO Research Starters)"
HULL = "Papers of Philip Arthur Larkin, file 'High Windows' (Hull History Centre, via Archives Hub)"
S24 = "Larkin's Public Poetry and Aden (South24 Center for News and Studies)"
GALE_AT = "An Arundel Tomb (Gale, Poetry for Students, via Encyclopedia.com)"
BUCK = "Larkin's 'Talking in Bed' (Journal of Language and Literature, University of Buckingham)"
QUARKS = "'Sad Steps' toward a Sedate Style (3 Quarks Daily)"
W_PEL = "Politics and the English Language (Wikipedia)"
ORW_BIB = "George Orwell bibliography (Wikipedia)"
THRESH = "Remembering Sam Selvon's Short Stories (Thresholds, University of Chichester)"
UWI = "Sam Selvon Collection (SC33), finding aid (The Alma Jordan Library, University of the West Indies)"

WORKS = [
W10("Church Going", LARKIN, "1955", "Poem (seven nine-line stanzas)", "significant",
  genres=G("Lyric Poetry", "Religious Poetry", "Formal Verse"),
  themes=T("Faith, doubt and the sacred", "Death, illness and mourning", "History, truth and the uses of the past"),
  movements=M(MOVE),
  overview="Church Going is a poem by Philip Larkin, written in 1954 and first published in his collection The Less "
           "Deceived (Marvell Press, 1955). An agnostic cyclist stops at an empty country church and, half mocking his own "
           "awkward reverence, asks what churches will become when belief has gone and why such buildings still draw him. It "
           "is generally regarded as one of his masterpieces.",
  content="The speaker's visit to an empty church: his inventory of its furnishings, the words he reads aloud from the "
          "lectern, the Irish sixpence he leaves; his speculation about what the building will become when no one uses it; "
          "and his conclusion that it remains 'a serious house on serious earth'.",
  summary="Making sure nothing is going on inside, the speaker lets the door close behind him and takes off his "
          "cycle-clips in awkward reverence. He notes the flowers, the brass and the organ, runs a hand over the font, "
          "mounts the lectern and reads a few verses, ending 'Here endeth' much more loudly than he meant, signs the book "
          "and donates an Irish sixpence, deciding the place was not worth stopping for. Yet he did stop, as he often does, "
          "and he wonders what he is looking for. When churches fall out of use, will they be kept as museums, left to the "
          "rain and sheep, or visited by women with children for luck and cures? Who will be the last to seek the place "
          "for what it was: a scholar of rood-lofts, a lover of ruins, a Christmas-addict, or someone like himself, bored "
          "and uninformed but drawn to the spot where marriage, birth and death were solemnised? The final stanza answers "
          "with a tone of settled conviction: the building's air holds all our compulsions, recognised and robed as "
          "destinies, and someone will always discover in himself a hunger to be more serious and gravitate to this "
          "ground, which he once heard was proper to grow wise in, if only because so many dead lie round.",
  themes_text="The poem measures the decline of religious belief against the survival of the needs religion served. Its "
              "irony is directed at the speaker as much as at the church, and the joking inventory gives way to respect "
              "for a place where the great events of life were made serious. It is agnostic without being dismissive, "
              "and ends on the human need for seriousness and on the presence of the dead.",
  structure="Seven nine-line stanzas in iambic pentameter, rhymed, moving from anecdote to speculation and to a closing "
            "stanza of grave statement.",
  style="Colloquial, self-deprecating narration ('brass and stuff / Up at the holy end') that rises into formal, "
        "almost liturgical cadence at the close; precise physical detail and comic deflation.",
  ctx="Drafted from April 1954 through some twenty-one pages, abandoned and resumed, and finished in July 1954 while Larkin "
      "was sub-librarian at Queen's University, Belfast; The Less Deceived made his reputation the following year.",
  sig="One of the best-known English poems of the century, and the poem that fixed the image of Larkin as the cycle-clipped, "
      "unillusioned observer; it is among his most anthologised and studied works.",
  crit="Wikipedia's article calls it generally regarded as one of his masterpieces, and notes Martin Amis's remark on the "
       "cycle-clips associated with Larkin in the popular imagination and Christopher Hitchens's on Larkin's fondness for "
       "church architecture beside his scepticism about Christianity.",
  canon="Secondary canon",
  biblio="First published in The Less Deceived (Hessle: The Marvell Press, November 1955, dated October). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F (p. 788).",
  notes="Whether the poem appeared in a periodical before The Less Deceived was not checked. The stanza count and metre are "
        "stated from the text, not from a consulted source.",
  comp=("1954", "1954"), ver="partially verified", sources=[W_CG, W_LIST, NAEL]),
W10("MCMXIV", LARKIN, "1964", "Poem (four eight-line stanzas forming one sentence)", "significant",
  genres=G("Lyric Poetry", "Elegiac Poetry", "Formal Verse"),
  themes=T("War, combat and its aftermath", "History, truth and the uses of the past", "Nationhood and national identity"),
  movements=M(MOVE),
  overview="MCMXIV, the year 1914 in Roman numerals as on a war memorial, is a poem by Philip Larkin completed in May 1960 "
           "and first published in The Whitsun Weddings (Faber, 1964). A single sentence over four stanzas, without a main "
           "verb, it looks at what seems a photograph of volunteers queuing to enlist in August 1914 and at the England "
           "around them, and ends: 'Never such innocence again'.",
  content="The long queues of men outside the recruiting offices; the shut shops, the coins and advertisements, the children "
          "named after kings and queens; the countryside and the great houses with their servants; and the closing lament "
          "for an innocence that changed into the past without a word.",
  summary="The poem opens on the lines of men standing patiently as if outside a cricket or football ground, their "
          "moustached, archaic faces grinning as if the war were an August Bank Holiday lark. It widens to the streets "
          "behind them, with shops shut and blinds drawn, farthings and sovereigns, children at play called after kings "
          "and queens, tin advertisements for cocoa and twist and pubs open all day, and then to the countryside, where the "
          "place names are hidden under the summer grass and the servants live in tiny rooms in huge houses. The last "
          "stanza turns to judgement: never such innocence before or since, which became the past without a word, with "
          "the men leaving the gardens tidy and the thousands of marriages lasting a little while longer. The war that "
          "ended this world is never described; the poem knows, as its people cannot, what is about to happen to them.",
  themes_text="The poem mourns the end of an England of settled hierarchy and unquestioning patriotism, and also the "
              "innocence of men who did not know what they were volunteering for. Its knowledge of the outcome, held back "
              "until the last stanza, turns a photograph into an elegy for a generation and a social order.",
  structure="Four eight-line stanzas forming one sentence with no main verb, built of noun phrases, so that the scene stays "
            "suspended in time until the closing lines.",
  style="Rhymed short lines, a catalogue of period detail and a restrained, elegiac cadence, with the Roman-numeral title "
        "recalling the inscriptions on war memorials.",
  ctx="Completed on 17 May 1960; collected in The Whitsun Weddings, published by Faber on 28 February 1964, the book that "
      "established Larkin with a wider public.",
  sig="One of the best-known English poems about the First World War written after it, often taught beside the poems of "
      "the war poets; its closing line has become proverbial.",
  canon="Secondary canon",
  biblio="First published in The Whitsun Weddings (London: Faber and Faber, 1964), according to Wikipedia. A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F (p. 789).",
  notes="Wikipedia's article on the poem is short and flagged as resting on one source. The details of the summary are "
        "stated from the text.",
  comp=("1960", "1960"), ver="partially verified", sources=[W_MCM, W_LIST, W_TWW, NAEL]),
W10("Talking in Bed", LARKIN, "1964", "Poem (twelve lines in four tercets)", "minor",
  genres=G("Lyric Poetry", "Love Poetry"),
  themes=T("Love, intimacy and loss", "Language, writing and the limits of representation"),
  movements=M(MOVE),
  overview="Talking in Bed is a short poem by Philip Larkin, completed in August 1960 and collected in The Whitsun Weddings "
           "(1964), about a couple for whom talk in bed, which ought to be easiest, has become difficult.",
  content="A couple lying together in silence; the wind, clouds and dark towns outside; and the closing difficulty of "
          "finding words at once true and kind.",
  summary="Talking in bed ought to be easiest, the speaker begins, since lying together is an emblem of two people being "
          "honest; yet more and more time passes in silence. Outside the wind builds and disperses clouds and dark towns "
          "heap up on the horizon, and none of it cares for the couple. Nothing explains why, at this unique distance from "
          "isolation, it becomes still harder to find words at once true and kind, or not untrue and not unkind.",
  themes_text="Intimacy that does not abolish loneliness, and the conflict between honesty and kindness in what lovers "
              "say; the indifferent world outside sharpens the couple's isolation.",
  structure="Twelve lines in four three-line stanzas, loosely rhymed, ending on a self-correcting double negative.",
  style="Plain statement, a single image of wind and towns, and a final litotes ('not untrue and not unkind') that "
        "enacts the hesitation it describes.",
  ctx="One of the poems of love and marriage in The Whitsun Weddings, written in the year of 'MCMXIV'.",
  sig="Frequently anthologised and taught; its last lines are among Larkin's most quoted.",
  crit="A stylistic study in the University of Buckingham's Journal of Language and Literature reads the ending as a "
       "conflict between Grice's maxim of quality and the politeness principle.",
  canon="Minor canon",
  biblio="Collected in The Whitsun Weddings (London: Faber and Faber, 1964). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F (p. 790).",
  notes="Earlier periodical publication, if any, was not checked.",
  comp=("1960", "1960"), ver="partially verified", sources=[W_LIST, W_TWW, BUCK, NAEL]),
W10("High Windows (poem)", LARKIN, "1974", "Poem (five quatrains)", "significant",
  genres=G("Lyric Poetry", "Formal Verse"),
  themes=T("Sexuality, desire and the closet", "Faith, doubt and the sacred", "Childhood, adolescence and coming of age"),
  movements=M(MOVE),
  overview="High Windows is the title poem of Philip Larkin's last collection, High Windows (Faber, 1974), completed in "
           "February 1967. An older man watching a young couple imagines their sexual freedom as the paradise his "
           "generation dreamed of, wonders whether his own freedom from religion once looked like paradise to his elders, "
           "and ends not in words but in an image of high windows and endless blue air.",
  content="The speaker's coarse imagining of a young couple's sex life; the reflection that every generation envies the "
          "next its freedom, and that his own youth was free of God and hell; and the final image of sun-filled glass and "
          "empty sky.",
  summary="Seeing a couple of kids, the speaker guesses that the boy is sleeping with the girl and that she takes the pill "
          "or wears a diaphragm, and he knows this is the paradise everyone old has dreamed of, with bonds and gestures "
          "pushed aside like an outdated combine harvester and the young sliding endlessly down to happiness. He wonders "
          "whether anyone looked at him forty years earlier and thought the same: no God any more, no sweating in the dark "
          "about hell, no hiding what you think of the priest, who will go down the long slide too, like free bloody birds. "
          "Then, rather than words, comes the thought of high windows: the sun-comprehending glass and, beyond it, the "
          "deep blue air that shows nothing, and is nowhere, and is endless.",
  themes_text="Envy of the young and the recognition that each generation's liberation looks like paradise only from "
              "outside; the loss of religious fear and of religious hope together. The ending offers a vision that is "
              "either transcendence or blank emptiness, and refuses to choose.",
  structure="Five four-line stanzas, loosely rhymed, with a turn at the last stanza from argument to image.",
  style="Obscenity and slang in the opening lines set against the lyrical abstraction of the close, a contrast "
        "characteristic of late Larkin.",
  ctx="Completed on 12 February 1967, the year of the Sexual Offences Act and of rapidly changing sexual mores, while "
      "Larkin lived in the top flat of 32 Pearson Park, Hull, whose windows are widely believed to have suggested the image.",
  sig="One of Larkin's most celebrated and discussed poems, and the title piece of the collection Clive James called "
      "'despair made beautiful'.",
  canon="Secondary canon",
  biblio="Collected in High Windows (London: Faber and Faber, 1974), the sixth of its twenty-four poems. A selection of The "
         "Norton Anthology of English Literature, 11th edition, vol. F (p. 790). The collection has its own record, "
         "High Windows.",
  notes="Wikipedia's article on the poem says the windows are mentioned 'after a funeral has been evoked'; no funeral is "
        "evoked in the text, and the statement is not used. The reference to the 1967 Act is context supplied here, not "
        "a claim of the sources about the poem.",
  comp=("1967", "1967"), ver="partially verified", sources=[W_HWP, W_HW, W_LIST, NAEL]),
W10("Going, Going", LARKIN, "1972", "Poem (nine six-line stanzas; commissioned)", "minor",
  genres=G("Political Poetry", "Social Poetry", "Formal Verse"),
  themes=T("Nature, ecology and environmental crisis", "Nationhood and national identity", "Land, place and regional belonging"),
  movements=M(MOVE),
  overview="Going, Going is a poem by Philip Larkin commissioned by the Department of the Environment and first printed in "
           "its working party report on the human habitat, How Do You Want to Live? (1972), then collected in High Windows "
           "(1974). It foresees the English countryside lost to development and profit.",
  content="The speaker's former confidence that the fields would last his time; the demands for more houses, parking and "
          "caravan sites; the business pages and takeover bids; and the prophecy that England will be gone, leaving "
          "concrete and tyres.",
  summary="The speaker had thought the sense of fields and farms beyond the town would last his time, and that the earth "
          "would always recover however it was abused. Now he doubts it, or perhaps is only getting old: the young crowd "
          "in the motorway cafe want more houses, more parking, more caravan sites, more pay, and the business pages "
          "approve takeovers that move industry into the unspoilt dales. Before he dies, he thinks, the whole country will "
          "be bricked in except for the tourist parts, the first slum of Europe; and that will be England gone, the "
          "shadows, meadows, lanes, guildhalls and carved choirs surviving only in books and galleries. Most things are "
          "never meant, he ends, but the greeds and garbage are too thick-strewn to be swept up now: he thinks it will "
          "happen soon.",
  themes_text="Environmental and cultural loss, the commercial greed behind it, and the speaker's suspicion that his alarm "
              "may be partly the pessimism of age.",
  structure="Nine six-line stanzas, rhymed, moving from memory through satire of the present to prophecy.",
  style="Conversational, sardonic and plain, with lists of modern clutter set against a lyrical inventory of the England "
        "being lost.",
  ctx="Completed on 25 January 1972 for the report of a Department of the Environment working party; Her Majesty's "
      "Stationery Office gave permission for its inclusion in High Windows.",
  sig="Larkin's best-known public poem and an early literary statement of environmental anxiety in Britain, often quoted "
      "in debates about planning and the countryside.",
  canon="Minor canon",
  biblio="First printed in How Do You Want to Live? A Report on the Human Habitat (London: HMSO, 1972); collected in High "
         "Windows (Faber, 1974). A selection of The Norton Anthology of English Literature, 11th edition, vol. F (p. 791).",
  notes="The report's title is given in the Hull archive catalogue as 'Human Habitat: how do you want to live'. Secondary "
        "commentary seen only in search results says the report printed the poem with passages cut; this was not "
        "confirmed and is not stated in the record.",
  comp=("1972", "1972"), ver="partially verified", sources=[HULL, W_HW, W_LIST, NAEL]),
W10("Sad Steps", LARKIN, "1974", "Poem (six tercets)", "minor",
  genres=G("Lyric Poetry"),
  themes=T("Childhood, adolescence and coming of age", "Art, the artist and the creative life"),
  movements=M(MOVE),
  overview="Sad Steps is a poem by Philip Larkin, completed in April 1968 and collected in High Windows (1974). Its title "
           "comes from Sir Philip Sidney's sonnet 'With how sad steps, O Moon, thou climb'st the skies'; Larkin's sad steps "
           "are a middle-aged man's on his way back to bed.",
  content="The speaker's sight of the moon at four in the morning; his mockery of the poetic moon; and his sober recognition "
          "of what it reminds him of.",
  summary="Groping back to bed after a piss, the speaker parts the curtains and is startled by the rapid clouds and the "
          "moon's cleanliness over the wedge-shadowed gardens. There is something laughable about the moon dashing "
          "through cloud, high and preposterous and separate, and he tries out and rejects the romantic apostrophes "
          "('Lozenge of love! Medallion of art!'). Instead he shivers: the hardness, brightness and far-reaching singleness "
          "of its stare remind him of the strength and pain of being young, which cannot come again but is for others "
          "undiminished somewhere.",
  themes_text="Ageing and the loss of youth; the gap between poetic convention and plain experience, closed at the end by a "
              "plainness that honours the moon instead of decorating it.",
  structure="Eighteen lines in six three-line stanzas, rhymed, turning on the word 'No' from mockery to reflection.",
  style="A crude opening, a parody of high poetic diction in the middle, and a sober, generous close.",
  ctx="Completed on 24 April 1968, during the years of the poems of ageing and mortality that make up much of High Windows.",
  sig="A much-anthologised example of Larkin's dialogue with the English lyric tradition, here with Sidney's Astrophil and "
      "Stella.",
  canon="Minor canon",
  biblio="Collected in High Windows (London: Faber and Faber, 1974), seventeenth of its poems. A selection of The Norton "
         "Anthology of English Literature, 11th edition, vol. F (p. 793).",
  notes="The summary is stated from the text; an essay in 3 Quarks Daily (2016) was seen only as a search extract. The "
        "source of the title in Astrophil and Stella, sonnet 31, is stated from general knowledge.",
  comp=("1968", "1968"), ver="partially verified", sources=[W_HW, W_LIST, QUARKS, NAEL]),
W10("Homage to a Government", LARKIN, "1969", "Poem (three six-line stanzas)", "minor",
  genres=G("Political Poetry", "Formal Verse"),
  themes=T("Decolonisation, the end of empire and the new nation", "Nationhood and national identity"),
  movements=M(MOVE),
  overview="Homage to a Government is an ironic poem by Philip Larkin about the British withdrawal of its forces from east "
           "of Suez because the country could no longer pay for them. Completed in January 1969, it first appeared in The "
           "Sunday Times and was collected in High Windows (1974).",
  content="The announcement that the soldiers are to come home for lack of money; the repeated assurance that this is all "
          "right; and the picture of a country whose statues stand unchanged while it has become a different country.",
  summary="Next year, the poem begins, we are to bring the soldiers home for lack of money, and it is all right: the places "
          "they guarded must guard themselves, and we want the money for ourselves at home instead of working. It is hard "
          "to say who wanted it, but nobody minds; the places are far off, and from what we hear the soldiers only made "
          "trouble. Next year we shall live in a country that brought its soldiers home for lack of money; the statues "
          "will stand in the same tree-muffled squares, our children will not know it is a different country, and all we "
          "can hope to leave them now is money.",
  themes_text="The end of empire seen as national humiliation and moral decline, with complacency and the love of money "
              "replacing duty.",
  structure="Three six-line stanzas whose line endings repeat key words (home, right, orderly, money), giving the poem "
            "the sound of a flat, repeated excuse.",
  style="Deadpan irony, the government's own reassuring idiom turned against it.",
  ctx="Written after the Labour government's decision, announced in January 1968, to withdraw British forces from east of "
      "Suez by 1971; a commentator quotes Larkin calling the withdrawal for reasons of cost 'a dreadful humiliation'.",
  sig="Larkin's most explicitly political poem, often cited in discussions of his conservatism and of the literature of "
      "Britain's imperial decline.",
  canon="Minor canon",
  biblio="First published in The Sunday Times, 19 January 1969 (according to a South24 article); collected in High Windows "
         "(Faber, 1974). A selection of The Norton Anthology of English Literature, 11th edition, vol. F (p. 793).",
  notes="The Sunday Times date and Larkin's remark rest on one source (South24, which reads the poem as being about Aden); "
        "Gale's Poetry for Students, seen as a search extract, describes it as criticising the withdrawal of the last "
        "British troops from bases east of Suez. The 1968 announcement is stated from general historical knowledge.",
  comp=("1969", "1969"), ver="partially verified", sources=[S24, GALE_AT, W_HW, W_LIST, NAEL]),
W10("The Explosion", LARKIN, "1974", "Poem (eight unrhymed tercets and a single line)", "significant",
  genres=G("Elegiac Poetry", "Narrative Poetry"),
  themes=T("Death, illness and mourning", "Class, labour and social mobility", "Faith, doubt and the sacred"),
  movements=M(MOVE),
  overview="The Explosion is a poem by Philip Larkin, completed in January 1970 and placed last in his final collection, "
           "High Windows (1974). It describes the morning of a mining disaster, the men walking to the pit, the tremor at "
           "noon, and the moment in which their widows, hearing the promises of the funeral service, see the dead "
           "transfigured.",
  content="Miners walking to the pithead on a sunny morning; one of them finding a nest of lark's eggs and putting it back; "
          "the tremor at noon; words of consolation from the chapel; and the wives' vision of their men walking towards "
          "them, one showing the eggs unbroken.",
  summary="On the day of the explosion, shadows point towards the pithead and the slagheap sleeps in the sun. Men in "
          "pitboots come down the lane, coughing oath-edged talk and pipe-smoke; one chases rabbits, loses them, and comes "
          "back with a nest of lark's eggs, which he shows the others and puts back in the grass. Fathers, brothers, "
          "nicknames, laughter, they pass through the tall gates. At noon there is a tremor; cows stop chewing for a "
          "second, and the sun dims as in a heat-haze. The explosion itself and the deaths underground are never shown. "
          "In italic lines the language of the chapel promises that the dead go on before us and that we shall see them "
          "face to face; and for a second the wives see the men of the explosion larger than in life, gold as on a coin, "
          "walking somehow from the sun towards them, one showing the eggs unbroken.",
  themes_text="Sudden death in an ordinary working day, the solidarity of a mining community, and the consolations of "
              "religious language, which the poem allows a moment of truth without asserting it. The unbroken eggs become "
              "a symbol of the wholeness of the men's lives, or of life continuing.",
  structure="Twenty-five lines: eight unrhymed three-line stanzas and a final isolated line, in trochaic tetrameter with "
            "variations, the measure of Longfellow's Hiawatha.",
  style="Spare, concrete narration in clipped clauses, a shift to a formal, scriptural register in the italic stanza, and "
        "a visionary close unusual in Larkin.",
  ctx="Completed on 5 January 1970. Larkin's papers include correspondence with the Poem of the Month Club about reprinting "
      "it in High Windows, of which it is the last poem.",
  sig="One of Larkin's most admired late poems, often read as a counterweight to his scepticism because it grants the "
      "religious vision a moment of reality; widely anthologised and taught.",
  canon="Secondary canon",
  biblio="Collected in High Windows (London: Faber and Faber, 1974), the last of its twenty-four poems. A selection of The "
         "Norton Anthology of English Literature, 11th edition, vol. F (p. 794).",
  notes="The correspondence with the Poem of the Month Club implies an earlier printing by the club, whose date was not "
        "established, so 1974 is recorded as the first publication in a book. Accounts that Larkin was prompted by a "
        "television documentary on mining in late 1969 were seen only on study sites and are not used. The EBSCO entry "
        "was seen as a search extract.",
  comp=("1970", "1970"), ver="partially verified", sources=[EBSCO_EXP, HULL, W_HW, W_LIST, NAEL]),
W10("This Be The Verse", LARKIN, "1971", "Poem (three quatrains)", "significant",
  genres=G("Light Verse", "Lyric Poetry", "Formal Verse"),
  themes=T("Family, marriage and domestic life", "Childhood, adolescence and coming of age"),
  movements=M(MOVE),
  overview="This Be The Verse is a poem by Philip Larkin, first published in the August 1971 issue of New Humanist and "
           "collected in High Windows (1974). Its profane first line about parents and its advice not to have children "
           "have made it one of the most quoted English poems of the century.",
  content="The claim that parents pass on their faults to their children; the observation that their own parents did the "
          "same; and the conclusion that misery is handed down and the only escape is to have no children.",
  summary="Your parents mess you up, the speaker says in far blunter words: they do not mean to, but they fill you with "
          "their faults and add some extra just for you. They were messed up in their turn by fools in old-style hats and "
          "coats, who were half the time soppy-stern and half at one another's throats. Man hands on misery to man; it "
          "deepens like a coastal shelf. Get out as early as you can, the poem ends, and don't have any kids yourself: "
          "the only way to stop the inheritance is to refuse to pass it on.",
  themes_text="Inherited unhappiness and the impossibility of good parenting, presented as a universal law with a comic "
              "bleakness that critics read both as despair and as ironic tenderness.",
  structure="Three four-line stanzas of rhymed iambic tetrameter, the neat form of a hymn or epitaph.",
  style="Shocking colloquial obscenity in a strict, light-verse form; the title parodies Robert Louis Stevenson's "
        "'Requiem' ('This be the verse you grave for me').",
  ctx="Completed in April 1971 and first printed in New Humanist, the journal of the Rationalist Press Association, in "
      "August 1971.",
  sig="Larkin's most quoted poem, endlessly cited and parodied; Wikipedia, citing the Oxford Companion to Modern Poetry, "
      "notes its dark humour, directness and taboo-breaking language.",
  canon="Secondary canon",
  biblio="First published in New Humanist, August 1971; collected in High Windows (Faber, 1974). A selection of The Norton "
         "Anthology of English Literature, 11th edition, vol. F (p. 795). Also spelled This Be the Verse.",
  notes="Wikipedia's article carries a citation flagged as not a real article; only its publication facts, which agree "
        "with the collection's table of completion dates, are used. The summary paraphrases the text.",
  comp=("1971", "1971"), ver="partially verified", sources=[W_TBTV, W_HW, W_LIST, NAEL], alt=["This Be the Verse"]),
W10("Politics and the English Language", GO, "1946", "Essay", "major",
  genres=G("Political Essay", "Literary Essay"),
  themes=T("Language, writing and the limits of representation", "Power, the state and surveillance", "History, truth and the uses of the past"),
  overview="Politics and the English Language is an essay by George Orwell, first published in the April 1946 issue of "
           "the monthly Horizon and collected in Shooting an Elephant and Other Essays (1950). It argues that the English "
           "of its time was ugly and inaccurate, that slovenly language and foolish thought reinforce each other, and that "
           "political language in particular is designed to make lies sound truthful and murder respectable. It closes "
           "with six rules for clear writing, and has become one of the most reprinted essays in English.",
  content="Five specimen passages of bad contemporary prose; a catalogue of faults (dying metaphors, verbal false limbs, "
          "pretentious diction, meaningless words); a parody of a verse of Ecclesiastes in modern officialese; the "
          "analysis of political euphemism; the argument that insincerity is the great enemy of clear language; and six "
          "rules, with the claim that the decline of the language is reversible.",
  summary="Orwell begins by rejecting the view that the decline of English is a natural, irreversible process. Language "
          "becomes ugly and inaccurate because our thoughts are foolish, but its slovenliness makes it easier to have "
          "foolish thoughts, as a man may drink because he feels a failure and then fail the more completely because he "
          "drinks; the process can be reversed by people willing to take the trouble. He quotes five passages, by Harold "
          "Laski, Lancelot Hogben, an essay on psychology in the American magazine Politics, a communist pamphlet and a "
          "letter to Tribune, and draws from them a catalogue of swindles and perversions: dying metaphors used without "
          "thought of their meaning, 'operators or verbal false limbs' that pad sentences with phrases instead of verbs, "
          "pretentious diction that dresses up bias as impartial and scientific, and meaningless words, common in art and "
          "literary criticism and in political terms such as democracy and fascism. Modern prose, he says, consists less "
          "of words chosen for their meaning than of phrases tacked together like the sections of a prefabricated "
          "henhouse, and he demonstrates it by translating a verse of Ecclesiastes ('the race is not to the swift') into "
          "modern English of the worst sort. Political speech and writing are largely the defence of the indefensible: "
          "the bombing of defenceless villages is called pacification, the expulsion of peasants transfer of population, "
          "imprisonment without trial elimination of unreliable elements. Orthodoxy demands a lifeless, imitative style, "
          "and the great enemy of clear language is insincerity: when there is a gap between real and declared aims, one "
          "turns to long words and exhausted idioms like a cuttlefish spurting out ink. Ready-made phrases think for the "
          "writer and can even conceal his meaning from himself. Orwell proposes that a writer should let the meaning "
          "choose the words, and offers six rules: never use a figure of speech you are used to seeing in print; never "
          "use a long word where a short one will do; cut every word you can; never use the passive where you can use "
          "the active; never use a foreign phrase, scientific word or jargon if there is an everyday English equivalent; "
          "and break any of these rules sooner than say anything outright barbarous. He concedes that his own essay "
          "commits the faults it attacks, insists that he is concerned with language as an instrument for expressing "
          "thought, not with its literary use, and ends that political language is designed to give an appearance of "
          "solidity to pure wind, and that one can at least send some worn-out phrase into the dustbin where it belongs.",
  themes_text="The essay ties the quality of prose to the quality of thought and of politics. Its central claim is that "
              "abstraction and euphemism allow writers and readers to accept atrocities they would reject if they were "
              "named concretely, so that clear language is a political and moral discipline. It treats stale language as "
              "a habit that thinks for the writer, and orthodoxy of any party as the enemy of individual, honest "
              "expression. The concern with how language can make certain thoughts impossible returns in the Newspeak of "
              "Nineteen Eighty-Four.",
  structure="An argumentative essay that moves from a general claim, through quoted specimens and a classified catalogue "
            "of faults, to the political analysis and the practical rules, ending with qualifications and a short "
            "peroration.",
  style="Plain, concrete and vigorous prose, rich in homely analogies (the drinker, the cuttlefish, the prefabricated "
        "henhouse, the packet of aspirins at one's elbow), quoting its examples and parodying them; Orwell admits that "
        "the essay itself breaks some of its rules.",
  ctx="Written in late 1945, when Orwell's payment book records it on 11 December, after the success of Animal Farm and "
      "the death of his wife; it was meant for George Weidenfeld's Contact, which turned it down, and appeared in Horizon "
      "almost at the same time as 'The Prevention of Literature', which shares its concern with truth and language under "
      "political pressure.",
  sig="One of the most influential essays in English on style and on political language. Lynn Z. Bloom found it reprinted "
      "118 times in 325 editions of 58 composition readers published between 1946 and 1996, and it remains a staple of "
      "writing courses; its phrases about making lies sound truthful and murder respectable are constantly quoted in "
      "discussion of political rhetoric.",
  crit="Michael Shelden called it Orwell's most important essay on style, while Bernard Crick's biography did not mention "
       "it. John Rodden notes Orwell's own admission that he commits the faults he attacks; Terry Eagleton praised its "
       "demystification of political language before turning against Orwell; Carl Freedman's 1981 article on the essay "
       "and English composition started a debate about its ideology. The linguist Geoffrey Pullum has called it "
       "dishonest and its insistence on avoiding familiar phrases unfollowable, and Merriam-Webster's Dictionary of "
       "English Usage notes that Orwell uses the passive in a little over 20 per cent of its sentences, more than the "
       "periodicals surveyed.",
  canon="Major canon",
  biblio="First published in Horizon, vol. 13, no. 76 (April 1946), pp. 252-265; collected in Shooting an Elephant and "
         "Other Essays (London: Secker and Warburg, 1950), which has its own record. A selection of The Norton Anthology "
         "of English Literature, 11th edition, vol. F (p. 596).",
  notes="Publication details, the payment-book date and the history with Contact are from Wikipedia's article, which cites "
        "the Orwell bibliography, D. J. Taylor (2003) and the New Oxford Review; the article carries a 'more citations "
        "needed' banner. The link to Newspeak is a common critical observation, stated here without a specific source.",
  comp=("1945", "1945"), ver="partially verified", sources=[W_PEL, ORW_BIB, NAEL]),
W10("Waiting for Aunty to Cough", SS, "1957", "Short story", "minor",
  genres=G("Short Story"),
  themes=T("Migration, exile and diaspora", "The city, the suburb and modern space", "Love, intimacy and loss"),
  movements=M(CAR, WIN),
  overview="Waiting for Aunty to Cough is a comic story by Samuel Selvon about Brackley, a young West Indian in London, and "
           "his English girlfriend Beatrice. It appeared in the Evening Standard on 1 April 1957 and was collected the same "
           "year in the London part of Ways of Sunlight.",
  content="Brackley's nightly journeys to see Beatrice home to the far suburbs; a night when she has forgotten her key and "
          "they wait outside for her aunt to cough; his violent solution at dawn; and the joke the boys make of it.",
  summary="Brackley, who has taken up with a girl living far from central London, must see Beatrice home every night and "
          "make his way back late, missing buses and trains. One night she has forgotten her door key, and rather than "
          "rouse the household they wait in the cold outside the house in the early hours, hoping to hear Aunty cough. "
          "Beatrice dozes on his arm while Brackley, folded into the small doorway, cramped and frozen, waits through the "
          "night. Between five and half past he thinks he hears Aunty cough and, to Beatrice's amazement and horror, pelts "
          "the house with a stone. Word gets round, and the boys never let him forget it, hailing him with 'Brackley! You "
          "still waiting for Aunty to cough?'",
  themes_text="The comedy of a West Indian immigrant negotiating English suburban propriety and an interracial romance, "
              "told as a 'lime', the Trinidadian gathering where such stories are shared.",
  structure="An anecdote framed as a story told among 'the boys', ending on their catch-phrase.",
  style="Selvon's creolised narrative voice, with Trinidadian syntax and idiom carrying the comedy.",
  ctx="One of the London stories of Ways of Sunlight (1957), written in the years of The Lonely Londoners and of the "
      "Windrush migration; Selvon's papers at the University of the West Indies hold its manuscript and the Evening "
      "Standard clipping.",
  sig="A frequently anthologised example of Selvon's comic London writing and of his use of Caribbean speech in "
      "narration.",
  canon="Minor canon",
  biblio="First published in the Evening Standard (London), 1 April 1957, under a 'London Calypso' heading, according to "
         "the finding aid of the Sam Selvon Collection; collected in Ways of Sunlight (London: MacGibbon and Kee, 1957), "
         "which has its own record. A selection of The Norton Anthology of English Literature, 11th edition, vol. F "
         "(p. 737).",
  notes="The plot rests on an essay on Selvon's stories in Thresholds (University of Chichester) and on the text; the "
        "Evening Standard date comes from the collection's finding aid, seen as search extracts because the archive "
        "server was unavailable. The Thresholds author's recollection of hearing Selvon read it on Caribbean Voices was "
        "not confirmed.",
  ver="partially verified", sources=[THRESH, UWI, NAEL]),
]
