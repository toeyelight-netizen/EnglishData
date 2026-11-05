"""Audit author coverage for a given period against the master database.

Compares a curated canon list for an installment's period against
``authors.full_name`` plus ``authors.alternative_names``, using surname +
initial matching so that "W. Somerset Maugham" matches "Somerset Maugham"
and "H. G. Wells" matches "Herbert George Wells".

Usage:
    python3 scripts/audit_coverage.py 08
    python3 scripts/audit_coverage.py 09 --starts-with W
    python3 scripts/audit_coverage.py 09 --quiet      # exit 1 if gaps remain
"""

import argparse
import os
import re
import sqlite3
import sys
import unicodedata

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, "database", "English_Literature_Master.db")

# ------------------------------------------------------------------ canons
# Installment 8: Victorian Britain and the American nineteenth century after
# 1832. Names already imported are deliberately included: the probe must show
# them as present, which is what proves the matcher works.
I08 = """
Charles Dickens|William Makepeace Thackeray|Charlotte Bronte|Emily Bronte|Anne Bronte
George Eliot|Elizabeth Gaskell|Anthony Trollope|Mark Twain|William Dean Howells|Henry James
Sarah Orne Jewett|Kate Chopin|Charlotte Perkins Gilman|Booker T. Washington|Charles W. Chesnutt
Paul Laurence Dunbar|Louisa May Alcott|Rebecca Harding Davis|Elizabeth Stuart Phelps
Frances E. W. Harper|Harriet E. Wilson|William Wells Brown|Anna Julia Cooper|Ida B. Wells
Bret Harte|Joel Chandler Harris|Algernon Charles Swinburne|William Morris|Arthur Symons
Ernest Dowson|Lionel Johnson|John Davidson|Francis Thompson|Michael Field|Margaret Oliphant
Charlotte M. Yonge|Dinah Mulock Craik|Eliza Lynn Linton|Mary Augusta Ward|H. Rider Haggard
George Moore|Israel Zangwill|Sarah Grand|Mona Caird|Edward Bulwer-Lytton|Benjamin Disraeli
George Bernard Shaw|Edward Lear|A. E. Housman|J. M. Barrie|Jerome K. Jerome|Stephen Crane
Frank Norris|Jack London|Edith Wharton|Ambrose Bierce|Hamlin Garland|George Washington Cable
Mary E. Wilkins Freeman|Alice Dunbar-Nelson|Sui Sin Far|Abraham Cahan|Theodore Dreiser
Henry Adams|Zitkala-Sa|Grant Allen|Vernon Lee|Lucas Malet|Richard Jefferies|W. H. Hudson
George Borrow|Mrs Henry Wood|W. S. Gilbert|Arthur Wing Pinero|Henry Arthur Jones|W. E. Henley
Robert Bridges|Henry Newbolt|George du Maurier|Anthony Hope|W. W. Jacobs|Alfred Tennyson
Robert Browning|Elizabeth Barrett Browning|Matthew Arnold|Arthur Hugh Clough
Gerard Manley Hopkins|Christina Rossetti|Dante Gabriel Rossetti|Emma Lazarus|Sidney Lanier
James Whitcomb Riley|Edwin Arlington Robinson|Charles Eastman|Thomas Carlyle|John Ruskin
John Stuart Mill|John Henry Newman|John Keble|Edward FitzGerald|Walter Bagehot|Samuel Butler
Harriet Taylor Mill|Richard Hurrell Froude|Wilkie Collins|George Meredith|Thomas Hardy
Robert Louis Stevenson|Oscar Wilde|Lewis Carroll|Bram Stoker|Arthur Conan Doyle
Herbert George Wells|Ralph Waldo Emerson|Henry David Thoreau|Margaret Fuller
Nathaniel Hawthorne|Herman Melville|Walt Whitman|Emily Dickinson|Harriet Beecher Stowe
Frederick Douglass|Harriet Jacobs|Mary Elizabeth Braddon|Joseph Sheridan Le Fanu|Charles Reade
Rhoda Broughton|Ouida|George Gissing|Arthur Morrison|Harriet Martineau|Frances Power Cobbe
Josephine Butler|Annie Besant|Walter Pater|John Addington Symonds|Leslie Stephen|Edmund Gosse
Andrew Lang|Alice Meynell|Amy Levy|Mathilde Blind|Augusta Webster|Coventry Patmore
Charles Kingsley|George MacDonald|Juliana Horatia Ewing|Mary Louisa Molesworth|Edith Nesbit
Kenneth Grahame|Beatrix Potter|Rudyard Kipling|Olive Schreiner|Henry Lawson|Ada Cambridge
Toru Dutt|Mary Seacole|Susanna Moodie|Ernest Jones|Joseph Skipsey
Hall Caine|Marie Corelli|Frances Hodgson Burnett|Richard Doddridge Blackmore|William Black
Samuel Rutherford Crockett|Ian Maclaren|George Douglas Brown|Silas Hocking|Joseph Hocking
E. W. Hornung|R. M. Ballantyne|W. H. G. Kingston|G. A. Henty|F. Anstey|George Grossmith
Henry Wadsworth Longfellow|John Greenleaf Whittier|Oliver Wendell Holmes|James Russell Lowell
Nathaniel Parker Willis|Jones Very|Frederick Goddard Tuckerman|Celia Thaxter|Fanny Fern
Harriet Prescott Spofford|Rose Terry Cooke|Mary Noailles Murfree|Grace King|Elizabeth Stoddard
Constance Fenimore Woolson|Helen Hunt Jackson|Thomas Wentworth Higginson|Edward Bellamy
Ignatius Donnelly|Henry George|Harold Frederic|Standish James O'Grady|Emily Lawless
William Allingham|Geraldine Jewsbury|William Barnes|Jean Ingelow|Alfred Austin
Richard Watson Dixon|Robert Buchanan|Sydney Dobell|William Edmondstoune Aytoun|Gerald Massey
Ebenezer Elliott|Richard Garnett|Charlotte Riddell|Mary Cecil Hay|Helen Mathers|Edna Lyall
Rosa Nouchette Carey|Emma Marshall|Evelyn Whitaker|Catherine Gore|Marguerite Blessington
Anne Marsh|Emily Eden|George Egerton|Netta Syrett|Elizabeth Robins|Cicely Hamilton
Gertrude Dix|Evelyn Sharp|Florence Bell|Dion Boucicault|Tom Taylor|Charles Kean|Augustin Daly
George Saintsbury|Henry Sidgwick|William Lecky
"""

