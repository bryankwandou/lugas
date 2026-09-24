# Roadmap — dari UAJM ke tesis, disertasi, semua kampus, semua bahasa

Urutan pengembangan: UAJM dulu, lalu jenjang lebih tinggi, lalu kampus lain di
Indonesia, lalu dunia, lalu bahasa. Tabel status di bawah jujur: yang belum dibaca dari
sumber primer ditulis *belum*.

## Status per September 2026

| Lapis | Status | Di mana |
|---|---|---|
| UAJM Informatika — KKP, proposal, RKD, skripsi, naskah jurnal | **terkodekan dari PDF primer** (2015) | skill ini + `pedoman/references/uajm-fti.md` |
| UAJM prodi lain (SI, Sipil, Arsitektur, Manajemen, Akuntansi, Hukum, …) | belum — pedoman belum dibaca | `kasus.md` K-38 |
| UAJM pascasarjana (tesis) | belum | → `pedoman/references/indonesia-general.md` §3 |
| Tesis dan disertasi, kampus lain | **terkodekan**: ITB, UI, IPB, UGM Faperta, UB PPS, ITS, Unair, Unhas, UNS, Unpad (isi bab), Undip (3 prodi) | `pedoman/references/<kampus>.md` |
| Kampus Indonesia lain | sumbu perbedaan + pertanyaan yang harus diajukan | `pedoman/references/indonesia-general.md` |
| Luar negeri | MIT, York, ANU, UM Fak. Sains, UTokyo GPEAK + gaya sitasi dunia | `pedoman/references/global-institutions.md`, `global.md` |
| Bahasa | arah tulisan, urutan nama, angka/tanggal CLDR untuk 20 lokal | `pedoman/references/languages.md` |

## Kalau pengguna UAJM naik ke tesis

Pedoman pascasarjana UAJM belum dibaca. Yang bisa dikatakan dengan jujur:

1. Tipografi biasanya mewarisi pedoman pascasarjana kampus → minta dokumennya.
2. Tuntutan isi naik: kebaruan harus diklaim eksplisit dan ditopang tinjauan pustaka;
   lihat tabel skripsi–tesis–disertasi di `pedoman/references/indonesia-general.md` §3.
3. Kebiasaan UAJM S1 yang **tidak** boleh dibawa tanpa cek: nomor tabel satu seri,
   larangan bullet, gaya pustaka nama-tahun UAJM.

## Cara menambah kampus atau prodi (termasuk prodi UAJM lain)

Aturan yang sama dengan `pedoman`: hanya dari dokumen primer, dengan klausul.

1. Minta PDF pedoman prodi. Simpan di `pedoman/sources/` (lokal saja; hak cipta milik
   kampus).
2. Buat `pedoman/references/uajm-<prodi>.md` dengan tabel sumber di atas.
3. Salin bentuk file di skill ini (`kkp.md`, `proposal.md`, `tugas-akhir.md`) menjadi
   `references/<prodi>/…` hanya untuk bagian yang **berbeda**; sisanya merujuk ke file
   Informatika dengan catatan "sama, dicek pada <tanggal>".
4. Tambah kasus uji di `tests/cases.md`.

## Cara menambah bahasa

Kerangka dan checklist di skill ini berbahasa Indonesia karena pedomannya berbahasa
Indonesia. Untuk keluaran dalam bahasa lain: struktur tetap mengikuti pedoman; ragam,
arah tulisan, nama, dan angka mengikuti `pedoman/references/languages.md`. Istilah bab
yang ditetapkan pedoman (mis. *Uraian Teknis Pelaksanaan KKP*) tetap ditulis apa adanya
kecuali prodi mengizinkan naskah berbahasa asing (TA 5.5.1).
