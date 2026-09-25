# Eval 24 — run output (UAJM KKP, missing fields) — RUN 2

Run 1 told the student to "take photos before 22 August" although today is 2026-09-25
and the KKP had ended. Fix: `uajm-kkp.md` §Tanggal KKP vs hari ini + check K11. This is run 2.

Skill files followed: SKILL.md → `uajm-kkp.md` (K1–K10) → `uajm-format.md` →
`appendices.md` → `checklist.md`. No question asked: campus and prodi are given; missing
data goes to `[ISI]`.

---

Kerangka ditulis dalam bahasa Indonesia; bilang kalau mau versi English.
Pedoman: *Pedoman KKP FTI UAJM*, 18 Januari 2015 — semua variabel format sudah dijawab
`uajm-kkp.md`/`uajm-format.md`, jadi tabel adaptasi tidak ditanyakan.

**Peringatan di awal — durasi.** 1 Juli–22 Agustus 2026 = **kurang dari 2 bulan** dan
±**37 hari kerja** (Senin–Jumat, dikurangi 17 Agustus). Pedoman meminta "minimal 2 bulan
berturut-turut dan maksimal 3 bulan **atau** minimal setara 42 hari kerja penuh". Dua-duanya
belum terpenuhi. `[CEK: hari libur/cuti bersama lain, hari Sabtu yang masuk kerja, dan
apakah prodi menerima durasi ini]`. Kalau KKP bisa diperpanjang ±1 minggu kerja, syarat 42
hari terpenuhi. K7 berstatus **Gagal** sampai ini jelas.

## 1. Peta inti

| Node | Isi |
|---|---|
| Should | layanan data di bidang aplikasi informatika dipantau lewat sistem yang terstruktur `[ISI: standar/SOP]` |
| Is | data layanan belum tersaji dalam dashboard `[ISI: kondisi sebelum]` |
| Gap | kebutuhan dashboard data layanan = masalah §1.2 |
| Reader | pembimbing kampus (70% nilai) + pembimbing lapangan (30%) |
| Core claim | Selama KKP di bidang aplikasi informatika Dinas Kominfo Makassar, penulis membangun dashboard data layanan berbasis Laravel yang `[ISI: hasil]` |
| Proof | uraian teknis per jenis pekerjaan + dokumentasi foto + tangkapan layar |
| Action | saran ke instansi + pelajaran untuk prodi |

## 2. Kerangka

**Bagian awal**
1. Sampul depan — **hijau** `[CEK: pedoman 3.1.1 menulis "warna program studi", 4.1.5 menulis "hijau"]`; judul memuat nama proyek `[ISI: nama resmi proyek/dashboard]`; `LAPORAN KULIAH KERJA PROFESI`; nama lengkap + NPM `[ISI]`; lambang UAJM; prodi/fakultas/universitas/Makassar; bulan-tahun.
2. Halaman judul (i).
3. Halaman pengesahan (ii) — `telah diperiksa dan disetujui melalui Seminar KKP`; dua pembimbing: Pak Andi (pembimbing kampus) dan `[ISI: nama pembimbing lapangan]` — label jabatan `[CEK: "Pembimbing Akademik/Kampus/KKP" di template prodi]`; Ketua Program Studi Informatika `[ISI]`.
4. Kata pengantar (iii) — terima kasih: pembimbing → ketua & sekretaris prodi → pihak instansi.
5. Daftar isi · daftar tabel · daftar gambar · daftar lampiran · daftar lambang & singkatan *(jika ada)*.
Tidak ada abstrak (KKP tidak memakai abstrak).

**BAB I PENDAHULUAN**

| Sub | Tugas | Isi | Bukti |
|---|---|---|---|
| 1.1 Latar Belakang | meyakinkan KKP perlu, di tempat dan divisi ini | a. kenapa kerja praktek perlu; b. di mana: Dinas Kominfo Makassar; c. **kenapa Kominfo** `[ISI]`; d. divisi: bidang aplikasi informatika; e. **kenapa divisi itu** `[ISI]` | profil instansi `[ISI]` |
| 1.2 Masalah | menamai kesenjangan sistem | data layanan belum tersaji dalam dashboard `[ISI: masalah yang diamati]` | observasi awal `[ISI]` |
| 1.3 Tujuan | yang ingin dicapai | a. membangun dashboard data layanan berbasis Laravel; b. `[ISI]` | — |
| 1.4 Manfaat | bagi mahasiswa / instansi / prodi | `[ISI]` | — |
| 1.5 Waktu dan Tempat | kapan dan di mana | 1 Juli–22 Agustus 2026 (lihat peringatan durasi); **alamat lengkap `[ISI]`** | surat penerimaan instansi |
| 1.6 Jadwal Kegiatan | tahap + alokasi waktu **per hari** | tabel tahap × tanggal `[ISI]` | Form Aktivitas Harian |

**BAB II TINJAUAN UMUM LOKASI KKP**
2.1 Sejarah Dinas Kominfo Makassar `[ISI: dari profil resmi]` · 2.2 Kegiatan instansi · 2.3 Struktur organisasi (bagan, bidang aplikasi informatika ditandai) · 2.4 Tujuan dan fungsi yang terkait bidang kajian (hanya yang menyambung ke dashboard) · 2.5 Sistem kerja bidang: alur data layanan, aplikasi yang sudah dipakai `[ISI]`. Setiap sub dipakai lagi di Bab III.

