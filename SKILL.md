---
name: lugas
description: Rewrite or draft any text so it reads like a careful human wrote it — plain, specific, no machine filler. Works for Indonesian first, English second. Use when the user says "tulisan ini terlalu AI", "parafrase", "bikin natural", "rapikan tulisan", "sounds like ChatGPT", "make this less robotic", "humanize", "edit this copy", or asks for a report, research paper, proposal, and for campus writing — kerangka and format for KKP/magang, proposal tugas akhir, skripsi, tesis, proposal kegiatan, especially Universitas Atma Jaya Makassar (UAJM), plus 11 more Indonesian and 5 foreign institutions. Also for website copy, README, commit message, video script, ad, brochure, pamphlet, email, or caption. Aims to get it right in one pass so the user does not have to re-prompt ten times.
---

# Lugas

*Lugas* (Indonesian): plain, direct, without ornament.

This skill makes text **good**, not "undetectable". The patterns that make text sound
machine-written are the same ones that make it bad: padding, vague claims, stock
phrases, symmetrical lists, fake enthusiasm. Remove those and the text improves for
every reader.

Read `references/boundaries.md` once. It is short and it matters.

## The one-pass workflow

Do these steps in order. Do not show the steps to the user unless asked; show the result.

### 1. Identify the job (10 seconds)

Answer four questions silently. If the user already answered them, do not ask again.

| Question | Why it matters |
|---|---|
| Language? | id → `patterns-id.md` · en → `patterns-en.md` · anything else → `patterns-universal.md`. Always write in the target language directly. |
| Genre? | Load the matching section of `references/genres.md` |
| Reader? (dosen, investor, customer, developer, general public) | Sets vocabulary and formality |
| Mode? **rewrite** existing text or **draft** new text | Rewrite must keep every fact; draft must not invent facts |

If one of these is truly unknowable and changes the output a lot, ask ONE short question.
Otherwise pick the most likely answer and state it in one line at the end.

### 2. Extract the substance

Before touching wording, list (internally) what the text actually says:
claims, numbers, names, dates, citations, requirements, calls to action.

