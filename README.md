# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Siti Nurhasanah  
**NIM:** 2225250073  
**Kelas:** 3 B

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input

Format data pada file `data/nilai.txt`:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Setiap baris terdiri atas:

```text
NIM,nilai
```

## Cara Menjalankan

Buka terminal pada folder proyek, lalu jalankan:

```bash
python tugas/rekap_nilai_file.py
```

atau

```bash
python3 tugas/rekap_nilai_file.py
```

## Error yang Ditangani

### 1. FileNotFoundError

Terjadi apabila file `data/nilai.txt` tidak ditemukan.

Contoh keluaran:

```text
File tidak ditemukan: data/nilai.txt
```

### 2. ValueError

Terjadi apabila nilai tidak dapat dikonversi menjadi angka.

Contoh data:

```text
A004,abc
```

Contoh keluaran:

```text
Baris 4 dilewati: A004,abc
```

Program tetap melanjutkan proses untuk data lainnya.

## Test Case

| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|----------|----------------------|-------------|---------|
| Semua data valid | Semua data diproses dan rekap dibuat | Semua data berhasil diproses | ✅ |
| File tidak ditemukan | Program menampilkan pesan error dan tidak crash | Sesuai | ✅ |
| Ada nilai invalid (abc) | Data invalid dilewati | Sesuai | ✅ |
| Ada baris kosong | Baris kosong dilewati | Sesuai | ✅ |
| Nilai 60 | Dihitung sebagai lulus | Sesuai | ✅ |

## Contoh Hasil Rekap

File `data/hasil_rekap.txt`:

```text
Jumlah data valid: 5
Rata-rata: 83.40
Minimum: 74.00
Maksimum: 92.00
Jumlah lulus: 5
```

## Refleksi

Saat mengerjakan tugas ini ditemukan error `ValueError` karena terdapat data yang tidak sesuai format angka, yaitu:

```text
A004,abc
```

Program menangani error tersebut menggunakan `try-except ValueError`, sehingga baris yang tidak valid dapat dilewati tanpa menghentikan keseluruhan proses. Dengan cara ini data lain yang valid tetap dapat dibaca, dihitung, dan ditulis ke file rekap.
