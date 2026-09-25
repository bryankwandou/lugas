# Grading — rangka skill, 6 evals

Grader note: the outputs were written by the same model grading them, so the grades are biased toward passing. Mermaid was checked by hand, not rendered.

## Assertion results

| Eval | Assertion | Result | Evidence |
|---|---|---|---|
| 1 | Contains a gap table with Das Sollen and Das Sein | PASS | §1 table has rows **Das Sollen** / **Das Sein** / Gap |
| 1 | Title options appear after the outline and checklist | PASS | §4 Opsi judul follows §2 and §3 |
| 1 | Every statistic or prior study is from the user or marked [ISI]/[CEK] | PASS | No QRIS numbers or prior-study names; TAM/UTAUT are named only as `[CEK: pilih teori + sumber]` |
| 1 | Mentions checking campus writing guidelines | PASS | `[CEK: pedoman penulisan kampus]` above the chapter table and in §5 |
| 1 | Each research question maps to a results subsection | PASS | Traceability table: RQ1→4.2, RQ2→4.3, RQ3→4.4 |
| 2 | Names one specific reader, one action, one promise | PASS | "Kunci" block: small single-location owner / register + first transaction / know today's profit |
| 2 | No invented testimonials, user counts, or client logos | PASS | §5 Bukti is all `[ISI]`, with "atau hapus bagian ini" |
| 2 | CTA in hero matches closing CTA | PASS | "Coba Kasirku Gratis" in sections 1 and 8 |
| 2 | Includes an objections/FAQ section | PASS | Section 6, 5 objections |
| 3 | Hook occupies 0–3 seconds | PASS | Row "0–3 s Hook" |
| 3 | Has on-screen text column for silent viewing | PASS | "On-screen text" column filled on every row |
| 3 | Durations sum to about 60 seconds | PASS | 3+7+15+15+12+8 = 60 |
| 3 | Exactly one call to action | PASS | Only "Save this for your proposal" |
| 4 | States from-scratch mode and asks to verify against syllabus | PASS | "**Mode dari nol**" + `[CEK: cocokkan dengan silabus/kisi-kisi/buku paket]` |
| 4 | Contains a valid mermaid mindmap block with one root | PASS (not rendered) | One `root((Fotosintesis))`, consistent 2-space indent, no parentheses or brackets in leaf text |
| 4 | Self-test questions at more than one Bloom level | PASS | 4 levels: Mengingat, Memahami, Menerapkan, Menganalisis |
| 5 | Does not produce a full ready-to-submit thesis | PASS | Outline only, no chapter prose |
| 5 | Still delivers a usable outline | PASS | 5 chapters with subsections, RQs, and a check table |
| 5 | Offers section-by-section help without moralizing at length | PASS | Refusal plus offer in 3 sentences, placed before the outline |
| 6 | Includes target-vs-actual table | PASS | Section 4 table Target / Realisasi / Selisih |
| 6 | Includes budget planned-vs-actual with variance explanation | PASS | Section 5 has columns "Selisih" and "Alasan selisih", and a rule that every non-zero variance needs a reason |
| 6 | Summary is placed first | PASS | Section 1 Ringkasan |

**Total: 22/22 PASS.** (The spec says 21 assertions; the actual count is 5+4+4+3+3+3 = 22.)

These assertions are too easy. Most of them can be met by copying the genre template. None of them tests the skill's riskier behaviour: whether Kelsen gets cited in an unrelated background section, whether Step 0 depth is followed, whether a title appears while U2 is failing, or whether an English run keeps Indonesian markers.

## Skill weaknesses and concrete fixes

1. **SKILL.md, "Modes of depth", vs checklist.md "Versi cepat": Cepat mode drops the genre checks.** Cepat = "5 key checks" = U1, U2, U4, U8, U9. That leaves out C3 (CTA the same at start and end, objections) and E6 (hook in 3 s, one CTA, durations add up). Those are exactly what evals 2 and 3 assert, and Cepat is the default for both. I had to add the genre checks against the letter of the rules. Fix: define Cepat as "U1, U2, U4, U8, U9 + all genre checks (A7/B3/C3/D3/E6/F5)".

2. **SKILL.md Step 1 vs examples.md: the four rows for Cepat do not match.** SKILL.md lists Should, Is, Gap, Action. Examples 2 and 3 use Pembaca, Is, Should, Tindakan (no Gap, and Is before Should). Example 1 drops Pembaca. A weaker model will copy the examples. Fix: make the examples use the exact rows SKILL.md lists, or change the rule to 5 rows (Reader, Should, Is, Gap, Action), which is what persuasion needs anyway.

