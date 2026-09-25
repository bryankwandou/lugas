# Menyesuaikan kerangka ke pedoman kampus mana pun

Rangka tidak menyimpan pedoman semua kampus — tidak mungkin dan akan cepat usang.
Yang disimpan adalah **prosedur adaptasi**: sedikit variabel yang benar-benar mengubah
kerangka, dan cara mengisinya dari pedoman yang user punya.

Urutan kewenangan: pedoman prodi > pedoman fakultas > pedoman universitas > kebiasaan
pembimbing > konvensi umum > isi berkas ini. Kalau bertabrakan, yang di kiri menang,
dan perbedaannya disebutkan terang-terangan.

## Langkah adaptasi

1. **Kalau user memberi berkas pedoman** (PDF/DOCX), baca dan isi tabel variabel di
   bawah. Selesai — jangan menebak apa pun yang tertulis di situ.
2. **Kalau tidak ada berkas**, pakai bawaan yang paling lazim di Indonesia (kolom
   "Bawaan"), tandai setiap butir yang berisiko dengan `[CEK: pedoman kampus]`, dan
   teruskan. Jangan menghentikan pekerjaan hanya karena pedoman belum ada.
3. **Kalau kampusnya UAJM FTI**, jangan pakai bawaan — pakai `uajm-*.md`.
4. **Kalau kampusnya punya berkas `campus-*.md`** (22 kampus: UI, UGM, ITB, ITS, Unhas,
   Binus, UNM, UMI, Unair, UB, IPB, Unpad, UIN Alauddin, Unismuh, Undip, UNS, UPI, UNY,
   UII, UMY, Telkom, UIN Jakarta), baca berkas itu dulu. Isi variabel dari berkas itu hanya untuk
   aturan yang tertulis berlaku se-universitas; variabel yang di berkas itu disebut
   "ditentukan fakultas/prodi" tetap `[CEK ke pedoman fakultas]` sampai user menyebut
   fakultasnya. Contoh empat kampus:

   | Kampus | Pedoman tingkat universitas? | Yang diatur fakultas/prodi |
   |---|---|---|
   | UI | Ya — pedoman teknis, SK Rektor 2143/2017 (format saja) | jumlah & nama bab, gaya sitasi, proposal |
   | UGM | Tidak ditemukan — per fakultas/departemen | hampir semuanya, termasuk spasi (1,15 / 1,5 / 2) dan margin |
   | ITB | S1 tidak ditemukan; tesis: SPs 2016 | S1: semuanya per prodi |
   | Unhas | Ya — SK Rektor 10438/2023 (struktur **dan** format; tanpa bab Tinjauan Pustaka) | proposal; ambang kemiripan; fakultas yang masih memakai pedoman lama |

5. **Kalau pedomannya berbahasa asing** (Inggris, Arab, Mandarin, Belanda, ...) atau
   kampusnya di luar negeri: baca pedoman itu dalam bahasa aslinya, isi 14 variabel
   dengan **kutipan pendek + nomor halaman/pasal** dari pedoman (bahasa asli, lalu
   terjemahan kerja dalam kurung), dan pakai **nama bagian persis seperti pedoman**
   (mis. `الفصل الأول: الإطار العام للدراسة`, `Chapter 2 Literature Review`) — terjemahan
   kerja hanya sebagai keterangan. Bentuk bawaan per tradisi ada di `international.md`.
6. **Kalau dua pedoman bertentangan** (pedoman universitas vs template prodi, edisi
   lama vs baru, teks vs contoh lampiran di pedoman yang sama): terapkan urutan
   kewenangan di atas, sebutkan kedua bunyinya, dan tandai `[CEK: ...]`. Jangan memilih
   diam-diam. Contoh nyata: pedoman KKP UAJM menulis sampul "warna program studi" di
   3.1.1 dan "hijau" di 4.1.5.
7. **Kalau tidak ada pedoman sama sekali dan kampusnya tidak dikenal**: pakai bawaan,
   tulis satu baris "Kerangka ini memakai bawaan umum karena pedoman kampus belum
   ada" di atas tabel variabel, dan jadikan "unggah/sebutkan pedoman" butir pertama di
   blok akhir.

Setiap nilai variabel di tabel yang ditampilkan ke user diberi **asal**: `pedoman (hlm.
n)` · `campus-*.md` · `bawaan [CEK]`. Nilai tanpa asal tidak boleh muncul.

## Variabel yang benar-benar mengubah kerangka

| # | Variabel | Bawaan (paling lazim di Indonesia) | Kalau berbeda, akibatnya |
|---|---|---|---|
| 1 | Jumlah bab | 5 | 4 bab (hasil+pembahasan+penutup digabung) atau 6 bab (pembahasan terpisah) |
| 2 | Letak rumusan masalah, tujuan, manfaat, batasan | sub-bab sejajar di Bab I | UAJM menaruhnya **di dalam** Latar Belakang |
| 3 | Bab II disebut | "Tinjauan Pustaka" | "Kajian Teori", "Landasan Teori", atau Bab II teori + Bab III kerangka konsep |
| 4 | Kerangka pikir/konsep | bagan di Bab I atau akhir Bab II | letaknya berpindah → nomor sub-bab bergeser |
| 5 | Hasil & pembahasan | satu bab | terpisah jadi dua bab |
| 6 | Penomoran sub-bab | `1.1`, `1.1.1` (Arab bertingkat) | `A.`, `1.`, `a.` (gaya banyak PTKIN/hukum) |
| 7 | Kedalaman maksimal | 4 tingkat | ada yang 3 |
| 8 | Gaya sitasi | penulis-tahun | APA 7, IEEE (teknik), Vancouver (kesehatan), Chicago (sejarah) |
| 9 | Abstrak | ID + EN | ada yang + bahasa daerah/Arab; batas kata 150–300 |
| 10 | Bagian awal khusus | pengesahan, pernyataan orisinalitas | pedoman penggunaan skripsi, peruntukan, transliterasi (PTKIN), motto |
| 11 | Nomor tabel/gambar | satu seri seluruh naskah | per bab (`Tabel 2.1`) |
| 12 | Luaran wajib | naskah jurnal | artikel terbit, poster, HKI, produk |
| 13 | Sistematika penulisan | disebut di akhir Bab I | ada yang melarang |
| 14 | Batas kemiripan | — | ada ambang (mis. 25%) → memengaruhi cara mengutip |

