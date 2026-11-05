# Installment 7 — open verification items

Resolve before the installment-7 commit. Each is a claim currently in `data/`
that has not been confirmed against a source.

1. **`The Fall of Hyperion: A Dream` — `meter_and_prosody` says "blank verse".**
   The record came from batch b2. The widely drawn critical contrast is that
   *Hyperion* is in Miltonic blank verse while *The Fall of Hyperion* is in
   rhymed couplets; a web check for the couplet claim returned nothing I could
   cite, so the field was left unchanged rather than rewritten from recall.
   Confirm against the Harvard/Longman text or the *Poetical Works* and correct
   `meter_and_prosody` if the couplet form is right.
   (Its `narrative_structure` was already neutralised — it no longer names a metre.)

2. **`Ode on a Grecian Urn` — "the house in the north of London which the poet
   shared with a friend".** This is Wentworth Place, Hampstead, shared with
   Charles Armitage Brown. Named explicitly only if the corpus convention for
   `historical_context` permits it; the anonymised phrasing is not wrong.

3. **Robert Southey's "Don Manuel Alvarez Espriella" by-line** for
   *Letters from England* is recorded in the work text but `pseudonyms` is null
   on b1's Southey author record. Add it there so the alias is searchable.

4. **`The Venetian Bracelet` (1829)** — verified as Landon's 1829 Longman, Rees,
   Orme, Brown and Green volume, whose full first-edition title is *The Venetian
   Bracelet, the Lost Pleiad, A History of the Lyre, and Other Poems*. The
   short title in `data/works/installment_07_works_batch4.json` should either be
   lengthened or the full title placed in `alternative_titles`.