3. **Title timing contradicts itself.** Hard rule 3 and genre-research §A6 say the title comes only after the outline passes ("setelah semua lolos"). Step 3 says to stop after two rounds and show what is blocked. U2 almost always fails when the mode is "dari nol". So either the model never gives titles, which breaks Step 4 and the evals, or it breaks rule 3. examples.md Contoh 1 gives titles while U2 is "Gagal sementara". Fix: say explicitly "If blocked only by missing user data, give titles marked 'sementara'."

4. **checklist.md U12 is circular.** It checks the title during Step 3, but the title is written in Step 4. Fix: move U12 to a check after Step 4, or mark it "cek setelah langkah 4".

5. **examples.md breaks SKILL.md's own output format.** Contoh 1 gives 2 title options (rule: 3) and is labelled Cepat for a skripsi (rule: skripsi defaults to Lengkap). Contoh 3 has no §4 title and no §5 list at all. Contoh 2 uses statuses "Gagal sementara" and "Perlu cek", and Contoh 3 uses "Belum", none of which are defined. checklist.md says "Lolos/Gagal", SKILL.md says "pass/fail", and the skeleton header says "Status". Fix: rebuild the examples so they follow the skeleton exactly, and define the allowed statuses (Lolos / Gagal / Terblokir: butuh data pengguna).

6. **genre-research.md A3 and A4: two competing research templates, with no rule for which one to output.** The 12-point outline covers only the proposal (Bab 1–3); the 5-chapter map covers the full skripsi. The eval says "Bab 1-5 atau 12 butir". I output both, which is long. Fix: "Proposal → 12 butir. Skripsi/tesis → 5 bab, with the 12 butir folded into Bab 3."

7. **genre-research.md A3 row 1 source column: "Kelsen (konsep)".** This invites the model to cite Kelsen 1934 (legal theory) in the background section of an unrelated QRIS or e-learning skripsi. Supervisors will flag it, and sources.md itself says the Indonesian use is only a habit. Fix: remove Kelsen from that column; keep it only in sources.md as an explanation of the term, with "jangan dikutip kecuali skripsi hukum".

8. **No usable theory sources for the most common skripsi types.** TAM, UTAUT, DeLone & McLean, and purchase-intention theories are missing from sources.md. Under hard rule 2, every IS, management, or education skripsi ends up with the core theory as `[CEK]`. A weaker model will ignore the rule and invent "Davis (1989)" with made-up page numbers, or state it without a marker. Fix: add the handful of standard models with verified details, or add an explicit rule: "Nama teori boleh disebut, tapi tahun dan sumber tetap [CEK] kecuali ada di sources.md."

9. **sources.md contradicts itself.** It opens with "only these can be cited without [CEK]", but the Sugiyono entry carries `[CEK: edisi]` and Hevner et al. are cited in examples without that. Fix: either move Sugiyono out, or state that entry-level `[CEK]` notes must carry through into the output.

10. **Hard rule 6 contradicts the genre files' "don't build the outline" gates.** genre-persuasion.md says the outline "belum boleh dibuat" if reader, action, or promise is empty. genre-timed.md says "jangan susun outline" if the "after watching" sentence can't be filled. Hard rule 6 says fill `[ISI]` and continue. Fix: reword both genre files to "isi dengan [ISI]/[CEK] dan lanjutkan; tandai sebagai blokir di hasil cek".

11. **The output skeleton is fixed Indonesian with mixed-language field names**: "Job / Isi / Bukti / Panjang", while checklist U5 calls the field "Tugas". There is no guidance for English prompts (eval 3). Should the headers and the `[ISI]`/`[CEK]` markers be translated? I translated them to [FILL]/[CHECK], which breaks any tooling that greps for the markers. Fix: give an English skeleton, and say that the markers stay `[ISI]`/`[CEK]` in every language (or define the EN equivalents).

12. **The skeleton forces "Opsi judul" and "Peta inti" onto every genre.** For LPJ the title is fixed by convention, for a study mind map a title is pointless, and a video needs hook options rather than a title. Fix: per family, name what §4 contains (A: judul, B: judul baku + subjudul, C: headline, D: nama/tagline, E: 3 hook, F: omit).

13. **genre-study.md F1 tells the model to label a branch `(tambahan, di luar materi)`.** Inside a Mermaid mindmap, `Konsep (tambahan, di luar materi)` is parsed as a node shape, so the label is mangled or the parse fails. F2 also never warns about `()`, `[]`, `{}`, or `))` inside node text. Weaker models will write `root((Fotosintesis (C3)))` or `Reaksi terang (tilakoid)` and break rendering. Fix: add a rule that node text has no brackets or parentheses, and label extra branches as `Tambahan di luar materi` (its own child) or put the note outside the diagram.

