# Mode Rangkum: banyak berkas → satu kerangka

Dua situasi yang berbeda, dan keduanya masuk ke sini:

| Situasi | Bahan | Hasil yang diminta |
|---|---|---|
| **R-draf** (reverse outline) | satu naskah/draf yang sudah berbentuk bab | kerangka apa adanya + diagnosis bolong |
| **R-catatan** (sintesis) | banyak berkas berantakan: catatan kuliah, hasil wawancara, potongan jurnal, chat, draf setengah jadi, tabel data | **satu** kerangka dokumen target (skripsi, laporan KKP, proposal, LPJ, ...) yang diisi dari berkas itu |

Tentukan situasinya di baris pertama keluaran. Kalau campuran (ada draf + catatan),
draf = tulang punggung, catatan = sisipan (lihat §Penggabungan).

Pemicu: "rangkum file ini jadi outline", "gabung catatan-catatan ini jadi kerangka",
"ini draf saya, benerin strukturnya", "bikin kerangka dari folder ini".

## Aturan yang tidak boleh dilanggar

1. **Baca berkasnya, bukan namanya.** Setiap berkas dibuka dan dibaca seluruhnya
   sebelum dipakai. Nama berkas (`final_FIX_bgt.docx`) tidak dianggap bukti isi atau urutan.
2. **Hanya dari isi berkas.** Tidak ada fakta, angka, nama, atau sumber dari luar.
   Bagian target yang tidak punya bahan → `[TIDAK ADA DI BERKAS: ...]` (en:
   `[NOT IN SOURCE: ...]`). Jangan mengisinya dari pengetahuan umum — dan jangan
   memakai `[ISI]` untuk menyamarkan bahwa berkasnya diam.
3. **Setiap butir isi membawa label asal** `[F2]` atau `[F2 §3]` / `[F2 baris 14]`.
   Butir tanpa label asal = butir karangan → hapus. Ini satu-satunya cara user bisa
   memeriksa rangkuman.
4. **Klaim tetap milik penulisnya.** Tulis apa yang *diklaim* berkas. Klaim meragukan
   dicatat di kolom Catatan, tidak diperbaiki diam-diam.
5. **Pertahankan nomor asli** bab/tabel/gambar dari berkas (R-draf).
6. **Berkas yang tidak terbaca disebutkan** (PDF pindaian tanpa teks, rusak, berkata
   sandi, format tak didukung, terlalu besar dan terpotong). Jangan mengarang isinya;
   minta versi teks atau tandai bagian yang terdampak.
7. **Kontradiksi tidak dilebur.** Dua berkas **atau dua bagian dalam satu berkas**
   berbeda soal fakta (angka, tanggal, nama, jumlah responden, jumlah fase/tahap/modul,
   nama instansi/perusahaan/klien, nama komponen atau agen) → `[KONFLIK: F1 bilang X;
   F4 bilang Y]` atau `[KONFLIK: F1 §1.5 bilang X; F1 §3.2 bilang Y]`, dan user yang
   memilih. Jangan memilih "yang lebih masuk akal", jangan merata-ratakan angka.
   Kontradiksi dalam satu draf biasanya sisa revisi atau salinan template/laporan lama;
   itu justru temuan paling merusak karena penguji membacanya di naskah yang sama.
   Untuk R-draf, cocokkan setiap angka hitungan (jumlah fase, tahap, hipotesis, responden)
   dan setiap nama diri antara abstrak, Bab I, bagan, Metode, dan jadwal.
8. **Duplikat dihitung satu.** Poin yang sama di tiga berkas ditulis sekali dengan
   semua label asal `[F1][F3][F5]` — pengulangan bukan bukti tambahan.

## Langkah

### 1. Inventaris (selalu tampil sebagai tabel pertama)

| ID | Berkas | Jenis | Panjang | Tanggal (dari isi, bukan nama) | Terbaca? | Peran |
|---|---|---|---|---|---|---|
| F1 | `...` | catatan/draf/data/transkrip/rujukan/chat | kata/hlm | `[tidak tertulis]` bila tak ada | ya / sebagian / tidak | tulang punggung · sisipan · varian · bahan · **di luar topik** |

- Berkas **di luar topik** tetap dicantumkan dengan peran itu, lalu tidak dipakai.
- Folder besar (>15 berkas): kelompokkan per jenis dulu, baca urut prioritas
  (draf utama → pendahuluan/abstrak → daftar isi → penutup → metode → data → sisanya).