**BAB III URAIAN TEKNIS PELAKSANAAN KKP** (porsi terbesar; susun per jenis pekerjaan)
3.1 Analisis kebutuhan dashboard `[ISI: sumber data, pengguna]` · 3.2 Perancangan (basis data, antarmuka) · 3.3 Implementasi dengan Laravel · 3.4 Pengujian `[ISI: metode]` · 3.5 `[ISI: pekerjaan lain yang diikuti]`.
Tiap jenis: konteks → yang dikerjakan → aturan/standar → perhitungan (jika ada) → keputusan *on-site* → hasil → **kesulitan & penanganan** → bukti (tangkapan layar, potongan kode) → rencana foto.

**BAB IV PENUTUP**
4.1 Kesimpulan — satu butir per tujuan §1.3, dari pengamatan lapangan.
4.2 Saran — dari pengamatan dan penyimpangan, kepada instansi dan pembaca; terpisah dari kesimpulan.

**Bagian akhir** — Daftar Pustaka (gaya UAJM, 3+ penulis → `dkk.`).

## 2b. Kerangka lampiran

| Lampiran | Status | Dirujuk dari | Kapan dikumpulkan |
|---|---|---|---|
| 1. Dokumentasi foto **tiap jenis pekerjaan**, mahasiswa ikut terfoto | WAJIB | 3.1–3.5 | KKP **sudah selesai** (22 Agustus; hari ini 25 September) → inventaris foto yang ada per jenis pekerjaan `[ISI]` |
| 2. Laporan harian/mingguan (Form Aktivitas Harian) | WAJIB | 1.6 | seharusnya sudah terisi selama KKP `[ISI: ada/tidak]` |
| 3. Lembar perkembangan pembimbing kampus | WAJIB | Bab III | tiap bimbingan |
| 4. Surat pengantar prodi & surat penerimaan instansi | BIASANYA | 1.5 | sudah ada `[ISI]` |
| 5. Form Penilaian pembimbing lapangan | BIASANYA | — | minta sekarang bila belum `[ISI]` |
| 6. Daftar hadir seminar (≥5 mahasiswa) | BIASANYA `[CEK]` | — | saat seminar |
| 7. Tangkapan layar / potongan kode dashboard | JIKA ADA | 3.3 | selama KKP |

**KKP sudah berakhir (22 Agustus 2026).** Lampiran mutlak tidak bisa lagi dibuat "selama
KKP". Kalau ada jenis pekerjaan di Bab III tanpa foto: (a) kumpulkan semua foto yang ada
dan petakan ke jenis pekerjaan; (b) minta izin instansi untuk foto susulan di lokasi,
diberi keterangan tanggal sebenarnya; (c) sampaikan kekurangannya ke Pak Andi sebelum
seminar. Jangan membuat foto atau log harian yang direkayasa. Batas satu semester (KKP 2.2 n):
`[CEK: semester KKP diinput]`.

## 3. Hasil cek

| Butir | Status | Perbaikan |
|---|---|---|
| K1 lingkup sah | Lolos — pemrograman perangkat lunak (kategori b: "Pembuatan Web dan sebagainya") | — |
| K2 alasan tempat & divisi | Menunggu data | isi 1.1 c dan e |
| K3 Bab II dipakai di Bab III | Lolos (rencana) | — |
| K4 rencana foto tiap pekerjaan | Menunggu data | foto sebelum KKP selesai |
| K5 kesimpulan ↔ tujuan | Lolos (struktur) | — |
| K6 saran ↔ kesimpulan/penyimpangan | Lolos (struktur) | — |
| K7 durasi | **Gagal** | ±37 hari kerja < 42 dan < 2 bulan; konfirmasi prodi |
| K8 tanpa abstrak | Lolos | — |
| K9 jadwal per hari | Menunggu data | tabel 1.6 |
| K10 data identitas | Menunggu data | pembimbing lapangan, alamat, nama proyek |
| K11 tanggal vs hari ini | Lolos | KKP selesai → inventaris + jalan jujur |
| U9 nol fakta karangan | Lolos | — |

## 4. Opsi judul (sementara)

1. Pembangunan Dashboard Data Layanan Berbasis Laravel pada Bidang Aplikasi Informatika Dinas Komunikasi dan Informatika Kota Makassar
2. Dashboard Data Layanan `[ISI: nama layanan]` Berbasis Laravel di Dinas Kominfo Kota Makassar
3. Perancangan dan Implementasi Dashboard `[ISI]` pada Dinas Kominfo Kota Makassar

Singkatan "Kominfo" di judul resmi ditulis kepanjangannya `[CEK: nama resmi instansi]`.

## 5. Yang perlu kamu lengkapi

- [ISI: nama pembimbing lapangan]
- [ISI: alamat lengkap Dinas Kominfo Makassar]
- [ISI: nama resmi proyek/dashboard]
- [ISI: alasan memilih Kominfo dan bidang aplikasi informatika]
- [ISI: jadwal per hari]
- [CEK: durasi KKP ke prodi — ±37 hari kerja]
- [CEK: warna sampul; label penanda tangan pengesahan]
- [CEK: apakah ada edisi pedoman setelah 2015]

Langkah berikut: petakan foto yang ada ke tiap jenis pekerjaan Bab III, lalu bawa kerangka dan soal durasi ke Pak Andi.
