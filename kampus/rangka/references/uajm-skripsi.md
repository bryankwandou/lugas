# UAJM — Kerangka Tugas Akhir / Skripsi, Bab I–V penuh + lampiran

Sumber: *Pedoman Penulisan Skripsi Prodi Teknik Informatika UAJM*, Bab IV.
Format naskah: `uajm-format.md`. Tahap proposal: `uajm-usulan-ta.md`.
Katalog lampiran: `appendices.md`.

Catatan penamaan: pedoman menyebut lima bagian utama tanpa penomoran Romawi eksplisit
di daftar isinya, tetapi penomoran bab naskah memakai angka Romawi (`BAB I` … `BAB V`).
Jadi lima bagian itu = Bab I sampai Bab V.

## Bagian awal — 15 komponen, urutan terkunci

| # | Komponen | Catatan |
|---|---|---|
| 1 | Sampul Depan | warna prodi, judul 14 bold, lambang UAJM, `PROGRAM STUDI ... / FAKULTAS TEKNOLOGI INFORMASI / UNIVERSITAS ATMA JAYA / MAKASSAR` + bulan & tahun lulus |
| 2 | Halaman Judul | isi sama, kertas putih |
| 3 | Halaman Pengajuan | pernyataan pengajuan untuk memenuhi syarat gelar |
| 4 | **Halaman Pernyataan Tidak Plagiat** | bermeterai — `[ISI: meterai + tanggal]` |
| 5 | Halaman Persetujuan/Pengesahan | pembimbing I & II, ketua prodi, panitia ujian |
| 6 | Halaman Pedoman Penggunaan Skripsi | izin pengutipan/penggandaan |
| 7 | Halaman Peruntukan | persembahan; **bukan tempat ucapan terima kasih** |
| 8 | Kata Pengantar | urutan terima kasih: pembimbing → ketua & sekretaris prodi → pihak lain; tanpa hal ilmiah; "saya" → "penulis" |
| 9 | **Abstrak bahasa Indonesia** | satu alinea, spasi tunggal |
| 10 | **Abstrak bahasa Inggris** | idem; untuk naskah jurnal dibatasi 100 kata |
| 11 | Daftar Isi | |
| 12 | Daftar Tabel | |
| 13 | Daftar Gambar | termasuk bagan, diagram, peta, foto, sketsa, skema |
| 14 | Daftar Lampiran | |
| 15 | Daftar Arti Lambang dan Singkatan | dua kolom, urut abjad; wajib bila singkatan/lambang banyak |

Komponen 3, 4, 6, dan 7 adalah yang paling sering hilang dari draf mahasiswa karena
tidak ada di template kampus lain. Selalu munculkan di kerangka, walau isinya `[ISI]`.

Isi abstrak (kerangka empat kalimat): masalah & konteks → tujuan → metode/pendekatan →
hasil utama + kata kunci 3–5.

## Bagian utama — Bab I sampai Bab V

### BAB I PENDAHULUAN
Semua butir di bawah berada **di dalam bab pendahuluan**, dengan urutan pedoman:

| Sub | Tugas | Isi | Uji cepat |
|---|---|---|---|
| 1.1 Latar Belakang | menunjukkan masalah penting untuk diteliti | Das Sollen → Das Sein → selisihnya | ada minimal satu fakta lapangan/angka, bukan hanya kutipan teori |
| 1.2 Rumusan Masalah | pertanyaan yang perlu dijawab lewat proses penelitian | kalimat tanya, diturunkan dari 1.1 | tiap pertanyaan punya bab yang menjawabnya |
| 1.3 Tujuan Penelitian | sesuatu yang ingin dicapai | satu tujuan per rumusan masalah | kata kerja terukur (merancang, menguji, mengukur — bukan "mengetahui" saja) |
| 1.4 Luaran yang Diharapkan | output konkret | sistem/prototipe/model/artikel jurnal | disebut lagi di Bab IV |
| 1.5 Manfaat Penelitian | manfaat bagi pengembangan ilmu **maupun pembangunan yang lebih luas** | teoretis + praktis | tidak mengulang tujuan |
| 1.6 Batasan / Ruang Lingkup | menjaga penelitian tetap fokus, tidak meluas dan mengambang | batas data, platform, wilayah, periode, pengguna | tiap batasan punya alasan, bukan sekadar daftar |
| 1.7 **Kerangka Pikir (bagan)** | memperlihatkan alur nalar | bagan: input → proses → output, atau masalah → teori → metode → luaran | wajib berbentuk bagan, bukan paragraf |

