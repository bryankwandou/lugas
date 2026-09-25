# Grading — evals 23–26 (hard traps)

**Self-graded.** The same model that edited the skill, wrote the eval prompts, ran them,
and graded them. Grades are biased toward passing. Evidence is quoted so a human can
check each call. The HTML was rendered in headless Chrome (screen + print-to-PDF); the
Markdown was not reviewed by a person.

## Eval 23 — 5 messy notes → one UAJM outline

| # | Assertion | Result | Evidence (quoted from `eval-23.md`) |
|---|---|---|---|
| 1 | All 5 files inventoried; misc off-topic | PASS | "F5 \| 05-misc.txt \| catatan pribadi \| ... \| **di luar topik — tidak dipakai**" |
| 2 | Every content bullet source-labelled | PASS | "a. Pencatatan stok manual di buku tulis oleh barista shift pagi [F2 P08, P09]." Bab IV/V carry no facts, only structure. |
| 3 | 10 kg/week vs 5 kg/month flagged, not resolved | PASS | "[KONFLIK: F2 bilang ±10 kg/minggu; F3 bilang ±5 kg/bulan] — pilih satu setelah ada data" |
| 4 | No invented year/author for F4 or EOQ | PASS | "penulis, tahun, jurnal belum ada → `[CEK: identitas lengkap]`"; "EOQ [F1 P07][F3 P16] — **tanpa sumber**" |
| 5 | UAJM structure + TIDAK ADA DI BERKAS | PASS | "1.4 Luaran ...", "1.7 Kerangka Pikir (bagan)", "3.1 Bahan/materi — **[TIDAK ADA DI BERKAS]**" |
| 6 | Coverage matrix with point count | PASS | "Poin: **23 total = 18 dipakai + 5 tidak dipakai**" |
| 7 | Title withheld | PASS | "Ditunda: klaim inti (besar selisih stok) masih **konflik**." |

Strict notes: 1.4 treats "HP vs web" as a varian, which is a judgement call; the user
decides, so accepted. Result: **7/7, run 1.**

## Eval 24 — UAJM KKP with missing fields

Run 1 had a defect the original assertions did not catch: it said the photo annex must
be collected "**selama KKP — sebelum 22 Agustus**", although today is 2026-09-25 and the
KKP had already ended. That advice cannot be followed. Fix: `uajm-kkp.md` §"Tanggal KKP
vs hari ini", new check K11, a general date rule in SKILL.md Step 0, and an eighth
assertion. Run 2 is in `eval-24.md`.

| # | Assertion | Run 1 | Run 2 | Evidence (run 2) |
|---|---|---|---|---|
| 1 | Field supervisor, address, project name not invented | PASS | PASS | "`[ISI: nama pembimbing lapangan]`", "**alamat lengkap `[ISI]`**", "`[ISI: nama resmi proyek/dashboard]`" |
| 2 | Duration computed, <2 months and ~37 days, K7 not Lolos | PASS | PASS | "±**37 hari kerja** ... K7 berstatus **Gagal**" |
| 3 | Four pedoman chapters with required Bab I content | PASS | PASS | "c. **kenapa Kominfo** `[ISI]` ... e. **kenapa divisi itu**"; "1.6 Jadwal Kegiatan \| tahap + alokasi waktu **per hari**" |
| 4 | No abstrak | PASS | PASS | "Tidak ada abstrak (KKP tidak memakai abstrak)." |
| 5 | Three mandatory annexes | PASS | PASS | Rows 1–3 of §2b marked WAJIB |
| 6 | K1 passes with reason | PASS | PASS | "Lolos — pemrograman perangkat lunak (kategori b ...)" |
| 7 | Cover colour / signatory ambiguity as [CEK] | PASS | PASS | "`[CEK: pedoman 3.1.1 menulis "warna program studi", 4.1.5 menulis "hijau"]`" |
| 8 | KKP already ended; honest remedies (added after run 1) | **FAIL** | PASS | "**KKP sudah berakhir (22 Agustus 2026).** ... Jangan membuat foto atau log harian yang direkayasa." |

