# Eval 13 — Rangkum draf jadi outline (jebakan: orphan claim)

Prompt: draf skripsi QRIS UMKM kuliner Makassar yang ditempel (lihat evals.json id 13).

Klasifikasi: id · Mode Rangkum (`summarize-to-outline.md`) · Genre A · pembaca: dosen pembimbing · Steps 3–4 tetap berlaku.

## 1. Berkas yang dibaca

| Berkas | Jenis | Panjang | Peran |
|---|---|---|---|
| Teks tempelan di chat | draf skripsi Bab I–V | ±150 kata, ringkasan per sub-bab | naskah utama (satu-satunya berkas) |

### Peta paragraf

| Bagian | Tugas | Klaim | Bukti | Dipakai lagi di |
|---|---|---|---|---|
| §1.1 | menyatakan konteks | UMKM kuliner Makassar mulai memakai QRIS; "semua UMKM di Makassar sudah memakai QRIS sejak 2023" | tidak ada | — |
| §1.2 | merumuskan masalah | RM1 tingkat penggunaan; RM2 faktor minat; RM3 dampak ke omzet | — | RM1→§4.1, RM2→§4.2, RM3→**tidak ada** |
| §2.1 | mendefinisikan pembayaran digital | definisi menurut Bank Indonesia | "menurut Bank Indonesia" (tanpa rincian sumber) | tidak tampak dipakai |
| §2.2 | (tidak bisa dirumuskan dengan satu kata kerja yang melayani RM) | sejarah uang kertas di Indonesia | — | **tidak ada** |
| §3.1 | menjelaskan pengumpulan data | kuesioner ke 100 pelaku UMKM di Kec. Panakkukang | — | §4.1, §4.2 |
| §4.1 | mengukur penggunaan | 62% responden memakai QRIS setiap hari (Tabel 4.1) | Tabel 4.1 | §5.1 |
| §4.2 | mengidentifikasi faktor | kemudahan dan promo cashback | — (cara analisis tidak disebut) | §5.1 (hanya kemudahan) |
| §5.1 | menyimpulkan | penggunaan tinggi, dipengaruhi kemudahan | §4.1, §4.2 | §5.2 |
| §5.2 | menyarankan | pemerintah memperluas sosialisasi QRIS | — | — |

## 2. Peta inti (sebagaimana tersirat di naskah)

| Node | Isi |
|---|---|
| Should | UMKM kuliner memakai QRIS dan mendapat manfaat (tersirat) |
| Is | §1.1 menyebut "mulai memakai" sekaligus "semua sudah memakai" — dua keadaan yang bertentangan |
| Gap | tidak dirumuskan eksplisit |
| Reader | dosen pembimbing/penguji |
| Core claim | "Penggunaan QRIS di UMKM kuliner Panakkukang tinggi dan dipengaruhi kemudahan" |
| Proof | kuesioner 100 responden, Tabel 4.1 |
| Action | sosialisasi QRIS oleh pemerintah |

## 3. Kerangka hasil rangkuman (nomor asli)

- **BAB I PENDAHULUAN**
  - 1.1 Latar Belakang — Tugas: konteks. Isi: adopsi QRIS UMKM kuliner Makassar. Bukti: tidak ada. Panjang asli: 2 kalimat.
  - 1.2 Rumusan Masalah — RM1, RM2, RM3.
- **BAB II TINJAUAN PUSTAKA**
  - 2.1 Pembayaran digital — definisi versi Bank Indonesia.
  - 2.2 Sejarah uang kertas di Indonesia.
- **BAB III METODE**
  - 3.1 Kuesioner, 100 pelaku UMKM, Kec. Panakkukang.
- **BAB IV HASIL**
  - 4.1 Tingkat penggunaan — Tabel 4.1: 62% memakai setiap hari.
  - 4.2 Faktor minat — kemudahan, promo cashback.
- **BAB V PENUTUP**
  - 5.1 Kesimpulan — penggunaan tinggi, dipengaruhi kemudahan.
  - 5.2 Saran — pemerintah memperluas sosialisasi.

## 4. Temuan (dari yang paling merusak)

