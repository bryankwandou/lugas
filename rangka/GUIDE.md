---
name: rangka
description: Build and check the outline (kerangka) of any document before drafting, or condense existing research files into one outline. Covers skripsi, tesis, disertasi, proposal/usulan TA, laporan KKP/magang, makalah, proposal kegiatan, LPJ, SK, AD/ART, surat, laporan, landing page, README, spec, video script, pitch deck, brosur, email, and study mind maps. Built-in Universitas Atma Jaya Makassar pedoman, sourced notes for 22 Indonesian campuses (UI, UGM, ITB, ITS, Unhas, UNM, UMI, UIN Alauddin, IPB, and more), foreign thesis norms, and an adapter for any guideline in any language. Use for "susun kerangka", "buat outline", "rangkum file jadi outline", "kerangka magang/KKP/proposal/tugas akhir", "bikin SK", "susun LPJ", "proposal kegiatan", "cek kesiapan judul", "struktur laporan/video/landing page", "outline this", or any long document without a fixed structure. Flowcharts ship as HTML with language/theme switch and light print. Not for one-line captions or polishing finished prose (use lugas).
---

# Rangka

*Rangka* (Indonesian): the frame that holds a body up. Write the frame first.

A weak document almost never fails at the sentence level. It fails because nobody
decided, before writing, who reads it, what gap it closes, and what each section must
prove. Rewriting sentences ten times does not fix that. Fixing the outline once does.

This skill produces an outline, not finished prose. When the outline passes the check,
hand drafting and wording to the `lugas` skill if it is installed.

## Hard rules (read first, apply always)

1. **Never invent facts.** No made-up numbers, sources, quotes, survey results, customer
   names, or regulations. Anything the user must supply is written as `[ISI: ...]`.
   Anything you are not sure of is written as `[CEK: ...]`. If the user writes in English,
   use `[FILL: ...]` and `[VERIFY: ...]` instead, throughout the whole output.
2. **Citations only from `references/sources.md`**, or sources the user gave. If a claim
   needs a source that is not there, write `[CEK: sumber untuk ...]`. Never guess a year,
   volume, or page.
3. **Title last.** The title or headline is written after the outline and the check.
   If checks fail only because the user's own data is missing (`[ISI]`), still give the
   titles but label them **sementara** (provisional). If a check fails for a structural
   reason (no gap, orphan question), fix the outline first; do not give titles.
4. **Campus and client rules win.** Indonesian university guidelines (pedoman penulisan)
   differ. When a structure is a convention, not a law, say so and add
   `[CEK: pedoman kampus/klien]`.
5. **No orphans.** Every question, claim, or promise in the outline must have a section
   that answers it and evidence that supports it. Every section must serve one of them.
6. **Ask at most one question before starting.** If information is missing, fill with
   `[ISI: ...]` and keep going. The user should get a usable outline in one reply.

## The workflow (same five steps for every genre)

### Step 0 — Classify (silent, 10 seconds)

Decide four things. Do not ask if the user already said them.

| Decide | Options |
|---|---|
| Language | id / en / any other — see `references/languages.md` |
| Genre family | see table below |
| Reader | dosen penguji, atasan, investor, calon pembeli, developer, pemirsa, pelajar, pemberi dana |
| Mode | **Dari nol** (topic only) / **Dari materi** (notes, data, draft) / **Rangkum** (existing files → one outline, see `references/summarize-to-outline.md`) |
| Institution | UAJM FTI → `uajm-*.md`. UI / UGM / ITB / Unhas / ITS / Binus / UNM / UMI / Unair / UB / IPB / Unpad / UIN Alauddin / Unismuh / Undip / UNS / UPI / UNY / UII / UMY / Telkom / UIN Jakarta → the matching `references/campus-*.md` **+** `pedoman-adapter.md`. Foreign campus → `references/international.md` **+** `pedoman-adapter.md`. Any other campus → `references/pedoman-adapter.md`. Not academic → skip |

| Genre family | Examples | Load |
|---|---|---|
| A. Riset | skripsi, proposal penelitian, jurnal, makalah ilmiah | `references/genre-research.md` |
| A+. Pascasarjana | tesis (S2), disertasi (S3) | `genre-research.md` **+** `references/genre-thesis.md` |
| B. Laporan & dokumen kerja | laporan magang/KKP/KP/PKL, laporan kegiatan, laporan bisnis, policy brief, memo, SOP | `references/genre-report.md` |
| G. Dokumen organisasi | proposal kegiatan, LPJ, SK, surat penugasan, AD/ART, surat permohonan, notulen, berita acara | `references/genre-organizational.md` (index) **+** `org-proposal-kegiatan.md` / `org-lpj.md` / `org-sk.md` |
| C. Persuasi | landing page, website, iklan, brosur, pamflet, poster, email marketing, pitch deck, proposal bisnis/sponsor | `references/genre-persuasion.md` |
| D. Teknis | README, dokumentasi, spec/PRD, ADR, tutorial, API docs | `references/genre-technical.md` |
| E. Media waktu | video pendek, video YouTube, podcast, presentasi lisan, webinar | `references/genre-timed.md` |
| F. Belajar | mind map materi kuliah, ringkasan bab, persiapan ujian | `references/genre-study.md` |

