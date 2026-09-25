# Contoh audit — laporan KKP fiktif

> **FIKTIF.** Mahasiswa, NPM, instansi, dan isi di bawah ini karangan untuk contoh.
> Tidak ada orang, perusahaan, atau laporan nyata di baliknya. Pelanggarannya
> disengaja, supaya bentuk audit `references/audit-template.md` terlihat utuh.

Pedoman yang dipakai: *Pedoman Kuliah Kerja Profesi*, Prodi Informatika FTI UAJM,
18 Januari 2015. Semua nomor klausul dicocokkan dengan `references/uajm-fti.md` dan
dengan teks PDF aslinya.

---

## 1. Draf yang diaudit

**Keterangan dari mahasiswa (fiktif):** sudah lulus 124 sks, KKP 46 hari kerja di
CV Contoh Data Nusantara, Makassar. Seminar belum. Setelan Word: margin kiri 3 cm,
atas/bawah/kanan 3 cm, Times New Roman 12, spasi 2. Rencana sampul: **biru tua**,
tulisan putih.

**Susunan yang diserahkan:**

```
Sampul · Halaman judul · Halaman pengesahan · Kata pengantar · Daftar isi
· Daftar tabel · Daftar gambar
BAB I    PENDAHULUAN
BAB II   URAIAN TEKNIS PELAKSANAAN KKP
BAB III  PENUTUP
DAFTAR PUSTAKA
LAMPIRAN 1  Laporan harian
LAMPIRAN 2  Lembar perkembangan pembimbing kampus
```

**Petikan isi:**

> **BAB I PENDAHULUAN** — 1.1 Latar Belakang
> Pada KKP ini saya ditempatkan di divisi TI selama 5 (lima) hari per minggu.
> Menurut Roger S. Pressman (2010), rekayasa perangkat lunak adalah …
>
> Sehingga dibutuhkan sistem inventaris berbasis web.

> **BAB II** — 2.3.1.2.1 Modul Stok Barang
> Kegiatan yang dikerjakan:
> • membuat tabel database
> • membuat halaman login
> • menguji form input
>
> *(tabel)* — di bawahnya: **Tabel 2.1. Daftar Tabel Database (dalam KB).**

> **BAB III PENUTUP**
> Sistem sudah berjalan baik dan sebaiknya dikembangkan lagi ke versi mobile.

> **DAFTAR PUSTAKA**
> Pressman, R. S. (2010). *Software engineering: A practitioner's approach* (7th ed.). McGraw-Hill.
> Dr. Sommerville, I. (2011). *Software engineering* (9th ed.). Addison-Wesley.

*(Sommerville tidak dirujuk di mana pun dalam naskah.)*

---

## 2. Hasil audit

## Hasil audit — Laporan KKP, UAJM FTI Prodi Informatika, pedoman edisi 18 Januari 2015

**Gerbang akademik:** 124 sks ≥ 122 sks (KKP 2.1); 46 hari kerja ≥ 42 hari kerja
(KKP 2.2h). Lolos. Seminar dengan ≥5 peserta (KKP 2.2k) belum — laporan boleh
disusun, belum boleh dicetak final.

### Keras
| Bagian | Aturan | Klausul | Temuan | Perbaikan |
|---|---|---|---|---|
| Bagian utama | empat bab: Pendahuluan · Tinjauan Umum Lokasi KKP · Uraian Teknis Pelaksanaan KKP · Penutup | KKP 3.2, 3.2.2 | bab Tinjauan Umum Lokasi KKP tidak ada | tambah bab berisi sejarah, kegiatan, struktur, tujuan dan fungsi instansi terkait bidang kajian, sistem kerja `[ISI: data instansi]` |
| Lampiran | foto tiap jenis pekerjaan dengan mahasiswa terfoto di dalamnya mutlak ada | KKP 3.3.2 | lampiran foto tidak ada | tambah lampiran dokumentasi foto |
| Penutup | kesimpulan dan saran dinyatakan terpisah | KKP 3.2.4 | satu paragraf campuran | pisah jadi subbab Kesimpulan dan Saran |
| Penutup — saran | saran ditujukan kepada pemilik pekerjaan/proyek, pelaksana, pembaca laporan, dst. | KKP 3.2.4b | saran tanpa alamat tujuan | sebut kepada siapa tiap saran ditujukan (perbaikan tingkat rangka, bukan tipografi) |
| Sembir | kiri 4 cm; atas, bawah, kanan 3 cm | KKP 4.1.2 | kiri 3 cm | setel margin kiri 4 cm |
| Rincian | tanda hubung, pagar, bintang, bullet tidak dibenarkan | KKP 4.2.5 | bullet `•` di Bab II | ganti dengan huruf abjad `a.` `b.` `c.` (urutan tidak tetap, KKP 4.2.4d); rincian kata pendek boleh ditulis menerus dalam satu baris (KKP 4.2.5) |
| Subjudul | sub-anak-subjudul tingkat terakhir yang diperbolehkan (4 tingkat) | KKP 4.2.3, 4.3.5 | `2.3.1.2.1` = 5 tingkat | naikkan jadi paling dalam `2.3.1.2`, atau jadikan rincian |
| Bahasa | titik pandang orang ketiga, kalimat pasif; tanpa *saya* | KKP 4.5.1c | "saya ditempatkan" di Bab I | ubah ke kalimat pasif tanpa kata ganti orang pertama |
| Daftar pustaka | hanya sumber yang benar-benar dirujuk dalam naskah | KKP 3.3.1 | Sommerville tercantum, tidak pernah dirujuk | rujuk dalam uraian atau hapus dari daftar |

