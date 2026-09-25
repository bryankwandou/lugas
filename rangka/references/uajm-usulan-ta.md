# UAJM — Kerangka Usulan Tugas Akhir (proposal) & Ringkasan Kapasitas Diri

Sumber: *Pedoman Penulisan Skripsi Prodi Teknik Informatika UAJM*, Bab II dan Bab III.
Format naskah: `uajm-format.md`. Kerangka skripsi penuh: `uajm-skripsi.md`.

## Dua skema — tanya ini lebih dulu

Mahasiswa memilih **salah satu**; dokumen yang disusun berbeda total.

| | Penelitian **Mandiri** | Penelitian **Terstruktur** |
|---|---|---|
| Diusulkan oleh | mahasiswa | mahasiswa ikut penelitian dosen/industri |
| Dokumen awal | **Usulan TA (proposal)** | **Ringkasan Kapasitas Diri (RKD)** |
| Diuji oleh | seminar usulan judul, **min. 4 dosen penguji** (setuju/tolak/revisi); kaprodi mengesahkan | ketua tim peneliti (evaluasi + wawancara) |
| Pembimbing | ditetapkan kaprodi | ketua tim = pembimbing I, anggota tim = pembimbing II |
| Evaluasi tengah | seminar hasil (penelitian sudah tahap akhir) | seminar kemajuan (**≥75%** dari tahap rencana) |
| Kehadiran panitia | ≥75%, min. 1 pembimbing + 2 penguji | min. 1 pembimbing + 1 penguji di luar tim |
| Peserta seminar | ≥5 rekan sejawat serumpun | — |

Kalau user belum tahu skemanya, **ini satu-satunya pertanyaan yang layak ditanyakan
di muka** (aturan "maksimal satu pertanyaan" di SKILL.md). Kalau tetap tak terjawab,
susun kerangka Usulan TA dan beri catatan bahwa skema terstruktur memakai RKD.

## Syarat masuk

115 sks lulus + mengambil MK Tugas Mandiri dan Seminar pada semester berjalan +
administrasi. Ujian TA: IPK minimum **2,75**, semua MK dan praktikum lulus, panitia
dibentuk dengan SK Dekan FTI.

Judul masih boleh berubah dalam pelaksanaan lewat persetujuan penuh pembimbing,
**asal tidak mengubah tujuan awal pengusulan.** Pakai ini saat user panik karena
datanya bergeser: yang harus dijaga adalah tujuan, bukan kalimat judul.

## Batas fisik

Usulan TA dan RKD: **tidak lebih dari 30 lembar** (TA 2.3, 3.2). Ini mengikat pembagian
panjang kerangka. Pembagian berikut adalah **anjuran Rangka, bukan pedoman**: Latar Belakang 4–6 · Tinjauan Pustaka &
Landasan Teori 8–12 · Metode 5–7 · Konsideran 2–3 · Jadwal 1 · sisanya bagian awal
dan daftar pustaka.

## Tujuh pertanyaan penguji (kerangka usulan harus menjawab semuanya)

1. Mengapa judul yang diajukan penting atau berguna?
2. Apa yang akan diteliti/dirancang/dianalisa, dan **sampai di mana batasnya**?
3. Teori apa yang mendukung, penelitian apa saja yang diacu?
4. Bagaimana cara/proses pelaksanaannya?
5. Apa perkiraan hasil/luaran yang diharapkan?
6. Berapa lama target waktunya?
7. Apakah sumber dayanya dapat dipenuhi?

Jalankan ini sebagai cek terakhir sebelum kerangka diserahkan. Pertanyaan 7 yang
paling sering menjatuhkan usulan mahasiswa Informatika: dataset tidak ada, akses
instansi belum pasti, atau perangkat tidak sanggup. Kalau ada yang menggantung,
tulis `[ISI: bukti ketersediaan ...]` dan katakan risikonya terang-terangan.

## Klasifikasi penelitian — tentukan sebelum menyusun Bab metode

**Berdasarkan fungsi:** dasar (mengembangkan teori) · terapan (menerapkan ke kenyataan
praktis) · evaluatif (menilai keberhasilan, manfaat, kelayakan program suatu unit).

**Berdasarkan metode keilmuan:**

*Rekayasa* — menerapkan ilmu jadi rancangan untuk mendapat kinerja sesuai persyaratan;
siklus `plan → analysis → construct → applied`:
- **Forward engineering** — perencanaan → perancangan → pembangunan → penerapan
  (abstraksi tinggi ke rendah);