# Installment 9: Edwardian and interwar Britain, Ireland and America, 1901-1945.
I09 = """
Joseph Conrad|Herbert George Wells|Arnold Bennett|John Galsworthy|E. M. Forster|Virginia Woolf
D. H. Lawrence|W. B. Yeats|T. S. Eliot|Ezra Pound|H. D. (Hilda Doolittle)|Edward Thomas
Siegfried Sassoon|Wilfred Owen|Rupert Brooke|Walter de la Mare|Robert Frost|Wallace Stevens
William Carlos Williams|Marianne Moore|Hart Crane|e e cummings|Isaac Rosenberg|Robert Graves
Edmund Blunden|John Masefield|J. M. Synge|Lady Gregory|Sean O'Casey|James Joyce
Lytton Strachey|Roger Fry|Dorothy Richardson|Ford Madox Ford|Katherine Mansfield
Hugh MacDiarmid|Lewis Grassic Gibbon|Edwin Muir|Gertrude Stein|Sherwood Anderson
Langston Hughes|Zora Neale Hurston|Claude McKay|Countee Cullen|Jean Toomer|F. Scott Fitzgerald
Ernest Hemingway|John Dos Passos|William Faulkner|Thomas Wolfe|Katherine Anne Porter
Eudora Welty|Carson McCullers|W. H. Auden|Christopher Isherwood|Stephen Spender|Louis MacNeice
George Orwell|Aldous Huxley|Evelyn Waugh|Agatha Christie|Dorothy L. Sayers|M. R. James
Algernon Blackwood|Arthur Machen|Noel Coward|Olaf Stapledon|John Boynton Priestley
Terence Rattigan|T. E. Lawrence|Saki (H. H. Munro)|Walter Greenwood|James Hanley
W. Somerset Maugham|P. G. Wodehouse|Graham Greene|G. K. Chesterton|John Buchan|Max Beerbohm
Hilaire Belloc|Vera Brittain|David Jones|R. C. Sherriff|Richard Aldington|Ivor Gurney
Frederic Manning|Herbert Read|Charles Sorley|Robert Nichols|Laurence Binyon|John McCrae
Julian Grenfell|John Steinbeck|Willa Cather|Sinclair Lewis|Eugene O'Neill|Thornton Wilder
Nathanael West|Dashiell Hammett|Richard Wright|Upton Sinclair|Djuna Barnes|Elizabeth Bowen
Jean Rhys|Stella Gibbons|Winifred Holtby|E. M. Delafield|Rosamond Lehmann|Ivy Compton-Burnett
Sylvia Townsend Warner|Patrick Hamilton|E. H. Young|Dorothy Whipple|Radclyffe Hall
Oliver Onions|T. F. Powys|Henry Green|Stevie Smith|W. E. B. Du Bois|James Weldon Johnson
Nella Larsen|Jessie Fauset|Arna Bontemps|Sterling Brown|Gwendolyn Brooks|Wallace Thurman
George Schuyler|Rudolph Fisher|Alain Locke|Marcus Garvey|Josephine Tey|Ngaio Marsh
Margery Allingham|Ronald Knox|Baroness Orczy|Erskine Childers|John Meade Falkner
Rafael Sabatini|P. C. Wren|Compton Mackenzie|Dornford Yates|Edgar Wallace|A. A. Milne
Arthur Ransome|J. R. R. Tolkien|C. S. Lewis|Charles Williams|W. H. Davies|Edith Sitwell
Osbert Sitwell|Sacheverell Sitwell|Charlotte Mew|Anna Wickham|T. E. Hulme|F. S. Flint
Richard Church|Padraic Colum|Douglas Hyde|I. A. Richards|William Empson|F. R. Leavis
Q. D. Leavis|E. M. W. Tillyard|J. C. Squire|Mary Webb|Sheila Kaye-Smith|Constance Holme
H. E. Bates|A. E. Coppard|Henry Williamson|Liam O'Flaherty|Frank O'Connor|Sean O'Faolain
Kate O'Brien|Molly Keane|Samuel Beckett|Flann O'Brien|Patrick Kavanagh|Austin Clarke
Neil Gunn|Naomi Mitchison|Teresa Deevy|Lennox Robinson|Paul Vincent Carroll|C. S. Forester
Dennis Wheatley|Howard Spring|A. J. Cronin|Robert Tressell|Storm Jameson|Phyllis Bentley
Ethel Mannin|F. Tennyson Jesse|Rodney Ackland|Emlyn Williams|Jack Common
Christopher Caudwell|Ralph Fox|Wyndham Lewis|H. P. Lovecraft|Arthur Koestler|C. P. Snow
J. B. S. Haldane|Malcolm Muggeridge|Harley Granville-Barker|St John Ervine|Githa Sowerby
Elizabeth Baker|Stanley Houghton|Allan Monkhouse
"""

