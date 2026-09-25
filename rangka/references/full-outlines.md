# Kerangka penuh: bagian awal → Bab I–V (atau lebih) → bagian akhir → lampiran

Dipakai saat user meminta "kerangka lengkap", "outline dari sampul sampai lampiran",
atau mode **Lengkap** untuk skripsi, tesis, atau disertasi. Berkas ini memberi **pohon
kerangka yang ditulis sebagai kerangka** — bukan tabel ringkas — supaya user bisa
langsung menyalinnya ke daftar isi, lalu mengisi `[ISI]`.

Urutan pakai:
1. Kampus punya berkas sendiri? UAJM → `uajm-skripsi.md` (menang atas pohon di bawah).
   Kampus lain dengan `campus-*.md` → nama bab dan urutan bagian awal dari berkas itu.
2. Sisanya: pakai pohon di bawah sebagai **bawaan**, isi 14 variabel
   `pedoman-adapter.md`, lalu ganti nama/urutan yang berbeda.
3. Setiap baris pohon yang akan ditulis di naskah memakai penomoran yang diizinkan
   pedoman (UAJM: `1.1`, `1.1.1`, `1.1.1.1`, rincian `a.`/`1.`, tanpa bullet).

Aturan keluaran:
- Tulis **setiap** bagian awal dan **setiap** lampiran sebagai baris kerangka, walau
  isinya `[ISI]`. Bagian yang opsional diberi label *(jika ada)*.
- Tiap sub-bab Bab I–V diberi satu baris **Tugas** (kata kerja) dan tanda bukti/`[ISI]`.
  Pohon di bawah menulis Tugas singkat di belakang `—`.
- Setelah pohon, wajib tabel penutup `rumusan → tujuan → bab/sub penjawab → bukti →
  kesimpulan → saran`, dan daftar lampiran dengan kolom "dirujuk dari" (lihat
  `appendices.md`).

---

## A. Skripsi (S1) — 5 bab, bawaan Indonesia

```
BAGIAN AWAL
  Sampul depan
  Halaman judul
  Halaman persetujuan pembimbing            — pembimbing I & II [ISI: nama]
  Halaman pengesahan penguji                 — setelah sidang
  Lembar pernyataan orisinalitas/tidak plagiat (bermeterai) [CEK: nominal meterai]
  Halaman persembahan / motto               (jika ada)
  Kata pengantar
  Abstrak (bahasa Indonesia)                 — [CEK: batas kata, mis. 150–250]
  Abstract (bahasa Inggris)
  Daftar isi
  Daftar tabel
  Daftar gambar
  Daftar lampiran
  Daftar singkatan dan lambang               (jika ada)
  Pedoman transliterasi Arab-Latin           (PTKIN saja)

BAB I PENDAHULUAN
  1.1 Latar Belakang          — menunjukkan Das Sollen, Das Sein, dan selisihnya dengan fakta lapangan [ISI]
  1.2 Rumusan Masalah         — merumuskan RM1..RMn sebagai kalimat tanya
  1.3 Tujuan Penelitian       — satu tujuan per RM, kata kerja terukur
  1.4 Manfaat Penelitian      — teoretis dan praktis
  1.5 Batasan Masalah         — membatasi data, lokasi, periode, platform, pengguna
  1.6 Sistematika Penulisan   — (jika pedoman memintanya; UAJM tidak)

BAB II TINJAUAN PUSTAKA
  2.1 Penelitian Terdahulu    — matriks penulis · tahun · metode · hasil · celah · beda dengan penelitian ini
  2.2 Landasan Teori
      2.2.1 [ISI: teori/konsep 1] — dipakai lagi di Bab III/IV
      2.2.2 [ISI: teori/konsep 2]
  2.3 Kerangka Pikir          — bagan masalah → teori → metode → luaran
  2.4 Hipotesis               (eksperimental/korelasional/kausal, atau rekayasa yang membandingkan dengan baseline memakai uji statistik)

BAB III METODE PENELITIAN
  3.1 Jenis dan Pendekatan Penelitian
  3.2 Lokasi dan Waktu Penelitian
  3.3 Populasi dan Sampel / Subjek / Sumber Data
  3.4 Variabel dan Definisi Operasional   (kuantitatif)
  3.5 Instrumen Penelitian (+ uji validitas & reliabilitas)
  3.6 Teknik Pengumpulan Data
  3.7 Tahapan Penelitian / Model Pengembangan  (rekayasa: analisis → desain → implementasi → pengujian)
  3.8 Rancangan Pengujian / Teknik Analisis Data

BAB IV HASIL DAN PEMBAHASAN
  4.1 Gambaran Umum Objek Penelitian
  4.2 Hasil untuk RM1         — tabel/grafik yang dirujuk di teks
  4.3 Hasil untuk RM2
  4.n Pembahasan              — tafsir + perbandingan dengan 2.1

BAB V PENUTUP
  5.1 Kesimpulan              — satu butir per RM, tidak ada yang baru
  5.2 Saran                   — menempel pada butir kesimpulan

BAGIAN AKHIR
  Daftar Pustaka              — gaya [CEK: APA/IEEE/penulis-tahun kampus]
  Lampiran 1 Surat izin penelitian & surat balasan instansi
  Lampiran 2 Instrumen (kuesioner / pedoman wawancara / lembar observasi)
  Lampiran 3 Hasil uji validitas & reliabilitas         (jika kuantitatif)
  Lampiran 4 Data mentah dan hasil olahan
  Lampiran 5 Dokumentasi (foto kegiatan, tangkapan layar)
  Lampiran 6 Kode sumber / rancangan sistem              (rekayasa)
  Lampiran 7 Hasil pengujian (black box / UAT)           (rekayasa)
  Lampiran 8 Kartu bimbingan
  Lampiran 9 Berita acara dan daftar hadir seminar
  Lampiran 10 Hasil cek kemiripan                        [CEK: wajib atau tidak]
  Lampiran 11 Daftar riwayat hidup
```