- **Reverse engineering** — dari produk/sistem/prototipe yang ada menjadi blueprint,
  formula, atau model (abstraksi rendah ke tinggi);
- **Re-engineering** — mengubah dan mengorganisasi ulang komponen sistem tanpa
  menghilangkan seluruh komponen lama, untuk standar yang lebih tinggi.

*Nonrekayasa* — historis · deskriptif · korelasional · kausal komparatif ·
eksperimental · grounded research · tindakan (action research) · studi kasus.

Konsekuensi yang wajib dipegang Rangka:

| Jenis | Metode berisi | Hasil berisi | Hipotesis |
|---|---|---|---|
| Rekayasa forward | tahap plan/analysis/construct/applied, alat & bahan, rancangan uji | spesifikasi, hasil pengujian, perbandingan dengan persyaratan | tidak ada, **kecuali** ada evaluasi komparatif (sistem vs baseline/metode pembanding) yang diuji statistik (mis. McNemar, Wilcoxon, uji-t berpasangan) — maka hipotesis perbandingan kinerja boleh, bahkan wajib bila uji itu ada di metode |
| Rekayasa reverse/re-eng | objek yang dibedah, tahap abstraksi yang dituju | model/blueprint hasil + validasinya | tidak ada |
| Eksperimental | perlakuan, kontrol, variabel | uji statistik | **wajib** |
| Korelasional / kausal komparatif | variabel, instrumen, populasi & sampel | uji hubungan | wajib |
| Deskriptif / studi kasus | unit analisis, batas kasus, teknik pengumpulan | pola temuan | opsional |
| Action research | siklus tindakan + decision maker | perubahan per siklus | opsional |

Kesalahan klasik mahasiswa Informatika: mengambil penelitian rekayasa (bikin aplikasi)
lalu memaksakan hipotesis dan uji-t. Kalau ini muncul, tolak dengan alasan, jangan
ikuti. Yang ditolak adalah uji-t pada fitur aplikasi **tanpa pembanding** (mis. "aplikasi
berpengaruh terhadap kepuasan" dari satu kuesioner), **bukan** hipotesis perbandingan
kinerja sistem terhadap baseline yang diuji statistik. Jangan buang H1–Hn yang
berpasangan dengan uji statistik di Metode; cek saja bahwa tiap hipotesis punya uji,
data, dan metrik yang cocok.

## Kerangka Usulan TA (proposal)

**Dua bentuk yang beredar — pilih dulu.** Pedoman 2015 memakai susunan **a–f** (di
bawah). Template prodi yang dipakai mahasiswa sekarang memakai **BAB I–V dengan subbab
terpisah** plus abstrak dan daftar-daftar (lihat "Bentuk B"). Cara memilih:

1. User membawa berkas (draf, template, contoh kakak tingkat) → **deteksi dari berkas**:
   ada "BAB I" / "1.1" / "Daftar Isi" / "Abstrak" → Bentuk B; ada "a. Latar Belakang …
   f. Jadwal" tanpa BAB → Bentuk A. Sebutkan dasar deteksinya dalam satu kalimat.
2. Tak ada berkas → tanyakan satu kali: "Template prodi Anda BAB I–V (dengan Daftar
   Isi/Abstrak) atau susunan a–f pedoman 2015?" Ini boleh menjadi satu-satunya pertanyaan
   di muka bersama pertanyaan skema; gabungkan jadi satu kalimat.
3. Tetap tak terjawab → keluarkan **Bentuk B** (lebih sering dipakai sekarang) dan beri
   peta satu baris ke Bentuk A. `[CEK: template prodi yang berlaku]`.

Isi wajib kedua bentuk sama; yang beda hanya letak dan tingkat heading.

### Bentuk B — template prodi (BAB I–V), bukan teks pedoman 2015

**Bagian awal:** Halaman Judul (label `Usulan/Proposal Tugas Akhir`) · Halaman
Persetujuan · Abstrak & Abstract *(jika template memintanya)* · Daftar Isi · Daftar Tabel
· Daftar Gambar · Daftar Lampiran · Daftar Arti Lambang dan Singkatan *(jika ada)*.

