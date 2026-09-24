# Audit mode — bentuk keluaran dan urutan keparahan

Dipakai ketika pengguna sudah punya draf dan ingin tahu apa yang melanggar pedoman.

## Prinsip

1. **Satu baris per pelanggaran, bukan per opini.** Kalau tidak bisa menunjuk
   klausul, itu saran, dan harus ditulis sebagai saran.
2. **Jangan menulis ulang prosa.** Audit menyebut apa yang salah dan apa perbaikannya.
   Mengganti kalimat mahasiswa dengan kalimat sendiri bukan pekerjaan skill ini.
3. **Yang keras dulu.** Mahasiswa yang punya waktu dua hari harus tahu tiga hal
   pertama yang wajib dikerjakan, bukan tiga puluh hal berurutan alfabet.
4. **Yang tidak bisa diperiksa, katakan tidak bisa diperiksa.** Warna sampul, jenis
   kertas, dan hasil jilid tidak terbaca dari file. Tandai `[CEK: ...]`, jangan
   diloloskan diam-diam dan jangan divonis salah.

## Tiga tingkat keparahan

| Tingkat | Arti | Contoh |
|---|---|---|
| **Keras** | naskah dikembalikan atau ditolak; wajib diperbaiki sebelum diserahkan | margin salah, bullet sebagai penanda rincian, bagian wajib hilang, kesimpulan tidak menjawab rumusan masalah |
| **Lunak** | akan dicoret penguji, tidak sampai menggagalkan | jarak spasi daftar tabel, huruf kapital pada judul tabel, konsistensi istilah |
| **Catatan** | pedoman diam; ini praktik lazim, bukan aturan | panjang bab, jumlah rujukan, gaya penomoran gambar pada lampiran |

Pelanggaran **struktural** (kesimpulan, saran, orphan pada rumusan masalah) tetap
masuk *Keras*, dengan catatan bahwa perbaikannya ada di tingkat rangka, bukan
tipografi.

## Bentuk tabel

```
## Hasil audit — <jenis dokumen>, <institusi>, pedoman edisi <edisi>

### Keras
| Bagian | Aturan | Klausul | Temuan | Perbaikan |
|---|---|---|---|---|
| Sembir | kiri 4 cm | KKP 4.1.2 | kiri 3 cm | setel margin kiri 4 cm |

### Lunak
| Bagian | Aturan | Klausul | Temuan | Perbaikan |

### Perlu dicek di luar file
- [CEK: warna sampul — hijau untuk KKP (KKP 4.1.5)]
- [CEK: jilid hardcover 3 eksemplar (KKP 2.2l)]

### Tidak diatur pedoman
- <hal> — pedoman diam. Praktik lazim: <saran>, ditandai sebagai saran.
```

Jika tidak ada temuan keras, tulis satu baris: `Keras: tidak ada.` Jangan hilangkan
bagiannya — ketiadaan temuan adalah informasi.

## Urutan pemeriksaan

Periksa dalam urutan ini, karena temuan di tingkat atas membuat pemeriksaan di
bawahnya sia-sia:

1. **Gerbang akademik** — boleh tidaknya dokumen ini diserahkan sekarang.
2. **Kelengkapan bagian** — ada/tidaknya tiap bagian wajib, berikut urutannya.
3. **Struktur isi** — tiap bab memuat butir yang diwajibkan; rumusan masalah →
   tujuan → bab → bukti → kesimpulan → saran tanpa baris kosong.
4. **Tipografi** — kertas, margin, huruf, spasi, indent, perataan.
5. **Penomoran** — halaman, bab, subjudul (kedalaman!), tabel, gambar, persamaan.
6. **Tabel dan gambar** — letak judul, penomoran seri, pemenggalan, satuan.
7. **Rujukan** — gaya entri, kelengkapan, dan kesesuaian dua arah antara naskah dan
   daftar.
8. **Bahasa** — kata ganti, kata sambung di awal paragraf, istilah asing yang tidak
   dimiringkan, bilangan di awal kalimat.
9. **Lampiran** — kelengkapan lampiran wajib.

## Kalimat penutup audit

Maksimal tiga baris: edisi pedoman yang dipakai, jumlah temuan keras/lunak, dan apa
yang tidak bisa diperiksa dari file. Tanpa penyemangat, tanpa ringkasan ulang.
