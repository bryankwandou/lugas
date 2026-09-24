# Dokumen dalam bahasa selain Indonesia dan Inggris

Dipakai ketika naskah harus patuh pedoman **dan** ditulis dalam bahasa yang konvensi
akademisnya berbeda. Isi file ini adalah hal-hal yang menyebabkan dokumen ditolak
karena bahasanya, bukan kursus bahasa.

## Aturan pertama

**Bahasa keluaran mengikuti bahasa pengguna**, kecuali diminta lain. Kalau pengguna
menulis dalam bahasa Jawa dan dokumennya harus berbahasa Indonesia, keluarkan
dokumennya dalam bahasa Indonesia dan penjelasannya dalam bahasa pengguna.

**Penanda tetap konsisten satu bahasa di seluruh keluaran.** `[ISI: ...]` dan
`[CEK: ...]` untuk bahasa Indonesia; `[FILL: ...]` dan `[VERIFY: ...]` untuk bahasa
Inggris. Jangan dicampur di satu dokumen.

## Empat hal yang berbeda antar-bahasa

### 1. Ragam formal dan sudut pandang

| Bahasa | Tuntutan yang mengikat |
|---|---|
| Indonesia | ragam baku, kalimat pasif, orang ketiga; *penulis* menggantikan *saya* |
| Inggris | makin banyak jurnal menerima *we*; sebagian departemen masih melarang — `[CEK]` |
| Jerman | ragam *Wissenschaftssprache*; nominalisasi lazim; *man* menggantikan orang pertama |
| Jepang | gaya *de aru*/*dearu* untuk naskah ilmiah, bukan *desu/masu* |
| Korea | gaya *hapsyo*/tertulis formal (*-다* ending), bukan ragam percakapan |
| Arab | ragam fusha (Arab standar modern), bukan dialek |
| Mandarin | 书面语 formal; hindari ragam lisan |
| Jawa / Sunda | ragam krama untuk dokumen resmi; ngoko menandai ketidakformalan |

Kalau ragamnya salah, pembaca akademik menganggapnya tidak serius, terlepas dari
isinya. Ini setara dengan kata ganti orang pertama dalam naskah Indonesia.

### 2. Arah tulisan dan tata letak

Bahasa yang ditulis kanan-ke-kiri — Arab, Ibrani, Persia, Urdu — mengubah hal-hal
yang tidak kelihatan sampai dokumen dicetak:

- margin jilidan pindah ke **kanan**;
- penomoran halaman dan daftar isi ikut berbalik;
- angka tetap kiri-ke-kanan di dalam kalimat kanan-ke-kiri, sehingga campuran
  angka-teks rawan berantakan;
- rumus, kode program, dan istilah Latin tetap kiri-ke-kanan dan butuh penanganan
  khusus;
- tabel berbalik arah kolom.

Sebutkan hal ini di awal, bukan setelah dokumen jadi.

### 3. Transliterasi dan nama dalam daftar pustaka

Ini penyebab kekacauan daftar pustaka yang paling sering:

- **Nama Cina, Korea, Jepang, Hungaria, Vietnam** menaruh nama keluarga di depan.
  Membaliknya "supaya seperti Barat" justru salah, dan gaya sitasi punya aturan
  masing-masing → `[CEK: aturan gaya untuk nama <bahasa>]`.
- **Nama Arab** dengan *al-*, *el-*, *ibn*, *abu*: pengabjadan berbeda antar-gaya
  dan antar-perpustakaan.
- **Transliterasi** (Arab, Rusia, Thai, Yunani) punya lebih dari satu sistem. Pilih
  satu, sebutkan yang dipilih, dan pakai seterusnya.
- **Sumber berbahasa asing** sering harus disertai terjemahan judul dalam kurung
  siku, dan bahasa aslinya dinyatakan. Aturannya milik gaya sitasi → `[CEK]`.

Pedoman UAJM sendiri sudah memuat aturan nama Belanda, Perancis, Jerman, Portugis,
Brasil, Spanyol, Arab, dan Cina — lihat `uajm-fti.md` §A.8. Untuk naskah UAJM,
aturan itu yang dipakai, bukan aturan gaya internasional.

### 4. Angka, tanggal, satuan