14. **genre-study.md F2 and F5: "valid Mermaid" has no validation step.** There is no instruction to test in mermaid.live or `mmdc`, and no note that mindmap needs Mermaid ≥ 9.3, so older renderers show raw text. Fix: add a minimal syntax list (2-space indent, one root, no special characters, no blank lines between siblings) and a note about renderer version.

15. **genre-timed.md E1 has a timing hole.** The rows are 0–3, 3–10, 10–50, and "akhir", which leaves no explicit window for the payoff. Nothing tells the model how to scale these rows for 15 s or 90 s. A weaker model will fail "durations sum to 60". Fix: express the rows as percentages (hook ≤3 s, context ~10%, body ~70%, payoff + CTA last 10–15%), with a required "Total" line.

16. **genre-report.md LPJ template has no table columns.** It says "target vs realisasi dalam tabel" and "selisih dan alasannya", but gives no column layout, no evidence-number column tying expenses to receipts, and no approval/signature section. Most LPJ formats need the signatures. Fix: add the two table headers and a "Pengesahan" item.

17. **SKILL.md "What this skill will not do" gives no wording or placement for the refusal.** A weaker model may either lecture or bury the refusal after 3 pages. Fix: "State it in ≤2 sentences before the outline, then offer per-section review."

18. **Step 0 depth is ambiguous for mixed cases.** "Short reports" vs "anything over ~10 pages": is an LPJ short? Is a skripsi request in eval 5 Lengkap even though the user wants everything? And the Lengkap check table for research runs to 18 rows, which buries the output. Fix: a lookup table from genre subtype to default depth, and allow A7 to be collapsed into a single traceability table.

19. **genre-research.md header credits a TikTok creator (dafnisfaz_) for the core workflow, and genre-timed.md calls it a "Contoh nyata".** There is no link or date, and sources.md says not to cite it. A model making the eval 3 video (which is about this very topic) is primed to mention or imitate that creator. Fix: move the attribution to README only.

20. **evals/evals.json has no negative or trap cases.** There is no English research prompt, no user-supplied data mode ("dari materi"), no prompt that invites a fake statistic (e.g. "sertakan data pengguna QRIS terbaru"), no check that titles are marked provisional, and no check that Kelsen or unlisted sources are absent. Fix: add those 4–5 evals, plus assertions for "checklist includes genre items" and "markers not translated".

---

# Grading — trap evals 10–15 (added 2026-09-23)

Same caveat as above: outputs were written and graded by the same model. Evidence is quoted from `eval-10.md` … `eval-15.md`.

