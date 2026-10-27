with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if not baris:
            continue

        try:
            nim, teks_nilai = baris.split(",")
            nilai = float(teks_nilai)
            print(nim, nilai)
        except ValueError:
            print(f"Data tidak valid: {baris}")