| Bagian | Jenis temuan | Akibat | Perbaikan |
|---|---|---|---|
| §1.2 RM3 (dampak ke omzet) | **Orphan claim** | dijanjikan di rumusan, tidak dijawab di Bab IV maupun V; penguji akan menanyakannya pertama kali | jawab (butuh data omzet) atau hapus RM3 |
| §1.2 ↔ §5.1 | **Putus** | kesimpulan menjawab RM1 dan RM2 saja | sejajarkan setelah RM3 diputuskan |
| §2.2 Sejarah uang kertas | **Orphan section** | tidak menjawab RM mana pun, tidak dipakai lagi | potong |
| §1.1 "semua UMKM di Makassar sudah memakai QRIS sejak 2023" | **Bukti hilang** + klaim meragukan | klaim naskah sendiri; tanpa sumber, dan bertentangan dengan "mulai memakai" di kalimat sebelumnya serta dengan 62% di Tabel 4.1 | dicatat, tidak saya ubah; penulis perlu sumber atau merevisi klaimnya |
| §3.1 | **Bukti hilang** (metode) | teknik sampling dan teknik analisis untuk RM2 tidak disebut | tambah |
| §4.2 → §5.1 | **Putus** kecil | "promo cashback" hilang di kesimpulan tanpa penjelasan | tentukan: masuk kesimpulan atau jelaskan kenapa tidak |
| §5.2 | Saran tidak menempel | "sosialisasi" tidak diturunkan dari temuan mana pun | tempelkan ke temuan §4.1/§4.2 |
| §2.1 "menurut Bank Indonesia" | **Sumber menggantung** | tidak ada daftar pustaka di berkas untuk dicocokkan | lengkapi rujukan |
| Seluruh naskah | **Timpang** | Bab II–IV masing-masing 1–2 kalimat | isi setelah struktur beres |

### Tabel pemetaan

| Rumusan | Tujuan | Bab penjawab | Bukti | Kesimpulan | Saran |
|---|---|---|---|---|---|
| RM1 tingkat penggunaan | [TIDAK ADA DI BERKAS] | §4.1 | Tabel 4.1 | §5.1 | §5.2 (lemah) |
| RM2 faktor minat | [TIDAK ADA DI BERKAS] | §4.2 | — | §5.1 (sebagian) | — |
| RM3 dampak ke omzet | [TIDAK ADA DI BERKAS] | **—** | **—** | **—** | **—** |

## 5. Rencana perbaikan (7 langkah)

1. **Gali** — putuskan RM3: kumpulkan data omzet sebelum–sesudah QRIS, atau hapus RM3 dari §1.2. Tanpa ini naskah putus.
2. **Gali** — sumber untuk klaim §1.1, atau ganti klaimnya dengan yang bisa dibuktikan.
3. **Potong** — §2.2 Sejarah uang kertas.
4. **Gali** — tambahkan landasan teori untuk RM2 di Bab II (teori minat/penerimaan teknologi) `[CEK: sumber]`.
5. **Gali** — lengkapi §3.1: teknik sampling, instrumen, teknik analisis RM2.
6. **Pindah** — tambah sub-bab Tujuan di Bab I yang sejajar dengan RM (sekarang tidak ada).
7. **Pindah** — sejajarkan §5.1 dan §5.2 dengan RM1–RM2(–RM3) dan temuan §4.2.

## 6. Yang tidak ada di berkas
- [TIDAK ADA DI BERKAS: tujuan penelitian]
- [TIDAK ADA DI BERKAS: sumber klaim "semua UMKM sudah memakai QRIS sejak 2023"]
- [TIDAK ADA DI BERKAS: data omzet untuk RM3]
- [TIDAK ADA DI BERKAS: teknik sampling & teknik analisis]
- [TIDAK ADA DI BERKAS: daftar pustaka]

## 7. Hasil cek

| Butir | Status | Perbaikan |
|---|---|---|
| R1 Tiap bagian punya baris peta | Lolos | 9 baris |
| R2 Tidak ada fakta dari luar berkas | Lolos | — |
| R3 Nomor asli dipertahankan | Lolos | §1.1–§5.2, Tabel 4.1 |
| R4 Berkas gagal dibaca disebut | Lolos | tidak ada |
| R5 Temuan menunjuk bagian | Lolos | — |
| R6 Potong/pindah/gali | Lolos | — |
| R7 Konflik antarberkas | Lolos (tidak berlaku) | satu berkas |
| U4 Tidak ada yatim (naskah) | Gagal | RM3, §2.2 |

Judul tidak diberikan: kerangka naskah gagal secara struktural (RM3 yatim). Setelah langkah 1 selesai, judul bisa disusun dari core claim.

Langkah berikut: putuskan RM3 dengan pembimbing sebelum menulis ulang apa pun.