If the user gives dates (KKP period, event date, deadline), compare them with **today's
date** before advising what to collect or schedule: advice for a finished activity differs
from advice for a running one.

If a request spans two families (e.g. a research-based landing page), use the family of
the **final reader's action**, and borrow sections from the other.

#### Routing for Indonesian academic documents

Genre family alone is not enough for campus documents — the *pedoman* decides the
structure. Route by document, then by campus:

| Document | Read |
|---|---|
| Laporan KKP / KP / PKL / magang, UAJM FTI | `references/uajm-kkp.md` |
| Usulan/proposal TA or Ringkasan Kapasitas Diri, UAJM FTI (two layouts: BAB I–V template or 2015 a–f; detect from files or ask) | `references/uajm-usulan-ta.md` |
| Skripsi / tugas akhir, UAJM FTI | `references/uajm-skripsi.md` |
| Any of the above, **other campus** | `genre-research.md`/`genre-report.md` + `references/pedoman-adapter.md` |
| Skripsi / TA / tesis / proposal at **UI** (Universitas Indonesia) | `references/campus-ui.md` + `pedoman-adapter.md` |
| Skripsi / proposal at **UGM** (Gadjah Mada) | `references/campus-ugm.md` + `pedoman-adapter.md` |
| Tugas Akhir / tesis at **ITB** (Institut Teknologi Bandung) | `references/campus-itb.md` + `pedoman-adapter.md` |
| Skripsi / tesis / proposal at **Unhas** (Universitas Hasanuddin) | `references/campus-unhas.md` + `pedoman-adapter.md` |
| Skripsi / TA / proposal at **ITS**, **Binus**, **UNM**, **UMI**, **Unair**, **UB**, **IPB**, **Unpad**, **UIN Alauddin**, **Unismuh**, **Undip**, **UNS**, **UPI**, **UNY**, **UII**, **UMY**, **Telkom University**, **UIN Syarif Hidayatullah Jakarta** | `references/campus-its.md` / `campus-binus.md` / `campus-unm.md` / `campus-umi.md` / `campus-unair.md` / `campus-ub.md` / `campus-ipb.md` / `campus-unpad.md` / `campus-uin-alauddin.md` / `campus-unismuh.md` / `campus-undip.md` / `campus-uns.md` / `campus-upi.md` / `campus-uny.md` / `campus-uii.md` / `campus-umy.md` / `campus-telkom.md` / `campus-uin-jakarta.md` + `pedoman-adapter.md` |
| Thesis / dissertation at a **foreign** university, or thesis by publication anywhere | `references/international.md` + `genre-thesis.md` + `pedoman-adapter.md` |
| Tesis / disertasi, any campus | `references/genre-thesis.md` + `pedoman-adapter.md` |
| Formatting, citation style, or "berapa spasi / margin / gaya pustaka" (UAJM) | `references/uajm-format.md` |
| Anything with lampiran | `references/appendices.md` |
| "Kerangka lengkap / dari sampul sampai lampiran" for skripsi, tesis, disertasi | `references/full-outlines.md` (UAJM: the tree in `uajm-skripsi.md`) |
| Thesis in Arabic or at an Arab university | `international.md` §2h + `languages.md` + `genre-thesis.md` |
| Proposal kegiatan · LPJ · SK / surat penugasan | `org-proposal-kegiatan.md` · `org-lpj.md` · `org-sk.md` |

Always run `pedoman-adapter.md`'s 14 variables for academic work, and show the filled
table to the user **before** the outline. If the campus is UAJM FTI, the `uajm-*.md`
files already answer those variables — say so instead of asking.

Never state a campus rule you have not read. Sources for UAJM are the 2015 FTI pedoman;
everything beyond them is `[CEK: pedoman kampus]`.

For every campus with a `campus-*.md` file, the `campus-*.md` file says which rules are university-wide
and which belong to the faculty or prodi. At all four, key rules (chapter count, citation
style, proposal format) differ by faculty. If the user names the campus but not the
faculty/prodi, that is the one question to ask (hard rule 6). Anything else that is
unclear (which guideline edition applies, research start date, template version) is not a
second question and is not bundled into the first: state the default you are using and
mark it `[CEK ke pedoman fakultas]`. If they do not answer, use
only the university-wide rules from the campus file, mark the rest
`[CEK ke pedoman fakultas]`, and never present one faculty's rule as the campus's rule.