### BAB II TINJAUAN PUSTAKA DAN LANDASAN TEORI
- 2.1 Tinjauan Pustaka — hasil penelitian sebelumnya yang **relevan** dengan masalah.
  Bentuk yang tahan uji: matriks `penulis · tahun · masalah · metode · hasil ·
  keterbatasan · relevansi dengan penelitian ini`. Matriks ini sekaligus jadi bukti
  keaslian yang dijanjikan di usulan.
- 2.2 Landasan Teori — penjabaran dari tinjauan pustaka; boleh uraian kualitatif, model
  matematik, atau persamaan; harus **langsung berkaitan** dengan materi yang diteliti.
- 2.3 Kerangka Konsep / Hipotesis *(bila jenis penelitiannya menuntut)*.

Aturan pemangkas: satu teori boleh masuk Bab II hanya kalau dipakai lagi di Bab III
(sebagai dasar metode) atau Bab IV (sebagai alat pembahasan). Teori yang tidak
dipakai lagi adalah orphan → buang.

### BAB III METODE PENULISAN DAN PENELITIAN
Tujuh unsur menurut pedoman:
1. **Bahan/materi penelitian** beserta spesifikasinya;
2. **Alat** yang digunakan beserta gambar dan spesifikasinya;
3. **Objek/jenis penelitian** — metode/klasifikasi/jenis penelitian yang dilakukan
   (lihat daftar jenis di `uajm-usulan-ta.md`);
4. **Alat/data/variabel** yang dapat memengaruhi kualitas hasil — diuraikan jelas;
5. **Rancangan dan langkah-langkah percobaan** — prosedur sistematis, terinci, jelas;
6. **Metode pengumpulan data** — langkah dan teknik;
7. **Hipotesis (opsional)** dan **analisis data + alat analisis** — model dan cara
   menganalisis data dan tabel.

Untuk penelitian rekayasa perangkat lunak, petakan langkah 5 ke siklus
`plan → analysis → construct → applied`, dan nyatakan model pengembangan yang dipakai
(waterfall, prototyping, RAD, Scrum) dengan sumbernya `[CEK: sumber model]`.
Rancangan pengujian (black box, white box, UAT, pengukuran kinerja) masuk di sini —
bukan baru muncul di Bab IV.

### BAB IV ANALISIS: HASIL DAN PEMBAHASAN
Dua lapis yang harus terpisah jelas:
- **Hasil** — hasil pengumpulan data dalam bentuk tabel, grafik, atau bentuk lain,
  dilengkapi uraian yang **merujuk pada tabel/grafik itu**. Setiap tabel dan gambar
  harus disebut di dalam teks; yang tak pernah disebut akan dicoret.
- **Pembahasan** — penjelasan teoretis atas hasil, kualitatif maupun kuantitatif atau
  statistik, dan **dibandingkan dengan hasil penelitian sebelumnya yang sejenis**
  (pedoman menganjurkan ini secara eksplisit — inilah yang menyambungkan Bab IV ke
  matriks Bab II).

Susun sub-bab Bab IV **mengikuti urutan rumusan masalah**, bukan urutan pekerjaan.

### BAB V PENUTUP
- 5.1 Kesimpulan — pada prinsipnya **jawaban dari rumusan masalah dan tujuan** di Bab I.
  Pemetaan satu-satu. Tidak ada kesimpulan baru yang tidak pernah ditanyakan.
