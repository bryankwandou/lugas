# Merangkum berkas penelitian menjadi satu kerangka (reverse outline)

Mode ini kebalikan dari alur biasa. Biasanya Rangka menyusun kerangka **sebelum**
naskah ada. Di sini naskah sudah ada — satu berkas atau satu folder — dan yang diminta
adalah kerangkanya: apa sebenarnya yang tertulis di situ, dan di mana bolongnya.

Teknik ini dikenal sebagai *reverse outlining*: baca yang sudah ditulis, catat
kerja tiap bagian, lalu nilai kerangkanya — bukan kalimatnya.

Gunakan saat user berkata: "rangkum file ini jadi outline", "ringkas skripsiku",
"ini draf saya, benerin strukturnya", "bikin kerangka dari folder ini", "gabung
beberapa file jadi satu kerangka".

## Aturan yang tidak boleh dilanggar

1. **Hanya dari isi berkas.** Tidak ada penambahan fakta, angka, atau sumber dari luar.
   Kalau bagian yang seharusnya ada ternyata tidak ada di berkas, tulis
   `[TIDAK ADA DI BERKAS: ...]` — jangan diisi dari pengetahuan umum.
2. **Klaim tetap milik penulisnya.** Rangkuman menuliskan apa yang *diklaim* naskah,
   bukan apa yang benar. Kalau klaimnya meragukan, catat di kolom Catatan, jangan
   diam-diam diperbaiki.
3. **Pertahankan nomor asli.** Nomor bab/sub-bab/tabel/gambar dari berkas dibawa apa
   adanya, supaya user bisa balik ke sumbernya.
4. **Berkas yang tidak terbaca disebutkan.** Kalau PDF hasil pindaian tanpa lapisan
   teks, atau berkas rusak, katakan — jangan mengarang isinya.

## Langkah

### 1. Inventaris
Daftar semua berkas: nama, jenis, perkiraan panjang, dan dugaan peran (draf bab,
data, instrumen, jurnal acuan, catatan). Untuk folder besar, kelompokkan dulu; jangan
membaca acak.

Prioritas baca: naskah utama → abstrak/pendahuluan → daftar isi → penutup → metode →
sisanya. Daftar isi dan penutup memberi kerangka paling cepat.

### 2. Peta paragraf (inti teknik ini)
Untuk tiap bagian naskah, catat satu baris:

```
§2.3 (hal. 14-17) | Tugas: membangun definisi X | Klaim: X terdiri atas 3 komponen
                  | Bukti: kutipan Sari 2021, Tabel 2.1 | Dipakai lagi di: §4.2
```

Kolom **Tugas** ditulis dengan kata kerja ("membuktikan", "membandingkan",
"mendefinisikan"). Kalau tugas sebuah bagian tidak bisa dirumuskan dalam satu kata
kerja, itu sendiri sudah temuan: bagian itu belum punya pekerjaan yang jelas.

Kolom **Dipakai lagi di** adalah detektor orphan.

### 3. Rekonstruksi peta inti
Dari peta paragraf, isi tabel Peta Inti (Should / Is / Gap / Reader / Core claim /
Proof / Action) — **sebagaimana tersirat di naskah**, bukan sebagaimana seharusnya.
Kalau core claim tidak bisa ditarik jadi satu kalimat, katakan: naskah ini belum
punya klaim tunggal, dan tunjukkan dua atau tiga klaim yang bersaing di dalamnya.

### 4. Kerangka hasil rangkuman
Keluarkan kerangka bernomor mengikuti struktur asli, tiap bagian: Tugas · Isi (2–5
butir, ringkas) · Bukti · Panjang asli (halaman/kata).

### 5. Diagnosis
Tabel temuan, diurut dari yang paling merusak:

| Jenis temuan | Artinya |
|---|---|
| **Orphan claim** | dijanjikan di awal, tidak pernah dijawab |
| **Orphan section** | ada isinya, tidak menjawab apa pun |
| **Bukti hilang** | klaim tanpa data/sumber |
| **Duplikasi** | isi sama muncul di dua tempat |
| **Urutan salah** | pembaca butuh B sebelum A, tapi A duluan |
| **Timpang** | bagian inti lebih pendek daripada bagian pengantar |
| **Putus** | rumusan masalah ≠ kesimpulan |
| **Sumber menggantung** | dirujuk di teks, tidak ada di daftar pustaka (atau sebaliknya) |

Untuk naskah akademik Indonesia, jalankan juga tabel pemetaan:
`rumusan masalah → tujuan → bab penjawab → bukti → kesimpulan → saran`.
Sel kosong = temuan.

### 6. Rencana perbaikan
Maksimal 7 langkah, diurut berdasar dampak, tiap langkah menyebut bagian mana yang
dipindah/dipotong/ditambah. Bedakan tegas: **potong** (buang), **pindah** (sudah ada,
salah tempat), **gali** (butuh data baru dari user).

## Format keluaran

```
## 1. Berkas yang dibaca
| Berkas | Jenis | Panjang | Peran |

## 2. Peta inti (sebagaimana tersirat di naskah)

## 3. Kerangka hasil rangkuman
(bernomor sesuai naskah asli)

## 4. Temuan
| Bagian | Jenis temuan | Akibat | Perbaikan |

## 5. Rencana perbaikan (maksimal 7 langkah)

## 6. Yang tidak ada di berkas
- [TIDAK ADA DI BERKAS: ...]

## 7. Hasil cek
| Butir | Status | Perbaikan |   (R1–R7, plus U4 untuk naskahnya)
```

Langkah 4 SKILL.md (judul) di mode ini: beri opsi judul hanya kalau user memintanya
**dan** naskah tidak punya temuan Orphan claim/Putus; kalau ada, tulis satu kalimat
bahwa judul menunggu temuan itu diperbaiki.

## Menggabungkan banyak berkas jadi satu kerangka

Kalau berkasnya beberapa (bab terpisah, versi berbeda, catatan tercecer):
1. Tentukan **satu** berkas sebagai tulang punggung — biasanya yang paling lengkap atau
   paling baru. Nyatakan pilihan itu terang-terangan.
2. Berkas lain dipetakan sebagai: **sisipan** (mengisi bagian kosong), **varian**
   (versi lain dari bagian yang sama), atau **bahan** (data/lampiran).
3. Untuk tiap varian, tampilkan bedanya dalam satu baris dan **biarkan user yang
   memilih** — jangan menggabung dua versi diam-diam.
4. Kalau ada dua berkas yang saling bertentangan soal fakta, tandai
   `[KONFLIK: berkas A bilang ..., berkas B bilang ...]`.

## Meringkas jadi bentuk lain

Setelah kerangka rangkuman jadi, turunannya murah:
- **Naskah jurnal** — ambil §Hasil terbesar, mampatkan pendahuluan (rasio di
  `uajm-format.md`);
- **Slide seminar** — satu slide per bagian tingkat 1, judul = kolom Tugas;
- **Abstrak** — masalah → tujuan → metode → hasil, dari peta inti;
- **Mind map** — keluarkan blok Mermaid `mindmap` bercabang sesuai kerangka.

## Cek rangkuman

| Kode | Cek |
|---|---|
| R1 | Setiap bagian naskah punya satu baris di peta paragraf? |
| R2 | Tidak ada fakta di kerangka yang tidak ada di berkas? |
| R3 | Nomor bab/tabel/gambar asli dipertahankan? |
| R4 | Berkas yang gagal dibaca disebutkan? |
| R5 | Tiap temuan menunjuk bagian tertentu, bukan keluhan umum? |
| R6 | Rencana perbaikan membedakan potong / pindah / gali? |
| R7 | Konflik antarberkas ditandai, bukan dilebur? |
