"""Installment 10, wave 30: the American prose block - DeLillo, Pynchon, Carver,
Bambara, Kingston, Silko, Reed and Rodriguez.

Eight new authors and eight works, covering ten of the Norton rows (both of
Kingston's selections map to The Woman Warrior, as the coverage matrix records).

First printings settled here:

    Don DeLillo, White Noise            Viking Press, 1985
    Thomas Pynchon, "Entropy"           Kenyon Review, Spring 1960
    Raymond Carver, "Cathedral"         The Atlantic Monthly, September 1981;
                                        Cathedral (Knopf, 1983)
    Toni Cade Bambara, "The Lesson"     Gorilla, My Love (Random House, 1972)
    Maxine Hong Kingston,
        The Woman Warrior               Knopf, 1976; "No Name Woman" in Viva, January 1975
    Leslie Marmon Silko, "Lullaby"      Laguna Woman (1974)
    Leslie Marmon Silko, "Language and
        Literature from a Pueblo Indian
        Perspective"                    The First Words conference volume (1981)
    Ishmael Reed, "Neo-HooDoo Manifesto" Conjure (University of Massachusetts Press, 1972)
    Richard Rodriguez, Hunger of Memory  David R. Godine, 1982
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAAL  # noqa: E402

DD = "Don DeLillo"
TP = "Thomas Pynchon"
RC = "Raymond Carver"
TCB = "Toni Cade Bambara"
MHK = "Maxine Hong Kingston"
LMS = "Leslie Marmon Silko"
IR = "Ishmael Reed"
RR = "Richard Rodriguez"

PM = "Postmodernism and Postmodern Fiction"
MET = "Metafiction"
MIN = "Minimalism and Dirty Realism"
NAR = "Native American Renaissance"
AAW = "Postwar African American Writing: Protest and Its Critics"
AAM = "Asian American Literary Movement"
SWF = "Second-Wave Feminist Writing"

W_DD = "Don DeLillo (Wikipedia)"
W_WN = "White Noise (Viking Press, 1985), publication and National Book Award records"
W_TP = "Thomas Pynchon (Wikipedia)"
W_ENT = "Entropy (short story) (Wikipedia) and The Kenyon Review, Spring 1960"
W_RC = "Raymond Carver (Wikipedia)"
W_CATH = "Cathedral (Knopf, 1983) and the Atlantic Monthly printing of September 1981"
W_TCB = "Toni Cade Bambara (Wikipedia)"
W_GORILLA = "Gorilla, My Love (Random House, 1972), catalogue and contents record"
W_MHK = "Maxine Hong Kingston (Wikipedia)"
W_WW = "The Woman Warrior (Alfred A. Knopf, 1976), copyright page and publication records"
W_LMS = "Leslie Marmon Silko (Wikipedia)"
W_LAGUNA = "Laguna Woman (1974) and Storyteller (1981), bibliographic records"
W_IR = "Ishmael Reed (Wikipedia)"
W_CONJURE = "Conjure: Selected Poems 1963-1970 (University of Massachusetts Press, 1972), catalogue record"
W_RR = "Richard Rodriguez (Wikipedia)"
W_HOM = "Hunger of Memory (David R. Godine, 1982), publication records"

AUTHORS = [
A10(DD, MAJ, "1936", "2026", "New York City, United States",
  "American; novelist, short-story writer and playwright writing in English",
  "American novelist of the systems novel, whose White Noise, Libra and Underworld made the media, "
  "the conspiracy and the American century itself into the matter of literary fiction",
  "Don DeLillo was born in New York City on 20 November 1936, the son of Italian immigrants from "
  "Molise, and grew up in the Bronx; he has said that he did not read a book until he was eighteen. He "
  "took a degree in communication arts at Fordham University in 1958, worked for five years in "
  "advertising in Manhattan, and began writing fiction in the evenings. Americana (1971) was his first "
  "novel; End Zone (1972), Great Jones Street (1973), Ratner's Star (1976) and Players (1977) followed "
  "before The Names (1982) and White Noise (1985), which won the National Book Award and made him "
  "famous at forty-eight. Libra (1988), a novel of the Kennedy assassination, Mao II (1991), "
  "Underworld (1997) - which sold more than any of his other books and is a history of the Cold War "
  "told through the baseball that ended the 1951 National League pennant - and The Body Artist (2001), "
  "Cosmopolis (2003), Falling Man (2007), Point Omega (2010) and Zero K (2016) followed. He wrote plays "
  "- The Engineer of Moonlight (1979), Valparaiso (1999) and Love-Lies-Bleeding (2005) - and essays "
  "collected in The Vondelpark (2020). He received the Jerusalem Prize in 1999, the Library of Congress "
  "Prize for American Fiction in 2013 and the National Book Foundation's Medal for Distinguished "
  "Contribution to American Letters in 2014, and died in New York on 13 October 2026.",
  "Novels: Americana (1971), End Zone (1972), Great Jones Street (1973), Ratner's Star (1976), Players "
  "(1977), Running Dog (1978), Amazons (1980, as Cleo Birdwell), The Names (1982), White Noise (1985), "
  "Libra (1988), Mao II (1991), Underworld (1997), The Body Artist (2001), Cosmopolis (2003), Falling "
  "Man (2007), Point Omega (2010), Zero K (2016) and The Silence (2020). Plays: The Engineer of "
  "Moonlight (1979), Valparaiso (1999) and Love-Lies-Bleeding (2005). Stories and essays: The Angel "
  "Esmeralda (2011) and The Vondelpark (2020).",
  "Long, flat, declarative sentences that report the most extreme events in the tone of a news wire; "
  "dialogue that is mostly people repeating the language of advertising, television and the "
  "corporation; lists and catalogues used as a formal device; a narrator who knows more than any "
  "character but refuses to explain; and an ending that stops rather than resolves.",
  "Consumer culture and the saturation of daily life by media; the conspiracy as a structure of "
  "American history; the fear of death and the technologies that manage it; the family as a site of "
  "improvisation and error; the Cold War and its aftermath; and language itself, which his novels "
  "treat as a system with its own momentum.",
  "DeLillo is the most influential American novelist of the post-1970 period. White Noise's National "
  "Book Award in 1985 is often taken as the moment the academy recognised the novel of media "
  "saturation; Underworld was voted one of the great American novels of the century; and his "
  "influence runs through the fiction of David Foster Wallace, Jonathan Franzen, Bret Easton Ellis and "
  "Jennifer Egan. The Library of America began issuing his work in 2022.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on DeLillo and from the "
           "publisher's records of White Noise; they were not checked against a printed bibliography. "
           "Installment 10 records one Norton selection - the 'Airborne Toxic Event' section of White "
           "Noise - so the other seventeen novels, the plays and the stories have no records, and the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_DD, W_WN, NAAL]),
A10(TP, MAJ, "1937", None, "Glen Cove, New York, United States",
  "American; novelist and short-story writer writing in English",
  "American novelist, the great recluse of postwar American letters, whose V., Gravity's Rainbow and "
  "Mason and Dixon made the historical conspiracy the form of the American novel and who has been "
  "fugitive from the public since the 1960s",
  "Thomas Ruggles Pynchon Jr. was born in Glen Cove, New York, on 8 May 1937 and grew up in Long "
  "Island; he took a degree in English at Cornell in 1959, where he is said to have attended Vladimir "
  "Nabokov's lectures, and served two years in the US Navy before working for the Boeing Company in "
  "Seattle, where he wrote technical copy and, in his spare time, his first novel. V. (1963) won the "
  "William Faulkner Foundation Award for a first novel; The Crying of Lot 49 (1966) was written while "
  "he was living in California; Gravity's Rainbow (1973), a novel of the V-2 rocket and the last "
  "months of the Second World War, won the National Book Award in 1974 and was famously awarded the "
  "Pulitzer Prize by its fiction jury only to be overruled by the Pulitzer board. Slow Learner (1984) "
  "collected his early stories with an introduction that is one of the few autobiographical documents "
  "he has published; Vineland (1990), Mason and Dixon (1997), Against the Day (2006), Inherent Vice "
  "(2009), Bleeding Edge (2013) and the posthumous Shadow Ticket (2025) followed. He has never given "
  "a public reading, has rarely been photographed since the 1960s, and his whereabouts - long rumoured "
  "to be New York City - are a running joke in American letters.",
  "Novels: V. (1963), The Crying of Lot 49 (1966), Gravity's Rainbow (1973), Vineland (1990), Mason "
  "and Dixon (1997), Against the Day (2006), Inherent Vice (2009), Bleeding Edge (2013) and Shadow "
  "Ticket (2025). Stories: Slow Learner (1984), collecting 'The Small Rain' (1959), 'Low-Lands' "
  "(1960), 'Entropy' (1960), 'Under the Rose' (1961) and 'The Secret Integration' (1964). Essays: "
  "The introduction to Slow Learner (1984) and the collected occasional pieces.",
  "Sentences that run for pages and subordinate clause upon clause until the reader is lost in the "
  "syntax on purpose; an encyclopaedic range of registers, from the bureaucratic to the slapstick; "
  "songs, parodies and doggerel set inside the narrative; a plot that is a conspiracy the reader can "
  "never fully assemble; and an ending that withholds the revelation it has been promising.",
  "The Second World War and the machinery of the V-2 as an image of the modern state; entropy and the "
  "second law of thermodynamics as a metaphor of culture; the underground, the postal system and the "
  "counter-histories that official history suppresses; empire and the survey as forms of violence; "
  "paranoia as a method of knowledge; and the possibility that the conspiracy is real and knowing it "
  "changes nothing.",
  "Pynchon is the central American novelist of the encyclopaedic mode and the one whose work did most "
  "to make the postwar American novel a system rather than a story. Gravity's Rainbow is on every "
  "short list of the great American novels of the century, the National Book Award of 1974 is only the "
  "most official of his honours, and his influence is visible in DeLillo, Wallace, Vollmann and the "
  "whole of the literary novel after 1973.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Pynchon and from the record of "
           "Slow Learner; they were not checked against a printed bibliography. Installment 10 records "
           "one Norton selection - 'Entropy' - so the nine novels and the other stories have no "
           "records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_TP, W_ENT, NAAL]),
A10(RC, MAJ, "1938", "1988", "Clatskanie, Oregon, United States",
  "American; short-story writer and poet writing in English",
  "American short-story writer and poet, the central figure of the American revival of the story in "
  "the 1970s and 1980s, whose spare, unconsoling stories of ordinary people in the American Northwest "
  "were first called 'minimalist' and are now simply the sound of the form",
  "Raymond Clevie Carver Jr. was born in Clatskanie, Oregon, on 25 May 1938, the son of a sawmill "
  "worker and a waitress, and grew up in Yakima, Washington. He married at nineteen, had two children "
  "by twenty-one, and worked - as a delivery boy, a janitor, a farm hand and a sawmill hand - while "
  "attending night classes; he took a BA at Chico State in 1963 and an MFA at the University of Iowa "
  "in 1965, and taught at several universities for the rest of his life. He was an alcoholic until he "
  "stopped drinking in 1977, a fact central to everything he wrote. Will You Please Be Quiet, Please? "
  "(1976) was a finalist for the National Book Award; Furious Seasons (1977), What We Talk About When "
  "We Talk About Love (1981) and Cathedral (1983) followed, the last two edited by Gordon Lish, whose "
  "cuts were so severe that the publication of the manuscripts as Carver wrote them - in 2009 and "
  "2015 - has changed the received account of his style. He also published six books of poems, "
  "including Near Klamath (1968), Winter Insomnia (1970), At Night the Salmon Move (1976), Where "
  "Water Comes Together with Other Water (1985) and Ultramarine (1986). He was elected to the American "
  "Academy of Arts and Letters in 1988, and died of lung cancer in Port Angeles, Washington, on 2 "
  "August 1988.",
  "Stories: Will You Please Be Quiet, Please? (1976), Furious Seasons (1977), What We Talk About When "
  "We Talk About Love (1981), Cathedral (1983), Elephant (1988) and Call If You Need Me (2000); "
  "collected in Where I'm Calling From (1988) and Carver: Collected Stories (Library of America, "
  "2009). Poetry: Near Klamath (1968), Winter Insomnia (1970), At Night the Salmon Move (1976), Where "
  "Water Comes Together with Other Water (1985), Ultramarine (1986), A New Path to the Waterfall "
  "(1989) and All of Us (1996).",
  "Short sentences, plain diction and almost no metaphor; dialogue recorded without commentary; "
  "detail used sparingly and where it lands hardest; scenes that end before the emotional consequence "
  "arrives; and a narrator who reports without judging, which is what gives the stories their "
  "pressure.",
  "Drinking and its aftermath; marriage and the slow work of its failure; work and money in the "
  "American Northwest; the ordinary epiphany that arrives too late to be useful; class, and the shame "
  "of not having enough; and, in the late stories, the possibility of grace.",
  "Carver is the most imitated American short-story writer of the last forty years and the one whose "
  "name is attached to the revival of the form in the 1980s. Cathedral was nominated for the National "
  "Book Critics Circle Award and the Pulitzer Prize, his stories are in every American anthology of "
  "the period, and the publication of his unedited manuscripts has made him a central case in the "
  "discussion of what an editor does to a writer.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Carver and from the records of "
           "Cathedral; they were not checked against a printed bibliography. Installment 10 records one "
           "Norton selection - 'Cathedral' - so the other five collections and the six books of poems "
           "have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_RC, W_CATH, NAAL]),
A10(TCB, MAJ, "1939", "1995", "New York City, United States",
  "American; short-story writer, novelist, essayist and filmmaker writing in English",
  "American short-story writer and essayist of the Black Arts generation, whose Gorilla, My Love and "
  "The Salt Eaters made the speech of Black neighbourhoods into a literary form and whose anthology "
  "The Black Woman put Black feminism on the map of American publishing",
  "Toni Cade Bambara was born Miltona Mirkin Cade in New York City on 25 March 1939 and grew up in "
  "Harlem, Brooklyn and Queens; she took the name Toni Cade in her teens and added Bambara in 1970 "
  "after discovering the West African ethnic group in a friend's artwork. She took a BA in theatre "
  "arts at Queens College in 1959, studied mime in Florence, and completed an MA in African American "
  "literature at the City College of New York in 1964, with a thesis on the Black short story. She "
  "taught at City College and at Livingston College, worked as a community organiser in Newark and "
  "New York, and in 1970 edited The Black Woman: An Anthology, one of the first collections of Black "
  "feminist writing in the United States. Gorilla, My Love (1972) collected her short stories; The "
  "Sea Birds Are Still Alive (1977) followed. The Salt Eaters (1980), her only novel, won the American "
  "Book Award and is one of the formal achievements of Black feminist fiction. From the late 1970s she "
  "worked increasingly in film, writing the screenplays for The Bombing of Osage Avenue, on the 1985 "
  "police bombing of the MOVE house in Philadelphia, and for Louis Massiah's W.E.B. Du Bois: A "
  "Biography in Four Voices. She taught at Spelman College and at Rutgers, and died of colon cancer in "
  "New York on 9 December 1995; Deep Sightings and Rescue Missions, a posthumous collection of essays "
  "and stories, appeared in 1996.",
  "Fiction: Gorilla, My Love (1972), The Sea Birds Are Still Alive (1977) and The Salt Eaters (1980). "
  "Anthology and essays: The Black Woman: An Anthology (1970) and Deep Sightings and Rescue Missions "
  "(1996). Screenplays: The Bombing of Osage Avenue and W.E.B. Du Bois: A Biography in Four Voices "
  "(1996).",
  "Narration in a child's or a neighbourhood voice that is allowed its own grammar; dialogue in "
  "unreconstructed Black vernacular, with the spelling to match; comedy used as a mode of political "
  "argument; an ending that withholds the adult's explanation; and a narrative that refuses to "
  "translate its community for an outside reader.",
  "Childhood and the education of a Black girl in the city; the church, the school and the "
  "neighbourhood as institutions of both belonging and constraint; the Black Arts and Black feminist "
  "politics of the 1970s; class and the economics of survival; and the ordinary genius of people who "
  "are not written about.",
  "Bambara is a central figure of the Black Arts Movement and one of the founders of Black feminist "
  "literary culture in the United States. The Black Woman was the first anthology of its kind, "
  "Gorilla, My Love is a standard text in American fiction courses, and The Salt Eaters is discussed "
  "as a landmark of Black feminist experimentation. Her influence on the short story of the 1980s and "
  "1990s is acknowledged by writers from Toni Morrison to Edwidge Danticat.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Bambara and from the catalogue "
           "records of Gorilla, My Love; they were not checked against a printed bibliography. "
           "Installment 10 records one Norton selection - 'The Lesson' - so the novel, the other "
           "stories and the anthologies have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_TCB, W_GORILLA, NAAL]),
A10(MHK, MAJ, "1940", None, "Stockton, California, United States",
  "American; memoirist, novelist and essayist writing in English",
  "Chinese American memoirist and novelist, whose The Woman Warrior changed the American memoir by "
  "refusing to choose between the life and the legend, and whose China Men and Tripmaster Monkey "
  "extended that refusal across two further books",
  "Maxine Hong Kingston was born Maxine Ting Ting Hong in Stockton, California, on 27 October 1940, "
  "the daughter of Chinese immigrants who had run a laundry and later a gambling house; she grew up "
  "listening to her mother's 'talk-stories', which became the method of her writing. She took a BA in "
  "English at the University of California at Berkeley in 1962 and a teaching certificate in 1963, "
  "married the actor Earll Kingston in 1962, and taught English and mathematics in California and "
  "then in Hawaii, where she moved in 1967. The Woman Warrior: Memoirs of a Girlhood Among Ghosts "
  "(1976) won the National Book Critics Circle Award for general nonfiction and made her - in "
  "disputes with Frank Chin that are now a standard part of the discussion of Asian American "
  "literature - the most controversial and most read Chinese American writer of the period. China "
  "Men (1980) won the National Book Award for nonfiction; Tripmaster Monkey: His Fake Book (1989) was "
  "her first novel; Hawai'i One Summer (1987), To Be the Poet (2002), The Fifth Book of Peace (2003) "
  "and I Love a Broad Margin to My Life (2011) followed. She taught at Berkeley from 1990, was "
  "arrested twice in anti-war protests, received the National Humanities Medal in 1997 and the "
  "National Medal of Arts in 2013, and is the subject of the documentary Maxine Hong Kingston: "
  "Talking Story (2010).",
  "Books: The Woman Warrior (1976), China Men (1980), Hawai'i One Summer (1987), Through the Black "
  "Curtain (1987), Tripmaster Monkey: His Fake Book (1989), To Be the Poet (2002), The Fifth Book of "
  "Peace (2003) and I Love a Broad Margin to My Life (2011).",
  "A first-person 'I' that is never quite the author; the 'talk-story' as the structural unit, so that "
  "a chapter begins as a folktale and ends as a memory; direct address to the reader and to the dead; "
  "a syntax that keeps the cadence of spoken Chinese-influenced English; and a refusal to tell the "
  "reader which parts are true.",
  "The relation of a daughter to a mother whose stories are her history; Chinese and Chinese American "
  "traditions, and the cost of leaving them; silence, and the voice a girl has to find; immigration, "
  "the paper sons and the exclusion laws; and the fictionality of all autobiography.",
  "The Woman Warrior is the book that made the Asian American memoir a national form and one of the "
  "most widely taught American books of the period. Its National Book Critics Circle Award, the "
  "decade of argument it provoked about authenticity and representation, and its influence on the "
  "memoirs and novels of the 1980s and 1990s make it a founding text of Asian American literature; "
  "Kingston's two national medals confirm her standing.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Kingston and from the "
           "copyright page of The Woman Warrior, which gives 'No Name Woman' as having appeared in "
           "slightly different form in Viva, January 1975; they were not checked against a printed "
           "bibliography. Installment 10 records the book once for both of its Norton selections - "
           "'No Name Woman' and the excerpt from 'A Song for a Barbarian Reed Pipe' - so China Men, "
           "Tripmaster Monkey and the later books have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_MHK, W_WW, NAAL]),
A10(LMS, MAJ, "1948", None, "Albuquerque, New Mexico, United States",
  "American; Laguna Pueblo novelist, poet and essayist writing in English",
  "Laguna Pueblo novelist, poet and essayist, whose Ceremony is the central novel of the Native "
  "American Renaissance and whose Storyteller made the photograph, the poem and the oral account parts "
  "of a single form",
  "Leslie Marmon Silko was born in Albuquerque, New Mexico, on 5 March 1948 and grew up at Laguna "
  "Pueblo, where her family - Laguna, Mexican and white - had lived for generations; she has said that "
  "she grew up 'on the border' of the Pueblo and never fully belonged to any of its parts, an "
  "experience that shapes everything she wrote. She took a BA in English at the University of New "
  "Mexico in 1969 and attended law school for three years before turning to writing. Laguna Woman "
  "(1974) was her first book of poems; Ceremony (1977), her first novel, tells the story of a Laguna "
  "veteran of the Second World War who is healed by a Navajo ceremony and a traditional story, and it "
  "is generally regarded as the finest novel of the Native American Renaissance. Storyteller (1981) "
  "combined poems, photographs and prose in a form modelled on the Pueblo oral tradition; "
  "Almanac of the Dead (1991), a vast novel of the Americas across five centuries, and Gardens in the "
  "Dunes (1999) followed, with the essays of Yellow Woman and a Beauty of the Spirit (1996) and "
  "Conversations with Leslie Marmon Silko (2000). She has received a MacArthur Fellowship (1981), the "
  "Native Writers' Circle of the Americas Lifetime Achievement Award and the 2020 lifetime achievement "
  "award of the Academy of American Poets.",
  "Fiction: Ceremony (1977), Almanac of the Dead (1991) and Gardens in the Dunes (1999). Poetry: "
  "Laguna Woman (1974). Mixed form: Storyteller (1981). Nonfiction and essays: Yellow Woman and a "
  "Beauty of the Spirit (1996) and Conversations with Leslie Marmon Silko (2000).",
  "A narrative that moves between the present and the mythic without marking the transition; the "
  "Pueblo oral tradition used as a structural principle rather than as decoration; a prose that is "
  "plain and declarative in the modern sections and incantatory in the traditional ones; the landscape "
  "of the Southwest presented as inhabited rather than as scenery; and an ending that returns to the "
  "story that opened the book.",
  "The survival of Native people and Native stories under colonisation; healing, and the difference "
  "between curing a body and restoring a person; the Second World War and the reservation; the land as "
  "a living relation rather than property; the oral tradition as history; and the continuity of "
  "women's knowledge across generations.",
  "Silko is one of the two or three central figures of the Native American Renaissance and the writer "
  "whose Ceremony is most often named as its finest novel. Storyteller changed what a book of Native "
  "American writing could look like, Almanac of the Dead is a landmark of the 1990s novel, and her "
  "MacArthur Fellowship of 1981 makes her one of the first Native American writers so honoured.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Silko and from the "
           "bibliographic records of Laguna Woman and Storyteller; they were not checked against a "
           "printed bibliography. Installment 10 records two Norton selections - 'Lullaby' and "
           "'Language and Literature from a Pueblo Indian Perspective' - separately, since they belong "
           "to different books, so the novels and the later essays have no records and the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_LMS, W_LAGUNA, NAAL]),
A10(IR, MAJ, "1938", None, "Chattanooga, Tennessee, United States",
  "American; novelist, poet, essayist, editor and songwriter writing in English",
  "American novelist, poet and editor, the founder of the Neo-HooDoo aesthetic, whose The Free-Lance "
  "Pallbearers, Mumbo Jumbo and the Yardbird anthologies made a satirical, syncretic Black American "
  "postmodernism that has been an alternative to the realist novel for fifty years",
  "Ishmael Scott Reed was born in Chattanooga, Tennessee, on 22 February 1938 and grew up in Buffalo, "
  "New York, where his mother worked as a housekeeper and his stepfather in a steel mill. He took a "
  "degree in English at the University of Buffalo in 1960, worked as a journalist and a radio "
  "announcer, moved to New York in 1962, co-founded the East Village Other - one of the first "
  "underground papers - and became a central figure in the Black Arts Movement, though never a "
  "believer in any of its orthodoxies. The Free-Lance Pallbearers (1967) was his first novel; Yellow "
  "Back Radio Broke-Down (1969) and Mumbo Jumbo (1972) followed, the last a comic history of the "
  "Harlem Renaissance as a conflict between Neo-HooDoo and the Western aesthetic, and now a standard "
  "text of the American postmodern novel. Conjure (1972) collected his poems; he edited the Yardbird "
  "anthologies (1973-1977) and later the multi-volume Before Columbus Foundation anthologies, founded "
  "the Before Columbus Foundation and its American Book Awards in 1976, and published Flight to Canada "
  "(1976), The Terrible Twos (1982), Reckless Eyeballing (1986), The Terrible Threes (1989), Japanese "
  "by Spring (1993) and Juice! (2011), as well as six further books of poems and collections of "
  "essays.",
  "Novels: The Free-Lance Pallbearers (1967), Yellow Back Radio Broke-Down (1969), Mumbo Jumbo (1972), "
  "The Last Days of Louisiana Red (1974), Flight to Canada (1976), The Terrible Twos (1982), Reckless "
  "Eyeballing (1986), The Terrible Threes (1989), Japanese by Spring (1993) and Juice! (2011). Poetry: "
  "catechism of d neoamerican hoodoo church (1970), Conjure (1972), Chattanooga (1973), A Secretary to "
  "the Spirits (1978), New and Collected Poems (1988) and others. Anthologies and essays: 19 Necromancers "
  "from Now (1970), the Yardbird series (1973-1977), Shrovetide in Old New Orleans (1978), God Made "
  "Alaska, He Just Didn't Finish It (1982) and Airing Dirty Laundry (1993).",
  "A satirical prose built on collage, parody and pastiche; chapters that switch register and medium; "
  "hoodoo as a principle of composition as well as a subject; the detective and the western used as "
  "found forms to be broken; and a narrator who is openly partisan and openly funny.",
  "The conflict between African-derived and European aesthetics in American culture; the suppression "
  "of Black cultural history and its underground survival; satire as a political instrument; the "
  "publishing industry and the politics of who gets anthologised; and American myth as a source to be "
  "plundered rather than revered.",
  "Reed is the founder of the Neo-HooDoo aesthetic and one of the most consistently inventive "
  "American novelists of the last half-century. Mumbo Jumbo is a set text in courses on the American "
  "postmodern novel, the Yardbird anthologies changed the visibility of Black writers in the 1970s, "
  "and his American Book Awards remain an alternative to the established prizes; his influence is "
  "acknowledged by writers as different as Toni Morrison and Paul Beatty.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Reed and from catalogue "
           "records of Conjure; they were not checked against a printed bibliography. Installment 10 "
           "records one Norton selection - 'Neo-HooDoo Manifesto' - which belongs to Conjure "
           "(University of Massachusetts Press, 1972), so the ten novels, the other books of poems and "
           "the anthologies have no records, and the bibliography is incomplete.",
  ver="partially verified", sources=[W_IR, W_CONJURE, NAAL]),
A10(RR, MAJ, "1944", None, "San Francisco, California, United States",
  "American; essayist and memoirist writing in English",
  "Mexican American essayist whose Hunger of Memory made the memoir of assimilation a national "
  "controversy and whose prose has been a sustained argument against the politics of affirmative "
  "action and bilingual education",
  "Richard Rodriguez was born in San Francisco on 31 July 1944, the son of Mexican immigrant parents "
  "from the state of Jalisco; the family moved to Sacramento when he was a small child, and his first "
  "language was Spanish until the nuns at his Catholic school asked his parents to speak English at "
  "home - an episode that became the founding scene of Hunger of Memory. He took a BA in English at "
  "Stanford in 1967, an MA at Columbia in 1969, and studied for a PhD in English at Berkeley, which he "
  "abandoned after three years; he was, by his own account, a beneficiary of affirmative action and "
  "has been its most articulate critic. Hunger of Memory: The Education of Richard Rodriguez (1982) "
  "made him famous and controversial in equal measure, particularly among Mexican American writers who "
  "took its rejection of 'minority' identity as a betrayal. Days of Obligation: An Argument with My "
  "Mexican Father (1992) and Brown: The Last Discovery of America (2002) completed a trilogy on "
  "American race and class, and Darling: A Spiritual Autobiography (2013) followed. He has been an "
  "editor at the Pacific News Service, a correspondent for The NewsHour with Jim Lehrer on PBS, and a "
  "contributor to Harper's, The American Scholar and The New York Times.",
  "Books: Hunger of Memory: The Education of Richard Rodriguez (1982), Days of Obligation: An Argument "
  "with My Mexican Father (1992), Brown: The Last Discovery of America (2002) and Darling: A Spiritual "
  "Autobiography (2013). Essays in Harper's, The American Scholar, The New York Times and elsewhere, "
  "and broadcast work for PBS.",
  "A formal, essayistic English that is deliberately more literary than conversational; the first "
  "person used as an argument rather than a confession; the long periodic sentence; quotation and "
  "anecdote used as evidence; and a habit of refusing the conclusion the reader has been led to "
  "expect.",
  "Assimilation and its costs; language and the loss of a mother tongue; class and the American "
  "university; race and the argument over affirmative action; the Mexican American family; and, in the "
  "later books, the religious imagination and the body.",
  "Hunger of Memory is one of the most widely taught American memoirs of the period and the book that "
  "made assimilation into a public argument for a Mexican American writer. Its reception - praised as "
  "a classic of immigrant autobiography and attacked as a rejection of its own community - is a "
  "standing case in the discussion of American multiculturalism, and the trilogy it belongs to is "
  "central to the literature of American race.",
  bib_status="incomplete",
  bib_note="The titles and dates above come from Wikipedia's article on Rodriguez and from the "
           "publication records of Hunger of Memory; they were not checked against a printed "
           "bibliography. Installment 10 records one Norton selection - the excerpt from Hunger of "
           "Memory - so the three later books and the uncollected essays have no records, and the "
           "bibliography is incomplete.",
  ver="partially verified", sources=[W_RR, W_HOM, NAAL]),
]

WORKS = [
W10("White Noise", DD, "1985", "Novel (postmodern, campus and family narrative)", "major",
  genres=G("Postmodern Fiction", "Satirical Fiction", "Campus Novel"),
  themes=T("Technology, media and consumer society", "Death, illness and mourning",
           "The city, the suburb and modern space"),
  movements=M(PM),
  overview="White Noise was published by Viking in 1985 and won the National Book Award. It is narrated "
           "by Jack Gladney, professor of Hitler studies at the College-on-the-Hill in the invented "
           "town of Blacksmith, and it is in three parts: 'Waves and Radiation', 'The Airborne Toxic "
           "Event' and 'Dylarama'. The Norton selection is the second part, in which a chemical spill "
           "sends a black cloud over the town and the Gladneys are evacuated. It is the novel that made "
           "DeLillo famous and that gave American fiction the phrase 'the airborne toxic event' as a "
           "name for the accidents of late-industrial life.",
  content="Part One establishes the Gladney household - Jack, his fourth wife Babette, and the children "
          "from their earlier marriages - and its economy of consumption: the supermarket, the "
          "television, the radio, the family's talk about death. Jack has built a career on Hitler "
          "studies without speaking German; Babette teaches a course in posture and takes part in "
          "secret experiments. Part Two, the Norton selection, begins with the sirens: a tank car has "
          "derailed and released a cloud of Nyodene Derivative, and the town is evacuated to a Boy "
          "Scout camp in a slow, comic, terrifying procession of cars. Jack is exposed to the cloud "
          "while filling his car, and a technician later tells him he has a 'mass' of Nyodene in his "
          "body. The part ends with the family returned to a town whose normality has been revealed as "
          "a fiction. Part Three follows Jack's discovery that Babette has been taking an experimental "
          "drug, Dylar, that is supposed to abolish the fear of death, and his attempt to obtain it.",
  summary="The 'Airborne Toxic Event' section is the novel's centre, and it works by refusing the "
          "apocalyptic register that its material invites. DeLillo describes the evacuation in the flat "
          "documentary tone of a local news report: the traffic, the radio bulletins that revise the "
          "name of the chemical and the nature of the exposure, the family's bickering in the car, the "
          "refugee camp's improvised routines. The comedy is inseparable from the horror - the town's "
          "disaster is administered by the same institutions that run its schools and its supermarkets "
          "- and that is DeLillo's argument about late-industrial America: catastrophe is not an "
          "interruption of ordinary life but one of its services. Jack's exposure connects the public "
          "event to his private obsession with death, and the section ends with the two scaled to each "
          "other: the cloud that everyone shares and the mass that only he carries. The famous "
          "'airborne toxic event' is a phrase the novel gives to the radio, and its migrations - the "
          "authorities rename the chemical and the event as the situation develops - are a study in how "
          "institutions manage language in order to manage fear. When the section closes, nothing has "
          "been resolved and everything has been normalised, which is the novel's point about the "
          "American 1980s.",
  themes_text="The first subject is the media's mediation of catastrophe: the radio names the event "
              "before anyone sees it, and the naming changes as the danger is reassessed, so that the "
              "language is a second disaster running alongside the first. The second is death, which "
              "the novel treats as a consumer problem - something to be feared, dosed, studied and "
              "sold. The third is the suburb as a system of consumption and waste, its supermarkets and "
              "its household products as the medium in which the family lives. The fourth is "
              "technology's ordinary violence, which the novel presents not as a takeover by machines "
              "but as the accidents of a system nobody is really running.",
  structure="The novel is in three parts and forty chapters; the Norton selection is Part Two, which "
            "runs from the sirens to the return home, and it moves in short scenes between the road, "
            "the camp and the family's conversation, with radio bulletins and public-address "
            "announcements set into the narrative.",
  style="Flat declarative sentences and a deadpan present tense; dialogue in which characters repeat the "
        "phrases of television, advertising and the news; lists of consumer goods used as a formal "
        "device; brand names treated as a natural part of speech; and a narrator who reports the "
        "uncanny without surprise.",
  ctx="Published by Viking in 1985 and awarded the National Book Award for Fiction in 1985. It appeared "
      "in the decade of Bhopal (1984) and Chernobyl (1986), and its chemical cloud belongs to that "
      "moment; the novel's campus setting draws on DeLillo's time at Bennington College, where he taught "
      "in the early 1980s. White Noise is generally taken as the book that brought the American "
      "postmodern novel into the academic canon, and its second part is the section most often "
      "anthologised.",
  sig="White Noise is DeLillo's best-known novel and one of the defining American books of the 1980s; "
      "its National Book Award marked the academy's recognition of the novel of media saturation, its "
      "second part is the standard anthology excerpt, and the phrase 'airborne toxic event' has passed "
      "into general American usage as a name for the industrial accident nobody predicted.",
  canon="Major canon",
  crit="Criticism reads the novel as the founding American text on media and simulation, and the "
       "'Airborne Toxic Event' as its demonstration that the disaster is inseparable from its "
       "reporting; the family's 'toxic' consumer life, the Hitler studies satire and the Dylar plot "
       "have each produced substantial literatures, and the novel is regularly paired with "
       "Baudrillard and with the systems fiction of Pynchon.",
  biblio="First published by Viking Press in New York in 1985; the National Book Award for Fiction, "
         "1985; the Norton selection is Part II, 'The Airborne Toxic Event'. A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The novel is recorded as one work with the Norton excerpt noted in the bibliography statement, "
        "following the convention set for other excerpts. The book was not read in a copy of the first "
        "edition for this record; the plot is recorded from the critical and reference sources read.",
  ver="partially verified", sources=[W_DD, W_WN, NAAL]),
W10("Entropy", TP, "1960", "Short story (science-fiction and social satire)", "significant",
  genres=G("Short Story", "Postmodern Fiction", "Science Fiction"),
  themes=T("Alienation, absurdity and existential freedom", "Technology, media and consumer society",
           "Utopia, dystopia and imagined futures"),
  movements=M(PM, "New Wave Science Fiction"),
  overview="'Entropy' was first published in The Kenyon Review for Spring 1960, when Pynchon was "
           "twenty-two and still at Cornell, and was collected in Slow Learner (1984). It is set in two "
           "adjacent apartments and moves between two parties: a rooftop gathering in a leaky "
           "Washington apartment building, and a sealed room on the floor below where a man named "
           "Callisto lives with his lover in a self-imposed bubble. The story takes the second law of "
           "thermodynamics as its governing metaphor and applies it to a culture.",
  content="The story opens with Meatball Mulligan's lease-breaking party on the fourth floor of a "
          "Washington apartment building in the early 1960s: sailors, girls, a jazz record, a "
          "refrigerator full of gin. Below, in a hermetically sealed apartment kept at a constant "
          "temperature, Callisto and Aubade live inside a structure of his own making, and Callisto "
          "explains to her his theory that the world is moving towards 'heat-death', the state in which "
          "all energy is evenly distributed and no work is possible. He has built an 'entropic' "
          "situation on purpose: a sealed room where nothing can happen. The story cuts between the "
          "two floors, and the party's noise begins to penetrate the sealed room as a bird trapped in "
          "the ventilation; the two worlds blur. It ends with Meatball deciding to bring a "
          "representative of the other tenants to the party, and with the party - the human world of "
          "noise and disorder - beginning to invade the sealed room.",
  summary="'Entropy' is a story built on a single scientific metaphor, and its interest is in how "
          "literally Pynchon takes it. Callisto's sealed apartment is an experiment in achieving "
          "equilibrium - the condition in which no further change is possible - and it is also a "
          "satire of the intellectual who withdraws from history into a constructed system. Meatball's "
          "party is the opposite: a mess of noise, alcohol and bodies that cannot be sealed. The story "
          "sets the two against each other and lets the second invade the first, which is the comic "
          "turn: entropy wins, but not in the way Callisto predicted. The prose is already the prose of "
          "the novels - long sentences, technical vocabulary used casually, jokes that depend on "
          "knowing what a Lagrangian is - and the two settings are the two poles of Pynchon's whole "
          "career: the engineered system and the uncontrollable crowd. It is an apprentice work, and "
          "Pynchon said so in the introduction he wrote for Slow Learner twenty-four years later, "
          "calling it 'a good deal of baloney' and an example of 'the kind of writing I was doing "
          "then'; but it is the seed of everything he wrote afterwards.",
  themes_text="The first subject is entropy - the second law of thermodynamics - used as a metaphor for "
              "culture, history and personal life, and taken seriously enough to generate a plot. The "
              "second is the sealed room, and the intellectual's desire to build a system that history "
              "cannot reach. The third is the party: the unsealed, noisy, bodily world that refuses "
              "equilibrium. The fourth is the relation between them, which the story stages as a "
              "physical pressure - the noise coming through the floor - rather than as an argument.",
  structure="A short story of about twenty pages that alternates between two adjacent settings, the "
            "rooftop party and the sealed apartment, with a third strand in which a bird enters the "
            "ventilation system; the strands converge without fully joining.",
  style="Long sentences with a technical and colloquial mix; dialogue among the party's guests in "
        "period slang; scientific vocabulary used without explanation; and a narrator who is amused by "
        "his own characters.",
  ctx="Published in The Kenyon Review, Spring 1960, and collected in Slow Learner (1984), where Pynchon "
      "added the introduction that remains his most extended autobiographical statement. The story was "
      "written while he was at Cornell and before his Navy service and Boeing; the cold-war Washington "
      "setting and the thermodynamic conceit belong to the moment when American writers were beginning "
      "to use science as a structure of metaphor rather than as a subject.",
  sig="'Entropy' is the Pynchon story most often anthologised and the standard introduction to his "
      "work for students, because it contains in miniature the two settings - the engineered system and "
      "the uncontrolled crowd - that his novels elaborate. It is a standard text in courses on "
      "postmodern fiction and on the use of science in literature.",
  canon="Secondary canon",
  crit="Criticism treats the story as the apprentice piece that establishes Pynchon's thermodynamic "
       "imagination, and reads Callisto as a satire of the system-builder that his later novels would "
       "make sympathetic; the story's relation to the New Wave science fiction of the 1960s and to "
       "Pynchon's own later dismissal of it in Slow Learner are both standard topics.",
  biblio="First published in The Kenyon Review, Spring 1960; collected in Slow Learner (Little, Brown, "
         "1984). A selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The Kenyon Review issue and season are recorded from the several accounts of the story's "
        "publication; the story was not read in the original periodical for this record.",
  ver="partially verified", sources=[W_TP, W_ENT, NAAL]),
W10("Cathedral", RC, "1981", "Short story (first-person narrative)", "significant",
  genres=G("Short Story", "Realist Fiction"),
  themes=T("Class, labour and social mobility", "Family, marriage and domestic life",
           "Art, the artist and the creative life"),
  movements=M(MIN),
  overview="'Cathedral' was first published in The Atlantic Monthly for September 1981, was collected in "
           "The Best American Short Stories 1982, and became the title story of Cathedral (New York: "
           "Alfred A. Knopf, 1983). It is narrated by a man whose wife has invited a blind friend, "
           "Robert, to stay the night, and it describes an evening in which the narrator's suspicion "
           "and condescension are undone by an act of shared drawing.",
  content="The narrator, unemployed and at home in the American Northwest, tells the story of the visit "
          "in a flat, defensive voice: he has never met Robert, a blind man who worked with his wife "
          "years earlier and whose voice has been on tapes they have exchanged for a decade. The "
          "narrator's account is full of casual prejudice - he assumes the man will be dull, that his "
          "wife's former marriage was a mistake, that blindness is a kind of absence - and the story "
          "lets him expose himself without comment. Robert arrives, eats a large dinner, smokes, and "
          "watches television with the family. Late in the evening, with the wife asleep, a programme "
          "about cathedrals comes on, and the narrator cannot describe one. Robert asks him to draw "
          "one, then puts his hand over the narrator's as he draws, and the story ends with the "
          "narrator's eyes still closed, feeling the paper, 'with my eyes still closed'.",
  summary="'Cathedral' is the story in which Carver's later manner arrives, and its method is "
          "withholding. The narrator's voice is so complete - so full of unearned certainty - that the "
          "story can dispense with commentary; the reader hears the prejudice in his own words and is "
          "never told what to think about it. The ending is the only moment in the story where "
          "something happens that the narrator cannot describe, and that is exactly why it works: the "
          "man who has narrated everything with confidence is left with his eyes closed, and the story "
          "stops there rather than telling us what he understood. Carver said that in writing it he "
          "knew he had 'gone as far the other way as I could or wanted to go, cutting everything down "
          "to the marrow', and the story is the hinge between the severe minimalism of What We Talk "
          "About When We Talk About Love and the more expansive manner of his last books. The drawing "
          "scene - two men with their hands on a sheet of paper, one of them blind - is one of the "
          "best known endings in American short fiction, and its power comes from the fact that the "
          "story has spent twenty pages establishing how little the narrator could see.",
  themes_text="The first subject is blindness, both literal and figurative, and the story is careful to "
              "let the literal blindness belong to the man who sees more. The second is class: the "
              "narrator's defensiveness is the defensiveness of a man without work, in a house his "
              "wife's salary sustains. The third is the ordinary American domestic evening - the "
              "television, the dinner, the drinks - used as the entire stage. The fourth is art, which "
              "arrives not as an object but as an act of shared attention, and which is the only thing "
              "in the story that the narrator cannot talk his way out of.",
  structure="A single first-person narrative in the past tense, without scene breaks, covering one "
            "evening from the narrator's waiting for the visit to the final drawing; the ending is a "
            "single closing gesture rather than a resolution.",
  style="Short sentences and a flat, colloquial first person; dialogue that reproduces ordinary speech "
        "including its repetitions and failures; very little metaphor; and an ending that withholds "
        "the character's realisation.",
  ctx="Published in The Atlantic Monthly in September 1981 and collected in Cathedral (Knopf, 1983), "
      "which was nominated for the National Book Critics Circle Award and the Pulitzer Prize. Carver "
      "was in the last years of his life when the collection appeared, and the story's movement away "
      "from the severe cuts of Gordon Lish's editing of the previous book is part of its history; the "
      "unedited manuscripts published after Carver's death have changed how the story is read.",
  sig="'Cathedral' is probably the most anthologised American short story of the last forty years and "
      "the one most often used to teach the form; it is a set text in courses on American fiction and "
      "on the short story, and its ending is one of the standard examples of the contemporary "
      "epiphany.",
  canon="Secondary canon",
  crit="Criticism reads the story as the turning point in Carver's style and as an instance of what has "
       "been called his 'post-minimalist' manner; the role of Gordon Lish in shaping Carver's earlier "
       "stories has made the story central to the argument about editing and authorship, and its "
       "treatment of blindness has been discussed in disability studies as well as in formal "
       "criticism.",
  biblio="First published in The Atlantic Monthly, September 1981; collected in The Best American Short "
         "Stories 1982 and in Cathedral (New York: Alfred A. Knopf, 1983). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The Atlantic Monthly printing of September 1981 is recorded from the critical and reference "
        "accounts read; some of those accounts give March 1981, and the discrepancy is noted here "
        "rather than resolved. The collection date of 1983 follows the Knopf first edition.",
  ver="partially verified", sources=[W_RC, W_CATH, NAAL]),
W10("The Lesson", TCB, "1972", "Short story (first-person narrative)", "significant",
  genres=G("Short Story", "Realist Fiction", "Satirical Fiction"),
  themes=T("Class, labour and social mobility", "Childhood, adolescence and coming of age",
           "Race, racism and the struggle for civil rights"),
  movements=M(AAW),
  overview="'The Lesson' was published in Gorilla, My Love (New York: Random House, 1972), Toni Cade "
           "Bambara's first collection of stories. It is narrated by Sylvia, a girl of about nine, who "
           "is taken with her cousin and the other neighbourhood children by Miss Moore - the one woman "
           "on the block with a college degree - to a toy store on Fifth Avenue, and who works out for "
           "herself what the trip has been for.",
  content="The story opens with Miss Moore assembling the children on a summer day - 'back in the days "
          "when everyone was old and stupid or young and foolish and me and Sugar were the only ones "
          "just right' - and Sylvia's resentment of her is established at once: the woman is 'black as "
          "hell' and has 'nappy hair' and no makeup and is always organising something educational. The "
          "trip takes them in two cabs to F. A. O. Schwarz, where the children look at a toy sailboat "
          "that costs more than a thousand dollars, a clown that costs thirty-five, and a paperweight "
          "with a tiny glass sculpture inside. Sylvia reads the price tag, is furious, and refuses to "
          "give Miss Moore the satisfaction of an answer. The story ends on the walk back: Sugar says "
          "that the country must be 'a democracy if you ask me, equal and fair', and then breaks away "
          "to spend her money; Sylvia, left alone, thinks that 'nobody gonna beat me at nuthin'.",
  summary="'The Lesson' is a story about the education of a child who refuses to be educated in "
          "public, and its entire effect depends on the gap between what Sylvia understands and what "
          "she will admit. Bambara's narrator is one of the great voices in American short fiction: "
          "the grammar, the invective, the fierce loyalty to her own world are all rendered without a "
          "trace of the author's correction. The trip to the toy store is a lesson in the price of "
          "things, and the story's achievement is that it makes the reader feel the arithmetic - a "
          "thousand-dollar boat in a shop a cab ride from a neighbourhood where children count coins - "
          "as Sylvia feels it, as an insult rather than a statistic. The ending is deliberate: Miss "
          "Moore does not get her answer, Sugar does not get her lesson, and Sylvia, who has learned "
          "the most, says nothing. That withholding is Bambara's politics - the education has "
          "happened, but it belongs to the child, not to the teacher - and it is why the story has "
          "become a standard text in courses on American fiction and on the teaching of class.",
  themes_text="The first subject is class as it is learned by a child, through prices rather than "
              "through argument. The second is education and who controls it: Miss Moore is an outsider "
              "in her own neighbourhood because she has been to college, and the story is alive to the "
              "resentment that her benevolence provokes. The third is race and the city, since the "
              "distance between Harlem and Fifth Avenue is travelled in a cab and is a distance in "
              "history as much as in geography. The fourth is pride, which the story treats as a form "
              "of knowledge rather than as an obstacle to it.",
  structure="A single first-person retrospective narrative in the voice of a child, moving from the "
            "assembling of the children through the cab ride and the toy store to the walk home; the "
            "story's climax is a conversation overheard rather than an event.",
  style="First-person narration in Black vernacular, with the spelling and grammar rendered rather than "
        "corrected; heavy use of dialogue and of the narrator's commentary; comedy carried by "
        "invective; and an ending that withholds the narrator's conclusion.",
  ctx="Published in Gorilla, My Love (Random House, 1972), Bambara's first collection, and set in the "
      "Harlem and Brooklyn of her own childhood. The story belongs to the Black Arts and Black feminist "
      "writing of the early 1970s, and to a moment when American short fiction was beginning to record "
      "the speech of Black neighbourhoods without translation.",
  sig="'The Lesson' is the most anthologised story Bambara wrote and one of the standard texts of the "
      "American short story of the 1970s; it is taught in courses on American fiction, on the "
      "literature of class and on Black women's writing, and its narrator's voice is regularly cited "
      "as a model of vernacular narration.",
  canon="Secondary canon",
  crit="Criticism reads the story as a study of the pedagogy of class and as an instance of Bambara's "
       "vernacular method; the figure of Miss Moore has been discussed as a critique of middle-class "
       "uplift, and Sylvia's refusal to answer has been read as the story's own refusal to deliver a "
       "lesson to its reader.",
  biblio="First published in Gorilla, My Love (New York: Random House, 1972). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The collection, publisher and year are recorded from the catalogue and reference records "
        "read; the story was not read in a copy of the first edition for this record.",
  ver="partially verified", sources=[W_TCB, W_GORILLA, NAAL]),
W10("The Woman Warrior", MHK, "1976", "Memoir (five-part, talk-story form)", "major",
  genres=G("Nonfiction Prose (1946–2000)", "Memoir", "Autobiographical Novel"),
  themes=T("Gender, feminism and women's lives", "Migration, exile and diaspora",
           "Family, marriage and domestic life"),
  movements=M(AAM, SWF),
  overview="The Woman Warrior: Memoirs of a Girlhood Among Ghosts was published by Alfred A. Knopf in "
           "1976 and won the National Book Critics Circle Award for general nonfiction. It is in five "
           "parts - 'No Name Woman', 'White Tigers', 'Shaman', 'At the Western Palace' and 'A Song for "
           "a Barbarian Reed Pipe' - and it moves between the author's childhood in Stockton, "
           "California, her mother's talk-stories, and the Chinese legends her mother told. The Norton "
           "selection prints 'No Name Woman' and an excerpt from 'A Song for a Barbarian Reed Pipe'.",
  content="'No Name Woman' opens with the mother's warning, delivered as the daughter begins to "
          "menstruate: she must not tell anyone what she is about to be told. The story is of an aunt "
          "in China who became pregnant by a man the village never identified, gave birth alone in a "
          "pigsty after the village raided the house, and drowned herself and the baby in the family "
          "well; the family has since behaved as if she never existed. The narrator reconstructs the "
          "aunt's story from the fragments her mother gave her, offering several incompatible "
          "explanations - rape, seduction, love - and refusing to settle on one. 'White Tigers' "
          "recounts the legend of Fa Mu Lan, the woman warrior, and the narrator's childhood training "
          "in it. 'Shaman' tells of her mother's medical training in China and the ghosts she "
          "encountered there. 'At the Western Palace' concerns an aunt who came to America and found "
          "her husband had taken another wife. 'A Song for a Barbarian Reed Pipe' is about the "
          "narrator's own girlhood, her silence in American schools, and her final breaking of that "
          "silence against her mother.",
  summary="The Woman Warrior changed the American memoir by refusing to decide what kind of book it "
          "was. Its five parts are held together by the voice of the daughter and by the practice the "
          "book calls 'talk-story' - the Chinese American habit of telling a story that is not quite "
          "true in order to say something that is - and the book's most important formal decision is to "
          "leave the reader unable to tell which passages are remembered, which are invented and which "
          "are translated legend. 'No Name Woman', the section the Norton prints in full, is the "
          "clearest demonstration: the narrator gives three or four possible stories of her aunt and "
          "never chooses, and the refusal is the point, since the woman's history was erased and any "
          "single version would complete the erasure in a different way. Kingston's prose carries the "
          "cadence of her mother's speech into English, and the book's anger - at the village, at the "
          "family, at the American school system that kept her silent for years - is delivered without "
          "editorial comment. It is a founding text of Asian American literature, and it was also the "
          "centre of the decade's argument about authenticity, in which Frank Chin and others accused "
          "Kingston of falsifying Chinese tradition for a white readership. Both the book's formal "
          "originality and that argument are now part of its history.",
  themes_text="The first subject is the relation between a daughter and a mother whose stories are the "
              "daughter's only access to her history, and the book's method is to keep that relation "
              "unresolved. The second is silence: the girl who cannot speak in American classrooms, the "
              "aunt who is not spoken of, the women whose lives were not recorded. The third is "
              "migration and its erasures - the aunts left in China, the husbands who did not send for "
              "them, the paper identities of the exclusion era. The fourth is the making of a woman "
              "writer, which the book presents not as a triumph but as a series of refusals, ending "
              "with the daughter's song that is also her mother's.",
  structure="Five parts that can be read as essays, stories or chapters: 'No Name Woman', 'White "
            "Tigers', 'Shaman', 'At the Western Palace' and 'A Song for a Barbarian Reed Pipe'; the "
            "book's unity is carried by the narrating voice and by recurring images rather than by "
            "chronology.",
  style="A first-person prose that keeps the rhythm of spoken Chinese-influenced English; direct "
        "address to the reader and to the dead; abrupt movement between legend, memory and commentary; "
        "and a refusal to mark which is which.",
  ctx="Published by Alfred A. Knopf in 1976; 'No Name Woman' had appeared, in slightly different form, "
      "in Viva for January 1975, and the book's copyright page records that. It appeared in the decade "
      "of the Asian American movement and of the women's movement, and it was attacked from both "
      "directions - by Frank Chin and others for falsifying tradition, by some feminists for not being "
      "feminist enough - which is a measure of how directly it intervened in both arguments.",
  sig="The Woman Warrior is the founding text of Asian American literary memoir and one of the most "
      "widely taught American books of the period; its National Book Critics Circle Award, its decade "
      "of controversy and its influence on the memoirs and novels that followed make it indispensable, "
      "and the Norton Anthology prints two sections of it.",
  canon="Major canon",
  crit="Criticism treats the book as the central case in the argument over Asian American "
       "representation, as an experiment in genre that anticipated the mixed-form memoir of the 1980s "
       "and 1990s, and as a feminist text about silence and voice; the Chin-Kingston dispute is "
       "documented in Asian American literary history and is still taught as a debate about who owns a "
       "tradition.",
  biblio="First published by Alfred A. Knopf in New York in 1976; 'No Name Woman' appeared in slightly "
         "different form in Viva, January 1975. The Norton selection prints 'No Name Woman' and an "
         "excerpt from 'A Song for a Barbarian Reed Pipe'. A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The book is recorded once for both of its Norton selections, following the convention set for "
        "excerpts. The copyright page gives the Viva printing of January 1975; the first edition was "
        "not read for this record.",
  ver="partially verified", sources=[W_MHK, W_WW, NAAL]),
W10("Lullaby", LMS, "1974", "Short story (third-person narrative)", "significant",
  genres=G("Short Story", "Realist Fiction"),
  themes=T("Indigenous survival, land and sovereignty", "Death, illness and mourning",
           "Land, place and regional belonging"),
  movements=M(NAR),
  overview="'Lullaby' was first published in Laguna Woman (1974), Leslie Marmon Silko's first book, a "
           "collection of poems and stories, and was collected in Storyteller (1981). It is set in the "
           "winter of the 1970s in the American Southwest and concerns an old Navajo woman, Ayah, and "
           "her husband Chato, and the losses that have accumulated over their marriage.",
  content="Ayah is old and blind in one eye and lives with Chato, a Mexican American who worked for "
          "years for the white ranchers, in a shack on land that has passed out of their hands. Their "
          "children have been taken from them: two died in infancy, one son was killed in the Korean "
          "War, and the others were taken by the authorities - the narrator remembers the day the "
          "white men came and took the children away while Chato was away. The story moves in "
          "Ayah's memory between these losses and the present, in which she and Chato are travelling "
          "towards the town in the snow; Chato drinks and then disappears into a storm, and Ayah goes "
          "to look for him. She finds him in the snow and lies down beside him, and the story closes "
          "with her singing a lullaby in Navajo, the song she sang to her infants, as she covers him "
          "and herself against the cold.",
  summary="'Lullaby' is a story of accumulated dispossession told without a single accusatory sentence, "
          "and its restraint is what makes it unbearable. Silko gives the facts - the children taken, "
          "the land lost, the husband dying - in the order in which Ayah remembers them rather than in "
          "chronological order, so that the reader assembles the history at the same time as the "
          "character relives it. The white men who took the children are described only as they "
          "appeared to a woman who did not understand their language, which both limits the reader's "
          "access to the scene and makes the scene's violence feel arbitrary, as it must have felt. "
          "The ending, in which Ayah lies down in the snow beside her dying husband and sings the "
          "lullaby, is one of the most famous in Native American fiction: it is not a surrender, "
          "because the song is an act of survival, carrying the language and the memory forward even as "
          "the body gives up. Silko's prose here is plain and unhurried, closer to the oral tradition "
          "she was raised in than to the contemporary short story, and that is the story's argument as "
          "well as its form.",
  themes_text="The first subject is the removal of Native children, which the story presents as the "
              "central violence of the twentieth century and records without editorialising. The second "
              "is land: the shack, the land that has gone out of the family's hands, the snow - all "
              "given as the substance of a life rather than as a setting. The third is language, since "
              "Ayah's Navajo is a world the English-speaking authorities cannot enter, and the lullaby "
              "at the end is the story's assertion that something survives. The fourth is marriage, and "
              "the story's unsentimental picture of a union made under pressure and held together by "
              "endurance.",
  structure="A single short story that moves between Ayah's present (the drive into the snow) and her "
            "recollections, without scene breaks or dates; the movement between them is associative and "
            "the story's chronology has to be assembled by the reader.",
  style="Plain, unhurried third-person prose with almost no metaphor; dialogue rendered in Ayah's "
        "English and in Chato's; the landscape given in concrete physical detail; and an ending that "
        "resolves on an action rather than an explanation.",
  ctx="First published in Laguna Woman (1974), Silko's first book, which collected poems and short "
      "stories and was a small-press production; the story reached a wide readership through "
      "Storyteller (1981), the mixed-form book in which Silko set her stories alongside photographs "
      "and poems. The removal of Native children to boarding schools and foster care was a live "
      "political issue throughout the 1970s, and the Indian Child Welfare Act of 1978 was passed in "
      "the same years.",
  sig="'Lullaby' is one of the two or three most anthologised Native American short stories and the "
      "standard introduction to Silko's shorter work; it is taught in courses on Native American "
      "literature and on the American short story, and its ending is regularly cited as an example of "
      "how a story can hold grief and survival at once.",
  canon="Secondary canon",
  crit="Criticism reads the story as a study of child removal and of the survival of language, and "
       "discusses its circular structure as an instance of the oral tradition's influence on Silko's "
       "form; it is usually paired with 'Ceremony' and with the stories of Storyteller, and the Navajo "
       "lullaby at the end has been the focus of the considerable body of work on Silko and song.",
  biblio="First published in Laguna Woman (Greenfield Center, NY: Greenfield Review Press, 1974); "
         "collected in Storyteller (New York: Little, Brown, 1981). A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E.",
  notes="The first publication in Laguna Woman (1974) is recorded from the bibliographic records of "
        "Silko's work; the story was not read in a copy of that edition for this record.",
  ver="partially verified", sources=[W_LMS, W_LAGUNA, NAAL]),
W10("Language and Literature from a Pueblo Indian Perspective", LMS, "1981",
  "Essay (lecture, prose)", "significant",
  genres=G("Literary Essay", "Cultural Criticism", "Personal Essay"),
  themes=T("Indigenous survival, land and sovereignty", "Language, writing and the limits of representation",
           "Myth, folklore and the supernatural"),
  movements=M(NAR),
  overview="'Language and Literature from a Pueblo Indian Perspective' is the text of a talk Silko gave "
           "at a conference at the State University of New York at Buffalo in 1979, published in the "
           "conference volume The First Words in 1981. It is the clearest statement she has given of "
           "how Pueblo storytelling works and of what happened to it when it met the written page, and "
           "it is the essay through which her poetics is most often taught.",
  content="Silko begins by explaining that she will not give a conventional paper, because the Pueblo "
          "way of speaking does not proceed by thesis and argument; instead she tells stories, and lets "
          "the stories carry the argument. She describes the structure of a Pueblo narrative - the way "
          "one story opens into another, the way the teller must know where every part of the "
          "community's history connects - and the importance of the audience, who may interrupt and "
          "who know the stories already. She gives examples: the story of the Laguna migration, the "
          "story of the gambler, and the story of how the people came up from the underworld. She then "
          "addresses the movement of oral narrative into English and into print, the loss that "
          "accompanies translation, and the continuance of the stories in new forms. She closes by "
          "telling the audience a story rather than concluding.",
  summary="The essay is a performance in prose, and its argument is carried by its own form: Silko "
          "refuses the conference paper's structure and demonstrates the Pueblo structure instead. The "
          "content is therefore inseparable from the way it is delivered - a point she makes explicit "
          "when she says that a Pueblo audience would already know the stories she is telling and would "
          "interrupt her, and that the non-Pueblo reader has to be told this, which is itself the "
          "subject of the essay. Her account of the oral tradition is precise rather than mystical: "
          "stories are not free-floating symbols but property, owned by families and clans, told at "
          "particular times, and their function is to keep the community's memory in working order. "
          "The essay's treatment of writing is generous and unsentimental - English is a language the "
          "Pueblo people have now, and the stories will change in it - and it closes with a story "
          "rather than a conclusion because a conclusion would be, in the essay's own terms, the wrong "
          "shape. It is the essay most often cited for the proposition that Native American literature "
          "is not a subject matter but a set of forms.",
  themes_text="The first subject is the structure of oral narrative - the way stories nest inside one "
              "another, the role of the audience, the ownership of stories - described from inside "
              "rather than as anthropology. The second is translation and loss, treated without "
              "nostalgia and without celebration. The third is community: the essay insists that a "
              "story belongs to people, not to a literature. The fourth is survival, which the essay "
              "presents as a matter of continuing to tell the stories in whatever language is "
              "available.",
  structure="A lecture that proceeds by anecdote and example rather than by argument, in numbered "
            "movements that correspond loosely to the parts of a Pueblo storytelling session, and "
            "closes with a story in place of a conclusion.",
  style="Spoken, unhurried prose with direct address to the audience; short declarative sentences set "
        "against long narrative ones; no footnotes or citations; and a deliberate refusal of academic "
        "vocabulary.",
  ctx="Delivered at a conference at the State University of New York at Buffalo in 1979 - the "
      "conference on Native American literature that also produced the volume The First Words (1981) - "
      "at a moment when Native American writers were beginning to define the field's terms for "
      "themselves. The essay is contemporaneous with Storyteller (1981) and shares that book's "
      "conviction that the oral tradition is a living form rather than a source.",
  sig="'Language and Literature from a Pueblo Indian Perspective' is the standard statement of Native "
      "American poetics by one of its central practitioners and is anthologised in the Norton "
      "Anthology, in collections of American essays and in course readers on Native American "
      "literature; it is the essay most often assigned alongside Momaday's The Way to Rainy Mountain "
      "and Silko's own fiction.",
  canon="Secondary canon",
  crit="Criticism reads the essay as the founding statement of a Pueblo aesthetics in English, and "
       "discusses its formal refusal of the academic paper as itself an argument about what counts as "
       "theory; it is regularly paired with Momaday's essays and with the work of Paula Gunn Allen on "
       "the sacred in Native American literature.",
  biblio="First published in The First Words: The Proceedings of a Conference on Native American "
         "Literature (1981) and collected in Yellow Woman and a Beauty of the Spirit: Essays on Native "
         "American Life Today (New York: Simon and Schuster, 1996). A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E.",
  notes="The Buffalo conference of 1979 and the 1981 volume are recorded from the accounts of the "
        "essay's publication; the exact conference title and the page numbers were not established "
        "from the sources consulted and are not stated above.",
  ver="partially verified", sources=[W_LMS, W_LAGUNA, NAAL]),
W10("Neo-HooDoo Manifesto", IR, "1972", "Poem-manifesto (prose and verse)", "significant",
  genres=G("Literary Manifesto", "Postmodern Poetry", "Satirical Fiction"),
  themes=T("Race, racism and the struggle for civil rights", "Art, the artist and the creative life",
           "Myth, folklore and the supernatural"),
  movements=M(PM, AAW),
  overview="'Neo-HooDoo Manifesto' is the opening statement of Conjure: Selected Poems 1963-1970 "
           "(Amherst: University of Massachusetts Press, 1972), and it is Reed's declaration of an "
           "aesthetic: a Black American art built on hoodoo - the African-derived folk magic of the "
           "American South - rather than on the European tradition, written in a mixture of manifesto "
           "prose, verse, parody and joke.",
  content="The piece declares that 'Neo-HooDoo' is 'the special deity' of the American Black, and "
          "proceeds through definitions, lists and satirical routines: hoodoo is opposed to the "
          "'Western aesthetic', to the museum, to the academy and to the idea of art as a separate "
          "realm. Reed names the practical sources - the conjure men, the church, the blues, the "
          "signifying tradition - and he attacks the institutions that have excluded Black art, "
          "including the publishing industry and the critics. The manifesto is deliberately "
          "self-contradictory: it asserts and denies in the same paragraph, uses the language of "
          "advertising and of the Old Testament interchangeably, and treats the reader as a participant "
          "in a performance rather than as a recipient of an argument.",
  summary="'Neo-HooDoo Manifesto' is one of the founding documents of the Black postmodern mode in "
          "American writing, and its strategy is to be a manifesto that makes fun of manifestos while "
          "making a real one. Reed's argument - that Black American culture has its own metaphysics, "
          "its own epistemology and its own procedures for making art, and that these are not "
          "decorative alternatives to the European tradition but its historical adversaries - is made "
          "in the form of a joke that keeps turning serious. The piece's typography and its switches "
          "of register are part of the argument: an aesthetic that cannot be contained in a paragraph "
          "of academic prose is expressed in a form that will not fit one. It belongs to the same "
          "moment as Mumbo Jumbo (1972), his novel of the Harlem Renaissance as a hoodoo conspiracy, "
          "and the two works together state the position that Reed has held for fifty years. It is a "
          "difficult text to anthologise precisely because it depends on performance, and its presence "
          "in the Norton selection is a measure of how central that difficulty has become to the "
          "American canon.",
  themes_text="The first subject is the existence of an African-derived American aesthetics, argued as "
              "a matter of fact rather than as a claim for recognition. The second is the Western art "
              "institution, which the manifesto treats as a rival religion with its own priests. The "
              "third is parody as method: the manifesto's jokes are not decoration but argument, since "
              "a form that cannot be taken seriously by the academy is exactly the form Reed wants. "
              "The fourth is the reader, who is addressed as an audience at a performance and thereby "
              "made responsible for the piece's completion.",
  structure="A short, discontinuous text in sections of prose and verse that has no continuous "
            "argument and ends without a conclusion; its unity is carried by the voice and by "
            "recurring terms.",
  style="A mixture of manifesto prose, verse, parody, catalogue and joke; deliberate "
        "self-contradiction; typographic play; a vocabulary drawn from hoodoo, the church, advertising "
        "and the academy; and a tone that is never entirely straight.",
  ctx="Published at the head of Conjure: Selected Poems 1963-1970 (University of Massachusetts Press, "
      "1972), at the height of Reed's involvement with the Black Arts Movement, and in the same year "
      "as Mumbo Jumbo. Reed's Neo-HooDoo aesthetic was developed across those two books and the "
      "Yardbird anthologies he edited from 1973, and it was offered as an alternative to both the "
      "Black Arts Movement's nationalism and the white avant-garde's experimentalism.",
  sig="'Neo-HooDoo Manifesto' is the statement of the aesthetic that made Reed the most consistently "
      "inventive Black American postmodernist and is a standard anthology text in courses on African "
      "American literature and on the American postmodern; its influence is visible in the fiction of "
      "Paul Beatty, Colson Whitehead and the writers of the twenty-first century who treat Black "
      "history as a store of forms to be recombined.",
  canon="Secondary canon",
  crit="Criticism treats the manifesto as the founding text of Neo-HooDoo and reads it alongside Mumbo "
       "Jumbo as a single project; its relation to the Black Arts Movement, which Reed supported while "
       "refusing its orthodoxies, and to the postmodern novel's use of the archive are the standard "
       "topics.",
  biblio="Published at the head of Conjure: Selected Poems 1963-1970 (Amherst: University of "
         "Massachusetts Press, 1972). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The volume, publisher and year are recorded from the catalogue records of Conjure; the piece "
        "was not read in a copy of that edition for this record.",
  ver="partially verified", sources=[W_IR, W_CONJURE, NAAL]),
W10("Hunger of Memory", RR, "1982", "Memoir (six-part essay sequence)", "major",
  genres=G("Nonfiction Prose (1946–2000)", "Memoir", "Personal Essay"),
  themes=T("Class, labour and social mobility", "Migration, exile and diaspora",
           "Education, institutions and the academy"),
  movements=M(),
  overview="Hunger of Memory: The Education of Richard Rodriguez was published by David R. Godine in "
           "1982. It is in six parts - a prologue, 'Aria', 'The Achievement of Desire', 'Credo', "
           "'Complexion' and 'Profession' - and it is an autobiography of assimilation told as an "
           "argument against the politics of assimilation. The Norton selection prints an excerpt.",
  content="'Aria' describes the Rodriguez family's life in Sacramento in the 1950s, when the children "
          "spoke Spanish at home and English was a public language, and the day the nuns came to the "
          "house to ask the parents to speak English to their children; the chapter is about the "
          "silence that followed, and the loss of the family's intimate speech. 'The Achievement of "
          "Desire' is an account of his education, built around his reading of Richard Hoggart's The "
          "Uses of Literacy and his recognition of himself in the figure of the 'scholarship boy' who "
          "is educated away from his family. 'Credo' describes his Catholicism and his refusal of the "
          "communal, ritual church for a private faith. 'Complexion' concerns his dark skin and the "
          "shame it caused him and his family. 'Profession' describes his refusal of a professorship "
          "and his decision to write instead.",
  summary="Hunger of Memory is a memoir that argues, and its argument is uncomfortable by design. "
          "Rodriguez presents his own success - Stanford, Columbia, a Berkeley PhD programme - as a "
          "series of losses, and he refuses the consolations that the genre of the immigrant "
          "autobiography normally supplies: there is no reconciliation with the family, no recovery of "
          "Spanish, no return to the community that made him. The book's most quoted sentence, that "
          "the scholarship boy 'cannot afford to think about himself', is a description of a class "
          "position as much as a psychological one. Its political intervention was to refuse the label "
          "of minority writer while claiming the experience of one, and to argue that bilingual "
          "education and affirmative action had, in his own case, cost more than they gave; those "
          "arguments made him famous and made him the target of sustained criticism from Mexican "
          "American writers. The prose is formal and deliberate, closer to the nineteenth-century essay "
          "than to the confessional memoir of the 1970s, and the book's design - six essays rather than "
          "a chronology - is itself an argument that a life is best understood as a set of "
          "propositions. The book's refusal to be grateful is what has kept it alive: it declines to turn "
          "its author's success into a story the reader can be comforted by, and it declines, "
          "equally, to apologise for it.",
  themes_text="The first subject is language and the private/public split, which the first chapter "
              "establishes as the book's founding loss. The second is education as a form of class "
              "migration and the guilt that accompanies it. The third is religion, which Rodriguez "
              "treats as a private structure of meaning rather than as a community. The fourth is race "
              "and colour within a family and a society, in the chapter on complexion. The fifth is the "
              "public argument about affirmative action and bilingual education, which the book "
              "intervenes in directly.",
  structure="A prologue and five chapters - 'Aria', 'The Achievement of Desire', 'Credo', 'Complexion' "
            "and 'Profession' - each an essay that can stand alone and that is ordered thematically "
            "rather than chronologically.",
  style="Formal, periodic, essayistic prose with a strong first person; quotation and allusion used as "
        "evidence; a refusal of the confessional register; and endings that refuse the resolution the "
        "reader expects.",
  ctx="Published by David R. Godine in Boston in 1982, at a moment when bilingual education and "
      "affirmative action were the central arguments of American racial politics, and when the "
      "Mexican American literary renaissance was producing its first major memoirs. The book's "
      "intervention in those arguments - from a position that was read as a rejection of the "
      "community it described - made it one of the most discussed American memoirs of the decade.",
  sig="Hunger of Memory is one of the foundational American memoirs of the period and the book that "
      "made assimilation a public argument for a Mexican American writer; it is a standard text in "
      "courses on American autobiography, on Chicano literature and on the politics of education, and "
      "the debate it provoked remains part of the literature.",
  canon="Major canon",
  crit="Criticism reads the book as the central case in the argument over assimilation and as an "
       "instance of the essay sequence as autobiography; Mexican American and Chicano critics have "
       "attacked its politics while acknowledging its literary force, and the book is routinely paired "
       "with Gloria Anzaldúa's Borderlands as the two poles of Mexican American writing about "
       "language in the period.",
  biblio="First published by David R. Godine in Boston in 1982; the Norton selection is an excerpt. A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The book is recorded as one work with the Norton excerpt noted, following the convention set "
        "for excerpts. The first edition was not read for this record; the chapter titles are from the "
        "book's contents as recorded by the sources consulted.",
  ver="partially verified", sources=[W_RR, W_HOM, NAAL]),
]
