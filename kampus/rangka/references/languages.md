# Bahasa keluaran

Aturan pokok: **kerangka ditulis dalam bahasa yang dipakai user**, kecuali user meminta
lain. Kalau user menulis campuran (lazim di Indonesia: kalimat Indonesia dengan istilah
Inggris), ikuti bahasa kalimatnya, bukan bahasa istilahnya.

Struktur kerangka tidak berubah karena bahasa. Yang berubah hanya label, penanda, dan
beberapa kebiasaan retoris.

## Penanda isian

| Bahasa | Perlu diisi user | Perlu diverifikasi | Tidak ada di berkas |
|---|---|---|---|
| Indonesia | `[ISI: ...]` | `[CEK: ...]` | `[TIDAK ADA DI BERKAS: ...]` |
| Inggris | `[FILL: ...]` | `[VERIFY: ...]` | `[NOT IN SOURCE: ...]` |
| Bahasa lain | pakai padanan setempat, **konsisten satu bentuk** di seluruh keluaran | | |

Untuk bahasa yang tidak punya padanan mapan, pakai bentuk Inggris (`[FILL]`/`[VERIFY]`)
dan jelaskan sekali di awal. Jangan mencampur dua bahasa penanda dalam satu keluaran.

## Label bagian

| id | en | Keterangan |
|---|---|---|
| Peta inti | Core map | |
| Kerangka | Outline | |
| Hasil cek | Check | |
| Opsi judul | Title options | |
| Yang perlu kamu lengkapi | What you need to supply | |
| Tugas / Isi / Bukti / Panjang | Job / Content / Evidence / Length | field tiap bagian |

### Label dalam bahasa lain

Terjemahan kerja, bukan istilah baku lembaga mana pun. Kalau pedoman kampus memakai istilah
lain, istilah pedoman yang menang.

| Kode | Peta inti | Kerangka | Hasil cek | Opsi judul | Yang perlu kamu lengkapi | Penanda isi / cek |
|---|---|---|---|---|---|---|
| ms | Peta teras | Kerangka | Semakan | Pilihan tajuk | Perkara yang perlu anda lengkapkan | `[ISI]` / `[SEMAK]` |
| jv | Peta inti | Rangka | Asil pamriksan | Pilihan irah-irahan | Sing kudu kokjangkepi | `[ISI]` / `[CEK]` |
| su | Peta inti | Rangka | Hasil pamariksaan | Pilihan judul | Nu kudu dilengkepan | `[ISI]` / `[CEK]` |
| es | Mapa central | Esquema | Revisión | Opciones de título | Lo que debes aportar | `[COMPLETAR]` / `[VERIFICAR]` |
| pt | Mapa central | Estrutura | Verificação | Opções de título | O que você precisa fornecer | `[PREENCHER]` / `[VERIFICAR]` |
| fr | Carte centrale | Plan | Vérification | Titres possibles | Ce que tu dois fournir | `[À COMPLÉTER]` / `[À VÉRIFIER]` |
| de | Kernübersicht | Gliederung | Prüfung | Titelvorschläge | Was du ergänzen musst | `[ERGÄNZEN]` / `[PRÜFEN]` |
| it | Mappa centrale | Scaletta | Verifica | Titoli possibili | Cosa devi fornire | `[COMPLETARE]` / `[VERIFICARE]` |
| nl | Kernoverzicht | Opzet | Controle | Titelopties | Wat je moet aanvullen | `[INVULLEN]` / `[CONTROLEREN]` |
| ru | Основная карта | План | Проверка | Варианты названия | Что нужно дополнить | `[ЗАПОЛНИТЬ]` / `[ПРОВЕРИТЬ]` |
| tr | Ana harita | Taslak | Kontrol | Başlık seçenekleri | Tamamlaman gerekenler | `[DOLDUR]` / `[KONTROL ET]` |
| ar | الخريطة الأساسية | المخطط | المراجعة | عناوين مقترحة | ما عليك استكماله | `[أكمل]` / `[تحقق]` |
| fa | نقشهٔ اصلی | طرح کلی | بررسی | عنوان‌های پیشنهادی | آنچه باید تکمیل کنی | `[تکمیل]` / `[بررسی]` |
| hi | मुख्य नक्शा | रूपरेखा | जाँच | शीर्षक विकल्प | आपको क्या जोड़ना है | `[भरें]` / `[जाँचें]` |
| bn | মূল মানচিত্র | রূপরেখা | যাচাই | শিরোনামের বিকল্প | যা আপনাকে পূরণ করতে হবে | `[পূরণ করুন]` / `[যাচাই করুন]` |
| zh | 核心图 | 提纲 | 检查 | 备选标题 | 需要你补充的内容 | `[待填]` / `[待核]` |
| ja | 全体像 | 構成案 | チェック | タイトル案 | ご自身で補う項目 | `[記入]` / `[要確認]` |
| ko | 핵심 지도 | 개요 | 점검 | 제목 후보 | 직접 채워야 할 항목 | `[작성]` / `[확인]` |
| vi | Bản đồ cốt lõi | Dàn ý | Kiểm tra | Phương án tiêu đề | Những gì bạn cần bổ sung | `[ĐIỀN]` / `[KIỂM TRA]` |
| th | แผนที่หลัก | โครงร่าง | การตรวจสอบ | ชื่อเรื่องที่เสนอ | สิ่งที่คุณต้องเติม | `[กรอก]` / `[ตรวจสอบ]` |
| tl | Pangunahing mapa | Balangkas | Pagsusuri | Mga posibleng pamagat | Ang kailangan mong punan | `[PUNAN]` / `[SURIIN]` |

