# Installment 07 — Sources Audit & Additions

## STATUS: IN PROGRESS

## KEY DISCREPANCY (first finding)
The task brief names ~30 suspicious records (Walter Scott: Critical Heritage Series;
Thomas Campbell "Weather Atlas" memoir; Jane Austen Complete Works garble; Walter Pater
prose (Eliot); English Historical Documents vol 9; Short History of the English Stage;
Journal of George Rose; British Journals and Periodicals 1789-1832; Romantic Reformation;
Oxford Handbook of Early Victorian Studies; DJB/Ainsworth; Maturin letters; Redekop &
McElroy Ainsworth; Waverley Novels Ainsworth set; Fitzpatrick Burns; De L. Jackson Burns
letters; Charlotte Bronte letters (Swinburne); Coleridge letters (Grader); De Quincey
Mainstone/Ingpen; Hosch Rise of the Novel).

The CURRENT data/sources/installment_07_sources.json does NOT contain these records.
It holds exactly 35 records (verified below). The file appears to have ALREADY been
cleaned in a prior session, OR the brief describes an earlier draft state.

ACTION: audit the 35 records that ARE actually present; verify each against live web
sources; correct only where a live source proves an error; record the named-but-absent
brief items as "NOT PRESENT IN FILE — nothing to falsify/delete".

## AUDIT OF PRESENT RECORDS (live web verification)
Records #1-#7,#10-#23,#25-#28,#31,#32,#34,#35 are standard well-documented editions whose
editor/publisher/year match catalogue records; verifying flagged volume counts now:
- #8  CPW Byron (7 vol) McGann — verifying count
- #9  Byron Letters & Journals Marchand (12 vol?) — verifying count
- #24 Lamb Works Lucas (6 vol?) — FLAG: normally 7 vol, verify
- #29 CBB Bicentennial Krause — verify editor middle initial + count
- #30 CBB Collected Writings Kamrath (7 vol, Bucknell) — verify existence
- #33 Bryant Letters Voss (6 vol, Fordham) — verify count/publisher
- #6  Bollingen Coleridge (16 vol) Coburn — verify count framing
(pending — append findings)

## RECOMMEND-DELETION
(pending)

## JOB 2 ADDITIONS
(pending — writing to data/sources/installment_07_sources_b.json)
