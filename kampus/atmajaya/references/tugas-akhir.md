# Tugas Akhir / Skripsi dan naskah jurnal

Sumber: *Pedoman Penulisan Skripsi*, Prodi Informatika FTI UAJM, 1 April 2015, revisi
10 Juni 2015. Klausul `TA x.y.z`.

## §1 Memilih jalur

Lihat `proposal.md` bagian awal: mandiri → proposal; terstruktur → Ringkasan Kapasitas
Diri. Skripsi akhirnya sama bentuknya untuk kedua jalur.

## §2 Gerbang ujian (TA 1.5)

| Syarat | Nilai |
|---|---|
| IPK | **≥ 2,75** |
| Mata kuliah | semua lulus, termasuk praktikum |
| Administrasi | terpenuhi |
| SK panitia | ditetapkan Dekan FTI |
| Kehadiran panitia | ≥ 80 %: Ketua atau Sekretaris + ≥ 2 penguji |
| Ketua sidang | min. Lektor Kepala / IV-A / S-3 |
| Pembimbing | anggota panitia **ex-officio, tidak ikut menguji** |

Penetapan pembimbing (TA 1.3.2): oleh prodi, ditetapkan ketua prodi, dengan
pertimbangan relevansi judul–keahlian, pemerataan bimbingan, dan asal judul (a–c).

| Peran | Syarat minimal | Klausul |
|---|---|---|
| Pembimbing I (utama) | Lektor **atau** golongan IV-A **atau** S-2 | TA 1.3.2d |
| Pembimbing II (pembantu) | Asisten Ahli **atau** S-2 | TA 1.3.2e |
| Dosen luar biasa | boleh sebagai pembimbing pembantu, dengan persetujuan jurusan | TA 1.3.2f |

## §3 Jenis penelitian menentukan Bab III (TA 2.2)

Tentukan ini sebelum menulis Bab III. Salah kategori merusak Bab III dan IV sekaligus.

| Pertanyaan | Kalau ya |
|---|---|
| Hasil utamanya sebuah sistem, aplikasi, model, atau rancangan yang dibangun? | **Rekayasa** (2.2.2a) |
| Membangun dari kebutuhan ke implementasi? | forward engineering |
| Membongkar sistem yang ada menjadi model/rancangan? | reverse engineering |
| Mengubah/menata ulang komponen sistem yang ada tanpa membuang semuanya? | re-engineering |
| Hasil utamanya pengetahuan tentang orang, organisasi, atau fenomena? | **Nonrekayasa** (2.2.2b): historis · deskriptif · korelasional · kausal komparatif · eksperimental · grounded · tindakan · studi kasus |

Fungsi penelitian (2.2.1), disebut di Bab III: dasar · terapan · evaluatif.

### Bab III versi rekayasa — siklus plan → analysis → construct → applied

```
BAB III METODE PENULISAN DAN PENELITIAN                   TA 4.2.3
3.1 Jenis Penelitian        [ISI: rekayasa, bentuk (forward/reverse/re-), fungsi (terapan…)]
3.2 Bahan/Materi            [ISI: data/dokumen yang dipakai + spesifikasi]
3.3 Alat                    [ISI: perangkat keras & lunak + spesifikasi; gambar bila perlu]
3.4 Tahapan Penelitian      [ISI: bagan alir tahapan]
    3.4.1 Perencanaan (plan)        [ISI]
    3.4.2 Analisis (analysis)       [ISI: analisis sistem berjalan, kebutuhan fungsional
                                     dan nonfungsional]
    3.4.3 Perancangan & Pembangunan (construct)   [ISI: model proses/data, UI, basis data]
    3.4.4 Penerapan & Pengujian (applied)         [ISI: metode uji — mis. black-box, UAT;
                                                   kriteria lulus uji]
3.5 Metode Pengumpulan Data [ISI: wawancara/observasi/dokumen — dengan siapa, kapan]
3.6 Analisis Data           [ISI: bagaimana hasil uji dianalisis]
```

### Bab III versi nonrekayasa

```
3.1 Jenis Penelitian        [ISI: salah satu dari delapan bentuk + fungsi]
3.2 Objek Penelitian        [ISI]
3.3 Variabel / Data         [ISI: definisi operasional]
3.4 Hipotesis (opsional)    [ISI]
3.5 Rancangan dan Langkah   [ISI]
3.6 Metode Pengumpulan Data [ISI: populasi, sampel, instrumen, kapan]
3.7 Analisis Data dan Alat Analisis   [ISI: teknik + perangkat lunak statistik]
```

Penomoran subbab di kedua versi adalah **saran** yang memuat seluruh butir TA 4.2.3.

## §4 Kerangka skripsi lengkap

