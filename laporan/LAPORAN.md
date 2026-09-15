# Laporan Praktikum EDA

| | |
|---|---|
| **Nama** | _(isi)_ |
| **NRP** | _(isi)_ |
| **Tanggal** | _(isi)_ |

---

## Bagian 1 — Lima Temuan EDA

Format wajib setiap temuan: **Temuan → Bukti → Implikasi**.
Bukti harus menyebut angka konkret dan blok/sel asalnya. Implikasi harus menyebut konsekuensi terhadap preprocessing atau validitas — bukan sekadar "perlu diperhatikan".

Contoh yang benar (jangan dihapus, pakai sebagai acuan):

> **Temuan:** Kelas target tidak seimbang.
> **Bukti:** Blok 5, `value_counts(normalize=True)` → 82.1% : 17.9%.
> **Implikasi:** Accuracy tidak dipakai sebagai metrik utama karena baseline mayoritas sudah 0.82; split memakai `stratify=y`; metrik utama PR-AUC.

### Temuan 1

**Temuan:**
**Bukti:**
**Implikasi:**

### Temuan 2

**Temuan:**
**Bukti:**
**Implikasi:**

### Temuan 3

**Temuan:**
**Bukti:**
**Implikasi:**

### Temuan 4

**Temuan:**
**Bukti:**
**Implikasi:**

### Temuan 5

**Temuan:**
**Bukti:**
**Implikasi:**

---

## Bagian 2 — Tabel Keputusan Preprocessing (dataset penelitian Anda sendiri)

Bukan dataset churn praktikum. Pakai dataset kandidat penelitian Anda.

**Nama dataset:**
**Sumber / cara perolehan:**
**Ukuran (baris × kolom):**
**Target dan definisinya:**

| Keputusan | Bukti dari EDA | Alasan |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

---

## Bagian 3 — Audit Leakage pada Dataset Penelitian Anda

Satu paragraf utuh. Jawab tiga hal: kolom mana yang berpotensi bocor, mengapa Anda menduganya, dan bagaimana Anda membuktikan atau menyangkalnya. Bila Anda yakin tidak ada leakage, tetap tulis bagaimana Anda sampai pada keyakinan itu — pertanyaan kuncinya: *pada saat prediksi harus dibuat, apakah nilai kolom ini sudah tersedia?*

_(tulis di sini)_

---

## Bagian 4 — Refleksi Singkat

Satu hal yang berubah dalam cara Anda memandang data setelah sesi ini:

_(tulis di sini)_

---

## Bagian 5 — Penggunaan Bantuan AI

Sebutkan alat yang Anda pakai dan untuk bagian apa. Menggunakan AI diperbolehkan; tidak menyebutkannya tidak.

| Alat | Dipakai untuk bagian | Apa yang Anda verifikasi sendiri |
|---|---|---|
| | | |
