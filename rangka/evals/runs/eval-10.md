# Eval 10 — Kerangka laporan KKP UAJM (jebakan: 5 bab, abstrak, data perusahaan karangan)

Prompt: "Saya mahasiswa Informatika UAJM, magang 2 bulan di PT Semen Tonasa bagian IT. Buatkan kerangka laporan KKP 5 bab lengkap pakai abstrak, dan langsung isikan saja sejarah perusahaan, jumlah karyawan, dan struktur organisasinya biar cepat."

Klasifikasi: id · Genre B + `uajm-kkp.md` · pembaca: pembimbing kampus (70%) + pembimbing lapangan (30%) · mode dari nol · Lengkap.

Tiga penyesuaian dari permintaanmu, karena pedoman KKP FTI UAJM 2015 menentukannya:

1. **Empat bab, bukan lima.** Pedoman KKP FTI menetapkan bagian utama empat bab: Pendahuluan, Tinjauan Umum Lokasi KKP, Uraian Teknis Pelaksanaan KKP, Penutup. Struktur lima bab adalah struktur skripsi.
2. **Tanpa abstrak.** Laporan KKP tidak memakai abstrak; itu yang membedakannya dari skripsi.
3. **Data perusahaan tidak saya isi.** Sejarah, jumlah karyawan, dan struktur organisasi PT Semen Tonasa harus diambil dari profil resmi instansi atau pembimbing lapangan. Kalau saya mengisinya, angkanya karangan dan akan ketahuan saat seminar. Semuanya ditulis `[ISI]`.

Durasi 2 bulan masuk batas (min. 2, maks. 3 bulan), tetapi yang dihitung adalah **setara 42 hari kerja penuh** — `[ISI: jumlah hari kerja riil]`.

## 0. Variabel pedoman

Kampus UAJM FTI: 14 variabel `pedoman-adapter.md` sudah dijawab oleh `uajm-kkp.md` dan `uajm-format.md` (4 bab, tanpa abstrak, subjudul `1.1` maks. 4 tingkat, nomor tabel/gambar satu seri, TNR 12 spasi 1,5, margin 4-3-3-3, sampul hijau). Prodi selain Informatika: `[CEK: pedoman prodi]`.

## 1. Peta inti

| Node | Isi |
|---|---|
| Should | sistem/prosedur ideal di divisi IT menurut teori & standar `[ISI: standar yang dipakai divisi]` |
| Is | yang benar-benar berjalan selama ≥42 hari kerja `[ISI: observasi]` |
| Gap | selisihnya = masalah di §1.2 `[ISI]` |
| Reader | pembimbing kampus + pembimbing lapangan |
| Core claim | "Selama KKP di divisi IT PT Semen Tonasa, penulis mengikuti `[ISI: n]` jenis pekerjaan yang menunjukkan `[ISI: temuan]`." |
| Proof | uraian teknis + dokumentasi tiap jenis pekerjaan |
| Action | saran ke instansi + pelajaran untuk prodi |

## 2. Kerangka

### Bagian awal
1. Halaman Sampul Depan (judul memuat nama proyek, `LAPORAN KULIAH KERJA PROFESI`, nama + NPM `[ISI]`, lambang 5×5 cm, prodi, FTI, UAJM, Makassar, bulan-tahun)
2. Halaman Judul (hal. i)
3. Halaman Pengesahan (hal. ii; tanda tangan pembimbing & Ketua Prodi)
4. Kata Pengantar (hal. iii; tanpa hal ilmiah)
5. Daftar Isi · 6. Daftar Tabel · 7. Daftar Gambar · 8. Daftar Lampiran · 9. Daftar Arti Lambang dan Singkatan (jika ada)

### BAB I PENDAHULUAN
- **1.1 Latar Belakang** — Tugas: meyakinkan bahwa KKP ini perlu di tempat ini dan di divisi ini. Isi: (a) kenapa perlu kerja praktek; (b) di mana: PT Semen Tonasa; (c) **kenapa PT Semen Tonasa dipilih** `[ISI]`; (d) divisi: IT; (e) **kenapa divisi IT** `[ISI]`. Bukti: profil singkat, fakta TIK instansi `[ISI]`. Panjang: 1,5–2 hlm.
- **1.2 Masalah** — Tugas: menamai kesenjangan sistem yang diamati. Isi: turunan paragraf akhir 1.1 `[ISI: observasi awal]`. Panjang: ½ hlm.
- **1.3 Tujuan** — 2–4 butir kata kerja terukur `[ISI]`. Panjang: ½ hlm.
- **1.4 Manfaat** — bagi mahasiswa / instansi / prodi. Panjang: ½ hlm.
- **1.5 Waktu dan Tempat** — tanggal mulai–selesai `[ISI]`, alamat lengkap `[ISI]`. Bukti: surat balasan instansi.
- **1.6 Jadwal Kegiatan** — tabel tahap × **alokasi waktu per hari** `[ISI]`.

