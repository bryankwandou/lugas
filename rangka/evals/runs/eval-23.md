# Eval 23 — run output (5 messy notes → one UAJM skripsi outline)

Skill files followed: SKILL.md → `summarize-to-outline.md` (R-catatan) → `uajm-skripsi.md`
(tree + checks S1–S12) → `uajm-format.md` → `checklist.md`.

---

Mode: Rangkum — **R-catatan** (5 berkas → kerangka skripsi Informatika UAJM FTI).
Kerangka ditulis dalam bahasa Indonesia; bilang kalau mau versi English.

## 1. Berkas yang dibaca

| ID | Berkas | Jenis | Panjang | Tanggal (dari isi) | Terbaca? | Peran |
|---|---|---|---|---|---|---|
| F1 | 01-catatan-bimbingan.txt | catatan bimbingan | ±70 kata | "12 agst" (tahun tidak tertulis) | ya | bahan: RM, metode, arahan dosen |
| F2 | 02-wawancara-owner.txt | transkrip wawancara | ±80 kata | "9 Agustus" | ya | bahan: Das Sein (fakta lapangan) |
| F3 | 03-draft-latarbelakang.md | draf setengah jadi | ±60 kata | `[tidak tertulis]`, "draft v1" | ya | varian 1.1 Latar Belakang |
| F4 | 04-link-jurnal.txt | daftar bacaan | 3 butir | `[tidak tertulis]` | ya | bahan Bab II (belum lengkap) |
| F5 | 05-misc.txt | catatan pribadi | 3 baris | — | ya | **di luar topik — tidak dipakai** |

Tulang punggung: **template skripsi UAJM** (tidak ada berkas yang berbentuk draf bab).

## 2. Kartu poin

| ID | Asal | Jenis | Isi |
|---|---|---|---|
| P01 | F1 | Metode/batasan | fokus ke masalah stok, tidak melebar ke kasir/POS (arahan dosen) |
| P02 | F1 | Ide/klaim | RM1: bagaimana merancang sistem pencatatan stok bahan baku |
| P03 | F1 | Ide/klaim | RM2: apakah selisih stok berkurang setelah memakai sistem |
| P04 | F1 | Metode | prototyping "ok" menurut dosen |
| P05 | F1 | Catatan kerja | cari 3 jurnal pembanding |
| P06 | F1 | Catatan kerja | tanya owner data stok bulan lalu |
| P07 | F1 | Teori | EOQ boleh dipakai asal ada sumber |
| P08 | F2 | Fakta | stok dicatat di buku tulis oleh barista shift pagi |
| P09 | F2 | Fakta | ada 3 barista |
| P10 | F2 | Fakta | selisih biji kopi ±10 kg **per minggu** (klaim pemilik, tanpa data) |
| P11 | F2 | Fakta | susu sering habis mendadak |
| P12 | F2 | Kebutuhan | sistem bisa dipakai di HP + peringatan stok hampir habis |
| P13 | F2 | Fakta | objek: Kedai Kopi Senja; wawancara 9 Agustus |
| P14 | F3 | Ide/klaim | "UMKM kopi di Makassar berkembang pesat" (tanpa data/sumber) |
| P15 | F3 | Fakta | selisih ±5 kg **per bulan** (asal angka tidak disebut) |
| P16 | F3 | Teori | EOQ untuk jumlah pesanan optimal (tanpa sumber) — duplikat P07 |
| P17 | F3 | Ide/klaim | dibutuhkan sistem informasi persediaan **berbasis web** |
| P18 | F4 | Sumber | "Sistem Informasi Persediaan Barang Berbasis Web" — penulis, tahun, jurnal tidak tertulis |
| P19 | F4 | Sumber | "Penerapan EOQ pada UMKM" — belum dibaca, identitas tidak lengkap |
| P20 | F4 | Sumber | artikel notifikasi stok minimum Android — judul tidak tertulis |
| P21–P23 | F5 | di luar topik | belanja, bayar kos, password wifi |

## 3. Peta inti (dari berkas)

| Node | Isi |
|---|---|
| Should | stok bahan baku tercatat sesuai stok fisik, ada peringatan sebelum habis [F2 P12] |
| Is | pencatatan buku tulis oleh barista shift pagi [F2 P08]; selisih biji kopi **[KONFLIK: F2 ±10 kg/minggu; F3 ±5 kg/bulan]**; susu habis mendadak [F2 P11] |
| Gap | selisih stok catatan vs gudang dan kehabisan bahan tanpa peringatan [F2] |
| Reader | panitia ujian skripsi + pembimbing I & II |
| Core claim | sistem pencatatan stok berbasis prototyping mengurangi selisih stok [F1 P02, P03] — besar selisih awal belum pasti (konflik) |
| Proof | data selisih sebelum–sesudah: **[TIDAK ADA DI BERKAS: data stok historis]** |
| Action | penerapan sistem di kedai + saran pengembangan |

