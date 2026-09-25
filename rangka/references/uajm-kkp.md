# UAJM — Kerangka Laporan KKP (magang / kerja praktek)

Sumber: *Pedoman Kuliah Kerja Profesi FTI UAJM*, Prodi Informatika, 18 Januari 2015
(Bab I–III), dicek ulang kalimat per kalimat 2026-09-25.
Format naskah: baca `uajm-format.md`. Bacaan ini hanya soal **struktur**.

KKP di UAJM adalah nama resmi untuk magang/kerja praktek. Kalau user menyebut
"magang", "KP", "PKL", atau "internship" dan kampusnya UAJM FTI, pakai berkas ini.

## Syarat yang menentukan bentuk kerangka

Ini bukan basa-basi administratif — tiga butir pertama mengubah isi Bab I dan
lampiran, jadi konfirmasikan lebih dulu (atau tulis `[ISI: ...]`).

| Butir | Ketentuan | Akibat pada kerangka |
|---|---|---|
| SKS | minimal 122 sks lulus | — |
| Durasi | min. 2 bulan berturut-turut, maks. 3 bulan; **min. setara 42 hari kerja penuh** (lokasi dalam kota) | jumlah entri log harian, rentang di §1.5 |
| Lingkup sah | (a) analisis & perancangan perangkat lunak/SI/jaringan, (b) pemrograman, (c) network administration | menentukan isi Bab III |
| Pembimbing | dosen pembimbing kampus (min. S-1, kompetensi sesuai materi) + pembimbing lapangan (ditunjuk pejabat instansi) | lihat catatan tanda tangan di Halaman Pengesahan |
| Seminar | setelah laporan disetujui pembimbing kampus; tim penilai = 1 dosen pembimbing kampus (ditunjuk kaprodi) + audiens **minimal 5 mahasiswa**; seminar **sebelum** dijilid dan disahkan | daftar hadir jadi lampiran `[CEK]` |
| Prosedur awal | observasi tempat → minta surat pengantar ke ketua prodi (lampirkan fotokopi KSM + form Permohonan Kerja Praktek) → serahkan ke instansi → serahkan **surat persetujuan penerimaan** ke prodi; kalau ditolak, surat pengantar baru wajib melampirkan **surat penolakan** | surat-surat ini masuk lampiran |
| Selama KKP | isi **Form Aktivitas Harian**; beri **Form Penilaian** ke pembimbing lapangan; orientasi, rencana kegiatan, catat struktur organisasi, analisis sistem berjalan, konsultasi, kumpulkan data | bahan Bab II–III |
| Nilai | lapangan 30% (kinerja, inovasi, kerja sama, kedisiplinan) + dosen pembimbing kampus 70% (materi, penguasaan materi, bahasa, tata penulisan, presentasi) | bobot 70% ada di laporan → Bab III harus tebal |
| Lingkup | instansi yang memakai TIK secara intensif; skala & kedalaman menimbang kontribusi pada bidang ilmu dan ketepatan waktu | — |
| Batas waktu | seluruh KKP maksimal satu semester, lewat → input ulang MK | jadwal di §1.6 harus realistis |

Kalau lingkup pekerjaan di lapangan tidak masuk salah satu dari tiga kategori
(misalnya mahasiswa ditaruh di bagian administrasi umum), itu **masalah kerangka
yang fatal**: seluruh Bab III kehilangan dasar. Jangan dipoles — katakan terus terang
dan tawarkan dua jalan: renegosiasi penempatan, atau cari irisan TIK dari pekerjaan
yang ada (mis. digitalisasi arsip → analisis sistem berjalan).

## Kerangka penuh