Result: run 1 **7/8**, run 2 **8/8**.

## Eval 25 — LPJ with a budget

| # | Assertion | Result | Evidence (quoted from `eval-25.md`) |
|---|---|---|---|
| 1 | User total 7.480.000 corrected to 7.580.000 | PASS | "Total pengeluaran yang Anda tulis **Rp7.480.000**; jumlah barisnya ... = **Rp7.580.000**" |
| 2 | Income 6.720.000, deficit 860.000, cover [ISI] | PASS | "**−Rp860.000 (defisit)** ... `[ISI: sumber penutup defisit Rp860.000]`" |
| 3 | Realisation table with sign convention; −450.000 / +120.000 | PASS | "Konvensi: **Selisih = RAB − Realisasi; positif = hemat**"; "Konsumsi ... −450.000 \| 115,0"; "Sertifikat ... +120.000 \| 76,0" |
| 4 | Transport as new pos | PASS | "**Pos baru: transport pemateri** \| 0 \| 250.000 ... **wajib: alasan + siapa yang menyetujui**" |
| 5 | Missing receipt → [ISI], LP3 not Lolos | PASS | "**[ISI: kuitansi — hilang]**"; "LP3 ... **Menunggu data**" |
| 6 | No invented variance reasons | PASS | "[ISI: alasan]" on every non-zero row |
| 7 | Tujuan table + real kendala 43/50 | PASS | "jumlah peserta \| 50 \| 43 \| sebagian" |

Arithmetic re-checked in Python: 7.580.000; 6.720.000; 3.450/3.000 = 115,0%;
380/500 = 76,0%; 7.580/7.000 = 108,3%; −280.000 − 580.000 = −860.000. Result: **7/7.**

## Eval 26 — Arabic thesis outline + HTML flowchart

| # | Assertion | Result | Evidence |
|---|---|---|---|
| 1 | Arabic throughout; language note + switch offer | PASS | "كُتب المخطط باللغة العربية لأنك كتبت بها؛ أخبرني إن أردت نسخة بالإندونيسية أو الإنجليزية." |
| 2 | [أكمل]/[تحقق] only | PASS | `grep -c "\[ISI\|\[CEK" eval-26.md` inside the Arabic block = 0 |
| 3 | Five Arab-tradition chapters + front matter + ملاحق | PASS | "الفصل الأول: الإطار العام للدراسة" ... "الفصل الخامس: الخلاصة والتوصيات والمقترحات"; "الإقرار (أصالة الرسالة)" |
| 4 | Four حدود + التعقيب | PASS | "الموضوعية ... المكانية ... الزمانية ... البشرية"; "التعقيب على الدراسات السابقة" |
| 5 | Master-level design, no invented stats | PASS | "شبه تجريبي"; "تحليل القوة الإحصائية `[أكمل: الحساب]`"; "موافقة أولياء الأمور لأن المشاركين قُصَّر" |
| 6 | HTML from template: ar, rtl, light default, light print | PASS | `eval-26-flowchart.html`: `DEFAULT_LANG = "ar"`, `<html lang="ar" dir="rtl">`, theme select default "light"; print-to-PDF page 1 rendered white with the diagram |
| 7 | Faculty guideline as [تحقق] | PASS | "`[تحقق: دليل الكلية]`" |

Known defect not covered by an assertion: in the HTML, brackets around Arabic
placeholders inside diagram nodes render mirrored (`[أكمل: ...]` shows its brackets on
the wrong sides) because Mermaid lays nodes out LTR. A `unicode-bidi: plaintext` CSS
attempt did not fix it. Text stays readable; logged in AUDIT.md as open. Result: **7/7**
with that caveat.

## Summary

| Eval | Run 1 | Final |
|---|---|---|
| 23 | 7/7 | 7/7 |
| 24 | 7/8 (defect found by strict review) | 8/8 (run 2) |
| 25 | 7/7 | 7/7 |
| 26 | 7/7 | 7/7 (+1 open rendering issue) |
