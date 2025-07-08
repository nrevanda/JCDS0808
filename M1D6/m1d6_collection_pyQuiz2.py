# =====================================================
# Debugging
# Program Pembayaran Otomatis (Dengan Pajak & Diskon)
# =====================================================
# Deskripsi:
# Program ini menerima total belanja pengguna.
# Fungsi `hitung_pembayaran()` harus mengembalikan
# harga setelah pajak 11% dan diskon 10% (jika belanja > 500000).

def hitung_pembayaran(jumlah):
    def tambah_pajak(jumlah):
        return jumlah * 1.11

    def diskon(jumlah):
        if jumlah > 500000:
            return jumlah * 0.9
        return jumlah

    setelah_diskon = diskon(jumlah)
    setelah_pajak = tambah_pajak(setelah_diskon)
    return setelah_pajak

# Main program
total = int(input("Masukkan total belanja Anda: "))
total_bayar = hitung_pembayaran(total)
print(f"Total yang harus dibayar (termasuk pajak & diskon): Rp{int(total_bayar)}")
