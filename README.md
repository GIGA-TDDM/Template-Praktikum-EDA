# Praktikum EDA — Topik Dalam Data Mining

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GIGA-TDDM/Template-Praktikum-EDA/blob/main/notebooks/praktikum01_eda.ipynb)
[![Repo](https://img.shields.io/badge/GitHub-GIGA--TDDM%2FTemplate--Praktikum--EDA-181717?logo=github)](https://github.com/GIGA-TDDM/Template-Praktikum-EDA)
[![Pemeriksaan](https://github.com/GIGA-TDDM/Template-Praktikum-EDA/actions/workflows/check-submission.yml/badge.svg)](https://github.com/GIGA-TDDM/Template-Praktikum-EDA/actions/workflows/check-submission.yml)

**EF235161 — Topik Dalam Data Mining (P) · S-2 Teknik Informatika · ITS**
Exploratory Data Analysis, Data Preprocessing & Experimental Validity · Sesi 120 menit

---

## Identitas

Isi tabel ini lebih dulu, lalu commit. Ini bagian pertama yang diperiksa.

| | |
|---|---|
| **Nama** | _(isi)_ |
| **NRP** | _(isi)_ |
| **Username GitHub** | _(isi)_ |

---

## Yang akan Anda kerjakan

| | Tahap | Waktu | Inti |
|---|---|---|---|
| 1 | **Muat dan periksa** | 18 menit | Satu baris data ini merepresentasikan apa? |
| 2 | **Temukan cacat** | 25 menit | Missing, duplikat, inkonsistensi, outlier, imbalance |
| 3 | **Bukti jadi keputusan** | 25 menit | Setiap keputusan preprocessing harus punya nomor bukti |
| 4 | **Pipeline dan uji** | 27 menit | Split, ColumnTransformer, baseline, cross-validation |
| 5 | **Bongkar leakage** | 10 menit | AUC 0.717 yang jujur vs AUC 1.000 yang bocor |

Dataset `data/customer_churn_eda.csv` **sengaja dibuat cacat**. Tugas Anda bukan memperbaikinya sampai bersih, melainkan **menemukan cacatnya lewat bukti** lalu mempertanggungjawabkan setiap keputusan yang Anda ambil.

> Pesan utama praktikum ini: *EDA bukan kegiatan membuat grafik. EDA adalah proses mengumpulkan bukti untuk mengambil keputusan preprocessing dan menjaga validitas eksperimen.*

---

## Mulai — pilih satu jalur

### Jalur A — Google Colab (dianjurkan, tanpa instalasi)

1. Klik badge **Open In Colab** di atas.
2. Di Colab: **File → Save a copy in GitHub**, pilih repositori ini, centang *Include a link to Colab*.
3. Kerjakan. Setiap kali ingin menyimpan, ulangi langkah 2 — itulah cara Anda melakukan commit dari Colab.

Notebook memuat dataset secara otomatis: dicoba dari folder lokal dulu, lalu dari repositori ini via URL, dan terakhir lewat dialog upload. Anda tidak perlu mengatur apa pun.

Bila Anda ingin bekerja langsung di dalam klon repositori Anda sendiri di Colab, jalankan sel pertama notebook lalu:

```python
!git clone https://github.com/GIGA-TDDM/Template-Praktikum-EDA.git
%cd Template-Praktikum-EDA
```

### Jalur B — Lokal (Jupyter)

```bash
git clone https://github.com/GIGA-TDDM/Template-Praktikum-EDA.git
cd Template-Praktikum-EDA
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab notebooks/praktikum01_eda.ipynb
```

### Jalur C — GitHub Codespaces

**Code → Codespaces → Create codespace on main**, lalu `pip install -r requirements.txt`.

---

## Isi repositori

```
.
├── notebooks/praktikum01_eda.ipynb   <- kerjakan di sini
├── laporan/LAPORAN.md                <- dan di sini
├── data/
│   ├── customer_churn_eda.csv        <- dataset praktikum (jangan diubah)
│   └── DATA_CARD.md                  <- asal-usul, skema, batas penggunaan
├── docs/
│   ├── ALUR_PRAKTIKUM.md             <- rangkuman 13 blok beserta maksudnya
│   └── RUBRIK.md                     <- dasar penilaian
├── tools/check_submission.py         <- pemeriksa yang dijalankan CI
├── outputs/                          <- simpan gambar/artefak di sini
└── requirements.txt
```

---

## Deliverable

1. **`notebooks/praktikum01_eda.ipynb`** — dijalankan penuh dari atas ke bawah, output tersimpan, setiap blok diberi satu kalimat interpretasi.
2. **`laporan/LAPORAN.md`** — berisi:
   - minimal **5 temuan EDA** berformat **Temuan → Bukti → Implikasi**;
   - **tabel keputusan preprocessing** untuk dataset penelitian Anda sendiri;
   - **satu paragraf audit leakage** pada dataset penelitian Anda.
3. Commit dan push sebelum tenggat. Yang dinilai adalah commit terakhir sebelum tenggat.

---

## Pemeriksaan otomatis

Setiap kali Anda push, GitHub Actions menjalankan `tools/check_submission.py`. Hasilnya muncul sebagai centang hijau atau silang merah di halaman repositori, dan rinciannya ada di tab **Actions**.

Yang diperiksa:

| # | Pemeriksaan |
|---|---|
| 1 | Identitas di README sudah diisi |
| 2 | Notebook valid dan **benar-benar sudah dijalankan** (bukan sekadar disimpan) |
| 3 | Tidak ada sel yang error |
| 4 | `churn_next_month_confirmed` dikeluarkan dari fitur model final |
| 5 | `train_test_split` memakai `stratify` |
| 6 | Tidak ada `fit` atau `fit_transform` yang menyentuh `X_test` |
| 7 | `RANDOM_STATE` ditetapkan |
| 8 | Minimal 5 temuan EDA terisi, masing-masing punya Bukti dan Implikasi |
| 9 | Paragraf audit leakage terisi memadai |

**Pemeriksaan ini bukan nilai Anda.** Ia hanya memastikan pekerjaan Anda lengkap dan tidak melanggar aturan validitas yang paling dasar. Centang hijau penuh tetap bisa berujung nilai sedang bila interpretasi Anda dangkal — dan itulah yang sebenarnya dinilai. Lihat `docs/RUBRIK.md`.

Menjalankan pemeriksa di komputer sendiri sebelum push:

```bash
python tools/check_submission.py
```

---

## Aturan

- Dataset di `data/` **tidak boleh diubah**. Semua pembersihan dilakukan di dalam notebook.
- Test set dikunci setelah split. Tidak dilihat, tidak dipakai memilih model, dibuka satu kali di akhir.
- Kolom leakage **boleh** dipakai di blok demonstrasi (Blok 12) — memang itu tujuannya. Ia **tidak boleh** ikut di model yang Anda laporkan sebagai hasil.
- Boleh berdiskusi; notebook dan laporan dikerjakan sendiri. Sebutkan bantuan AI yang Anda pakai beserta bagian mana, di bagian akhir `laporan/LAPORAN.md`.

---

## Bila macet

| Gejala | Tindakan |
|---|---|
| `FileNotFoundError` dataset | Jalankan ulang sel pemuat data; ia punya tiga lapis fallback |
| `ModuleNotFoundError` di Colab | `%pip install -q imbalanced-learn` lalu **Runtime → Restart session** |
| `ValueError: Input contains NaN` | Imputer belum masuk pipeline, atau Anda `fit` di luar pipeline |
| `Unknown category` saat test | Pastikan `OneHotEncoder(handle_unknown="ignore")` |
| Performa tiba-tiba ~1.00 | Cari leakage. Ini gejala, bukan prestasi |
| Notebook tidak lolos cek "sudah dijalankan" | **Runtime → Run all**, simpan, lalu push ulang |

---

## Lisensi & atribusi

Materi: CC BY-SA 4.0. Kode di `tools/`: MIT. Lihat `LICENSE`.
Dataset `customer_churn_eda.csv` adalah **data sintetis untuk pembelajaran** — tidak boleh dipakai sebagai dasar klaim empiris apa pun. Lihat `data/DATA_CARD.md`.

Disiapkan oleh GIGA ITS Lab, Departemen Teknik Informatika, Institut Teknologi Sepuluh Nopember.
