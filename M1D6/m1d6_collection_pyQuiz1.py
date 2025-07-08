# =====================================================
# Code Completion
# Program Analisis Nilai Siswa
# =====================================================
# Deskripsi:
# Program ini menerima daftar nilai dari pengguna,
# lalu menggunakan beberapa fungsi untuk:
# 1. Menghitung rata-rata
# 2. Menentukan grade berdasarkan skor
# 3. Menyimpulkan hasil akhir
#
# Lengkapi bagian yang kosong agar program dapat berjalan.

def hitung_rata_rata(nilai_list):
    total = 0
    for n in nilai_list:
        total += n
    return total / len(nilai_list)

def tentukan_grade(rata2):
    if rata2 >= 85:
        return "A"
    elif rata2 >= 75:
        return "B"
    elif rata2 >= 65:
        return "C"
    else:
        return "D"

# TODO: Fungsi untuk menyimpulkan status lulus/tidak
def evaluasi_akhir(rata2, grade):
    print(f"Rata-rata nilai: {rata2}")
    print(f"Grade: {grade}")
    if grade in ["A", "B"]:
        print("Status: LULUS")
    else:
        print("Status: TIDAK LULUS")

# # TODO: Ambil 5 nilai siswa
print("Masukkan 5 nilai siswa:")
nilai_siswa = []
for i in range(5):
    nilai = int(input(f"Nilai ke-{i+1}: "))
    nilai_siswa.append(nilai)

# TODO: Hitung rata-rata
rata2 = hitung_rata_rata(nilai_siswa)

# TODO: Tentukan grade
grade = tentukan_grade(rata2)

# TODO: Evaluasi akhir
evaluasi_akhir(rata2, grade)