## 4. Kerangka hasil (template UAJM FTI; rincian `a.`/`1.`)

**Bagian awal** — 15 komponen `uajm-skripsi.md`: Sampul (hijau muda; judul ID + EN miring) · Halaman Judul · Pengajuan · Pernyataan Tidak Plagiat (bermeterai) · Persetujuan/Pengesahan (Pembimbing I, II, Ketua Prodi) · Pedoman Penggunaan Skripsi · Peruntukan *(jika ada)* · Kata Pengantar · Abstrak 200–250 kata · Abstract · Daftar Isi/Tabel/Gambar/Lampiran · Daftar Lambang *(jika ada)*. Isi semua `[ISI]`.

**BAB I PENDAHULUAN**
- 1.1 Latar Belakang — Tugas: menunjukkan selisih stok sebagai masalah nyata.
  a. Pencatatan stok manual di buku tulis oleh barista shift pagi [F2 P08, P09].
  b. Selisih biji kopi **[KONFLIK: F2 bilang ±10 kg/minggu; F3 bilang ±5 kg/bulan]** — pilih satu setelah ada data (lihat §7).
  c. Susu habis mendadak [F2 P11].
  d. Klaim "UMKM kopi Makassar berkembang pesat" [F3 P14] — butuh sumber `[CEK: sumber]` atau dihapus.
  Bukti: wawancara pemilik 9 Agustus [F2]; data stok historis **[TIDAK ADA DI BERKAS]**.
- 1.2 Rumusan Masalah — RM1 perancangan sistem pencatatan stok [F1 P02]; RM2 pengaruh terhadap selisih stok [F1 P03].
- 1.3 Tujuan — satu per RM (merancang; mengukur selisih sebelum–sesudah) [F1].
- 1.4 Luaran — sistem pencatatan stok dengan peringatan stok minimum [F2 P12]; platform **[KONFLIK/varian: F2 "bisa di HP"; F3 "berbasis web"]** — keduanya cocok dengan web responsif, user yang memutuskan.
- 1.5 Manfaat — **[TIDAK ADA DI BERKAS]**.
- 1.6 Batasan — hanya stok bahan baku, tidak mencakup kasir/POS [F1 P01]; objek Kedai Kopi Senja [F2 P13]; bahan yang dicakup (biji kopi, susu, lainnya?) `[ISI]`.
- 1.7 Kerangka Pikir (bagan) — masalah [F2] → teori [F1 P07, F4] → prototyping [F1 P04] → luaran [F2 P12].

**BAB II TINJAUAN PUSTAKA DAN LANDASAN TEORI**
- 2.1 Tinjauan Pustaka (matriks) — calon: tiga bacaan di F4 [P18–P20]; **penulis, tahun, jurnal belum ada** → `[CEK: identitas lengkap]`; P19 belum dibaca. Jumlah minimal & pembanding: catatan kerja P05.
- 2.2 Landasan Teori — 2.2.1 Sistem informasi persediaan [F3 P17, F4 P18]; 2.2.2 EOQ [F1 P07][F3 P16] — **tanpa sumber**; dipakai hanya bila Bab III/IV memakainya (aturan pemangkas S5); 2.2.3 Prototyping [F1 P04] `[CEK: sumber model]`.

**BAB III METODE PENULISAN DAN PENELITIAN**
- 3.1 Bahan/materi — **[TIDAK ADA DI BERKAS]** (data stok, daftar bahan).
- 3.2 Alat — **[TIDAK ADA DI BERKAS]**.
- 3.3 Objek/jenis — rekayasa (forward) dengan prototyping [F1 P04]; objek Kedai Kopi Senja [F2].
- 3.4 Data/variabel yang memengaruhi hasil — selisih stok (definisi & satuan belum pasti; konflik P10/P15).
- 3.5 Rancangan & langkah — tahap prototyping [F1 P04]; rancangan pengujian **[TIDAK ADA DI BERKAS]**.
- 3.6 Pengumpulan data — wawancara pemilik [F2]; data stok historis **[TIDAK ADA DI BERKAS]** (catatan kerja P06).
- 3.7 Hipotesis — tidak dipakai (penelitian rekayasa; `uajm-usulan-ta.md`).
- 3.8 Analisis — perbandingan selisih sebelum–sesudah [F1 P03]; cara ukur **[TIDAK ADA DI BERKAS]**.

**BAB IV ANALISIS: HASIL DAN PEMBAHASAN** — 4.1 → RM1, 4.2 → RM2, 4.3 pembahasan vs penelitian sejenis [F4] — belum ada bahan (wajar sebelum penelitian).

**BAB V PENUTUP** — 5.1 Kesimpulan (satu per RM) · 5.2 Saran (menempel kesimpulan) — belum ada bahan.