Varian yang sering: **4 bab** (Hasil+Pembahasan+Penutup digabung — jarang); **6 bab**
(Bab IV Hasil, Bab V Pembahasan, Bab VI Penutup); rumpun hukum memakai `A.`/`1.`/`a.`
dan bahan hukum sebagai ganti populasi-sampel.

## B. Tesis (S2) — 5 atau 6 bab

Bedanya dengan skripsi dijelaskan di `genre-thesis.md`; pohon ini memuat semuanya.

```
BAGIAN AWAL
  Sampul · Halaman judul · Halaman pengajuan tesis
  Lembar persetujuan komisi pembimbing / promotor
  Lembar pengesahan tim penguji
  Pernyataan keaslian tesis + pelimpahan hak cipta (bermeterai)
  Prakata
  Abstrak / Ringkasan (Indonesia)            — [CEK: abstrak ±250 kata atau ringkasan 1–2 hlm]
  Abstract / Summary (Inggris)
  Daftar isi · daftar tabel · daftar gambar · daftar lampiran
  Daftar singkatan dan istilah               (jika ada)

BAB I PENDAHULUAN
  1.1 Latar Belakang          — memposisikan masalah dalam perdebatan bidang, bukan hanya kasus
  1.2 Rumusan Masalah
  1.3 Tujuan Penelitian
  1.4 Manfaat (teoretis, praktis, kebijakan)
  1.5 Kebaruan / Posisi Penelitian (state of the art) — satu dari 4 bentuk kebaruan (genre-thesis.md)
  1.6 Ruang Lingkup

BAB II TINJAUAN PUSTAKA
  2.1 Protokol Tinjauan       — basis data, kata kunci, rentang tahun, inklusi/eksklusi, jumlah lolos [ISI]
  2.2 Kajian Teori
  2.3 Sintesis Penelitian Terdahulu dan Research Gap
  2.4 Kerangka Teoretis
  2.5 Kerangka Konseptual
  2.6 Hipotesis               (jika ada)

BAB III METODE PENELITIAN
  3.1 Desain Penelitian
  3.2 Lokasi, Waktu, Populasi, Sampel (+ perhitungan besar sampel)
  3.3 Definisi Operasional Variabel (tabel: variabel, definisi, indikator, skala, alat ukur)
  3.4 Instrumen dan Uji Validitas-Reliabilitas
  3.5 Prosedur Pengumpulan Data
  3.6 Analisis Data (+ uji asumsi)
  3.7 Etika Penelitian (ethical clearance, informed consent, kerahasiaan)

BAB IV HASIL PENELITIAN
  4.1 Deskripsi Data/Sampel
  4.2 Hasil per Rumusan Masalah
  4.3 Uji Hipotesis           (jika ada)

BAB V PEMBAHASAN              (digabung ke Bab IV bila pedoman 5 bab)
  5.1 Interpretasi Temuan
  5.2 Perbandingan dengan Penelitian Terdahulu (kembali ke 2.3)
  5.3 Implikasi Teoretis
  5.4 Implikasi Praktis/Kebijakan
  5.5 Keterbatasan Penelitian

BAB VI SIMPULAN DAN SARAN
  6.1 Simpulan
  6.2 Saran (akademis dan praktis)

BAGIAN AKHIR
  Daftar Pustaka
  Lampiran 1 Ethical clearance / izin penelitian
  Lampiran 2 Instrumen dan lembar persetujuan responden
  Lampiran 3 Protokol dan hasil pencarian literatur (PRISMA bila systematic review)
  Lampiran 4 Output analisis statistik / transkrip + koding
  Lampiran 5 Bukti submit/terbit artikel               [CEK: syarat publikasi S2]
  Lampiran 6 Hasil cek kemiripan
  Lampiran 7 Riwayat hidup
```

