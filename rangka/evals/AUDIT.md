# Audit — rangka skill (2026-09-25)

**Caveat: self-graded.** The same model audited the skill, changed it, wrote the new
evals, ran them, and graded them. Scores are one reviewer's judgement, biased toward the
work it just did. Treat them as a starting point for a human review, not a measurement.
"Before" line numbers refer to commit `8d75830`; "after" line numbers refer to the audit
commit.

## Scores

| Dimension | Before | After | Why it moved |
|---|---|---|---|
| Strength (rules correct, traps caught) | 6 | 8 | 9 UAJM rules corrected against the PDFs; hard-trap evals 23–26 pass after one fix |
| Recency | 5 | 6 | pedoman is still the 2015 edition (only source available); the skill now says so and flags regulation numbers as `[CEK]`. Capped until a newer pedoman is read |
| Completeness | 6 | 8 | full outline trees for S1/S2/S3, separate LPJ/SK/proposal files, robust multi-file condensing, diagram output template |
| Clarity | 6 | 7 | routing tables list every new file; check codes renumbered; the SKILL.md body is longer (276 lines) and denser |

### Evidence — before

| Dimension | File:line (commit 8d75830) | Finding |
|---|---|---|
| Strength | `references/uajm-skripsi.md:23` | Abstrak described as "satu alinea, spasi tunggal". The pedoman (TA 4.1.9) says **200–250 words**, paragraph 1 = name, title, "dibimbing oleh" |
| Strength | `references/uajm-skripsi.md:19` | Pengesahan lists "panitia ujian". The pedoman (TA 4.1.5, Lampiran 5) has Pembimbing I, II and Ketua Prodi only |
| Strength | `references/uajm-skripsi.md:21` | Peruntukan treated as required. TA 4.1.7: "bukan halaman yang diharuskan" |
| Strength | `references/uajm-skripsi.md:130` | Reader "4 penguji + 2 pembimbing". "Min. 4 penguji" applies to the seminar usulan; at the sidang, pembimbing are ex-officio and do not examine (TA 1.5) |
| Strength | `references/uajm-format.md:21` | Skripsi cover `[CEK: warna prodi]`. TA 4.1.1 / 5.1.5: **hijau muda** |
| Strength | `references/uajm-usulan-ta.md:132` | RKD listed with "Konsideran". TA 3.2.2 replaces it with **Kapasitas Diri** and has no hipotesa |
| Strength | `references/uajm-format.md` (whole file) | Missing: "3+ authors → dkk./et al.", name-order rules, footnote & quotation rules, "5 (lima)" ban, prosiding reference type, naskah jurnal margins 2.5/2.5/4/2 cm, ≤15 pages, max 3 heading levels, Harvard-vs-[1] contradiction |
| Strength | `references/genre-organizational.md:131-134` | "Bulan Romawi" and "bukan PERTAMA" stated as absolute rules. A real FTI UAJM document numbers `006/FTI/SK/Kajur TI/KP/2026` with no month |
| Recency | `references/uajm-format.md:3-5` | 2015 pedoman presented without saying it could have been replaced |
| Completeness | `SKILL.md` (whole file) | No diagram/HTML output guidance: no language switch, no theme default, no print rule |
| Completeness | `references/summarize-to-outline.md:234-250` | Built for one draft. No per-point source labels, no duplicate merging, no point count, no off-topic files, no route to a target template |
| Completeness | `references/genre-organizational.md:56-86` | LPJ had no budget-realisation columns (% serapan, bukti), no sign convention, no recomputation rule, no deficit handling |
| Completeness | `references/genre-thesis.md:27-69` | Chapter lists as prose; no front matter → lampiran tree for tesis/disertasi |
| Completeness | `evals/runs/` | Runs for evals 7, 8, 9 absent |
| Clarity | `references/pedoman-adapter.md:19` | Step 4 names only 4 campuses while 22 campus files exist |
| Clarity | `references/uajm-kkp.md:14,40` | Rangka rules of thumb (40–50% for Bab III) mixed with pedoman rules without saying which is which |

### Evidence — after

