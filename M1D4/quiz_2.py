# Diberikan daftar produk, masing-masing berupa tuple (nama_produk, harga)

produk = [
    ("Sabun", 10000),
    ("Sampo", 25000),
    ("Pasta Gigi", 15000),
    ("Tisu", 5000)
]

# 1. Buat list baru yang berisi NAMA PRODUK dalam huruf kapital semua.
# 2. Hitung total harga dari semua produk dan tampilkan.

# 1. Buat list nama produk dalam huruf kapital:
produk_kapital = [nama.upper() for nama, harga in produk]
print(produk_kapital)

# 2. Hitung total harga:
total_harga = 0
for nama, harga in produk:
    total_harga += harga
print(f"total harga: {total_harga}")