## C. Disertasi (S3) — pola monograf, 7 bab

```
BAGIAN AWAL
  Sampul · Halaman judul · Halaman pengajuan disertasi
  Persetujuan promotor & ko-promotor
  Pengesahan tim penguji (ujian tertutup / terbuka)
  Pernyataan orisinalitas (bermeterai)
  Prakata
  Ringkasan (Indonesia)                      — lebih panjang dari abstrak [CEK: halaman]
  Summary (Inggris)
  Daftar isi · tabel · gambar · lampiran · singkatan
  Daftar publikasi yang dihasilkan dari disertasi

BAB I PENDAHULUAN
  1.1 Latar Belakang dan Masalah Bidang
  1.2 Rumusan Masalah / Pertanyaan Penelitian
  1.3 Tujuan
  1.4 Kebaruan (novelty) dan Kontribusi Orisinal — protokol pencarian ditunjukkan [ISI]
  1.5 Manfaat
  1.6 Peta Jalan Penelitian (roadmap: studi 1 → studi 2 → model)
  1.7 Sistematika Disertasi

BAB II KAJIAN PUSTAKA DAN LANDASAN TEORI
  2.1 Peta Bidang dan Perdebatan Teoretis
  2.2 Tinjauan Sistematis Penelitian Terdahulu
  2.3 Celah Penelitian

BAB III KERANGKA TEORETIK / MODEL YANG DIAJUKAN
  3.1 Konstruk dan Proposisi
  3.2 Model Konseptual
  3.3 Hipotesis / Proposisi yang Diuji

BAB IV METODE PENELITIAN
  4.1 Paradigma dan Desain (multi-studi / mixed methods)
  4.2 Data, Sampel, Instrumen per Studi
  4.3 Analisis
  4.4 Keabsahan / Validitas
  4.5 Etika

BAB V HASIL PENELITIAN
  5.1 Hasil Studi 1
  5.2 Hasil Studi 2
  5.3 Pengujian Model

BAB VI PEMBAHASAN
  6.1 Temuan terhadap Teori
  6.2 Kebaruan yang Terbukti (dipetakan ke 1.4)
  6.3 Implikasi Teoretis, Metodologis, Praktis
  6.4 Keterbatasan

BAB VII SIMPULAN, KEBARUAN, DAN SARAN
  7.1 Simpulan
  7.2 Kebaruan Penelitian
  7.3 Saran dan Agenda Penelitian Lanjut

BAGIAN AKHIR
  Daftar Pustaka
  Lampiran 1 Ethical clearance per studi
  Lampiran 2 Instrumen per studi
  Lampiran 3 Protokol tinjauan sistematis
  Lampiran 4 Output analisis
  Lampiran 5 Artikel terbit/diterima + pernyataan kontribusi penulis
  Lampiran 6 Hasil cek kemiripan
  Lampiran 7 Riwayat hidup akademik
```

## D. Disertasi berbasis artikel (sandwich)

```
BAGIAN AWAL      (sama dengan C, + daftar artikel beserta status terbit dan kontribusi penulis)
BAB I   Pendahuluan Umum        — masalah bidang, pertanyaan besar, bagaimana artikel menjawabnya bersama
BAB II  Kerangka Teoretik Menyeluruh
BAB III Artikel 1 (Abstrak · Pendahuluan · Metode · Hasil · Pembahasan · Simpulan · Pustaka)
BAB IV  Artikel 2 (idem)          — diawali 1 hlm jembatan: kenapa studi ini menyusul studi 1
BAB V   Artikel 3 (idem)
BAB VI  Pembahasan Umum         — argumen yang tidak bisa dibuat satu artikel sendirian
BAB VII Simpulan Umum dan Saran
BAGIAN AKHIR     Daftar Pustaka umum · Lampiran izin penerbit (hak cipta) · etik · instrumen
```

## Cek kerangka penuh

| Kode | Cek |
|---|---|
| F1 | Semua bagian awal tertulis sebagai baris (opsional diberi *jika ada*)? |
| F2 | Semua bab sampai penutup punya sub-bab bertugas, tidak ada bab kosong? |
| F3 | Setiap lampiran dirujuk dari satu sub-bab? |
| F4 | Tabel penutup RM → tujuan → bab → bukti → kesimpulan → saran terisi? |
| F5 | Nama bab dan jumlah bab mengikuti pedoman kampus, atau ditandai `[CEK]`? |
| F6 | Jenjang tepat: tesis punya kebaruan & protokol tinjauan; disertasi punya kebaruan terbukti di bab akhir? |