- 5.2 Saran — **diprioritaskan pada butir-butir kesimpulan yang ada**.
- 5.3 Keterbatasan Penelitian *(opsional)* — keterbatasan yang nyata ada.

Tabel penutup yang wajib dibuat Rangka sebelum menyerahkan kerangka:

| Rumusan masalah | Tujuan | Bab/sub yang menjawab | Bukti | Kesimpulan | Saran |
|---|---|---|---|---|---|

Baris yang kosong di kolom mana pun = cacat kerangka. Perbaiki sebelum drafting.

## Bagian akhir
- **Daftar Rujukan/Pustaka** — gaya UAJM, lihat `uajm-format.md`.
- **Lampiran** — nomor urut 1..n; nomor halaman melanjutkan bab sebelumnya. Boleh
  berupa daftar pertanyaan (kuesioner), transkrip wawancara, lembar hitungan, print-out
  statistik, daftar riwayat hidup, dan keterangan lain.
- **Naskah jurnal** — berkas terpisah, format di `uajm-format.md`.

Lampiran yang praktis selalu diminta untuk TA Informatika UAJM:
kartu/lembar bimbingan · berita acara & daftar hadir seminar judul dan seminar hasil ·
matriks tanggapan penguji + bukti perbaikan · surat izin penelitian & surat balasan
instansi · instrumen penelitian (kuesioner/panduan wawancara) + uji validitas-
reliabilitas · data mentah dan hasil olahan · **kode sumber program** · dokumentasi
antarmuka · hasil pengujian (black box / UAT) · daftar riwayat hidup · pernyataan
tidak plagiat bermeterai · hasil cek kemiripan `[CEK: apakah prodi mewajibkan]`.

## Peta inti khas skripsi rekayasa UAJM

| Node | Isi |
|---|---|
| Should | perilaku sistem/proses yang dituntut teori, standar, atau kebutuhan pengguna |
| Is | sistem/proses yang berjalan sekarang + kelemahannya (data lapangan) |
| Gap | rumusan masalah |
| Reader | 4 penguji + 2 pembimbing; yang dinilai: isi & penulisan, penguasaan materi, penampilan |
| Core claim | "Dengan [metode], [masalah] dapat [diselesaikan/diukur] sehingga [hasil terukur]" |
| Proof | rancangan + implementasi + hasil pengujian, dibanding penelitian sejenis |
| Action | kontribusi keilmuan + rekomendasi penerapan + arah penelitian lanjutan |

## Cek khusus skripsi (tambahan untuk `checklist.md`)

| Kode | Cek |
|---|---|
| S1 | Ke-15 komponen bagian awal muncul di kerangka (termasuk Pengajuan, Tidak Plagiat, Pedoman Penggunaan, Peruntukan)? |
| S2 | Abstrak Indonesia **dan** Inggris ada? |
| S3 | Kerangka pikir berbentuk bagan di Bab I? |
| S4 | Setiap rumusan masalah punya tujuan, bab penjawab, bukti, kesimpulan, dan saran (tabel penutup terisi penuh)? |
| S5 | Setiap teori di Bab II dipakai lagi di Bab III atau IV? |
| S6 | Tujuh unsur Bab III lengkap, termasuk rancangan pengujian? |
| S7 | Sub-bab Bab IV mengikuti urutan rumusan masalah? |
| S8 | Pembahasan membandingkan hasil dengan penelitian sebelumnya yang sejenis? |
| S9 | Tidak ada kesimpulan yang tak pernah ditanyakan di Bab I? |
| S10 | Setiap saran menempel pada satu butir kesimpulan? |
| S11 | Daftar lampiran sinkron dengan lampiran yang benar-benar direncanakan? |
| S12 | Kerangka naskah jurnal sudah diturunkan dari kerangka TA? |