### Bagian awal
1. Halaman Sampul Depan — **hijau** (4.1.5; tetapi 3.1.1 menulis "warna program studi" → `[CEK: warna sampul]`), tidak bercorak · judul (sesingkat mungkin, memuat **nama proyek** yang dilaporkan, huruf 14 bold, mulai tepat di sembir atas) · tulisan `LAPORAN KULIAH KERJA PROFESI` (huruf 20 bold menurut 3.1.1 b; paragraf penutup 3.1.1 menyebut "yang lainnya 12" → `[CEK: ukuran]`) · nama lengkap + NPM · lambang UAJM 5×5 cm hitam · `PROGRAM STUDI [CEK: nama prodi resmi saat ini — pedoman KKP 2015 menulis "Informatika", pedoman TA rev. Juni 2015 menulis "Teknik Informatika"; keduanya diterima, asal sama di semua halaman]` · `FAKULTAS TEKNOLOGI INFORMASI` · `UNIVERSITAS ATMA JAYA` · `MAKASSAR` · bulan & tahun
2. Halaman Judul — sama, kertas putih, halaman `i` (nomor tidak dicetak)
3. Halaman Pengesahan — halaman `ii`; berlatar lambang UAJM biru langit 9×9 cm, bingkai ganda biru langit 24×16 cm; memuat `Disusun dan diajukan oleh:` · nama/NPM · `telah diperiksa dan disetujui melalui Seminar KKP` · tanggal · `dan dinyatakan telah memenuhi syarat` · `Menyetujui,` · dua pembimbing (kiri = ketua/pembimbing I, kanan = anggota/pembimbing II) — teks pedoman menulis "Pembimbing Akademik, dan Pembimbing Kampus", contoh Lampiran 2 menulis "Pembimbing Akademik" + "Pembimbing KKP" → `[CEK: label jabatan dua penanda tangan di template prodi]` · `Ketua Program Studi Informatika`. Nama bergaris bawah; judul terlalu panjang → jarak 4,5 spasi jadi 4
4. Kata Pengantar — halaman `iii`; maksud penyusunan, penjelasan ringkas, ucapan terima kasih (pembimbing lebih dulu, lalu ketua & sekretaris prodi, lalu pihak lain); **tanpa hal ilmiah**; tempat & tanggal di kanan, `Penulis` di bawahnya
5. Daftar Isi
6. Daftar Tabel
7. Daftar Gambar
8. Daftar Lampiran
9. Daftar Arti Lambang dan Singkatan *(jika ada)*

Catatan: laporan KKP **tidak memakai abstrak**. Jangan menambahkannya; itu
membedakan KKP dari skripsi.

### Bagian utama — empat bab

**BAB I PENDAHULUAN**
| Sub | Tugas | Isi | Bukti |
|---|---|---|---|
| 1.1 Latar Belakang | meyakinkan bahwa KKP ini perlu, **di tempat ini**, **di divisi ini** | (a) kenapa perlu kerja praktek; (b) di mana; (c) kenapa tempat itu dipilih; (d) divisi apa; (e) kenapa divisi itu | profil singkat instansi, fakta TIK-nya `[ISI]` |
| 1.2 Masalah | menamai kesenjangan sistem yang diamati | turunan langsung dari paragraf akhir 1.1 | observasi awal `[ISI]` |
| 1.3 Tujuan | apa yang ingin dicapai dari pelaksanaan KKP | 2–4 butir, kata kerja terukur | — |
| 1.4 Manfaat | manfaat yang diharapkan | bagi mahasiswa / instansi / prodi | — |
| 1.5 Waktu dan Tempat | kapan dan di mana | tanggal mulai–selesai, **alamat lengkap** | surat balasan instansi |
| 1.6 Jadwal Kegiatan | tahap kegiatan + **alokasi waktu per hari** | tabel tahap × waktu | rencana yang disetujui pembimbing lapangan |

Kalau instansi mewajibkan kerahasiaan (NDA, kode/data milik klien), tambahkan **1.7
Batasan dan Kerahasiaan Laporan**: apa yang tidak dicantumkan (kode sumber, data
pelanggan, nama klien) dan alasannya, serta bagaimana penggantinya (pseudokode, data
tiruan, tangkapan layar yang disamarkan). Ini bukan aturan pedoman, praktik yang
disarankan `[CEK: pembimbing]`; ia menentukan apa yang boleh masuk Bab III dan lampiran.

Titik gagal paling umum: 1.1 menjelaskan pentingnya TIK secara umum tapi tidak pernah
menjawab (c) dan (e). Pedoman menuntut keduanya secara eksplisit.

