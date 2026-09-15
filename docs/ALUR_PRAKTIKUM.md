# Alur Praktikum — 13 Blok

Peta ini menjelaskan **maksud** setiap blok notebook, bukan jawabannya. Bacalah sebelum sesi agar Anda tahu ke mana arah kelas malam ini.

---

## Tahap 1 — Muat dan periksa (Blok 0–2, ±18 menit)

| Blok | Isi | Pertanyaan yang harus Anda jawab |
|---|---|---|
| **0** | Setup, versi library, `RANDOM_STATE`, muat dataset | Mengapa mencatat versi dan seed adalah syarat minimum reproduksibilitas, bukan formalitas? |
| **1** | Struktur dataset: jumlah baris, kolom, nilai unik | Satu baris di dataset ini merepresentasikan apa? |
| **2** | Data dictionary: dtype, cardinality, missing | Mana kolom yang **tidak boleh** jadi fitur input, dan mengapa? |

Konsep kunci: **file type vs semantic type**. Sebuah kolom bisa bertipe `int64` tetapi maknanya kategori. Selisih ini adalah sumber kesalahan preprocessing paling umum.

---

## Tahap 2 — Temukan cacat (Blok 3–6, ±25 menit)

| Blok | Isi | Pertanyaan yang harus Anda jawab |
|---|---|---|
| **3** | Missing values dan analisis missingness | Bukan "berapa persen hilang", tetapi **mengapa** hilang — MCAR, MAR, atau MNAR? |
| **4** | Duplikat dan inkonsistensi kategori | Mengapa normalisasi string boleh sebelum split, tetapi imputasi tidak? |
| **5** | Distribusi target dan statistik deskriptif | Dua angka di blok ini menentukan seluruh desain eksperimen. Yang mana? |
| **6** | Outlier dengan aturan IQR | Kapan outlier layak dibuang, dan kapan membuangnya justru merusak populasi penelitian? |

Konsep kunci: **preprocessing leakage**. Transformasi yang *belajar dari data* (median, mean, skala, kategori) harus dihitung **hanya dari data latih**. Transformasi deterministik (mengubah huruf besar-kecil) aman kapan saja.

---

## Tahap 3 — Bukti jadi keputusan (Blok 7–9, ±25 menit)

| Blok | Isi | Pertanyaan yang harus Anda jawab |
|---|---|---|
| **7** | Bivariate: fitur terhadap target | Mana kalimat yang boleh Anda tulis, dan mana yang melampaui bukti? |
| **8** | Korelasi — menemukan *redundant feature* dan *leakage* | Ada nilai yang terlalu bagus untuk jadi kenyataan. Apa artinya? |
| **9** | Tabel keputusan preprocessing dan split | Bisakah setiap baris keputusan Anda ditunjuk nomor buktinya? |

Konsep kunci: **EDA menghasilkan asosiasi, bukan kausalitas.** Kalimat kausal menuntut desain eksperimen yang sama sekali berbeda. Bila kalimat kausal muncul di laporan tanpa desain itu, penguji akan menghantam tepat di situ.

Konsep kunci kedua: **deteksi leakage bukan pekerjaan statistik.** Ia dijawab dengan pertanyaan domain — *pada saat prediksi harus dibuat, apakah nilai kolom ini sudah tersedia?*

---

## Tahap 4 — Pipeline dan uji (Blok 10–11, ±27 menit)

| Blok | Isi | Pertanyaan yang harus Anda jawab |
|---|---|---|
| **10** | `ColumnTransformer`, `Pipeline`, baseline `DummyClassifier` | Mengapa Pipeline adalah alat penjaga validitas, bukan sekadar kerapian kode? |
| **11** | Cross-validation, lalu evaluasi final di test set | Mengapa accuracy model bisa berada **di bawah** baseline dan itu tetap benar? |

Konsep kunci: **baseline menentukan apakah kontribusi Anda nyata.** Pada data tidak seimbang, menebak kelas mayoritas sudah memberi akurasi tinggi. Angka yang tidak dibandingkan dengan baseline tidak bermakna apa-apa.

Konsep kunci kedua: **test set dikunci** sejak split sampai evaluasi akhir. Melihat test set lalu mengubah model membuat angka akhir Anda bukan lagi estimasi generalisasi, melainkan hasil tuning.

---

## Tahap 5 — Bongkar leakage (Blok 12–13, ±10 menit)

| Blok | Isi | Pertanyaan yang harus Anda jawab |
|---|---|---|
| **12** | Demonstrasi: apa yang terjadi bila fitur leakage ikut dilatih | Mengapa cross-validation **tidak** menyelamatkan Anda di sini? |
| **13** | Reproducibility log | Apa yang harus dicatat agar orang lain bisa mengulang hasil Anda? |

Ini puncak sesi. Satu perubahan kecil — memasukkan kembali satu kolom — dan seluruh metrik berubah total. Anda akan melihat sendiri bahwa cross-validation pun menunjukkan angka sempurna, karena CV melindungi dari *overfitting*, bukan dari kebocoran informasi masa depan.

> Bila suatu hari model Anda tiba-tiba mendapat AUC mendekati sempurna pada data nyata, reaksi pertama yang benar bukan menulis paper. Reaksi pertama yang benar adalah **mencari leakage**.

---

## Lima kalimat yang dibawa pulang

1. EDA adalah proses mengumpulkan bukti, bukan membuat grafik.
2. Setiap keputusan preprocessing harus dapat ditunjuk buktinya.
3. Split sebelum preprocessing yang belajar dari data; test set dikunci.
4. Accuracy pada data tidak seimbang menyesatkan ke dua arah — bandingkan selalu dengan baseline.
5. Nilai terlalu sempurna adalah gejala, bukan prestasi.