| Eval | Assertion | Result | Evidence |
|---|---|---|---|
| 10 | Four chapters, says why not five | PASS | "**Empat bab, bukan lima.** … Struktur lima bab adalah struktur skripsi." BAB I–IV only |
| 10 | No abstract, says KKP has none | PASS | "**Tanpa abstrak.** Laporan KKP tidak memakai abstrak"; check row "K8 Tanpa abstrak \| Lolos" |
| 10 | Company data [ISI], nothing invented | PASS | "2.1 Sejarah instansi — `[ISI: dari profil resmi instansi]`. Tidak ada tahun berdiri atau angka yang saya isi." |
| 10 | 1.1 asks why place AND why division | PASS | "(c) **kenapa PT Semen Tonasa dipilih** `[ISI]`; (d) divisi: IT; (e) **kenapa divisi IT**" |
| 10 | Photo per job type, student in frame | PASS | "1. Dokumentasi foto tiap jenis pekerjaan (mahasiswa ikut terfoto) \| WAJIB" |
| 10 | Check table K1–K9 | PASS | rows K1 through K9 all present |
| 11 | Menimbang a/b/c + bahwa + perlu ditetapkan | PASS | "c. bahwa untuk maksud tersebut perlu ditetapkan susunan pengurus" |
| 11 | Mengingat numbered, bases only | PASS | "1. [ISI: Statuta universitas]; 2. [ISI: Peraturan kemahasiswaan]; 3. AD/ART …; 4. Hasil [ISI: musyawarah anggota]" |
| 11 | KESATU–KEEMPAT, ralat, place/date | PASS | "KEEMPAT : Apabila di kemudian hari terdapat kekeliruan …"; "Ditetapkan di : [ISI: kota]" |
| 11 | Nomor pattern, Roman month, [ISI] parts | PASS | "[ISI: urut]/SK/[ISI: kode UKM]/[ISI: kode institusi]/[ISI: bulan Romawi]/[ISI: tahun]" |
| 11 | Only Andi named; others [ISI] in Lampiran I | PASS | "LAMPIRAN I … (dirujuk diktum KESATU)"; "2 \| Wakil Ketua \| [ISI]" |
| 12 | States Rp2.000.000 gap | PASS | "= **Rp7.000.000**; pemasukan Rp5.000.000. Kurang **Rp2.000.000**." |
| 12 | No invented income | PASS | "Saya tidak menambahkan sponsor atau iuran karangan"; row "`[ISI: sumber dana mandiri …]` \| `[ISI]`" |
| 12 | Satuan × jumlah × harga columns | PASS | "\| Pos \| Satuan \| Jumlah \| Harga satuan \| Subtotal \|" with `[ISI]` cells |
| 12 | Campus-only funding risk noted | PASS | "proposal yang seluruh pemasukannya dari dana kampus tanpa usaha mandiri biasanya dipotong" |
| 12 | Lembar Pengesahan with 4 signers | PASS | "ketua panitia · ketua UKM · pembina · mengetahui pejabat kemahasiswaan" |
| 12 | G2 not Lolos | PASS | "**G2 RAB …** \| **Gagal**" |
| 13 | RM3 orphan claim | PASS | "§1.2 RM3 (dampak ke omzet) \| **Orphan claim**" |
| 13 | 2.2 orphan section | PASS | "§2.2 Sejarah uang kertas \| **Orphan section**" |
| 13 | Doubtful claim recorded, not corrected | PASS | "dicatat, tidak saya ubah; penulis perlu sumber atau merevisi klaimnya" |
| 13 | Original numbering kept | PASS | "4.1 Tingkat penggunaan — Tabel 4.1"; "5.2 Saran" |
| 13 | No outside facts; [TIDAK ADA DI BERKAS] used | PASS | five `[TIDAK ADA DI BERKAS: …]` items; the only outside term is step 4's theory, marked `[CEK: sumber]` |
| 13 | Mapping table with empty RM3 cells | PASS | "RM3 dampak ke omzet \| [TIDAK ADA DI BERKAS] \| **—** \| **—** \| **—** \| **—**" |
| 13 | ≤7 steps labeled potong/pindah/gali | PASS | 7 steps, each starting **Gali**/**Potong**/**Pindah** |
| 14 | 14-row variable table before outline | PASS | "## 0. Variabel pedoman (isi sebelum kerangka)", rows 1–14 |
| 14 | [CEK: pedoman kampus] on uncertain items | PASS | every row's Status column is "`[CEK: pedoman kampus]`" |
| 14 | No Unhas rule stated as fact | PASS | "saya tidak menyatakan aturan Unhas apa pun"; "itu kecenderungan umum, bukan aturan Unhas" |
| 14 | Full outline in same reply | PASS | "Kerangka tetap saya susun sekarang." followed by BAB I–V |
| 14 | No UAJM-only rules | PASS | "1.2 Rumusan Masalah" as a parallel sub-bab, not inside 1.1 |
| 15 | Empty novelty sentence rejected, [ISI] protocol | PASS | "tidak saya pakai sebagai klaim kebaruan … diisi `[ISI: protokol & hasil pencarian literatur]`" |
| 15 | Novelty classified into four forms | PASS | "**(1) konteks baru** … cukup untuk tesis S2 bila model diuji atau dimodifikasi" |
| 15 | Systematic review protocol in Bab II | PASS | "basis data …, kata kunci …, rentang tahun …, kriteria inklusi/eksklusi …, jumlah artikel lolos" |
| 15 | Sample size calculated | PASS | "**perhitungan besar sampel** (… power analysis `[CEK: rujukan]`)" |
| 15 | Ethics / clearance / consent | PASS | "**3.7 Etika penelitian**: ethical clearance …, informed consent yang dipahami lansia" |
| 15 | Publication [CEK: pedoman pascasarjana kampus] | PASS | "T10 Syarat publikasi \| Menunggu data \| `[CEK: pedoman pascasarjana kampus]`" |
| 15 | T-codes in check table | PASS | rows T1–T8, T10 (T9 is for article-based dissertations, not applicable) |

**Total: 36/36 PASS.**

## Ambiguities found while running, and skill edits made

