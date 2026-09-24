# Genre D — Teknis (README, dokumentasi, spec/PRD, ADR, tutorial)

Pembaca dokumen teknis datang dengan tugas. Outline disusun dari tugas itu, bukan dari
struktur kode. Peta Should/Is: **Should** = perilaku atau kemampuan yang diharapkan,
**Is** = kondisi sekarang, **Gap** = perubahan atau pengetahuan yang dibutuhkan.

## D1. Pilih jenis dokumen dulu (Diátaxis)

Diátaxis (Procida) membagi dokumentasi menjadi empat jenis dengan tujuan berbeda.
Mencampurnya dalam satu halaman adalah penyebab dokumentasi membingungkan paling umum.

| Jenis | Pembaca sedang… | Bentuk |
|---|---|---|
| Tutorial | belajar, pemula | langkah terpandu dengan hasil pasti |
| How-to guide | bekerja, punya tujuan spesifik | langkah untuk satu masalah |
| Reference | mencari fakta | daftar lengkap, konsisten, tanpa cerita |
| Explanation | ingin paham | latar, alasan, perbandingan |

## D2. Template per jenis

### README
1. Nama + satu kalimat: apa ini dan untuk siapa
2. Tangkapan layar atau contoh output (jika ada antarmuka)
3. Quick start: prasyarat, instalasi, satu perintah yang berhasil
4. Penggunaan umum (2–4 contoh)
5. Konfigurasi (tabel: nama, default, arti)
6. Cara kerja singkat / arsitektur (opsional)
7. Kontribusi, pengujian
8. Lisensi
Setiap perintah di outline harus diuji sebelum README final. Tandai `[CEK: dijalankan?]`.

### Spec / PRD
1. Masalah (Should vs Is, dengan bukti: tiket, data, keluhan)
2. Tujuan dan non-tujuan (apa yang sengaja tidak dikerjakan)
3. Pengguna dan skenario
4. Persyaratan (bernomor; fungsional dan non-fungsional)
5. Desain yang diusulkan (alur, data, API)
6. Alternatif yang ditolak dan alasannya
7. Risiko, keamanan, privasi
8. Metrik keberhasilan (terukur)
9. Rencana rilis dan rollback
10. Pertanyaan terbuka

### ADR (Architecture Decision Record, format Nygard)
Judul · Status (proposed/accepted/superseded) · Context · Decision · Consequences.
Satu keputusan per ADR.

### Tutorial
1. Yang akan dibuat (tampilkan hasil akhir)
2. Prasyarat (versi spesifik)
3. Langkah bernomor; tiap langkah: tindakan → kode → hasil yang harus terlihat
4. Titik cek ("jika kamu melihat X, lanjut")
5. Masalah umum
6. Langkah berikutnya

### Dokumentasi API (reference)
Per endpoint/fungsi: ringkasan satu baris · parameter (tabel: nama, tipe, wajib, arti) ·
respons/return · error · contoh request dan response · batasan (rate limit, izin).

### Laporan bug / insiden (postmortem)
Ringkasan dampak → linimasa → akar masalah → yang berjalan baik → yang tidak → tindakan
perbaikan (pemilik + tenggat). Tanpa menyalahkan individu.

## D3. Pemeriksaan khusus teknis

- [ ] Jenis Diátaxis jelas; tidak dicampur dalam satu halaman.
- [ ] Setiap perintah dan contoh kode sudah atau akan diuji (`[CEK]` jika belum).
- [ ] Versi dan prasyarat disebut.
- [ ] Non-tujuan ditulis (spec).
- [ ] Metrik keberhasilan terukur (spec).
- [ ] Tidak ada rahasia (API key, token, password) di contoh.
