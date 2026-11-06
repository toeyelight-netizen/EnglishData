"""Installment 10, wave 14: the Norton selections of authors recorded by installment 9.

Jean Rhys, Samuel Beckett and W. H. Auden (The Norton Anthology of English Literature,
11th edition, vol. F) and Gwendolyn Brooks (The Norton Anthology of American Literature,
vol. E) have author records from installment 9. Their selections first published
1946-2000 are recorded here and linked to those records; the installment-10 statements of
their bibliographies are the extensions in i10_extensions.py.

Waiting for Godot is recorded as Beckett's English text (1954), the version Norton prints,
with the French original (En attendant Godot, 1952) named in the record. Brooks's poems are
recorded singly, each naming its collection; the NAAL list gives no page numbers.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import W10, G, T, M, NAEL, NAAL  # noqa: E402

RHYS = "Jean Rhys"
SB = "Samuel Beckett"
WHA = "W. H. Auden"
GB = "Gwendolyn Brooks"
CAR = "Caribbean Literature in English"
POSTCOL = "Postcolonial Literature"
ABSURD = "Theatre of the Absurd"
PROTEST = "Postwar African American Writing: Protest and Its Critics"
BAM = "Black Arts Movement"

CAM_RHYS = "'The Day They Burned the Books' (chapter 6 of a Cambridge University Press study of Jean Rhys, Cambridge Core)"
W_SIOL = "Sleep It Off Lady (Wikipedia)"
TROVE_SIOL = "Sleep It Off Lady: Stories (Trove, National Library of Australia)"
W_GODOT = "Waiting for Godot (Wikipedia)"
W_LIME = "In Praise of Limestone (Wikipedia)"
W_SHIELD = "The Shield of Achilles (Wikipedia)"
W_WRC = "We Real Cool (Wikipedia)"
W_AA = "Annie Allen (Wikipedia)"
GALE_BE = "The Bean Eaters (Gale, Poetry for Students, via Encyclopedia.com)"
NPG_GB = "Gwendolyn E. Brooks, portrait by Sara S. Miller (National Portrait Gallery, Smithsonian), exhibition label"
RG_TILL = "Maids Mild and Dark Villains, Sweet Magnolias and Seeping Blood: Gwendolyn Brooks's Poetic Response to the Lynching of Emmett Till (ResearchGate abstract)"
SAGE_GB = "Brooks, Gwendolyn (SAGE Encyclopedia of Motherhood)"
PENN_MECCA = "In the Mecca: Poems (University of Pennsylvania Libraries, Franklin catalogue)"
BBP_DIAS = "To The Diaspora (work) (Black Bibliography Project, Rutgers University)"

WORKS = [
W10("The Day They Burned the Books", RHYS, "1960", "Short story", "significant",
  genres=G("Short Story"),
  themes=T("Decolonisation, the end of empire and the new nation", "Race, racism and the struggle for civil rights",
           "Childhood, adolescence and coming of age"),
  movements=M(CAR, POSTCOL),
  overview="A short story by Jean Rhys, set in the Dominica of her childhood around the turn of the twentieth century and "
           "told by a white Creole girl who remembers her friend Eddie and the day his mother burned his dead father's "
           "books. Rhys wrote it while she was working on Wide Sargasso Sea, and it was published in 1960, six years "
           "before the novel; it was collected in Tigers Are Better-Looking (1968).",
  content="The narrator's friendship with Eddie Sawyer, the son of an Englishman and a coloured wife; Mr Sawyer's room of "
          "books from England; his death, and the afternoon when Mrs Sawyer clears the room, sorting the books to be sold "
          "or burned; the two children's attempt to save a book each.",
  summary="The narrator, a white Creole girl of twelve on a West Indian island, recalls her friend Eddie, small, "
          "consumptive and precocious, the son of Mr Sawyer, an Englishman who works as an agent for a steamship line and "
          "has settled on the island for no reason anyone can see. He is not a gentleman by colonial standards, and he "
          "treats his pretty, nicely educated coloured wife with insulting contempt. His one passion is the room of books "
          "he has had sent out from England, which Eddie calls his own and where the children read; through Eddie the "
          "narrator first comes to doubt the England the colonials call home. After "
          "Mr Sawyer dies suddenly, Mrs Sawyer and her servant clear the room, sorting the books into those to be sold and "
          "those to be burned, and Mrs Sawyer tears and pitches them with evident satisfaction. Eddie protests and rushes "
          "at her, and in the confusion the two children each snatch a book and run. Eddie's is Kim, torn; the narrator's "
          "turns out to be Maupassant's Fort comme la mort, in French.",
  themes_text="Books stand for the culture and authority of England, which the white colonial child has learned to revere "
              "and which the coloured wife, humiliated by the man who owned them, rejects; the burning gives her a "
              "revenge. The children inherit both the love and the hatred. The story turns on race, class and gender "
              "within a colonial household, and on the child's first doubts about the mother country.",
  structure="A first-person reminiscence told from an unspecified later date but through the child's eyes, as a cluster "
            "of vivid memories; brief scenes build to the single afternoon of the burning and end abruptly with the "
            "two rescued books.",
  style="Plain, exact and economical prose; imagistic detail of heat, light and the room; the child's half-understanding "
        "of adult tensions conveyed without commentary.",
  ctx="Written in the years when Rhys, long out of print and thought by many to be dead, was working on Wide Sargasso Sea, "
      "and drawing on her childhood in Dominica, where she was born in 1890; the story looks back to the colonial "
      "society of about 1900.",
  sig="One of Rhys's most discussed stories and a companion piece to Wide Sargasso Sea, it is a frequently anthologised "
      "text of Caribbean and postcolonial writing; Norton prints it with \"On Not Shooting Sitting Birds\".",
  crit="A Cambridge University Press study of Rhys devotes a chapter to it, reading the title as an echo of Caliban's plot "
       "to burn Prospero's books and the story as one about the rejection of colonialism, about how the children of "
       "colonialism deal with their inheritance of love and hate, and about how Rhys became the kind of writer she was.",
  canon="Secondary canon",
  biblio="First published in 1960 (the periodical was not identified in the sources consulted); collected in Tigers Are "
         "Better-Looking (1968). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, "
         "beginning on page 566.",
  notes="The Norton list's note that the story first appeared in the London Magazine (1960) was not confirmed. The plot "
        "details beyond the Cambridge chapter's summary (the sorting of the books, the two rescued books) are stated from "
        "general knowledge of the text; unauthorised online copies of the story were not used.",
  ver="partially verified", sources=[CAM_RHYS, NAEL]),
W10("On Not Shooting Sitting Birds", RHYS, "1976", "Short story", "minor",
  genres=G("Short Story"),
  themes=T("Love, intimacy and loss", "Migration, exile and diaspora", "Gender, feminism and women's lives"),
  movements=M(CAR),
  overview="A short story by Jean Rhys, collected in Sleep It Off Lady (1976), her last collection, after an earlier "
           "printing in The New Yorker: a young West Indian woman in London recalls an evening with an Englishman that "
           "goes wrong over a story about shooting birds.",
  content="An evening out between a young woman from the Caribbean and an Englishman she hopes to impress, and the remark "
          "about shooting birds at home that ends his interest in her.",
  summary="The narrator, a young woman from the West Indies living in London, goes out with an Englishman she wants to "
          "please. Trying to interest him, she talks about her island and about going out shooting there; when he "
          "gathers that she has shot sitting birds, the one thing his sporting code forbids, he is put off, the evening "
          "falls flat and he drops her for good.",
  themes_text="Misunderstanding across nationality and class, the outsider's failed attempt to speak the codes of English "
              "respectability, and the woman's vulnerability and self-possession in an affair that does not happen.",
  structure="A brief first-person reminiscence, one of the stories of Sleep It Off Lady that follow a Caribbean heroine "
            "from girlhood through Edwardian London.",
  style="Spare, understated prose and dialogue in which the comedy of manners is barely distinguished from humiliation.",
  ctx="Sleep It Off Lady, published by André Deutsch in October 1976, arranges sixteen stories chronologically from the "
      "Dominica of the 1890s to the old age of its last heroines; Rhys died in 1979.",
  sig="One of the late stories that confirmed Rhys's revival after Wide Sargasso Sea; Norton pairs it with \"The Day They "
      "Burned the Books\".",
  canon="Minor canon",
  biblio="Collected in Sleep It Off Lady (London: André Deutsch, 1976), which lists it among its sixteen stories; earlier "
         "printed in The New Yorker (date not established). A selection of The Norton Anthology of English Literature, "
         "11th edition, vol. F, beginning on page 570.",
  notes="Wikipedia's summary of the collection calls the heroine Elsa; whether she is named in this story was not checked. "
        "The date of the New Yorker printing was not established, so 1976 is the date recorded.",
  ver="partially verified", sources=[W_SIOL, TROVE_SIOL, NAEL]),
W10("Waiting for Godot", SB, "1954", "Play (tragicomedy in two acts; the author's English version of En attendant Godot)",
  "major",
  genres=G("Absurdist Drama", "Modern Tragicomedy", "Full-Length Play"),
  themes=T("Alienation, absurdity and existential freedom", "Faith, doubt and the sacred", "Death, illness and mourning"),
  movements=M(ABSURD),
  alt=["En attendant Godot"],
  overview="Samuel Beckett's tragicomedy in two acts, in which two tramps, Vladimir and Estragon, wait by a leafless tree "
           "on a country road for a Mr Godot, who never comes. Beckett wrote it in French between October 1948 and January "
           "1949; En attendant Godot was published in 1952 and first performed in Paris in January 1953, and his own "
           "English version, recorded here because it is the text Norton prints, was published in 1954 and first staged "
           "in London in 1955. It is his best-known work and one of the most influential plays of the century.",
  content="Two acts on two successive evenings, each with the same shape: Vladimir and Estragon pass the time waiting for "
          "Godot; the master Pozzo and his servant Lucky pass by; a boy brings word that Godot will not come today but "
          "surely tomorrow; the two decide to go and do not move. Between the acts Pozzo has gone blind and Lucky dumb, "
          "and the tree has put out a few leaves.",
  summary="Act I. On a country road by a bare tree, in the evening, Estragon struggles to pull off his boot and tells "
          "Vladimir that he spent the night in a ditch and was beaten. They talk at length, about the two thieves "
          "crucified with Christ and why only one gospel says one was saved, about hanging themselves from the tree, and "
          "about the man they are waiting for, Godot, though they are not sure they have ever met him, whether this is "
          "the right place or the right day, or what they asked him for. Pozzo arrives, driving Lucky before him on a "
          "rope and laden with his bags. Pozzo eats chicken while Estragon begs for the bones, lectures on the twilight, "
          "and says he is taking Lucky to the fair to sell him. At Pozzo's order Lucky dances and then, told to think, "
          "pours out a torrent of broken academic and theological speech about a personal God and a shrinking, "
          "petrifying humanity, which ends only when the others seize his hat. Pozzo and Lucky leave. A boy comes with "
          "a message from Mr Godot: he will not come this evening but surely tomorrow. The boy minds the goats; his "
          "brother, who minds the sheep, is beaten. Night falls and the moon rises. 'Well, shall we go?' 'Yes, let's "
          "go.' They do not move.\n\n"
          "Act II. The next day, the same time and place; the tree has a few leaves. Vladimir sings a circular song "
          "about a dog; Estragon has been beaten again and remembers little of yesterday. To pass the time they abuse "
          "each other, make up, exercise, play at being Pozzo and Lucky and juggle hats, including the one Lucky left "
          "behind. Pozzo and Lucky return: Pozzo is now blind and Lucky dumb, and they fall in a heap from which Vladimir "
          "and Estragon, after much delay, raise them. Pozzo remembers nothing of the day before and, asked when his "
          "blindness came, rages that one day is like any other: they give birth astride of a grave, the light gleams "
          "an instant, then it is night once more. When they have gone Vladimir, watching Estragon sleep, wonders "
          "whether he too is asleep and what he will remember of today. The boy returns, or another like him, says he "
          "did not come yesterday and repeats the message: Mr Godot will not come this evening but tomorrow. Godot, "
          "the boy says, does nothing, and his beard is white. The two try to hang themselves with the cord that holds up "
          "Estragon's trousers, which breaks, and the trousers fall. They will hang themselves tomorrow, unless Godot "
          "comes; then they will be saved. 'Well? Shall we go?' 'Yes, let's go.' They do not move.",
  themes_text="Waiting is the play's subject and its form: in the absence of Godot, whom the characters and audiences "
              "have read as God, meaning, rescue or nothing at all, life becomes a matter of filling time with talk, "
              "routine and play. The pairing of Vladimir and Estragon, mutually dependent and unable to part, and of "
              "Pozzo and Lucky, master and slave bound by a rope, gives the play its account of human relations, of "
              "habit, cruelty and need. Memory fails, time repeats with small changes, and suffering is unexplained; "
              "the story of the two thieves frames the question of arbitrary salvation. Yet the play is also a comedy "
              "of friendship and endurance, in which the companions keep each other going and the music-hall routines "
              "are a kind of courage.",
  structure="Two acts of nearly identical design, the second a variation of the first with the decline of Pozzo and "
            "Lucky; a single setting (a country road, a tree, evening); cross-talk, repetition, routines, pauses and "
            "silences; Lucky's monologue as the one unbroken torrent of speech; each act ends with an exchange "
            "contradicted by the stage direction 'They do not move'.",
  style="Spare, rhythmic dialogue built from short exchanges, repetitions and echoes; the comedy of the music hall, "
        "the circus and silent film (hats, boots, falling trousers) set against lyrical and philosophical passages; "
        "an English version that keeps the French text's plainness while adding its own idiom.",
  ctx="Beckett, an Irish writer living in Paris, turned to writing in French after the Second World War, in which he had "
      "served in the Resistance; he wrote the play between his novels Malone meurt and L'Innommable. Roger Blin directed "
      "the premiere at the Théâtre de Babylone in January 1953. Martin Esslin later placed it at the head of what he "
      "called the Theatre of the Absurd.",
  sig="Voted the most significant English-language play of the twentieth century in a 1998 poll by the Royal National "
      "Theatre, the play transformed modern drama in Britain, Ireland, Europe and America, freeing the stage from plot "
      "and psychological realism and influencing Pinter, Stoppard and generations of dramatists. It made Beckett famous "
      "and was central to the case for his Nobel Prize in Literature (1969). It is constantly revived, adapted and "
      "studied, and Norton prints it entire.",
  crit="Critics have called it one of the most enigmatic plays of modern literature, and its readings are religious, "
       "philosophical, classical, social, psychoanalytical and biographical. Esslin's The Theatre of the Absurd (1961) "
       "made it the type of a theatre that presents the absurdity of the human condition without arguing about it; "
       "Beckett himself refused to explain Godot. Its first English-language reception was divided, until critics such "
       "as Harold Hobson and Kenneth Tynan championed it.",
  chars="Vladimir (Didi); Estragon (Gogo); Pozzo; Lucky; a Boy",
  comp=("1948", "1949"), perf="1955", canon="Major canon",
  biblio="Written in French between 9 October 1948 and 29 January 1949; published as En attendant Godot (Paris, 1952) and "
         "first performed at the Théâtre de Babylone, Paris, on 5 January 1953. Beckett's own English version was "
         "published in 1954 and first performed in London in 1955. A selection of The Norton Anthology of English "
         "Literature, 11th edition, vol. F, beginning on page 613.",
  notes="The composition dates, the French publication and premiere, the London premiere year and the 1998 poll come from "
        "Wikipedia (citing Federman and Fletcher's bibliography and Ackerley and Gontarski). The English publication "
        "(Grove Press, New York, 1954), the London director (Peter Hall, Arts Theatre) and the reviewers Hobson and Tynan "
        "are general knowledge, not checked against a consulted source; so are Beckett's war service, the place of the "
        "play among his French novels, Esslin's date, the Nobel year and the play's influence on later dramatists.",
  ver="partially verified", sources=[W_GODOT, NAEL]),
W10("In Praise of Limestone", WHA, "1948", "Poem (meditative and topographical, in long and short unrhymed lines)",
  "significant",
  genres=G("Lyric Poetry", "Pastoral and Rural Poetry"),
  themes=T("Land, place and regional belonging", "Faith, doubt and the sacred", "Love, intimacy and loss"),
  overview="A poem by W. H. Auden, written on Ischia in May 1948, the first he wrote in Italy, and published in Horizon in "
           "July 1948 before its collection in Nones (1951). A meditation on the Mediterranean limestone landscape as "
           "the one human landscape, it is regarded as central to his canon and one of his finest poems.",
  content="A description of a limestone landscape and of the people it forms, set against the granite, clay and ocean "
          "that tempt saints, tyrants and romantic solitaries, and ending in a vision of faultless love and the life to "
          "come as a limestone landscape.",
  summary="If there is one landscape that 'we, the inconstant ones' are consistently homesick for, the poem begins, it is "
          "because limestone dissolves in water: its rounded hills, caves, springs and short distances shape a people "
          "who are local, sensual, quarrelsome and unable to imagine a god of rage. The best and worst never stayed "
          "there long but sought immoderate soils: granite wastes for the saints-to-be, clays and gravels for the "
          "would-be tyrants, who left slamming the door, and the oceanic whisper for the really reckless: 'I am the "
          "solitude that asks and promises nothing'. The speaker admits that the landscape seems historically "
          "unimportant, and that the poet, admired for calling the sun the sun, is made uneasy by it. Yet it makes a "
          "further point: in a world where sins can be forgiven and bodies rise from the dead, the blessed will not care "
          "from what angle they are seen, having nothing to hide. Dear, he ends, I know nothing of either, but when I "
          "try to imagine a faultless love or the life to come, what I hear is the murmur of underground streams, what I "
          "see is a limestone landscape.",
  themes_text="The landscape is read as an allegory of Mediterranean civilisation, set against the Protestant, rationalist "
              "'Gothic North', and, by Edward Mendelson and others, as an allegory of the human body, at the human "
              "scale and indifferent to great events. The poem rejects abstraction and the will to be little gods, and "
              "justifies the ordinary and the bodily in theological terms, with an erotic warmth addressed to 'Dear'.",
  structure="A single long verse paragraph moving from description through the catalogue of other soils and the poet's "
            "unease to the theological turn and the closing confession.",
  style="Conversational, discursive and witty, with long sentences and a relaxed, unrhymed line; a mixture of plain "
        "speech and theological vocabulary.",
  ctx="Auden, who had moved to the United States in 1939 and returned to Christianity, spent the spring and summer of 1948 "
      "on Ischia with Chester Kallman; the poem opens the Italian phase of his work. He revised it from 1958 and gave it a "
      "prominent place in Collected Shorter Poems, 1922-1957 (1966).",
  sig="Called sui generis and even the first postmodern pastoral, it is one of the most studied of Auden's later poems "
      "and a central text for his post-war turn to the body, the ordinary and Christian belief.",
  crit="Anthony Hecht wrote a whole essay on it (1979); Rebecca Price Parkin, Alan W. France, Rainer Emig and Hugh "
       "Underhill have read it variously as a facsimile of immediacy, as a contrast of Mediterranean South and Gothic "
       "North, and as an erotics of the ground.",
  canon="Secondary canon",
  biblio="First published in Horizon (July 1948); collected in Nones (1951); revised version from 1958. A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 683.",
  notes="The poem's metre (Auden wrote it in syllabic lines) is general knowledge, not checked against a consulted source; "
        "the form field therefore describes the lines only as long and short. Which version Norton prints was not "
        "checked.",
  comp=("1948", "1948"), ver="partially verified", sources=[W_LIME, NAEL]),
W10("The Shield of Achilles", WHA, "1952", "Poem (two alternating stanza forms, one in rhyme royal)", "significant",
  genres=G("Lyric Poetry", "Political Poetry", "Formal Verse"),
  themes=T("War, combat and its aftermath", "Power, the state and surveillance", "Violence, crime and justice"),
  overview="A poem by W. H. Auden, first published in 1952 and the title poem of his collection The Shield of Achilles "
           "(1955), which won the National Book Award for Poetry in 1956. It rewrites Homer's description of the shield "
           "of Achilles in the Iliad: Thetis looks for scenes of peace and plenty and finds the barren, impersonal "
           "violence of the modern world.",
  content="Thetis watches Hephaestus making the shield for her son; the scenes she expects and the scenes he makes: a "
          "faceless army, an execution watched by a passive crowd, a ragged urchin in a vacant field; her dismay.",
  summary="Thetis looks over Hephaestus's shoulder for vines and olive trees, marble cities and ships on untamed seas, but "
          "on the shining metal he has put an artificial wilderness under a sky like lead. An unintelligible multitude, "
          "a million eyes and boots in line, waits on a featureless plain while a voice without a face proves by "
          "statistics that some cause was just; they march away enduring a belief whose logic brings them somewhere else "
          "to grief. She looks for ritual pieties, white flower-garlanded heifers and libation, and sees instead a "
          "barbed-wire enclosure where bored officials lounge and sentries sweat, while a crowd of ordinary decent folk "
          "watch three pale figures led forth and bound to posts, unable to hope for help. She looks for athletes at "
          "their games and dancers moving to music, and sees a weed-choked field where a ragged urchin, aimless and "
          "alone, throws a stone at a bird; he takes for granted that girls are raped and that two boys knife a third, "
          "and has never heard of any world where promises are kept or one could weep because another wept. The "
          "thin-lipped armourer limps away, and Thetis cries out in dismay at what the god has made to please her son, "
          "the strong, iron-hearted, man-slaying Achilles, who would not live long.",
  themes_text="Against Homer's world, where even in war the imagination ran to scenes of peace, Auden sets a modern world "
              "of mass obedience, statistics and bureaucratic killing, of spectators who do nothing and of children "
              "for whom violence is normal. The execution of the three figures recalls the Crucifixion; the poem is an "
              "indictment of the totalitarian age and of the banality of violence.",
  structure="Short-lined eight-line stanzas, giving what Thetis looks for, alternate with seven-line stanzas of longer "
            "lines in rhyme royal (ababbcc), describing what Hephaestus makes; a final short-lined stanza gives Thetis's "
            "cry.",
  style="The lyric, ballad-like short stanzas contrast with the grave, documentary long stanzas; flat, abstract diction "
        "for the modern scenes, sensuous imagery for the Homeric ones.",
  ctx="Written in the aftermath of the Second World War, the camps and the show trials, and published in the first years "
      "of the Cold War; the 1955 collection gathers poems of about 1951-1954, including the sequences Bucolics and "
      "Horae Canonicae.",
  sig="One of Auden's best-known poems and a classic modern ekphrasis, widely anthologised as a poem about war and "
      "atrocity; the collection it names won the National Book Award.",
  canon="Secondary canon",
  biblio="First published in 1952 (the periodical was not identified in the sources consulted); the title poem of The "
         "Shield of Achilles (London: Faber and Faber, 1955). A selection of The Norton Anthology of English Literature, "
         "11th edition, vol. F, beginning on page 685.",
  notes="Wikipedia cites John Fuller's commentary and Mendelson's Later Auden in general and Rick Brown's essay on the "
        "banality of violence; none was consulted. The Crucifixion reading is a common one, stated here from the text.",
  ver="partially verified", sources=[W_SHIELD, NAEL]),
W10("The Children of the Poor", GB, "1949", "Sonnet sequence (in 'The Womanhood', the last part of Annie Allen)", "minor",
  genres=G("Sonnet", "Formal Verse", "Social Poetry"),
  themes=T("Family, marriage and domestic life", "Class, labour and social mobility", "Race, racism and the struggle for civil rights"),
  movements=M(PROTEST),
  overview="A sequence of sonnets by Gwendolyn Brooks that opens 'The Womanhood', the final part of Annie Allen (1949), "
           "the book that made her the first African American to win the Pulitzer Prize. A mother asks what she can give "
           "her children, who are poor and black, to carry them through the world.",
  content="A mother's meditation, in sonnets, on what she can give her poor children, on whether to teach them to pray, "
          "and on what they must do to survive.",
  summary="The sonnets speak as a mother. In the best-known, she asks what she can give her children, who are poor, "
          "'adjudged the leastwise of the land', her 'sweetest lepers', who demand no luxuries but have begged her for "
          "a firm shape, crying that they are unfinished, made by a hand less than sure. Her hand is full of mode, "
          "design and device, but she lacks access to her proper stone, and no plan, grief or love will be enough to "
          "ratify her little halves as they cross an autumn freezing everywhere. Other sonnets ask whether she should "
          "teach them to pray, and urge that they first fight, then fiddle.",
  themes_text="The limits of a mother's power against poverty and racism, and the place of art, faith and resistance in "
              "raising children who are 'contraband' in their own country.",
  structure="Petrarchan and Shakespearean sonnets, compressed and syntactically intricate, in the sequence that begins "
            "the volume's final part.",
  style="Dense, Latinate diction and inversions ('My hand is stuffed with mode, design, device') set against plain "
        "speech; the formal sonnet bent to a mother's anger and tenderness.",
  ctx="Annie Allen, published by Harper and Brothers on 1 October 1949, follows its heroine from girlhood through the mock "
      "epic 'The Anniad' to 'The Womanhood', where she looks at a world she would like to change; it won Poetry's Eunice "
      "Tietjens Prize and the 1950 Pulitzer Prize.",
  sig="The sonnets are among Brooks's most admired formal achievements and a key text of mid-century African American "
      "poetry; Norton prints the sequence, or part of it, as its representation of Annie Allen.",
  canon="Minor canon",
  biblio="Published in Annie Allen (New York: Harper and Brothers, 1949), in 'The Womanhood'. A selection of The Norton "
         "Anthology of American Literature, vol. E (the Norton list gives 'The Womanhood: The Children of the Poor (II)'; "
         "no page numbers).",
  notes="The quotations and the content of the sonnets are stated from the text, not from a consulted source, and the "
        "number of sonnets Norton prints was not established. Recorded under 'The Children of the Poor', the sequence's "
        "title.",
  ver="partially verified", sources=[W_AA, NAAL]),
W10("We Real Cool", GB, "1960", "Poem (four rhymed couplets)", "significant",
  genres=G("Lyric Poetry", "Social Poetry"),
  themes=T("Childhood, adolescence and coming of age", "Counterculture, drugs and rebellion", "Death, illness and mourning"),
  movements=M(PROTEST),
  overview="A poem by Gwendolyn Brooks, written in 1959 and published in her third collection, The Bean Eaters (1960). In "
           "eight short lines, seven young pool players boast of the life they lead and arrive at its end, 'We / Die "
           "soon.' It is one of the most famous and most taught American poems of the century.",
  content="Under the heading 'The Pool Players. / Seven at the Golden Shovel', the players list what they do: leave "
          "school, lurk late, strike straight, sing sin, thin gin, jazz June, and die soon.",
  summary="The poem is spoken by seven pool players at a hall called the Golden Shovel. 'We real cool,' they begin, and in "
          "short boasts they say what they do: they left school, they lurk late, they strike straight, they sing sin and "
          "thin gin, they jazz June. Each line ends on 'We', so that every boast is carried over into the next line, "
          "until the last, which has no 'We' after it: 'We / Die soon.' The swagger collapses into the knowledge, or the "
          "fate, the boasting has concealed.",
  themes_text="Youth, rebellion and doom: the players defy school and the establishment, which Brooks said June "
              "represents, but their cool is fragile. Brooks said the 'we's should be spoken softly, as if the boys "
              "were questioning the validity of their existence; the poem is compassionate rather than censorious.",
  structure="Four couplets of three-word lines (after the two-line heading), with internal and end rhyme and the pronoun "
            "'We' placed at the end of each line but the last, so that the enjambment enacts the players' hesitation.",
  style="Monosyllabic, vernacular speech with the syncopation of jazz; alliteration ('strike straight', 'sing sin') and "
        "the dropped copula of Black English.",
  ctx="Brooks said the poem came from passing a pool hall full of boys in her Chicago neighbourhood and wondering how "
      "they felt about themselves. The Bean Eaters (1960) takes many of its subjects from the news of the civil rights "
      "years.",
  sig="Cited as one of the most celebrated examples of jazz poetry, it has been printed on broadsides, reprinted in "
      "textbooks, banned in places for 'jazz', and answered by later writers; Terrance Hayes's 'golden shovel' form "
      "takes its name from it.",
  canon="Secondary canon",
  biblio="Written in 1959; published in The Bean Eaters (New York: Harper, 1960), Brooks's third collection. A selection "
         "of The Norton Anthology of American Literature, vol. E (no page numbers).",
  notes="Brooks's comments come from her 1970 interview with George Stavros in Contemporary Literature and a recorded "
        "reading, as reported by Wikipedia; neither was consulted directly. The publisher's name is general knowledge.",
  comp=("1959", "1959"), ver="partially verified", sources=[W_WRC, NAAL]),
W10("The Bean Eaters", GB, "1960", "Poem (three short stanzas)", "minor",
  genres=G("Lyric Poetry", "Social Poetry"),
  themes=T("Family, marriage and domestic life", "Class, labour and social mobility", "Death, illness and mourning"),
  movements=M(PROTEST),
  overview="The title poem of Gwendolyn Brooks's third collection, The Bean Eaters (1960): an old couple eat their dinner "
           "of beans in a rented back room crowded with the keepsakes of their life.",
  content="An elderly couple at a plain meal; their routine of dressing and tidying; their memories, stirred by the "
          "objects that fill their room.",
  summary="'They eat beans mostly, this old yellow pair.' Dinner is a casual affair of plain chipware, creaking wood and "
          "tin flatware. They are two who are 'Mostly Good', two who have lived their day but keep on putting on their "
          "clothes and putting things away, and remembering, with twinklings and twinges, as they lean over the beans "
          "in their rented back room full of beads and receipts and dolls and cloths, tobacco crumbs, vases and fringes.",
  themes_text="Poverty and old age, the dignity of routine, and memory, presented with sympathy and without sentiment; "
              "critics have read the couple's colour and circumstances as a comment on race and class.",
  structure="Three brief stanzas of irregular line length and loose rhyme, ending in a long catalogue line.",
  style="Plain description with ironic touches ('Dinner is a casual affair') and the closing list of objects, which "
        "holds the couple's past.",
  ctx="The Bean Eaters (1960) is the collection in which Brooks turned increasingly to the lives of poor Chicagoans and "
      "to the public events of the civil rights years.",
  sig="One of Brooks's most anthologised short poems; Gale's Poetry for Students gives it an entry of its own.",
  canon="Minor canon",
  biblio="The title poem of The Bean Eaters (New York: Harper, 1960). A selection of The Norton Anthology of American "
         "Literature, vol. E (no page numbers).",
  notes="Text and readings from Gale's Poetry for Students entry, which cites Norris B. Clark's essay in A Life "
        "Distilled (1987) for a reading of the poem as primarily about race.",
  ver="partially verified", sources=[GALE_BE, NAAL]),
W10("A Bronzeville Mother Loiters in Mississippi. Meanwhile, a Mississippi Mother Burns Bacon", GB, "1960",
  "Poem (long narrative and dramatic poem in free verse)", "significant",
  genres=G("Narrative Poetry", "Political Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Violence, crime and justice", "Family, marriage and domestic life"),
  movements=M(PROTEST),
  alt=["A Bronzeville Mother Loiters in Mississippi"],
  overview="A long poem by Gwendolyn Brooks on the murder of Emmett Till, published in The Bean Eaters (1960). It is told "
           "through the consciousness of a white woman modelled on Carolyn Bryant, whose husband was one of the men "
           "accused of killing the fourteen-year-old Chicago boy in Mississippi in 1955, as she makes breakfast in her "
           "kitchen after the acquittal.",
  content="The young wife's reflections on the ballad she had imagined herself in, on the 'Dark Villain' who turned out "
          "to be a child, on her husband and her own children, and on the boy's mother; her growing revulsion from her "
          "husband.",
  summary="From childhood the woman has imagined life as a ballad, with herself as the milk-white maid, a Dark Villain and "
          "a Fine Prince who rescues her. Now, in her kitchen, burning the bacon as she makes breakfast after the trial, "
          "she finds the story will not fit: the villain was a child of fourteen, his eyes and his mother's grief haunt "
          "her, and the prince is her husband, who has killed and been acquitted. When he slaps one of their small "
          "children across the face, the blood she has been imagining seems to rise in the room, and as he embraces "
          "her she can think only of the killing. She does not scream, but a hatred for him bursts into glorious "
          "flower, bigger than all magnolias. The poem ends by pointing to the last bleak news of the ballad: 'The "
          "last quatrain.'",
  themes_text="The poem exposes the racial and sexual myths, the ballad of white womanhood threatened and avenged, that "
              "justified lynching, and shows the white wife's complicity breaking under the recognition of what was "
              "done in her name. Setting the poem in a kitchen makes racialised violence part of everyday domestic life; "
              "images of red and seeping blood bind it to its companion poem about Till's mother.",
  structure="Long free-verse paragraphs of varying line length following the woman's thoughts through a single morning, "
            "with the ballad as a frame she keeps testing; the title's full stop divides it into two headline-like "
            "sentences, and the last line hands over to 'The Last Quatrain of the Ballad of Emmett Till'.",
  style="Interior monologue in the third person, mixing fairy-tale and ballad diction with domestic realism and "
        "newspaper fact; recurrent imagery of red, blood and magnolias.",
  ctx="Emmett Till, a black Chicago teenager visiting relatives, was murdered in August 1955 after being accused of "
      "whistling at Carolyn Bryant; his mother's open-casket funeral and the acquittal of the killers made the case a "
      "catalyst of the civil rights movement. Brooks, a mother in Chicago, published the poem five years later.",
  sig="Brooks's most ambitious poem in The Bean Eaters and one of the major literary responses to the Till case, "
      "unusual in imagining it through the white wife.",
  crit="A scholarly article on Brooks's poetic response to the lynching reads the pair of poems as a study of Carolyn "
       "Bryant's consciousness and of Mamie Bradley's grief, both set in the kitchen and joined by images of blood; "
       "encyclopedias of motherhood and the National Portrait Gallery present them as Brooks's moving meditations on "
       "the aftermath of the murder.",
  canon="Secondary canon",
  biblio="Published in The Bean Eaters (New York: Harper, 1960). A selection of The Norton Anthology of American "
         "Literature, vol. E (no page numbers).",
  notes="The plot is stated from the text; the reading of the woman as Carolyn Bryant comes from the ResearchGate abstract "
        "and the SAGE encyclopedia entry. The facts of the Till case are general knowledge.",
  ver="partially verified", sources=[RG_TILL, SAGE_GB, NPG_GB, NAAL]),
W10("The Last Quatrain of the Ballad of Emmett Till", GB, "1960", "Poem (short free-verse lyric)", "minor",
  genres=G("Lyric Poetry", "Political Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "Death, illness and mourning", "Family, marriage and domestic life"),
  movements=M(PROTEST),
  overview="A short poem by Gwendolyn Brooks that follows 'A Bronzeville Mother Loiters in Mississippi' in The Bean Eaters "
           "(1960) and completes its ballad: Emmett Till's mother, after the murder and the burial, alone in a red room.",
  content="Till's mother in Chicago after her son's funeral: her appearance, her red room, her black coffee, her kiss for "
          "her killed boy, and the chaos of the landscape.",
  summary="Subtitled 'after the murder, after the burial', the poem shows Emmett's mother, a pretty-faced woman the tint "
          "of pulled taffy, sitting in a red room drinking black coffee. She kisses her killed boy, and she is sorry. "
          "The poem closes on chaos in windy grays through a red prairie.",
  themes_text="Grief reduced to its barest gestures, and the private mourning that answers the public ballad of the "
              "companion poem; red binds the room, the prairie and the blood of the murder.",
  structure="A handful of very short lines, presented as the 'last quatrain' that the preceding poem announces.",
  style="Understated, almost flat statement ('And she is sorry') and a closing image of colour and weather.",
  ctx="Mamie Till Bradley's insistence on an open casket made her son's murder in 1955 a national cause; Brooks, writing "
      "from Chicago, gives her the last word of the pair of poems.",
  sig="Paired with 'A Bronzeville Mother' as Brooks's response to the Till case, it is among her most frequently "
      "anthologised short poems.",
  canon="Minor canon",
  biblio="Published in The Bean Eaters (New York: Harper, 1960). A selection of The Norton Anthology of American "
         "Literature, vol. E (no page numbers).",
  notes="The quoted phrases are stated from the text.",
  ver="partially verified", sources=[RG_TILL, NPG_GB, NAAL]),
W10("The Blackstone Rangers", GB, "1968", "Poem (sequence in three parts)", "minor",
  genres=G("Political Poetry", "Social Poetry", "Black Arts Poetry"),
  themes=T("Race, racism and the struggle for civil rights", "The city, the suburb and modern space", "Violence, crime and justice"),
  movements=M(BAM),
  overview="A poem in three parts by Gwendolyn Brooks on the Blackstone Rangers, a Chicago street gang, published in In the "
           "Mecca (1968), the book of her turn towards the Black Arts Movement.",
  content="The gang as seen by those who would discipline it; its leaders; and a 'Rangerette', one of the gang girls.",
  summary="In 'As Seen by Disciplines' the Rangers are thirty at the corner, black, raw, ready, sores in the city that do "
          "not want to heal. 'The Leaders' names Jeff, Gene, Geronimo and Bop, who are hardly the dupes of downtown, "
          "hardly Belafonte, King or Malcolm X, and whose country is a nation on no map. 'Gang Girls' follows Mary Ann, "
          "a rose in a whiskey glass, whose year passes in the narrow world of the gang, save for her love.",
  themes_text="The poem refuses the official view of the gang as a social disease and imagines its members from inside, "
              "as a self-made nation and as young people with longings of their own; it reflects Brooks's new "
              "commitment to the black community after 1967.",
  structure="Three titled sections of different length and manner, moving from the outside view to the leaders and "
            "then to a single girl.",
  style="Compressed, inventive diction and wordplay ('They cancel, cure and curry'), mixing street names and lyrical "
        "figures; freer forms than her earlier work.",
  ctx="In the Mecca (Harper and Row, 1968), Brooks's first new collection in nearly ten years, pairs its long title poem "
      "with shorter poems on contemporary figures and events, among them Medgar Evers, Malcolm X, the Chicago Picasso, "
      "the Wall mural and the Blackstone Rangers.",
  sig="A key poem of Brooks's late-1960s transformation and of the Black Arts era's attention to the black city.",
  canon="Minor canon",
  biblio="Published in In the Mecca (New York: Harper and Row, 1968), in three parts: I. As Seen by Disciplines; II. The "
         "Leaders; III. Gang Girls. A selection of The Norton Anthology of American Literature, vol. E (no page numbers).",
  notes="The quotations are stated from the text. Brooks's writing workshop of 1967, which drew in young members of the "
        "gang, is general knowledge, not checked.",
  ver="partially verified", sources=[PENN_MECCA, NAAL]),
W10("To the Diaspora", GB, "1981", "Poem (free verse)", "minor",
  genres=G("Lyric Poetry", "Black Arts Poetry"),
  themes=T("Migration, exile and diaspora", "Identity, authenticity and the divided self", "Race, racism and the struggle for civil rights"),
  movements=M(BAM),
  overview="A poem by Gwendolyn Brooks in To Disembark (1981), published by Third World Press, subtitled 'you did not know "
           "you were Afrika': an address to black people of the diaspora on a journey towards Africa that turns out to "
           "be a journey into themselves.",
  content="An address to 'you', who set out for Africa without knowing that the black continent to be reached was "
          "yourself; the speaker's earlier, disbelieved prophecy; a call to the hard work still to be done.",
  summary="When you set out for Afrika, the speaker tells the diaspora, you did not know you were going, because you did "
          "not know you were Afrika, that the black continent that had to be reached was you. The speaker could not have "
          "told you then that some sun would come, evoking the diamonds of you; you would not have believed it, and when "
          "told you smiled and thanked her but hardly believed. Here is some sun, the poem says, and now off into the "
          "places rough to reach: your work, that was done, to be done to be done to be done.",
  themes_text="Black identity and self-discovery: Africa is found within rather than abroad, and pride is the beginning "
              "of a labour that never ends.",
  structure="Free-verse paragraphs addressed to 'you', moving from the journey to the speaker's prophecy and to the "
            "repeated, open-ended last line.",
  style="Direct address, the spelling 'Afrika', repetition and incantation in the closing line.",
  ctx="After 1967 Brooks left Harper and published with black presses such as Broadside Press and Third World Press; To "
      "Disembark gathers poems of this period.",
  sig="A representative late poem of Brooks's Black Arts commitment, and the latest of her poems that Norton prints.",
  canon="Minor canon",
  biblio="Published in To Disembark (Chicago: Third World Press, 1981). A selection of The Norton Anthology of American "
         "Literature, vol. E (no page numbers).",
  notes="The paraphrase is stated from the text. Brooks's move to black presses is general knowledge, not checked.",
  ver="partially verified", sources=[BBP_DIAS, NAAL]),
]