### Lunak
| Bagian | Aturan | Klausul | Temuan | Perbaikan |
|---|---|---|---|---|
| Spasi | teks 1,5; spasi tunggal untuk abstrak, kutipan langsung, judul, daftar-daftar, entri pustaka >1 baris | KKP 4.1.6 | spasi 2 | setel spasi 1,5 |
| Tabel — letak judul | judul di atas tabel, rapat sembir kiri | KKP 4.4.1 | judul di bawah tabel | pindah ke atas tabel |
| Tabel — judul | kapital hanya huruf pertama kata pertama, tanpa titik akhir, satuan tidak boleh dalam judul | KKP 4.4.1 | kapital tiap kata, titik akhir, "(dalam KB)" | `Tabel n. Daftar tabel database`; satuan KB pindah ke kepala kolom |
| Tabel — nomor | angka Arab, berurut dari awal sampai akhir | KKP 4.3.2 | `Tabel 2.1` (per bab) | nomor satu seri: `Tabel 1`, `Tabel 2`, … |
| Awal paragraf | kata sambung tidak boleh menjadi awal paragraf | KKP 4.2.2 | paragraf dibuka "Sehingga" | gabung ke kalimat sebelumnya atau susun ulang |
| Bilangan | `5 (lima)` dinyatakan salah | KKP 4.2.1 | "5 (lima) hari" | tulis "5 hari" |
| Rujukan dalam uraian | sebut nama akhir saja | KKP 4.6.1 | "Roger S. Pressman (2010)" | "Menurut Pressman (2010)" |
| Daftar pustaka — pola | nama akhir, inisial bertitik, tahun, judul miring, penerbit, kota; bukan APA | KKP 4.6.2, 3.3.1 | pola APA: tahun dalam kurung, edisi dalam kurung, tanpa kota | ikuti pola buku teks UAJM: `Pressman, R. S., 2010. Software Engineering: A Practitioner's Approach, Seventh Edition, McGraw-Hill, [CEK: kota terbit].` |
| Daftar pustaka — gelar | gelar akademis atau pangkat tidak dicantumkan | KKP 4.6.2e | "Dr. Sommerville" | hapus "Dr." |

### Perlu dicek di luar file
- [CEK: warna sampul — laporan KKP **hijau** dengan tulisan tinta hitam (KKP 4.1.5). Rencana "biru tua, tulisan putih" melanggar dua-duanya. Catatan: KKP 3.1.1 menyebut warna program studi; 4.1.5 lebih spesifik dan dipakai.]
- [CEK: bahan sampul — kertas buffalo atau sejenis, diperkuat karton, dilapisi plastik (KKP 4.1.5)]
- [CEK: cetak satu muka, HVS 80 gram A4 putih, printer bukan dot matrix (KKP 4.1.4)]
- [CEK: seminar dihadiri dosen pembimbing kampus dan minimal 5 peserta (KKP 2.2k)]
- [CEK: hardcover 3 eksemplar setelah seminar (KKP 2.2l)]

### Tidak diatur pedoman
- Panjang tiap bab — pedoman diam. Praktik lazim: Uraian Teknis menjadi bab terpanjang; ini saran, bukan aturan.
- Jumlah minimum rujukan — pedoman diam; KKP 3.3.1 hanya meminta sumber yang benar-benar dirujuk.

Pedoman KKP Prodi Informatika FTI UAJM, 18 Januari 2015. Temuan: 9 keras, 9 lunak.
Warna dan bahan sampul, kertas, seminar, dan jilid tidak bisa diperiksa dari file.