| Dimension | File | Change |
|---|---|---|
| Strength | `references/uajm-skripsi.md` §Bagian awal | 15 components with page numbers and pedoman wording; abstrak 200–250 words; pengesahan signatories; Peruntukan *(jika ada)*; meterai `[CEK]` |
| Strength | `references/uajm-skripsi.md` §Syarat | pembimbing qualifications, seminar hasil/kemajuan quorum, sidang: IPK 2.75, 80% attendance, ketua sidang rank, ex-officio pembimbing |
| Strength | `references/uajm-usulan-ta.md` §RKD | structure table with Kapasitas Diri, no hipotesa/konsideran; check P11 |
| Strength | `references/uajm-kkp.md` | procedure (KSM, permohonan form, refusal letter), seminar composition, cover colour and signatory conflicts marked `[CEK]`, K10 (missing identity data), K11 (dates vs today) |
| Strength | `references/uajm-format.md` | rewritten with section citations (KKP 4.x / TA 5.x) for every rule; internal pedoman contradictions called out |
| Strength | `references/org-sk.md` | numbering/diktum rules softened to "template lembaga wins"; SK vs surat penugasan vs surat pengantar from a real UAJM example (structure only, no names) |
| Recency | `references/uajm-format.md:3-14` | dated re-read; "cek edisi setelah 2015" line required |
| Completeness | `references/full-outlines.md` | copy-ready trees: skripsi, tesis, disertasi monograf, disertasi berbasis artikel; checks F1–F6 |
| Completeness | `references/summarize-to-outline.md` | R-draf vs R-catatan, point cards with `[Fn]`, conflict/duplicate rules, coverage matrix + point count, R1–R10 |
| Completeness | `references/org-proposal-kegiatan.md`, `org-lpj.md`, `org-sk.md` | full structures, RAB and realisation tables, recomputation, deficit, OP/LP/SK checks |
| Completeness | `assets/flowchart-template.html` + `SKILL.md:208` | language switch (id/en diagrams, 6-language UI, RTL), light by default, print always light |
| Completeness | `references/international.md` §2h, `pedoman-adapter.md` steps 5–7 | Arabic thesis pattern (فصول, حدود ×4, التعقيب, split reference list); foreign-language guideline procedure; conflicting guidelines; A7–A8, N6–N7 |
| Clarity | `SKILL.md:57,90-92,193,257-261` | routing rows for every new file; output-language statement; description 1000/1024 chars |

## UAJM verification log

Every UAJM rule was checked against `E:\Download\magang\Pedoman`: *Pedoman KKP FTI 15.pdf*
(18 Jan 2015), *Pedoman TA TI 15.pdf* (1 Apr 2015) and *Pedoman TA TI 15b 10 juni.pdf*.
A text diff of the two TA editions shows the June revision only renames the programme
("Informatika" → "Teknik Informatika") and fixes the table of contents. No separate
proposal PDF exists: proposal/usulan rules come from TA Bab II–III.

Corrected: abstrak length and structure · pengesahan signatories · Peruntukan optional ·
sidang reader and quorum · skripsi cover colour · RKD sections · naskah jurnal margins,
page limit, heading depth · page-number rule for titled sections · KKP Bab III share
labelled as advice.

Added: dkk./et al. · name-order rules · footnotes and quotations · number/unit rules ·
language-error list · prosiding reference type (plus the swapped g/h labels in the TA
pedoman) · pembimbing qualifications · ujian rules · KKP procedure letters · halaman
pengajuan wording · Pedoman Penggunaan content · abstract paragraph 1 format.

Contradictions inside the pedoman, now surfaced as `[CEK]` rather than resolved
silently: KKP cover colour (3.1.1 vs 4.1.5) · KKP cover font size (20 vs "others 12") ·
KKP signatory labels (text vs Lampiran 2) · naskah jurnal citation (numbered examples vs
"Harvard") · skripsi pengesahan page number (iv vs the Lampiran 11 contents) · degree
wording (Sarjana Komputer vs Sarjana Teknik Informatika).

## Fixes to the reference flowchart

`E:\Download\rangka-contoh\flowchart-antrean-puskesmas.html` had two print bugs, both
fixed in `assets/flowchart-template.html`:
1. **System theme + dark OS printed dark.** The print override `:root` had lower
   specificity than `:root:not([data-theme="light"])`. Now uses `!important`.
2. **Tall diagrams printed blank** (confirmed in headless Chrome print-to-PDF): the
   card's `overflow-x:auto` plus `break-inside:avoid` clipped the SVG. The print CSS now
   sets `overflow: visible` and caps SVG height at 22 cm.