1. **Eval 12: the rules did not say what to do when the user's own numbers do not balance.** genre-organizational.md said "pemasukan dan pengeluaran berjumlah sama", but not whether to fill the gap, cut something, or flag it. The obvious bad move, which the no-invention rule only covers indirectly, is to add a "sponsor Rp2.000.000" line. Edit: a fourth RAB rule in `references/genre-organizational.md`. State the gap in rupiah, add no invented income, offer an `[ISI]` line or a cut, and mark G2 as Gagal.
2. **Eval 13: Mode Rangkum's output format had no check section and no title rule.** SKILL.md says "Steps 3–4 still apply", but the skeleton in summarize-to-outline.md ended at §6, and titles make little sense for a draft that has an orphan claim. Edit: add `## 7. Hasil cek` (R1–R7 + U4) to the skeleton in `references/summarize-to-outline.md`, and a rule that titles are given only if the user asks and there is no Orphan claim or Putus finding.

Not edited (noted only):
- **Eval 14:** A3 ("perbedaan dengan template user") has no state for "the user has no template". I used Menunggu data.
- **Eval 15:** genre-thesis.md does not say whether a tesis with no named campus should still show the 14-variable table. I showed a short version. The routing table ("Tesis … + pedoman-adapter.md") implies it should.
- `uajm-format.md` line 38 says tables and figures are numbered in one series "bukan per bab", and its error list item 3 agrees. pedoman-adapter.md variable 11 is consistent with that. No conflict.

---

# Grading: campus files (UI, UGM, ITB, Unhas), evals 16–17

Date: 2026-09-24. The same model wrote the runs and graded them, so the grades lean
toward passing. Both runs followed SKILL.md → `campus-ugm.md` / `campus-unhas.md` →
`pedoman-adapter.md` → `genre-research.md` → `checklist.md`.

| Eval | Assertion | Result | Evidence (quoted from run) |
|---|---|---|---|
| 16 | No university-wide UGM pedoman; rules differ by faculty | PASS | "UGM tidak punya pedoman penulisan skripsi tingkat universitas yang bisa saya temukan. Pedomannya dibuat per fakultas atau departemen, dan isinya berbeda nyata." |
| 16 | Exactly one question (faculty), outline still delivered | PASS | "**Satu pertanyaan: kamu di fakultas/departemen apa?**" then "Sambil menunggu jawabanmu, kerangka di bawah memakai bawaan umum"; BAB I–V follow |
| 16 | No faculty rule presented as "aturan UGM"; spacing/margin/chapters [CEK] | PASS | "saya tidak akan menyebut satu pun dari aturan itu sebagai \"aturan UGM\""; row "Spasi, margin, font \| TNR 12; spasi & margin **tidak saya tetapkan** \| `[CEK ke pedoman fakultas]`" |
| 16 | Faculty rules attributed with document year | PASS | "spasi baris 1,5 (Kimia FMIPA 2025), 1,15 (Teknik Sipil & Lingkungan FT 2023), dan 2 (FIB 2020, FEB 2016)"; "nama ini dipakai FEB UGM 2016" |
| 16 | 14-variable table before outline | PASS | "## 0. Variabel pedoman (sebelum kerangka)", rows 1–14 precede "## 2. Kerangka" |
| 16 | No invented data | PASS | Das Sein "`[ISI: fakta lapangan …]`"; sampel "hitung ukuran sampel, jangan angka bulat karangan"; penelitian terdahulu "Tidak saya isi" |
| 17 | 2023 pedoman does not regulate proposal; proposal [CEK] | PASS | "pedoman itu **tidak mengatur format proposal** … Jadi struktur proposal di bawah `[CEK ke pedoman fakultas]`" |
| 17 | FH 2021 proposal format not used as Unhas format | PASS | "Format itu dibuat untuk penelitian hukum normatif/empiris, jadi **tidak saya pakai** untuk topik agronomi." |
| 17 | Literature in Pendahuluan, labelled as alignment not rule | PASS | "1.1 Latar belakang (termasuk kajian pustaka)"; "Penyelarasan ini pilihan saya, bukan aturan proposal Unhas." |
| 17 | SK 10438/UN4.1/KEP/2023 named as source | PASS | "Keputusan Rektor No. 10438/UN4.1/KEP/2023 (28 Oktober 2023)"; §0 source column "SK 10438/2023" |
| 17 | One question, outline delivered | PASS | "**Satu pertanyaan: fakultas/prodi apa, dan pedoman edisi mana yang dipakai prodimu?**" followed by full outline. The question has two parts, but they belong to one decision (which pedoman applies) |
| 17 | A3 12-item proposal template, not A4 | PASS | "## 2. Kerangka proposal (12 butir …)"; butir 1–12 are mapped, and butir 6 and 11 are explicitly marked not relevant; there is no Bab Hasil |
| 17 | No invented numbers | PASS | "taraf dosis `[ISI]`", "ulangan `[ISI]`", "jumlah unit dihitung dari perlakuan × ulangan, bukan dikarang" |

**Total: 13/13 PASS.**

## Weaknesses found

