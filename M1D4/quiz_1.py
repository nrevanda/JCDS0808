# Diberikan data mahasiswa dalam bentuk list of tuple.
# Setiap tuple berisi: (nama, nilai)

mahasiswa = [
    ("Ani", 80),
    ("Budi", 70),
    ("Citra", 85),
    ("Dedi", 65),
    ("Eka", 90)
]

# TUGAS:
# 1. Cetak nama mahasiswa yang memiliki nilai di atas 75.
# 2. Hitung dan cetak rata-rata nilai dari semua mahasiswa.

# 1. Cetak mahasiswa dengan nilai > 75:
nilai_75 = []
for nama, nilai in mahasiswa:
    if nilai > 75:
        nilai_75.append(nama)
print(f"mahasiswa yang mendapat nilai >75 adalah {nilai_75}")


# 2. Hitung rata-rata nilai mahasiswa:
print()
jumlah_nilai = 0
for nama, nilai in mahasiswa:
    jumlah_nilai += nilai
avg = jumlah_nilai/ len(mahasiswa)

print(f"jumlah nilai {len(mahasiswa)} mahasiswa adalah {jumlah_nilai} sehingga rata-rata nya adalah {avg}")