| Bab | Subbab | Asal di Bentuk A |
|---|---|---|
| BAB I Pendahuluan | 1.1 Latar Belakang · 1.2 Rumusan Masalah · 1.3 Tujuan · 1.4 Luaran/Hasil yang Diharapkan · 1.5 Manfaat · 1.6 Batasan Masalah · 1.7 Keaslian Penelitian *(kerangka pikir boleh di 1.x atau di Bab II)* | §a |
| BAB II Tinjauan Pustaka dan Landasan Teori | 2.1 Tinjauan Pustaka (penelitian terdahulu, tabel pembanding) · 2.2 Landasan Teori · 2.3 Kerangka Pikir (bagan) · 2.4 Hipotesis *(jika ada — lihat tabel Konsekuensi)* | §b, §c |
| BAB III Metode Penelitian | 3.1 Objek/Jenis Penelitian · 3.2 Alat dan Bahan · 3.3 Rancangan dan Langkah Penelitian · 3.4 Metode Pengumpulan Data · 3.5 Analisis Data | §d |
| BAB IV Konsideran Percobaan | 4.1 Data Masukan · 4.2 Penyusunan Model/Sistem · 4.3 Uji Kesahihan · 4.4 Analisa Kepekaan | §e |
| BAB V Jadwal Pelaksanaan | tahap · rincian · durasi (tabel/Gantt) | §f |

**Bagian akhir:** Daftar Pustaka · Lampiran (termasuk Daftar Riwayat Hidup bila template
memintanya). Batas ≤30 lembar tetap berlaku; bagian awal yang lebih panjang memakan
jatah itu.

### Bentuk A — susunan pedoman 2015 (a–f)

**Bagian awal**
1. Halaman Judul — sama seperti halaman judul skripsi, **ditambah tulisan
   `Usulan/Proposal Tugas Akhir`** tepat pada sembir atas, bold + italic, simetris.
   Judul singkat, tepat menunjuk masalah, tidak membuka penafsiran beragam.
2. Halaman Persetujuan — pembimbing I, pembimbing II, ketua prodi + tanda tangan
   dan tanggal.

**Bagian utama**

| § | Bagian | Tugas | Isi wajib |
|---|---|---|---|
| a | Latar Belakang Penulisan/Penelitian | membuat penguji yakin masalahnya nyata **dan baru** | penjelasan umum materi · alasan masalah menarik, penting, perlu diungkap (**perumusan masalah**) · **tujuan** spesifik · **luaran** yang diharapkan · **manfaat** bagi ilmu & pembangunan · **batasan/ruang lingkup** · **kerangka pikir dalam bentuk bagan** · **keaslian**: tunjukkan masalah belum pernah dipecahkan atau nyatakan tegas bedanya dengan yang sudah ada |
| b | Tinjauan Pustaka | menunjukkan masalah belum terjawab memuaskan | uraian sistematis hasil penelitian sebelumnya, diambil dari **sumber asli**, dengan nama penulis + tahun. Landasan teori dijabarkan dari tinjauan pustaka, **disusun sendiri oleh mahasiswa**, boleh uraian kualitatif/definisi/model matematik/persamaan |
| c | Hipotesa *(jika ada)* | jawaban sementara | pernyataan singkat yang disimpulkan dari landasan teori + tinjauan pustaka, masih harus dibuktikan |
| d | Metode Penulisan/Penelitian | menunjukkan penelitian bisa dijalankan | 1) objek/jenis penelitian 2) alat yang digunakan (+ gambar & keterangan bila perlu) 3) rancangan dan langkah-langkah percobaan 4) metode pengumpulan data 5) analisis data |
| e | Konsideran Percobaan | menutup lubang kelayakan | data masukan yang jadi landasan pengembangan · penyusunan model/sistem dari data itu · metode **uji kesahihan** dan **analisa kepekaan** terhadap hasil |
| f | Jadwal Pelaksanaan | membuktikan waktunya cukup | tahap · rincian kegiatan tiap tahap · waktu tiap tahap |

Catatan penting soal §a: di UAJM, **rumusan masalah, tujuan, luaran, manfaat, batasan,
dan kerangka pikir semuanya berada di dalam "Latar Belakang"**, bukan sebagai sub-bab
sejajar. Banyak template dari kampus lain memisahkannya — kalau user membawa template
begitu, sebutkan bedanya dan ikuti pedoman UAJM kecuali pembimbing memerintahkan lain
(`[CEK: preferensi pembimbing]`).

**Bagian akhir** — Daftar Pustaka + Lampiran (jika ada).

## Kerangka Ringkasan Kapasitas Diri (RKD)

Fungsi berbeda: bukan membuktikan **masalahnya** layak, tapi membuktikan **orangnya**
layak ikut penelitian terstruktur yang sudah ada.

