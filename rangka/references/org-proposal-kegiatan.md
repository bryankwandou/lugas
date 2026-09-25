# Proposal kegiatan

Keluarga G. Dokumen yang **meminta izin dan dana** untuk satu kegiatan (seminar,
lomba, bakti sosial, dies natalis, pelatihan, kunjungan, PkM). Pembacanya pemberi izin
dan pemberi dana: pembina, Wakil Dekan/Wakil Rektor bidang kemahasiswaan, BEM/DPM,
sponsor, pemerintah desa/dinas.

Sumber struktur: praktik umum organisasi kemahasiswaan dan lembaga di Indonesia, serta
dokumen organisasi mahasiswa UAJM yang pernah dipakai membangun skill ini. **Tidak ada
peraturan nasional yang mengunci susunan proposal kegiatan**; lembaga pemberi dana
sering punya format sendiri → `[CEK: format proposal lembaga/kampus]`. Proposal dana
hibah pemerintah (mis. PKM Kemdikbudristek, hibah desa) memakai panduan resminya
sendiri — kalau user menyebutnya, minta/ikuti panduan itu, bukan berkas ini.

## Kerangka

```
SAMPUL        PROPOSAL <NAMA KEGIATAN> · tema (jika ada) · logo organisasi & institusi ·
              nama organisasi · institusi · tahun
LEMBAR PENGESAHAN   ketua panitia · sekretaris panitia · ketua organisasi ·
                    mengetahui: pembina/pembimbing · pejabat kemahasiswaan [CEK: siapa wajib]
KATA PENGANTAR      (opsional, lazim di kampus)
DAFTAR ISI          (jika >8 halaman)

I    PENDAHULUAN
     A. Latar Belakang       — keadaan sekarang → kebutuhan → kenapa organisasi ini
     B. Dasar Kegiatan       — AD/ART, program kerja hasil rapat + tanggal, SK kepengurusan,
                               peraturan kemahasiswaan [ISI: nomor & tanggal]
II   NAMA, TEMA, DAN BENTUK KEGIATAN
III  TUJUAN DAN SASARAN
     A. Tujuan               — umum + khusus, berbutir, terukur
     B. Sasaran / Peserta    — jumlah + kriteria [ISI]
     C. Indikator Keberhasilan — satu indikator per tujuan (dipakai lagi di LPJ)
IV   WAKTU DAN TEMPAT        — hari, tanggal, jam, lokasi
V    SUSUNAN KEPANITIAAN     — pelindung · penanggung jawab · pembina · ketua · sekretaris ·
                               bendahara · koordinator divisi (nama di lampiran bila panjang)
VI   SUSUNAN ACARA / RUNDOWN — jam · kegiatan · penanggung jawab
VII  RENCANA ANGGARAN BIAYA  — lihat tabel di bawah
VIII PENUTUP                 — permohonan dukungan, kontak narahubung
LAMPIRAN   rincian RAB · SK panitia · surat pendukung/izin tempat · desain publikasi ·
           proposal sponsor (paket & kompensasi) · CV pembicara · denah lokasi
```

## RAB — tabel wajib

**A. Pemasukan**

| No | Sumber dana | Jumlah (Rp) | Status |
|---|---|---|---|
| 1 | Dana kemahasiswaan fakultas/universitas | [ISI] | diajukan |
| 2 | Iuran peserta: [ISI] orang × Rp[ISI] | [ISI] | perkiraan |
| 3 | Sponsor | [ISI] | belum pasti |
| 4 | Kas organisasi / usaha dana | [ISI] | pasti |
| | **Total pemasukan** | **[ISI]** | |

**B. Pengeluaran**

| No | Pos | Uraian | Volume | Satuan | Harga satuan (Rp) | Jumlah (Rp) |
|---|---|---|---|---|---|---|
| 1 | Kesekretariatan | cetak proposal/sertifikat | [ISI] | lembar | [ISI] | volume × harga |
| 2 | Konsumsi | snack peserta | [ISI] | kotak | [ISI] | |
| ... | | | | | | |
| | **Total pengeluaran** | | | | | **[ISI]** |

Aturan RAB:
1. Setiap baris = **volume × satuan × harga satuan**; tidak ada angka gelondongan.
2. **Total pemasukan = total pengeluaran.** Kalau angka user tidak seimbang, tulis
   selisihnya dalam rupiah di awal jawaban, beri baris `[ISI: sumber dana untuk menutup
   Rp...]` atau opsi pos yang dipangkas, dan beri OP2 status **Gagal** sampai user memilih.
   Jangan menambah pemasukan karangan.
3. **Rangka menghitung ulang** setiap baris dan total yang user berikan, dan melaporkan
   salah hitung dengan barisnya.
4. Sumber dana disebut; pemasukan yang seluruhnya "dana kampus" tanpa usaha mandiri
   lazim dipotong `[CEK: kebijakan lembaga]`.
5. Harga belum pasti → `[ISI: harga penawaran vendor]`, bukan tebakan.
6. Pos RAB inilah yang **harus muncul lagi baris per baris di LPJ** (`org-lpj.md`).
   Beri nomor pos yang stabil.

## Peta inti

| Node | Isi |
|---|---|
| Should | kegiatan yang dituntut visi/program kerja organisasi |
| Is | keadaan peserta/organisasi sekarang |
| Gap | kebutuhan yang belum terwadahi |
| Reader | pemberi izin + pemberi dana |
| Core claim | kegiatan ini perlu, layak dijalankan, dan anggarannya wajar |
| Proof | dasar kegiatan, rundown, panitia, RAB seimbang |
| Action | menyetujui dan mencairkan dana |

## Cek proposal (OP)

| Kode | Cek |
|---|---|
| OP1 | Setiap tujuan punya kegiatan di rundown dan indikator keberhasilan? |
| OP2 | RAB: volume × harga per baris, hitungan benar, pemasukan = pengeluaran? |
| OP3 | Dasar kegiatan menyebut dokumen dengan nomor/tanggal atau `[ISI]`? |
| OP4 | Lembar pengesahan memuat penanda tangan yang disyaratkan lembaga (atau `[CEK]`)? |
| OP5 | Tanggal, tempat, jumlah peserta, harga, nama — tidak ada yang dikarang? |
| OP6 | Pos RAB bernomor stabil untuk dipakai di LPJ? |