Nama field Tugas / Isi / Bukti / Panjang diterjemahkan dengan cara yang sama
(en: Job / Content / Evidence / Length; ja: 役割 / 内容 / 根拠 / 分量; zh: 作用 / 内容 /
依据 / 篇幅; ar: الوظيفة / المحتوى / الدليل / الطول).

### Bahasa yang tidak ada di tabel

Semua bahasa tetap didukung dengan aturan ini:
1. Terjemahkan keenam label, keempat field, dan dua penanda ke bahasa itu sekali, di awal.
2. Struktur, urutan cek, dan jumlah bagian **tidak berubah**.
3. Istilah akademik yang tidak kamu yakini padanannya: tulis istilah Inggris dalam kurung
   di kemunculan pertama dan tandai `[CEK]` (atau padanan lokal penanda itu).
4. Nama bab mengikuti pedoman kampus atau jurnal user bila ada; terjemahan kerja hanya
   dipakai kalau tidak ada.

## Arah tulisan dan aksara

- **Arab, Ibrani, Persia, Urdu (RTL)** — keluaran Markdown tetap berfungsi; jangan
  menyisipkan penanda arah. Nomor bab tetap angka; hindari tabel yang terlalu lebar
  karena campuran RTL/LTR sulit dibaca.
- **Tionghoa, Jepang, Korea** — hitung panjang dalam **karakter**, bukan kata
  (padanan kasar: 1 kata Inggris ≈ 1,5–2 karakter Tionghoa; 1 halaman Jepang ≈ 400
  karakter dalam genkō yōshi).
- **Thai, Khmer, Lao** — tidak memakai spasi antarkata; panjang dihitung dalam karakter
  atau halaman, jangan dalam kata.
- **Bahasa daerah Indonesia** (Jawa, Sunda, Bugis, Makassar, Bali, dll.) — dipakai di
  beberapa prodi sastra daerah; sering disertai kewajiban abstrak dalam bahasa Indonesia
  dan Inggris, dan kadang aksara daerah. `[CEK: aksara dan jumlah bahasa abstrak]`.
- **Transliterasi Arab-Latin** di PTKIN mengikuti pedoman SKB Menag & Mendikbud;
  halaman pedoman transliterasi masuk bagian awal. `[CEK: versi transliterasi]`.

## Kebiasaan retoris yang berbeda antarbahasa

Ini mengubah **urutan**, jadi penting untuk kerangka:

| Tradisi | Kebiasaan |
|---|---|
| Inggris akademik | klaim di depan (*topic sentence first*); tesis dinyatakan di akhir pendahuluan |
| Indonesia akademik | pengantar melingkar dulu, klaim di akhir paragraf — tetap sah, tapi penguji makin sering menuntut ketegasan di awal |
| Prancis | *problématique* + rencana dua/tiga bagian simetris, diumumkan di akhir pendahuluan |
| Jerman | *Forschungsstand* (status penelitian) sebagai bagian tersendiri sebelum pertanyaan penelitian |
| Jepang | *ki-shō-ten-ketsu* di tulisan umum; naskah ilmiah tetap IMRaD |
| Arab | pembukaan (*muqaddimah*) lebih panjang; pujian pembuka lazim dan tidak dihitung sebagai isi |

Kalau user menulis untuk penguji Indonesia tetapi dalam bahasa Inggris, pakai struktur
pedoman kampusnya dan gaya retoris Inggris — sebut pilihan itu sekali.

## Istilah yang tidak diterjemahkan

Nama dokumen dan tahapan akademik Indonesia dipertahankan walau keluarannya berbahasa
Inggris, dengan penjelasan sekali di kemunculan pertama:

`skripsi` (undergraduate final thesis) · `KKP/KP/PKL` (internship / field practice) ·
`sempro`, `semhas` · `munaqasyah` · `pedoman penulisan` (writing guidelines) ·
`SK` (decree) · `LPJ` (accountability report) · `AD/ART` (statutes and bylaws).

Sebaliknya, istilah teknis Inggris yang sudah mapan di naskah Indonesia
(*machine learning*, *black box testing*, *user acceptance test*) tetap Inggris dan
ditulis miring, sesuai aturan istilah asing di `uajm-format.md`.

## Cek bahasa

| Kode | Cek |
|---|---|
| B1 | Seluruh keluaran memakai satu bahasa, tidak berganti di tengah? |
| B2 | Satu bentuk penanda isian saja dipakai? |
| B3 | Panjang dihitung dengan satuan yang cocok untuk aksaranya? |
| B4 | Istilah dokumen lokal dipertahankan dan dijelaskan sekali? |
| B5 | Kalau bahasa naskah ≠ bahasa pedoman, pilihan gaya retoris disebutkan? |