- Kalau ada dua versi berkas yang sama, tentukan yang terbaru dari **tanggal atau
  penanda versi di dalam isi**; kalau tidak ada penanda, keduanya varian dan user memilih.

### 2. Kartu poin (inti mode R-catatan)

Pecah semua berkas menjadi poin atomik — satu gagasan, fakta, angka, atau kutipan per
baris:

```
P07 [F3 baris 12-15] Fakta   : antrean rata-rata 2 jam (klaim narasumber, tanpa data)
P08 [F5 §2]          Fakta   : antrean 45 menit (log sistem Maret)      → KONFLIK dgn P07
P09 [F1][F4]         Teori   : model FIFO (tanpa sumber pustaka)       → butuh sumber
P10 [F2]             Tugas   : "cari 3 jurnal pembanding"               → bukan isi, catatan kerja
```

Jenis poin: **Fakta · Data · Teori/Sumber · Metode · Ide/Klaim · Pertanyaan terbuka ·
Catatan kerja (to-do)**. Catatan kerja dan pertanyaan terbuka tidak masuk kerangka;
kumpulkan di blok akhir.

Untuk R-draf, kartu poin diganti **peta paragraf**, satu baris per bagian:
```
§2.3 (hlm. 14-17) | Tugas: mendefinisikan X | Klaim: X terdiri atas 3 komponen
                  | Bukti: Sari 2021, Tabel 2.1 | Dipakai lagi di: §4.2
```
Tugas yang tidak bisa ditulis dengan satu kata kerja = temuan (bagian tanpa pekerjaan).

### 3. Pilih kerangka target

- User menyebut dokumennya (skripsi UAJM, laporan KKP, LPJ, ...) → ambil template dari
  berkas genre/kampus yang sesuai (routing SKILL.md). **Struktur dari template, isi dari
  kartu poin.** Jangan menurunkan struktur dari urutan catatan.
- User tidak menyebut → tebak dari isi, nyatakan tebakan itu sebagai bawaan
  ("Kerangka: skripsi 5 bab, dari isi F1–F3") dan lanjutkan. Tidak bertanya lebih dari satu
  hal (hard rule 6).

### 4. Petakan poin → bagian (matriks cakupan)

| Bagian target | Poin | Berkas | Status |
|---|---|---|---|
| 1.1 Latar Belakang | P01, P07, P08 | F1, F3, F5 | **konflik** (P07/P08) |
| 2.2 Landasan Teori | P09 | F1, F4 | ada, **tanpa sumber** |
| 3.3 Populasi & Sampel | — | — | **TIDAK ADA DI BERKAS** |

Status yang boleh: `cukup` · `tipis` (1 poin) · `tanpa sumber` · `konflik` · `TIDAK ADA DI
BERKAS`. Setiap poin berjenis Fakta/Data/Teori/Metode/Ide harus masuk tepat satu baris,
atau masuk daftar **Tidak dipakai** dengan alasan (di luar topik, duplikat, catatan kerja).
Hitung: jumlah poin = dipakai + tidak dipakai. Kalau selisih, ada poin yang hilang —
cari sebelum lanjut.

### 5. Rekonstruksi peta inti
Isi Peta Inti (Should / Is / Gap / Reader / Core claim / Proof / Action) **dari poin
yang ada**, masing-masing berlabel asal. Kalau berkas memuat dua atau tiga klaim inti
yang bersaing, tampilkan semuanya dan jangan memilihkan — itu temuan paling penting.

### 6. Kerangka hasil
Kerangka bernomor mengikuti template target (R-catatan) atau struktur asli (R-draf).
Tiap bagian: **Tugas · Isi** (2–5 butir, tiap butir berlabel asal) **· Bukti · Panjang**.

### 7. Diagnosis

| Jenis temuan | Artinya |
|---|---|
| **Orphan claim** | dijanjikan di awal, tidak pernah dijawab |
| **Orphan section** | ada isinya, tidak menjawab apa pun |
| **Bukti hilang** | klaim tanpa data/sumber |
| **Konflik** | dua berkas **atau dua bagian dalam satu berkas** berbeda soal fakta yang sama (mis. 3 fase di Bab I vs 4 fase di Metode; nama instansi di pengesahan ≠ di Bab II) |
| **Duplikasi** | isi sama di dua tempat |
| **Urutan salah** | pembaca butuh B sebelum A |
| **Timpang** | bagian inti lebih tipis dari pengantar |
| **Putus** | rumusan masalah ≠ kesimpulan |
| **Sumber menggantung** | dirujuk di teks, tidak ada di pustaka (atau sebaliknya) |
| **Kosong** | bagian wajib template tanpa satu poin pun |

