"""Installment 10, wave 19: Norton's order resumed after the climate-change section - Margaret Atwood,
J. M. Coetzee and Eavan Boland (Atwood and Coetzee each recorded once, for the whole book an excerpt
comes from; Boland's three poems recorded separately).

All three authors are new to the database. Nothing beyond the Norton selections is recorded.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL  # noqa: E402

MA = "Margaret Atwood"
JC = "J. M. Coetzee"
EB = "Eavan Boland"
CANLIT = "Canadian Literary Nationalism"
SAAP = "South African Writing under Apartheid"
POSTCOL = "Postcolonial Literature"
NIP = "Northern Irish Poetry and the Belfast Group"

W_MA = "Margaret Atwood (Wikipedia)"
W_WB = "Waiting for the Barbarians (Wikipedia)"
W_JC = "J. M. Coetzee (Wikipedia)"
W_EB = "Eavan Boland (Wikipedia)"
BOL_MSU = "Eavan Boland, 'The Dolls Museum in Dublin' (course page, Michigan State University)"
BOL_POSTID = ("'Chronicles of Impeded Growth: Eavan Boland and the Reconstruction of Identity' "
              "(Post Identity, University of Michigan)")
BOL_LOST = "Eavan Boland, 'The Lost Land' (Poetry Foundation)"
ATW_EBSCO = "EBSCO Research Starters, 'Death by Landscape' by Margaret Atwood"
ATW_CRIMSON = "Atwood's Poetry Focuses on a Home (review of Morning in the Burned House, The Harvard Crimson)"
ATW_SPLIT = "Tina Burchette, 'The Split Self in Atwood's Miss July Grows Older' (Margaret Atwood Studies 8, 2014)"

AUTHORS = [
A10(MA, MAJ, "1939", None, "Ottawa, Ontario, Canada",
  "Canadian; poet, novelist, short-story writer and critic writing in English",
  "Canadian poet and novelist whose speculative fictions of gender, power and survival, from The Handmaid's "
  "Tale to the MaddAddam trilogy, have made her the most widely read Canadian writer of her generation",
  "Margaret Eleanor Atwood was born in Ottawa on 18 November 1939, the daughter of a forest entomologist, and "
  "spent much of her childhood in the bush of northern Quebec and Ontario, an experience that underlies the "
  "wilderness settings of much of her work. She took her BA at the University of Toronto in 1961 and her MA at "
  "Radcliffe College in 1962, and began publishing poetry while still a student: Double Persephone (1961), The "
  "Circle Game (1964, Governor General's Award) and The Animals in That Country (1968). Her first novel, The "
  "Edible Woman (1969), was followed by Surfacing (1972), Lady Oracle (1976), Life Before Man (1979), Bodily "
  "Harm (1981) and The Handmaid's Tale (1985), which won the Governor General's Award and became her best-known "
  "book; Cat's Eye (1988), The Robber Bride (1993), Alias Grace (1996, Booker shortlist), The Blind Assassin "
  "(2000, Booker Prize), Oryx and Crake (2003), The Year of the Flood (2009) and MaddAddam (2013) followed, with "
  "the poetry collections Procedures for Underground (1970), Power Politics (1971), You Are Happy (1974), Two-"
  "Headed Poems (1978), True Stories (1981), Interlunar (1984), Morning in the Burned House (1995) and The Door "
  "(2007). She has taught at the University of British Columbia, York University and elsewhere, was president of "
  "the Writers' Union of Canada and of PEN Canada, and lives in Toronto.",
  "Fiction: The Edible Woman (1969), Surfacing (1972), Lady Oracle (1976), Life Before Man (1979), Bodily Harm "
  "(1981), The Handmaid's Tale (1985), Cat's Eye (1988), The Robber Bride (1993), Alias Grace (1996), The Blind "
  "Assassin (2000), Oryx and Crake (2003), The Penelopiad (2005), The Year of the Flood (2009), MaddAddam "
  "(2013), Hag-Seed (2016) and The Testaments (2019). Stories: Dancing Girls (1977), Bluebeard's Egg (1983), "
  "Wilderness Tips (1991), Good Bones (1992), Moral Disorder (2006) and Stone Mattress (2014). Poetry: Double "
  "Persephone (1961), The Circle Game (1964), The Animals in That Country (1968), Procedures for Underground "
  "(1970), Power Politics (1971), You Are Happy (1974), Two-Headed Poems (1978), True Stories (1981), "
  "Interlunar (1984), Selected Poems II (1986), Morning in the Burned House (1995), Eating Fire (1998) and The "
  "Door (2007). Criticism: Survival (1972), Second Words (1982), Strange Things (1995) and Negotiating with the "
  "Dead (2002).",
  "A lucid, ironic, syntactically exact prose and a poetry of sharp declarative statement, unsettling "
  "personification and buried myth; a taste for the Gothic, for doubled and split selves and for the "
  "documentary roughness of found documents, letters and newspaper reports; the wilderness and the city "
  "juxtaposed, and a cool surface over considerable anger.",
  "The politics of gender and the body; Canadian national identity and the colonial mentality; wilderness, "
  "nature and the violence of settlement; survival as a national and personal theme; storytelling, memory and "
  "the unreliability of narrative; dystopia, environmental catastrophe and speculative futures; myth, fairy "
  "tale and classical allusion reworked from a woman's point of view.",
  "Atwood is the most widely read and most frequently taught Canadian writer of her generation, and one of the "
  "few poets to have become a public intellectual of global standing; The Handmaid's Tale has become a "
  "touchstone for the politics of gender and authoritarianism, and the dystopian novels of the 2000s extended "
  "her reach. Her criticism, above all Survival, shaped the terms in which Canadian literature was discussed.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Atwood, read directly, and from general "
           "knowledge; the short-story, poetry and criticism lists were not checked against a bibliography. "
           "Installment 10 records only the two Norton selections, 'Death by Landscape' (Wilderness Tips, 1991) "
           "and 'Miss July Grows Older' (Morning in the Burned House, 1995); the novels and the other "
           "collections have no records, so the bibliography is incomplete.",
  ver="partially verified", sources=[W_MA, ATW_EBSCO, NAEL]),
A10(JC, MAJ, "1940", None, "Cape Town, South Africa",
  "South African and Australian; novelist, essayist, translator and critic writing in English",
  "South African-born novelist and Nobel laureate whose spare, allegorical fictions of colonialism, torture "
  "and the limits of the novel, from Dusklands to Disgrace, made him the most discussed South African writer of "
  "his time",
  "John Maxwell Coetzee was born in Cape Town on 9 February 1940. He studied mathematics and English at the "
  "University of Cape Town, took a doctorate at the University of Texas at Austin in 1969, and taught at the "
  "State University of New York at Buffalo, the University of Cape Town and the University of Chicago before "
  "moving to Australia in 2002; he became an Australian citizen in 2006 and lives in Adelaide. His first book, "
  "the two novellas of Dusklands, appeared in 1974; In the Heart of the Country (1977), Waiting for the "
  "Barbarians (1980), Life & Times of Michael K (1983, Booker Prize), Foe (1986), Age of Iron (1990), The "
  "Master of Petersburg (1994), Disgrace (1999, Booker Prize and the first novel to win it twice), Elizabeth "
  "Costello (2003), Slow Man (2005), Diary of a Bad Year (2007), The Childhood of Jesus (2013) and The Pole "
  "(2023) followed, with the fictionalised memoirs Boyhood (1997), Youth (2002) and Summertime (2009) and the "
  "essay collections White Writing (1988), Doubling the Point (1992), Giving Offense (1996), Stranger Shores "
  "(2001), Inner Workings (2007) and Late Essays (2017). He was awarded the Nobel Prize in Literature in 2003.",
  "Fiction: Dusklands (1974), In the Heart of the Country (1977), Waiting for the Barbarians (1980), Life & "
  "Times of Michael K (1983), Foe (1986), Age of Iron (1990), The Master of Petersburg (1994), Disgrace (1999), "
  "Elizabeth Costello (2003), Slow Man (2005), Diary of a Bad Year (2007), The Childhood of Jesus (2013), The "
  "Schoo lteacher (2016), The Death of Jesus (2019) and The Pole (2023). Memoir: Boyhood (1997), Youth (2002) "
  "and Summertime (2009). Essays and criticism: White Writing (1988), Doubling the Point (1992), Giving Offense "
  "(1996), The Lives of Animals (1999), Stranger Shores (2001), Inner Workings (2007), Here and Now (2013, "
  "with Paul Auster) and Late Essays (2017). Translations of Dutch and Afrikaans writing.",
  "A plain, exact, rigorously unadorned prose, with a first-person narrator who reports and withholds in equal "
  "measure; short sentences, little metaphor, an avoidance of psychological explanation; allegory and "
  "allegorical geography; free indirect style used to lay bare the mind of a compromised official.",
  "Colonialism, empire and the frontier; torture, complicity and the banality of state violence; the ethics of "
  "writing and the authority of the novel; animals, ecology and the limits of sympathy; South African history, "
  "apartheid and its aftermath; old age, disgrace and the body.",
  "Coetzee is the most honoured South African writer since Nadine Gordimer and one of the very few to have won "
  "the Booker Prize twice; his novels are central to the study of colonial and postcolonial fiction, and his "
  "essays and lectures - above all 'The Lives of Animals' and the Elizabeth Costello fictions - have made him "
  "an important voice in the debate on animal rights and on the ethics of representation.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Coetzee, read directly, and from the "
           "Wikipedia article on Waiting for the Barbarians; they were not checked against a bibliography. "
           "Installment 10 records only the Norton selection, Waiting for the Barbarians (1980), printed as the "
           "extract 'From Waiting for the Barbarians'; the other novels and the essays have no records, so the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_JC, W_WB, NAEL]),
A10(EB, SEC, "1944", "2020", "Dublin, Ireland",
  "Irish; poet, critic and teacher writing in English",
  "Irish poet and critic who made the domestic life of women in the suburbs a subject of Irish poetry, and "
  "whose later work brought the silence of women into the national history",
  "Eavan Aisling Boland was born in Dublin on 24 September 1944, the daughter of the diplomat Frederick Boland "
  "and the painter Frances Kelly. Her father's postings took the family to London in 1950, where she met the "
  "anti-Irish hostility she later recorded in 'An Irish Childhood in England: 1951', and then to New York; she "
  "returned to Dublin at fourteen to attend the Holy Child School, Killiney, and read English at Trinity College "
  "Dublin, graduating in 1966. Her first pamphlet, 23 Poems, appeared in 1962; New Territory (1967), The War "
  "Horse (1975), In Her Own Image (1980), Night Feed (1982), The Journey (1987), Outside History (1990), In a "
  "Time of Violence (1994), The Lost Land (1998), Code (2001), Against Love Poetry (2001) and Domestic Violence "
  "(2007) followed, with the prose study Object Lessons (1995) and A Journey with Two Maps (2011). She taught "
  "at Stanford University from 1996 and was a regular reviewer and broadcaster; she died in Dublin on 27 April "
  "2020.",
  "Poetry: 23 Poems (1962), New Territory (1967), The War Horse (1975), In Her Own Image (1980), Night Feed "
  "(1982), The Journey (1987), Selected Poems (1989), Outside History (1990), In a Time of Violence (1994), The "
  "Lost Land (1998), Code (2001), Against Love Poetry (2001), Domestic Violence (2007), New Collected Poems "
  "(2008) and The Historians (2020). Prose: Object Lessons: The Life of the Woman and the Poet in Our Time "
  "(1995) and A Journey with Two Maps: Becoming a Woman Poet (2011).",
  "Conversational, plain and exact free verse, with short lines and unemphatic enjambment; a rhetoric of "
  "questions and direct address; the lyric 'I' placed in kitchens, gardens, hospitals and suburban streets; "
  "later poems built of compressed, epigrammatic stanzas and of a deliberately bare diction that refuses the "
  "ornament of the Irish poetic tradition.",
  "The lives of women in the Irish suburbs, marriage, motherhood and domestic work; the silence of women in "
  "official Irish history and in the literary tradition; the Famine, the emigrant ship and the ''hidden' past; "
  "language and naming, especially the English of the colonised; a woman poet's relation to the Irish poetic "
  "inheritance from Yeats and the Revival.",
  "Boland is the central Irish woman poet of her generation and one of the most influential poets in Ireland in "
  "the last fifty years; her insistence that the domestic and the suburban were proper subjects for Irish "
  "poetry changed the terms of the tradition, and her work as editor, teacher and critic (Object Lessons) "
  "helped make the case for a woman's tradition in Irish writing.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Boland, read directly, from the "
           "contents listing of New Collected Poems in a library catalogue, and from general knowledge; they "
           "were not checked against a bibliography. Installment 10 records only the three Norton selections, "
           "'Fond Memory' (The Journey, 1987), 'The Dolls Museum in Dublin' (In a Time of Violence, 1994) and "
           "'The Lost Land' (The Lost Land, 1998); the other collections have no records, so the bibliography "
           "is incomplete.",
  ver="partially verified", sources=[W_EB, BOL_MSU, BOL_POSTID, BOL_LOST, NAEL]),
]

WORKS = [
W10("Death by Landscape", MA, "1991", "Short story", "significant",
  genres=G("Short Story", "Domestic Fiction", "Regional Fiction"),
  themes=T("Childhood, adolescence and coming of age", "Memory, trauma and testimony", "Nature, ecology and environmental crisis"),
  movements=M(CANLIT),
  overview="A story from Atwood's Wilderness Tips (1991): Lois, widowed and living in Toronto, looks at her "
           "collection of Canadian landscape paintings and remembers the summer at Camp Manitou when her friend "
           "Lucy disappeared from a cliff above the lake.",
  content="A story in two times: the elderly Lois in her waterfront apartment among her Group of Seven "
          "landscapes, and the thirteen-year-old Lois at a girls' summer camp in northern Ontario, where a "
          "canoe trip ends with her friend's disappearance and a lifetime of unexplained guilt.",
  summary="Lois, now widowed and living alone in a Toronto condominium overlooking Lake Ontario, has filled her "
          "walls with Canadian landscape paintings - 'every one of them is a picture of Lucy', as the story's "
          "last line puts it. The story moves back to her summers at Camp Manitou, a girls' camp in the "
          "northern Ontario bush, where she was sent from the age of nine and where she became friends with "
          "Lucy, a girl from Chicago whose parents were divorcing and who was, by their last summer, moody and "
          "restless. On a canoe trip into the interior the two girls climb a trail to a lookout above the lake; "
          "Lucy steps off the path to relieve herself and does not come back. Lois hears a scream - or thinks "
          "she hears one - and raises the alarm, but no trace of Lucy is ever found. The camp director's "
          "insinuation that Lois may have pushed her, the police search, and the return to a camp where the "
          "girls' bunk is rearranged so that no one has to sleep in Lucy's bed are the story's aftermath. In "
          "the present, Lois has spent her life living 'two lives', she says, one of them the life in which Lucy "
          "went on existing somewhere in the landscape; and the paintings, which she has bought without quite "
          "knowing why, become the place where the lost girl is kept.",
  themes_text="The story is about the wilderness as an idea rather than a place: the camp domesticates it with "
              "songs, canoes and schedules, while the real bush beyond the portages is indifferent and "
              "bottomless, and Lucy's disappearance is the point at which the two meet. Atwood uses the "
              "Canadian landscape tradition - the Group of Seven paintings Lois collects - as a critique: the "
              "paintings turn the wilderness into property and scenery, and yet they are also the only place "
              "where Lois can put her grief. Guilt, memory and the unreliability of witness run through the "
              "story, which never settles whether Lucy fell, was taken, or chose to vanish.",
  structure="A double narrative, moving without chapter breaks between the present of Lois's apartment and the "
            "remembered summers at Camp Manitou; the story is told in close third person, in the iterative "
            "present for the camp years and in a slower present for Lois's old age, and ends on a short "
            "declarative sentence that reverses the meaning of everything before it.",
  style="A cool, exact, deceptively flat prose with a journalist's eye for period detail (the camp songs, the "
        "wartime rationing, the girls' nicknames) and a poet's ear for the sentence as a unit of disclosure; "
        "the paintings are described in the language of art criticism, and the wilderness in the language of "
        "the camp brochure, so that neither is allowed to be innocent.",
  ctx="Wilderness Tips (McClelland and Stewart, 1991) gathers stories written in the late 1980s, several of "
      "them, like this one, about women revisiting the myths of Canadian childhood; the camp story belongs to "
      "the tradition of Canadian writing about the bush that runs from Susanna Moodie through Atwood's own "
      "Survival (1972) and her Moodie poems in The Journals of Susanna Moodie (1970).",
  sig="One of Atwood's most anthologised stories and a standard text in courses on Canadian literature, on the "
      "short story and on ecocriticism; it is her selection in the Norton Anthology alongside the poem 'Miss "
      "July Grows Older'.",
  canon="Secondary canon",
  biblio="Published in Wilderness Tips (Toronto: McClelland and Stewart, 1991; London: Bloomsbury, 1991). A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 1031. "
         "The Norton list does not print a date for it; it is dated here to the collection.",
  notes="The plot follows the EBSCO Research Starters entry on the story, read as a search extract, which agrees "
        "with other summaries on the camp, the cliff, the scream and the paintings; the text itself was not read "
        "complete, and the quotations are those printed in that entry and in the critical article cited for the "
        "poem.",
  ver="partially verified", sources=[ATW_EBSCO, W_MA, NAEL]),
W10("Miss July Grows Older", MA, "1995", "Poem", "significant",
  genres=G("Lyric Poetry", "Dramatic Monologue", "Confessional Poetry"),
  themes=T("Gender, feminism and women's lives", "Sexuality, desire and the closet", "Death, illness and mourning"),
  movements=M("Second-Wave Feminist Writing", CANLIT),
  overview="A poem from Morning in the Burned House (1995) in the voice of a calendar pin-up, Miss July, now "
           "grown old, who looks back on the body that was once her fortune.",
  content="A dramatic monologue of some forty lines in which the ageing Miss July reflects on beauty, the "
          "calendar, the men who once looked at her, and the way the sun now moves through the hours.",
  summary="Miss July - the girl on the July page of a nude calendar - speaks in the first person about her "
          "life since the photograph was taken. She remembers the body she had, and the power it gave her: 'I "
          "had a talent', she says in effect, and 'men were a skill'. She is unsentimental about her younger "
          "self, who was vain and not very intelligent, and unsentimental about the men who wanted her, whom "
          "she describes with a mixture of contempt and amusement. What has changed is not only her body but "
          "her relation to time: 'the way the sun moves through the hours becomes important', and the calendar "
          "has become a way of measuring what is left rather than what is on offer. The poem is neither a "
          "lament nor a joke. It gives the pin-up a mind and a voice, and lets her look steadily at the "
          "transaction she was once part of; by the end the reader is asked to see the ageing woman's "
          "self-knowledge as a form of power too, though a bleaker and lonelier one.",
  themes_text="Atwood takes the most stereotyped of female images - the calendar girl, whose only function is to "
              "be looked at - and gives her the position of the speaking subject. The poem is a critique of the "
              "commerce in female beauty, but it refuses to absolve its speaker: Miss July enjoyed her power "
              "and used it, and the poem's honesty about that is what makes it more than a polemic. Ageing and "
              "the body's betrayal are the second subject, and the poem's final turn towards the sun and the "
              "hours makes mortality itself the measure of value.",
  structure="A dramatic monologue in loose, short-lined free verse, without stanza divisions or an obvious "
            "rhyme scheme; the voice is colloquial and self-interrupting, and the poem moves by association "
            "from the calendar photograph to the young men, to the present body and to the passing of time.",
  style="Conversational, ironic and deliberately flat in places, with sudden lyrical turns; short lines and "
        "abrupt enjambments; a diction that mixes the demotic ('Don't get me wrong') with precise physical and "
        "temporal notation; the tone is that of a woman talking to herself in a room.",
  ctx="Morning in the Burned House (McClelland and Stewart, 1995) was Atwood's first collection of new poems for "
      "eight years and won the Trillium Award; its second section reworks female archetypes - Miss July, Helen "
      "of Troy and others - in monologues that draw on the feminist critique of the image and of the beauty "
      "myth developed in the 1970s and 1980s.",
  sig="One of the best known poems of Morning in the Burned House and a frequently taught example of the "
      "feminist dramatic monologue; it is Atwood's selection in the Norton Anthology alongside 'Death by "
      "Landscape'.",
  canon="Secondary canon",
  biblio="Published in Morning in the Burned House (Toronto: McClelland and Stewart, 1995; Boston: Houghton "
         "Mifflin, 1995). A selection of The Norton Anthology of English Literature, 11th edition, vol. F, "
         "beginning on page 1043.",
  notes="The poem was not read complete; the description follows the accounts in the Harvard Crimson review of "
        "the collection, the ProQuest article on the poem and the Oxford Research Encyclopedia chapter cited, "
        "which quote 'men were a skill' and 'the way the sun / moves through the hours becomes important'.",
  ver="partially verified", sources=[ATW_EBSCO, W_MA, ATW_CRIMSON, ATW_SPLIT, NAEL]),
]

WORKS += [
W10("Waiting for the Barbarians", JC, "1980", "Novel", "major",
  genres=G("Literary Novel", "Political Novel", "Philosophical Fiction"),
  themes=T("Power, the state and surveillance", "Decolonisation, the end of empire and the new nation",
           "Violence, crime and justice"),
  movements=M(SAAP, POSTCOL),
  overview="J. M. Coetzee's third novel (1980), the first-person testimony of an unnamed magistrate on a "
           "far frontier of an unnamed empire, who is broken by the state's security police for trying to "
           "return a tortured barbarian woman to her own people, and who learns in prison what the Empire's "
           "justice is.",
  content="A novel in six parts: the magistrate's settled frontier town; the arrival of Colonel Joll and the "
          "Third Bureau; the magistrate's care for the blinded barbarian girl and his expedition to return her; "
          "his arrest, imprisonment and torture; the collapse of the imperial campaign; and his return, "
          "unbroken in his own mind but stripped, to the ordinary life of the town.",
  summary="The novel is narrated by the magistrate of a small settlement on the frontier of the Empire, a man "
          "who has spent his working life administering a place where nothing much happens, collecting "
          "antiquities and sleeping with a local woman. The Empire declares a state of emergency and sends the "
          "Third Bureau, its security service, under Colonel Joll, who interrogates and tortures a group of "
          "captives on suspicion of being barbarians. Joll leaves, the frontier empties, and the magistrate "
          "takes in a young barbarian woman left crippled and half-blind by the torture; he washes her feet, "
          "sleeps beside her, and cannot say what he wants from her. He decides to return her to her people "
          "and sets out with two soldiers and a horse across the salt flats, a journey the novel describes "
          "with a physical exactness that becomes an allegory of the Empire's ignorance of the land it claims. "
          "Having handed her over, he comes back to find the Third Bureau in charge and is arrested for "
          "desertion and for consorting with the enemy; he is imprisoned in a cellar, beaten, hung by the "
          "arms, and reduced to begging for food. When the imperial campaign collapses and Joll returns with "
          "captives for a public spectacle of torture, the magistrate interrupts it and is beaten again. The "
          "soldiers leave; the barbarians never appear. The novel ends with the magistrate helping the "
          "townspeople repair the walls and clean up, while the question of what the Empire was defending, and "
          "what the magistrate was complicit in, is left open.",
  themes_text="The novel is an allegory of empire and torture, but its resistances are deliberate: the Empire, "
              "the barbarians and even the town are unnamed, the frontier could be South Africa, Latin America "
              "or anywhere, and the magistrate's goodness is as compromised as the state's violence - he enjoys "
              "his authority, he is complicit in the settlement and he cannot undo what Joll does. Coetzee's "
              "subject is the way in which a decent official becomes part of a machine of cruelty and is then "
              "punished by that machine; the barbarian girl's body, which he wants to read as a text from "
              "which a meaning can be extracted, is the novel's image of the limits of interpretation. The "
              "Empire's enemy is finally its own invention, and the novel's ending - the barbarians do not "
              "come - makes the point that the threat was always a pretext.",
  structure="Six chronological chapters, narrated in the first person by the magistrate as a retrospective "
            "confession and testimony; the narrative is deliberately unadorned, with short scenes and summary "
            "rather than dramatised interiority, and the allegory depends on the suppression of names and "
            "historical particulars.",
  style="A spare, grave, almost transparent prose; short declarative sentences and minimal metaphor; the "
        "lexicon of administration and bureaucracy (reports, warrants, requisitions, 'the Bureau'); first-"
        "person narration that reports physical detail with clinical precision and leaves moral judgment to "
        "the reader; dialogue in an unmarked, serviceable English.",
  ctx="Waiting for the Barbarians was published by Secker and Warburg (London) on 27 October 1980, three years "
      "after In the Heart of the Country and before Life & Times of Michael K (1983); it won the James Tait "
      "Black Memorial Prize and the Geoffrey Faber Memorial Prize, takes its title and its central situation "
      "from Cavafy's poem 'Waiting for the Barbarians' (1904) and from Buzzati's The Tartar Steppe (1940), and "
      "was written in South Africa during the apartheid years and the border wars of the 1970s and 1980s.",
  sig="The novel that established Coetzee's international reputation and one of the most widely taught "
      "allegories of colonial power in English; Philip Glass made an opera of it in 2005, it is central to "
      "the criticism of Coetzee's ethics, and it is his selection in the Norton Anthology, printed as the "
      "extract 'From Waiting for the Barbarians'.",
  canon="Major canon",
  crit="The novel has been central to the critical literature on Coetzee and on the ethics of postcolonial "
       "representation: critics have read it against Cavafy's poem, against the South African border wars of "
       "the 1980s and against the philosophy of torture, and have debated whether allegory is a way of evading "
       "history or the only honest way of representing it. Its deliberate refusal of national names has been "
       "both praised as a universalising move and attacked as a withdrawal from specific South African "
       "responsibility; the recurrent reading of the magistrate as a version of the liberal conscience, "
       "complicit and self-deceived, has shaped the reception of all of Coetzee's later work, and the novel "
       "has been compared to Conrad's Heart of Darkness as a founding text of the colonial frontier narrative.",
  biblio="Published on 27 October 1980 by Secker and Warburg (London); 156 pages in the first hardcover edition. "
         "A selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page "
         "1046; the Norton text is an extract, and this record covers the whole novel.",
  notes="The plot and publication details follow Wikipedia's article on the novel, read directly, which is "
        "consistent with the summary in Coetzee's article and with general accounts of the book; the novel was "
        "not read complete in this session.",
  ver="partially verified", sources=[W_WB, W_JC, NAEL]),
]

WORKS += [
W10("Fond Memory", EB, "1987", "Poem", "significant",
  genres=G("Lyric Poetry", "Confessional Poetry", "Narrative Poetry"),
  themes=T("Migration, exile and diaspora", "Nationhood and national identity", "Childhood, adolescence and coming of age"),
  movements=M("Second-Wave Feminist Writing"),
  overview="A poem from Boland's The Journey (1987) about her childhood in 1950s London, where an Irish girl at "
           "an English school learns that the songs she is taught are not, after all, her country.",
  content="A short poem in several unrhymed stanzas, recalling a London classroom, the teacher who taught the "
          "children Thomas Moore's Irish melodies, and the moment the child realised that the patriotism of "
          "the song did not belong to her.",
  summary="Boland remembers a classroom in London, the children 'in darned worsted', the teacher, and a song "
          "sung from Thomas Moore's Irish Melodies - 'Oft in the Stilly Night', with its refrain about fond "
          "memory bringing 'the light of other days around me'. For the Irish child in an English school the "
          "song is both a link to home and an embarrassment: the other children sing it without knowing what "
          "they are singing, while she knows and cannot say. The poem's title takes the song's own phrase and "
          "turns it: 'fond memory' is what the emigrant lives on, but it is also the false consolation that "
          "makes a country into a song. The poem ends on the speaker's recognition that she thought this was "
          "her country - 'was, will be again' - and that the upward-straining music was a 'safe inventory of "
          "pain': a shared, sentimentalised account of Irish suffering that she was wrong to trust. The adult "
          "poem keeps the melody and withdraws the belief.",
  themes_text="The poem is about the education of an emigrant child into a national identity she has not chosen "
              "and cannot quite own. Moore's melodies, which were the sound of Irish nationalism in middle-"
              "class drawing rooms on both sides of the Irish Sea, are shown to be a kind of manufactured "
              "memory, and the child's discomfort is the beginning of the poet's later critique of the "
              "rhetoric of Irish suffering. Displacement, class (the darned worsted, the London school) and "
              "the pressure of a national song on a private child run together, and the poem's irony is "
              "directed as much at the speaker's own longing as at the English school.",
  structure="Four irregular stanzas in free verse, with short lines and a syntax that breaks across line "
            "endings; the poem moves from scene (the classroom) to song (Moore's lyric) to reflection, and the "
            "final stanza's flat contradiction ('And I was wrong') turns the poem against itself.",
  style="Plain, exact, conversational free verse with a deliberately unpoetic vocabulary and a few"
        " highly charged abstractions; the quoted song supplies the only regular rhythm, and the poem's own "
        "lines are broken to resist it; the tone is wry, wounded and self-correcting.",
  ctx="The Journey (Carcanet, 1987) is the collection in which Boland turned from the inherited rhetoric of "
      "Irish poetry to her own history as a diplomat's daughter in London and New York; 'Fond Memory' and its "
      "companion 'An Irish Childhood in England: 1951' belong to that autobiographical turn, and 'Fond "
      "Memory' revises Thomas Moore's 'Oft in the Stilly Night' (Irish Melodies, 1808-1834).",
  sig="One of Boland's most discussed poems of the 1980s and a set text in Irish schools; it is one of her "
      "three selections in the Norton Anthology and the poem most often used to introduce her treatment of "
      "exile and national identity.",
  canon="Secondary canon",
  biblio="Published in The Journey and Other Poems (Manchester: Carcanet, 1987; New York: Carcanet, 1987). A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 1059.",
  notes="The poem was not read complete; the description follows the quotations and discussion in the Post "
        "Identity article on Boland and the Liverpool University Press chapter on her memory poems, both read "
        "as search extracts, which quote the closing lines and name Moore's song.",
  ver="partially verified", sources=[BOL_POSTID, W_EB, NAEL]),
W10("The Dolls Museum in Dublin", EB, "1994", "Poem", "significant",
  genres=G("Lyric Poetry", "Political Poetry", "Formal Verse"),
  themes=T("History, truth and the uses of the past", "Nationhood and national identity", "War, combat and its aftermath"),
  movements=M("Second-Wave Feminist Writing"),
  overview="A poem from In a Time of Violence (1994) that walks through a Dublin museum of dolls and finds, "
           "behind the glass cases, Easter 1916 and the innocent society that the Rising destroyed.",
  content="A poem in unrhymed quatrains that describes the dolls - their cracked paint, soiled cotton and "
          "waxen arms - and then reconstructs, through them, the Dublin of the Easter week of 1916, the "
          "officers, the terraces, the Shelbourne bar, and the children with their governesses on College "
          "Green.",
  summary="The poem begins with the dolls' damage: 'The wounds are terrible. The paint is old', the cracks on "
          "the lips cannot be fixed, and the arms are 'ivory dissolved to wax'. From there the poem "
          "reconstructs the world the dolls belonged to - the Quadrille, the waltz, the yacht-club terraces, "
          "the carriage wheels on the cobbled quays - and then names the occasion: 'And recreate Easter in "
          "Dublin.' The second half is a sequence of images of the city in Easter week, 1916: booted officers "
          "and their mistresses, sunlight on College Green, the bar of the Shelbourne full, laughter on the "
          "terraces, rumour at the barracks, 'The Empire is summoning its officers' and the carriages turning "
          "back. Children walk with governesses, looking down at their dolls and then up at the passing "
          "carriage, 'the shadow chilling them'. The poem returns to the museum and to twilight: the shadows "
          "on the dolls are 'bruises on the stitched cotton clothes', and the dolls' wide eyes cannot address "
          "the helplessness of what they have survived. The last lines make them the keepers of a history they "
          "can record but not feel - 'To be the present of the past. / To infer the difference / with a "
          "terrible stare. / But not feel it. / And not know it.'",
  themes_text="Boland reads the 1916 Rising through the objects of the society that it interrupted: the dolls "
              "are the possessions of the Anglo-Irish middle class whose world the Rising ended, and their "
              "damage is history's. The poem is an act of historical imagination that refuses nostalgia - the "
              "elegance of the Shelbourne and the yacht club is not defended, but the violence that ends it is "
              "not celebrated either - and its final insistence on the dolls' inability to feel or know is a "
              "warning about the museum as a way of remembering: glass cases preserve the past and drain it of "
              "consequence. The poem's ekphrastic gaze is also a feminist one, finding public history in the "
              "domestic and decorative objects of women and children.",
  structure="Eleven unrhymed quatrains, mostly in loose iambic pentameter with occasional trimeter lines; the "
            "poem moves from description to reconstruction to reflection, and the last five short lines break "
            "the quatrain pattern to deliver the verdict on the dolls.",
  style="Plain, declarative, almost flat in its diction, with a strong visual and tactile register (cracked "
        "paint, soiled cotton lawn, parchment-coloured waists); short sentences and a repeated imperative "
        "('Recall... Hum... Promenade... Put back...') that makes the poem a guided tour; the rhythm is "
        "regular enough to feel like a museum catalogue and irregular enough to keep the reader uneasy.",
  ctx="In a Time of Violence (Carcanet, 1994) is Boland's sequence of poems about Ireland, history and the "
      "violence of representation, including 'That the Science of Cartography Is Limited' and the title "
      "sequence; 'The Dolls Museum in Dublin' responds to the Easter Rising of 1916 and to the tradition of "
      "Yeats's poems on the Rising, and takes its title from the doll collection formerly displayed in "
      "Dublin.",
  sig="One of the most anthologised Irish poems of the 1990s and a standard text for the study of Boland's "
      "historical poems; it is one of her three Norton selections and is widely read alongside Yeats's "
      "'Easter 1916'.",
  canon="Secondary canon",
  biblio="Published in In a Time of Violence (Manchester: Carcanet, 1994; New York: W. W. Norton, 1994). A "
         "selection of The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 1060. "
         "The text is quoted here from the course page at Michigan State University, which prints the poem.",
  notes="The poem's text was read complete on the Michigan State University course page, and the reading of it "
        "follows the discussion in the Post Identity article; the museum itself and the details of its "
        "collection were not otherwise verified.",
  ver="partially verified", sources=[BOL_MSU, BOL_POSTID, W_EB, NAEL]),
W10("The Lost Land", EB, "1998", "Poem", "significant",
  genres=G("Lyric Poetry", "Elegiac Poetry", "Free Verse"),
  themes=T("Migration, exile and diaspora", "Memory, trauma and testimony", "Land, place and regional belonging"),
  movements=M("Second-Wave Feminist Writing"),
  overview="The title poem of Boland's 1998 collection: a woman with two grown daughters tries to give them a "
           "country, and finds that memory itself has become an emigrant.",
  content="A short poem in free verse in which the speaker counts what she wanted from the earth - her "
          "daughters, and one piece of ground, one city, one river - and then imagines them leaving Ireland as "
          "generations had left it before.",
  summary="The poem opens with an inventory of desire: 'I have two daughters. / They are all I ever wanted "
          "from the earth. / Or almost all.' What she wanted besides was 'one piece of ground', 'One city "
          "trapped by hills. One urban river. An island in its element', so that she could say 'mine. My own' "
          "and mean it. Now the daughters are grown and far away, and memory itself has become an emigrant, "
          "'wandering in a place / where love dissembles itself as landscape', where the hills are the "
          "colours of a child's eyes and the children are 'distances, horizons'. At night, on the edge of "
          "sleep, she sees the shore of Dublin Bay and its granite pier and asks whether this is how the "
          "emigrants saw it, 'backing out on the mailboat at twilight'. The last movement imagines her own "
          "place at the landward rail of that boat, searching for the last sight of a hand, and then 'on the "
          "underworld side of that water' in the dark, saying over 'all the names I know for a lost land: / "
          "Ireland. Absence. Daughter.'",
  themes_text="The lost land of the title is not one place but three at once - Ireland, the past and the "
              "children - and the poem's power comes from refusing to separate them. Boland writes about "
              "emigration as a structure of feeling rather than an event: the mailboat, the railway pier and "
              "the dark water are the inherited images of Irish departure, and the poem's speaker finds "
              "herself, a woman who stayed, occupying the emigrant's position because her daughters have left. "
              "Motherhood and national belonging are placed on the same footing, and the poem's ending - the "
              "three names said in the dark - makes absence itself the ground on which identity is built.",
  structure="Four movements of unequal length in free verse: the inventory of what she wanted, the emigration "
            "of memory, the imagined departure of the daughters, and the speaker's own imagined place on the "
            "boat; the poem ends with a three-word list that acts as a refrain and a summary.",
  style="Short, spare lines and a conversational syntax; repetition ('One piece of ground', 'One city', 'One "
        "urban river') and anaphora; a plain vocabulary of landscape and family, with only a few charged "
        "metaphors ('memory itself / has become an emigrant'); the last lines are unpunctuated as a list.",
  ctx="The Lost Land (Carcanet, 1998) is the collection in which Boland wrote most directly about emigration, "
      "the Famine and the Irish diaspora, and the title poem is its statement of theme; the 'underworld side "
      "of that water' draws on the classical descent to the dead as well as on the Irish emigrant's crossing, "
      "and the poem's Dublin Bay is the scene of the mailboat departures from Dún Laoghaire.",
  sig="The title poem of one of Boland's central collections and among her most frequently quoted poems on "
      "emigration and motherhood; it is one of her three Norton selections.",
  canon="Secondary canon",
  biblio="Published in The Lost Land (Manchester: Carcanet, 1998; New York: W. W. Norton, 1998). A selection of "
         "The Norton Anthology of English Literature, 11th edition, vol. F, beginning on page 1061. The text is "
         "quoted here from the Poetry Foundation's printing.",
  notes="The poem's text was read complete on the Poetry Foundation page, which reports the 1998 Norton "
        "printing; the review in the January Magazine was also read as a search extract for the collection's "
        "reception.",
  ver="partially verified", sources=[BOL_LOST, W_EB, NAEL]),
]
