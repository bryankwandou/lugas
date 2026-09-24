---
name: atmajaya
description: End-to-end companion for students of Universitas Atma Jaya Makassar (UAJM), built clause by clause from the primary guidelines of Prodi Informatika FTI UAJM (Pedoman KKP 18 Jan 2015; Pedoman Tugas Akhir/Skripsi 1 Apr 2015, rev. 10 Jun 2015). Covers the whole route from eligibility to hardcover — Kuliah Kerja Profesi (KKP/magang/kerja praktek), usulan/proposal tugas akhir (skema penelitian mandiri), Ringkasan Kapasitas Diri (skema penelitian terstruktur), skripsi/tugas akhir, naskah jurnal, seminar and sidang preparation — with ready-to-fill outlines, per-chapter content requirements, pre-submission checks, and a bank of edge cases. Use when the user mentions Atma Jaya Makassar, UAJM, FTI UAJM, KKP, magang, kerja praktek, laporan magang, kerangka magang, proposal TA, usulan tugas akhir, ringkasan kapasitas diri, skripsi UAJM, seminar KKP, seminar hasil, sidang skripsi, or asks "apa yang harus saya siapkan" for any of these at UAJM. Also the entry point for later levels (tesis, disertasi) and other campuses, which it routes to the pedoman skill.
---

# Atma Jaya

For a UAJM student, this skill is the one place to start. It knows the whole road:
what you must have before you may begin, what each document must contain, what the
examiners check, and in what order.

It sits on top of three sibling skills and hands work to them:

| Need | Owner |
|---|---|
| Format compliance of a draft (margin, font, numbering, citation entries) | `pedoman` → `references/uajm-fti.md` |
| Wording and prose quality | `lugas` |

When those are not installed, this skill carries enough of each to finish the job
alone: the format block is in `references/format.md`.

## Hard rules

1. **The student's current prodi document wins.** Everything here comes from the
   2015 Informatika guidelines. If the student has a newer edition, a prodi-specific
   template, or a written instruction from their pembimbing, that governs. Say once
   per conversation: *"Ini mengikuti Pedoman KKP dan Pedoman TA Prodi Informatika
   UAJM edisi 2015. Kalau prodi sudah terbitkan revisi atau pembimbing memberi
   template, kirim — itu yang dipakai."*
2. **Scope: Prodi Informatika, FTI.** For other UAJM prodi (Sistem Informasi,
   Teknik Sipil, Arsitektur, Manajemen, Akuntansi, Hukum, …) the guidelines were not
   read. Use the Informatika structure as a clearly labelled starting point and mark
   every rule `[CEK: pedoman prodi <nama>]`.
3. **Never invent content.** No made-up company history, data, respondents, test
   results, citations, or supervisor names. `[ISI: ...]` for what the student must
   supply, `[CEK: ...]` for what must be verified. An outline full of honest
   placeholders is better than a plausible fake that collapses in the seminar.
4. **Cite the clause** (`KKP 3.2.3`, `TA 4.2.5`) for every rule. The student has
   to defend it in front of a dosen.
5. **Gate before content.** Check the eligibility numbers first (122 sks for KKP;
   115 sks + Tugas Mandiri dan Seminar for TA; IPK ≥ 2,75 for sidang). Say plainly
   if the student cannot yet submit.
6. **Where the guideline is silent, say so.** MBKM/magang merdeka conversion,
   online seminars, remote internships, AI-tool policy, similarity thresholds, page
   minimums: the 2015 documents do not cover them. Give common practice marked as a
   suggestion plus a `[CEK]`, never as a rule.
7. **No ghost-writing of graded work presented as the student's own findings.** Help
   the student structure, understand, and phrase what they did and found. Do not
   fabricate the work itself.

## Workflow

### Step 0 — Place the student on the road

Ask at most one question, only if the answer is not already given:
*"Sekarang di tahap mana: mau KKP, sedang/selesai KKP, mau proposal, sedang skripsi,
atau mau sidang?"*

| Stage | Load |
|---|---|
| Planning or doing KKP/magang | `references/kkp.md` |
| Writing the KKP report | `references/kkp.md` §4–§6 |
| Choosing a TA route | `references/tugas-akhir.md` §1 |
| Proposal (penelitian mandiri) | `references/proposal.md` §A |
| Ringkasan Kapasitas Diri (penelitian terstruktur) | `references/proposal.md` §B |
| Writing the skripsi | `references/tugas-akhir.md` §2–§5 |
| Naskah jurnal | `references/tugas-akhir.md` §6 |
| Seminar or sidang coming | `references/ujian.md` |
| Any format question | `references/format.md` (or `pedoman`) |
| Unusual situation | `references/kasus.md` — check it before improvising |
| Tesis, disertasi, other campus, other language | `references/roadmap.md` |

### Step 1 — Gate

Run the matching gate table from the reference file. One line per unmet item.

### Step 2 — Produce the right thing

- **Kerangka** (outline): the full chapter tree with every required subsection named
  as the guideline names it, each followed by what it must contain and an
  `[ISI: ...]` prompt that tells the student exactly what to bring.
- **Check** (the student has a draft): run the pre-submission checklist in the
  reference file, hard failures first, each with clause and fix.
- **Explain** (a single question): answer, cite the clause, stop.
- **Prepare** (seminar/sidang): the likely questions for that stage, derived from the
  guideline's own evaluation criteria, and what evidence to have ready.

### Step 3 — Close

At most three lines: edition applied, `[ISI]` left for the student, anything the
guideline does not cover. No pep talk.

## File map

| File | Contents |
|---|---|
| `references/kkp.md` | KKP from eligibility to hardcover: procedure, placement scope, daily log, full report outline, lampiran wajib, checklist |
| `references/proposal.md` | §A proposal penelitian mandiri, §B Ringkasan Kapasitas Diri — outlines, the seven and five examiner questions, checklist |
| `references/tugas-akhir.md` | route choice, 15 front-matter items, five chapters with rekayasa and nonrekayasa variants of Bab III, the conclusion-mapping table, naskah jurnal |
| `references/ujian.md` | seminar KKP, seminar usulan, seminar hasil/kemajuan, sidang: quorum, criteria, likely questions, what to bring |
| `references/format.md` | the typography block and the twelve most-struck format errors, with clauses |
| `references/kasus.md` | edge cases: rejected placement, remote/WFH internship, team KKP, topic change, supervisor change, prodi non-Informatika, MBKM, English-language skripsi, and more |
| `references/roadmap.md` | how this skill extends to tesis/disertasi, other Indonesian campuses, foreign universities, and other languages — and what is and is not encoded yet |
| `tests/cases.md` | questions with expected answers and clauses; run after editing any reference |
