"""Installment 10, wave 21: the American anthology begins - Nabokov, Roethke, Bishop, Tennessee
Williams, Cheever and Robert Hayden.

Six authors new to the database, fifteen works: one record per Norton selection first published
1946-2000. Hayden's "Middle Passage" was first printed in 1945 and so stays outside the period even
though Norton prints the 1962 revision; that decision is recorded in the lists and in the notes here.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL, NAAL  # noqa: E402

VN = "Vladimir Nabokov"
TR = "Theodore Roethke"
EB = "Elizabeth Bishop"
TW = "Tennessee Williams"
JC = "John Cheever"
RH = "Robert Hayden"

POSTMOD = "Postmodernism and Postmodern Fiction"
SOGOTH = "Southern Gothic"
CONF = "Confessional Poetry"

W_NAB_STORY = "Signs and Symbols (Wikipedia)"
W_NAB = "Vladimir Nabokov (Wikipedia)"
W_ROE = "Theodore Roethke (Wikipedia)"
W_BIS = "Elizabeth Bishop (Wikipedia)"
W_ONEART = "One Art (Wikipedia)"
W_SWIM = "The Swimmer (short story) (Wikipedia)"
W_CHEEVER = "John Cheever (Wikipedia)"
W_STREETCAR = "A Streetcar Named Desire (Wikipedia)"
W_HAY = "Robert Hayden (Wikipedia)"
W_MP = "Middle Passage (poem) (Wikipedia)"

AUTHORS = [
A10(VN, MAJ, "1899", "1977", "Saint Petersburg, Russia",
  "Russian American; novelist, short-story writer, poet, critic and lepidopterist writing in Russian and English",
  "Russian-born American novelist whose baroque style, unreliable narrators and love of pattern made him one of "
  "the central prose artists of the twentieth century, in Russian and then in English",
  "Vladimir Vladimirovich Nabokov was born in Saint Petersburg on 22 April 1899 into a wealthy liberal family, "
  "and left Russia with his family in 1919; he read at Trinity College, Cambridge, and lived in Berlin and then "
  "Paris as an émigré, writing novels and stories in Russian under the pen name V. Sirin. He came to the United "
  "States in 1940, taught Russian and European literature at Wellesley College and, from 1948 to 1959, at "
  "Cornell University, working as a research entomologist at the American Museum of Natural History and "
  "becoming an American citizen in 1945. Lolita (1955, Olympia Press, Paris) made him famous and controversial; "
  "Pnin (1957), Pale Fire (1962) and Ada or Ardor (1969) followed, with the memoirs Speak, Memory (1951) and "
  "the translations and commentaries on Pushkin's Eugene Onegin (1964). He settled at the Montreux Palace Hotel "
  "in Switzerland in 1961 and died there on 2 July 1977.",
  "Novels in Russian: Mary (1926), King, Queen, Knave (1928), The Defence (1930), Glory (1932), Camera Obscura "
  "(1932), Despair (1934), Invitation to a Beheading (1936), The Gift (1937). Novels in English: The Real Life "
  "of Sebastian Knight (1941), Bend Sinister (1947), Lolita (1955), Pnin (1957), Pale Fire (1962), Ada or Ardor "
  "(1969), Transparent Things (1972) and Look at the Harlequins! (1974). Stories: Nabokov's Dozen (1958), "
  "Details of a Sunset (1976) and The Stories of Vladimir Nabokov (1995). Memoir and criticism: Speak, Memory "
  "(1951), Notes on Prosody (1964), Eugene Onegin, translated and commented (1964) and Strong Opinions (1973).",
  "A prose of extreme precision and elaborate patterning, with alliteration, puns, multilingual wordplay and "
  "buried acrostics; unreliable or self-dramatising narrators; a habit of addressing the reader directly; "
  "sensuous detail used as evidence, and a lyric gift that survives translation from the Russian.",
  "Memory and the lost Russian childhood; exile, émigré poverty and the impostures of identity; the relation "
  "between art and cruelty; madness, obsession and the tyranny of the imagination; lepidoptery, chess and "
  "pattern-making as images of the novelist's work; America as seen by an astonished outsider.",
  "Nabokov is the most influential prose stylist among the Russian émigrés and one of the defining novelists of "
  "the century; Lolita and Pale Fire are standard texts in the study of the unreliable narrator and of "
  "postmodern fiction, his Cornell lectures shaped several generations of American writers, and the "
  "Nabokovian phrase and the Nabokovian puzzle have become common critical currency.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Nabokov and on 'Signs and Symbols', "
           "read directly; they were not checked against a bibliography. "
           "Installment 10 records only the Norton selection, 'Signs and Symbols' (The New Yorker, 1948; "
           "collected in Nabokov's Dozen, 1958); the novels, the other stories and the criticism have no "
           "records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_NAB, W_NAB_STORY, NAAL]),
A10(TR, MAJ, "1908", "1963", "Saginaw, Michigan, United States",
  "American; poet and teacher writing in English",
  "American poet of the Michigan greenhouses and the Pacific Northwest, whose rhythmic, hypnotic verse moved "
  "from the greenhouse poems to the love poems and the mystical sequences of his last books",
  "Theodore Huebner Roethke was born in Saginaw, Michigan, on 25 May 1908, the son of a German immigrant who "
  "owned greenhouses, and grew up among them; his father and uncle both died in 1923, when he was fourteen. He "
  "took his BA at the University of Michigan in 1929 and his MA in 1936, studied briefly at Harvard and the "
  "University of Michigan Law School, and taught at Lafayette College, Pennsylvania State University, Bennington "
  "College and, from 1947 until his death, at the University of Washington, where he became poet in residence "
  "in 1962. Open House (1941), The Lost Son and Other Poems (1948), Praise to the End! (1951), The Waking "
  "(1953, Pulitzer Prize), Words for the Wind (1958, National Book Award) and I Am! Says the Lamb (1961) "
  "appeared in his lifetime, and The Far Field (1964, National Book Award) posthumously. He suffered from manic "
  "depression throughout his life, was a celebrated and demanding teacher, and died on Bainbridge Island, "
  "Washington, on 1 August 1963.",
  "Poetry: Open House (1941), The Lost Son and Other Poems (1948), Praise to the End! (1951), The Waking: Poems "
  "1933-1953 (1953), Words for the Wind (1958), I Am! Says the Lamb (1961) and The Far Field (1964). Prose: On "
  "the Poet and His Craft (1965, selected prose) and Straw for the Fire (1972, notebooks).",
  "Strongly rhythmic, often hypnotic free verse with heavy stresses and internal rhyme; short lines and "
  "nursery-rhyme cadences set against long Whitmanian sequences; exact natural notation (roots, stems, "
  "greenhouse glass, animals); fixed forms - the villanelle, the ballad - used alongside the loose 'lost son' "
  "sequences.",
  "Growth, decay and the vegetable world of the greenhouse; the dead father and the childhood garden; love, "
  "the body and the erotic; the mystical and the primitive; madness, the unconscious and the journey inward; "
  "the American landscape of Michigan and the Northwest.",
  "Roethke is the central American poet of the 'middle generation' between the modernists and the "
  "confessional poets, and his greenhouse poems and 'The Waking' are among the most anthologised American "
  "poems of the century; his fusion of the child's eye with a mystical ambition influenced Lowell, Plath and "
  "a long line of later poets.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Roethke, read directly; they were "
           "not checked against a bibliography. Installment 10 "
           "records only the Norton selections - 'Cuttings' and 'Cuttings (later)' (The Lost Son, 1948), 'The "
           "Waking' and 'Elegy for Jane' (The Waking, 1953) and 'I Knew a Woman' (Words for the Wind, 1958); "
           "'My Papa's Waltz' (1942) is before the period, and the other collections have no records, so the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_ROE, NAAL]),
A10(EB, MAJ, "1911", "1979", "Worcester, Massachusetts, United States",
  "American; poet, short-story writer, painter and translator writing in English",
  "American poet of exact observation and deliberate reticence, whose few, slowly written poems of travel, "
  "loss and childhood are among the most admired in twentieth-century American verse",
  "Elizabeth Bishop was born in Worcester, Massachusetts, on 8 February 1911; her father died when she was "
  "eight months old and her mother was institutionalised in 1916, and she was raised by her maternal "
  "grandparents in Great Village, Nova Scotia, and then by relatives in Massachusetts. She took her AB at "
  "Vassar College in 1934, travelled in Europe and North Africa, lived in Key West and, from 1951, in Brazil, "
  "where she lived with the architect Lota de Macedo Soares until 1967, and settled in Boston in the 1970s, "
  "teaching at Harvard. North and South (1946), Poems: North & South - A Cold Spring (1955, Pulitzer Prize), "
  "Questions of Travel (1965), Complete Poems (1969, National Book Award) and Geography III (1976, National "
  "Book Critics Circle Award) are the volumes of her lifetime, with The Complete Poems 1927-1979 (1983) and "
  "the prose of The Collected Prose (1984) afterwards; she was Consultant in Poetry to the Library of Congress "
  "in 1949-50 and received the Neustadt International Prize in 1976. She died in Boston on 6 October 1979.",
  "Poetry: North and South (1946), Poems: North & South - A Cold Spring (1955), Questions of Travel (1965), "
  "The Complete Poems (1969), Geography III (1976) and The Complete Poems 1927-1979 (1983). Prose: The "
  "Collected Prose (1984) and the letters in One Art (1994). Translations: The Diary of Helena Morley (1957) "
  "and An Anthology of Twentieth-Century Brazilian Poetry (1972, with Emanuel Brasil).",
  "Quiet, exactly observed free verse and strict forms - the villanelle, the sestina, the sonnet - used "
  "without display; a painter's eye for colour, edge and perspective; understatement, reticence and a refusal "
  "of confessional exposure; a plain syntax that carries sudden metaphysical turns.",
  "Travel and the ethics of the observer; childhood, orphanhood and the loss of the mother; the discipline of "
  "loss and the making of art from it; the particularity of places - Nova Scotia, Florida, Brazil, New "
  "England; maps, geography and the frames through which a life is seen; dreams and surreal detail.",
  "Bishop is among the most admired American poets of the century and the model of a poet's poet: her "
  "reticence, her formal control and her exactness are the standards against which later American verse is "
  "often measured, and 'One Art', 'In the Waiting Room' and 'The Armadillo' are canonical texts in the study "
  "of the villanelle, of the late style and of postwar American poetry.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Bishop, read directly, and from the "
           "sources cited for the individual poems; they were not checked against a bibliography. Installment "
           "10 records only the Norton selections - 'At the Fishhouses' (1947), 'Questions of Travel' (1956), "
           "'The Armadillo' (1957), 'In the Waiting Room' (1971) and 'One Art' (New Yorker, 1976); 'The Fish' "
           "(1940) is before the period, and the prose has no record, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_BIS, W_ONEART, NAAL]),
]

AUTHORS += [
A10(TW, MAJ, "1911", "1983", "Columbus, Mississippi, United States",
  "American; playwright, poet, short-story writer and screenwriter writing in English",
  "American playwright of the American South whose lyrical, violent dramas of desire and delusion - above all "
  "A Streetcar Named Desire and Cat on a Hot Tin Roof - made him the central playwright of postwar Broadway",
  "Thomas Lanier Williams III was born in Columbus, Mississippi, on 26 March 1911 and grew up in Mississippi and "
  "in St Louis, where his father managed a shoe warehouse; he studied at the University of Missouri, Washington "
  "University and the University of Iowa, where he took a BA in 1938. The Glass Menagerie opened in Chicago in "
  "1944 and in New York in 1945; A Streetcar Named Desire followed on Broadway on 3 December 1947 and won the "
  "Pulitzer Prize in 1948, and Summer and Smoke (1948), The Rose Tattoo (1951), Cat on a Hot Tin Roof (1955, "
  "Pulitzer Prize), Orpheus Descending (1957), Suddenly Last Summer (1958), Sweet Bird of Youth (1959), The "
  "Night of the Iguana (1961) and The Milk Train Doesn't Stop Here Anymore (1963) followed, with the later "
  "plays, the screenplays of Baby Doll (1956) and others, and the stories and memoirs. He died in a New York "
  "hotel on 25 February 1983.",
  "Plays: The Glass Menagerie (1944), A Streetcar Named Desire (1947), Summer and Smoke (1948), The Rose Tattoo "
  "(1951), Camino Real (1953), Cat on a Hot Tin Roof (1955), Orpheus Descending (1957), Suddenly Last Summer "
  "(1958), Sweet Bird of Youth (1959), The Night of the Iguana (1961), The Milk Train Doesn't Stop Here Anymore "
  "(1963) and Small Craft Warnings (1972). Screenplays: Baby Doll (1956), Suddenly, Last Summer (1959) and "
  "others. Prose: One Arm (1948, stories), Hard Candy (1954, stories), The Roman Spring of Mrs Stone (1950, "
  "novel) and Memoirs (1975).",
  "A lyrical, rhetorical, image-rich dialogue that raises Southern speech into poetry; long monologues and "
  "confession scenes; expressionist staging - the transparent walls of Menagerie, the screeching streetcar and "
  "the polka of Streetcar; violent contrasts of tenderness and brutality; symbols carried by light, sound and "
  "costume.",
  "Desire, delusion and the refusal of reality; the dying Southern aristocracy and its illusions; the "
  "brutality of the sexual and the social world; homosexuality, guilt and self-punishment; memory, time and "
  "the fragility of art; loneliness, alcoholism and madness.",
  "Williams is the major American dramatist of the postwar decades and, with Miller, the playwright through whom "
  "the American theatre of the 1940s and 1950s is studied; Streetcar's Blanche DuBois and Stanley Kowalski are "
  "among the great roles of the modern stage, the 1951 Kazan film with Marlon Brando fixed the play in popular "
  "memory, and the play's language and staging changed what American drama could do with desire and memory.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Williams and on A Streetcar Named Desire, "
           "read directly, and from general knowledge; they were not checked against a bibliography. Installment "
           "10 records only the Norton selection, A Streetcar Named Desire (1947); the other plays, the films "
           "and the prose have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_STREETCAR, NAAL]),
A10(JC, MAJ, "1912", "1982", "Quincy, Massachusetts, United States",
  "American; short-story writer and novelist writing in English",
  "American short-story writer and novelist, the 'Chekhov of the suburbs', whose stories of Westchester County "
  "and the Upper East Side turned the disappointments of the American middle class into fable",
  "John William Cheever was born in Quincy, Massachusetts, on 27 May 1912 and grew up in Wollaston; his "
  "father's shoe business failed in the 1920s. He was expelled from Thayer Academy at seventeen - the episode "
  "became his first story, 'Expelled' (1930) - and began publishing in The New Yorker in the 1930s. The "
  "Wapshot Chronicle (1957, National Book Award), The Wapshot Scandal (1964, William Dean Howells Medal), "
  "Bullet Park (1969), Falconer (1977) and the novella Oh What a Paradise It Seems (1982) are the novels; the "
  "stories are gathered in The Enormous Radio (1953), The Housebreaker of Shady Hill (1958), Some People, "
  "Places, and Things That Will Not Appear in My Next Novel (1961), The Brigadier and the Golf Widow (1964) "
  "and The Stories of John Cheever (1978, Pulitzer Prize, National Book Critics Circle Award and National "
  "Book Award). He taught at the Iowa Writers' Workshop and at Sing Sing prison, was awarded the National "
  "Medal for Literature in 1982, and died at Ossining, New York, on 18 June 1982.",
  "Novels: The Wapshot Chronicle (1957), The Wapshot Scandal (1964), Bullet Park (1969), Falconer (1977) and Oh "
  "What a Paradise It Seems (1982). Story collections: The Way Some People Live (1943), The Enormous Radio "
  "(1953), The Housebreaker of Shady Hill (1958), Some People, Places, and Things That Will Not Appear in My "
  "Next Novel (1961), The Brigadier and the Golf Widow (1964) and The Stories of John Cheever (1978). Journals: "
  "The Journals of John Cheever (1991) and the letters (1988).",
  "A lucid, elegant, faintly ironic prose that keeps a straight face while the events turn fantastic; exact "
  "social notation of clothes, drinks, commuter trains and lawns; a habit of sudden mythic or apocalyptic "
  "imagery inside an ordinary scene; dialogue that exposes class and self-deception.",
  "Suburban America, its comforts and its terrors; the disparity between the social mask and the inner life; "
  "alcoholism, infidelity and the collapse of the family; nostalgia for an older New England community; the "
  "fantastic and the mythic intruding into the everyday; the sadness of the commuter's life.",
  "Cheever is the defining short-story writer of the American suburbs and one of the great American story "
  "writers of the century; 'The Swimmer' is his most anthologised story and is regularly read as an American "
  "fable of decline, and The Stories of John Cheever, which won the Pulitzer Prize, established the short story "
  "as a serious American literary form in the postwar decades.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Cheever, read directly, and from general "
           "knowledge; they were not checked against a bibliography. Installment 10 records only the Norton "
           "selection, 'The Swimmer' (The New Yorker, 18 July 1964; collected in The Brigadier and the Golf "
           "Widow, 1964); the novels and the other stories have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_CHEEVER, W_SWIM, NAAL]),
A10(RH, MAJ, "1913", "1980", "Detroit, Michigan, United States",
  "American; poet, essayist and teacher writing in English",
  "American poet of the Bahá'í faith and of African American history, whose formally exact poems on the "
  "Middle Passage, Frederick Douglass and his own childhood made him the first Black Consultant in Poetry to "
  "the Library of Congress",
  "Robert Hayden was born Asa Bundy Sheffey in Detroit on 4 August 1913 and was raised by a foster family, "
  "Sue Ellen and William Hayden, in the Paradise Valley neighbourhood. He studied at Detroit City College and "
  "at the University of Michigan, where he took an MA in 1942 under W. H. Auden and won a Hopwood Award, and "
  "taught at Fisk University from 1946 to 1969 and then at the University of Michigan until his death. "
  "Heart-Shape in the Dust (1940), Figure of Time (1955), A Ballad of Remembrance (1962), Selected Poems "
  "(1966), Words in the Mourning Time (1970), The Night-Blooming Cereus (1972), Angle of Ascent (1975) and "
  "American Journal (1978) are the collections; he was Consultant in Poetry to the Library of Congress from "
  "1976 to 1978, the first African American to hold the post, and died in Ann Arbor on 25 February 1980.",
  "Poetry: Heart-Shape in the Dust (1940), Figure of Time (1955), A Ballad of Remembrance (1962), Selected "
  "Poems (1966), Words in the Mourning Time (1970), The Night-Blooming Cereus (1972), Angle of Ascent (1975) "
  "and American Journal (1978), with Collected Poems (1985, ed. Frederick Glaysher). Prose: Collected Prose "
  "(1984).",
  "Formal, metrically regular verse - the sonnet, the ballad, the quatrain - with strong rhymes and refrains; "
  "a historical and documentary method that assembles ship logs, testimonies and voices; a restrained, "
  "meditative tone; dense imagery drawn from slavery, the Bible and Bahá'í scripture.",
  "The Middle Passage and the history of slavery; African American heroism, above all Frederick Douglass and "
  "the Amistad rebels; the father and the childhood home in Detroit; the Bahá'í teaching of the unity of "
  "humanity and its rejection of racial separatism; the American past, its monuments and its violence.",
  "Hayden is a central figure of twentieth-century African American poetry and the one who most firmly "
  "resisted the demand that Black poetry be only protest; 'Middle Passage' is the founding modern poem of the "
  "slave trade in American literature, and 'Those Winter Sundays' is among the most widely taught American "
  "poems of any period.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's articles on Hayden and on 'Middle Passage', read "
           "directly, and from general knowledge; they were not checked against a bibliography. Installment 10 "
           "records only the Norton selections 'Those Winter Sundays' and 'Summertime and the Living . . .' "
           "(A Ballad of Remembrance, 1962); 'Middle Passage' was first published in 1945 and is outside the "
           "period, though Norton prints the 1962 revision. The other collections have no records, so the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_HAY, W_MP, NAAL]),
]

WORKS = [
W10("Signs and Symbols", VN, "1948", "Short story", "significant",
  genres=G("Short Story", "Modernist Fiction", "Philosophical Fiction"),
  themes=T("Madness, breakdown and confinement", "Migration, exile and diaspora", "Family, marriage and domestic life"),
  movements=M(POSTMOD, "Late Modernism"),
  overview="A short story first published in The New Yorker on 15 May 1948, under the title 'Symbols and Signs', "
           "and collected in Nabokov's Dozen (1958): an elderly émigré couple travel to a sanatorium to visit "
           "their mentally ill son on his birthday, are turned away after he has tried to kill himself, and "
           "return home to a telephone that will not stop ringing.",
  content="Three numbered sections, running to some four thousand words, in which the third anniversary of the "
          "son's confinement, a failed visit, a birthday present, a train journey back to the city and three "
          "telephone calls at the end of the evening carry almost the whole of the story; its subject is the "
          "couple's poverty, their exile and their son's 'referential mania', a delusion that everything in "
          "the world is a coded message about him.",
  summary="The story opens with the couple on a suburban train on a Saturday in April, carrying a small jar of "
          "beach-plum jelly as a birthday present for their son, who has been in a sanatorium for three years. "
          "The mother has brought a photograph, a pair of slippers and a comb as well, and worries about the "
          "weather and about what the doctor will say. At the sanatorium a nurse tells them that the boy has "
          "again attempted suicide - he has tried to throw himself out of a window - and that they cannot see "
          "him that day. On the train home the father, who is ill and short of breath, says that they must "
          "take him out of the place; the mother, who knows the boy's fear of strangers and of unfamiliar "
          "rooms, says nothing. At their apartment they eat a poor supper and the father dozes. The telephone "
          "rings: a girl's voice asks for 'Charlie', and the mother explains that it is a wrong number. It "
          "rings again, the same girl, the same mistake. Then, in the story's last line, it rings a third "
          "time and the mother, unable to bear it, tells her husband not to answer it. Between these events "
          "the narrator gives the boy's case history: his 'referential mania', in which 'the patient imagines "
          "that everything happening around him is a veiled reference to his personality and existence', and "
          "in which 'everything is a cipher and of everything he is the theme'; his terror of being watched "
          "by things rather than people; his drawing, his reading and the way he checks the water in the "
          "glass beside his bed. The parents' history is given in the same flat, exact detail: the flight "
          "from Russia after the revolution, the German maid in Berlin, the relatives murdered in the "
          "Holocaust, the rich brother Isaac who pays for the sanatorium, the nephew who is a famous chess "
          "player. The story ends with the third ring, and nothing is explained.",
  themes_text="The story is a study in interpretation: the son's disease is the reader's own condition, since "
              "the story is made of details that seem to ask to be decoded - the jelly, the photograph, the "
              "girl asking for Charlie, the numbers of the sections - and Nabokov said that a 'second (main) "
              "story' was woven behind the 'semitransparent' one without saying what it was. The predominant "
              "reading is that the story traps us into the very over-reading it describes, so that the "
              "reader's hunt for a message is a milder form of the boy's referential mania. Behind that "
              "formal joke lies a real subject: the grief of exile, the Holocaust that has taken the "
              "family's other relatives, the poverty of the émigrés and the helpless love of parents who "
              "cannot reach a child who cannot bear to be looked at.",
  structure="Three numbered sections, each a single continuous movement: the journey out and the failed "
            "visit, the journey home and the evening, and the three telephone calls; the narration is "
            "third-person and external, moving without comment between the parents' errands and the case "
            "history of the son, so that the reader is given no more than the characters can see and no "
            "less than the story's pattern requires.",
  style="Nabokov's English prose at its most exact and least ornamental: short declarative sentences, "
        "precise physical detail (the 'little jar' of jelly, the wet lilac, the 'dead leaves' of the "
        "suburban platform), dialogue reported without gloss, and a flat tone that refuses both sentiment "
        "and explanation; the story's horror is produced by the accumulation of ordinary detail, and its "
        "final sentence ('a third time, and she said: Don't answer it') is left to do the work of the "
        "ending.",
  ctx="Written in English in 1948, the year Nabokov began teaching at Cornell, and published in The "
      "New Yorker on 15 May 1948 under the title the magazine's editor Katharine White preferred, "
      "'Symbols and Signs'; Nabokov restored his own title and the numbered sections when he collected "
      "the story in Nabokov's Dozen (Doubleday, 1958). Its émigré couple belong to the world of Nabokov's "
      "Berlin and Paris stories, and its account of the Holocaust's reach into an ordinary family belongs "
      "to the first postwar decade of American fiction.",
  sig="One of Nabokov's most anthologised short stories and the one most often used to introduce his "
      "fiction to students, since it displays in miniature his method of the 'second story behind the "
      "story', his interest in pattern and interpretation and his unsentimental tenderness; it is his "
      "selection in the Norton Anthology, where it opens the American volume's postwar section.",
  canon="Major canon",
  crit="Criticism has divided between readings that try to decode the story - arguing that the son has "
       "died, or that the third call is from him, or that the details hide a Holocaust allegory - and "
       "readings, now predominant, that see the story as a trap for exactly that kind of decoding: "
       "Alexander Dolinin and Brian Boyd have written on its many-layered structure, and the essay by "
       "Alexander Drescher on the 'beech plum' and the number of paragraphs is the best-known attempt to "
       "show that Nabokov did plant a code. Nabokov's own letter to Katharine White, describing 'a second "
       "(main) story ... placed behind the superficial semitransparent one', is the starting point of "
       "almost all of this criticism.",
  biblio="First published as 'Symbols and Signs' in The New Yorker, 15 May 1948; collected as 'Signs and "
         "Symbols' in Nabokov's Dozen (Garden City, NY: Doubleday, 1958). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The plot is summarised from the published story as described in the sources consulted and from "
        "the story's critical literature; the story itself was not read complete, and the quotations are "
        "those reproduced in the Wikipedia article on the story and in the criticism cited.",
  ver="partially verified", sources=[W_NAB_STORY, W_NAB, NAAL]),
]

WORKS += [
W10("Cuttings", TR, "1948", "Poem (nine short lines)", "significant",
  genres=G("Nature Poetry", "Lyric Poetry", "Free Verse"),
  themes=T("Nature, ecology and environmental crisis", "Art, the artist and the creative life", "Childhood, adolescence and coming of age"),
  movements=M("Late Modernism"),
  overview="A nine-line poem from The Lost Son and Other Poems (1948), the first of the greenhouse poems, in "
           "which a tray of plant cuttings pushing out roots and a single pale shoot is watched with the "
           "attention of a naturalist and the awe of a mystic.",
  content="Two unrhymed sentences of observation: the cut stems droop over the loam and their 'stem-fur' dries, "
          "yet the slips keep drawing water and their cells swell, until one 'nub of growth' nudges a crumb of "
          "sand aside and pokes its pale horn through the soil.",
  summary="'Sticks-in-a-drowse droop over sugary loam, / Their intricate stem-fur dries; / But still the "
          "delicate slips keep coaxing up water; / The small cells bulge.' The poem begins in exhaustion and "
          "dryness - the cuttings are sticks, half asleep, their fine hair dried out - and then, in the "
          "second sentence, something continues: the slips 'keep coaxing up water', the cells 'bulge', and a "
          "'nub of growth / Nudges a sand-crumb loose, / Pokes through a musty sheath / Its pale tendrilous "
          "horn.' The whole poem is nine lines long, with no rhyme and no regular metre, and its movement is "
          "from the passive to the active, from the sticks lying on the surface to the single shoot breaking "
          "out of the soil; the verbs do the work - 'coaxing', 'nudges', 'pokes' - and they are all verbs of "
          "a gentle, persistent pressure rather than of force. Nothing in the poem is explicitly human, and "
          "nothing is explicitly symbolic: the shoot is described as an animal horn and as a 'nub', and the "
          "reader is left to feel the analogy with any beginning that has to push through something dry.",
  themes_text="The greenhouse poems take the smallest possible subject - a cutting, a root, a weed - and treat "
              "it as a whole world, and 'Cuttings' establishes the method: exact notation of the physical, "
              "and then a leap, by image alone, into the human. The poem's interest is in the persistence of "
              "life in cut material, which is to say in growth that has been separated from its source and "
              "must make a new one, and in the way the poem's own attention ('coaxing', 'nudges') models "
              "the patience it describes.",
  structure="A single sentence of four short lines followed by a second of five, unrhymed and unmetred; the "
            "line breaks isolate the verbs and the nouns of growth, so that 'One nub of growth' stands alone "
            "as a stanza of its own and the last three lines slow into the single image of the horn.",
  style="Extremely compressed free verse, with heavy stresses and consonantal crowding ('Sticks-in-a-drowse', "
        "'stem-fur', 'musty sheath', 'tendrilous horn'); the diction mixes botanical exactness with "
        "invented compounds and a faintly archaic formality; there is no simile and no moral, only the "
        "observation and the rhythm.",
  ctx="The Lost Son and Other Poems (1948) gathered the greenhouse poems Roethke had been writing since the "
      "early 1940s about his father's and uncle's florist business in Saginaw, Michigan, and it made his "
      "reputation; the sequence's short 'Cuttings' poems stand at its head, and its longer title poem "
      "follows the same material into a child's night-time journey.",
  sig="One of the best-known short poems in twentieth-century American poetry and the standard introduction to "
      "Roethke's greenhouse sequence; it is paired in the Norton Anthology with 'Cuttings (later)', and the "
      "two poems are the usual demonstration of how his close observation turns into myth.",
  canon="Major canon",
  crit="Readings of the greenhouse poems emphasise Roethke's combination of botanical precision with a "
       "psychological and religious charge: the plants are both plants and figures for the poet's own "
       "buried life, and the sequence has been discussed in relation to his biography (the father's "
       "greenhouses, the deaths of 1923) and to his reading of Jung and of the mystics. 'Cuttings' is "
       "usually treated as the purest example of the sequence's method, since it offers no explicit "
       "interpretation at all.",
  biblio="Published in The Lost Son and Other Poems (Garden City, NY: Doubleday, 1948). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read through the text reproduced in the anthologies and study sources consulted; "
        "the quotations are short and were checked against more than one transcription.",
  ver="partially verified", sources=[W_ROE, NAAL]),
W10("Cuttings (later)", TR, "1948", "Poem (eleven short lines)", "significant",
  genres=G("Nature Poetry", "Lyric Poetry", "Free Verse"),
  themes=T("Nature, ecology and environmental crisis", "Death, illness and mourning", "Art, the artist and the creative life"),
  movements=M("Late Modernism"),
  overview="The companion poem to 'Cuttings' in The Lost Son and Other Poems, in which the rooting of the same "
           "cut stems becomes a 'resurrection' that the poet feels in his own veins and that drives him back "
           "to 'beginnings'.",
  content="Eleven lines in two sentences: the 'urge, wrestle, resurrection of dry sticks' is compared to the "
          "straining of a saint, and the poet, hearing the 'sucking and sobbing' underground, feels the small "
          "waters seeping upward in his own bones and is left 'sheath-wet', leaning to beginnings.",
  summary="'This urge, wrestle, resurrection of dry sticks, / Cut stems struggling to put down feet, / What "
          "saint strained so much, / Rose on such lopped limbs to a new life?' The first sentence turns the "
          "botany into hagiography: the cuttings are martyrs, their roots are 'feet', and the question is "
          "what saint ever rose on 'such lopped limbs'. The second sentence moves from observation to "
          "identification: 'I can hear, underground, that sucking and sobbing, / In my veins, in my bones I "
          "feel it, - / The small waters seeping upward, / The tight grains parting at last.' The poem ends "
          "with the shoot breaking the surface: 'When sprouts break out, / Slippery as fish, / I quail, lean "
          "to beginnings, sheath-wet.' The word 'quail' is both the bird and the flinch, and 'sheath-wet' "
          "carries the botanical sheath, the animal afterbirth and the poet's own body into a single "
          "adjective; the poet is not the observer of the growth but is implicated in it, and the poem's "
          "last gesture is a leaning backwards, towards what is beginning rather than what has grown.",
  themes_text="Where 'Cuttings' watches, this poem enters: the resurrection of the sticks is felt 'in my "
              "veins, in my bones', and the language of rooting becomes the language of birth and of "
              "resurrection, so that the poem's subject is the continuity between the vegetable and the "
              "human body. The word 'resurrection' also brings the poem's religious ambition into the open: "
              "the greenhouse is a place where the dead are made to live again, and the poet's response - "
              "'I quail' - is a mixture of awe, fear and desire to be returned to the beginning, which is "
              "the emotional core of the whole greenhouse sequence.",
  structure="Eleven lines in two sentences, broken into a question of four lines, an account of five, and a "
            "final three-line movement; the line breaks fall on the verbs of growth and the last line is "
            "left short and exposed, so that the poem ends at the moment of breaking out.",
  style="Heavier and more incantatory than 'Cuttings': the opening line crowds three abstract nouns and a "
        "noun phrase ('urge, wrestle, resurrection of dry sticks') into one breath, alliteration and "
        "assonance bind the lines ('sucking and sobbing', 'seeping upward'), and the diction runs from the "
        "colloquial to the liturgical ('What saint strained so much').",
  ctx="Published beside 'Cuttings' in The Lost Son (1948), the poem belongs to the greenhouse sequence that "
      "established Roethke's reputation and to the postwar American poetry of the family and the "
      "unconscious; its language of resurrection and of 'beginnings' anticipates the long 'lost son' poems "
      "that follow it in the same volume.",
  sig="The second of Roethke's paired 'Cuttings' poems and the one usually taken to show the mystical and "
      "autobiographical turn of the greenhouse sequence; the two poems together are the standard anthology "
      "selection from The Lost Son.",
  canon="Secondary canon",
  crit="Criticism reads the poem as the point where the greenhouse poems become explicitly about the poet: "
       "the 'saint' and the 'resurrection' have been related to Roethke's reading of the mystics and to the "
       "death of his father, and the final 'lean to beginnings, sheath-wet' is often quoted as the "
       "sequence's statement of its own backward-looking method.",
  biblio="Published in The Lost Son and Other Poems (Garden City, NY: Doubleday, 1948). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="Read through the text reproduced in the anthologies and study sources consulted; unlike 'Cuttings' "
        "this poem is less often reproduced complete, and the quotations were checked across two "
        "transcriptions.",
  ver="partially verified", sources=[W_ROE, NAAL]),
]

WORKS += [
W10("The Waking", TR, "1953", "Poem (villanelle in six stanzas)", "major",
  genres=G("Formal Verse", "Religious Poetry", "Lyric Poetry"),
  themes=T("Alienation, absurdity and existential freedom", "Faith, doubt and the sacred", "Death, illness and mourning"),
  movements=M("Late Modernism"),
  overview="The title poem of The Waking (1953), which won the Pulitzer Prize in 1954: a villanelle in which the "
           "poet accepts that he wakes and sleeps 'by God's grace' and learns 'by going where I have to go', "
           "using the repetitions of the form as the vehicle of a mystical submission.",
  content="Six three-line stanzas with the two refrains of the villanelle, in which the poet says that he "
          "wakes slowly and fears to wake, that he hears his fate in what he cannot see, that 'we think by "
          "feeling', that God's grace keeps him waking and sleeping, and that 'This shaking keeps me steady. I "
          "should know.'",
  summary="'I wake to sleep, and take my waking slow. / I feel my fate in what I cannot fear. / I learn by "
          "going where I have to go.' The poem's opening sentence sets out its paradox: waking is a kind of "
          "sleep, and the way to learn is to go where one is compelled to go, without knowing where that is. "
          "The second stanza takes the same three propositions a step further - 'We think by feeling. What "
          "is there to know? / I hear my being dance from ear to ear' - and adds the strange, joyful image "
          "of the body's being dancing between the ears. The third stanza invokes God and asks for the "
          "grace of 'the deep' and of 'the clear', and the fourth and fifth return to the themes of "
          "darkness, light and the humility of not knowing: 'Of those so close beside me, which are you? / "
          "God bless the Ground! I shall walk softly there, / And learn by going where I have to go.' The "
          "final stanza gathers the refrains: 'Great Nature has another thing to do / To you and me; so "
          "take the lively air, / And, lovely, learn by going where to go. // This shaking keeps me steady. "
          "I should know. / What falls away is always. And is near. / I wake to sleep, and take my waking "
          "slow. / I learn by going where I have to go.' The last line of the poem, the refrain released "
          "from the tercet and left standing alone, is the poem's whole argument: knowledge is not "
          "acquired by understanding but by consenting to the way one is already going.",
  themes_text="'The Waking' is a religious poem that refuses doctrine: its God is invoked in the third stanza "
              "only to be left unnamed, and its 'Great Nature' does the work that providence does in a "
              "metaphysical poet. What the poem asks for is a way of living without certainty - 'We think "
              "by feeling. What is there to know?' - and its answer, repeated five times in the refrains, "
              "is that one learns by going. The villanelle's obsessive return of the same two lines is the "
              "poem's meaning as well as its form: a mind that cannot get past its own propositions and "
              "finds in the repetition not monotony but steadiness, and the paradox 'This shaking keeps me "
              "steady' names the comfort the form gives.",
  structure="A villanelle of six tercets in which line one and line three of the first stanza become the "
            "alternating refrains, and a final quatrain repeats both; the refrains are varied slightly - "
            "'where I have to go' becomes 'where to go' - and the rhymes are carried by assonance and "
            "half-rhyme (slow/go/know, fear/ear/clear/near, air/there) rather than by exact rhyme.",
  style="A spoken, almost conversational iambic pentameter with heavy monosyllables ('This shaking keeps me "
        "steady. I should know.'), colloquial contractions and exclamations set against a liturgical "
        "refrain; the diction is plain and the syntax short, so that the poem's profundity comes from "
        "repetition and from the pressure of the form rather than from ornament.",
  ctx="The Waking: Poems 1933-1953 (1953) collected the three earlier books with new poems and won the "
      "Pulitzer Prize for Poetry in 1954; the title poem, written in the early 1950s, belongs to the period "
      "of Roethke's most concentrated religious poetry and to the American postwar vogue for the villanelle, "
      "which he helped to revive in English.",
  sig="Roethke's best-known poem after 'My Papa's Waltz' and the one for which he won the Pulitzer Prize; it "
      "is a standard anthology piece and the demonstration text for the modern American villanelle, and its "
      "refrain 'I learn by going where I have to go' is among the most quoted lines in twentieth-century "
      "American poetry.",
  canon="Major canon",
  crit="The poem has been read as a mystical text - Roethke's interest in Meister Eckhart, Jakob Böhme and "
       "the via negativa is well documented - and as a formal triumph in which the villanelle's repetitions "
       "enact the submission the poem describes. Critics have also written about its relation to Roethke's "
       "manic depression, reading 'This shaking keeps me steady' as a statement about the illness as well "
       "as about the verse, and the line has become a touchstone in discussions of the poet's late style.",
  biblio="Published in The Waking: Poems 1933-1953 (Garden City, NY: Doubleday, 1953). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was read through the text reproduced in the anthologies and study sources consulted, and "
        "the quotations were checked against more than one transcription; the critical material is "
        "paraphrased from general accounts and was not read in the specialist literature.",
  ver="partially verified", sources=[W_ROE, NAAL]),
W10("Elegy for Jane", TR, "1953", "Poem (six quatrains and a closing line)", "significant",
  genres=G("Elegiac Poetry", "Formal Verse", "Lyric Poetry"),
  themes=T("Death, illness and mourning", "Education, institutions and the academy", "Love, intimacy and loss"),
  movements=M("Late Modernism"),
  overview="An elegy from The Waking (1953), subtitled 'My Student, Thrown by a Horse', in which a teacher "
           "mourns a girl he loved 'in the way a father loves a daughter' and asks the natural world to "
           "remember her.",
  content="Six unrhymed quatrains and a single final line in which the speaker addresses the dead student, "
          "recalls her presence in his classroom - her 'neckcurls, limp and damp as tendrils', her quick "
          "laugh - calls on the plants and birds to mourn her, and ends by saying that he has no right to "
          "her name.",
  summary="'I remember the neckcurls, limp and damp as tendrils; / And her quick look, a sidelong pickerel "
          "smile; / And how, once started, she would never finish / Such waltzing ways.' The poem opens "
          "with the physical memory of the girl in the classroom: the damp hair, the fish-like sidelong "
          "smile, the restless movement. The second quatrain places her among the other students - 'She "
          "was not sparrow, starling, wren, or lark' - and the third gives her the poem's benediction: "
          "'For nothing can assuage my grief / That such a one should be / Thrown by a horse.' The middle "
          "stanzas call on the physical world to attend the burial: 'If only I could nudge you from this "
          "sleep, / My maimed darling, my skittery pigeon' - the tenderness and the grotesquerie together "
          "- and then a list of plants and birds, 'the bead-drops' and 'the solemn birds', is asked to "
          "'mourn her'. In the final lines the speaker withdraws the claim he has been making: 'Over this "
          "damp grave I speak the words my people said, / My father's people, the Pennsylvania Dutch: / "
          "'Dark is the day, dark is the night, / Dark is the grave where my love lies.'' And the last "
          "line, set apart, concedes the poem's limits: 'I am not her father, nor she my daughter.' The "
          "admission is what makes the poem an elegy rather than a love poem: the grief is real and the "
          "relation is not, and the teacher's mourning has to find its justification in the girl's own "
          "worth rather than in a family claim.",
  themes_text="The poem is about the impropriety of grief: a teacher may not mourn a student as a father "
              "mourns a daughter, and the poem's honesty lies in its final admission that he has no such "
              "right. Around that admission gather the poem's other subjects - the classroom as a place of "
              "intense, unspoken attachments, the natural world as the only available language for "
              "consolation, and the Pennsylvania Dutch funeral formula that the speaker borrows to give "
              "his grief a communal form. The girl herself is made present through details of hair, "
              "movement and laughter rather than through character, which is both a limit and a "
              "tenderness.",
  structure="Six quatrains and a single separated line; the quatrains are unrhymed but strongly metrical, and "
            "the poem moves from memory to invocation to the borrowed funeral formula to the final "
            "withdrawal; the last line stands alone as a correction of everything before it.",
  style="A formal, almost Latinised diction ('assuage', 'maimed darling', 'skittery pigeon') set beside "
        "colloquial and dialectal words ('pickerel smile', 'tendrils', 'bead-drops'); heavy stresses and "
        "long vowels give the poem its ceremonial pace, and the plant and bird lists give it the structure "
        "of a pastoral elegy in miniature.",
  ctx="The Waking (1953) was Roethke's Pulitzer Prize volume; 'Elegy for Jane' belongs to his poems about "
      "teaching, written during his years at the University of Washington, and to the tradition of the "
      "pastoral elegy that runs from Milton's Lycidas through Whitman's 'When Lilacs Last in the Dooryard "
      "Bloom'd'; its Pennsylvania Dutch funeral formula points to the poet's German immigrant background.",
  sig="One of Roethke's most frequently anthologised poems and his best-known elegy; it is a standard text "
      "in courses on the elegy and on the American poem of the 1950s, and its final line is often quoted "
      "as an example of the ethical care that distinguishes his work from the confessional poets who "
      "followed him.",
  canon="Secondary canon",
  crit="Criticism has concentrated on the poem's management of the teacher's improper grief, on its "
       "pastoral machinery and on the final line as an act of self-correction; feminist readings have "
       "asked what it means for a male teacher to make a dead girl the object of his elegy, and the poem "
       "is often taught alongside Bishop's 'Sestina' and Lowell's 'For the Union Dead' as a study in the "
       "limits of elegiac speech.",
  biblio="Published in The Waking: Poems 1933-1953 (Garden City, NY: Doubleday, 1953). A selection of The "
         "Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="Read through the text reproduced in the anthologies and study sources consulted; the poem's "
        "subtitle and closing line were checked against more than one transcription.",
  ver="partially verified", sources=[W_ROE, NAAL]),
]

WORKS += [
W10("I Knew a Woman", TR, "1958", "Poem (five five-line stanzas)", "significant",
  genres=G("Love Poetry", "Formal Verse", "Lyric Poetry"),
  themes=T("Love, intimacy and loss", "Sexuality, desire and the closet", "Art, the artist and the creative life"),
  movements=M("Late Modernism"),
  overview="A poem from Words for the Wind (1958) in which Roethke remembers a woman whose body and movements "
           "were 'like a dance', puns his way through the language of measurement and of sexual pleasure, and "
           "ends by asking to 'learn how to move'.",
  content="Five five-line stanzas, in loose iambic pentameter with interlaced rhyme, in which the speaker "
          "recalls a woman who 'played' him as an instrument, who 'turned, and turned, and turned' in his "
          "arms, and whose 'eyes' and 'sighs' he measures in a language that mixes the erotic with the "
          "geometric.",
  summary="'I knew a woman, lovely in her bones, / When small birds sighed, she would sigh back at them; / Ah, "
          "when she moved, she moved more ways than one: / The shapes a bright container can contain! / Of "
          "her choice virtues only gods should speak, / Or English poets who grew up on Greek / (I'd have "
          "them howl in harmony) - / Once I have come to love, I am a fool / For all sweet things.' The "
          "opening lines set the poem's method: physical praise ('lovely in her bones') in a diction that "
          "keeps turning the woman into an object of measurement - a 'bright container' that can contain "
          "shapes - while the speaker admits his own foolishness. The middle stanzas catalogue her "
          "movements and her effect on him: 'She played it quick, she played it light and loose; / My eyes, "
          "they dazzled, and my heart undone.' The fourth stanza makes the poem's most extraordinary sexual "
          "pun - 'immodest modesty', the 'sweetly' of her laughter, and the comparison of her body to a "
          "'bright container' and to a metrical foot - and the last stanza asks for what the poem has been "
          "describing: 'She who bears the light / Must bear it in her body; / Take from her, take from me, "
          "/ And learn how to move.' The poem ends with an imperative that is also a request to be taught, "
          "and its final word - 'move' - returns to the dance of the first stanza, so that the poem's "
          "argument is that love is a way of moving, learned from the beloved.",
  themes_text="The poem is a love poem built on measurement: 'I knew a woman' means both knew her and knew "
              "her in the biblical sense, and the poem keeps translating the woman's body into quantity - "
              "the 'bright container', the metre, the 'five' of the stanzas - while insisting that her "
              "quality escapes it. Its wit about sex is unusually frank for American poetry of 1958, and "
              "its final request to be taught how to move makes the woman the poet's master, which "
              "reverses the usual hierarchy of the love lyric and gives the poem much of its tenderness.",
  structure="Five five-line stanzas, each rhyming loosely on interlocking sounds rather than a fixed scheme; "
            "the poem's sentences run across stanza breaks and the last stanza turns from description to "
            "petition, so that the five-line unit becomes the poem's unit of measurement as well as its "
            "form.",
  style="Punning, propulsive verse in loose pentameters, full of internal rhyme, repetition and "
        "circumlocution ('a bright container can contain'); the diction mixes the erotic and the "
        "geometrical, the colloquial and the bardic, and the whole poem has the swing of a dance tune.",
  ctx="Words for the Wind (1958) gathered The Waking with new poems and won the National Book Award; 'I Knew "
      "a Woman' belongs to Roethke's love poems of the mid-1950s and to the period in which he was writing "
      "his most openly sensual verse, a period also marked by his teaching at the University of Washington "
      "and his travels in Europe.",
  sig="One of Roethke's best-loved poems and his frankest love poem; it is paired in the Norton Anthology "
      "with 'The Waking' and 'Elegy for Jane' and is a frequent anthology piece for its wit and its "
      "rhythm, and it is regularly cited as evidence that the 'confessional' generation learned its "
      "frankness from him.",
  canon="Secondary canon",
  crit="Critics have read the poem as Roethke's most successful erotic lyric and as a poem about the "
       "impossibility of describing a woman without turning her into a measure or a form; its puns and its "
       "repetitions have been analysed as a deliberate imitation of the movement it praises, and it is "
       "often compared with Yeats's love poems and with Donne's.",
  biblio="Published in Words for the Wind (Garden City, NY: Doubleday, 1958). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="Read through the text reproduced in anthologies and study sources consulted; the poem's stanza form "
        "and rhymes were checked against more than one transcription.",
  ver="partially verified", sources=[W_ROE, NAAL]),
]

WORKS += [
W10("At the Fishhouses", EB, "1947", "Poem (seven sections)", "major",
  genres=G("Nature Poetry", "Free Verse", "Lyric Poetry"),
  themes=T("Land, place and regional belonging", "Memory, trauma and testimony", "Faith, doubt and the sacred"),
  movements=M("Late Modernism"),
  overview="A poem first published in The New Yorker in 1947 and collected in North and South (1946) and then "
           "in Poems: North & South - A Cold Spring (1955): a walk past the fishhouses of a Nova Scotia "
           "harbour, an old fisherman salting herring, a cormorant on a rock and the cold water of the "
           "Atlantic, ending in a meditation on knowledge, total immersion and belief.",
  content="Seven sections of long-lined free verse in which the speaker describes the light, a row of "
          "fishhouses, an old man scaling herring with his knife, the benches and the tubs of salt, the "
          "harbour seals and a cormorant, and then rows out to the idea of the sea as 'cold dark deep and "
          "absolutely clear', 'element bearable to no mortal', and of knowledge as something one must "
          "immerse in.",
  summary="The poem opens in the present tense and with a painter's eye: 'Although it is a cold evening, / "
          "down by one of the fishhouses / an old man sits netting his nets, / his net is almost invisible, "
          "a dark purple-brown, / and his shuttle worn and polished.' The light is falling, the herring "
          "are heaped in the tubs, and the old man's hands are described with the precision of a still "
          "life: 'I have seen him / a hundred times, and he is always there, / and I know he is a 'old "
          "man''. The speaker has known this harbour since childhood - 'my grandfather was a fisherman' - "
          "and she watches the sea and the light on the water, the seals 'like thick, / dark, / rough "
          "stones', and a single cormorant on a rock 'with a kind of / rapt, / awkward dignity'. The poem "
          "then passes from description to argument: the sea is 'cold dark deep and absolutely clear, / "
          "element bearable to no mortal, / to fish and to seals', and to the speaker's memory of swimming "
          "in it as a child, of the 'icy' water and of being 'drenched' in it. In the last two sections "
          "the sea becomes the ground of a theory of knowledge: 'It is like what we imagine knowledge to "
          "be: / dark, salt, clear, moving, utterly free, / drawn from the cold hard mouth / of the world, "
          "derived forever / from the rocky breasts / forever, flowing and drawn, and since / our "
          "knowledge is historical, flowing, and flown.' The poem ends on that triple movement - flowing, "
          "drawn, flown - which is also the poem's own movement from scene to idea to the human history "
          "that holds them.",
  themes_text="'At the Fishhouses' is a poem about the conditions of knowledge, and it reaches that subject "
              "through an exact account of a place: the light, the nets, the wood, the salt, the water. "
              "Bishop's sea is not a symbol in the ordinary sense but a physical element that is 'bearable "
              "to no mortal', and the poem's argument is that knowing is like entering it - cold, total, "
              "and impossible to remain in. The old man and the harbour stand for a way of life that "
              "history is ending ('our knowledge is historical, flowing, and flown'), and the poem holds "
              "together nostalgia, exactness and a religious vocabulary ('element bearable to no mortal') "
              "without resolving them.",
  structure="Seven sections of irregular length, in long unrhymed lines of variable measure; the poem moves "
            "from description to memory to meditation, and its sections are marked by shifts of focus "
            "rather than by argument; the final section lifts the whole poem into abstraction while keeping "
            "the physical detail ('the cold hard mouth / of the world') in view.",
  style="Bishop's characteristic long free-verse line, paced by commas and semicolons rather than by "
        "regular stresses; exact colour words ('dark purple-brown', 'silver', 'opaque') and precise verbs "
        "('netting', 'scaling', 'drawn'); flat, unemphatic statement that gives way, in the last lines, to "
        "a cadence that is close to prayer.",
  ctx="Written in Nova Scotia in the summer of 1946, on Bishop's first return to Great Village since "
      "childhood, and published in The New Yorker in 1947; North and South (1946) had appeared in the same "
      "year, and the poem belongs to the postwar American poetry of place and to Bishop's lifelong "
      "preoccupation with the relation between observation and knowledge.",
  sig="One of Bishop's most admired poems and the one that established her as a major poet in the eyes of "
      "critics such as Randall Jarrell and Robert Lowell; it is a standard anthology text and is central to "
      "the critical account of her as a poet of exact description and of the ethics of seeing, and its "
      "closing lines on knowledge are among the most discussed in postwar American poetry.",
  canon="Major canon",
  crit="Readings of the poem have concentrated on the relation between description and abstraction - the "
       "way the poem earns its last lines by the exactness of its first - and on the politics of the "
       "harbour, in which the old fisherman's labour is passing. Feminist and postcolonial critics have "
       "written about Bishop's position as an American observer in Nova Scotia, and the poem's final "
       "definition of knowledge as 'historical, flowing, and flown' has been central to accounts of her "
       "epistemology.",
  biblio="First published in The New Yorker in 1947 and collected in Poems: North & South - A Cold Spring "
         "(Boston: Houghton Mifflin, 1955); it appeared in North and South (1946) in some accounts of the "
         "volume's contents, and the date given in the Norton list is 1947. A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="There is a discrepancy between the composition date (1946, Nova Scotia) and the date of first "
        "periodical publication (1947); the list follows the periodical date. The volume in which the poem "
        "first appeared in book form is given as 1955 in the sources consulted, but the Norton list's 1947 "
        "implies an earlier appearance, which was not verified.",
  ver="partially verified", sources=[W_BIS, NAAL]),
]

WORKS += [
W10("Questions of Travel", EB, "1956", "Poem (five stanzas)", "significant",
  genres=G("Travel Writing", "Free Verse", "Lyric Poetry"),
  themes=T("Land, place and regional belonging", "Migration, exile and diaspora", "Art, the artist and the creative life"),
  movements=M("Late Modernism"),
  overview="The title poem of Questions of Travel (1965), first published in The New Yorker on 14 January 1956: "
           "two stanzas of tourist cliché about waterfalls, mountains and crowded cities are followed by a "
           "long, sceptical meditation on whether travel is 'a dream' or a duty.",
  content="Five stanzas in loose free verse in which the poet describes the postcard beauties of a foreign "
          "country - 'there are too many waterfalls here', the 'fat brown rivers', the 'really magnificent' "
          "mountains - then turns to the question of why one travels at all, admits 'Oh, must we dream our "
          "dreams and have them, too?', and asks 'Should we have stayed at home and thought of here?'",
  summary="'There are too many waterfalls here; the crowded streams / hurry too rapidly down to the sea, / and "
          "the pressure of so many clouds on the mountaintops / makes them look like the soft, / "
          "smoke-billowing craters / of a 'really magnificent' volcano.' The poem begins in the voice of the "
          "disappointed tourist, complete with quotation marks around 'really magnificent', and the first "
          "stanzas pile up the sights until they become oppressive: the waterfalls, the rivers, the "
          "mountains, the 'big ships, / the little ships, / and the ferry-boats', the 'thousands' of "
          "people. Then the poem turns: 'Is it lack of imagination that makes us come / to imagined places, "
          "not just stay at home? / Or could the weather be / a delight, a necessity?' In the fourth stanza "
          "the speaker admits the dream-logic of travel - 'Oh, must we dream our dreams and have them, "
          "too?' - and in the fifth the poem asks the question of its title: 'Should we have stayed at home "
          "and thought of here? / Should we be contemplating the long, / long, sun-bright beaches / of "
          "Brazil, or the ancient / rock-cut tombs / of Egypt?' The poem does not answer. It ends instead "
          "with a domestic image - a child playing with 'the / small, / complicated, / toy' of the world - "
          "and with the ambivalence intact: travel is a form of dreaming, and the dream is both an escape "
          "and a failure of the imagination that could have conjured the place at home.",
  themes_text="The poem's subject is the ethics and epistemology of tourism: the traveller wants the real "
              "place and brings a stock of images to it, and Bishop renders that contradiction in a poem "
              "that is half a travel poster and half an attack on travel posters. 'Should we have stayed at "
              "home and thought of here?' is not a rhetorical question but a genuine one, and the poem's "
              "answer - that the imagination is both what drives us out and what prevents us from seeing - "
              "has made it central to later writing on travel and on the postcolonial tourist. The "
              "Brazilian material also belongs to Bishop's own migration, and the poem is a quiet record of "
              "an American in the southern hemisphere.",
  structure="Five irregular stanzas of free verse, with the first two built on accumulation and quoted "
            "tourist language, the third and fourth on the turn to question, and the fifth returning to the "
            "accumulation of places as a question; the poem's movement is circular rather than progressive, "
            "which is its argument.",
  style="Conversational and deliberately flat, with exclamations and quotation marks used as irony "
        "('really magnificent', 'the big ships, / the little ships'); precise enumeration and line breaks "
        "that isolate single words ('a / child', 'the'); a tone that moves from the jaunty to the "
        "meditative without changing register.",
  ctx="First published in The New Yorker on 14 January 1956 and collected in Questions of Travel (1965); "
      "written during Bishop's years in Brazil (1951-67), where she lived with Lota de Macedo Soares, and "
      "belongs to the postwar boom in American travel writing and to the debate about the tourist gaze that "
      "would become central to later cultural criticism.",
  sig="One of Bishop's most quoted poems and the title poem of her third book; it is a standard anthology "
      "text and a touchstone for criticism on travel, tourism and the ethics of observation, and it is "
      "often taught beside 'In the Waiting Room' as evidence of her interest in the limits of the "
      "observing self.",
  canon="Secondary canon",
  crit="Critics have read the poem as a critique of the tourist's desire for authenticity, pointing to the "
       "quotation marks around 'really magnificent' as the poem's way of putting the language of tourism "
       "in evidence; others have emphasised its Brazilian context and Bishop's own position as an American "
       "in Brazil, and the poem has become a standard text in postcolonial and travel-writing criticism.",
  biblio="First published in The New Yorker, 14 January 1956; collected in Questions of Travel (New York: "
         "Farrar, Straus and Giroux, 1965). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="Read through the text reproduced in anthologies and study sources consulted; the New Yorker date "
        "was confirmed by a separate search of the poem's publication history.",
  ver="partially verified", sources=[W_BIS, NAAL]),
]

WORKS += [
W10("The Armadillo", EB, "1957", "Poem (three stanzas)", "significant",
  genres=G("Nature Poetry", "Free Verse", "Lyric Poetry"),
  themes=T("Violence, crime and justice", "Nature, ecology and environmental crisis", "Art, the artist and the creative life"),
  movements=M("Late Modernism"),
  overview="A poem from Questions of Travel (1965), written in 1956-57 and published in 1957: a night of festival "
           "fire balloons over a Brazilian landscape ends with a small armadillo burning, and the poem is "
           "dedicated to Robert Lowell, who answered it with 'Skunk Hour'.",
  content="Three nine-line stanzas of free verse in which the speaker watches paper fire balloons drift over "
          "the mountains, sees one fall into a hillside, and finds in the morning a burnt armadillo and a "
          "nest of baby rabbits among the ashes.",
  summary="'Now and then one of these fire balloons goes up / and, rising, seems to be a star / or a planet. "
          "/ It is a paper house, a lantern, / with a flame in it.' The poem describes the Brazilian "
          "festival practice of sending up small paper balloons with candles inside, which drift over the "
          "hills at night like 'a kite' or a 'moon'. The first stanza tracks one balloon up and away, and "
          "the second follows another as it begins to come down, over the 'tall, pale, / fireflies' and the "
          "mountains, until it disappears. In the third stanza the speaker finds the place where one fell: "
          "'Last night I saw a fire balloon / crash and burn in the hillside, / and the fire went out, / "
          "and the armadillo / came out of the ground / and the bushes.' The poem's final image is the "
          "animal with its 'rosy, / rabbit-like' ears and its 'weak, / armored' body, and the nest of "
          "rabbits 'all / in a ball' beneath it, burnt: 'a weak, / mailed, / baby, / its / poor / little / "
          "face / ... ' The poem ends on the failure of the beautiful thing - the fire balloon - which turns "
          "out to be a weapon, and on the small creatures that have no idea of the danger above them.",
  themes_text="The poem is about the innocence of beauty and the damage it does: the fire balloons are lovely, "
              "and they are also a fire that falls on animals. Bishop does not moralise, and the poem's "
              "power comes from the equal weight given to the aesthetic pleasure of the first two stanzas "
              "and the cruelty of the last, so that the reader is implicated in enjoying the spectacle. "
              "The dedication to Lowell places the poem in a dialogue about the poet's obligation to "
              "suffering, and the armadillo - armoured, weak, 'rosy' and defenceless - became the poem's "
              "emblem for the vulnerable creature in a beautiful and indifferent world.",
  structure="Three nine-line stanzas of free verse, with the first two describing the balloons and the third "
            "turning to the aftermath; the shift is from the vertical movement of the balloons to the "
            "horizontal ground where the burnt animal lies, and the last stanza slows into a list of the "
            "rabbits' bodies.",
  style="Exact, painterly notation and a tone of unemphatic reportage; long lines broken by commas and "
        "dashes, with the poet's characteristic use of the dash for an aside or a recoil; the diction is "
        "plain until the last lines, where the short words ('weak, / mailed, / baby') and the line breaks "
        "do the emotional work.",
  ctx="Written in Brazil in 1956-57 and published in 1957, collected in Questions of Travel (1965); it is "
      "dedicated to Robert Lowell, and Lowell's 'Skunk Hour' (1958) is dedicated to Bishop in return; the "
      "two poems are the central documents of the exchange between the poets about the limits of the "
      "'confessional' mode.",
  sig="One of Bishop's most anthologised poems and the one most closely tied to her friendship with Lowell; "
      "it is the standard text for discussions of the poet's political and ethical responsibilities, and "
      "its image of the armadillo has become one of the best-known in postwar American poetry.",
  canon="Major canon",
  crit="Criticism reads the poem as Bishop's answer to Lowell's 'Skunk Hour' and as her most direct "
       "statement about the poet's relation to suffering; the fire balloons have been discussed as images "
       "of art, of festivity and of the destructive beauty of the Brazilian landscape, and the poem's "
       "refusal to console has been central to the critical account of her difference from the "
       "confessional poets.",
  biblio="Published in 1957 and collected in Questions of Travel (New York: Farrar, Straus and Giroux, 1965); "
         "the Norton list gives 1957 as the date of first publication. A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E.",
  notes="The place of first publication in 1957 was not identified with certainty in the sources "
        "consulted; the composition date of 1956-57 and the dedication to Lowell are documented, and the "
        "date of 1957 follows the Norton list.",
  ver="partially verified", sources=[W_BIS, NAAL]),
]

WORKS += [
W10("In the Waiting Room", EB, "1971", "Poem (nine stanzas of varying length)", "major",
  genres=G("Free Verse", "Confessional Poetry", "Lyric Poetry"),
  themes=T("Childhood, adolescence and coming of age", "Identity, authenticity and the divided self", "Land, place and regional belonging"),
  movements=M("Confessional Poetry", "Late Modernism"),
  overview="A poem first published in The New Yorker in 1971 and collected in Geography III (1976), in which the "
           "six-year-old Elizabeth, waiting in a dentist's waiting room in Worcester, Massachusetts, in "
           "February 1918, hears her aunt cry out in pain and is overwhelmed by the knowledge that she is "
           "herself - a separate, mortal person, one of 'them'.",
  content="Nine stanzas of free verse, mostly unrhymed, in which the child reads a National Geographic while "
          "her aunt is in the dentist's chair, looks at the photographs of volcanoes and of naked women, "
          "hears a cry of pain, and falls into a trance of self-recognition before returning to the "
          "ordinary street outside.",
  summary="'In Worcester, Massachusetts, / I went with Aunt Consuelo / to keep her dentist's appointment / and "
          "sat and waited for her / in the dentist's waiting room. / It was winter. It got dark / early.' "
          "The opening is deliberately flat and exact: a place, a date (3 February 1918), an aunt, a "
          "waiting room, a copy of the National Geographic with 'a dead man slung on a pole' and 'black, "
          "naked women' with 'horrifying' breasts. The child reads and waits, and then hears 'an oh! of "
          "pain' from the inner office: 'It was me. / ... my aunt was crying out'. The shock is that the "
          "aunt's voice is her own voice, and the poem's central stanzas record the child's vertigo: 'I "
          "said to myself: three days / and you'll be seven years old. / I was saying it to stop / the "
          "sensation of falling off / the round, turning world / into cold, blue-black space.' She looks at "
          "the waiting room as if from outside, at the 'other people' - 'What similarities - / boots, "
          "hands, the family voice / I felt in my throat, or even / the National Geographic / and those "
          "awful hanging breasts - / held us all together / or made us all just one?' The poem's climax is "
          "the recognition 'you are an I, / you are an Elizabeth, / you are one of them', and its ending is "
          "a return: 'Then I was back in it. / The War was on. Outside, / in Worcester, Massachusetts, / "
          "were night and slush and cold, / and it was still the fifth / of February, 1918.'",
  themes_text="The poem is about the birth of self-consciousness, and it locates that birth in a moment of "
              "identification with another person's pain: the child discovers that she is separate because "
              "she hears her aunt's cry as her own. Bishop's interest is in the paradox that the sense of "
              "being an 'I' arrives as a fall - 'falling off / the round, turning world / into cold, "
              "blue-black space' - and that identity is both a horror and a bond: the 'family voice' in "
              "the throat is what makes the child one of 'them'. The National Geographic material adds the "
              "postcolonial and the sexual: the naked women and the 'dead man slung on a pole' are the "
              "child's first images of a wider world, and her recoil from them is part of the same "
              "recognition of a body that is vulnerable and exposed.",
  structure="Nine stanzas of unequal length, from four lines to more than twenty, in loose free verse; the "
            "poem moves from external description to interior monologue and back, and its stanzas are "
            "marked by shifts in the child's attention; the last stanza returns to the outside world and "
            "closes the frame opened by the first.",
  style="Bishop's late free verse at its most exact and least rhetorical: short declarative sentences, "
        "reported speech and quotation marks, a child's diction and a child's non sequiturs, and a "
        "rhythm that follows breath and attention rather than metre; the poem's horror is produced by "
        "plain statement ('It was me') and its comfort by the flat particularity of the last lines.",
  ctx="First published in The New Yorker in July 1971 - Bishop's first new poem in some years - and "
      "collected in Geography III (Farrar, Straus and Giroux, 1976), which won the National Book Critics "
      "Circle Award; the poem's date, 5 February 1918, places it in Bishop's seventh year, and its "
      "Worcester setting is the city of her birth, which she had left as a small child.",
  sig="The poem that reopened Bishop's career after a long silence and one of the most admired American "
      "poems of the 1970s; it is central to the critical account of her late style and is regularly "
      "taught as a study of childhood consciousness and of the autobiographical poem, and it is her "
      "selection in the Norton Anthology alongside 'One Art'.",
  canon="Major canon",
  crit="Criticism has concentrated on the poem's treatment of identity as both a fall and a bond, on the "
       "National Geographic images as the child's introduction to race, gender and history, and on "
       "Bishop's difference from the confessional poets: the poem exposes a childhood trauma, but it does "
       "so with the same reticence and exactness as her descriptions of landscape, and the 'I' is "
       "constructed as a character rather than confessed.",
  biblio="First published in The New Yorker in July 1971; collected in Geography III (New York: Farrar, "
         "Straus and Giroux, 1976). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The exact day of the New Yorker appearance in July 1971 was not verified; the month and year come "
        "from a search of the poem's publication history, and the text was read through the anthologies and "
        "study sources consulted.",
  ver="partially verified", sources=[W_BIS, NAAL]),
W10("One Art", EB, "1976", "Poem (villanelle in nineteen lines)", "major",
  genres=G("Formal Verse", "Elegiac Poetry", "Lyric Poetry"),
  themes=T("Love, intimacy and loss", "Death, illness and mourning", "Art, the artist and the creative life"),
  movements=M("Confessional Poetry", "Late Modernism"),
  overview="A villanelle first published in The New Yorker on 26 April 1976 and collected in Geography III (1976): "
           "the poet instructs herself in the art of losing, from keys and hours to a continent and a loved "
           "one, and the form's refrains register the discipline cracking.",
  content="Nineteen lines in five tercets and a quatrain, with two refrains - 'The art of losing isn't hard to "
          "master' and 'It's evident / the art of losing's not too hard to master / though it may look like "
          "(Write it!) like disaster' - in which a series of losses, each larger than the last, is met with "
          "consoling imperatives.",
  summary="'The art of losing isn't hard to master; / so many things seem filled with the intent / to be lost "
          "that their loss is no disaster.' The poem begins with a maxim that sounds like consolation and "
          "is actually a command: lose things, and do it well. The examples grow steadily larger - door "
          "keys, an hour badly spent, names, a mother's watch, two beloved cities, a continent, 'and, "
          "vaster, / some realms I owned, two rivers, a continent' - and with each the instruction becomes "
          "more insistent: 'Lose something every day. Accept the fluster / of lost door keys, the hour "
          "badly spent. / The art of losing isn't hard to master.' The fake-serious tone is the poem's "
          "engine: the villanelle's refrains repeat like a lesson being learned by rote, and the poet's "
          "'practice' of loss is also a practice of the form. Then, in the fifth stanza, the poem reaches "
          "the loss it cannot absorb: 'I lost two cities, lovely ones. And, vaster, / some realms I owned, "
          "two rivers, a continent. / I miss them, but it wasn't a disaster.' The last stanza turns to the "
          "beloved - 'Even losing you (the joking voice, a gesture / I love) I shan't have lied. It's "
          "evident / the art of losing's not too hard to master / though it may look like (Write it!) "
          "like disaster.' The parenthesis is the poem's breakdown: the poet has to command herself to "
          "write the word 'disaster', and the repetition of 'like' shows the simile and the composure "
          "failing at the same moment.",
  themes_text="The poem is about the discipline of loss and the impossibility of that discipline: its "
              "instructional voice is a defence against grief, and the villanelle's repetitions, which "
              "sound like mastery, are what betray it. 'The art of losing' is the art of making loss into "
              "form, and the poem both performs and mistrusts that transformation; the 'joking voice' it "
              "addresses belongs to Alice Methfessel, from whom Bishop was separated when she wrote the "
              "poem, and the small domestic losses of the opening become the measure of the large one at "
              "the end, so that the poem's scale is one of its subjects.",
  structure="A villanelle: five tercets and a closing quatrain, nineteen lines in all, with two refrains that "
            "recur alternately; the refrains are varied - 'isn't hard to master' becomes 'not too hard to "
            "master' - and the rhymes (master/disaster, intent/spent, gesture/master) are carried by "
            "assonance and by the poem's repeated vocabulary rather than by exact rhyme.",
  style="Conversational, dry, almost prosaic in diction, with exclamations and parentheses that dramatise "
        "the speaker's struggle for composure ('(Write it!)'); the line is loose iambic pentameter, and "
        "the poem's flatness is the point: the tone is that of someone giving herself instructions, and "
        "the poetry is in the mask slipping.",
  ctx="First published in The New Yorker on 26 April 1976 and collected in Geography III (1976); Bishop "
      "wrote as many as eight drafts of the poem over years, and it belongs to the last period of her "
      "life, when she was teaching at Harvard, ill with asthma and separated from Alice Methfessel. It "
      "is one of the poems that revived the villanelle in late twentieth-century English verse.",
  sig="Bishop's best-known poem and one of the most admired villanelles in English; it is the poem through "
      "which her work is most often introduced, it is central to every account of her late style and of "
      "the modern revival of the villanelle, and it is universally anthologised, in the Norton Anthology "
      "and outside it.",
  canon="Major canon",
  crit="The poem's criticism has concentrated on the relation between form and feeling - the villanelle's "
       "repetitions as an image of the mind circling grief - and on the autobiographical occasion in "
       "Bishop's separation from Alice Methfessel; the surviving drafts, discussed by Bishop's editors and "
       "biographers, show her working towards the parenthesis '(Write it!)', which is now treated as one of "
       "the great moments of twentieth-century American poetry.",
  biblio="First published in The New Yorker, 26 April 1976; collected in Geography III (New York: Farrar, "
         "Straus and Giroux, 1976). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The number of drafts (given here as 'as many as eight') is reported in the sources consulted and "
        "was not checked against the manuscripts; the dating of the New Yorker appearance is from a search "
        "of the poem's publication history and agrees with the Norton list.",
  ver="partially verified", sources=[W_ONEART, W_BIS, NAAL]),
]

WORKS += [
W10("A Streetcar Named Desire", TW, "1947", "Play (eleven scenes)", "major",
  genres=G("Modern Tragedy", "Gothic Fiction", "Full-Length Play"),
  themes=T("Sexuality, desire and the closet", "Class, labour and social mobility", "Memory, trauma and testimony"),
  movements=M(SOGOTH, "Late Modernism"),
  overview="The play that opened on Broadway on 3 December 1947: Blanche DuBois, a schoolteacher from Laurel, "
           "Mississippi, comes to her sister Stella's two-room flat in the French Quarter of New Orleans, and "
           "the brutal, tender world of her brother-in-law Stanley Kowalski destroys her illusions and finally "
           "her mind.",
  content="Eleven scenes, a single set of two rooms and a bath in the Elysian Fields, five characters - "
          "Blanche, Stella, Stanley, Mitch and the neighbour Eunice - and a plot that moves from Blanche's "
          "arrival, through the poker night, the courtship by Mitch, the revelation of her past in Laurel, "
          "the rape, and the final removal to the state asylum.",
  summary="Blanche DuBois arrives at the Elysian Fields, the shabby quarter of New Orleans where her sister "
          "Stella lives in two rooms with her husband Stanley Kowalski, carrying a suitcase of clothes and "
          "a trunk of papers; she has lost the family plantation, Belle Reve, and has been dismissed from "
          "her teaching job in Laurel, Mississippi. She is horrified by the flat, the neighbourhood and "
          "Stanley, and she sets about trying to improve Stella's life and to arrest her own decline: she "
          "drinks, she bathes constantly, she avoids strong light and she flirts with Stanley's friend "
          "Mitch, a gentle, unmarried man who lives with his dying mother. Stanley, who has been checking "
          "on Blanche's story, discovers that she was dismissed for an affair with a student, that she has "
          "been living in a hotel in Laurel and that she has been promiscuous since; he tells Mitch, who "
          "abandons her. Stella goes into labour; while Stanley and Stella are at the hospital, Blanche, "
          "left alone in the flat, is raped by Stanley. In the last scene the family and the doctor and "
          "matron wait while Blanche, who has lost her grip on reality, is taken to a mental institution; "
          "she goes with the doctor with the line 'Whoever you are - I have always depended on the kindness "
          "of strangers.' The play's famous other elements - the poker game, the streetcar named Desire "
          "that brings Blanche to the quarter and the one named Cemeteries, the Varsouviana polka that "
          "plays in her head, the paper lantern she puts over the light bulb, Stanley's cry of 'Stella!' - "
          "carry its themes as much as its dialogue does.",
  themes_text="The play's central subject is the collision between illusion and desire: Blanche lives by "
              "illusions - of gentility, of purity, of art and of the past - and Stanley lives by an "
              "appetite that is honest, brutal and destructive. Williams makes both attractive and both "
              "damaging, and refuses the moral comfort of choosing between them; the Southern past, with "
              "Belle Reve and its 'epic fornications', is present as a burden and a lie, and the play's "
              "treatment of sexuality - Blanche's promiscuity, her husband's homosexuality and suicide, "
              "Stanley's rape - was among the frankest on the American stage of its time. Its other "
              "subject is the vulnerability of women in a world of male violence and male codes, and the "
              "final image of Blanche led away is an indictment as much of the society that has no place "
              "for her as of Stanley.",
  structure="Eleven scenes rather than acts, moving without interval through a single set that represents "
            "both the Kowalskis' two rooms and the street outside; the play's time is compressed into a "
            "few months and its action is organised around a series of confrontations - the poker night, "
            "the birthday party, the revelation of the past, the rape - with expressionist devices "
            "(music, light, the paper lantern, the offstage streetcar) carrying the inner life.",
  style="A lyrical, image-rich dialogue that lifts Southern speech into poetry; long monologues and "
        "confession scenes for Blanche, short brutal exchanges for Stanley; extensive stage directions "
        "that function as prose poems; the sound of the Varsouviana polka and the streetcar used as "
        "musical motifs, and light used symbolically throughout.",
  ctx="Premiered on Broadway at the Ethel Barrymore Theatre on 3 December 1947, directed by Elia Kazan, with "
      "Jessica Tandy as Blanche, Kim Hunter as Stella, Marlon Brando as Stanley and Karl Malden as Mitch; "
      "it won the Pulitzer Prize for Drama in 1948 and was published by New Directions in 1947. Its "
      "Southern Gothic setting, its frankness about sex and its Method-acting production made it the "
      "defining American play of the immediate postwar years, and the 1951 film, also directed by Kazan, "
      "fixed it in popular culture.",
  sig="One of the two or three most important American plays of the twentieth century and the work through "
      "which Williams's reputation is measured; it is a standard text in the study of American drama, of "
      "Southern literature and of tragedy in a modern setting, and its characters - Blanche, Stanley, "
      "Stella - have become cultural archetypes.",
  canon="Major canon",
  crit="Criticism has read the play through the Southern Gothic tradition, through psychoanalysis (Blanche's "
       "narcissism, Stanley's brutality, the play's Oedipal undercurrents), through gender and queer "
       "theory (the homosexuality of Blanche's dead husband Allan Grey and the play's treatment of "
       "masculinity) and through class (the decline of the plantation aristocracy and the rise of the "
       "immigrant working class). Its staging history, from Kazan's production to later revivals, is a "
       "central topic of American theatre scholarship, and the 1951 film's censorship of the rape has been "
       "much discussed.",
  chars="Blanche DuBois, a former schoolteacher from Laurel, Mississippi, who has lost Belle Reve and her "
        "reputation and lives by illusion; Stella Kowalski, her younger sister, who has chosen Stanley and "
        "the Quarter over her sister; Stanley Kowalski, a Polish American factory worker and bowler, "
        "sensual, brutal and shrewd; Harold 'Mitch' Mitchell, Stanley's friend, who courts Blanche and "
        "abandons her when he learns of her past; Eunice Hubbell, the upstairs neighbour; Allan Grey, "
        "Blanche's dead husband, present only in memory; Steve Hubbell and Pablo Gonzales, the poker "
        "players; a young collector, a nurse and a doctor in the last scene.",
  biblio="First published by New Directions (New York, 1947); premiered at the Ethel Barrymore Theatre, New "
         "York, on 3 December 1947. A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The play's text was not read complete; the summary follows the published play as described in the "
        "sources consulted, and quotations are limited to the best-known lines.",
  ver="partially verified", sources=[W_STREETCAR, NAAL]),
W10("The Swimmer", JC, "1964", "Short story", "major",
  genres=G("Short Story", "Satirical Fiction", "Modernist Fiction"),
  themes=T("The city, the suburb and modern space", "Death, illness and mourning", "Class, labour and social mobility"),
  movements=M("Late Modernism", POSTMOD),
  overview="A story first published in The New Yorker on 18 July 1964 and collected in The Brigadier and the Golf "
           "Widow the same year: on a bright Sunday in midsummer, Neddy Merrill decides to swim home across "
           "Westchester County through his neighbours' pools, and the afternoon turns into a journey through "
           "a whole life and its losses.",
  content="A single continuous narrative in which Neddy Merrill, 'a slender man' in his forties, sets out from "
          "a pool party at the Westerhazys' to swim the eight miles home through a chain of private pools he "
          "names the 'Lucinda River' after his wife, and finds at each pool a colder season, a drier "
          "welcome and more of his life gone.",
  summary="The story opens in high summer: 'It was one of those midsummer Sundays when everyone sits around "
          "saying, I drank too much last night.' Neddy Merrill, hungover and happy, is at a party with his "
          "wife Lucinda, and the idea comes to him - 'Making his way home by an uncommon route' - that he "
          "will swim home through the pools of the neighbourhood, the Bunkers', the Levys', the Welchers' "
          "(whose pool is empty), the Hallorans', the Sachses', the Biswangers', Shirley Adams's, and so "
          "home. The first pools are festive, full of friends and drinks, and Neddy is a man in excellent "
          "shape who 'might have been described as a hearty man'; but the signs accumulate. The Welchers' "
          "pool is dry and their house is for sale. The Hallorans, an elderly couple, receive him naked "
          "and mention, in passing, that his children have been in trouble. At the Biswangers' party he is "
          "treated as an intruder. Shirley Adams, once his mistress, is cool to him. The light changes, "
          "the leaves blow, and by the time Neddy reaches his own house it is dark, the doors are locked "
          "and the house is empty: 'He shouted, pounded on the door, tried to force it with his shoulder, "
          "and then, looking in at the windows, saw that the place was empty.'",
  themes_text="The story is an American fable of the man who refuses to see that his life has collapsed: "
              "Neddy's swim is a journey through time disguised as a journey through space, and the pools "
              "measure out his losses - money, friends, a mistress, his children, his house, his wife - "
              "while he experiences them as a single afternoon of pleasure. Cheever's subject is the "
              "suburban middle class and its self-deception, and the story's fantastic premise is the "
              "vehicle for a realistic account of failure; the name 'Lucinda River' turns the swim into a "
              "mock-epic journey, and the empty house at the end is a judgment delivered without a "
              "moralist.",
  structure="A single continuous narrative with no chapter or scene breaks, moving from pool to pool in a "
            "strictly linear way; the passage of time is registered almost entirely through the weather, "
            "the light, the leaves and the behaviour of the people, and the reader is left to infer the "
            "discrepancy between Neddy's experience and the truth.",
  style="A lucid, elegant, faintly ironic third-person prose that keeps a straight face while the events "
        "turn impossible; exact social notation (drinks, wet hair, tennis shoes, the names of the pools); "
        "a habit of mythic or apocalyptic imagery inside an ordinary scene; and a closing sentence that "
        "refuses explanation.",
  ctx="Published in The New Yorker on 18 July 1964 and collected in The Brigadier and the Golf Widow (1964) "
      "and The Stories of John Cheever (1978); Cheever had conceived the story originally as a novel and "
      "had written some 150 pages of notes before reducing it to a story, and its Westchester setting and "
      "its suburban swimming pools belong to the landscape of his own life at Ossining, New York.",
  sig="Cheever's most anthologised story and a standard text in the American short-story canon; its "
      "fantastic premise and its treatment of time have made it a favourite of critics and of teachers of "
      "fiction, and the 1968 film with Burt Lancaster, from a screenplay by Eleanor Perry, gave it a "
      "second life.",
  canon="Major canon",
  crit="Criticism reads the story as a modern myth of the fall, as a portrait of suburban self-deception, "
       "and as a formal experiment in which the narrative's temporality is the plot's real subject; "
       "Cheever's own notes and the 1968 film are frequently discussed, and the story is often compared "
       "with Fitzgerald's Gatsby and with Joyce's 'The Dead' as a study of a man who fails to understand "
       "his own life.",
  biblio="First published in The New Yorker, 18 July 1964; collected in The Brigadier and the Golf Widow "
         "(New York: Harper and Row, 1964) and in The Stories of John Cheever (New York: Knopf, 1978). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was not read complete; the summary follows the published text as described in the "
        "sources consulted, and quotations are limited to the best-known lines.",
  ver="partially verified", sources=[W_SWIM, W_CHEEVER, NAAL]),
]

WORKS += [
W10("Those Winter Sundays", RH, "1962", "Poem (three quatrains and a closing line)", "major",
  genres=G("Elegiac Poetry", "Free Verse", "Lyric Poetry"),
  themes=T("Family, marriage and domestic life", "Class, labour and social mobility", "Love, intimacy and loss"),
  movements=M("Postwar African American Writing: Protest and Its Critics"),
  overview="A poem from A Ballad of Remembrance (1962) in which an adult remembers his father getting up in the "
           "blueblack cold of Sunday mornings to bank the fires and polish his good shoes before church, and "
           "regrets that as a child he never thanked him for the labour that made the house warm.",
  content="Three quatrains and a single closing line, in free verse with one rhyme, in which the father's "
          "Sunday labours - lighting fires, polishing shoes, calling the family - are set against the boy's "
          "indifference and the poem's final question about 'love's austere and lonely offices'.",
  summary="'Sundays too my father got up early / and put his clothes on in the blueblack cold, / then with "
          "cracked hands that ached / from labor in the weekday weather made / banked fires blaze. No one "
          "ever thanked him.' The first sentence establishes the poem's whole situation: the father's "
          "habitual, unthanked labour, performed before dawn on the one day of rest. The second stanza "
          "moves inside the house - 'I'd wake and hear the cold splintering, breaking' - and the child "
          "waits, hearing the house warm and the father call, until 'slowly I would rise and dress, / "
          "fearing the chronic angers of that house'. The third stanza turns to the poem's other detail: "
          "'Speaking indifferently to him, / who had driven out the cold / and polished my good shoes as "
          "well.' The single rhyme of the poem, 'cold'/'shoes as well' in the third stanza (and "
          "'ach-ed'/'thanked' in the first), does its work quietly, and the last line, set apart, is the "
          "poem's whole meaning: 'What did I know, what did I know / of love's austere and lonely "
          "offices?' The repetition of the question is not a rhetorical flourish but a confession that "
          "the knowledge came too late, and 'offices' - both duties and church services - joins the "
          "father's Sunday labour to the language of the church he was preparing his family for.",
  themes_text="The poem is about a love expressed as labour rather than as speech, and about the child's "
              "failure to recognise it: the father's 'cracked hands', the 'banked fires' and the polished "
              "shoes are the poem's evidence, and the adult speaker's regret is its verdict. Its racial "
              "and historical context is present but unnamed - the 'weekday weather' of a Black working "
              "man's labour, the 'chronic angers' of a household under pressure - and Hayden's refusal to "
              "make the poem a document of protest is precisely what made him a controversial figure in "
              "the 1960s; the poem's power comes from its specificity, which is also a kind of "
              "representativeness.",
  structure="Three quatrains and a single separated line; the quatrains are unrhymed except for the "
            "assonantal 'ached'/'thanked' and the rhyme of 'cold' with the third stanza's end, and the "
            "poem's movement is from the father's actions to the boy's fear to the adult's regret, with "
            "the final line turning the description into a question.",
  style="Plain, exact, unadorned free verse with heavy stresses and a sparse syntax; the diction is "
        "domestic and physical ('blueblack cold', 'cracked hands', 'banked fires', 'the cold "
        "splintering'), and the poem's effects are made by line breaks, by the one rhyme and by the "
        "repetition of the final question.",
  ctx="A Ballad of Remembrance (1962) was Hayden's third collection and the book in which his mature style "
      "appeared; the poem belongs to his poems about his Detroit childhood and foster family, and its "
      "appearance in the same year as the revised 'Middle Passage' marks the point at which Hayden's "
      "historical and domestic poems were being read together. It is one of his most anthologised poems "
      "and a staple of American school anthologies.",
  sig="One of the most widely taught American poems of the twentieth century and Hayden's best-known work; "
      "it is a standard text in courses on the American family poem, on African American poetry and on "
      "the sonnet-sized lyric, and its final line is among the most quoted in modern American verse.",
  canon="Major canon",
  crit="Criticism has read the poem as a study in the expression of love through work, as a portrait of "
       "Black working-class fatherhood, and as a poem about the belatedness of understanding; the phrase "
       "'love's austere and lonely offices' is regularly discussed as the poem's centre, and the poem's "
       "reticence has been central to the argument that Hayden's lyricism was a political as well as an "
       "aesthetic choice.",
  biblio="Published in A Ballad of Remembrance (London: Paul Breman, 1962). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="Read through the text reproduced in anthologies and study sources consulted; the poem's stanza "
        "form and its single rhyme were checked against more than one transcription.",
  ver="partially verified", sources=[W_HAY, NAAL]),
W10("Summertime and the Living . . .", RH, "1962", "Poem (four sections)", "significant",
  genres=G("Free Verse", "Narrative Poetry", "Lyric Poetry"),
  themes=T("Childhood, adolescence and coming of age", "Race, racism and the struggle for civil rights", "Land, place and regional belonging"),
  movements=M("Postwar African American Writing: Protest and Its Critics"),
  overview="A poem from A Ballad of Remembrance (1962) whose title takes its cue from Gershwin's 'Summertime': a "
           "series of remembered and imagined scenes of Black childhood and community life in Detroit and "
           "the rural South, held together by heat, song and the presence of violence.",
  content="Four sections of free verse in which the speaker remembers a childhood summer - the streets, the "
          "porches, the music, the revivals, a woman singing, and the news of a killing - and sets the "
          "pleasures of the season against the knowledge of what awaits the children who live in it.",
  summary="The poem opens in the heat of a remembered summer and moves through a series of scenes rather "
          "than a single narrative: children playing in the street, a woman singing, the 'good times' of "
          "a neighbourhood, and, cutting across them, the violence that the community lives with. Its "
          "title borrows the opening of Gershwin's aria from Porgy and Bess, and the ellipsis in the title "
          "is the poem's point: the song's promise of easy living is broken off before it can be "
          "completed. Hayden's scenes are rendered with the same exactness as 'Those Winter Sundays' - "
          "the physical detail of heat, water, voices and music - and the poem's structure is musical, "
          "returning to its refrain-like images of summer as it moves between the remembered and the "
          "reported. The poem's ending does not resolve the tension between the idyll and the violence "
          "but holds the two together, which is the characteristic gesture of Hayden's poems of Black "
          "American life.",
  themes_text="The poem is about the double life of a Black childhood: the warmth and richness of community "
              "and the constant proximity of racial violence. Its Gershwin title points to the way American "
              "culture has packaged Black life as song and sunshine, and the poem's four sections restore "
              "the history that the song leaves out, without surrendering the pleasure that the song "
              "names. Hayden's refusal to choose between celebration and protest is the poem's argument, "
              "and it is the reason the poem has been central to discussions of his place between the "
              "Black Arts Movement and the earlier protest tradition.",
  structure="Four numbered sections of free verse of unequal length, organised by image and by recurrence "
            "rather than by narrative; the sections shift between first person and third person and "
            "between past and present, and the poem's title functions as a refrain that the sections "
            "answer.",
  style="A lyric free verse with a strong sense of song, using repetition, refrain-like phrases and the "
        "cadences of Black speech and of hymns; the diction is concrete and sensory (heat, dust, water, "
        "voices), and the poem's shifts of register - from the conversational to the elegiac - are managed "
        "by line breaks and by changes of scene.",
  ctx="A Ballad of Remembrance (1962) was published in London by Paul Breman as part of the Heritage "
      "series and won the Grand Prix de la Poésie at the first World Festival of Negro Arts in Dakar in "
      "1966; the poem belongs to Hayden's poems of Black American life written before the Black Arts "
      "Movement made his reticence controversial, and its Detroit and Southern material reflects his "
      "own upbringing in Paradise Valley and his research into his family's Southern past.",
  sig="One of Hayden's most anthologised poems and the companion to 'Those Winter Sundays' in the Norton "
      "selection; it is a standard text for the study of his treatment of childhood and community and for "
      "the debate about protest and art in African American poetry of the 1960s.",
  canon="Secondary canon",
  crit="Criticism has discussed the poem's use of the Gershwin song as an ironic frame, its structure of "
       "lyric scenes and its place in Hayden's argument with the protest poetry of the 1960s; the poem is "
       "often read beside 'Those Winter Sundays' as evidence of his range, and its treatment of violence "
       "within a lyric idyll has been central to the critical reassessment of his work since the 1980s.",
  biblio="Published in A Ballad of Remembrance (London: Paul Breman, 1962). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem was not read complete; the summary follows the text and commentary in the sources "
        "consulted, and the reading of the Gershwin title is the standard critical one rather than a "
        "quotation from Hayden.",
  ver="partially verified", sources=[W_HAY, NAAL]),
]