**BAB II TINJAUAN UMUM LOKASI KKP**
| Sub | Isi |
|---|---|
| 2.1 Sejarah instansi | `[ISI: dari profil resmi instansi]` |
| 2.2 Kegiatan instansi | bidang usaha/layanan |
| 2.3 Struktur organisasi | bagan + posisi divisi tempat KKP ditandai |
| 2.4 Tujuan dan fungsi instansi **yang terkait bidang kajian** | bukan seluruh tupoksi — hanya yang menyambung ke Bab III |
| 2.5 Sistem kerja | alur kerja divisi, sistem/aplikasi yang dipakai |
| 2.6 Profil klien/proyek *(jika instansi vendor/konsultan TI mengerjakan proyek untuk pihak lain)* | hanya bagian klien yang menyambung ke Bab III (siapa klien, apa proyeknya, peran instansi) `[CEK: pembimbing; perhatikan kerahasiaan §1.7]` |

Bab II sering membengkak jadi salinan company profile. Aturannya: setiap sub-bab
harus dipakai lagi di Bab III. Kalau tidak dipakai, potong.

**BAB III URAIAN TEKNIS PELAKSANAAN KKP** — inti laporan, porsi terbesar
(indikasi 40–50% halaman bagian utama — **anjuran Rangka, bukan pedoman**; pedoman
hanya menuntut "detail dan mendalam"). Memuat:
- pekerjaan-pekerjaan yang **diikuti**, diuraikan detail dan mendalam (bukan daftar);
- aturan/standar yang digunakan;
- perhitungan-perhitungan;
- keputusan *on-site* dan hal-hal khusus;
- **kesulitan yang dihadapi** — wajib, bukan opsional.

Susun per jenis pekerjaan, bukan per tanggal. Tiap jenis pekerjaan: konteks → apa yang
dikerjakan → aturan/metode → hasil → kesulitan & penanganan → bukti (tangkapan layar,
potongan kode, tabel uji) `[ISI]`.

**BAB IV PENUTUP**
- 4.1 Kesimpulan — pernyataan singkat dan tepat, dijabarkan dari **pengamatan di
  lapangan**, untuk membuktikan/membandingkan kebenaran teori yang pernah didapat.
  Setiap butir harus menempel pada tujuan di 1.3.
- 4.2 Saran — berdasar pengamatan dan **penyimpangan yang terjadi**, ditujukan kepada
  pemilik pekerjaan/proyek, konsultan perencana, pelaksana, konsultan pengawas, dan
  pembaca laporan. Nyatakan terpisah dari kesimpulan.

### Bagian akhir
- **Daftar Rujukan/Pustaka** — pola di `uajm-format.md`.
- **Lampiran** — bernomor urut 1..n, nomor halaman melanjutkan bab sebelumnya.
  Yang **mutlak ada**:
  1. Dokumentasi foto **untuk setiap jenis pekerjaan yang diikuti**, dengan mahasiswa
     KKP ikut terfoto (bukti proses berjalan);
  2. Laporan harian/mingguan (Form Aktivitas Harian);
  3. Lembar perkembangan/bimbingan pembimbing kampus.

  Yang biasanya diminta juga: surat pengantar prodi, surat balasan/penerimaan instansi,
  Form Penilaian pembimbing lapangan, daftar hadir seminar (≥5 peserta), KSM/KRS.

  Aturan turunan yang sering baru disadari di akhir: **kalau ada jenis pekerjaan di Bab
  III yang tidak punya foto, lampiran dianggap tidak lengkap.** Karena itu daftar jenis
  pekerjaan di Bab III harus difinalkan *sebelum* KKP berakhir, bukan sesudah.

  **KKP jarak jauh (remote/daring).** Pedoman 2015 tidak mengaturnya, dan syarat "mahasiswa
  ikut terfoto" tidak bisa dipenuhi apa adanya. Bukti proses yang setara: tangkapan layar
  sesi daring yang memperlihatkan mahasiswa (rapat, pair programming) + log commit/merge
  request/tiket bertanggal atas nama mahasiswa + Form Aktivitas Harian yang ditandatangani
  pembimbing lapangan. Tulis `[CEK: persetujuan prodi untuk KKP jarak jauh dan bentuk
  dokumentasinya]`. Jangan menyarankan foto rekayasa di lokasi fisik.