CANONS = {"08": I08, "09": I09}


def names(raw):
    return [n.strip() for n in raw.replace("\n", "|").split("|") if n.strip()]


def normalise(text):
    text = unicodedata.normalize("NFKD", text or "")
    text = text.encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", " ", text).split()


def load_corpus():
    con = sqlite3.connect(DB_PATH)
    try:
        return [(r[0], r[1], r[2] or "") for r in
                con.execute("select author_id, full_name, alternative_names from authors")]
    finally:
        con.close()


def find(name, corpus):
    tokens = normalise(name)
    if not tokens:
        return None
    surname, initials = tokens[-1], [t for t in tokens[:-1] if len(t) == 1]
    for _aid, full, alt in corpus:
        haystack = normalise(full) + normalise(alt)
        if surname not in haystack:
            continue
        if initials and not all(i in [t[0] for t in haystack] for i in initials):
            continue
        return full
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("installment", choices=sorted(CANONS))
    ap.add_argument("--starts-with", default=None,
                    help="only report names whose surname starts with this letter")
    ap.add_argument("--quiet", action="store_true",
                    help="print nothing; exit 1 when gaps remain")
    args = ap.parse_args()

    corpus = load_corpus()
    wanted = names(CANONS[args.installment])
    absent = [(n, find(n, corpus)) for n in dict.fromkeys(wanted)]
    absent = [n for n, hit in absent if not hit]
    if args.starts_with:
        letter = args.starts_with.lower()
        absent = [n for n in absent if n.split()[-1].lower().startswith(letter)]

    if args.quiet:
        return 1 if absent else 0

    print("installment %s: %d names in canon, %d absent from the database"
          % (args.installment, len(set(wanted)), len(absent)))
    for i in range(0, len(absent), 4):
        print("  " + " | ".join(n[:27].ljust(27) for n in absent[i:i + 4]))
    return 1 if absent else 0


if __name__ == "__main__":
    sys.exit(main())