#### Mode Rangkum (files → one outline)

If the user points at files, a folder, or a finished draft and wants it condensed into a
single outline, follow `references/summarize-to-outline.md` instead of Steps 1–2. Steps
3–4 still apply. Read the files; never summarise from the filename.

### Step 1 — Core map (the gap)

Every useful document closes a gap between how things should be and how they are.
Researchers in Indonesia call these *Das Sollen* and *Das Sein*. The same idea works
everywhere. Fill this table before any outline:

| Node | Research | Report | Persuasion | Technical | Video/Study |
|---|---|---|---|---|---|
| **Should** (Das Sollen) | theory, norm, regulation, target | plan, KPI, SOP | the life the buyer wants | the spec, expected behavior | what the viewer/learner should be able to do after |
| **Is** (Das Sein) | field facts, data | what actually happened | the pain today | current behavior, bug, missing doc | what they can do now |
| **Gap** | research problem | deviation to explain | the problem you solve | the change needed | the lesson |
| **Reader** | penguji | decision maker | buyer | developer/user | viewer/learner |
| **Core claim** | answer to RQ (unknown yet, so: what will be tested) | main finding | the promise | what this doc lets you do | the one takeaway |
| **Proof** | method + data | data, evidence | proof points, testimonial, demo | code, examples | demo, examples |
| **Action** | contribution, recommendation | decision requested | CTA | next command/step | next step, quiz |

Rule: if Should and Is do not differ, there is no document yet. Say so and ask for a fact
from the field, or propose two candidate gaps marked `[CEK]`.

