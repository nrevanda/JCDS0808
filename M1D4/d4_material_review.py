# =====================================
# REVIEW MATERI PYTHON: LIST & TUPLE
# =====================================

"""
Topik: List dan Tuple di Python

Deskripsi:
Script ini merupakan materi review tentang penggunaan struktur data List dan Tuple dalam Python.
Materi mencakup:
1. Pengertian List dan Tuple
2. Operasi dasar List dan Tuple
3. Operasi List (Menambah, Menghapus, Mengakses, Mengurutkan, dll.)
4. Operasi Tuple (Mengakses, Menelusuri, Mengetahui Isi)
5. Perbedaan utama antara List dan Tuple
6. Studi kasus sederhana penggunaan List dan Tuple

"""

# -------------------------------
# 1. PENGERTIAN LIST DAN TUPLE
# -------------------------------

# List: struktur data yang bisa diubah (mutable), digunakan untuk menyimpan kumpulan item
list_buah = ['apel', 'jeruk', 'pisang']

# Tuple: struktur data yang tidak bisa diubah (immutable), juga digunakan untuk menyimpan kumpulan item
tuple_hewan = ('kucing', 'burung', 'kelinci')

print("Contoh List:", list_buah)
print("Contoh Tuple:", tuple_hewan)

# ----------------------------------
# 2. OPERASI DASAR LIST DAN TUPLE
# ----------------------------------

# Akses elemen
# list[start:stop:step]
# list[index]
print("Elemen pertama list:", list_buah[0])
print("Menampilkan 3 elemen pertama list: ", list_buah[:3])
print("Elemen kedua tuple:", tuple_hewan[1])

# Panjang
print("Panjang list:", len(list_buah))
print("Panjang tuple:", len(tuple_hewan))

# Iterasi
print("Iterasi List:")
for buah in list_buah:
    print("-", buah)

print("Iterasi Tuple:")
for hewan in tuple_hewan:
    print("-", hewan)

# Update elemen pada List
list_buah[0] = 'mangga'
print("List setelah update:", list_buah)

# Penambahan elemen menggunakan append()
list_buah.append('anggur')
print("List setelah append:", list_buah)

# ---------------------------------------------
# 3. OPERASI UMUM PADA LIST
# ---------------------------------------------

angka = [3, 1, 4, 1, 5]
print("\nList angka awal:", angka)

# === MENAMBAHKAN DATA ===
angka.append(9)
print("Setelah append(9):", angka)
angka.insert(2, 10)
print("Setelah insert(2, 10):", angka)
angka.extend([7, 8])
print("Setelah extend([7, 8]):", angka)

# === MENGHAPUS DATA ===
angka.remove(1)  # menghapus elemen pertama yang cocok dengan 1
print("Setelah remove(1):", angka)
angka.pop()      # menghapus elemen terakhir
print("Setelah pop():", angka)
angka.clear()    # menghapus semua elemen
print("Setelah clear():", angka)

# Reset angka untuk operasi berikut
angka = [3, 1, 4, 1, 5]

# === MENGAKSES & INFORMASI DATA ===
print("Jumlah angka 1:", angka.count(1))
print("Index dari angka 4:", angka.index(4))

# === MENGURUTKAN DATA ===
angka.sort() # Hanya bisa digunakan saat tipe datanya sama
print("Setelah sort():", angka)
angka.reverse()
print("Setelah reverse():", angka)

# ---------------------------------------------------
# 4. OPERASI UMUM PADA TUPLE (tidak bisa dimodifikasi)
# ---------------------------------------------------

# Akses elemen
print("Elemen pertama tuple:", tuple_hewan[0])

# Iterasi elemen
print("Iterasi tuple:")
for h in tuple_hewan:
    print("-", h)

# Informasi isi
print("Jumlah kemunculan 'kucing':", tuple_hewan.count('kucing'))
print("Index dari 'anjing':", tuple_hewan.index('burung'))

# tuple_hewan.append('singa')  # ERROR: Tuple tidak mendukung append
# tuple_hewan[0] = 'singa'     # ERROR: Tuple tidak bisa diubah

# ---------------------------------------------
# 5. PERBEDAAN UTAMA ANTARA LIST DAN TUPLE
# ---------------------------------------------
"""
| Fitur            | List              | Tuple             |
|------------------|-------------------|-------------------|
| Mutable          | Ya                | Tidak             |
| Notasi           | [ ]               | ( )               |
| Kinerja          | Lebih lambat      | Lebih cepat       |
| Digunakan untuk  | Data berubah      | Data tetap        |
"""

# ------------------------------------------------------
# 6. STUDI KASUS: PENGGUNAAN LIST DAN TUPLE DALAM DATA
# ------------------------------------------------------

# Kasus: Menyimpan daftar transaksi harian dengan nama item dan harga
transaksi_harian = [
    ("Nasi Goreng", 20000),
    ("Es Teh", 5000),
    ("Mie Ayam", 15000)
]  # Menggunakan tuple agar data per item tidak berubah

print("\nDaftar Transaksi Hari Ini:")
total = 0
for item, harga in transaksi_harian:
    print(f"- {item} : Rp {harga}")
    total += harga

print(f"Total pemasukan hari ini: Rp {total}")

# ------------------------------------------------------
# CATATAN TAMBAHAN:
# ------------------------------------------------------
"""
Gunakan List ketika:
- Anda perlu menambah, menghapus, atau mengubah data
- Data bersifat dinamis

Gunakan Tuple ketika:
- Data bersifat tetap dan tidak berubah
- Tujuan efisiensi dan keamanan data
"""