| Hal | Variasi |
|---|---|
| Desimal | koma (Indonesia, sebagian besar Eropa) vs titik (Inggris, Amerika) |
| Pemisah ribuan | titik vs koma vs spasi tipis |
| Tanggal | 03/04 bisa 3 April atau 4 Maret — tulis nama bulan pada naskah akademik |
| Angka | Arab-Timur (٣) vs Arab-Barat (3) pada naskah Arab |
| Kalender | Hijriah, Jepang (*nengō*), Buddhis — sebutkan sistemnya bila dipakai |

Pedoman UAJM mewajibkan satuan dengan singkatan resmi tanpa titik, dan bilangan
yang mengawali kalimat harus dieja. Aturan sejenis ada di hampir semua bahasa,
dengan rincian berbeda.

## Naskah dwibahasa

Yang lazim diminta kampus: judul dalam dua bahasa, abstrak dalam dua bahasa, isi
dalam satu bahasa. Yang perlu diperiksa:

1. Kedua judul benar-benar bermakna sama; judul Inggris hasil terjemahan mesin yang
   menggeser makna adalah temuan yang rutin dicoret.
2. Kedua abstrak memuat butir yang sama, bukan salah satunya lebih pendek.
3. Batas kata berlaku untuk keduanya.
4. Istilah teknis diterjemahkan konsisten di seluruh naskah, bukan berganti-ganti.

Untuk UAJM: sampul TA memuat judul Indonesia dan judul Inggris (miring); abstrak ada
dalam dua bahasa, masing-masing 200–250 kata; naskah jurnal hanya memuat *abstract*
Inggris maksimal 100 kata. Tiga angka berbeda untuk tiga tempat berbeda.

## Tabel bahasa tambahan — hanya yang bersumber

Baris di bawah **hanya** memuat apa yang tertulis di sumber yang disebut. Kolom yang
tidak bersumber dibiarkan "—"; jangan diisi dari ingatan. Ragam formal untuk bahasa
baru **tidak** ditambahkan karena belum ada sumber primer yang dibaca.

Sumber:
- **[W3C-RTL]** W3C Internationalization, *Languages using right-to-left scripts* —
  https://www.w3.org/International/questions/qa-scripts (data Ethnologue per 16 Juni 2022).
- **[W3C-NAMA]** W3C Internationalization, *Personal names around the world* —
  https://www.w3.org/International/questions/qa-personal-names
- **[CLDR]** Unicode CLDR, paket `cldr-numbers-full` dan `cldr-dates-full` versi
  **48.2.0** (via cdn.jsdelivr.net/npm), kalender Gregorian, pola `long` dan `short`.
  Ini format **bawaan lokal**, bukan aturan kampus: pedoman kampus tetap menang
  (contoh: ITB mewajibkan desimal koma — `itb-sps.md` §7).

### Arah tulisan [W3C-RTL]

Arah milik **aksara**, bukan bahasa: Azeri ditulis LTR dalam Latin/Sirilik, RTL
dalam aksara Arab. Aksara RTL yang terdaftar di sumber mencakup Arab, Ibrani
(Hebrew), Suryani (Syriac), Thaana, N'Ko, dan Adlam, di antara 12 aksara RTL.
Bahasa yang tercantum ditulis dengan aksara RTL antara lain Arab, Persia, Urdu,
Pashto, Sindhi, Kurdi Sorani, Uyghur, Ibrani, Yiddish, dan Dhivehi. Semua dampak
tata letak di §2 berlaku untuk mereka.

### Urutan nama [W3C-NAMA]

| Budaya | Yang tertulis di sumber |
|---|---|
| Cina | nama keluarga di depan (毛泽东: keluarga *Mao*) |
| Jepang, Korea, Hungaria | nama keluarga diikuti nama diri |
| Vietnam | keluarga–tengah–diri (Nguyễn Tấn Dũng), tetapi disapa dengan nama diri |
| Islandia | nama diri + patronim (-son/-dóttir); direktori diurut menurut **nama diri** |
| Thailand | daftar diurut menurut nama diri; nama panggilan dipakai di situasi tak formal |
| Rusia | diri–patronim–keluarga; ragam kurang formal keluarga–diri–patronim |
| Spanyol | dua nama keluarga, umumnya ayah + ibu; Brasil (Portugis) umumnya ibu + ayah |
| India Selatan, Malaysia, Indonesia | banyak orang hanya punya nama diri, **tanpa nama keluarga** |
| Jepang (tambahan) | kanji nama bisa dibaca beberapa cara; lazim disertai kana untuk lafal |

