# Kampus Indonesia selain UAJM FTI — dan jenjang tesis/disertasi

**Status kepercayaan: sedang.** File ini untuk kampus yang **belum** punya file
sendiri. Sebelas kampus sudah dikodekan dari pedoman primernya (lihat tabel Step 0 di
`SKILL.md`); untuk mereka, pakai file kampusnya, bukan file ini. Yang ada di file ini adalah (1) sumbu-sumbu tempat
pedoman antar-kampus benar-benar berbeda, (2) pertanyaan yang harus ditanyakan,
dan (3) konvensi yang umum tapi **bukan aturan**. Tidak ada di file ini yang boleh
dikutip sebagai "aturan kampus X".

Kalimat pembuka yang wajib diucapkan sekali, sebelum apa pun:

> Saya belum punya pedoman <kampus/prodi>. Yang bisa saya lakukan sekarang: menyebut
> hal-hal yang biasanya diatur dan menandai mana yang wajib dicek. Kalau file
> pedomannya dikirim, saya ikut file itu dan semua tanda `[CEK]` hilang.

## 1. Empat belas sumbu perbedaan

Inilah yang berbeda antar-kampus. Isi tabelnya dari pedoman yang dikirim; yang belum
terisi tetap `[CEK]`. Tunjukkan tabel yang sudah terisi ke pengguna **sebelum**
menghasilkan apa pun.

| # | Variabel | Rentang yang benar-benar ditemui di Indonesia |
|---|---|---|
| 1 | Margin | kiri 4 cm / kanan 3 cm / atas 3 / bawah 3 adalah yang paling umum; sebagian kampus memakai 4-3-4-3 atau 3-3-3-3 |
| 2 | Huruf | Times New Roman 12 dominan; sebagian prodi desain/komputer mengizinkan Arial 11 |
| 3 | Spasi | 1,5 dominan; sebagian memakai 2 untuk teks utama |
| 4 | Warna sampul | ditentukan fakultas atau prodi — **selalu** `[CEK]` |
| 5 | Kedalaman heading | 3 atau 4 tingkat; sebagian melarang penomoran desimal dan memakai huruf |
| 6 | Penanda rincian | sebagian melarang bullet (seperti UAJM), sebagian mengizinkan |
| 7 | Penomoran tabel/gambar | satu seri sepanjang naskah **atau** per bab (`Tabel 2.1`) — ini beda tajam |
| 8 | Gaya rujukan | nama-tahun gaya kampus · APA · IEEE · Harvard · Vancouver; makin banyak yang mewajibkan Mendeley/Zotero |
| 9 | Abstrak | 150 / 200–250 / 300 kata; satu bahasa atau dua bahasa |
| 10 | Jumlah bab | lima bab dominan; sebagian prodi rekayasa memakai empat atau enam |
| 11 | Bagian awal wajib | pernyataan orisinalitas, persetujuan publikasi, dan lembar bebas plagiasi makin umum |
| 12 | Syarat SKS & IPK | berbeda tiap prodi |
| 13 | Ambang similarity | sebagian kampus menetapkan angka (mis. 25 %) — jangan pernah menebak angkanya |
| 14 | Luaran wajib | artikel jurnal, HKI, atau seminar nasional; ada/tidaknya berbeda |

Enam pertanyaan yang cukup untuk mengisi sebagian besar tabel di atas, kalau pedoman
tidak ada: kampus dan prodi · jenjang · jenis dokumen · gaya rujukan yang diminta ·
jumlah bab · adakah lembar orisinalitas.

## 2. Yang benar-benar berlaku nasional

Pendek, karena memang sedikit. Jangan tambahkan tanpa membaca sumbernya.

- **Ejaan.** Ragam baku mengikuti pedoman ejaan bahasa Indonesia yang berlaku, dan
  istilah mengikuti pedoman pembentukan istilah. Hampir semua pedoman kampus
  merujuk ke sana alih-alih menulis ulang aturannya.
- **Plagiarisme.** Ada regulasi nasional tentang pencegahan dan penanggulangan
  plagiat di perguruan tinggi, dan tiap kampus menurunkannya jadi lembar pernyataan
  dan pemeriksaan kemiripan. **Rujuk keberadaannya, bukan nomor pasalnya**, kecuali
  pengguna mengirim regulasinya → `[CEK: aturan plagiasi kampus]`.
- **Unggah karya ilmiah.** Banyak kampus mewajibkan unggah repositori dan/atau
  artikel. Wajib/tidaknya adalah urusan kampus → `[CEK]`.

Apa pun angka (ambang similarity, jumlah halaman minimum, jumlah rujukan minimum)
yang tidak tertulis di pedoman yang dibaca: **jangan disebut**. Angka yang salah
merugikan lebih besar daripada mengatakan tidak tahu.

## 3. Tesis (S2) dan disertasi (S3)

Yang berubah dari skripsi bukan tipografinya, melainkan tuntutan isinya. Tipografi
umumnya mewarisi pedoman pascasarjana kampus → `[CEK: pedoman pascasarjana]`.

| Aspek | Skripsi | Tesis | Disertasi |
|---|---|---|---|
| Tuntutan inti | mampu menerapkan metode dengan benar | kebaruan pada tingkat penerapan atau pengujian | **kebaruan yang diklaim eksplisit** dan dipertahankan |
| Posisi teori | memakai teori | menguji atau memperluas teori | menyumbang pada teori |
| Tinjauan pustaka | memetakan yang sudah ada | memetakan + menunjukkan celah | memetakan + celah + posisi penulis terhadap perdebatan |
| Bab kebaruan | tidak ada | kadang bagian dari Bab I | biasanya bab/subbab tersendiri: *state of the art*, orisinalitas, kontribusi |
| Rumusan masalah | boleh satu | biasanya 2–3 yang saling menopang | berlapis, dengan pertanyaan induk |
| Publikasi | kadang | umumnya wajib, jurnal nasional terakreditasi | umumnya wajib, jurnal internasional bereputasi |
| Ujian | sidang | seminar proposal, hasil, tesis | kualifikasi, proposal, hasil, tertutup, terbuka |
| Penguji luar | jarang | kadang | umumnya wajib |

Konsekuensi praktis untuk audit: pada tesis dan disertasi, **klaim kebaruan yang
tidak ditopang tinjauan pustaka adalah temuan keras**, setara dengan margin salah
pada skripsi. Kalau pedoman kampus menyediakan lembar/bab orisinalitas, periksa
apakah isinya benar-benar menyebut apa yang baru, bukan sekadar menyatakan bukan
plagiat.

Jumlah dan nama tahapan ujian berbeda tiap program → `[CEK: tahapan ujian program]`.

## 4. Cara mengodekan kampus baru

Kalau pengguna mengirim pedoman lengkap dan meminta ini dipakai seterusnya, buat
`references/<kode>.md` dengan bentuk yang sama dengan `uajm-fti.md`:

1. Tulis tabel sumber primer di paling atas: judul dokumen, penerbit (prodi/fakultas),
   tanggal edisi.
2. Kodekan **hanya dari dokumen itu**. Jangan menambal bagian yang tidak ada dengan
   kebiasaan kampus lain; tulis "pedoman diam".
3. Cantumkan nomor klausul pada setiap aturan. Aturan tanpa nomor klausul tidak bisa
   dipertahankan mahasiswa di depan pembimbing.
4. Catat kejanggalan internal pedoman apa adanya (aturan yang bertabrakan di dua
   klausul), beserta klausul mana yang dipakai dan alasannya.
5. Tutup dengan daftar pelanggaran tersering, dipisah antara yang tipografis dan
   yang struktural.
