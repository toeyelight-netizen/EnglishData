"""Installment 10, wave 20: the rest of the English anthology's in-scope authors - Anne Carson,
Paul Muldoon, bpNichol, Hanif Kureishi, Carol Ann Duffy and Kiran Desai.

Three of them (Carson, bpNichol, Kureishi, Duffy, Desai) are new to the database; Muldoon is
recorded once per Norton selection (four poems, one long sequence). Nothing beyond the Norton
selections is recorded; an excerpt is recorded as the book it comes from (Desai).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL  # noqa: E402

AC = "Anne Carson"
PM = "Paul Muldoon"
BP = "bpNichol"
HK = "Hanif Kureishi"
CD = "Carol Ann Duffy"
KD = "Kiran Desai"

NIP = "Northern Irish Poetry and the Belfast Group"
POSTCOL = "Postcolonial Literature"
CONCRETE = "Concrete Poetry"
BLACKBRIT = "Black British Writing and the Windrush Generation"
SCOT = "The Scottish Literary Revival of the 1980s and 1990s"
SAS = "South Asian Literature in English"

W_AC = "Anne Carson (Wikipedia)"
W_AC_BRIT = "The Glass Essay (Britannica)"
W_PM = "Paul Muldoon (Wikipedia)"
GALWAY_7M = "7, Middagh Street (database entry, University of Galway)"
ENCY_MTB = "Meeting the British (poem guide, Encyclopedia.com)"
BRILL_WBL = "Chapter 3, Why Brownlee Left, in Paul Muldoon and the Language of Poetry (Brill, 2019)"
BRILL_MTB = "Chapter 5, Meeting the British, in Paul Muldoon and the Language of Poetry (Brill, 2019)"
BRILL_AOC = "Chapter 7, The Annals of Chile, in Paul Muldoon and the Language of Poetry (Brill, 2019)"
FEBHOUSE = "Denis Donoghue, House of the spirits (review of February House, The Boston Globe)"
FODEN_MTB = "Giles Foden, For me, Meeting the British blew away the very idea of certainty (The Guardian)"
CD_PEARLS = "Warming Her Pearls by Carol Ann Duffy (poem analysis page)"
CD_VALENTINE = "Valentine by Carol Ann Duffy (revision notes, Save My Exams)"
CD_MEDUSA = "Carol Ann Duffy, Medusa and Mrs Lazarus (Genius annotations)"
W_BP = "BpNichol (Wikipedia)"
BP_VISPO = "First Screening: Computer Poems by bpNichol (Rhizome, 2007)"
W_HK = "Hanif Kureishi (Wikipedia)"
DESAI_NYER = "Kiran Desai, 'The Sermon in the Guava Tree' (extract, The New Yorker, 23 June 1997)"
W_CD = "Carol Ann Duffy (Wikipedia)"
W_KD = "Kiran Desai (Wikipedia)"
DESAI_ECO = ("'Searching for an Environmental Identity: Hullabaloo in the Guava Orchard by Kiran Desai'"
             " (ResearchGate article)")

AUTHORS = [
A10(AC, MAJ, "1950", None, "Toronto, Ontario, Canada",
  "Canadian; poet, classicist, translator and essayist writing in English",
  "Canadian poet and classicist whose genre-breaking books - verse essays, translations of Sappho and "
  "Greek tragedy, and the novel-in-verse Autobiography of Red - made her one of the most original poets in "
  "English of her generation",
  "Anne Patricia Carson was born in Toronto on 21 June 1950 and grew up in a series of small Ontario towns, the "
  "daughter of a bank manager. She read classics at the University of Toronto (BA 1974), took an MA there and a "
  "PhD in classics at the University of Toronto in 1981, and taught classics and creative writing at the "
  "universities of Calgary, Princeton, Emory, McGill, Michigan and New York University. Her first books were "
  "academic - Eros the Bittersweet (1986), a study of desire in Sappho and the Greek lyric poets - and her "
  "poetry began with Short Talks (1992) and Plainwater (1995), followed by Glass, Irony and God (1995), "
  "Autobiography of Red (1998), Men in the Off Hours (2000), The Beauty of the Husband (2001), Decreation "
  "(2005), Nox (2010), Antigonick (2012), Red Doc> (2013), Float (2016) and Wrong Norma (2024), with "
  "translations of Sappho (If Not, Winter, 2002), Euripides (Bakkhai, 2015) and others. She has won the Lannan "
  "Literary Award, a MacArthur Fellowship, the Griffin Poetry Prize (twice), the T. S. Eliot Prize and the "
  "Princess of Asturias Award, and was appointed a Member of the Order of Canada in 2005.",
  "Poetry and verse prose: Short Talks (1992), Plainwater (1995), Glass, Irony and God (1995), Autobiography of "
  "Red (1998), Men in the Off Hours (2000), The Beauty of the Husband (2001), Decreation (2005), Nox (2010), "
  "Antigonick (2012), Red Doc> (2013), Float (2016) and Wrong Norma (2024). Criticism and essays: Eros the "
  "Bittersweet (1986) and The Albertine Workout (2014). Translations: If Not, Winter: Fragments of Sappho "
  "(2002), Grief Lessons: Four Plays by Euripides (2006), An Oresteia (2009) and Bakkhai (2015).",
  "A spare, epigrammatic, often flatly declarative free verse, with line breaks used as a form of argument; the "
  "collage of poetry, prose, quotation, translation and scholarly footnote; a tone of deadpan wit and sudden "
  "emotional exposure; long sequences built of short numbered sections.",
  "Desire, eros and the body; the classical tradition and its modern uses; translation and the fragment; "
  "siblings, marriage and the family romance; grief, absence and the failure of language; the essay as a poetic "
  "form and the poem as a form of thinking.",
  "Carson is the most formally inventive poet in English of her generation and the one who has done most to "
  "reopen the border between poetry, translation and the essay; her Sappho translations and her verse novel "
  "Autobiography of Red are standard points of reference in the study of contemporary poetry, and the Nobel "
  "Prize in 2026 confirmed a reputation long established among poets and critics.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Carson, read directly, and from general "
           "knowledge; they were not checked against a bibliography. Installment 10 records only the Norton "
           "selection, 'The Glass Essay' (Glass, Irony and God, 1995), printed as an extract; the other "
           "collections, the translations and the criticism have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_AC, W_AC_BRIT, NAEL]),
A10(PM, MAJ, "1951", None, "Portadown, County Armagh, Northern Ireland",
  "Northern Irish and Irish; poet, critic and editor writing in English",
  "Northern Irish poet whose formal virtuosity, sly wordplay and long sequences of oblique narrative made him "
  "the most influential Irish poet of the generation after Heaney",
  "Paul Muldoon was born on 20 June 1951 on a farm at The Moy, near Portadown in County Armagh, the eldest of "
  "three children of a farmer and a schoolteacher, and was educated at Queen's University Belfast, where he "
  "read English and came under the influence of Seamus Heaney and the Belfast Group. New Weather (1973) "
  "appeared while he was still a student; Mules (1977), Why Brownlee Left (1980), Quoof (1983), Meeting the "
  "British (1987), Madoc: A Mystery (1990), The Annals of Chile (1994, T. S. Eliot Prize), Hay (1998), Moy Sand "
  "and Gravel (2002, Pulitzer Prize), Horse Latitudes (2006), Maggot (2010), One Thousand Things Worth Knowing "
  "(2015) and Howdie-Skelp (2021) followed, with the critical collection To Ireland, I (2000) and the libretti "
  "and song cycles written with Warren Zanes and others. He worked as an arts producer for the BBC in Belfast "
  "from 1973 to 1986 and has taught at the University of East Anglia, Cambridge and Princeton, where he is "
  "Howard G. B. Clark '21 University Professor in the Humanities; he was Oxford Professor of Poetry from 1999 "
  "to 2004 and poetry editor of The New Yorker from 2007 to 2017.",
  "Poetry: New Weather (1973), Mules (1977), Why Brownlee Left (1980), Quoof (1983), Meeting the British (1987), "
  "Madoc: A Mystery (1990), The Annals of Chile (1994), Hay (1998), Moy Sand and Gravel (2002), Horse Latitudes "
  "(2006), Maggot (2010), One Thousand Things Worth Knowing (2015) and Howdie-Skelp (2021); Selected Poems "
  "1968-1986 (1986) and Poems 1968-1998 (2001). Criticism: To Ireland, I (2000).",
  "Extravagant, punning, syntactically dislocated verse that moves between strict traditional forms - sonnet, "
  "sestina, villanelle, haiku - and free verse; dense internal rhyme and assonance; long sequences of short "
  "sections in the voices of other people; a diction that mixes Ulster speech, literary allusion and obscure "
  "vocabulary.",
  "Northern Ireland, the Troubles and the inheritance of Irish history; language, translation and the "
  "untranslatability of experience; family, parents and the farm; the relation of art to politics and of the "
  "poet to his predecessors; exile, America and the crossing of borders.",
  "Muldoon has been the dominant formal presence in Irish poetry since the 1980s, and his influence on younger "
  "poets in Ireland, Britain and America has been decisive; the Pulitzer Prize and the T. S. Eliot Prize, "
  "together with his long tenure as The New Yorker's poetry editor, made him the most publicly prominent Irish "
  "poet of his generation after Heaney.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Muldoon, read directly, and from general "
           "knowledge; they were not checked against a bibliography. Installment 10 records only the Norton "
           "selections - 'Anseo', 'Meeting the British' and '7, Middagh Street' (Meeting the British, 1987) and "
           "'Milkweed and Monarch' (The Annals of Chile, 1994) - and 'Turtles' was dated out of the period "
           "(Horse Latitudes, 2006). The later collections have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_PM, GALWAY_7M, ENCY_MTB, NAEL]),
A10(BP, MAJ, "1944", "1988", "Vancouver, British Columbia, Canada",
  "Canadian; poet, sound poet, editor and children's writer working in English",
  "Canadian poet and sound poet, the central figure of the Toronto concrete and sound poetry scene, whose "
  "lifelong poem The Martyrology and early computer poems made language itself the subject of his work",
  "Barrie Phillip Nichol, who signed himself bpNichol, was born in Vancouver on 30 September 1944 and died in "
  "Toronto on 25 September 1988. He studied at the University of British Columbia and taught in Vancouver "
  "schools before moving to Toronto, where he became a central figure of the small-press and sound-poetry "
  "movement: he founded Ganglia Press with David Aylward in 1964 and the magazine grOnk in 1967, edited at "
  "Coach House Press from 1975, and was a member of the sound-poetry group The Four Horsemen with Rafael "
  "Barreto-Rivera, Paul Dutton and Steve McCaffery. His books include Journeying & the Returns (1967), "
  "Konfessions of an Elizabethan Fan Dancer (1969), Still Water (1970), The Martyrology (in nine books, "
  "1972-1990), Continental Trance (1978), Selected Organs (1988) and the computer poems First Screening (1984); "
  "he won the Governor General's Award for poetry in 1970 and wrote for the children's television series "
  "Fraggle Rock and The Raccoons.",
  "Poetry: Journeying & the Returns (1967), Konfessions of an Elizabethan Fan Dancer (1969), Still Water (1970), "
  "The Martyrology, Books 1-2 (1972), The Martyrology, Book 3 (1976), The Martyrology, Book 4 (1977), The "
  "Martyrology, Book 5 (1982), The Martyrology, Book 6 (1987), Book 7 (1990) and the posthumous Books 8-9; "
  "Continental Trance (1978), Selected Organs (1988) and First Screening: Computer Poems (1984, floppy disk). "
  "Children's books and television scripts, including Fraggle Rock and The Raccoons.",
  "Concrete and visual poetry that treats the page as a field; typewriter poems, hand-drawn letterforms, "
  "sound-poetry scores and performance texts; short lyric poems of great simplicity set against the "
  "proliferation of The Martyrology; the computer poems of First Screening, in which letters and words move and "
  "mutate on the screen.",
  "Language as material and as a system; the letter as image and as sound; the body in performance; "
  "spirituality and the 'saints' of The Martyrology, whose names are made from the letters of ordinary words; "
  "the relation of writing to reading and of the book to other media.",
  "bpNichol is the central figure of Canadian concrete and sound poetry and a pioneer of electronic literature: "
  "First Screening, made in 1983-84 on an Apple IIe, is among the earliest works of programmed kinetic poetry, "
  "and The Martyrology is one of the major long poems in Canadian literature. His selection in the Norton "
  "Anthology marks the recognition of Canadian avant-garde writing within the English tradition.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on bpNichol, read directly, from the Rhizome "
           "account of First Screening and from general knowledge; they were not checked against a "
           "bibliography. Installment 10 records only the Norton selection, First Screening (1984), as a whole "
           "work; the Martyrology books and the other collections have no records, so the bibliography is "
           "incomplete.",
  ver="partially verified", sources=[W_BP, BP_VISPO, NAEL]),
A10(HK, MAJ, "1954", None, "Bromley, Kent, England",
  "British; playwright, screenwriter and novelist writing in English",
  "British playwright, screenwriter and novelist of Pakistani descent whose plays and films of the 1980s and "
  "1990s made race, class and sexuality in Thatcher's Britain their central subject",
  "Hanif Kureishi was born on 5 December 1954 in Bromley, Kent, the son of an English mother and a Pakistani "
  "father who had come to Britain in 1950, and was educated at Bromley Technical High School, Lancaster "
  "University and King's College London, where he read philosophy. He began writing for the theatre at the "
  "Royal Court and the Hampstead Theatre in the 1970s; his screenplay for Stephen Frears's My Beautiful "
  "Laundrette (1985) was nominated for an Academy Award, and Sammy and Rosie Get Laid (1987) and London Kills "
  "Me (1989) followed. His plays include The King and Me (1980), Outskirts (1981), Borderline (1981), Birds of "
  "Passage (1983), The Mother Country (1984) and Sleep with Me (1999); his fiction includes The Buddha of "
  "Suburbia (1990, Whitbread First Novel Award), The Black Album (1995), Intimacy (1998), Gabriel's Gift "
  "(2001), Something to Tell You (2008) and The Last Word (2014), and the story collections Love in a Blue "
  "Time (1997), Midnight All Day (1999) and The Body (2003). His memoir Shattered (2024) records the spinal "
  "injury that left him paralysed in 2022.",
  "Plays: The King and Me (1980), Outskirts (1981), Borderline (1981), Birds of Passage (1983), The Mother "
  "Country (1984) and Sleep with Me (1999). Screenplays: My Beautiful Laundrette (1985), Sammy and Rosie Get "
  "Laid (1987) and London Kills Me (1989). Fiction: The Buddha of Suburbia (1990), The Black Album (1995), Love "
  "in a Blue Time (1997, stories), Intimacy (1998), Midnight All Day (1999), Gabriel's Gift (2001), The Body "
  "(2003), Something to Tell You (2008), The Last Word (2014) and Shattered (2024, memoir).",
  "A colloquial, fast-moving, comic prose and dialogue with a strong ear for London speech and for mixed "
  "registers; short scenes and abrupt shifts of tone; a taste for farce and for bodily comedy set against "
  "political argument; screenwriting techniques - cross-cutting, montage, close-up - carried into the fiction.",
  "Race, racism and the British Asian experience; class, money and social mobility under Thatcherism; "
  "sexuality and the family; popular culture, pop music and the media; religion, secularism and the rise of "
  "Islamic fundamentalism; fathers and sons.",
  "Kureishi is the central British Asian writer of his generation and one of the writers who changed the "
  "representation of black and Asian Britain on stage and screen in the 1980s; My Beautiful Laundrette and The "
  "Buddha of Suburbia are standard texts in the study of black British writing and of postcolonial London.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Kureishi, read directly, and from general "
           "knowledge; they were not checked against a bibliography. Installment 10 records only the Norton "
           "selection, 'My Son the Fanatic', a story first published in 1994 and collected in Love in a Blue "
           "Time (1997); the plays, films and novels have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_HK, NAEL]),
A10(CD, MAJ, "1955", None, "Glasgow, Scotland",
  "Scottish; poet and playwright writing in English",
  "Scottish poet and playwright, the first woman, the first Scot and the first openly gay poet to be Poet "
  "Laureate, whose dramatic monologues and love poems made her the most widely read British poet of her "
  "generation",
  "Carol Ann Duffy was born in the Gorbals, Glasgow, on 23 December 1955, to a Catholic family of Irish "
  "descent, and grew up in Stafford, where her father worked for English Electric. She read philosophy at the "
  "University of Liverpool and worked as a free-lance writer from 1985. Her collections are Standing Female "
  "Nude (1985), Selling Manhattan (1987, Somerset Maugham Award), The Other Country (1990), Mean Time (1993, "
  "Whitbread Poetry Award), Selected Poems (1994), The World's Wife (1999), Feminine Gospels (2002), Rapture "
  "(2005, T. S. Eliot Prize), The Bees (2011, Costa Poetry Award) and Sincerity (2018), with the plays "
  "Take My Husband (1982), Cavern of Dreams (1984), Little Women, Big Boys (1986), Loss (1986) and Casanova "
  "(1990), and the children's books and anthologies. She was appointed Poet Laureate in May 2009, the first "
  "woman to hold the post, and served until 2019; she is Professor of Contemporary Poetry at Manchester "
  "Metropolitan University.",
  "Poetry: Fleshweathercock (1973), Standing Female Nude (1985), Selling Manhattan (1987), The Other Country "
  "(1990), Mean Time (1993), Selected Poems (1994), The World's Wife (1999), Feminine Gospels (2002), New "
  "Selected Poems (2004), Rapture (2005), The Bees (2011) and Sincerity (2018). Plays: Take My Husband (1982), "
  "Cavern of Dreams (1984), Little Women, Big Boys (1986), Loss (1986) and Casanova (1990).",
  "Accessible, conversational free verse with a strong rhythmic pulse; the dramatic monologue used to give "
  "voice to the unheard - wives, servants, figures from myth and history; wordplay, puns and half-rhymes; "
  "short lines and sharp, often shocking images; a diction that moves easily between demotic speech and "
  "literary allusion.",
  "Love and desire, especially their painful and unequal forms; gender, power and the objectification of "
  "women; class, money and the servant's eye; the retelling of myth, fairy tale and history from a woman's "
  "point of view; memory, loss and the passage of time; Scotland, England and the languages of both.",
  "Duffy is the most widely read British poet of her generation and the first woman to be Poet Laureate; her "
  "poems are set texts in British schools to a degree unmatched by any contemporary, and The World's Wife has "
  "become one of the defining collections of the feminist rewriting of myth.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Duffy, read directly, and from general "
           "knowledge; they were not checked against a bibliography. Installment 10 records only the Norton "
           "selections - 'Warming Her Pearls' (Selling Manhattan, 1987), 'Valentine' (Mean Time, 1993) and "
           "'Medusa' and 'Mrs Lazarus' (The World's Wife, 1999); the other collections and the plays have no "
           "records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_CD, NAEL]),
]

WORKS = [
W10("The Glass Essay", AC, "1995", "Poem", "major",
  genres=G("Narrative Poetry", "Confessional Poetry", "Long Poem"),
  themes=T("Love, intimacy and loss", "Family, marriage and domestic life", "Language, writing and the limits of representation"),
  movements=M("Second-Wave Feminist Writing"),
  overview="Anne Carson's long poem from Glass, Irony and God (1995): a woman visits her mother in the country "
           "after a love affair ends, rereads Emily Brontë, and finds in Brontë's solitude and in the 'Nudes' "
           "she hallucinates an image of her own grief, in a poem that mixes lyric, narrative and literary "
           "criticism.",
  content="A sequence of nine numbered sections, mixing lyric, narrative and essay, in which the speaker travels "
          "to her mother's house, reads Emily Brontë's poems and Wuthering Heights, describes the 'Nudes' that "
          "appear to her in bed and on the road, and considers the end of a love affair and the decline of her "
          "father.",
  summary="The poem begins with a journey: 'I travel all day on trains and bring a lot of books - / some for my "
          "mother, some for me / including The Collected Works of Emily Brontë. / This is my favourite author. "
          "/ Also my main fear, which I mean to confront.' The speaker has come to visit her mother in the "
          "country after the end of an affair, and the flat, wintry landscape around her mother's house makes "
          "her feel she is turning into Emily Brontë - solitary, exposed, walking the moor, 'my ungainly body "
          "stumping over the mud flats'. The visit is ordinary and sad: the mother is brisk and unsentimental, "
          "the father is in a nursing home with Alzheimer's disease, and the speaker sleeps badly, wakes "
          "thinking of the man she calls Law, and sees in the mirror a face she hardly recognises. Throughout, "
          "she reads Brontë: the poems 'not at all like the poetry women generally write', the isolation of the "
          "Haworth parsonage, the death-haunted biography, and the accusation that Brontë's work is 'too much "
          "about the self'. Interleaved with this are the 'Nudes' - hallucinated figures of a woman, naked and "
          "exposed, that appear to her at the edge of sleep and grow more real and more compassionate as the "
          "poem goes on. The sections move between the mother's kitchen, the nursing home, the train, "
          "Brontë's letters and the snow-covered fields, and the poem ends without consolation, in a quiet "
          "acceptance that the self is not cured by reading or writing but is, for a moment, held.",
  themes_text="The poem's subject is grief that has no socially sanctioned form - the grief of a woman abandoned "
              "by a lover, which the poem examines with the same seriousness as death - and it puts that grief "
              "beside Brontë's, whose loneliness is both a literary inheritance and a warning. Carson refuses "
              "the confessional bargain of the 'sincere' poem: 'The Glass Essay' quotes, translates, "
              "annotates and essayises, and its intellectual work is part of its feeling, not a retreat from "
              "it. The mother-daughter relation, the failing father and the 'three silent women at the kitchen "
              "table' - mother, daughter and Brontë - make a counter-family of women whose intimacy is "
              "partly made of reading, and the Nudes, which begin as images of exposure, become a way of "
              "imagining a female suffering that is not shameful and not alone.",
  structure="Nine numbered sections in a loose, long-lined free verse that often reads as prose; the sections "
            "shift between first-person narrative, close reading of Brontë's poems and of the 'Nudes', and "
            "disquisition on sound, hysteria and the gendering of emotion; the poem's continuity is thematic "
            "and imagistic rather than plotted, and its length (some thirty pages) makes it a verse essay.",
  style="A style at once plain and strange: short declarative sentences, exact physical detail ('The April light "
        "is clear as an alarm'), and sudden abstract questions; the incorporation of quotation, footnote and "
        "scholarly aside; a deadpan humour (Aristotle's 'women are like things / that speak') set against "
        "passages of great tenderness; no regular metre or rhyme, but a strong rhythmic line shaped by "
        "breath and syntax.",
  ctx="Glass, Irony and God was published by New Directions in 1995 and gathered 'The Glass Essay', 'Book of "
      "Isaiah' and 'The Fall of Rome'; Carson had already published Eros the Bittersweet (1986) and "
      "Plainwater (1995), and the poem's mixture of classics, autobiography and literary criticism became the "
      "model for much of her later work. Its Brontë material belongs to the feminist rereading of the "
      "nineteenth-century woman writer, and its form to the tradition of the long poem as essay that runs from "
      "the Romantics through to the twentieth century.",
  sig="The poem that established Carson's reputation with a general readership and the most widely discussed of "
      "her works; it is her selection in the Norton Anthology, printed as an extract, and it is a standard "
      "text in courses on the long poem, on the essay and on contemporary Canadian poetry.",
  canon="Major canon",
  crit="Criticism has treated 'The Glass Essay' as the defining example of Carson's mixed-genre poetics: "
       "readings of the poem have concentrated on its use of Brontë as a double, on the 'Nudes' as figures for "
       "the female body in pain, and on the essay form as a way of thinking through feeling. The poem is "
       "central to the critical case for Carson as a poet who has renewed the long poem, and it is frequently "
       "compared with her later verse novels and with the confessional tradition she is said to have revised "
       "rather than continued; its account of reading as consolation and of consolation's limits has been "
       "influential in discussions of literature and grief.",
  biblio="Published in Glass, Irony and God (New York: New Directions, 1995). A selection of The Norton "
         "Anthology of English Literature, 11th edition, vol. F, beginning on page 1075; the Norton text is an "
         "extract, and this record covers the whole poem.",
  notes="The text was read in substantial part through the quotations in the reviews and study material cited "
        "and through the opening passages reproduced in them; the poem was not read complete. The accounts of "
        "the nine sections, the Nudes and the poem's ending follow those sources and general knowledge.",
  ver="partially verified", sources=[W_AC, W_AC_BRIT, NAEL]),
]

WORKS += [
W10("Anseo", PM, "1980", "Poem", "significant",
  genres=G("Narrative Poetry", "Lyric Poetry", "Political Poetry"),
  themes=T("Nationhood and national identity", "Education, institutions and the academy", "War, combat and its aftermath"),
  movements=M(NIP),
  overview="A poem from Why Brownlee Left (1980) about a school roll call in Irish - 'Anseo', here - and the "
           "schoolboy, Joseph Mary Plunkett Ward, who learns obedience in the classroom and later commands an "
           "IRA unit.",
  content="A short narrative poem in several unrhymed stanzas: the master calls the roll, the boys answer "
          "'Anseo', and one of them, Ward, is beaten into answering and later answers to a different name and "
          "a different kind of roll call.",
  summary="The poem opens with the word itself: 'Anseo' is the first word of Irish the speaker learned, 'the "
          "first word of Irish I spoke', and it means 'here, here and now, / All present and correct'. The "
          "scene is a classroom in a Catholic school in the north, where the master, with 'an ash-plant, a "
          "salley-rod', calls the roll in Irish and the boys must answer. Joseph Mary Plunkett Ward is the "
          "boy who does not answer, who is late, who is beaten; the poem follows him through the school's "
          "regime of punishment - the master's 'careful' violence, the naming of the boys after Irish "
          "patriots - until he leaves. The last stanza jumps forward: Ward, now 'Joe Ward', the diminutive "
          "marking his change, is a commandant of an IRA unit, and 'His volunteers would call back Anseo / "
          "And raise their hands / As their names occurred.' The poem does not comment. It shows a single "
          "word carrying both the intimacy of a language and the discipline of an army, and leaves the reader "
          "to see how the schoolroom's obedience became the paramilitary's.",
  themes_text="The poem is about the Irish language as a shibboleth and as an instrument of authority: 'Anseo' "
              "is the word of presence and of being accounted for, and Muldoon lets it pass from the roll call "
              "of a primary school to the roll call of an IRA unit without a break. Education, punishment and "
              "nationalist inheritance are shown as a single system, and the poem's irony is directed at the "
              "schooling that produced soldiers - the boys named after the executed leaders of 1916 become "
              "the volunteers of the 1970s. The Norther Ireland of the Troubles is present only at the edges, "
              "in the name of the master, the ash-plant and the final roll call, and the poem's restraint is "
              "part of its judgement.",
  structure="A short narrative in unrhymed quatrains and longer stanzas, moving chronologically from the roll "
            "call to the beating to the leap forward to Ward's command; the last stanza repeats the answering "
            "word and gesture of the first, closing the poem on a rhyme of institutions.",
  style="Spare, exact, colloquial verse with a strong iambic pulse, short lines and abrupt enjambment; a "
        "mixture of Irish words, Northern Irish speech ('He would arrive as a matter of course') and literary "
        "naming; almost no metaphor, and no overt comment; a tone of dry, withheld irony.",
  ctx="Why Brownlee Left (Faber, 1980) was Muldoon's third collection and the one in which the Troubles and his "
      "County Armagh childhood became explicit subjects; 'Anseo' is one of a group of poems about school, "
      "family and the inheritance of Irish nationalism, and its Irish-language title belongs to the period's "
      "debate over language and identity in the north.",
  sig="One of Muldoon's most anthologised and most taught poems, a standard text on the Troubles and on the "
      "politics of language in Northern Irish poetry; it is his first selection in the Norton Anthology.",
  canon="Secondary canon",
  biblio="Published in Why Brownlee Left (London: Faber and Faber, 1980). A selection of The Norton Anthology of "
         "English Literature, 11th edition, vol. F, beginning on page 1080.",
  notes="The poem was not read complete; the account follows the quotations and discussion in the Brill chapter "
        "on Why Brownlee Left, the Galway poem database entries, the Slate review of the Selected Poems and "
        "general knowledge, which agree on the roll call, Ward's name and the IRA ending.",
  ver="partially verified", sources=[W_PM, BRILL_WBL, GALWAY_7M, NAEL]),
W10("Meeting the British", PM, "1987", "Poem", "significant",
  genres=G("Narrative Poetry", "Dramatic Poetry", "Political Poetry"),
  themes=T("Decolonisation, the end of empire and the new nation", "Race, racism and the struggle for civil rights", "Violence, crime and justice"),
  movements=M(NIP, POSTCOL),
  overview="The title poem of Muldoon's 1987 collection: an eighteenth-century Native American speaker recalls "
           "the winter meeting with General Amherst and Colonel Bouquet, who gave his people six fishhooks and "
           "two blankets embroidered with smallpox.",
  content="An eighteen-line poem in a single stanza, spoken by a Native American who describes a meeting with "
          "two British officers in a forest clearing, the exchange of willow-tobacco and scented handkerchief, "
          "and the gifts that carry disease.",
  summary="'We met the British in the dead of winter.' The speaker, a Native American, describes the meeting in a "
          "forest clearing: the sky lavender, the snow lavender-blue, two frozen streams coming together, and "
          "the strangeness of hearing himself 'calling out in French across that forest-clearing'. General "
          "Jeffrey Amherst and Colonel Henry Bouquet cannot stomach the people's willow-tobacco; the Colonel "
          "shakes out a handkerchief and explains, in French, that the scent is lavender, 'une fleur mauve "
          "comme le ciel'. The poem ends with the transaction: 'They gave us six fishhooks / and two blankets "
          "embroidered with smallpox.' Nothing follows: no reaction, no death, no reflection. The withheld "
          "last word is the poem's whole meaning, and the courteous, scented, lavender-coloured scene is "
          "revealed as the setting of a deliberate act of biological warfare.",
  themes_text="The poem dramatises the colonial encounter as a failed and fatal act of communication: the "
              "speaker's French, the Colonel's French, the lavender and the smallpox all belong to a "
              "vocabulary the Native Americans are given but cannot control. Muldoon's subject is the "
              "'gift' as an instrument of empire, and the poem's historical reference - the blankets "
              "distributed at Fort Pitt during Pontiac's War in 1763 - makes it an indictment of British "
              "colonial practice that Irish readers have always read as an analogy for their own history. The "
              "poem's brevity and its refusal of lament are the source of its anger: the atrocity is delivered "
              "as a courtesy, in the tone of a travel anecdote.",
  structure="A single eighteen-line stanza of short lines without stanza breaks; the poem proceeds as a "
            "first-person anecdote in the past tense, with two lines of quoted French, and closes on a single "
            "sentence that delivers the poem's withheld information.",
  style="Flat, understated, almost prosaic free verse with a strong stress pulse; exact colour words (lavender, "
        "mauve) and precise physical detail (frozen streams, fishhooks, embroidered blankets); the "
        "juxtaposition of French quotation and English reportage; no metaphor except the terrible one of the "
        "embroidery.",
  ctx="Meeting the British (Faber, 1987) was Muldoon's fifth collection, published in the year he moved to the "
      "United States; the title poem draws on the documented distribution of smallpox-contaminated blankets "
      "to Delaware delegates at Fort Pitt in 1763, during Pontiac's War, and belongs to the 1980s Irish "
      "debate about colonialism, the north and the uses of history.",
  sig="One of Muldoon's best known and most frequently anthologised poems, a standard text in postcolonial "
      "criticism of Irish poetry; it is one of his selections in the Norton Anthology and gives its title to "
      "the collection.",
  canon="Secondary canon",
  biblio="Published in Meeting the British (London: Faber and Faber, 1987). A selection of The Norton Anthology "
         "of English Literature, 11th edition, vol. F, beginning on page 1081.",
  notes="The poem's text was read complete through the reproduction in the Tumblr poetry post and the analysis "
        "pages cited, which agree word for word; the historical background follows the Encyclopedia.com guide "
        "and the accounts of the Fort Pitt incident in the sources cited.",
  ver="partially verified", sources=[ENCY_MTB, W_PM, NAEL]),
]

WORKS += [
W10("7, Middagh Street", PM, "1987", "Poem", "significant",
  genres=G("Dramatic Poetry", "Narrative Poetry", "Long Poem"),
  themes=T("Art, the artist and the creative life", "War, combat and its aftermath", "History, truth and the uses of the past"),
  movements=M(NIP),
  overview="A long sequence at the end of Meeting the British (1987) in which seven people who lived or visited "
           "the house at 7 Middagh Street, Brooklyn Heights, in 1940-41 - Auden, Gypsy Rose Lee, Britten, "
           "Kallman, Dalí, McCullers and MacNeice - speak in turn.",
  content="A sequence of some twenty pages of monologues in different metres and forms, spoken by the seven "
          "inhabitants of the Brooklyn house in the winter of 1940-41, about art, politics, sex and the war in "
          "Europe.",
  summary="The poem is set in a rented house in Brooklyn Heights where, in 1940-41, W. H. Auden, the "
          "burlesque dancer Gypsy Rose Lee, the composer Benjamin Britten, Auden's lover Chester Kallman, the "
          "painter Salvador Dalí, the novelist Carson McCullers and the poet Louis MacNeice lodged or visited. "
          "Each of the seven speaks in turn, and Muldoon writes each in a form suited to the voice: Auden in "
          "tetrameters and syllabics, lectures and catechisms; Gypsy Rose Lee in the language of the stage; "
          "Britten in letters and musical notation; Dalí in outrageous aphorisms; McCullers in a prose that "
          "echoes her own fiction; MacNeice in lyric stanzas and in his diaries' idiom. Across the sequence "
          "the talk is of art and its uses, of the war in Europe and the United States' non-intervention, of "
          "sex and of money. The poem's frame is the question of what a community of artists is for: the house "
          "is a 'February House', a temporary gathering of people with nothing in common but their work, and "
          "Muldoon lets each speak his or her own prejudices and self-deceptions. The sequence ends with "
          "MacNeice, the poet closest to Muldoon in background and trade, and with a movement out of the house "
          "and into the war.",
  themes_text="The poem is a study of the relation between art and politics: the artists in the house are "
              "famous, self-absorbed and mostly wrong about the war and about themselves, and Muldoon's "
              "ventriloquism lets their voices be brilliant and unreliable at once. The house at 7 Middagh "
              "Street is an image of modernism in exile, a community of gay and eccentric artists in wartime "
              "Brooklyn, and the sequence's interest in money, sex and reputation is a corrective to the idea "
              "of modernist purity. The Irish strand (MacNeice and, through him, Muldoon's own Northern Irish "
              "inheritance) makes the poem a meditation on what a poet from a small country does with the "
              "great moderns.",
  structure="A sequence of seven monologues, each in a different form and voice, with a prologue and "
            "interconnecting passages; the poem is one of Muldoon's longest and most architecturally "
            "organised, using section numbers, changing line lengths and typography to distinguish voices, "
            "and closing with MacNeice's section as a coda.",
  style="A polyphonic poem whose style changes with each speaker; Auden's section is metrical, didactic and "
        "colloquial, Gypsy Rose Lee's is theatrical and punning, McCullers's is lyrical and gothic, MacNeice's "
        "is plain, wry and occasional; throughout, Muldoon's own wordplay and rhymes surface in every voice.",
  ctx="Meeting the British (Faber, 1987) ends with '7, Middagh Street', written after Muldoon had moved from "
      "Belfast to Cambridge and then to the United States; the house at 7 Middagh Street was the 'February "
      "House' described in Sherill Tippins's book of that name, and the poem draws on Auden's and MacNeice's "
      "correspondence and on the history of the period 1940-41, when Britain stood alone and the United "
      "States was not yet at war.",
  sig="Muldoon's most ambitious long poem of the 1980s and the one that established his interest in the "
      "sequence and in the ventriloquism of historical voices; it is one of his selections in the Norton "
      "Anthology, printed as an extract, and a standard point of reference in criticism of his politics and "
      "poetics.",
  canon="Secondary canon",
  biblio="Published in Meeting the British (London: Faber and Faber, 1987); the sequence runs to some twenty "
         "pages in Poems 1968-1998 (Faber, 2001), pp. 175-193. A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning on page 1082, where it is printed with the opening line "
         "'(And were Yeats living at this hour)'; the Norton text is an extract, and this record covers the "
         "whole sequence.",
  notes="The sequence was not read complete; the account follows the Brill chapter on Meeting the British, the "
        "Galway poem database entry, the Boston Globe account of February House and the Guardian essay by "
        "Giles Foden, which agree on the seven speakers, the house and the poem's concerns.",
  ver="partially verified", sources=[BRILL_MTB, GALWAY_7M, FEBHOUSE, FODEN_MTB, NAEL]),
W10("Milkweed and Monarch", PM, "1994", "Poem", "significant",
  genres=G("Elegiac Poetry", "Formal Verse", "Confessional Poetry"),
  themes=T("Death, illness and mourning", "Family, marriage and domestic life", "Love, intimacy and loss"),
  movements=M(NIP),
  overview="A villanelle from The Annals of Chile (1994) in which the poet kneels at his parents' grave and finds "
           "his mouth filled not with grief for them but with the taste of a former lover's pickled gherkin.",
  content="A twenty-five-line poem in seven tercets and a quatrain, built on two refrains, in which a visit to "
          "the grave of the speaker's mother and father gives way to memories of a woman and of the plants and "
          "foods of childhood.",
  summary="'As he knelt by the grave of his mother and father / the taste of dill, or tarragon - / he could "
          "barely tell one from the other - / filled his mouth.' The poem's opening moves from the grave to the "
          "palate, and its confusion of the two parents is also a confusion of places and times: the graveyard "
          "at Collegelands, the herbs of an Irish childhood, the American sea otter and the 'pickled gherkin' "
          "of a girlfriend in the United States, the Cliffs of Moher and a Russian samovar. The refrains turn "
          "on the doubles of the title - milkweed and monarch, the plant and the butterfly that feeds on it, "
          "inseparable and mutually dependent - and on the speaker's inability to 'tell one from the other'. "
          "The poem's central grief is displaced: the dead parents are half-forgotten in the surge of erotic "
          "memory, and the mother's name ('Regan') is misread as 'Anger', which is the poem's admission of "
          "what it feels. The last tercets return to the grave, and the quatrain closes on the doubled "
          "refrain, so that the elegy ends in the state of not being able to distinguish, which the poem has "
          "made its form.",
  themes_text="The poem is about the way grief is contaminated by other feelings: the speaker cannot mourn his "
              "parents without the intrusion of a lover, and cannot think of the lover without the parents' "
              "grave. Muldoon uses the villanelle's two refrains as the vehicle of that doubleness, so that "
              "the form itself performs the confusion of identities, and the poem's wit - 'savour', "
              "'palaver', 'Moher', 'samovar' - is not decoration but the mind's attempt to keep moving. The "
              "poem is also an elegy for a marriage and for a childhood landscape, and its refusal of "
              "decorum (anger, erotic memory and food at the graveside) is a deliberate breach of the "
              "conventions of the elegy.",
  structure="A villanelle in twenty-five lines: seven tercets and a closing quatrain, with two refrains that "
            "alternate and recur; the poem's syntax runs across the stanza breaks, and the rhymes are "
            "half-rhymes and assonantal chimes rather than full rhymes, so that the form is both strict and "
            "unsettled.",
  style="Highly wrought, punning verse with a strong rhyme-drive and a diction that mixes the literary (Moher, "
        "samovar) with the domestic (gherkin, dill, tarragon); short lines, heavy enjambment and internal "
        "echoes; a tone of dry, wounded irony that breaks into tenderness at the refrains.",
  ctx="The Annals of Chile (Faber, 1994) won the T. S. Eliot Prize and contains 'Incantata', the elegy for the "
      "artist Mary Farl Powers, and 'Yarrow', as well as 'Milkweed and Monarch', written after the deaths of "
      "Muldoon's mother (1974) and father (1985); the poem's graveyard is at Collegelands, near The Moy, and "
      "its American material belongs to the years Muldoon spent teaching in the United States from 1987.",
  sig="One of the most admired short poems of Muldoon's middle period and a frequently anthologised modern "
      "villanelle; it is one of his selections in the Norton Anthology and the poem through which his use of "
      "fixed forms is usually introduced.",
  canon="Secondary canon",
  biblio="Published in The Annals of Chile (London: Faber and Faber, 1994). A selection of The Norton Anthology "
         "of English Literature, 11th edition, vol. F, beginning on page 1083.",
  notes="The poem's opening and several lines were read through the quotations in the Brill chapter, The "
        "Independent's review of The Annals of Chile and the study pages cited, which agree on the villanelle "
        "form, the refrains and the poem's occasion; it was not read complete.",
  ver="partially verified", sources=[BRILL_AOC, W_PM, NAEL]),
]

WORKS += [
W10("First Screening", BP, "1984", "Digital poetry suite", "significant",
  genres=G("Concrete Poetry", "Visual Poetry", "Experimental Poetry"),
  themes=T("Language, writing and the limits of representation", "Technology, media and consumer society", "Art, the artist and the creative life"),
  movements=M(CONCRETE),
  overview="A suite of twelve kinetic poems that bpNichol programmed in Apple BASIC on an Apple IIe in 1983-84 "
           "and issued through Underwhich Editions on a 5.25-inch floppy disk: an early and influential work of "
           "electronic literature.",
  content="Twelve short programmed poems in which letters and words move, mutate, dissolve and re-form on the "
          "screen; distributed as a signed floppy disk with printed matter, later recreated in HyperCard and "
          "JavaScript.",
  summary="First Screening was made in 1983 and 1984, when Nichol taught himself enough Apple BASIC to program "
          "the Apple IIe. The suite consists of twelve poems, each a short program: in one, a letter travels "
          "across the screen and returns; in another, words fall apart into their letters and reassemble; in "
          "another, a line of text scrolls and loops. The poems have no printed page. Their unit is the screen "
          "and the cycle of the loop, and their meaning is inseparable from the movement: a word that "
          "dissolves as you watch it cannot be read the way a printed word is read. 'Off-Screen Romance', one "
          "of the best known of the twelve, sends words across the screen like dancers. Nichol issued the suite "
          "through Underwhich Editions as 100 numbered and signed copies on 5.25-inch disks with printed "
          "matter, and it soon became inaccessible as the Apple IIe and then the HyperCard platform died; it "
          "was recreated in HyperCard by J. B. Hohm in 1992 and in JavaScript by Jim Andrews and others in "
          "2007, and those recreations are now the usual way the work is read.",
  themes_text="First Screening continues Nichol's concrete-poetry concern with the letter as a visual and "
              "material object, but it adds time: the poem is a sequence of positions and transformations "
              "rather than a static arrangement, and the reader's attention is held by the movement rather "
              "than the page. The suite's subject is the instability of language - words that will not stay "
              "put, letters that lose their place - and, implicitly, the new medium's own fragility: the work "
              "was made obsolete within a decade of its making, and its history is now part of what it is "
              "about.",
  structure="Twelve separate short programs, each a self-contained poem, presented in sequence on a floppy disk; "
            "each runs as a loop, so the poem has no fixed beginning or end, and the suite as a whole is "
            "organised as a set of variations on movement and transformation rather than as a narrative.",
  style="Programmed kinetic typography: capital and lower-case letters, words and short phrases moved by BASIC "
        "commands; simple line-drawn shapes and colour changes; repetition, looping and delay as rhythmic "
        "devices; the aesthetic is that of the typewriter poem and the animated cartoon at once.",
  ctx="Nichol made First Screening after two decades of typewriter and concrete poetry, and issued it through "
      "Underwhich Editions, the imprint he had founded in 1979; it belongs to the first wave of literary works "
      "made for the personal computer, alongside the experiments of the 1980s in hypertext and computer "
      "animation, and it has become a founding example in the historiography of electronic literature.",
  sig="One of the earliest works of programmed kinetic poetry in English and the work through which Nichol is "
      "known in the field of electronic literature; its selection in the Norton Anthology is a landmark in the "
      "anthologising of digital writing, and its reconstruction history is a standard case study in the "
      "preservation of born-digital art.",
  canon="Secondary canon",
  biblio="Programmed in Apple BASIC on the Apple IIe in 1983-84 and issued by Underwhich Editions (Toronto, 1984) "
         "as 100 numbered and signed copies on 5.25-inch floppy disks with printed matter. Recreated in "
         "HyperCard by J. B. Hohm (1992) and in JavaScript by Jim Andrews, Geof Huth, Lionel Kearns, Marko "
         "Niemi and Dan Waber (2007). A selection of The Norton Anthology of English Literature, 11th edition, "
         "vol. F, at page 1117.",
  notes="The work was not run in its original form. The account follows the Rhizome editorial on the 2007 "
        "reconstruction, which reproduces the history of the Underwhich edition, and the Wikipedia article on "
        "bpNichol; the descriptions of individual poems are limited to those named in those sources.",
  ver="partially verified", sources=[BP_VISPO, W_BP, NAEL]),
W10("My Son the Fanatic", HK, "1994", "Short story", "significant",
  genres=G("Short Story", "Domestic Fiction", "Social Novel"),
  themes=T("Faith, doubt and the sacred", "Race, racism and the struggle for civil rights", "Family, marriage and domestic life"),
  movements=M(BLACKBRIT, POSTCOL),
  overview="A story first published in 1994 and collected in Love in a Blue Time (1997): Parvez, a Pakistani taxi "
           "driver in an English city, watches his son Ali reject his parents' assimilated life for a strict "
           "Islam, and cannot understand what has happened to him.",
  content="A short story in six or seven scenes, in which Parvez investigates his son's change of life, "
          "consults his friends and a prostitute named Bettina, takes Ali to dinner, and finally confronts him "
          "with violence.",
  summary="Parvez, a Pakistani immigrant who has driven a taxi in an unnamed English city for more than twenty "
          "years, notices that his son Ali is behaving strangely: he has stopped eating with the family, given "
          "up his accounting studies for prayer, thrown away his tapes and clothes, and grown a beard. Fearing "
          "drugs, Parvez searches Ali's room and finds a prayer mat and a Quran. He consults his two closest "
          "friends, who advise him that the boy must be on drugs, and Bettina, a prostitute he drives "
          "regularly, who tells him to look in the boy's room and then, later, to talk to him. Parvez takes "
          "Ali to a restaurant, where he drinks too much and Ali lectures him on the filth of the West, on "
          "his drinking and on his friendship with a prostitute. When Bettina later tries to talk to Ali in "
          "the taxi, Ali insults her and she leaves. The story ends with Parvez, drunk and enraged, going into "
          "his son's room and beating him, while Ali neither defends himself nor retaliates; the last words of "
          "the story are Ali's: 'So who's the fanatic now?'",
  themes_text="The story is about the failure of a father's model of assimilation: Parvez has worked to become "
              "English, and his son's religion exposes the bargain as a loss. Kureishi refuses to make either "
              "position simply right: Ali's Islam is shown as rigid and intolerant, but the West Parvez "
              "defends is one of drinking, prostitutes and the money that pays for both, and the story's "
              "sympathy is with the father's bewilderment rather than his values. The conflict between "
              "generations, between secular and religious authority, and between an immigrant's public "
              "performance of belonging and his private life is played out in domestic scenes, and the ending "
              "- violence answered by a question - leaves the moral judgement unresolved.",
  structure="A short story in a series of short scenes, told in the third person from Parvez's point of view, "
            "moving between the taxi, the family house, his friends' shop and the restaurant; the story's "
            "dialogue carries most of the action, and its ending with Ali's question is a deliberate reversal "
            "of the title.",
  style="Colloquial, fast-moving prose with a strong ear for the speech of the taxi trade and the immigrant "
        "household; free indirect style used to render Parvez's puzzlement; comedy of embarrassment and "
        "misunderstanding; short paragraphs and abrupt cuts, as in a screenplay.",
  ctx="The story was first published in 1994 and collected in Love in a Blue Time (Faber, 1997), Kureishi's first "
      "collection of stories; it belongs to the British Asian writing of the 1990s and to the decade's debate "
      "about Islam, race and multiculturalism in Britain, and was filmed by Udayan Prasad in 1997 with Om Puri "
      "and Rachel Griffiths.",
  sig="One of Kureishi's most widely taught stories and a set text in British schools on identity and "
      "multiculturalism; it is his selection in the Norton Anthology and the story most often used to "
      "introduce his fiction.",
  canon="Secondary canon",
  biblio="First published in 1994 and collected in Love in a Blue Time (London: Faber and Faber, 1997). A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 1151.",
  notes="The plot follows the paraphrase on the Wikipedia article and the several summaries read as search "
        "extracts, which agree on Parvez, Ali, Bettina and the closing question; the story was not read "
        "complete, and the first publication year and the collection date are those given in those sources.",
  ver="partially verified", sources=[W_HK, DESAI_NYER, NAEL]),
]

WORKS += [
W10("Warming Her Pearls", CD, "1987", "Poem", "significant",
  genres=G("Dramatic Monologue", "Lyric Poetry", "Love Poetry"),
  themes=T("Class, labour and social mobility", "Sexuality, desire and the closet", "Gender, feminism and women's lives"),
  movements=M("Second-Wave Feminist Writing", SCOT),
  overview="A poem from Selling Manhattan (1987) spoken by a maid who is made to wear her mistress's pearl "
           "necklace against her skin all day, to warm it, and whose service becomes an unspoken and unreturned "
           "desire.",
  content="A dramatic monologue in six quatrains in which the maid describes the daily ritual of the pearls, the "
          "mistress's toilette, her own attic bed and her sleepless nights, and admits at last that she burns.",
  summary="'Next to my own skin, her pearls.' The maid speaks: her mistress bids her wear the pearls and warm them "
          "until evening, when she will brush her hair and fasten them round her 'cool, white throat'. All day "
          "she thinks of her mistress in the Yellow Room, choosing between silk and taffeta, fanning herself, "
          "while the maid works 'willingly, my slow heat entering / each pearl'. The necklace is 'slack on my "
          "neck, her rope' - an image of both intimacy and servitude. In the attic at night she dreams of her, "
          "pictures her dancing with tall men, and feels the pearls' absence cooling in the room below: 'All "
          "night / I feel their absence and I burn.' The poem never names the desire as lesbian or as hopeless; "
          "it is carried entirely by the pearls, which pass between the two women's bodies and hold the maid's "
          "heat against the mistress's skin. The class relation is inseparable from the erotic one: the "
          "mistress's beauty is the product of the maid's labour, and the intimacy the maid is allowed is the "
          "intimacy of service.",
  themes_text="The poem is about desire that can only be expressed as work: the maid's body heats the pearls that "
              "will decorate another woman's body, and her feeling is transferred along with her warmth. Duffy "
              "makes the Victorian and Edwardian household - the Yellow Room, the toilette, the attic - the "
              "setting for a study of class and sexuality together, so that the power that keeps the maid in "
              "service is the same power that makes her desire unspeakable. The pearls are a fetish in the "
              "precise sense: an object that stands for a body and carries its heat, and the poem's final "
              "burn is both sexual frustration and the physical resentment of a servant.",
  structure="Six quatrains in loose iambic pentameter, unrhymed but heavily alliterative and assonantal; the "
            "poem moves through a single day and night, from the morning putting-on of the pearls to the "
            "night-time absence, and ends on a one-line sentence that breaks the stanza's flow.",
  style="Restrained, sensuous, cool in diction and hot in implication; long vowel sounds and soft consonants; "
        "domestic detail used as erotic notation (skin, throat, hair, heat); the tone is that of a servant's "
        "even and uncomplaining report, which makes the last line's 'I burn' a shock.",
  ctx="Selling Manhattan (Anvil Press, 1987) was Duffy's second major collection and won the Somerset Maugham "
      "Award; the poem draws on the historical practice of warming pearls against the skin to improve their "
      "lustre, and belongs to the 1980s revival of the dramatic monologue and to the lesbian and feminist "
      "poetry of the period.",
  sig="One of the most anthologised poems of Duffy's early career and a standard text on desire, class and the "
      "dramatic monologue in modern British poetry; it is her first selection in the Norton Anthology.",
  canon="Secondary canon",
  biblio="Published in Selling Manhattan (London: Anvil Press Poetry, 1987). A selection of The Norton Anthology "
         "of English Literature, 11th edition, vol. F, beginning on page 1159.",
  notes="The poem was read complete in the text reproduced on the Poem Analysis page; the reading of the class "
        "and desire material follows that page and general criticism, and the historical note on warming "
        "pearls is that page's account, not verified elsewhere.",
  ver="partially verified", sources=[CD_PEARLS, W_CD, NAEL]),
W10("Valentine", CD, "1993", "Poem", "significant",
  genres=G("Lyric Poetry", "Love Poetry", "Free Verse"),
  themes=T("Love, intimacy and loss", "Gender, feminism and women's lives", "Language, writing and the limits of representation"),
  movements=M("Second-Wave Feminist Writing", SCOT),
  overview="A poem from Mean Time (1993) that offers an onion instead of a rose or a satin heart, and uses it to "
           "say what love is actually like: layered, tear-making, possessive and lasting.",
  content="A short poem in irregular free-verse stanzas, in which the speaker gives her lover an onion, compares "
          "it to the moon wrapped in brown paper, to tears and to a wedding ring, and warns that its scent will "
          "cling to the knife.",
  summary="The poem opens by refusing the conventional Valentine - 'Not a red rose or a satin heart' - and offers "
          "the onion instead: 'It is a moon wrapped in brown paper. / It promises light / like the careful "
          "undressing of love.' The onion will make the lover cry, as love does, and will turn her reflection "
          "into 'a wobbling photo of grief'. The speaker insists on it - 'I am trying to be truthful' - and "
          "rejects the commercial tokens, 'a cute card or a kissogram'. Then the poem's second half darkens: "
          "the onion's 'fierce kiss' will stay on the lips, its 'platinum loops' can shrink to a wedding ring "
          "'if you like', and it is 'Lethal'. It will cling to the fingers, to the knife, for weeks - the "
          "smell of it a warning of possessiveness, of the knife that could be used. The poem ends with the "
          "onion's after-scent persisting, the gift accepted and the danger named at once.",
  themes_text="Duffy's subject is the honesty that the conventional language of romance prevents: the onion is a "
              "better emblem of love than the rose because it has layers, makes you cry, leaves a smell and "
              "cannot be disposed of quickly. The poem plays the metaphysical conceit - an ordinary object "
              "made to carry an argument about love - against the debased currency of the Valentine's card, "
              "and its final movement from tenderness to threat ('Lethal', the knife) refuses the separation "
              "of love from possession and violence. The 'if you like' of the wedding ring makes the marriage "
              "proposal a question the lover can decline, and the whole poem is addressed to a 'you' whose "
              "answer is not recorded.",
  structure="Free verse in irregular stanzas of one to six lines, with no rhyme scheme; the poem is built on "
            "the repetition of 'I give you an onion' and on a series of short, end-stopped sentences; the "
            "single-word lines ('Here.', 'Lethal.') act as beats of emphasis.",
  style="Plain, monosyllabic, spoken diction with sharp, concrete images (moon wrapped in brown paper, platinum "
        "loops, knife); the conceit sustained with logical rigour; a tone that moves from playful refusal to "
        "sensual tenderness to flat menace without changing register.",
  ctx="Mean Time (Anvil Press, 1993) won the Whitbread Poetry Award and contains many of Duffy's best known "
      "love poems; 'Valentine' belongs to the early 1990s vogue for the anti-romantic love poem and to "
      "Duffy's project of writing in the plain speech of the demotic, and it has become one of the most "
      "widely set poems in British schools.",
  sig="The most famous poem of Duffy's middle period and one of the most widely taught poems in Britain; it is "
      "her selection in the Norton Anthology alongside 'Warming Her Pearls', 'Medusa' and 'Mrs Lazarus', and "
      "it is the poem through which her use of the conceit is usually introduced.",
  canon="Secondary canon",
  biblio="Published in Mean Time (London: Anvil Press Poetry, 1993). A selection of The Norton Anthology of "
         "English Literature, 11th edition, vol. F, beginning at page 1160.",
  notes="The poem was read in the quotations reproduced on the revision and study pages cited, which agree word "
        "for word on the opening, the moon and brown paper, 'Lethal' and the knife; it was not read complete "
        "from the printed collection.",
  ver="partially verified", sources=[CD_VALENTINE, W_CD, NAEL]),
]

WORKS += [
W10("Medusa", CD, "1999", "Poem", "significant",
  genres=G("Dramatic Monologue", "Mythological Retelling", "Lyric Poetry"),
  themes=T("Gender, feminism and women's lives", "Love, intimacy and loss", "Myth, folklore and the supernatural"),
  movements=M("Second-Wave Feminist Writing", SCOT),
  overview="A poem from The World's Wife (1999) in which Medusa speaks in the first person about the jealousy "
           "that turned her hair to snakes and her eyes to stone, and about the love that keeps her dangerous.",
  content="A dramatic monologue in seven stanzas of free verse, in which Medusa describes her transformation, "
          "addresses the man she loves, and warns him - and the reader - not to look at her.",
  summary="Medusa begins with the origin of her condition: 'A suspicion, a doubt, a jealousy / grew in my mind, "
          "/ which turned the hairs on my head / to filthy snakes / as though my thoughts / hissed and spat on "
          "my scalp.' The poem follows the transformation through her body - her breath souring, her lungs "
          "'grey bags', her mouth foul, her teeth yellow fangs, 'bullet tears' in her eyes - and then turns to "
          "the man she loves: 'Be terrified. / It's you I love, / perfect man, Greek God, my own; / but I "
          "know you'll go, betray me, stray / from home.' She imagines the women he will look at, and what will "
          "become of them; she tells him that she is not the monster he thinks, that the stone is the "
          "hardening of a love that has been hurt. The poem's final movement is a warning and a confession: "
          "the gaze that petrifies is the gaze of someone who has been betrayed and will not be looked at "
          "again, and the poem's bitterness is directed as much at the woman's own jealousy as at the man.",
  themes_text="Duffy rewrites the Medusa myth as the story of a woman destroyed by jealousy rather than by a "
              "curse: the snakes are her thoughts, and the petrifying gaze is the hardening of love into "
              "suspicion. The poem belongs to The World's Wife's project of giving the women of myth and "
              "history their own voices, and it makes a feminist argument about the way women are turned "
              "into monsters by the fear of betrayal, while refusing to excuse the violence that Medusa's "
              "own suspicion produces. The direct address to the lover makes the poem a love poem as well as "
              "a curse, and the imagery of the body - breath, lungs, eyes, teeth - keeps the myth physical.",
  structure="Seven stanzas of free verse, the first of five lines and the rest of six, without a regular rhyme "
            "scheme but with strong internal rhyme, assonance and consonance; the poem moves from diagnosis "
            "to transformation to address to warning, and ends on an image rather than a statement.",
  style="Blunt, monosyllabic, deliberately ugly diction in the transformation stanzas ('foul mouthed', 'yellow "
        "fanged') set against the plain tenderness of 'It's you I love'; heavy alliteration and sibilance; "
        "short lines and hard enjambments; the tone is jeering, wounded and seductive at once.",
  ctx="The World's Wife (Picador, 1999) is Duffy's best-selling collection, a series of dramatic monologues in "
      "which the wives and women of myth, history and literature answer back; 'Medusa' belongs to its "
      "sequence of classical and biblical retellings, and the collection was written in the years before "
      "Duffy became Poet Laureate in 2009.",
  sig="One of the most widely taught poems of The World's Wife and a standard example of the feminist "
      "revisionary myth poem; it is one of Duffy's four selections in the Norton Anthology.",
  canon="Secondary canon",
  biblio="Published in The World's Wife (London: Picador, 1999). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning at page 1160.",
  notes="The poem's opening and several lines were read through the annotation page cited, which prints the text "
        "and describes the seven-stanza structure; it was not read complete from the printed collection.",
  ver="partially verified", sources=[CD_MEDUSA, W_CD, NAEL]),
W10("Mrs Lazarus", CD, "1999", "Poem", "significant",
  genres=G("Dramatic Monologue", "Mythological Retelling", "Elegiac Poetry"),
  themes=T("Death, illness and mourning", "Gender, feminism and women's lives", "Love, intimacy and loss"),
  movements=M("Second-Wave Feminist Writing", SCOT),
  overview="A poem from The World's Wife (1999) in which the wife of Lazarus describes her grief, her slow "
           "recovery and remarriage, and the ruin brought back when her husband is raised from the dead.",
  content="A dramatic monologue in eight five-line stanzas of free verse, in which Mrs Lazarus moves from "
          "frenzied mourning through the routines of widowhood to a new life, and then confronts the returned "
          "Lazarus.",
  summary="The poem begins in the extremity of grief: Mrs Lazarus shrieks, tears her hair, lies on the grave, "
          "and performs the mourning that is expected of her, 'howling' and 'shrieking' until she has no "
          "voice left. Then the poem's time begins to move: she takes off her black, goes back to work, "
          "learns to sleep alone, and eventually meets another man and marries him. Duffy compresses the "
          "years - 'I would have to ask / how long' - and shows the recovery as unspectacular and physical: "
          "the body's habits changing, the house rearranged. The last two stanzas bring the miracle: Lazarus "
          "returns, and his wife, who has grieved him properly and buried him and made a life, is left with "
          "a husband she no longer knows and a new husband she cannot keep. The poem's final image is of the "
          "two men and the woman between them, and of 'the hours I had' - the life she had built - being "
          "taken back.",
  themes_text="The poem's subject is the work of mourning and the way a miracle can be a catastrophe: Lazarus's "
              "resurrection, which the Gospel treats as a sign of divine power, is experienced by his wife as "
              "the destruction of the life she has slowly rebuilt. Duffy gives the woman the time the "
              "biblical narrative does not - the years of widowhood, the second marriage - and makes her "
              "grief a process with stages rather than a tableau. The poem is also about the social "
              "performance of mourning: the shrieking and hair-tearing that begin it are what is expected, "
              "and the poem's interest is in what comes after the performance ends.",
  structure="Eight five-line stanzas of free verse, with no rhyme scheme; the poem is chronological, moving from "
            "the death to the mourning to the remarriage to the return, and its stanzas shorten and quicken "
            "as the miracle approaches.",
  style="Plain, first-person, colloquial free verse with a strong physical vocabulary (shrieking, howling, the "
        "taste of ash, the smell of the grave); short sentences and abrupt line breaks; a tone that moves "
        "from raw grief to domestic calm to a final, quiet horror.",
  ctx="The World's Wife (Picador, 1999) reworks the stories of women attached to famous men, from Mrs Midas to "
      "Mrs Darwin and Queen Herod; 'Mrs Lazarus' takes the raising of Lazarus in the Gospel of John (11:1-44) "
      "as its source and extends the four days of the biblical narrative into years, so that the wife's "
      "remarriage becomes credible.",
  sig="One of the most frequently taught poems of The World's Wife and a set text in British schools; it is one "
      "of Duffy's four selections in the Norton Anthology and the collection's clearest example of its "
      "method of giving the untold woman's side of a familiar story.",
  canon="Secondary canon",
  biblio="Published in The World's Wife (London: Picador, 1999). A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning at page 1161.",
  notes="The account follows the annotation page cited, which prints the poem's opening stanzas and describes "
        "its eight-stanza structure and its departure from the Gospel narrative; the poem was not read "
        "complete from the printed collection.",
  ver="partially verified", sources=[CD_MEDUSA, W_CD, NAEL]),
W10("Hullabaloo in the Guava Orchard", KD, "1998", "Novel", "significant",
  genres=G("Comic Novel", "Satirical Fiction", "Regional Fiction"),
  themes=T("Faith, doubt and the sacred", "Nature, ecology and environmental crisis", "Power, the state and surveillance"),
  movements=M(SAS, POSTCOL),
  overview="An extract from Kiran Desai's first novel, Hullabaloo in the Guava Orchard (1998), in which Sampath "
           "Chawla, a clerk who has climbed a guava tree in a Shahkot orchard, is discovered there and turned "
           "by his family and the town into a holy man.",
  content="A comic sequence from the novel: the Chawla family's search for Sampath, the discovery of him in the "
          "tree, the debate over whether he is mad, the arrival of the first devotees, and the beginnings of "
          "the 'sermon in the guava tree' that makes him a celebrity.",
  summary="Sampath Chawla, the son of Mr and Mrs Chawla of Shahkot, has failed at school, at his job in the post "
          "office and at the marriage his parents arranged for him, and has run away to live in a guava tree "
          "in a ruined orchard on the edge of town. The family finds him there: 'Searching for Sampath, the "
          "family clacked about the trees and shouted up into the leaves, the three women uttering his name "
          "with mournful wails, Mr Chawla shouting like an Army major.' A doctor is consulted and a debate "
          "follows over whether Sampath is mad - 'Is he biting his neighbors? Biting himself? Is he "
          "sleepwalking? Does he stick out his tongue and roll his eyes? Is he rude to strangers?' - and the "
          "answer, that he eats and sleeps and is polite, settles that he is not. The orchard, however, has "
          "other visitors: the townspeople, hearing of the man in the tree, begin to bring offerings; and the "
          "extract follows the first pilgrims, the gifts of food and money, the raising of a cot and an "
          "umbrella into the branches, and the transformation of a failed clerk into a guru whose answers - "
          "nonsense delivered with the authority of revelation - become 'the sermon in the guava tree'. The "
          "extract ends with Sampath installed in comfort, and with the town's credulity and his family's "
          "enterprise in full flood.",
  themes_text="Desai's comedy is about the manufacture of sanctity: Sampath is a holy man because he is sitting in "
              "a tree and because a town needs a holy man, and the novel's satire is directed at the "
              "commercial and religious appetite that produces him. The orchard is also an ecological subject "
              "- a remnant of greenery that the town's traffic, rubbish and advertisements gradually overrun "
              "- and Sampath's retreat into it is a retreat from the noise of post-independence India into a "
              "silence he cannot keep. The family's eagerness to profit from his new status, and the "
              "bureaucracy's attempt to manage it, make the novel a study of how private eccentricity is "
              "converted into public property.",
  structure="A novel in thirty-odd short chapters, comic and episodic, with a large cast and a narrator who "
            "moves between the family's perspective and the town's; the Norton extract is a continuous "
            "sequence from the middle of the novel, covering the search, the diagnosis and the first "
            "devotees.",
  style="Exuberant, comic, over-heated prose with long lists, exclamations and sudden lyric passages; a strong "
        "sense of place (the orchard, the town, the railway) and a taste for the absurd; dialogue in an "
        "Indian English with a vivid demotic energy, and a narrator who shares the characters' excitability.",
  ctx="Hullabaloo in the Guava Orchard was published by Faber and Faber in 1998 and won the Betty Trask Award; it "
      "was begun while Desai was studying creative writing in the United States, and it draws on her childhood "
      "in India and on the tradition of Indian comic fiction. 'The Sermon in the Guava Tree' was printed in "
      "The New Yorker in June 1997 as an extract from the then forthcoming novel, and the Norton Anthology "
      "reprints a passage of the same material.",
  sig="Desai's first novel and the book that made her name before The Inheritance of Loss won the Booker Prize "
      "in 2006; the guava-tree episode is the novel's central comic idea, and the extract is her selection in "
      "the Norton Anthology.",
  canon="Secondary canon",
  biblio="Published by Faber and Faber (London) in 1998. Norton prints an extract under the title 'The Sermon "
         "in the Guava Tree', beginning at page 1200; a version of the same material appeared under that title in "
         "The New Yorker, 23 June 1997. This record covers the whole novel.",
  notes="The plot of the extract follows the New Yorker text (its opening and the quoted exchanges) and the "
        "summaries of the novel in the scholarly and reference sources cited; Desai's own date of first "
        "publication for the novel (1998) and the extract's New Yorker appearance (June 1997) are taken from "
        "those pages. The novel was not read complete.",
  ver="partially verified", sources=[W_KD, DESAI_NYER, DESAI_ECO, NAEL]),
]

AUTHORS.append(
A10(KD, MAJ, "1971", None, "New Delhi, India",
  "Indian; novelist writing in English",
  "Indian novelist whose comic first novel Hullabaloo in the Guava Orchard and whose Booker-winning The "
  "Inheritance of Loss made her the youngest woman to win the prize at the time",
  "Kiran Desai was born in New Delhi on 3 September 1971, the daughter of the novelist Anita Desai. She grew up "
  "in Delhi, Punjab and Bombay, where she attended the Cathedral and John Connon School, and left India at "
  "fifteen; after a year in England she and her mother moved to the United States, where she studied creative "
  "writing at Bennington College, Hollins University and Columbia University. Her first novel, Hullabaloo in "
  "the Guava Orchard (1998), won the Betty Trask Award; her second, The Inheritance of Loss (2006), set in the "
  "Himalayas during the Gorkhaland agitation, won the Man Booker Prize and the National Book Critics Circle "
  "Award, making her the youngest woman to win the Booker at the age of thirty-five. She held a Berlin Prize "
  "fellowship at the American Academy in Berlin in 2013, and her third novel, The Loneliness of Sonia and "
  "Sunny, appeared in 2025 after a gap of nearly two decades.",
  "Novels: Hullabaloo in the Guava Orchard (1998), The Inheritance of Loss (2006) and The Loneliness of Sonia "
  "and Sunny (2025).",
  "Comic, exuberant, image-rich prose with long lists and sudden lyric turns; a strong sense of place - the "
  "small-town orchard, the Himalayan hill station - and an ear for the demotic language of Indian English; "
  "a narrative that can move between farce and political violence within a paragraph.",
  "Post-independence India and the failures of the state; religion, credulity and the manufacture of holy men; "
  "nature, ecology and the encroachments of development; globalisation, migration and the unequal traffic "
  "between India and the West; family, parents and the inheritance of disappointment.",
  "Kiran Desai is among the most significant Indian novelists in English of her generation and the winner of "
  "the Booker Prize in 2006, and Hullabaloo in the Guava Orchard established the comic idiom that The "
  "Inheritance of Loss deepened into a political one; her selection in the Norton Anthology follows the "
  "generation of Roy and Rushdie.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Desai, read directly, and from general "
           "knowledge; they were not checked against a bibliography. Installment 10 records only the Norton "
           "selection, the extract published as 'The Sermon in the Guava Tree' from Hullabaloo in the Guava "
           "Orchard (1998); the other novels have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_KD, DESAI_NYER, NAEL]))
