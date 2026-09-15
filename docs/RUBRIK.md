# Rubrik Penilaian

Total 100 poin. Pemeriksaan otomatis (GitHub Actions) **tidak memberi poin** — ia hanya syarat masuk: pekerjaan yang gagal pemeriksaan dinilai setelah diperbaiki, dengan potongan keterlambatan bila melewati tenggat.

---

## A. Kelengkapan & Reproduksibilitas — 15 poin

| Poin | Kriteria |
|---|---|
| 13–15 | Notebook jalan penuh tanpa error, seed ditetapkan, log reproduksibilitas lengkap, identitas terisi, commit rapi |
| 9–12 | Jalan penuh, ada satu-dua kelalaian pencatatan |
| 5–8 | Ada sel yang tidak dijalankan atau error yang dibiarkan |
| 0–4 | Notebook tidak dapat dijalankan ulang |

## B. Kualitas Temuan EDA — 30 poin

Ini komponen terbesar. Yang dinilai adalah **rantai bukti**, bukan jumlah grafik.

| Poin | Kriteria |
|---|---|
| 26–30 | Kelima temuan menyebut angka spesifik dan sel asalnya; implikasinya konkret terhadap preprocessing atau validitas; sekurangnya satu temuan melampaui daftar yang jelas terlihat di kelas |
| 20–25 | Kelima temuan berbukti angka, implikasi sebagian besar konkret |
| 12–19 | Temuan benar tetapi implikasi generik ("perlu ditangani", "harus dibersihkan") |
| 5–11 | Temuan tanpa angka, atau sekadar menarasikan output |
| 0–4 | Kurang dari lima temuan, atau menyalin contoh |

**Penalti ketepatan bahasa:** setiap klaim kausal yang tidak didukung desain eksperimen (*"X menyebabkan churn"*) memotong 3 poin. Klaim asosiatif yang tepat (*"X menunjukkan churn rate lebih tinggi"*) tidak dipotong.

## C. Keputusan Preprocessing — 20 poin

| Poin | Kriteria |
|---|---|
| 17–20 | Setiap keputusan ditautkan ke bukti bernomor; urutan split-lalu-fit benar; pilihan imputasi dan transformasi dijustifikasi dari distribusi, bukan kebiasaan |
| 12–16 | Sebagian besar keputusan berbukti; satu-dua mengikuti kebiasaan tanpa alasan |
| 6–11 | Keputusan disebut tanpa bukti |
| 0–5 | Preprocessing dilakukan sebelum split, atau menghapus kolom tanpa analisis |

## D. Desain Eksperimen & Validitas — 25 poin

| Poin | Kriteria |
|---|---|
| 22–25 | Split stratified, pipeline mencegah kebocoran, baseline dibandingkan, metrik dipilih dengan alasan yang menyebut kondisi data, test set jelas dibuka satu kali, hasil dilaporkan dengan sebaran |
| 16–21 | Desain benar, satu komponen lemah (mis. baseline tidak dibahas) |
| 9–15 | Metrik tidak sesuai kondisi data, atau baseline tidak ada |
| 0–8 | Ada kebocoran di jalur eksperimen yang dilaporkan sebagai hasil |

**Diskualifikasi komponen ini (0 poin):** fitur leakage ikut dilatih pada model yang dilaporkan sebagai hasil. Memakainya di blok demonstrasi tidak termasuk — memang itu tujuannya.

## E. Audit Leakage pada Dataset Penelitian Sendiri — 10 poin

| Poin | Kriteria |
|---|---|
| 9–10 | Menyebut kolom konkret, alasan kecurigaan yang berakar pada proses pengumpulan data, dan cara pembuktian yang bisa dijalankan |
| 6–8 | Menyebut kolom dan alasan, pembuktian masih kabur |
| 3–5 | Pernyataan umum tanpa kolom konkret |
| 0–2 | Menyatakan "tidak ada leakage" tanpa penalaran |

---

## Yang membedakan nilai A dari nilai B

Nilai B diberikan untuk pekerjaan yang **benar**: semua langkah dilakukan, semua angka dilaporkan.

Nilai A menuntut satu hal lagi — **penilaian (judgement)**. Menunjukkan bahwa Anda tahu kapan sebuah aturan tidak berlaku. Contoh yang layak A: menolak membuang outlier dengan alasan domain yang spesifik; menjelaskan mengapa accuracy yang turun justru konsekuensi desain yang benar; menemukan masalah kualitas data yang tidak dibahas di kelas; atau menunjukkan bahwa metrik yang dianjurkan pun kurang tepat untuk dataset penelitian Anda, beserta usulan penggantinya.

---

## Keterlambatan

| Keterlambatan | Pengali |
|---|---|
| ≤ 24 jam | 0,90 |
| 24–72 jam | 0,75 |
| > 72 jam | Dinilai hanya bila ada alasan yang disetujui sebelumnya |
