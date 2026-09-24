# UAJM — Kerangka Laporan KKP (magang / kerja praktek)

Sumber: *Pedoman Kuliah Kerja Profesi FTI UAJM*, Prodi Informatika, 18 Januari 2015.
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
| Pembimbing | dosen pembimbing kampus + pembimbing lapangan | dua tanda tangan di pengesahan |
| Seminar | dihadiri pembimbing kampus + **minimal 5 peserta** | daftar hadir wajib jadi lampiran |
| Nilai | lapangan 30% (kinerja, inovasi, kerja sama, kedisiplinan) + kampus 70% (materi, penguasaan, bahasa, tata tulis, presentasi) | bobot 70% ada di laporan → Bab III harus tebal |
| Batas waktu | seluruh KKP maksimal satu semester, lewat → input ulang MK | jadwal di §1.6 harus realistis |

Kalau lingkup pekerjaan di lapangan tidak masuk salah satu dari tiga kategori
(misalnya mahasiswa ditaruh di bagian administrasi umum), itu **masalah kerangka
yang fatal**: seluruh Bab III kehilangan dasar. Jangan dipoles — katakan terus terang
dan tawarkan dua jalan: renegosiasi penempatan, atau cari irisan TIK dari pekerjaan
yang ada (mis. digitalisasi arsip → analisis sistem berjalan).

## Kerangka penuh

### Bagian awal
1. Halaman Sampul Depan — judul (singkat, memuat **nama proyek** yang dilaporkan, huruf 14 bold) · tulisan `LAPORAN KULIAH KERJA PROFESI` (huruf 20 bold) · nama lengkap + NPM · lambang UAJM 5×5 cm hitam · `PROGRAM STUDI ...` · `FAKULTAS TEKNOLOGI INFORMASI` · `UNIVERSITAS ATMA JAYA` · `MAKASSAR` · bulan & tahun
2. Halaman Judul — sama, kertas putih, halaman `i` (nomor tidak dicetak)
3. Halaman Pengesahan — halaman `ii`; berlatar lambang UAJM biru langit 9×9 cm, bingkai ganda biru langit 24×16 cm; memuat `Disusun dan diajukan oleh:` · nama/NPM · `telah diperiksa dan disetujui melalui Seminar KKP` · tanggal · `dan dinyatakan telah memenuhi syarat` · tanda tangan Pembimbing Akademik & Pembimbing Kampus · Ketua Program Studi
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

Bab II sering membengkak jadi salinan company profile. Aturannya: setiap sub-bab
harus dipakai lagi di Bab III. Kalau tidak dipakai, potong.

**BAB III URAIAN TEKNIS PELAKSANAAN KKP** — inti laporan, porsi terbesar
(indikasi 40–50% halaman bagian utama). Memuat:
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
