# Debuging
# Rekap Gaji Mingguan Pegawai Shift

# Deskripsi 
# Program ini bertujuan untuk:
# 1. Meminta input nama pegawai, jumlah hari kerja, dan tarif per jam.
# 2. Untuk setiap hari, meminta input jumlah jam kerja.
# 3. Jika jam kerja == 0, hari dianggap libur → continue
# 4. Jika jam kerja > 12, program dihentikan karena overload → break
# 5. Jika jam kerja > 8 tapi ≤ 12, dianggap lembur, kelebihan jam dikali tarif 1.5×
# 6. Total gaji dihitung dan ditampilkan di akhir program

print("=== PROGRAM REKAP GAJI MINGGUAN v3 ===")

nama = input("Masukkan nama pegawai: ")
hari_kerja = int(input("Jumlah hari kerja minggu ini: "))
tarif_per_jam = float(input("Tarif per jam (contoh: 20000): "))

gaji_total = 0
hari = 1

while hari <= hari_kerja:
    print("Hari ke-", hari)
    jam_kerja = int(input("Masukkan jumlah jam kerja: "))

    if jam_kerja == "0":
        print("Hari libur. Lanjut ke hari berikutnya.\n")
        continue

    elif jam_kerja > 12:
        print("Jam kerja melebihi batas maksimum! Program dihentikan.\n")
        break

    elif jam_kerja > 8 and jam_kerja <= 12:
        lembur = jam_kerja
        gaji_harian = (tarif_per_jam * 8) + (tarif_per_jam * 1.5 * lembur)
    else:
        gaji_harian = tarif_per_jam * jam_kerja

    hari += 1
    gaji_total += gaji_harian 


print(f"Total gaji minggu ini untuk", {nama.upper()}, "adalah Rp", gaji_total)