Isi tabel ini di awal pekerjaan dan **tampilkan hasilnya ke user** sebelum kerangka.
Itu membuat perbedaan dengan template yang mereka punya jadi terlihat, bukan jadi
kejutan saat bimbingan.

## Ragam yang sudah diketahui di Indonesia

Ini peta kasar untuk mengarahkan dugaan — **bukan pengganti pedoman**. Selalu
`[CEK: pedoman kampus]`.

| Rumpun | Kecenderungan |
|---|---|
| Teknik/informatika | penelitian rekayasa lazim; Bab III berisi perancangan (UML/ERD); Bab IV berisi implementasi + pengujian; sitasi IEEE atau penulis-tahun; luaran berupa sistem |
| Ekonomi/manajemen | kuantitatif dominan; definisi operasional variabel wajib; uji asumsi klasik; Bab IV memuat uji hipotesis; APA |
| Pendidikan | PTK (penelitian tindakan kelas) dengan siklus; R&D (ADDIE/4D/Borg & Gall); instrumen + validasi ahli |
| Kesehatan/keperawatan | ethical clearance wajib; kerangka teori **dan** kerangka konsep terpisah; definisi operasional; Vancouver |
| Hukum | yuridis normatif vs empiris; bahan hukum primer/sekunder/tersier menggantikan "populasi & sampel"; penomoran huruf; catatan kaki |
| PTKIN (UIN/IAIN/STAIN) | transliterasi Arab-Latin di bagian awal; pedoman transliterasi SKB Menag-Mendikbud; kadang abstrak tiga bahasa |
| Sosial/komunikasi kualitatif | paradigma & pendekatan dinyatakan; triangulasi; keabsahan data (kredibilitas, transferabilitas, dependabilitas, konfirmabilitas) |
| Vokasi/D3–D4 | laporan tugas akhir terapan; bobot pada proses dan produk, bukan kebaruan teori |

Istilah lokal yang sering ditemui dan artinya: **KKP / KP / PKL / Magang / MBKM** =
kerja praktek; **Usulan Penelitian / Proposal / Pra-proposal** = tahap awal TA;
**Seminar Judul / Seminar Proposal / Sempro**; **Seminar Hasil / Semhas**;
**Sidang / Ujian Komprehensif / Munaqasyah** (PTKIN) = ujian akhir; **Skripsi /
Tugas Akhir / Karya Tulis Ilmiah (KTI, D3 kesehatan)**.

## Di luar Indonesia

Kerangka intinya sama (gap → pertanyaan → metode → bukti → klaim); yang berbeda
kemasannya.

| Wilayah/sistem | Ciri |
|---|---|
| IMRaD (standar artikel ilmiah sedunia) | Introduction · Methods · Results · Discussion (+ Abstract, References) |
| Inggris/Australia (PhD monograf) | Introduction · Literature Review · Methodology · Findings · Discussion · Conclusion; ada *thesis statement* dan *contribution to knowledge* |
| Amerika Serikat | proposal = bab 1–3; ada *Definition of Terms*, *Assumptions and Limitations*, *Delimitations*; IRB approval setara ethical clearance |
| Eropa daratan (article-based) | rangkaian artikel + *kappa*/summary chapter |
| Jerman | struktur bebas, penekanan pada *Forschungsfrage* dan *Forschungsstand* |
| Prancis | *problématique* (bukan sekadar rumusan masalah) · *plan* dua atau tiga bagian yang simetris · *introduction/développement/conclusion* |
| Amerika Latin (Brasil/Meksiko) | *TCC/monografia*: Introdução · Referencial Teórico · Metodologia · Resultados e Discussão · Considerações Finais; ABNT untuk Brasil |
| Jepang/Korea/Tiongkok | mendekati IMRaD; sering menuntut ringkasan bahasa Inggris + bahasa setempat |
| Belanda/Skandinavia | *research design* dan *operationalization* dipisah tegas |

Untuk kampus mana pun di luar Indonesia, jalankan prosedur yang sama: isi 14 variabel
dari pedoman yang user punya (*style guide*, *thesis handbook*, *rubric*), pakai IMRaD
sebagai bawaan, dan tandai selebihnya `[VERIFY: department handbook]`.

## Cek adaptasi

| Kode | Cek |
|---|---|
| A1 | 14 variabel sudah diisi, dari pedoman bila ada? |
| A2 | Setiap butir yang belum pasti ditandai `[CEK: pedoman kampus]`? |
| A3 | Perbedaan dengan template yang dibawa user sudah disebutkan? |
| A4 | Istilah lokal dipakai sesuai kampus (KKP vs KP vs PKL, dst.)? |
| A5 | Gaya sitasi konsisten di seluruh kerangka? |
| A6 | Tidak ada aturan kampus yang dikarang? |
| A7 | Tiap nilai variabel diberi asal (pedoman + halaman / campus file / bawaan [CEK])? |
| A8 | Pedoman berbahasa asing: nama bagian dipakai dalam bahasa asli pedoman, konflik antarpedoman disebut? |