Also: `beforeprint` re-rendering was async and could print dark SVGs, so both light and
dark SVGs are now rendered up front and print CSS shows the light one. The default
language now comes from `DEFAULT_LANG` (the user's language) instead of the browser
locale. Mermaid errors show the source instead of a blank card. The original file in
`E:\Download` was not modified.

## Evals 23–26 (hard traps)

| Eval | Trap | Run 1 | Final |
|---|---|---|---|
| 23 | 5 messy notes: conflict, duplicate, off-topic file, unsourced refs | 7/7 | 7/7 |
| 24 | UAJM KKP, missing fields, duration under the minimum, already finished | 7/8 | 8/8 (run 2, after adding K11 and the date rule) |
| 25 | LPJ: wrong user total, new pos, lost receipt, deficit | 7/7 | 7/7 |
| 26 | Arabic master's thesis + HTML flowchart | 7/7 | 7/7 |

Details and quoted evidence: `evals/runs/grading-23-26.md`.

## Still open

1. ~~Brackets around Arabic placeholders inside Mermaid nodes render mirrored in the HTML.~~ Fixed 2026-09-25 (see below).
2. The only UAJM pedoman available is from 2015; a newer edition would override parts of this audit.
3. The regulation numbers for tata naskah dinas (ANRI, Permendagri) are deliberately not cited; `[CEK]` stays until someone checks the current texts.
4. Runs for evals 7–9 are still missing from `evals/runs/`.
5. No human has reviewed any of the grades.

## Real-document test fixes (2026-09-25)

Three real UAJM Informatika documents (two usulan TA, one laporan KKP) were outlined
blind from the title only, then compared with the actual headings. The documents stay
outside the repo. No names, addresses, phone numbers or topics from them were copied
in. The old running example in `genre-research.md` matched one document's real topic,
so it was replaced with a neutral made-up one.

| Code | Fix | File |
|---|---|---|
| B1 | Engineering research may have comparative hypotheses (system vs baseline with a statistical test); P3 updated | `uajm-usulan-ta.md`, `full-outlines.md` |
| B2 | Usulan TA has two layouts: B = BAB I–V template (abstrak, daftar isi/tabel/gambar/lampiran/singkatan, Konsideran = Bab IV, Jadwal = Bab V) and A = 2015 a–f; detect from the user's files, else ask, else B; P12 | `uajm-usulan-ta.md`, `SKILL.md` routing row |
| B4 | Contradictions inside one file (phase counts, company/agency names) are handled the same as contradictions across files: rule 7, the Konflik diagnosis, R7, new U13 | `summarize-to-outline.md`, `checklist.md` |
| B5 | Daftar Tabel/Gambar must match the body numbering: U14, S13, format item 13 | `checklist.md`, `uajm-skripsi.md`, `uajm-format.md` |
| B6 | P-check order fixed (P9, P10, P11); K10/K11 order fixed too | `uajm-usulan-ta.md`, `uajm-kkp.md` |
| B7/B8 | KKP slots: 2.6 Profil Klien, 1.7 Batasan dan Kerahasiaan; K14 | `uajm-kkp.md` |
| B9 | Both "Informatika" and "Teknik Informatika" are accepted; they must be consistent across cover, pengesahan and body (K12, S14, format item 14) | `uajm-kkp.md`, `uajm-skripsi.md`, `uajm-format.md` |
| B10 | Verbatim transcripts/logs in appendices are exempt from the bullet/language rules | `uajm-format.md` |
| B11 | Remote KKP: screenshot + dated commit-log evidence instead of the photo rule; K13 | `uajm-kkp.md` |
| B12 | Running example and A6 title replaced by a neutral topic (lab equipment loan system) | `genre-research.md`, `sources.md`, `README.md` |
| B13 | P7 / U15 read the *content* of the sensitivity analysis, not the heading (TELOS, SWOT or functional tests fail) | `uajm-usulan-ta.md`, `checklist.md` |
| Bidi | `fixBidi()` sets `dir="rtl"` on every Mermaid label that contains RTL script | `assets/flowchart-template.html`, `evals/runs/eval-26-flowchart.html` |

Bidi verification (headless Chrome 2x): a test diagram with labels `[أكمل: العدد] مشاركًا`,
`المدة [أكمل: 8 أسابيع]` and `النموذج [تحقق: ADDIE]`. The old template put the bracket of a
line-initial placeholder on the wrong side. The new template matches a plain `dir="rtl"`
reference paragraph on all three labels, with no Mermaid errors. The earlier eval-26
labels render the same both ways (all-Arabic text inside the brackets, preceded by
Arabic), so that eval could not show the bug.

Blind "from title" scores (same counting as the test README: one unit per front-matter
component, level-2 subsection, chapter without subsections, reference list and KKP
appendix, matched by function):

| Document | Before | After | What changed |
|---|---|---|---|
| 1 Usulan TA (engineering, compared with baselines) | 26/34 = 76% | 34/34 = 100% | layout B adds 7 front-matter parts; hypotheses no longer dropped |
| 2 Laporan KKP | 33/43 = 77% | 35/43 = 81% | 1.7 Kerahasiaan + 2.6 Profil Klien slots; the remaining 8 are Bab III jobs and appendices that cannot be known from a title |
| 3 Usulan TA | 24/30 = 80% (inflated by the leaked example) | 30/30 = 100% | layout B adds 6 front-matter parts; the score no longer depends on the topic |

Caveat: self-graded and rescored against the section inventory, not a fresh cold run.
The 100% scores measure structure only. They do not measure content quality.