Untuk naskah akademik Indonesia, tambah tabel `rumusan → tujuan → bab → bukti →
kesimpulan → saran`. Sel kosong = temuan.

### 8. Rencana perbaikan (maksimal 7 langkah, urut dampak)
Tiap langkah memakai satu kata kerja: **potong** (buang) · **pindah** (sudah ada, salah
tempat) · **pilih** (selesaikan konflik/varian) · **gali** (butuh data baru dari user).

## Penggabungan banyak berkas

1. Tentukan **satu** tulang punggung (paling lengkap/terbaru menurut isi) dan
   nyatakan alasannya. Untuk R-catatan tanpa draf, tulang punggungnya adalah
   **template target**, bukan berkas mana pun.
2. Berkas lain: **sisipan** (mengisi bagian kosong), **varian** (versi lain dari bagian
   yang sama), **bahan** (data/lampiran), atau **di luar topik**.
3. Varian ditampilkan berdampingan satu baris dan **user memilih**.
4. Konflik fakta → `[KONFLIK: ...]` di kerangka **dan** di blok akhir.

## Format keluaran

```
Mode: Rangkum — R-catatan (5 berkas → kerangka <dokumen target>)

## 1. Berkas yang dibaca
| ID | Berkas | Jenis | Panjang | Tanggal | Terbaca? | Peran |

## 2. Peta inti (dari berkas, berlabel asal)

## 3. Kerangka hasil
(template target; tiap butir berlabel [Fn])

## 4. Matriks cakupan
| Bagian | Poin | Berkas | Status |
Poin: N total = X dipakai + Y tidak dipakai

## 5. Temuan
| Bagian | Jenis temuan | Akibat | Perbaikan |

## 6. Rencana perbaikan (≤7, potong/pindah/pilih/gali)

## 7. Tidak ada di berkas / konflik / tidak dipakai / catatan kerja
- [TIDAK ADA DI BERKAS: ...]
- [KONFLIK: ...]
- Tidak dipakai: P.. (alasan)
- Catatan kerja user yang ditemukan: ...

## 8. Hasil cek
| Butir | Status | Perbaikan |   (R1–R10, plus U4 dan cek genre target)
```

Judul (Step 4 SKILL.md): beri opsi judul hanya bila user memintanya **dan** tidak ada
temuan Orphan claim/Putus/Konflik pada klaim inti; selain itu satu kalimat bahwa judul
menunggu temuan itu diselesaikan.

## Turunan setelah kerangka jadi

- **Naskah jurnal** — ambil §Hasil, mampatkan pendahuluan (UAJM: `uajm-format.md`).
- **Slide seminar** — satu slide per bagian tingkat 1, judul = Tugas.
- **Abstrak** — masalah → tujuan → metode → hasil, dari peta inti.
- **Mind map / bagan** — blok Mermaid; kalau diminta HTML, pakai
  `assets/flowchart-template.html` (lihat SKILL.md §Keluaran diagram).

## Cek rangkuman

| Kode | Cek |
|---|---|
| R1 | Setiap berkas ada di inventaris, termasuk yang tak terbaca dan yang di luar topik? |
| R2 | Tidak ada fakta di kerangka tanpa label asal `[Fn]`? |
| R3 | Nomor bab/tabel/gambar asli dipertahankan (R-draf)? |
| R4 | Berkas yang gagal dibaca disebutkan beserta bagian yang terdampak? |
| R5 | Tiap temuan menunjuk bagian tertentu? |
| R6 | Rencana perbaikan memakai potong/pindah/pilih/gali? |
| R7 | Konflik antarberkas **dan antarbagian dalam satu berkas** (hitungan fase/tahap, nama instansi/komponen) ditandai `[KONFLIK]`, tidak dilebur atau dirata-rata? |
| R8 | Hitungan poin: total = dipakai + tidak dipakai? |
| R9 | Duplikat digabung jadi satu butir dengan semua label asal? |
| R10 | Struktur mengikuti template dokumen target, bukan urutan catatan; bagian wajib yang kosong tertulis `TIDAK ADA DI BERKAS`? |
