"""Installment 9: the satirist-journalist, the Ulster critic and the Manchester School (authors, part 22)."""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _lib import A  # noqa: F401

MAJ = "Major / canonical"
SEC = "Significant / secondary"
MIN = "Minor / lesser-known"
OBS = "Obscure / historically neglected"

AUTHORS = [
A("Malcolm Muggeridge", SEC, "1903", "1990", "Sanderstead, Surrey, England",
  "British; the satirical journalist of the thirties and the Moscow correspondent",
  "Journalist, satirist and novelist; the author of Winter in Moscow and The Thirties.",
  "Born Thomas Malcolm Muggeridge at Sanderstead, Surrey, on 24 March 1903, the son of the Labour politician H. T. Muggeridge; he grew up in Croydon, read natural sciences at Selwyn College, Cambridge, taught English literature at Union Christian College in the Kingdom of Cochin, India, and then in Egypt, where Arthur Ransome recommended him to the Manchester Guardian. He went to Moscow for the paper in 1932; his reports of the famine in Ukraine were printed anonymously in March 1933, and his novel Picture Palace, drawn from his years at the Guardian, was published in 1934 but not distributed for fear of libel. Winter in Moscow (1934), The Earnest Atheist (1936), a study of Samuel Butler, In a Valley of This Restless Mind (1938) and The Thirties (1940) followed. He served as a soldier and intelligence officer in East Africa and Paris during the Second World War, was deputy editor of the Daily Telegraph (1950-53), converted to Christianity under the influence of Hugh Kingsmill and later became a Roman Catholic, and died in Hastings on 14 November 1990.",
  "Malcolm Muggeridge was a satirical journalist of the thirties: his anonymous Manchester Guardian reports of March 1933 were, with Gareth Jones's, among the accounts that confirmed the extent of the famine in Ukraine, and Winter in Moscow satirised the Western journalists who took an uncritical view of the Soviet regime.",
  "The satirical sentence of the journalist with the moralist's edge; the Moscow satire; the social survey of the decade in The Thirties; the broadcast voice of the later years; the ridicule carried by the Christian conscience.",
  "The Soviet regime and its Western admirers; the famine and its reporting; the newspaper world; the social history of the thirties; the pilgrim's road of the later conversion.",
  "Malcolm Muggeridge was a satirical journalist of the thirties: his famine reports of 1933 and Winter in Moscow (1934) set him against the uncritical Western reporting of the Soviet regime, and his later career ran from the Daily Telegraph and Punch to religious broadcasting.",
  infl=["Hugh Kingsmill"],
  alt=["Thomas Malcolm Muggeridge"],
  also=["Three Flats: A Play in Three Acts (1931)",
        "Picture Palace (1934; withdrawn for fear of libel, reissued 1987)",
        "La Russie (pamphlet in French, Paris, c. 1934)",
        "The Earnest Atheist: A Study of Samuel Butler (1936)",
        "In a Valley of This Restless Mind (1938)",
        "The Thirties, 1930-1940, in Great Britain (1940)",
        "unsigned reports on the famine in the Manchester Guardian (25, 27 and 28 March 1933)"]),

A("St John Ervine", SEC, "1883", "1971", "Belfast, Ireland",
  "Irish; the Ulster playwright of John Ferguson and the Abbey's manager",
  "Playwright, novelist and critic; the Ulster dramatist of Jane Clegg and John Ferguson.",
  "Born St John Ervine at Belfast on 1 February 1883; he worked in London insurance and journalism before the plays of Jane Clegg (1913) and John Ferguson (1915) made him the Ulster dramatist of the new drama, and the novel Mrs. Martin's Man (1914) carried the same country into the fiction. He managed the Abbey Theatre in 1915-16, served in the war and was wounded on the Somme, became the Observer's dramatic critic and one of the century's most combative reviewers, and wrote the great life of his friend Bernard Shaw; he died at Oxfordshire on 14 June 1971.",
  "St John Ervine is the Ulster playwright of the new drama: John Ferguson, with its Bible on the table and its avenger from America, is the classic play of the Ulster conscience, Jane Clegg made the deserted wife a figure of the suffrage stage, and his Abbey management and his criticism carried the same combative conscience into the institutions.",
  "The plain Ulster dialogue of the farmhouse and the chapel; the conscience and its scripture in the dramatic argument; the critic's combative sentence; the Shaw of the biography; the moral passion of the new drama without its subtlety.",
  "Ulster and its conscience; the scripture and the revenge; the deserted wife and the suffrage stage; the Abbey and its management; Shaw and the friendship of the biography.",
  "St John Ervine is the Ulster playwright of the new drama: John Ferguson is the classic play of the Ulster conscience and Jane Clegg made the deserted wife a figure of the suffrage stage.",
  infl=["Ulster nonconformity", "Bernard Shaw", "the new drama of the repertories", "the Abbey Theatre"],
  alt=["St. John Ervine", "St John Greer Ervine"],
  also=["Bernard Shaw: His Life, Work and Friends (1956)", "the Observer criticism", "the Abbey management of 1915-16"]),

A("Githa Sowerby", SEC, "1876", "1970", "South Shields, County Durham, England",
  "British; the playwright of Rutherford and Son and the children's author",
  "Playwright and children's author; the author of Rutherford and Son.",
  "Born Katharine Githa Sowerby at South Shields on 6 October 1876, of the glass-making family of the Tyne; she published children's books and verse before Rutherford and Son (1912), produced at the Vaudeville under her initials K. G. Sowerby and quickly revealed to be the work of a woman, made her the playwright of the Edwardian stage. The Stepmother (1924) and the later plays and children's books followed; she died at Oxford on 30 June 1970.",
  "Githa Sowerby is the playwright of Rutherford and Son: the old glassmaster, his children and the stolen design made the patriarchal tyranny and the woman's escape one of the great plays of the Edwardian stage, and the century's revival made her the recovered dramatist of the suffrage generation.",
  "The plain dialogue of the provincial household and the works; the patriarch's tyranny in the glass trade; the woman's escape and the price of the design; the children's book and the verse beside the plays; the Edwardian problem play with the woman's question at its centre.",
  "The patriarchal household and its tyranny; the glass trade and the family firm; the woman's work and the escape; the children's books and the recovered play; South Shields and the industrial north-east.",
  "Githa Sowerby is the playwright of Rutherford and Son: the glassmaster's tyranny and the woman's escape made one of the great plays of the Edwardian stage, and the century's revival recovered her for the suffrage canon.",
  infl=["the glass-making family of the Tyne", "Ibsen and the new drama", "the suffrage stage", "the children's book tradition"],
  alt=["Katharine Githa Sowerby", "K. G. Sowerby"],
  also=["A Man and Some Women (1923)", "the children's books of the K. G. Sowerby name"]),

A("Elizabeth Baker", SEC, "1876", "1962", "London, England",
  "British; the playwright of Chains and of the clerks' London",
  "Playwright; the author of Chains and the realist dramas of the lower middle class.",
  "Born Elizabeth Baker in London on 20 August 1876; she worked as a typist while writing plays, and Chains (1909) - first performed at the Court Theatre and then in the Duke of York's repertory season - made the obscure office worker one of the most discussed playwrights in England. Her dozen produced plays kept to the clerks, the shopgirls and the suburban strivers - The Price of Thomas Scott (1913) at the Gaiety, Manchester, Partnership (1917) at the Court - and she continued her typing through the success; she died on 8 March 1962.",
  "Elizabeth Baker is the playwright of the clerks' London: Chains, with its suburban couple, the dream of Australia and the return to the routine, is the landmark realist play of the lower middle class, and her repertory plays carried the typist's own knowledge of the office and the suburb onto the new drama's stage.",
  "The plain exact dialogue of the clerk and the shopgirl; the suburb, the office and the routine of the lower middle class; the moral dilemma in the small decision; the woman's knowledge of the typist's world; the new drama's realism without its propaganda.",
  "The clerks and the shopgirls of the Edwardian city; the suburb and its chains; the dream of escape and the return; the woman's work and the typist's life; the repertory theatres of Manchester and the Court.",
  "Elizabeth Baker is the playwright of the clerks' London: Chains is the landmark realist play of the lower middle class, and her repertory plays carried the typist's knowledge of the office onto the new drama's stage.",
  infl=["the typist's office", "the repertory movement", "Ibsen and the new drama", "Annie Horniman's Gaiety"],
  alt=["Elizabeth Baker"],
  also=["Miss Tassey (1910)", "Edith (1912)", "Bert's Girl (1927)"]),

A("Stanley Houghton", SEC, "1881", "1913", "Ashton-under-Lyne, Lancashire, England",
  "British; the Manchester School playwright of Hindle Wakes",
  "Playwright; the author of Hindle Wakes and The Younger Generation.",
  "Born Stanley Houghton at Ashton-under-Lyne on 19 February 1881; he worked in the Manchester textile trade and wrote for the Manchester Guardian before the repertory of Annie Horniman's Gaiety Theatre produced his plays. Hindle Wakes (1912), with Fanny Hawthorn's holiday week and its refusal of marriage, made him the playwright of the Lancashire new drama, and The Younger Generation (1912) followed; his career of the Manchester School was cut short by his death at Manchester on 4 December 1913.",
  "Stanley Houghton is the Manchester School's greatest playwright: Hindle Wakes - Fanny Hawthorn, the mill-owner's son and the holiday week - made the Lancashire working woman's refusal of the respectable marriage one of the new drama's most famous scenes, and the play's revivals have kept it on the stage for a century.",
  "The plain Lancashire dialogue of the mill and the terrace; the working woman's independence in the holiday week; the generational conflict of the factory family; the Manchester repertory's realism; the comedy carried by the dialect and the moral.",
  "The Lancashire mill town and its classes; the working woman and the refusal of marriage; the younger generation against the old; the holiday week and the pleasure resort; the Manchester School and the repertory.",
  "Stanley Houghton is the Manchester School's greatest playwright: Hindle Wakes made the Lancashire working woman's refusal of the respectable marriage one of the new drama's most famous scenes.",
  infl=["the Manchester textile trade", "Annie Horniman's Gaiety Theatre", "Ibsen and the new drama", "the Lancashire dialect"],
  alt=["Stanley Houghton"],
  also=["The Perfect Cure", "Independent Means", "Partners", "Marriages in the Making"]),

A("Allan Monkhouse", MIN, "1858", "1936", "Bowdon, Cheshire, England",
  "British; the Manchester Guardian critic and the playwright of Mary Broome",
  "Playwright, critic and poet; the author of Mary Broome and the Guardian's art critic.",
  "Born Allan Monkhouse at Bowdon, Cheshire, on 27 April 1858; he worked in the Manchester timber trade while writing verse and criticism, became an art and drama critic for the Manchester Guardian, and wrote the one-act plays of the repertory - Mary Broome (1911) and Nothing Like Leather (1913) among them - that put the class question and the woman's emancipation on the Manchester stage. He died in 1936.",
  "Allan Monkhouse is the critic-playwright of the Manchester School: Mary Broome, the servant's play of the class and the marriage, made him the Guardian critic whose own one-acts stood beside Houghton's at the Gaiety, and his criticism recorded the Manchester repertory from within.",
  "The plain dialogue of the servant's hall and the drawing room; the class question in the one act; the woman's emancipation of the Edwardian stage; the critic's eye in the playwright's scene; the Manchester repertory's economy of the short form.",
  "The servant and the class question; the marriage and the woman's emancipation; the Manchester repertory and the Gaiety; the Guardian's criticism; the one-act play as the form of the new drama.",
  "Allan Monkhouse is the critic-playwright of the Manchester School: Mary Broome put the servant's class question and the woman's emancipation on the Gaiety stage beside Houghton's plays.",
  infl=["the Manchester Guardian", "Annie Horniman's Gaiety Theatre", "Ibsen", "the Manchester timber trade"],
  alt=["Allan Monkhouse"],
  also=["The Choice (1910)", "the Guardian's art and drama criticism", "collected verse"]),
]