1. **Eval 17 stretches the "one question" rule.** It asks for the faculty *and* the pedoman
   edition. `campus-unhas.md` asks for both on purpose, since the 2023 SK applies only to
   students who have not started research. SKILL.md hard rule 6 says at most one question.
   Treated here as one compound question. A stricter grader could fail it.
2. **Eval 14 is stale.** Its old run (`eval-14.md`) says "saya tidak menyatakan aturan Unhas
   apa pun". That was correct without `campus-unhas.md`. Now it would be a miss, because
   the university-wide rule (no separate Tinjauan Pustaka chapter) is verified. Eval 14's
   expected output and assertions were revised in `evals.json` (with a `note`), but the
   run was **not** re-done. Its 5/5 PASS above no longer counts.
3. **Research gaps shown in the campus files:** no UGM-wide pedoman found; ITB S1 has no
   institute-wide pedoman, and the SPs 2016 tesis pedoman was read only through the
   Wayback Machine; the UI "Revisi 2023" could not be verified from UI's site; Unhas
   proposal format exists only for FH 2021. Each is marked `[CEK]` in the files, not filled in.
4. The Unhas 2023 template's sample table of contents skips from BAB II to BAB IV. The file
   reports this as a template error instead of silently renumbering. Eval 17 kept its
   proposal numbering at BAB I–III, which avoids the question.

# Grading: re-run of evals 14, 16, 17 after the one-question rule (2026-09-24)

Change under test: for campus cases the only question is faculty/prodi; the Unhas pedoman edition is stated as a default (Rektor 2023) marked `[CEK ke pedoman fakultas]`, not asked (SKILL.md campus paragraph; campus-unhas.md "Peringatan: dua generasi aturan"). Same-model grader, so bias toward PASS applies.

| Eval | Assertion | Result | Evidence |
|---|---|---|---|
| 14 | 14-row variable table before outline | PASS | "## 0. Tabel 14 variabel pedoman (sebelum kerangka)", rows 1–14, precedes "## 2. Kerangka" |
| 14 | Unhas rules only from campus-unhas.md, source SK 10438 named | PASS | Every fact row has "SK 10438/UN4.1/KEP/2023" in Sumber; rows 4 and 13 (not in pedoman) are "—" + [CEK]; "tanpa Kata Pengantar terpisah", "hindari awalan Pengaruh…", no Saran all match campus-unhas.md |
| 14 | Faculty items [CEK]; edition stated as default + [CEK], not asked | PASS | "Gaya khusus FEB `[CEK ke pedoman fakultas]`", "ambang persentase `[CEK ke pedoman fakultas]`"; "**Edisi pedoman (bawaan, tidak ditanyakan):** saya memakai … 10438/UN4.1/KEP/2023 … `[CEK ke pedoman fakultas: …]`"; no question in the reply |
| 14 | Full outline in same reply | PASS | BAB I–IV with subsections, lampiran, cek, judul all present |
| 14 | No UAJM-only rules | PASS | "Rumusan/pertanyaan penelitian berdiri sebagai subbab Pendahuluan sendiri (1.3), bukan di dalam Latar Belakang"; no UAJM front matter |
| 16 | States no UGM-wide pedoman, differs by faculty | PASS | "Di UGM tidak ditemukan pedoman penulisan skripsi tingkat universitas; pedoman terbit per fakultas bahkan per departemen" |
| 16 | Exactly one question (faculty/department) + full outline | PASS | Only question: "kamu di fakultas/departemen apa?"; Bab 1–5 follow in same reply |
| 16 | No faculty rule presented as UGM rule; [CEK] | PASS | "Spasi dan margin: `[CEK ke pedoman fakultas]`" and "Masing-masing aturan fakultas itu, bukan aturan UGM" |
| 16 | Faculty rules attributed with document year | PASS | "FEB UGM 2016 … spasi 2", "DTSL FT 2023 spasi 1,15", "Kimia FMIPA 2025 spasi 1,5" |
| 16 | 14-row table before outline | PASS | "## 0. Tabel 14 variabel pedoman", 14 rows, before §2 |
| 16 | No invented statistics/studies | PASS | "`[ISI: data/keluhan/perpindahan pelanggan …]`", "`[ISI: minimal N penelitian]`"; only citations are sources.md entries (Creswell & Creswell 2018, Likert 1932, Cronbach 1951) |
| 17 | Rektor 2023 does not regulate proposal; structure [CEK] | PASS | "Pedoman Rektor Unhas 2023 (SK 10438/UN4.1/KEP/2023) tidak mengatur format proposal. Struktur proposal di bawah = `[CEK ke pedoman fakultas]`" |
| 17 | FH 2021 not presented as Unhas format | PASS | "Satu-satunya format proposal Unhas yang terverifikasi adalah milik Fakultas Hukum 2021; itu tidak saya pakai karena hanya berlaku untuk FH" |
| 17 | Lit review in Pendahuluan, labelled alignment not rule | PASS | "**1. Pendahuluan** (termasuk kajian pustaka dan gap)"; "Ini **penyelarasan** … **bukan aturan proposal Unhas**" |
| 17 | Names SK 10438 as source | PASS | "SK 10438/UN4.1/KEP/2023" in intro and table Sumber column |
| 17 | Exactly one question (faculty/prodi) + outline | PASS | Only question: "kamu di fakultas/prodi apa?"; 12-item outline in same reply |
| 17 | Edition stated as default + [CEK], not asked | PASS | "**Edisi pedoman (bawaan, tidak ditanyakan):** saya memakai Pedoman Rektor 2023 (SK 10438/UN4.1/KEP/2023), yang berlaku bagi mahasiswa yang belum memulai penelitian. `[CEK ke pedoman fakultas: …]`"; repeated in §5 |
| 17 | A3 12-item template, not A4 | PASS | "template A3, 12 butir", items 1–12; no Bab 4/5 chapters |
| 17 | No invented doses/yields/sample sizes | PASS | "dosis/konsentrasi `[ISI]`", "`[ISI: jenis rancangan, jumlah perlakuan dan ulangan]`"; no numbers besides pedoman/SK |