Write the core claim as one sentence a stranger understands. If you cannot, the outline
is not ready. (This is Minto's governing thought; see `references/sources.md`.)

### Step 2 — Outline from the genre template

Open the genre file from Step 0 and fill its template. For each section write:

- **Heading**
- **Job**: what this section must make the reader believe or do (one line)
- **Content points**: 2–5 bullets, facts or `[ISI: ...]`
- **Evidence**: data, source, example, or `[ISI]`/`[CEK]`
- **Length hint**: words, pages, seconds, or slides

Order sections by what the reader needs next, not by the order you learned things.

### Step 3 — Check (do not skip)

Run `references/checklist.md`: the universal checks, then the genre checks. Report the
result as a short table: item, pass/fail, fix. Fix failures in the outline, then re-run
only the failed items. Two rounds maximum; if still failing, show what is blocked and why
(usually missing user data).

### Step 4 — Title/headline and handoff

- Give 3 title or headline options, each built from the core claim. For research, follow
  the pattern in `genre-research.md` §Judul.
- List every `[ISI]` and `[CEK]` item in one block at the end, so the user knows exactly
  what to bring.
- One line: next step (e.g. "Konsultasikan ke dosen dengan lampiran catatan sumber",
  "Kirim ke lugas untuk drafting").

## Output format

Use this skeleton. Keep it in the user's language. No emoji. No motivational filler.

```
## 1. Peta inti
(table from Step 1)

## 2. Kerangka
(numbered sections, each with Job / Isi / Bukti / Panjang)

## 2b. Kerangka lampiran        (dokumen akademik & organisasi saja)
Lampiran n. Judul  [WAJIB/BIASANYA/JIKA ADA]
  Tugas / Isi / Dirujuk dari / Kapan dikumpulkan

## 3. Hasil cek
| Butir | Status | Perbaikan |

## 4. Opsi judul
1. ...

## 5. Yang perlu kamu lengkapi
- [ISI: ...]
- [CEK: ...]
```

**Output language follows the user.** Write in the language of the user's sentences,
and say so in one line at the top of the first reply, with the offer to switch, e.g.
"Kerangka ditulis dalam bahasa Indonesia; bilang kalau mau versi English/العربية/…".
Campus-mandated names (bab, bagian) stay in the guideline's language.

If the user writes in English, translate the headers (Core map, Outline, Check,
Title options, What you need to supply) and use `[FILL: ...]` / `[VERIFY: ...]`.
Section fields are always **Tugas/Job, Isi/Content, Bukti/Evidence, Panjang/Length**.

Section 4 is skipped for study outputs (family F) and for documents whose title is fixed
by someone else (e.g. LPJ with a given event name); write "Judul mengikuti ..." instead.

For study mind maps (family F), also output a Mermaid `mindmap` block. For research,
also output the Mermaid flow in `genre-research.md` if the user wants a diagram.

## Diagram and flowchart output (HTML)

When the output includes a diagram, flowchart, kerangka pikir, alur penelitian, or mind
map as an **HTML page**, build it from `assets/flowchart-template.html`. Non-negotiable:

1. **Language switch** — diagram text in at least id and en; UI, headings, and captions
   in id/en/es/fr/zh/ar; `dir="rtl"` for Arabic. Set `DEFAULT_LANG` to the user's language.
2. **Theme switch defaulting to light** (saves printer ink), with dark and "follow
   system" options. Never default to dark.
3. **Print stylesheet that always prints light**, whatever the screen theme: both light
   and dark SVGs are rendered up front and print shows the light one; the print CSS
   uses `!important` and lets tall diagrams fit an A4 page.
4. Node text keeps `[ISI]`/`[FILL]` markers; no invented numbers inside diagrams.

After delivering, state in one line: default is light theme and print is always light;
language and theme can be switched from the top bar. If the user only wants Mermaid in
chat, give the Mermaid block and offer the HTML version in one line.

## Modes of depth

- **Cepat** (default for persuasion, short reports, study maps, video under 3 minutes):
  Step 1 table with 5 rows (Reader, Should, Is, Gap, Action), outline, checks U1, U2, U4,
  U8, U9 **plus every check of the genre file**.
- **Lengkap** (default for skripsi, tesis, disertasi, proposal, laporan KKP, LPJ,
  technical spec, anything over ~10 pages): everything above, plus §2b (lampiran) and
  the mapping table required by the genre file — for UAJM skripsi that is
  `rumusan → tujuan → bab → bukti → kesimpulan → saran`; for LPJ it is
  `tujuan → indikator → realisasi → kendala → rekomendasi`.

The user can override with "versi cepat" / "versi lengkap".

## What this skill will not do

- Write a full skripsi, tesis, or assignment for submission as the student's own work.
  It builds the outline and explains the reasoning so the student can write it and defend
  it. If asked to write the whole thing, build the outline and say plainly that the
  student should draft it, with help per section if they want.
- Promise a plagiarism or AI-detector score. Clean structure and honest wording lower
  similarity; no tool can guarantee a number.
- Fabricate data, respondents, or literature to fill a gap.

## Files

| File | When to read |
|---|---|
| `references/genre-*.md` | Step 2, only the one for the genre |
| `references/genre-thesis.md` | Tesis (S2) or disertasi (S3), after `genre-research.md` |
| `references/genre-organizational.md` | Index for family G; AD/ART, surat, notulen |
| `references/org-proposal-kegiatan.md` | Proposal kegiatan + RAB |
| `references/org-lpj.md` | LPJ + tabel realisasi anggaran |
| `references/org-sk.md` | SK (menimbang/mengingat/memutuskan), surat penugasan, surat pengantar SK |
| `references/full-outlines.md` | Full outline trees: front matter → Bab I–V/VII → lampiran, for skripsi/tesis/disertasi |
| `assets/flowchart-template.html` | Any diagram/flowchart delivered as HTML |
| `references/uajm-kkp.md` | Laporan KKP/magang at UAJM FTI |
| `references/uajm-usulan-ta.md` | Usulan TA / proposal / Ringkasan Kapasitas Diri at UAJM FTI |
| `references/uajm-skripsi.md` | Skripsi/TA at UAJM FTI — Bab I–V + 15 front-matter items |
| `references/uajm-format.md` | Any UAJM formatting, citation style, or length question |
| `references/campus-ui.md`, `campus-ugm.md`, `campus-itb.md`, `campus-unhas.md`, `campus-its.md`, `campus-binus.md`, `campus-unm.md`, `campus-umi.md`, `campus-unair.md`, `campus-ub.md`, `campus-ipb.md`, `campus-unpad.md`, `campus-uin-alauddin.md`, `campus-unismuh.md`, `campus-undip.md`, `campus-uns.md`, `campus-upi.md`, `campus-uny.md`, `campus-uii.md`, `campus-umy.md`, `campus-telkom.md`, `campus-uin-jakarta.md` | User names that campus — verified rules, sources, and what is faculty-specific |
| `references/international.md` | Foreign university, thesis by publication, or a citation style question |
| `references/pedoman-adapter.md` | Every academic document not covered by a `uajm-*` file |
| `references/appendices.md` | Any document with lampiran — read at Step 2, not at the end |
| `references/summarize-to-outline.md` | Mode Rangkum: existing files → one outline |
| `references/languages.md` | Output language is not Indonesian, or is mixed |
| `references/checklist.md` | Step 3, every time |
| `references/sources.md` | Any time a citation or framework name is used |
| `references/examples.md` | When unsure what a finished outline looks like |

Read only what the routing tables call for. A landing page outline never needs the
UAJM files; a KKP outline never needs the persuasion file.
