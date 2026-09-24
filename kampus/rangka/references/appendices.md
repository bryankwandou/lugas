# Lampiran — katalog dan cara merangkanya

Lampiran adalah keterangan tambahan penting yang, jika ditaruh di bagian utama, akan
mengganggu kesinambungan alur tulisan. Itu definisinya, dan itu juga ujinya: kalau
sebuah tabel dibutuhkan pembaca *saat membaca argumen*, tempatnya di bagian utama,
bukan di lampiran.

Rangka memperlakukan lampiran sebagai bagian dari kerangka, bukan tempelan akhir.
Alasannya praktis: banyak lampiran hanya bisa dikumpulkan **saat penelitian berjalan**
(foto kegiatan, tanda tangan, log harian). Kalau baru dipikirkan setelah naskah jadi,
sebagian tidak bisa lagi diadakan.

## Aturan teknis (UAJM; kebanyakan kampus Indonesia serupa)

- Nomor urut 1 sampai selesai.
- Nomor halaman lampiran **melanjutkan** nomor halaman bab sebelumnya.
- Judul tiap lampiran masuk ke **Daftar Lampiran** di bagian awal — keduanya harus sama
  persis.

## Katalog lampiran menurut jenis dokumen

Tandai tiap baris `[WAJIB]`, `[BIASANYA]`, atau `[JIKA ADA]` di kerangka, dan beri
kolom "kapan harus dikumpulkan".

### Laporan KKP / magang / PKL
| Lampiran | Status | Kapan dikumpulkan |
|---|---|---|
| Dokumentasi foto tiap jenis pekerjaan, mahasiswa ikut terfoto | WAJIB | **selama magang** — tidak bisa dibuat belakangan |
| Laporan harian/mingguan (form aktivitas) | WAJIB | harian |
| Lembar perkembangan/bimbingan pembimbing kampus | WAJIB | tiap konsultasi |
| Surat pengantar prodi | BIASANYA | sebelum berangkat |
| Surat balasan/penerimaan instansi | BIASANYA | sebelum mulai |
| Form penilaian pembimbing lapangan | BIASANYA | akhir magang |
| Daftar hadir seminar (≥5 peserta) | BIASANYA | saat seminar |
| Struktur organisasi & profil instansi | JIKA ADA | awal |
| Tangkapan layar sistem / potongan kode | JIKA ADA | selama magang |

### Proposal / usulan penelitian
Jadwal (bila tidak di bagian utama) · instrumen rancangan · surat izin pendahuluan ·
bukti ketersediaan data/dataset · rencana anggaran (bila didanai) · CV pengusul.

### Skripsi / tesis / disertasi
| Kelompok | Isi |
|---|---|
| Administratif | kartu bimbingan · berita acara & daftar hadir seminar proposal/hasil · matriks tanggapan penguji + bukti perbaikan · SK pembimbing/panitia · pernyataan tidak plagiat bermeterai · hasil cek kemiripan |
| Perizinan | surat izin penelitian · surat balasan instansi · ethical clearance (kesehatan/psikologi/penelitian pada manusia) |
| Instrumen | kuesioner · panduan wawancara · lembar observasi · informed consent · hasil uji validitas & reliabilitas · hasil uji pakar/expert judgement |
| Data | data mentah · transkrip wawancara · koding & kategorisasi (kualitatif) · print-out statistik · tabel distribusi/tabel bantu |
| Teknis (rekayasa) | kode sumber · diagram (use case, activity, class, ERD) · dokumentasi antarmuka · hasil pengujian black box/white box/UAT · hasil pengukuran kinerja · manual pengguna |
| Penutup | daftar riwayat hidup · naskah jurnal (bila terpisah) |

### Dokumen organisasi (proposal kegiatan, LPJ, SK)
Lihat `genre-organizational.md` — di sana lampiran justru sering menjadi isi utama
(susunan pengurus, RAB, absensi, kuitansi, dokumentasi).

## Cara menulis lampiran di dalam kerangka

Satu baris per lampiran, bukan judul kosong:

```
Lampiran 3. Panduan wawancara pembimbing lapangan  [WAJIB]
  Tugas   : membuktikan data kualitatif Bab IV berasal dari instrumen yang tetap
  Isi     : 12 pertanyaan, 4 tema  [ISI: daftar pertanyaan]
  Dirujuk : §3.6 (metode pengumpulan data), §4.2 (hasil wawancara)
  Ambil   : sebelum turun lapangan
```

Baris `Dirujuk` adalah yang terpenting. **Lampiran yang tidak pernah dirujuk dari
bagian utama adalah orphan** dan melanggar aturan No orphans di SKILL.md — entah
rujukannya yang kurang, atau lampirannya yang tidak perlu.

## Cek lampiran

| Kode | Cek |
|---|---|
| L1 | Tiap lampiran dirujuk minimal sekali dari bagian utama? |
| L2 | Daftar Lampiran sama persis dengan judul lampiran? |
| L3 | Lampiran `[WAJIB]` untuk jenis dokumen ini semuanya muncul? |
| L4 | Lampiran yang hanya bisa diambil saat kegiatan berlangsung sudah ditandai waktunya? |
| L5 | Tidak ada isi yang dibuang ke lampiran padahal pembaca membutuhkannya saat membaca argumen? |
| L6 | Data pribadi responden disamarkan bila perlu (etika + perlindungan data)? |
