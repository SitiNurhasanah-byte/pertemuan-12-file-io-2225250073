def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)

                    if not nim.strip():
                        raise ValueError

                    data.append((nim.strip(), nilai))

                except ValueError:
                    print(f"Baris {nomor} tidak valid: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
        return None

    return data


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI MAHASISWA\n")
        file.write("=====================\n")

        if not data:
            file.write("Tidak ada data valid.\n")
            return

        nilai = [record[1] for record in data]
        jumlah = len(nilai)
        rata_rata = sum(nilai) / jumlah
        minimum = min(nilai)
        maksimum = max(nilai)
        lulus = sum(1 for angka in nilai if angka >= 60)

        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {minimum:.2f}\n")
        file.write(f"Nilai maksimum: {maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {lulus}\n")
        file.write(f"Jumlah tidak lulus: {jumlah - lulus}\n")

        file.write("\nDetail nilai valid:\n")
        for nim, angka in data:
            status = "Lulus" if angka >= 60 else "Tidak lulus"
            file.write(f"{nim},{angka:g},{status}\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data is not None:
    tulis_rekap(output_file, data)
    print(f"Rekap berhasil disimpan ke {output_file}")

    if data:
        nilai = [record[1] for record in data]
        print(f"Jumlah data valid: {len(data)}")
        print(f"Rata-rata: {sum(nilai) / len(nilai):.2f}")
        print(f"Nilai minimum: {min(nilai):.2f}")
        print(f"Nilai maksimum: {max(nilai):.2f}")
        print(f"Jumlah lulus: {sum(1 for angka in nilai if angka >= 60)}")
    else:
        print("Tidak ada data valid untuk dihitung.")