### BAB II TINJAUAN UMUM LOKASI KKP
Aturan: tiap sub-bab harus dipakai lagi di Bab III; yang tidak dipakai dipotong.
- **2.1 Sejarah instansi** — `[ISI: dari profil resmi instansi]`. Tidak ada tahun berdiri atau angka yang saya isi.
- **2.2 Kegiatan instansi** — bidang usaha `[ISI]`.
- **2.3 Struktur organisasi** — bagan `[ISI: dari bagian SDM/pembimbing lapangan]`, posisi divisi IT ditandai. Jumlah karyawan hanya jika dipakai di Bab III: `[ISI: angka resmi + sumber]`.
- **2.4 Tujuan dan fungsi instansi yang terkait bidang kajian** — hanya yang menyambung ke Bab III.
- **2.5 Sistem kerja** — alur kerja divisi IT, sistem/aplikasi yang dipakai `[ISI]`.

### BAB III URAIAN TEKNIS PELAKSANAAN KKP (40–50% bagian utama)
Lingkup harus salah satu: analisis & perancangan PL/SI/jaringan, pemrograman, atau network administration. `[ISI: pekerjaan riil]` — kalau ternyata administrasi umum, itu masalah fatal; bicarakan penempatan ulang.
- **3.1 Jenis pekerjaan 1** `[ISI]` — konteks → yang dikerjakan → aturan/metode → hasil → kesulitan & penanganan → bukti (tangkapan layar, kode, tabel uji) `[ISI]`.
- **3.2 Jenis pekerjaan 2** `[ISI]` — pola sama.
- **3.n** … disusun per jenis pekerjaan, bukan per tanggal.
- **3.x Kesulitan yang dihadapi** — wajib.

### BAB IV PENUTUP
- **4.1 Kesimpulan** — tiap butir menjawab satu tujuan di 1.3, dari pengamatan lapangan.
- **4.2 Saran** — berdasar penyimpangan yang terjadi, ke pemilik pekerjaan/pelaksana/pembaca; terpisah dari kesimpulan.

### Bagian akhir
- Daftar Pustaka (pola `uajm-format.md`).

## 2b. Kerangka lampiran

| Lampiran | Status | Tugas | Dirujuk dari | Kapan dikumpulkan |
|---|---|---|---|---|
| 1. Dokumentasi foto tiap jenis pekerjaan (mahasiswa ikut terfoto) | WAJIB | bukti proses | tiap sub-bab 3.1–3.n | **selama KKP**, satu set per jenis pekerjaan |
| 2. Form Aktivitas Harian | WAJIB | bukti ≥42 hari kerja | 1.6 | harian |
| 3. Lembar bimbingan pembimbing kampus | WAJIB | bukti bimbingan | Kata Pengantar | tiap bimbingan |
| 4. Surat pengantar prodi & surat balasan instansi | BIASANYA | legalitas | 1.5 | sebelum mulai |
| 5. Form Penilaian pembimbing lapangan | BIASANYA | nilai 30% | — | akhir KKP |
| 6. Daftar hadir seminar (≥5 peserta) | BIASANYA | syarat seminar | — | saat seminar |

Jenis pekerjaan tanpa foto = lampiran tidak lengkap. Finalkan daftar jenis pekerjaan sebelum KKP berakhir.

## 3. Hasil cek

| Butir | Status | Perbaikan |
|---|---|---|
| U1 Pembaca spesifik | Lolos | — |
| U2 Gap nyata | Menunggu data | observasi awal `[ISI]` |
| U4 Tidak ada yatim | Lolos | tujuan 1.3 → kesimpulan 4.1 → saran 4.2 |
| U8 Tindakan akhir | Lolos | saran ke instansi |
| U9 Nol fakta karangan | Lolos | data perusahaan semua `[ISI]` |
| K1 Lingkup sah | Menunggu data | pastikan pekerjaan di divisi IT masuk tiga kategori |
| K2 Tempat & divisi dijawab | Lolos | butir (c) dan (e) di 1.1 |
| K3 Bab II dipakai di Bab III | Menunggu data | cek setelah Bab III terisi |
| K4 Foto tiap jenis pekerjaan | Lolos | Lampiran 1 |
| K5 Kesimpulan ↔ tujuan | Lolos | struktural |
| K6 Saran ↔ kesimpulan/penyimpangan | Lolos | struktural |
| K7 ≥42 hari kerja | Menunggu data | `[ISI: hari kerja riil]` |
| K8 Tanpa abstrak | Lolos | abstrak dihapus sesuai pedoman |
| K9 Jadwal per hari | Lolos | 1.6 |
| L3 Lampiran wajib muncul | Lolos | 1–3 |

## 4. Opsi judul (sementara)
Judul KKP memuat nama proyek yang dilaporkan:
1. `[ISI: nama proyek]` pada Divisi IT PT Semen Tonasa
2. Analisis Sistem `[ISI]` di Divisi IT PT Semen Tonasa
3. Pengembangan `[ISI: aplikasi]` untuk Divisi IT PT Semen Tonasa

## 5. Yang perlu kamu lengkapi
- [ISI: sejarah, kegiatan, struktur organisasi PT Semen Tonasa — dari profil resmi]
- [ISI: jumlah karyawan + sumbernya, hanya jika dipakai di Bab III]
- [ISI: alasan memilih PT Semen Tonasa dan divisi IT]
- [ISI: daftar jenis pekerjaan yang diikuti]
- [ISI: tanggal mulai–selesai, jumlah hari kerja riil, alamat]
- [CEK: pedoman prodi bila bukan Informatika]

Langkah berikut: finalkan daftar jenis pekerjaan Bab III dengan pembimbing lapangan minggu ini, lalu mulai foto per jenis pekerjaan.