```
BAGIAN AWAL — nomor Romawi kecil, diperhitungkan tetapi TIDAK dicetak   TA 4.1
 a Sampul depan (hijau muda polos; judul Indonesia + judul Inggris italic)  4.1.1
 b Halaman judul                                    i                 4.1.2
 c Halaman pengajuan                                ii                4.1.3
 d Halaman pernyataan tidak plagiat                 iii               4.1.4
 e Halaman persetujuan/pengesahan                   iv                4.1.5
 f Halaman pedoman penggunaan skripsi               v                 4.1.6
 g Halaman peruntukan (tidak wajib)                 vi                4.1.7
 h Kata pengantar                                   vii               4.1.8
 i Abstrak (Indonesia) — 200–250 kata, spasi 1                         4.1.9
 j Abstract (Inggris) — ketentuan sama                                 4.1.10
 k Daftar isi · l Daftar tabel · m Daftar gambar · n Daftar lampiran   4.1.11–14
 o Daftar arti lambang dan singkatan (jika ada)                        4.1.15

BAB I PENDAHULUAN                                                      4.2.1
 1.1 Latar Belakang        [ISI: mengapa masalah ini penting diteliti — dengan data]
 1.2 Rumusan Masalah       [ISI: bernomor]
 1.3 Tujuan Penelitian     [ISI: berpasangan 1-1 dengan 1.2]
 1.4 Luaran yang Diharapkan [ISI: konkret]
 1.5 Manfaat Penelitian    [ISI]
 1.6 Batasan Masalah       [ISI]
 1.7 Kerangka Pikir        [ISI: BAGAN]
 (1.8 Sistematika Penulisan — tidak diminta pedoman; tanyakan pembimbing)

BAB II TINJAUAN PUSTAKA DAN LANDASAN TEORI                             4.2.2
 2.1 Penelitian Terdahulu  [ISI: yang relevan; tabel pembanding disarankan]
 2.2 Landasan Teori        [ISI: penjabaran tinjauan pustaka — kualitatif,
                            model matematik, atau persamaan yang langsung terkait]

BAB III METODE PENULISAN DAN PENELITIAN — versi §3                     4.2.3

BAB IV ANALISIS: HASIL DAN PEMBAHASAN                                  4.2.4
 4.1 Hasil                 [ISI: tabel/grafik — SETIAP tabel/gambar dirujuk di uraian]
 4.2 Pembahasan            [ISI: kualitatif/kuantitatif/statistik;
                            SEBAIKNYA dibandingkan dengan penelitian sejenis di 2.1]

BAB V PENUTUP                                                          4.2.5
 5.1 Kesimpulan            [ISI: jawaban atas tiap rumusan masalah dan tujuan]
 5.2 Saran                 [ISI: diprioritaskan pada butir kesimpulan]
 (5.3 Keterbatasan Penelitian — opsional)

DAFTAR PUSTAKA — nama-tahun gaya UAJM (pola TA 4.3.1), hanya yang dirujuk
LAMPIRAN — bernomor urut; nomor halaman melanjutkan bab sebelumnya
```

## §5 Tabel pemetaan — isi sebelum menyerahkan draf ke pembimbing

TA 4.2.5 membuat dua aturan yang paling sering menggagalkan revisi: kesimpulan adalah
jawaban atas rumusan masalah dan tujuan, dan saran diprioritaskan pada butir
kesimpulan. Isi tabel ini dari draf. **Satu sel kosong = kegagalan keras.**

| Rumusan masalah (1.2) | Tujuan (1.3) | Subbab yang menjawab | Bukti (Tabel/Gambar n) | Butir kesimpulan (5.1) | Saran (5.2) |
|---|---|---|---|---|---|
| RM1 | T1 | | | K1 | S1 |
| RM2 | T2 | | | K2 | S2 |

Tambahan: tiap luaran di 1.4 harus muncul sebagai hasil di Bab IV.

## §6 Naskah jurnal — berkas terpisah yang wajib menyertai TA

Ringkas dari lampiran *Tata Cara Penulisan Naskah Jurnal*; rinciannya di
`format.md` §C.

```
JUDUL (judul TA yang disetujui — TNR 14 bold kapital)
Penulis¹ (TNR 10 bold) · afiliasi · e-mail
ABSTRACT — Inggris, 1 alinea, ≤ 100 kata, TNR 11 italic, satu kolom:
           isu pokok + tujuan + metode + hasil
Keywords — 3–5, Inggris, dipisah koma
1 PENDAHULUAN            latar, masalah, tujuan, rencana pemecahan; belum pernah dipublikasikan
2 TINJAUAN PUSTAKA       teori + penelitian terdahulu → kerangka pemikiran; sitasi [n]
3 METODOLOGI PENELITIAN  NARATIF: rancangan, ruang lingkup, alat/data, pengumpulan & analisis
4 HASIL DAN PEMBAHASAN   tabel/grafik disarankan; interpretasi dikaitkan dengan teori
5 KESIMPULAN             menjawab tujuan; butir atau paragraf pendek
6 DAFTAR PUSTAKA         bernomor [n], Harvard; semua dirujuk di teks
```

Tiga angka yang sering tertukar: abstrak skripsi **200–250 kata** · abstract jurnal
**≤ 100 kata** · keywords **3–5**. Dan dua gaya pustaka: skripsi nama-tahun UAJM,
jurnal bernomor Harvard.

## §7 Pemeriksaan sebelum menyerahkan untuk sidang

Keras:

- [ ] Tabel pemetaan §5 tanpa sel kosong
- [ ] Halaman pernyataan tidak plagiat ada (4.1.4)
- [ ] Abstrak 200–250 kata; paragraf pertama: NAMA KAPITAL, *judul miring*,
      (dibimbing oleh … tanpa gelar) (4.1.9)
- [ ] Judul Inggris italic di sampul (4.1.1)
- [ ] Kerangka pikir berbentuk bagan; luaran disebut (4.2.1)
- [ ] Jenis penelitian cocok dengan isi Bab III (2.2.2)
- [ ] Setiap tabel/gambar dirujuk di uraian (4.2.4)
- [ ] Format: margin 4-3-3-3, heading ≤ 4 tingkat, tanpa bullet, nomor tabel/gambar
      satu seri, judul tabel di atas dan judul gambar di bawah (`format.md`)
- [ ] Naskah jurnal terpisah siap (lampiran TA)

Lunak:

- [ ] Pembahasan tidak membandingkan dengan penelitian sejenis (4.2.4 "sebaiknya")
- [ ] Daftar tabel memakai 1,5 spasi antarnama — TA meminta 1 spasi (4.1.12)
