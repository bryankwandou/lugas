# Laporan uji Lugas — 25 September 2026

## Pertanyaan yang diuji

Apakah Lugas, saat menulis ulang teks bergaya AI, (1) membuat teks lebih mirip
tulisan manusia, (2) tanpa menghilangkan fakta, dan (3) tanpa menambah isi yang
tidak ada di teks asli?

## Bahan

`corpus.jsonl`: 50 teks bergaya AI, ditulis tangan satu per satu (tanpa generator,
tanpa kalimat yang dipakai ulang antar-teks). 25 bahasa Indonesia, 25 bahasa
Inggris, 10 genre (abstrak, latar belakang skripsi, laporan KKP, email kantor,
copy produk, berita, esai opini, surat lamaran, README, notulen). 130–220 kata per
teks. Tiap teks memuat 6–15 fakta (angka, nama, tanggal) yang dicatat di kolom
`facts` — total 476 fakta.

## Metode

1. Lugas menulis ulang tiap teks (mode rewrite).
2. `metrics.py` mengukur: fakta yang masih ada kata per kata, jumlah kata, frasa
   khas AI, variasi panjang kalimat.
3. Tiap pasangan asli–hasil diacak menjadi A/B (seed tetap 20260925). Kunci jawaban
   (`blind-key.json`) disimpan terpisah.
4. Tiga penilai buta hanya membaca `blind-pairs.jsonl` — tanpa kunci, tanpa teks
   asli yang ditandai. Tiap penilai menjawab per pasangan: mana yang lebih mirip
   tulisan manusia; apakah salah satu versi menambah kalimat; apakah salah satu
   versi kehilangan fakta, klaim, atau hubungan sebab-akibat.
5. Jawaban dicocokkan dengan kunci oleh skrip.

## Riwayat ronde

| Ronde | Temuan penilai pada versi Lugas | Perbaikan aturan |
|---|---|---|
| 1 | 6 teks menambah kalimat yang tidak ada di asli (en07, en08, en14, en15, en16, en25) | `checklist.md`: tiap kalimat hasil harus bisa dirujuk ke kalimat asli |
| 2 | 0 kalimat tambahan; 1 penilai menemukan klaim/kaitan sebab hilang di 3 teks (id07, id13, id15) | `checklist.md`: klaim, pernyataan masalah, dan kaitan sebab-akibat wajib tetap ada; hanya basa-basi yang dibuang |
| 3 | Penilai yang lebih ketat: kata penghubung sebab-akibat hilang di ±10 teks; 3 teks memakai tanda `[isi]` dalam mode rewrite | Aturan ronde 2 berlaku; penanda dilarang dalam mode rewrite |
| **Akhir** | **Jalan ulang penuh 50 teks dengan aturan akhir. 0 temuan.** | — |

Catatan kejujuran untuk ronde 2: tiga teks (id07, id13, id15) ditambal langsung,
bukan dijalankan ulang lewat skill. Karena itu ronde akhir menjalankan ulang
**semua** 50 teks dari awal lewat skill, dan hanya hasil ronde akhir yang dipakai
untuk klaim.

Keluaran ronde 1–2 tertimpa selama perbaikan; jawaban penilainya tersimpan di
`round1/`, `round2/`, `round3/`. Keadaan ronde 3 ada di commit `fbad1cd`.

## Hasil ronde akhir (`final/`)

| Ukuran | Hasil |
|---|---|
| Penilaian yang memilih versi Lugas sebagai lebih mirip tulisan manusia | **150/150** (3 penilai × 50) |
| Fakta utuh, kata per kata | **476/476** |
| Kalimat tambahan yang ditemukan penilai | **0** |
| Fakta, klaim, atau sebab-akibat hilang yang ditemukan penilai | **0** |
| Frasa khas AI | 79 → 2 |
| Kata dipangkas | 20,3 % |
| Variasi panjang kalimat (CV) | 0,30 → 0,39 |

Ulangi sendiri: `cd final && python metrics.py`, lalu cocokkan `judge-*.jsonl`
dengan `blind-key.json`.

## Batasan

- **Penilai bukan manusia.** Ketiga penilai adalah instans model AI terpisah, tanpa
  akses ke kunci atau konteks penulisan. Model bisa berbagi selera dengan model
  penulis. Untuk bukti penilaian manusia: berikan `final/blind-pairs.jsonl` kepada
  penilai manusia dan cocokkan jawabannya dengan `final/blind-key.json`.
- **Belum diuji dengan detektor AI** (Turnitin, GPTZero). Lugas tidak dirancang
  untuk mengakali detektor; tujuannya tulisan yang lebih baik.
- **Hasil berlaku untuk 50 teks ini.** Teks sungguhan (draf mahasiswa) lebih
  beragam; hasil pada teks lain bisa berbeda.
- **Imbal balik:** aturan akhir menjaga klaim dan kaitan sebab-akibat, sehingga
  pemangkasan turun dari 31 % (ronde 1) ke 20 %.
- Angka 61.608 cerita dan 93,2 % di lugaskit.vercel.app berasal dari penelitian
  StoryScope (Russell dkk., arXiv:2604.03136) yang menjadi dasar aturan Lugas,
  bukan dari uji ini.