## Tanggal KKP vs hari ini (cek sebelum menulis lampiran)

Bandingkan tanggal KKP dengan **tanggal hari ini** sebelum memberi saran lampiran:
- **KKP belum selesai** → jadwalkan foto tiap jenis pekerjaan, Form Aktivitas Harian,
  dan Form Penilaian sebelum tanggal selesai.
- **KKP sudah selesai** → jangan menyuruh "ambil foto sebelum selesai". Katakan terus
  terang lampiran mutlak mana yang mungkin sudah tidak bisa dibuat, dan tawarkan jalan
  yang jujur: kumpulkan foto yang sudah ada per jenis pekerjaan, minta izin instansi untuk
  foto susulan di lokasi, konsultasikan kekurangan ke pembimbing kampus. Jangan
  menyarankan foto rekayasa atau log harian yang ditulis ulang seolah-olah harian.
- Hitung juga batas **satu semester** (KKP 2.2 n): kalau lewat, MK harus diinput ulang.

## Peta inti khas KKP

| Node | Isi |
|---|---|
| Should | sistem/prosedur ideal di divisi itu menurut teori & standar |
| Is | yang benar-benar berjalan selama 42+ hari kerja |
| Gap | selisihnya = "masalah" di §1.2 |
| Reader | pembimbing kampus (70%) + pembimbing lapangan (30%) |
| Core claim | "Selama KKP di [divisi], penulis mengikuti [n jenis pekerjaan] yang menunjukkan [temuan]" |
| Proof | uraian teknis + dokumentasi tiap jenis pekerjaan |
| Action | saran ke instansi + pelajaran untuk prodi |

## Cek khusus KKP (tambahan untuk `checklist.md`)

| Kode | Cek |
|---|---|
| K1 | Lingkup pekerjaan masuk salah satu dari tiga kategori sah? |
| K2 | §1.1 menjawab kenapa **tempat** itu dan kenapa **divisi** itu? |
| K3 | Setiap sub-bab Bab II dipakai kembali di Bab III? |
| K4 | Tiap jenis pekerjaan di Bab III punya rencana foto dokumentasi? |
| K5 | Setiap butir kesimpulan menjawab satu tujuan di §1.3? |
| K6 | Tiap saran menempel pada butir kesimpulan atau penyimpangan yang disebut? |
| K7 | Durasi ≥42 hari kerja dan log harian mencukupi? |
| K8 | Tidak ada abstrak (KKP tidak memakainya)? |
| K9 | Jadwal §1.6 berisi alokasi waktu **per hari**, bukan hanya per minggu? |
| K10 | Semua **data wajib identitas** ada atau ditandai `[ISI]`: nama instansi + alamat lengkap, divisi, tanggal mulai–selesai, nama pembimbing kampus & lapangan, nama proyek untuk judul? Yang kosong **tidak boleh diisi tebakan** — dan kalau yang kosong menentukan lulus/tidaknya syarat (durasi, lingkup), K7/K1 berstatus *Menunggu data*, bukan Lolos. |
| K11 | Tanggal KKP dibandingkan dengan hari ini; saran lampiran sesuai (belum selesai: jadwalkan; sudah selesai: inventaris yang ada + jalan jujur)? |
| K12 | Nama prodi, nama instansi, nama pembimbing, dan judul tertulis **sama persis** di sampul, halaman judul, pengesahan, kata pengantar, dan isi (Bab I–II)? "Informatika" dan "Teknik Informatika" sama-sama diterima, tapi harus satu bentuk di semua halaman. Nama instansi yang berbeda antarbagian (sisa template/laporan lama) = temuan berat. |
| K13 | KKP jarak jauh: bukti proses pengganti foto (tangkapan layar sesi daring + log bertanggal) ada, dan persetujuan prodi ditandai `[CEK]`? |
| K14 | Ada kerahasiaan instansi/klien → §1.7 ada, dan Bab III/lampiran tidak memuat kode/data yang dilarang? Instansi vendor → §2.6 profil klien ada bila Bab III bekerja untuk klien? |