**Daftar Pustaka** (gaya UAJM) · **Lampiran**: transkrip wawancara [F2] · data stok · rancangan sistem · hasil pengujian · kartu bimbingan `[ISI]` · **Naskah jurnal** (berkas terpisah).

## 5. Matriks cakupan

| Bagian | Poin | Berkas | Status |
|---|---|---|---|
| 1.1 | P08, P09, P10, P11, P14, P15 | F2, F3 | **konflik** (P10/P15) + P14 tanpa sumber |
| 1.2–1.3 | P02, P03 | F1 | cukup |
| 1.4 | P12, P17 | F2, F3 | varian (HP vs web) |
| 1.5 | — | — | TIDAK ADA DI BERKAS |
| 1.6 | P01, P13 | F1, F2 | tipis |
| 1.7 | P04, P07, P12 | F1, F2 | cukup untuk bagan |
| 2.1 | P18, P19, P20 | F4 | tanpa sumber lengkap |
| 2.2 | P07, P16, P17, P18 | F1, F3, F4 | tanpa sumber |
| 3.1, 3.2 | — | — | TIDAK ADA DI BERKAS |
| 3.3–3.5 | P04, P10, P15 | F1, F2, F3 | tipis |
| 3.6 | — (P06 catatan kerja) | F2 | TIDAK ADA DI BERKAS (data historis) |

Poin: **23 total = 18 dipakai + 5 tidak dipakai** (P05, P06 catatan kerja; P21–P23 di luar topik). P07 dan P16 duplikat → satu butir dengan dua label.

## 6. Temuan

| Bagian | Jenis | Akibat | Perbaikan |
|---|---|---|---|
| 1.1 / 3.4 | **Konflik** | besar masalah tidak pasti → RM2 tak bisa diukur | pilih: minta catatan stok 4–8 minggu terakhir |
| 1.1 | Bukti hilang | P14 klaim tanpa sumber | beri sumber atau potong |
| 2.1–2.2 | Sumber menggantung | 3 bacaan tanpa identitas; EOQ tanpa sumber | lengkapi identitas |
| 2.2.2 | Orphan section potensial | EOQ belum dipakai di RM mana pun | pakai di RM atau potong |
| 3.1–3.2, 3.5 | Kosong | Bab III belum bisa diuji di seminar | gali |
| 1.4 | Varian | platform belum diputuskan | pilih |

## 7. Rencana perbaikan

1. **Gali** data stok historis (catatan kerja P06) — sekaligus menyelesaikan konflik P10/P15.
2. **Pilih** angka selisih yang dipakai di 1.1 sesudah langkah 1.
3. **Gali** identitas lengkap tiga bacaan F4, baca P19.
4. **Pilih** posisi EOQ: masuk RM (mis. saran jumlah pesan) atau **potong** dari Bab II.
5. **Pilih** platform (web responsif vs Android).
6. **Potong** klaim P14 bila tidak ada sumber.
7. **Gali** alat, bahan, rancangan pengujian untuk Bab III.

## 8. Tidak ada di berkas / konflik / tidak dipakai / catatan kerja

- [TIDAK ADA DI BERKAS: manfaat penelitian; alat & bahan; data stok historis; rancangan pengujian; cara ukur selisih]
- [KONFLIK: F2 bilang selisih ±10 kg/minggu; F3 bilang ±5 kg/bulan]
- [KONFLIK/varian: F2 "bisa di HP"; F3 "berbasis web"]
- Tidak dipakai: P21–P23 (F5, di luar topik).
- Catatan kerja: cari 3 jurnal pembanding (F1); tanya owner data stok bulan lalu (F1).
- [CEK: apakah ada edisi pedoman setelah 2015]

## 9. Hasil cek

| Butir | Status | Perbaikan |
|---|---|---|
| R1 semua berkas di inventaris | Lolos | — |
| R2 label asal tiap fakta | Lolos | — |
| R4 berkas gagal dibaca | Lolos (tidak ada) | — |
| R7 konflik ditandai | Lolos | — |
| R8 hitungan poin | Lolos (23 = 18 + 5) | — |
| R9 duplikat digabung | Lolos (P07/P16) | — |
| R10 struktur dari template, bagian kosong ditandai | Lolos | — |
| U2 gap nyata | Menunggu data | konflik angka |
| U9 nol fakta karangan | Lolos | — |
| S3 kerangka pikir bagan | Lolos (rencana bagan 1.7) | — |
| S5 teori dipakai lagi | Gagal (EOQ) | langkah 4 |
| S6 unsur Bab III lengkap | Menunggu data | langkah 7 |

## Opsi judul

Ditunda: klaim inti (besar selisih stok) masih **konflik**. Judul disusun setelah langkah 1–2.

Langkah berikut: bawa catatan stok ke bimbingan berikutnya, lalu minta Rangka memperbarui 1.1 dan Bab III.
