#!/usr/bin/env python3
"""
Pemeriksa kelengkapan pekerjaan Praktikum EDA.

Menjalankan sembilan pemeriksaan struktural pada notebook dan laporan.
Ini BUKAN penilai. Ia tidak menilai kualitas interpretasi — hanya memastikan
pekerjaan lengkap dan tidak melanggar aturan validitas paling dasar.

Pakai:
    python tools/check_submission.py
    python tools/check_submission.py --notebook lain.ipynb --laporan lain.md

Keluar dengan kode 1 bila ada pemeriksaan yang gagal.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Akar repositori mahasiswa. Default: direktori kerja saat ini, sehingga skrip
# tetap benar baik ketika dijalankan dari dalam repositori
# (python tools/check_submission.py) maupun ketika salinan tepercayanya
# dijalankan dari luar (autograder: python "$CLASSROOM50_BUNDLE_DIR/check_submission.py").
ROOT = Path.cwd()
PLACEHOLDER = re.compile(r"_\(isi\)_|\(isi\)|^\s*$|^-+$|^_+$", re.IGNORECASE)

hasil: list[tuple[bool, str, str]] = []


def cek(ok: bool, judul: str, pesan: str = "") -> bool:
    hasil.append((ok, judul, pesan))
    return ok


def baca(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def isi_kosong(nilai: str) -> bool:
    nilai = nilai.strip().strip("*_` ")
    return not nilai or bool(PLACEHOLDER.match(nilai))


# --------------------------------------------------------------------------- 1
def cek_identitas(readme: str | None) -> None:
    if readme is None:
        cek(False, "Identitas di README", "README.md tidak ditemukan")
        return
    kosong = []
    for label in ("Nama", "NRP", "Username GitHub"):
        m = re.search(rf"\|\s*\*\*{re.escape(label)}\*\*\s*\|([^|]*)\|", readme)
        if m is None or isi_kosong(m.group(1)):
            kosong.append(label)
    cek(
        not kosong,
        "Identitas di README terisi",
        f"belum diisi: {', '.join(kosong)}" if kosong else "",
    )


# ------------------------------------------------------------------------- 2-3
def muat_notebook(path: Path):
    teks = baca(path)
    if teks is None:
        cek(False, "Notebook ditemukan dan valid", f"{path} tidak ditemukan")
        return None
    try:
        nb = json.loads(teks)
    except json.JSONDecodeError as e:
        cek(False, "Notebook ditemukan dan valid", f"JSON rusak: {e}")
        return None
    cek(True, "Notebook ditemukan dan valid")
    return nb


def sel_kode(nb):
    return [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]


def cek_dijalankan(nb) -> None:
    belum = [
        i
        for i, c in enumerate(sel_kode(nb), 1)
        if "".join(c.get("source", [])).strip() and c.get("execution_count") is None
    ]
    cek(
        not belum,
        "Notebook sudah dijalankan (output tersimpan)",
        f"{len(belum)} sel kode belum dijalankan. Runtime -> Run all, simpan, push ulang."
        if belum
        else "",
    )


def cek_tanpa_error(nb) -> None:
    err = []
    for i, c in enumerate(sel_kode(nb), 1):
        for out in c.get("outputs", []):
            if out.get("output_type") == "error":
                err.append(f"sel {i}: {out.get('ename', 'Error')}")
    cek(not err, "Tidak ada sel yang error", "; ".join(err[:3]))


# ------------------------------------------------------------------------- 4-7
def _kode(nb) -> str:
    return "\n".join("".join(c.get("source", [])) for c in sel_kode(nb))


def cek_leakage(nb) -> None:
    ada = re.search(r"DROP\s*=\s*\[[^\]]*churn_next_month_confirmed", _kode(nb))
    cek(
        bool(ada),
        "Fitur leakage dikeluarkan dari model final",
        "'churn_next_month_confirmed' harus ada di daftar DROP sebelum split. "
        "Memakainya di blok demonstrasi tidak masalah; memakainya di model yang "
        "dilaporkan sebagai hasil tidak boleh."
        if not ada
        else "",
    )


def cek_stratify(nb) -> None:
    ada = re.search(r"train_test_split\s*\([^)]*stratify\s*=", _kode(nb), re.DOTALL)
    cek(
        bool(ada),
        "train_test_split memakai stratify",
        "Data tidak seimbang; split tanpa stratify membuat proporsi kelas bergeser."
        if not ada
        else "",
    )


def cek_testset(nb) -> None:
    bocor = re.findall(r"\.fit(?:_transform)?\s*\(\s*X_test", _kode(nb))
    cek(
        not bocor,
        "Tidak ada fit/fit_transform pada X_test",
        f"ditemukan {len(bocor)} kali. Test set tidak boleh dipakai melatih apa pun, "
        "termasuk imputer dan scaler."
        if bocor
        else "",
    )


def cek_seed(nb) -> None:
    ada = re.search(r"RANDOM_STATE\s*=\s*\d+", _kode(nb))
    cek(bool(ada), "RANDOM_STATE ditetapkan", "" if ada else "Hasil tidak dapat direproduksi tanpa seed.")


# ------------------------------------------------------------------------- 8-9
def _teks_laporan(path: Path) -> str | None:
    return baca(path)


def cek_temuan(path: Path) -> None:
    teks = _teks_laporan(path)
    if teks is None:
        cek(False, "Minimal 5 temuan EDA lengkap (Temuan/Bukti/Implikasi)", f"{path} tidak ditemukan")
        return

    blok = re.split(r"^###\s+Temuan\s+\d+\s*$", teks, flags=re.MULTILINE)[1:]
    lengkap, catatan = 0, []
    for n, b in enumerate(blok, 1):
        b = re.split(r"^##\s+", b, flags=re.MULTILINE)[0]
        kurang = []
        for label in ("Temuan", "Bukti", "Implikasi"):
            m = re.search(rf"\*\*{label}:\*\*(.*?)(?=\n\s*\*\*|\Z)", b, re.DOTALL)
            if m is None or len(m.group(1).strip().strip("_*` ")) < 15:
                kurang.append(label)
        if kurang:
            catatan.append(f"Temuan {n} kurang: {'/'.join(kurang)}")
        else:
            lengkap += 1
    cek(
        lengkap >= 5,
        "Minimal 5 temuan EDA lengkap (Temuan/Bukti/Implikasi)",
        f"baru {lengkap} dari 5 lengkap. " + "; ".join(catatan[:3]) if lengkap < 5 else "",
    )


def cek_audit(path: Path) -> None:
    teks = _teks_laporan(path)
    if teks is None:
        cek(False, "Audit leakage dataset penelitian terisi", f"{path} tidak ditemukan")
        return
    m = re.search(r"##\s*Bagian 3(.*?)(?=^##\s|\Z)", teks, re.DOTALL | re.MULTILINE)
    isi = ""
    if m:
        isi = re.sub(r"_\(tulis di sini\)_", "", m.group(1))
        isi = re.sub(r"^>.*$", "", isi, flags=re.MULTILINE)          # buang kutipan instruksi
        isi = re.sub(r"^Satu paragraf utuh\..*$", "", isi, flags=re.MULTILINE)
        isi = re.sub(r"[#*_`|-]", " ", isi)
    jml = len([w for w in isi.split() if len(w) > 1])
    cek(
        jml >= 40,
        "Audit leakage dataset penelitian terisi",
        f"baru {jml} kata, minimal 40. Sebutkan kolom konkret, alasan kecurigaan, "
        "dan cara pembuktiannya."
        if jml < 40
        else "",
    )


# --------------------------------------------------------------------------- #
PEMERIKSAAN = {
    "identitas":  "identitas di README",
    "notebook":   "notebook valid",
    "dijalankan": "notebook sudah dijalankan",
    "error":      "tidak ada sel error",
    "leakage":    "fitur leakage dikeluarkan dari model final",
    "stratify":   "split memakai stratify",
    "testset":    "test set tidak dipakai untuk fit",
    "seed":       "RANDOM_STATE ditetapkan",
    "temuan":     "5 temuan EDA lengkap",
    "audit":      "audit leakage terisi",
}


def main() -> int:
    p = argparse.ArgumentParser(
        description="Pemeriksa kelengkapan Praktikum EDA",
        epilog="Kunci --only: " + ", ".join(PEMERIKSAAN),
    )
    p.add_argument("--notebook", default="notebooks/praktikum01_eda.ipynb")
    p.add_argument("--laporan", default="laporan/LAPORAN.md")
    p.add_argument("--readme", default="README.md")
    p.add_argument(
        "--root",
        metavar="DIR",
        help="akar repositori yang diperiksa (default: direktori kerja saat ini)",
    )
    p.add_argument(
        "--only",
        metavar="KUNCI",
        help="jalankan satu pemeriksaan saja (untuk autograder per-tes)",
    )
    p.add_argument("--daftar", action="store_true", help="tampilkan semua kunci --only lalu keluar")
    a = p.parse_args()

    global ROOT
    if a.root:
        ROOT = Path(a.root).resolve()

    if a.daftar:
        for k, v in PEMERIKSAAN.items():
            print(f"{k:12s} {v}")
        return 0

    if a.only and a.only not in PEMERIKSAAN:
        print(f"Kunci '{a.only}' tidak dikenal. Pilihan: {', '.join(PEMERIKSAAN)}")
        return 2

    pilih = (lambda k: a.only in (None, k))

    butuh_nb = any(pilih(k) for k in ("notebook", "dijalankan", "error", "leakage", "stratify", "testset", "seed"))

    if pilih("identitas"):
        cek_identitas(baca(ROOT / a.readme))

    nb = None
    if butuh_nb:
        nb = muat_notebook(ROOT / a.notebook)
        if a.only and a.only != "notebook" and nb is not None:
            hasil.pop()  # hasil "notebook valid" hanya relevan pada mode penuh
    if nb is not None:
        if pilih("dijalankan"):
            cek_dijalankan(nb)
        if pilih("error"):
            cek_tanpa_error(nb)
        if pilih("leakage"):
            cek_leakage(nb)
        if pilih("stratify"):
            cek_stratify(nb)
        if pilih("testset"):
            cek_testset(nb)
        if pilih("seed"):
            cek_seed(nb)

    if pilih("temuan"):
        cek_temuan(ROOT / a.laporan)
    if pilih("audit"):
        cek_audit(ROOT / a.laporan)

    lolos = sum(1 for ok, _, _ in hasil if ok)
    total = len(hasil)

    if a.only:
        ok, judul, pesan = hasil[-1] if hasil else (False, a.only, "pemeriksaan tidak berjalan")
        print(f"{'PEMERIKSAAN_LOLOS' if ok else 'PEMERIKSAAN_GAGAL'} — {judul}")
        if pesan:
            print(f"  -> {pesan}")
        return 0 if ok else 1

    baris = ["", f"PEMERIKSAAN KELENGKAPAN — {lolos}/{total} lolos", "=" * 58]
    for ok, judul, pesan in hasil:
        baris.append(f"{'[ OK ]' if ok else '[GAGAL]'} {judul}")
        if pesan:
            baris.append(f"        -> {pesan}")
    baris.append("=" * 58)
    baris.append(
        "Semua pemeriksaan lolos. Ini syarat kelengkapan, bukan nilai Anda — "
        "kualitas interpretasi dinilai terpisah (lihat docs/RUBRIK.md)."
        if lolos == total
        else "Perbaiki butir yang GAGAL lalu push ulang."
    )
    print("\n".join(baris))

    ringkasan = os.environ.get("GITHUB_STEP_SUMMARY")
    if ringkasan:
        with open(ringkasan, "a", encoding="utf-8") as f:
            f.write(f"## Pemeriksaan kelengkapan — {lolos}/{total} lolos\n\n")
            f.write("| Status | Pemeriksaan | Catatan |\n|---|---|---|\n")
            for ok, judul, pesan in hasil:
                f.write(f"| {'✅' if ok else '❌'} | {judul} | {pesan or '—'} |\n")

    return 0 if lolos == total else 1


if __name__ == "__main__":
    sys.exit(main())