Lima pertanyaan dasarnya:
1. Mengapa keterlibatan diri yang diajukan relevan atau berguna?
2. Apa yang dipahami terhadap topik yang diteliti; sampai di mana pemahaman terhadap
   tujuan penelitian itu?
3. Pengetahuan dan/atau pengalaman apa yang mendukung keterlibatan?
4. Sejauh mana pemahaman terhadap landasan pengetahuan dan teori serta tujuan penelitian
   yang jadi prasyarat keterlibatan?
5. Berapa lama waktu yang diperlukan?

Struktur (TA Bab III, 3.2):

| Bagian | Isi | Beda dengan Usulan TA |
|---|---|---|
| Halaman Judul | sama dengan halaman judul skripsi + tulisan `Ringkasan Kapasitas Diri Tugas Akhir` pada sembir atas, bold + italic, simetris | label berbeda |
| Halaman Persetujuan | pembimbing I, pembimbing II, ketua prodi + tanda tangan & tanggal | sama |
| a. Latar Belakang | pemahaman materi · alasan **kapasitas mahasiswa** dipandang layak · pemahaman tujuan penelitian **terhadap rentang waktu yang disepakati** · luaran · manfaat (bagi ilmu & pengembangan penelitian) · batasan/ruang lingkup · **kerangka pikir dalam bentuk bagan** | tanpa keaslian/novelty — masalahnya milik tim peneliti |
| b. Tinjauan Pustaka (+ landasan teori) | menunjukkan mahasiswa **memahami** permasalahan; landasan teori menunjukkan kompetensi diri | fungsi berbeda: bukti paham, bukan bukti celah |
| c. Metode Penulisan/Penelitian | pemahaman atas 5 unsur: objek/jenis · alat · rancangan & langkah · pengumpulan data · analisis data | sama, dinyatakan sebagai "pemahaman" |
| d. **Kapasitas Diri** | pemahaman, pengetahuan, dan pengalaman mahasiswa sebagai landasan keterlibatan | **menggantikan Konsideran Percobaan** |
| e. Jadwal Pelaksanaan | tahap · rincian kegiatan · waktu | sama |
| Bagian akhir | Daftar Pustaka + Lampiran (jika ada) | sama |

RKD **tidak memuat Hipotesa dan tidak memuat Konsideran Percobaan**. Maksimal 30 lembar.
Setelah RKD: ketua tim peneliti mengevaluasi + mewawancarai; ketua prodi mengesahkan;
ketua tim = pembimbing I, anggota tim = pembimbing II. Keterlibatan boleh berubah/batal
dengan persetujuan ketua tim, disampaikan ke ketua prodi.

Perbedaan nada yang harus dijaga: RKD boleh — bahkan harus — menyatakan bekal konkret
pengusul (mata kuliah, proyek, bahasa pemrograman, pengalaman kerja). Itu bukan
kesombongan, itu isi dokumennya.

## Cek khusus usulan (tambahan untuk `checklist.md`)

| Kode | Cek |
|---|---|
| P1 | Ketujuh pertanyaan penguji terjawab di kerangka? |
| P2 | Jenis penelitian ditetapkan, dan metode + hasil konsisten dengan jenis itu? |
| P3 | Hipotesis ada hanya jika jenis penelitiannya menuntut — termasuk rekayasa yang membandingkan dengan baseline memakai uji statistik? Tiap hipotesis punya uji di Metode? |
| P4 | **Keaslian** dinyatakan tegas (belum pernah dipecahkan, atau beda dengan yang ada)? |
| P5 | Kerangka pikir tersedia **dalam bentuk bagan**? |
| P6 | Batasan/ruang lingkup menutup penafsiran yang melebar? |
| P7 | Konsideran memuat uji kesahihan dan analisa kepekaan **terhadap hasil** — baca isinya, bukan judulnya: parameter/masukan mana yang diubah, metrik mana yang diamati, rentangnya? Kelayakan TELOS/finansial, SWOT, atau uji fungsional *bukan* analisa kepekaan; kalau isinya begitu, tandai walau judul subbabnya benar. |
| P8 | Jadwal punya tahap + rincian + durasi, dan muat dalam satu semester? |
| P9 | Total ≤30 lembar? |
| P10 | Ketersediaan data/akses/perangkat sudah dibuktikan atau ditandai `[ISI]`? |
| P11 | (RKD) Ada bagian **Kapasitas Diri**, dan tidak ada Hipotesa/Konsideran? |
| P12 | Bentuk (A a–f atau B BAB I–V) sudah dipilih/dideteksi, dan dipakai konsisten dari daftar isi sampai isi? |