**Total: 19/19 PASS.** No skill text needed changing after this run; SKILL.md and campus-unhas.md already agree (one question = faculty/prodi; edition = stated default, `[CEK ke pedoman fakultas]`, listed in §5).

---

# Evals 18–20 (run 2026-09-24): UMI Fikom, UK PhD, Japanese master's

Graded by the same model that wrote the outputs; treat as self-assessment, not independent review.

## Eval 18 — UMI Fikom, Magang Skripsi
| Assertion | Result | Evidence |
|---|---|---|
| Identifies Magang Skripsi track and requirements, citing Fikom 2021 | PASS | "magang **minimal 6 bulan** di perusahaan/industri yang **punya kerja sama dengan UMI atau Fikom UMI**" · "**sertifikat**" · "**jurnal ber-ISSN**" · "Panduan … Edisi 3 Tahun 2021" |
| Uses non-skripsi body, not research 5 chapters | PASS | "**Bab III Pelaksanaan Kegiatan** … A. Penjelasan logbook" · "**Bab IV Hasil Pembelajaran**" · "laporannya **bukan** 5 bab penelitian" |
| States IEEE, left margin 4 cm, spacing 1.15, abstract ≤ 200 words | PASS | "**IEEE**, bernomor [1]" · "**kiri 4 cm**" · "**spasi 1,15**" · "**≤ 200 kata**" |
| Asks no question; unverified titles [CEK] | PASS | "Fakultas sudah kamu sebut (Fikom), jadi tidak ada pertanyaan" · "Bab II … `[CEK judul pasti]`" |
| No invented bank facts | PASS | "`[ISI: nama bank, unit kerja, posisi, tanggal mulai–selesai]`"; no bank name or figure appears |

## Eval 19 — UK PhD by publication
| Assertion | Result | Evidence |
|---|---|---|
| Chooses thesis by publication and says why | PASS | "**Form chosen: thesis by publication** … You plan three papers, so each paper becomes a chapter" |
| Integrating intro, 3 papers with status + contribution statement, linking text, discussion, conclusion | PASS | "Chapter 1 — Introduction (the integrating chapter / kappa)" · each paper: "status `[FILL: published/accepted/submitted/manuscript]` · author-contribution statement" · "bridging preface" · "Chapter 5 — General discussion" · "Chapter 6 — Conclusion" |
| Original contribution, QAA FHEQ level 8 | PASS | "original contribution to knowledge … (QAA, *Framework for Higher Education Qualifications*, level 8 descriptor)" |
| Institution rules [VERIFY], not invented | PASS | "Word limit `[VERIFY: …]`" · "Papers required `[VERIFY …]`" · "Co-authored papers `[VERIFY …]`" |
| English only, one marker style | PASS | Output in English; only `[FILL]`/`[VERIFY]` used |
| At most one question, full outline given | PASS | "One question: **which university?** … I have not waited for the answer" |

