# =====================================================
# BUAT PROGRAM
# PROGRAM MANAJEMEN INVENTARIS GUDANG
# =====================================================

# Deskripsi:
# Program ini digunakan untuk mencatat, menghitung, dan mengevaluasi
# data barang dalam gudang. Setiap barang memiliki:
# - nama barang
# - jumlah stok
# - harga per unit

# Fitur Program:
# 1. Tambah data barang:
#    - Meminta input nama, stok, dan harga barang
#    - Menyimpan ke dalam daftar inventaris

# 2. Hitung total nilai inventaris:
#    - Total = jumlah stok × harga untuk semua barang

# 3. Tampilkan barang dengan stok rendah (< 10):
#    - Menampilkan daftar barang dengan stok di bawah 10 unit

# 4. Cari barang termahal:
#    - Menentukan barang dengan harga tertinggi
#    - Gunakan fungsi `max()` dan lambda expression

# 5. Program berjalan berulang sampai pengguna memilih keluar

# Catatan penting:
# - Gunakan struktur data list of dictionary
# - Setiap fitur ditangani oleh fungsi terpisah
# - Fokus pada penggunaan fungsi, loop, input, if-else, lambda


"""Contoh output yang diharapkan

=== Menu Gudang ===
1. Tambah Barang
2. Total Nilai Inventaris
3. Tampilkan Barang Stok Rendah
4. Cari Barang Termahal
5. Keluar
Pilih menu: 1

Nama barang: Mouse
Stok barang: 8
Harga per unit: 85000
Barang 'Mouse' ditambahkan.

=== Menu Gudang ===
1. Tambah Barang
2. Total Nilai Inventaris
3. Tampilkan Barang Stok Rendah
4. Cari Barang Termahal
5. Keluar
Pilih menu: 1

Nama barang: Monitor
Stok barang: 15
Harga per unit: 1750000
Barang 'Monitor' ditambahkan.

=== Menu Gudang ===
Pilih menu: 2
Total nilai inventaris: Rp27.050.000

=== Menu Gudang ===
Pilih menu: 3
Barang dengan stok rendah (<10):
- Mouse (Stok: 8)

=== Menu Gudang ===
Pilih menu: 4
Barang termahal: Monitor (Rp1.750.000)

=== Menu Gudang ===
Pilih menu: 5
Terima kasih. Program selesai.

"""

# Buat kode anda di bawah ini
inventaris = []

def tambah_barang(): # pengerjaan terakhir
    inventaris.append(
        {"Nama barang":"Monitor",
        "Stok barang": 15,
        "Harga per unit": 1750000})
    print(f"Barang {inventaris[0]['Nama barang']} ditambahkan")
    

def total_nilai():
    print("\nmenu untuk melihat total nilai inventaris belum tersedia\n")

def stok_rendah():
    print("\nmenu untuk melihat stok rendah belum tersedia\n")

def cari_barang():
    print("\nmenu untuk mencari barang termahal belum tersedia\n")


def main_menu():
    while True:
        print("=== Menu Gudang ===")
        print("1. Tambah Barang")
        print("2. Total Nilai Inventaris")
        print("3. Tampilkan Barang Stok Rendah")
        print("4. Cari Barang Termahal")
        print("5. Keluar")

        input_menu = input("Masukan no menu yang anda inginkan: ")

        if input_menu.isdigit() and 1 <= int(input_menu) <=5:
            input_menu = int(input_menu)
            if input_menu == 1:
                tambah_barang()
            elif input_menu == 2:
                total_nilai()
            elif input_menu == 3:
                stok_rendah()
            elif input_menu == 4:
                cari_barang()
            elif input_menu == 5:
                print("\nTerima kasih. Program selesai.\n")
                break
        else:
            print("input tidak valid. Masukan no menu yang tersedia\n")
            # continue
    
main_menu()
