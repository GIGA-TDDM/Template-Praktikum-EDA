# Data Card — `customer_churn_eda.csv`

## Ringkas

| | |
|---|---|
| **Nama** | `customer_churn_eda.csv` |
| **Jenis** | **Data sintetis**, dibangkitkan untuk keperluan pengajaran |
| **Ukuran** | 3.012 baris × 15 kolom |
| **Unit analisis** | Satu baris = satu pelanggan |
| **Target** | `churn` (0 = tidak churn, 1 = churn) |
| **Lisensi** | CC BY-SA 4.0, mengikuti lisensi materi repositori |

## Peringatan penggunaan

Dataset ini **tidak merepresentasikan populasi pelanggan nyata mana pun**. Angka-angkanya dibangkitkan secara sintetis. Karena itu:

- Dataset ini **tidak boleh** dipakai sebagai dasar klaim empiris, rekomendasi bisnis, atau temuan penelitian.
- Dataset ini **tidak boleh** dipakai sebagai benchmark untuk membandingkan metode.
- Dataset ini **hanya** sah dipakai untuk melatih keterampilan EDA, preprocessing, dan pemeriksaan validitas eksperimen.

Dataset sengaja dirancang mengandung sejumlah masalah kualitas data yang harus Anda temukan sendiri melalui EDA. Daftar masalahnya tidak dicantumkan di sini — menemukannya adalah inti praktikum.

## Skema

| Kolom | Tipe | Keterangan |
|---|---|---|
| `customer_id` | string | Identifier pelanggan |
| `age` | int | Umur (tahun) |
| `monthly_income` | float | Pendapatan bulanan (Rupiah) |
| `tenure_months` | float | Lama menjadi pelanggan (bulan) |
| `monthly_spend` | float | Pengeluaran bulanan (Rupiah) |
| `transactions_per_month` | int | Jumlah transaksi per bulan |
| `support_tickets` | int | Jumlah tiket bantuan |
| `satisfaction_score` | float | Skor kepuasan, skala 1–5 |
| `city` | string | Kota |
| `segment` | string | Segmen pelanggan (Basic / Silver / Gold) |
| `channel` | string | Kanal layanan (App / Web / Branch) |
| `premium_member` | int | Status keanggotaan premium (0/1) |
| `annual_spend` | float | Pengeluaran tahunan (Rupiah) |
| `churn_next_month_confirmed` | int | Status churn terkonfirmasi (0/1) |
| `churn` | int | **Target** (0/1) |

Perhatikan: tabel di atas mendaftar kolom **apa adanya**. Ia tidak menyatakan bahwa semua kolom layak dipakai sebagai fitur. Menilai kelayakan setiap kolom adalah pekerjaan Anda di Blok 2 dan Blok 8.

## Integritas berkas

Jangan mengubah berkas ini. Semua pembersihan dilakukan di dalam notebook agar setiap langkah terekam dan dapat direproduksi. Bila Anda tidak sengaja mengubahnya:

```bash
git checkout -- data/customer_churn_eda.csv
```