- **Rewrite mode:** every item on this list must survive. Never add a number, source,
  quote, or result that was not in the input. If the input has a gap (e.g. "increased
  significantly" with no figure), keep it vague or mark it `[angka?]` / `[figure?]` —
  never invent.
- **Draft mode:** use only facts the user gave or that are general knowledge. Mark
  anything that needs the user's data as `[isi: ...]` / `[fill: ...]`.

### 3. Cut

Apply the kill list for the language (`patterns-id.md` §1–§4 or `patterns-en.md` §1–§4).
Typical cut on AI text: 20–40% of words with zero loss of meaning.

### 4. Rebuild

Apply the rebuild rules (`patterns-*.md` §5) and the genre rules (`genres.md`).
Core rules, all languages:

1. **Concrete over abstract.** "Waktu tunggu turun dari 14 ke 3 hari" beats "efisiensi meningkat signifikan".
2. **One idea per sentence.** Vary length. Some sentences are four words.
3. **Subject + verb early.** Put the actor first. Prefer active voice unless the genre demands passive (some Indonesian academic styles do — see `genres.md`).
4. **No throat-clearing.** Start with the point. Delete the first sentence if it only announces the topic.
5. **No summary ending** unless the genre needs one (reports, papers do; copy, emails usually don't).
6. **Lists only for truly parallel items.** Three-item lists are not mandatory. Two or five is fine.
7. **Formatting follows the medium.** No bold/headers/bullets in an email, caption, script, or pamphlet body unless the user's format uses them.
8. **Zero emoji** unless the user's brand voice explicitly uses them.
9. **Keep the author's voice.** If the input has a quirk that is correct and intentional, keep it.

### 4.5. Restructure (texts over ~300 words)

Wording is the shallow layer. The habits that make text read as machine-written are
structural, and they survive any amount of rephrasing — this is measured, not a hunch
(`references/research-basis.md` §A). Skip this step only for captions, commit messages,
and other very short work.

Run the seven-point pass in `references/structure-tells.md` §3:

1. Delete the sentences that explain what the reader just read.
2. Keep one thread unresolved. A text where everything closes is hiding something.
3. Name what the main decision cost.
4. Name what acted from outside the subject's control.
5. Turn every generic noun into a real one — or an honest `[isi: ...]`. Never invent it.
6. Check that intensity rises. Interchangeable sections mean a flat piece.
7. Cut the epilogue if the genre does not require a summary.

If the text passes the wording rules but fails this pass, the wording pass was wasted.

For fiction and long narrative (over ~1,000 words), also fill the outline audit in
`references/storyscope.md` §5 from the draft. The measured signal is spread across
many dimensions at once, so fixing one habit does not move the shape; fix up to
three red flags per pass.

### 5. Check (the gate)

Run `references/checklist.md`. It takes under a minute. If any **hard fail** item
triggers, fix it before answering. Do not report the checklist to the user.

### 6. Deliver

- Output the finished text first, ready to paste. No preamble like "Berikut hasilnya:".
- After the text, at most 3 short lines: assumptions made, `[placeholders]` left, or a
  fact the user should verify. Skip this if there is nothing.
- If the user asked for a diff or explanation, give a compact table: *before → after → reason*.

## Token economy

The point is to stop the 10-retry loop. So:

- Load only the reference files the job needs (language + genre + checklist).
- For texts over ~1,500 words, process section by section, keeping a running fact list.
- Never produce "3 alternative versions" unless asked. One good version.
- If the user says "lagi" / "again" with no feedback, ask what felt wrong in one line
  (offer 3 options: terlalu formal / terlalu santai / masih kaku) instead of regenerating blindly.

## File map

| File | Load when |
|---|---|
| `references/boundaries.md` | Always, once per session |
| `references/patterns-id.md` | Indonesian text |
| `references/patterns-en.md` | English text |
| `references/patterns-universal.md` | Any other language (and regional languages of Indonesia) |
| `references/structure-tells.md` | Step 4.5 — any text over ~300 words, always for narrative |
| `references/storyscope.md` | Narrative over ~1,000 words (run its §5 outline audit), or when asked why a structural rule exists — all 30 measured features and the model fingerprints |
| `references/genres.md` | Always — jump to the genre section |
| `references/checklist.md` | Step 5, always |
| `examples/before-after-id.md` | Unsure what "good" looks like in Indonesian |
| `examples/before-after-en.md` | Unsure what "good" looks like in English |
| `references/patterns-universal.md` | Any language without its own pattern file |
| `references/adding-a-language.md` | User wants another language |
| `references/research-basis.md` | User asks why a rule exists, or you are changing one |
| `references/literature.md` | Look up a `[lit: ...]` tag, or check the evidence before changing a rule (130 annotated sources by theme) |
| `references/literature-2.md` | 385 further sources (arXiv, 2022–2026): narrative, creativity, detection, evasion, stylometry, academic writing, non-English, co-writing — screened by abstract, read the paper before leaning on one |

## Kampus: Atma Jaya Makassar and other universities

Lugas carries three campus guides in `kampus/`. Each has a `GUIDE.md` (read it first)
and its own `references/`; paths inside a guide are relative to that guide's folder.
Where a guide says "the `pedoman` skill" or "the `rangka` skill", read the sibling
folder here instead. Order of work: **outline → prose → format**.

| Need | Read |
|---|---|
| UAJM student: KKP/magang, proposal TA, Ringkasan Kapasitas Diri, skripsi, naskah jurnal, seminar, sidang — the whole route with outlines and checks | `kampus/atmajaya/GUIDE.md` |
| Outline (kerangka bab/subbab) of any document: proposal kegiatan, LPJ, SK, AD/ART, laporan, makalah, tesis, website, video — or turning research files into one outline | `kampus/rangka/GUIDE.md` |
| Format compliance against a guideline: margins, fonts, cover, numbering, citation style, eligibility gates — UAJM FTI plus ITB, UI, IPB, UGM Faperta, UB, ITS, Unair, Unhas, UNS, Unpad, Undip, and five foreign institutions | `kampus/pedoman/GUIDE.md` |

Guidelines outrank this file on format and structure; this file owns the prose inside
the structure. Never invent campus facts — mark gaps `[ISI: …]` or `[CEK: …]`.
