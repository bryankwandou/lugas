# Checklist

Jalankan bagian U (universal) untuk semua dokumen, lalu bagian genre dari file genre
yang dipakai (A7, B3, C3, D3, E6, F5, G1/G11–G14 + OP/LP/SK). Laporkan sebagai tabel: Butir | Status | Perbaikan. Jangan menulis "semua lolos" tanpa tabel.

Berkas rujukan lain membawa cek tambahan yang dijalankan **bersama** cek genre, bila
berkas itu dipakai:

| Berkas | Kode | Kapan dijalankan |
|---|---|---|
| `uajm-kkp.md` | K1–K14 | laporan KKP/magang UAJM |
| `uajm-usulan-ta.md` | P1–P12 | usulan TA / proposal / RKD |
| `uajm-skripsi.md` | S1–S14 | skripsi/TA |
| `genre-thesis.md` | T1–T10 | tesis & disertasi |
| `genre-organizational.md` | G1, G11–G14 | semua dokumen organisasi |
| `org-proposal-kegiatan.md` | OP1–OP6 | proposal kegiatan |
| `org-lpj.md` | LP1–LP9 | LPJ |
| `org-sk.md` | SK1–SK8 | SK, surat penugasan, surat pengantar SK |
| `full-outlines.md` | F1–F6 | kerangka penuh skripsi/tesis/disertasi |
| `appendices.md` | L1–L6 | setiap dokumen yang punya lampiran |
| `summarize-to-outline.md` | R1–R10 | mode rangkum-dari-berkas |
| `pedoman-adapter.md` | A1–A8 | setiap dokumen akademik |
| `languages.md` | B1–B5 | keluaran bukan bahasa Indonesia, atau campuran |

Hanya tiga status yang boleh dipakai:
- **Lolos** — terpenuhi.
- **Menunggu data** — struktur benar, tapi butuh `[ISI]` dari pengguna. Judul boleh diberikan dengan label *sementara*.
- **Gagal** — struktur salah. Perbaiki kerangka dulu.

U12 dicek setelah judul ditulis (Step 4), bukan sebelumnya.

## U. Universal

| # | Butir | Cara cek |
|---|---|---|
| U1 | Pembaca spesifik | Bisa disebut dengan satu frasa yang bukan "semua orang/umum" |
| U2 | Gap nyata | Should dan Is berbeda, dan Is punya dasar (data, observasi, keluhan) atau `[ISI]` |
| U3 | Core claim satu kalimat | Orang di luar bidang paham kalimatnya |
| U4 | Tidak ada yatim | Setiap pertanyaan/janji/klaim → ada bagian yang menjawab → ada bukti atau `[ISI]` |
| U5 | Tidak ada bagian tanpa tugas | Setiap bagian punya baris "Tugas" yang melayani U3 atau U4 |
| U6 | Urutan sesuai kebutuhan pembaca | Baca judul bagian saja dari atas ke bawah: alurnya masuk akal tanpa isi |
| U7 | Tidak tumpang tindih | Dua bagian tidak menjawab hal yang sama (prinsip MECE: saling lepas, lengkap bersama) |
| U8 | Tindakan akhir jelas | Pembaca tahu apa yang harus dilakukan atau disimpulkan |
| U9 | Nol fakta karangan | Setiap angka, nama, kutipan, sumber berasal dari pengguna, `sources.md`, atau ditandai `[ISI]`/`[CEK]` |
| U10 | Aturan eksternal ditandai | Pedoman kampus, format klien, regulasi → `[CEK]` bila belum dipastikan |
| U11 | Panjang realistis | Jumlah petunjuk panjang tiap bagian sesuai batas total |
| U12 | Judul/headline dari core claim | Ditulis terakhir, tidak menjanjikan lebih dari isi |
| U13 | Konsisten di dalam satu naskah | Hitungan (jumlah fase, tahap, hipotesis, responden) dan nama diri (instansi, prodi, komponen, pembimbing) sama di semua bagian: sampul, pengesahan, abstrak, isi, bagan, jadwal. Beda = `[KONFLIK]` |
| U14 | Daftar sinkron dengan isi | Daftar Isi/Tabel/Gambar/Lampiran cocok nomor dan judulnya dengan isi; bukan semua "Tabel 1" |
| U15 | Isi sesuai judul bagian | Untuk bagian wajib, baca isinya, bukan hanya judulnya (mis. "Analisa Kepekaan" yang isinya TELOS = Gagal) |

## Versi cepat

Untuk mode Cepat: U1, U2, U4, U8, U9, U13, **ditambah semua butir cek genre**. Butir genre tidak pernah dilewati.

## Kegagalan yang paling sering dan perbaikannya

| Gejala | Penyebab | Perbaikan |
|---|---|---|
| Latar belakang panjang tapi rumusan masalah tidak nyambung | Gap tidak dirumuskan | Tulis ulang Step 1, lalu turunkan rumusan dari Gap |
| Landing page penuh fitur, tidak ada yang membeli | Tidak ada janji tunggal | Kunci pembaca-tindakan-janji di C, buang fitur yang tidak mendukung janji |
| Laporan dibaca tapi tidak ada keputusan | Kesimpulan di akhir | Pindahkan jawaban ke ringkasan (SCQA) |
| Dosen: "judulnya terlalu luas" | Judul dibuat sebelum outline | Kembali ke A1, persempit objek/lokasi/variabel |
| README tidak bisa diikuti | Tutorial dan reference dicampur | Pisahkan jenis Diátaxis |
| Video ditinggalkan di detik awal | Hook lambat atau janji tidak jelas | Pindahkan hasil/masalah ke 3 detik pertama |
| Bab 4 tidak menjawab rumusan | Yatim | Buat tabel rumusan → data → analisis → subbab |
| Lampiran wajib tidak bisa diadakan lagi (foto, tanda tangan, log) | Lampiran baru dipikirkan setelah kegiatan selesai | Rangka lampiran di awal, beri kolom "kapan dikumpulkan" (`appendices.md`) |
| LPJ dikembalikan bendahara | Pos keuangan tidak sama dengan RAB proposal | Sejajarkan daftar pos, hitung ulang, jelaskan tiap selisih (LP1–LP4, `org-lpj.md`) |
| SK ditolak sekretariat | Alasan masuk ke "Mengingat", dasar hukum masuk ke "Menimbang" | Tukar sesuai pola di `org-sk.md` (SK1) |
| Proposal disertasi disebut "hanya studi kasus" | Kebaruan berupa konteks baru saja | Naikkan ke bentuk kebaruan 2–4 (`genre-thesis.md` T3) |
| Template kampus berbeda dengan kerangka yang diberikan | Variabel pedoman tidak diisi di awal | Jalankan 14 variabel `pedoman-adapter.md` sebelum menyusun |