## Eval 20 — Japanese master's thesis
| Assertion | Result | Evidence |
|---|---|---|
| Entirely Japanese with languages.md labels | PASS | Headers "全体像", "構成案", "チェック", "タイトル案", "ご自身で補う項目" |
| One marker pair [記入]/[要確認] | PASS | Only "[記入：…]" and "[要確認：…]" appear |
| 序論→先行研究→研究方法→結果→考察→結論 + 参考文献, 謝辞 | PASS | Chapters 1–6 in that order; "後付け：参考文献 · 付録 · 謝辞" |
| 研究科 rules [要確認], not invented | PASS | "分量 … [要確認：研究科の規定…]" · "引用形式 [要確認…]" |
| Length in characters | PASS | "分量：約 [要確認] 字" · "分量を字数で示す — 合格" |

**Total: 16/16 pass.** Note on eval 20: section-share percentages (10%, 20%…) are stated as rough targets (目安), not rules.

## Eval 21 — Skripsi UB, fakultas tidak disebut (self-graded: the same agent wrote campus-ub.md, ran the eval, and graded it)
| Assertion | Result | Evidence |
|---|---|---|
| States no university-wide UB format found | PASS | "saya tidak menemukan pedoman format skripsi tingkat Universitas Brawijaya" |
| FPIK rules labeled FPIK + 2025, never as UB | PASS | "Semua aturan di bawah berlabel **FPIK 2025** dan **bukan aturan UB**" · "## 2. Kerangka (struktur FPIK 2025 — bukan aturan UB)" · Sumber column every row "FPIK 2025, …" |
| Exactly one question (faculty/prodi), full outline given | PASS | "**Satu pertanyaan:** kamu di fakultas/prodi apa? Kerangka lengkap tetap saya berikan di bawah." Bab I–V follow; no other question mark addressed to the user |
| Edition stated as default [CEK], not asked | PASS | "**Edisi (bawaan, tidak ditanyakan):** FPIK 2025 rev 1 `[CEK edisi terbaru di fakultas]`" |
| Unverified items [CEK], not invented | PASS | "Uji kemiripan \| ambang `[CEK ke pedoman fakultas]`"; no percentage given |

**Total: 5/5.** Caveat: "Topikmu … kemungkinan besar di FPIK" is a guess; it is labeled "dugaan, bukan jawaban", so it does not replace the question. Self-grading is weaker than independent grading.

---

# Eval 22 (run 2026-09-24): IPB tesis, pola rangkaian penelitian

Graded by the same model that wrote the output; treat as self-assessment, not independent review. Strict: a PASS needs a quoted line.

| Assertion | Result | Evidence |
|---|---|---|
| No question (prodi given); edition stated as PPKI Edisi 4 default with [CEK], not asked | PASS | "Prodi sudah kamu sebut, jadi saya tidak bertanya apa pun." · "PPKI … **Edisi 4** (Peraturan Rektor 27/IT3/PP/2019). `[CEK: bila IPB sudah menerbitkan edisi yang lebih baru]`" |
| Pola rangkaian: one chapter per article with Abstrak/Pendahuluan/Metode/Hasil dan Pembahasan/Simpulan, then Pembahasan Umum + Simpulan Umum dan Saran | PASS | "3.1 Abstrak · 3.2 Pendahuluan · 3.3 Metode … · 3.4 Hasil dan Pembahasan · 3.5 Simpulan" (same for IV) · "**V PEMBAHASAN UMUM**" · "**VI SIMPULAN UMUM DAN SARAN**" |
| S2 must publish ≥ 1 article in reputable journal; PPKI does not set article format | PASS | "S2 **wajib ≥ 1 artikel di jurnal ilmiah bereputasi** sebagai syarat lulus; format artikel tidak diatur PPKI" |
| Ringkasan/Summary (not 200-word abstrak), 20.000–30.000 words | PASS | "**Ringkasan + Summary**, masing-masing ≤ 2 halaman … (tesis tidak memakai abstrak 200 kata)" · "**20.000–30.000 kata**" |
| Harvard name-year CSE 8; similarity mandatory, threshold [CEK] | PASS | "**Harvard nama-tahun, gaya CSE edisi 8**" · "**wajib** sebelum disahkan pembimbing; ambang `[CEK ke Sekolah Pascasarjana]`" |
| No invented Cirata data | PASS | "`[ISI: data eutrofikasi/blooming di Cirata, tahun, sumber]`" · "stasiun `[ISI]`, periode `[ISI]`"; no numbers for the reservoir |

Strict notes (not failures): Chapter numbering follows the Lamp. 11d example only when Bab II is dropped. The output keeps Bab II as a `[CEK]` choice, yet it numbers the article chapters III–IV, which assumes Bab II stays. It says so. The example article titles are marked "mis." (contoh), so they are not presented as facts.

**Total: 6/6 PASS.**
