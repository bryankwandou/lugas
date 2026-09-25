# Final Gate

Run before delivering. Silent. Fix, don't report.

## Hard fail — must fix

- [ ] A fact, number, name, date, or citation from the input is missing or changed (rewrite mode).
- [ ] A fact, number, quote, testimonial, or reference appears that was not in the input or common knowledge.
- [ ] Opening sentence is throat-clearing (§1 of the pattern file).
- [ ] Any emoji, unless the user's brand voice uses them.
- [ ] Output starts with a preamble ("Berikut hasil parafrase ...", "Here's the rewritten version:").
- [ ] Register or form of address changes mid-text (Anda ↔ kamu).
- [ ] Genre structure violated (e.g. headers in an email, paragraphs on a flyer, marketing adjectives in a paper).
- [ ] Anything from `boundaries.md` "does not do" list.

## Soft fail — fix if it takes under a minute

- [ ] More than 2 items from §2 of the pattern file in any 100 words.
- [ ] Three consecutive sentences of similar length.
- [ ] Every paragraph ends in a mini-conclusion.
- [ ] A list of exactly three appears more than twice.
- [ ] A claim of quality ("efektif", "powerful") with no evidence next to it.
- [ ] Sentences over the genre's length limit.
- [ ] Non-baku spelling in formal Indonesian (analisa, praktek, resiko, merubah, ijin).

## Structural gate — texts over ~300 words

Wording can pass while the shape still reads as machine-written. See
`structure-tells.md` for the evidence and the fixes.

Hard fail:

- [ ] A sentence explains what the reader just read (the single largest human/AI gap).
- [ ] A generic noun stands where a real name belongs, with no `[isi: ...]` marking it.
- [ ] A specific name, number, or source was invented to fill such a gap. Never.
- [ ] Output is mostly `[isi: ...]` and says nothing about where to get the data.
      After the text, add one line per gap type: what to collect and from whom
      (e.g. "stok opname terakhir — minta ke bagian gudang"; "3–5 penelitian
      sejenis — Google Scholar/Garuda, 5 tahun terakhir"; "masalah nyata —
      wawancara pemilik"). A skeleton without a route to fill it is not finished.

Soft fail — fix if the genre allows:

- [ ] Nothing is left unresolved; every thread closes.
- [ ] The main decision or recommendation is shown as costless.
- [ ] Nothing outside the subject's control affects the outcome.
- [ ] Emotion appears only as physical sensation, never named plainly.
- [ ] Every quote lands the thesis in the text's own vocabulary.
- [ ] Sections are interchangeable in intensity — no escalation.
- [ ] A closing section only restates, in a genre that does not need a summary.
- [ ] The main person is introduced by a physical description before doing or saying anything.
- [ ] Every setting mirrors the mood of the scene it is in.
- [ ] Narrative runs in strict time order and nothing late changes how an early part reads.
- [ ] The problem arrives only after a long scene-setting opening.

Claude-specific, check these two every time: **flat escalation**, and **an epilogue
nobody asked for**.

## Read-aloud test

Read the first and last paragraph as if speaking to the intended reader. If a phrase
would make them roll their eyes, cut it.