Konsekuensi untuk daftar pustaka: jangan memaksa "nama belakang, inisial" pada
nama tanpa nama keluarga. ITB mengatur ini eksplisit: nama Indonesia tanpa nama
keluarga ditulis seperti penulisnya menulis sendiri (`itb-sps.md` §6, T VI.2).
UTokyo GPEAK: nama mahasiswa asing yang tidak ditulis dalam kanji ditranskripsi ke
katakana, dan urutan nama harus sama di semua dokumen (`global-institutions.md`).

### Angka dan tanggal bawaan lokal [CLDR 48.2.0]

| Lokal | Sistem angka bawaan | Desimal | Ribuan | Tanggal panjang | Tanggal pendek |
|---|---|---|---|---|---|
| id (Indonesia) | latn | , | . | d MMMM y | dd/MM/yy |
| ms (Melayu) | latn | . | , | d MMMM y | d/MM/yy |
| en (AS) | latn | . | , | MMMM d, y | M/d/yy |
| en-GB | latn | . | , | d MMMM y | dd/MM/y |
| de | latn | , | . | d. MMMM y | dd.MM.yy |
| fr | latn | , | spasi sempit tak putus (U+202F) | d MMMM y | dd/MM/y |
| nl | latn | , | . | d MMMM y | dd-MM-y |
| es | latn | , | . | d 'de' MMMM 'de' y | d/M/yy |
| pt | latn | , | . | d 'de' MMMM 'de' y | dd/MM/y |
| ru | latn | , | spasi tak putus (U+00A0) | d MMMM y 'г'. | dd.MM.y |
| tr | latn | , | . | d MMMM y | d.MM.y |
| vi | latn | , | . | d MMMM, y | d/M/yy |
| ar | latn (asli: arab) | . | , | d MMMM y | d/M/y |
| fa | **arabext** | ٫ (U+066B) | ٬ (U+066C) | d MMMM y | y/M/d |
| he | latn | . | , | d בMMMM y | d.M.y |
| hi | latn (asli: deva) | . | , | d MMMM y | d/M/yy |
| th | latn (asli: thai) | . | , | d MMMM G y | d/M/yy |
| ja | latn | . | , | y年M月d日 | y/MM/dd |
| ko | latn | . | , | y년 MMMM d일 | yy. M. d. |
| zh | latn (asli: hanidec) | . | , | y年M月d日 | y/M/d |

Yang penting dari tabel ini: **"tanggal pendek" berbeda urutan** (M/d vs d/M vs y/M/d),
jadi naskah akademik sebaiknya menulis nama bulan (§4). Pola Persia memakai angka
Arab-Timur-diperluas secara bawaan; Arab bawaan CLDR memakai angka Latin.

### Dari pedoman institusi yang sudah dibaca

| Bahasa | Aturan | Sumber |
|---|---|---|
| Arab (naskah di UM, Fakultas Sains) | huruf **Traditional Arabic 16** | `global-institutions.md`, UM-FS hlm. 3 |
| Melayu | abstrak wajib dalam **bahasa Malaysia dan Inggris** (UM-FS) | UM-FS hlm. 6 |
| Jepang | abstrak diketik **horizontal**, dicetak A4 tegak; ≤ 4000 karakter | UTokyo GPEAK 3.5.2 |
| Inggris (di UNS) | bila naskah berbahasa Inggris: *past tense*, *passive verbs* | `uns-pps.md` §4 |
| Indonesia (ITB) | *dkk.*, bukan *et al.*, karena naskah berbahasa Indonesia | `itb-sps.md` §6 |
| Indonesia (UGM Faperta, UNS) | justru *et al.* | `ugm-faperta.md` §5 · `uns-pps.md` §5 |

Baris terakhir penting: "dkk. vs et al." **berbeda antar-kampus Indonesia**. Jangan
membetulkan satu ke yang lain tanpa melihat pedoman kampusnya.

## Menambah bahasa ke file ini

Tulis hanya apa yang bisa dipertanggungjawabkan: ragam formal yang benar, arah
tulisan, kaidah nama, dan format angka/tanggal. Jangan menuliskan "aturan tesis"
sebuah negara tanpa membaca pedoman universitasnya — itu tetap `[CEK]`.
