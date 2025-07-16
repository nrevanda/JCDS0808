from tabulate import tabulate
import datetime as dt

inventaris = [
    {"id_barang": "WH001", "nama_barang": "Pupuk Urea", "kategori": "Pupuk", "jumlah_stok": 50, "stok_minimal": 20, "lokasi": "Gudang A"},
    {"id_barang": "WH002", "nama_barang": "Bibit Padi IR64", "kategori": "Bibit", "jumlah_stok": 80, "stok_minimal": 30, "lokasi": "Gudang B"},
    {"id_barang": "WH003", "nama_barang": "Pestisida Organik", "kategori": "Pestisida", "jumlah_stok": 15, "stok_minimal": 10, "lokasi": "Gudang A"},
    {"id_barang": "WH004", "nama_barang": "Traktor Mini", "kategori": "Alat", "jumlah_stok": 5, "stok_minimal": 2, "lokasi": "Gudang C"},
    {"id_barang": "WH005", "nama_barang": "Pompa Air", "kategori": "Alat", "jumlah_stok": 7, "stok_minimal": 3, "lokasi": "Gudang C"},
    {"id_barang": "WH006", "nama_barang": "Ember Tanam", "kategori": "Perlengkapan", "jumlah_stok": 100, "stok_minimal": 40, "lokasi": "Gudang B"},
    {"id_barang": "WH007", "nama_barang": "Mulsa Plastik", "kategori": "Perlengkapan", "jumlah_stok": 30, "stok_minimal": 15, "lokasi": "Gudang B"},
    {"id_barang": "WH008", "nama_barang": "Bibit Jagung Hibrida", "kategori": "Bibit", "jumlah_stok": 9, "stok_minimal": 10, "lokasi": "Gudang A"},
    {"id_barang": "WH009", "nama_barang": "Sarung Tangan Tani", "kategori": "Perlengkapan", "jumlah_stok": 7, "stok_minimal": 10, "lokasi": "Gudang C"},
    {"id_barang": "WH010", "nama_barang": "Furadan 3GR", "kategori": "Pestisida", "jumlah_stok": 12, "stok_minimal": 5, "lokasi": "Gudang A"}
]

riwayat_mutasi = [
    {"id_mutasi": "IN-0001", "id_barang": "WH001", "nama_barang": "Pupuk Urea", "kategori": "Pupuk", "jenis_mutasi": "Masuk", "jumlah": 30, "tanggal": "2025-07-01", "lokasi": "Gudang A"},
    {"id_mutasi": "OUT-0001", "id_barang": "WH001", "nama_barang": "Pupuk Urea", "kategori": "Pupuk", "jenis_mutasi": "Keluar", "jumlah": 10, "tanggal": "2025-07-02", "lokasi": "Gudang A"},
    {"id_mutasi": "IN-0002", "id_barang": "WH002", "nama_barang": "Bibit Padi IR64", "kategori": "Bibit", "jenis_mutasi": "Masuk", "jumlah": 80, "tanggal": "2025-07-01", "lokasi": "Gudang B"},
    {"id_mutasi": "IN-0003", "id_barang": "WH003", "nama_barang": "Pestisida Organik", "kategori": "Pestisida", "jenis_mutasi": "Masuk", "jumlah": 15, "tanggal": "2025-07-03", "lokasi": "Gudang A"},
    {"id_mutasi": "IN-0004", "id_barang": "WH004", "nama_barang": "Traktor Mini", "kategori": "Alat", "jenis_mutasi": "Masuk", "jumlah": 5, "tanggal": "2025-07-01", "lokasi": "Gudang C"},
    {"id_mutasi": "IN-0005", "id_barang": "WH005", "nama_barang": "Pompa Air", "kategori": "Alat", "jenis_mutasi": "Masuk", "jumlah": 10, "tanggal": "2025-07-01", "lokasi": "Gudang C"},
    {"id_mutasi": "OUT-0002", "id_barang": "WH005", "nama_barang": "Pompa Air", "kategori": "Alat", "jenis_mutasi": "Keluar", "jumlah": 3, "tanggal": "2025-07-04", "lokasi": "Gudang C"},
    {"id_mutasi": "IN-0006", "id_barang": "WH006", "nama_barang": "Ember Tanam", "kategori": "Perlengkapan", "jenis_mutasi": "Masuk", "jumlah": 100, "tanggal": "2025-07-01", "lokasi": "Gudang B"},
    {"id_mutasi": "IN-0007", "id_barang": "WH007", "nama_barang": "Mulsa Plastik", "kategori": "Perlengkapan", "jenis_mutasi": "Masuk", "jumlah": 30, "tanggal": "2025-07-03", "lokasi": "Gudang B"},
    {"id_mutasi": "IN-0008", "id_barang": "WH008", "nama_barang": "Bibit Jagung Hibrida", "kategori": "Bibit", "jenis_mutasi": "Masuk", "jumlah": 9, "tanggal": "2025-07-01", "lokasi": "Gudang A"},
    {"id_mutasi": "IN-0009", "id_barang": "WH009", "nama_barang": "Sarung Tangan Tani", "kategori": "Perlengkapan", "jenis_mutasi": "Masuk", "jumlah": 7, "tanggal": "2025-07-02", "lokasi": "Gudang C"},
    {"id_mutasi": "IN-0010", "id_barang": "WH010", "nama_barang": "Furadan 3GR", "kategori": "Pestisida", "jenis_mutasi": "Masuk", "jumlah": 12, "tanggal": "2025-07-03", "lokasi": "Gudang A"}
]


def main_menu():
    """Fungsi utama yang menampilkan menu utama.

        Fungsi ini berjalan dalam loop hingga user memilih opsi keluar (Exit)."""
    while True:
        stok_rendah = hitung_stok_rendah()
        print("================================")
        print("     --Your company name--")
        print("          [Warehouse]")
        print("================================")
        print("[1] Data Base")
        print("[2] Barang Masuk")
        print("[3] Barang Keluar")
        print("[4] Update Data Base")
        print(f"[5] Pesan ({len(stok_rendah)})")
        print("[6] Exit program")

        input_menu = input("Masukkan nomor menu: ")
        if input_menu.isdigit() and 1 <= int(input_menu) <=6 :
            input_menu = int(input_menu)

            if input_menu == 1:
                data_base()
            elif input_menu == 2:
                barang_masuk()
            elif input_menu == 3:
                barang_keluar()
            elif input_menu == 4:
                update_riwayat()
            elif input_menu == 5:
                notifikasi()
            elif input_menu == 6:
                print("\nTerimakasih. Program selesai")
                break
        else:
            print("\nInput tidak valid. silahkan masukan angka 1 sampai 6.\n")

def data_base():
    """Menampilkan submenu untuk melakukan sesuatu dengan database inventaris"""
    while True:        
        print("Menu:")
        print("[1] Tampilkan database")
        print("[2] Sort database")
        print("[3] Cari barang")
        print("[4] Riwayat database")
        print("[5] Kembali")

        pilihan = input("\nPilih opsi menu:")
        if pilihan.isdigit() and 1 <= int(pilihan) <= 5:
            pilihan = int(pilihan)
            if pilihan == 1: 
                print("\n--= Database gudang =--\n")
                print(tabulate(inventaris, headers="keys", tablefmt="fancy_grid"))
            elif pilihan == 2:
                sort_database()
            elif pilihan == 3:
                filter_database()
            elif pilihan == 4:
                riwayat_database()
            elif pilihan == 5:
                break
        else:
            print("\nInput tidak valid. silahkan masukan angka 1 sampai 5")

def sort_database():
    """Menyediakan fitur pengurutan database inventaris"""
    while True:
        print("=== Sort / Urutkan Barang ===")
        print("[1] Sort by ID")
        print("[2] Sort by kategori")
        print("[3] Sort by jumlah stok")
        print("[4] Sort by lokasi penyimpanan")
        print("[5] Kembali")
        input_user = input("\nPilih opsi menu: ")

        if input_user.isdigit() and 1 <= int(input_user) <= 5:
            input_user = int(input_user)

            if input_user == 1:
                sort_item = sorted(inventaris, key=lambda item: item["id_barang"])
                print("--= Database sort by ID =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 2:
                sort_item = sorted(inventaris, key=lambda item: item["kategori"])
                print("--= Database sort by kategori =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 3:
                sort_item = sorted(inventaris, key=lambda item: item["jumlah_stok"])
                print("--= Database sort by jumlah stok barang =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 4:
                sort_item = sorted(inventaris, key=lambda item: item["lokasi"])
                print("--= Database sort by lokasi penyimpanan =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 5:
                break
            
        else:
            print("\nInput tidak valid. Silahkan masukkan angka 1 sampai 5")
    
def filter_database():
    """Menyediakan fitur pencarian barang dalam database inventaris"""
    while True:
        print("=== Filter / Cari Barang ===")
        print("[1] Berdasarkan ID")
        print("[2] Berdasarkan Nama Barang")
        print("[3] Berdasarkan Kategori")
        print("[4] Berdasrkan Lokasi Penyimpanan")
        print("[5] Kembali")
        
        input_user = input("\nPilih filter: ")
        if input_user.isdigit() and 1 <= int(input_user) <= 5:
            input_user = int(input_user)
            if input_user == 1:
                kata_kunci = input("Masukan ID barang: ").lower()
                filtered = []
                for item in inventaris:
                    if kata_kunci in item["id_barang"].lower():
                        filtered.append(item)
                if filtered:
                    print("\nHasil pencarian berdasarkan ID")
                    print(tabulate(filtered, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("\nData tidak ditemukan.")

            elif input_user == 2:
                kata_kunci = input("Masukkan nama barang: ").lower()
                filtered = []
                for item in inventaris:
                    if kata_kunci in item["nama_barang"].lower():
                        filtered.append(item)
                if filtered:
                    print("\nHasil pencarian berdasarkan nama barang")
                    print(tabulate(filtered, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("\nData tidak ditemukan")

            elif input_user == 3:
                kata_kunci = input("Masukkan kategori barang: ").lower()
                filtered = []
                for item in inventaris:
                    if kata_kunci in item["kategori"].lower():
                        filtered.append(item)
                if filtered:
                    print("\nHasil pencarian berdasarkan kategori")
                    print(tabulate(filtered, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("\nData tidak ditemukan")

            elif input_user == 4:
                kata_kunci = input("Masukkan lokasi penyimpanan barang: ").lower()
                filtered = []
                for item in inventaris:
                    if kata_kunci in item["lokasi"].lower():
                        filtered.append(item)
                if filtered:
                    print("\nHasil pencarian berdasarkan lokasi penyimpanan")
                    print(tabulate(filtered, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("\nData tidak ditemukan")

            elif input_user == 5:        
                break
        else:
            print("\nInput tidak valid. Silahkan masukkan angka 1 sampai 5")


def riwayat_database():
    """Memberikan pilihan sesuatu yang bisa dilakukan dengan database riwayat mutasi barang"""
    while True:
        print("Menu: ")
        print("[1] Tampilkan riwayat")
        print("[2] Sort riwayat")
        print("[3] Cari riwayat")
        print("[4] Kembali")
        input_user = input("\nPilih opsi menu: ")
        if input_user.isdigit() and 1 <= int(input_user) <= 4:
            input_user = int(input_user)
            
            if input_user == 1:
                print("\nData riwayat mutasi gudang")
                print(tabulate(riwayat_mutasi, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 2:
                sort_riwayat()
            elif input_user == 3:
                filter_riwayat()
            elif input_user == 4:
                break
        else:
            print("\nInput tidak valid. silahkan masukkan angka 1 sampai 4")
            
            
def sort_riwayat():
    """Mengurutkan data riwayat mutasi"""
    while True:
        print("\n=== Sort / Urutkan Database Riwayat ===")
        print("[1] Sort by tanggal mutasi")
        print("[2] Sort by jenis mutasi (masuk/keluar)")
        print("[3] Sort by ID barang")
        print("[4] Sort by ID mutasi")
        print("[5] Kembali")
        input_user = input("\nPilih opsi menu: ")

        if input_user.isdigit() and 1 <= int(input_user) <= 5:
            input_user = int(input_user)

            if input_user == 1:
                sort_item = sorted(riwayat_mutasi, key=lambda item: item["tanggal"])
                print("\n--= Riwayat sort by tanggal =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 2:
                sort_item = sorted(riwayat_mutasi, key=lambda item: item["jenis_mutasi"])
                print("\n--= Riwayat sort by jenis mutasi =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 3:
                sort_item = sorted(riwayat_mutasi, key=lambda item: item["id_barang"])
                print("\n--= Riwayat sort by ID barang =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 4:
                sort_item = sorted(riwayat_mutasi, key=lambda item: item["id_mutasi"])
                print("\n--= Riwayat sort by ID mutasi =--")
                print(tabulate(sort_item, headers="keys", tablefmt="fancy_grid"))
            elif input_user == 5:
                break
        else:
            print("Input tidak valid. Silakan masukkan angka 1 sampai 5.")
            

def filter_riwayat():
    """Menyediakan fitur pencarian pada riwayat mutasi barang"""
    while True:
        print("=== Filter / Cari Mutasi ===")
        print("[1] Berdasarkan tanggal")
        print("[2] Berdasarkan jenis mutasi")
        print("[3] Berdasarkan nama barang")
        print("[4] Kembali")
        input_user = input("\nPilih opsi menu: ")
        
        if input_user.isdigit() and 1 <= int(input_user) <= 4:
            input_user = int(input_user)
            
            if input_user == 1:
                tanggal = input("Masukkan tanggal (YYYY-MM-DD): ").strip()
                filtered = []
                for item in riwayat_mutasi:
                    if tanggal == item["tanggal"]:
                        filtered.append(item)
                if filtered:
                    print("\nHasil pencarian berdasarkan tanggal")
                    print(tabulate(filtered, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("\nData tidak ditemukan. Silahkan masukan tanggal dengan format YYYY-MM-DD")
                    
            if input_user == 2:
                jenis = input("Masukkan jenis mutasi (masuk/keluar): ").lower()
                filtered = []
                for item in riwayat_mutasi:
                    if jenis == item["jenis_mutasi"].lower():
                        filtered.append(item)
                if filtered:
                    print("\nHasil pencarian berdasarkan jenis mutasi")
                    print(tabulate(filtered, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("\nData tidak ditemukan.")
                
            if input_user == 3:
                nama = input("Masukkan nama barang: ").lower()
                filtered = []
                for item in riwayat_mutasi:
                    if nama in item["nama_barang"].lower():
                        filtered.append(item)
                if filtered:
                    print("\nHasil pencarian berdasarkan nama barang")
                    print(tabulate(filtered, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("\nData tidak ditemukan.")
            
            if input_user == 4:
                break
        else:
            print("\nInput tidak valid. silahkan masukkan angka 1 sampai 4")


def barang_masuk():
    """Menambahkan barang baru
    
    Data barang barus juga akan dicatat ke dalam 'riwayat_mutasi' dengan jenis mutasi 'masuk'"""
    while True:
        print("Menu: ")
        print("[1] Input barang baru")
        print("[2] Kembali")
        input_user = input("\nPilih opsi menu: ")
        if input_user.isdigit() and 1 <= int(input_user) <= 2:
            input_user = int(input_user)

            if input_user == 1:
                print("Masukkan data barang yang akan diinput:")
                id_barang = input_tidak_kosong("ID barang: ").upper()
                nama_barang = input_tidak_kosong("Nama barang: ")
                kategori = input_tidak_kosong("Kategori: ")
                jumlah_stok = input_hanya_angka("Banyak barang: ")
                stok_minimal = input_hanya_angka("Stok minimal di gudang: ")
                lokasi = input_tidak_kosong("Lokasi barang akan disimpan: ")

                barang_lama = None
                for item in inventaris:
                    if item["id_barang"] == id_barang:
                        barang_lama = item
                        break

                konfirmasi = input("Apakah anda yakin untuk menambahkan barang tersebut (Y/N): ").lower()
                if konfirmasi in ["y", "yes"]:
                    if barang_lama:
                        barang_lama["jumlah_stok"] += jumlah_stok
                        print("\n++++++++++++++++++++++++++++++++++++++++++++++")
                        print("Barang sudah ada. Stok berhasil diperbarui.")
                    else:
                        barang_baru = {
                            "id_barang": id_barang,
                            "nama_barang": nama_barang,
                            "kategori": kategori,
                            "jumlah_stok": jumlah_stok,
                            "stok_minimal": stok_minimal,
                            "lokasi": lokasi
                        }
                        inventaris.append(barang_baru)
                        print("\nBarang baru berhasil ditambahkan.")

                    riwayat_mutasi.append({
                        "id_mutasi": generate_id_mutasi("IN"),
                        "id_barang": id_barang,
                        "nama_barang": nama_barang,
                        "kategori": kategori,
                        "jenis_mutasi": "Masuk",
                        "jumlah": jumlah_stok,
                        "tanggal": dt.date.today().isoformat(),
                        "lokasi": lokasi
                    })
                    print("Mutasi berhasil dicatat dalam riwayat.")
                    print("++++++++++++++++++++++++++++++++++++++++++++++")
                else:
                    print("Input dibatalkan.\n")

            elif input_user == 2:
                break
        else:
            print("\nInput tidak valid. Silahkan masukkan angka 1 sampai 2.")


def barang_keluar():
    """Mengurangi jumlah stok barang berdasarkan ID barang.
    
    Akan tercatat sebagai jenis mutasi 'Keluar' di 'riwayat_mutasi'"""
    print("\n=== Input Barang Keluar ===")
    
    id_barang = input_tidak_kosong("Masukkan ID barang: ").upper()

    barang = None
    for item in inventaris:
        if item['id_barang'] == id_barang:
            barang = item
            break

    if barang:
        print(f"\nBarang ditemukan: {barang['nama_barang']}")
        print(f"Stok saat ini: {barang['jumlah_stok']}")
        jumlah_keluar = input_hanya_angka("Jumlah barang keluar: ")
        
        if jumlah_keluar <= barang["jumlah_stok"]:
            konfirmasi = input("Apakah anda yakin ingin mengeluarkan barang ini? (Y/N): ").lower()
            if konfirmasi in ["y", "yes"]:
                barang["jumlah_stok"] -= jumlah_keluar
                
                riwayat_mutasi.append({
                    "id_mutasi": generate_id_mutasi("OUT"),
                    "id_barang": barang["id_barang"],
                    "nama_barang": barang["nama_barang"],
                    "kategori": barang["kategori"],
                    "jenis_mutasi": "Keluar",
                    "jumlah": jumlah_keluar,
                    "tanggal": dt.date.today().isoformat(),
                    "lokasi": barang["lokasi"]
                })
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\nBarang berhasil dikeluarkan dan dicatat dalam riwayat.\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                print("Proses dibatalkan.")
        else:
            print("Stok tidak cukup untuk dikeluarkan!")
    else:
        print("Barang tidak ditemukan di inventaris.")
 

def update_riwayat():
    """Menyediakan pilihan untuk mengupdate data barang didatabase
    
    atau menghapus barang dari database"""
    while True:
        print("\n=== Menu Update Data ===")
        print("[1] Update informasi barang")
        print("[2] Hapus barang dari database")
        print("[3] Kembali")
        
        input_user = input("\nPilih opsi menu:")
        if input_user.isdigit() and 1 <= int(int(input_user)) <= 3:
            input_user = int(input_user)
        
        if input_user == 1:
            update_barang()
        elif input_user == 2:
            hapus_barang()
        elif input_user == 3:
            break
        else:
            print("Input tidak valid.")
    
    
def update_barang():
    """Mengubah value/atribut dari suati barang didalam database berdasarkan ID"""
    print("\n=== Update Data Barang ===")
    id_barang = input_tidak_kosong("Masukkan ID barang yang ingin diupdate: ").upper()
    
    barang = None
    for item in inventaris:
        if item['id_barang'] == id_barang:
            barang = item
            break

    if not barang:
        print("Barang tidak ditemukan di database.")
        return

    while True:
        print(f"\nData saat ini untuk {id_barang}:")
        print(tabulate([barang], headers="keys", tablefmt="fancy_grid"))
        
        print("Pilih data yang ingin diubah:")
        print("[1] Nama barang")
        print("[2] Kategori")
        print("[3] Lokasi penyimpanan")
        print("[4] Stok minimal")
        print("[5] Jumlah stok")
        print("[6] Kembali")

        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            barang["nama_barang"] = input_tidak_kosong("Nama barang baru: ")
        elif pilihan == "2":
            barang["kategori"] = input_tidak_kosong("Kategori baru: ")
        elif pilihan == "3":
            barang["lokasi"] = input_tidak_kosong("Lokasi penyimpanan baru: ")
        elif pilihan == "4":
            barang["stok_minimal"] = input_hanya_angka("Stok minimal baru: ")
        elif pilihan == "5":
            barang["jumlah_stok"] = input_hanya_angka("Jumlah stok baru: ")
        elif pilihan == "6":
            break
        else:
            print("Input tidak valid. Silahkan masukkan angka 1 sampai 6.")

        print("\nData berhasil diperbarui.")


def hapus_barang():
    """Menghapus data barang dari database berdasarkan ID"""
    print("\n=== Hapus Data Barang ===")
    id_barang = input_tidak_kosong("Masukkan ID barang yang ingin dihapus: ").upper()
    
    barang_dihapus = None
    for item in inventaris:
        if item["id_barang"] == id_barang:
            barang_dihapus = item
            break

    if not barang_dihapus:
        print("Barang tidak ditemukan dalam database.")
        return 

    print("\nData barang yang akan dihapus: ")
    print(tabulate([barang_dihapus], headers="keys", tablefmt="fancy_grid"))
        
    konfirmasi = input("Apakah kamu yakin ingin menghapus barang ini? (Y/N): ").lower()
    if konfirmasi in ["y", "yes"]:
        inventaris.remove(barang_dihapus)
        print(f"Barang dengan ID {id_barang} berhasil dihapus dari inventaris.")
    else:
        print("Proses penghapusan dibatalkan.")
    
    
def notifikasi():
    """Menampilkan daftar barang yang jumlah stoknya lebih sedikit dibanding stok minimal
    
    Berperan sebagai alat notifikasi untuk restock barang"""
    print("\n=== Notifikasi Stok Rendah ===")
    stok_rendah = hitung_stok_rendah()

    if stok_rendah:
        print("Berikut barang dengan stok dibawah batas minimal")
        print(tabulate(stok_rendah, headers="keys", tablefmt="fancy_grid"))
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n!mohon segera lakukan pengadaan barang kembali!\n")
        print("+++++++++++++++++++++++++++++++++++++++++++++++\n")
    else:
        print("Semua barang memiliki stok yang cukup")
    
def hitung_stok_rendah():
    """
    Return list barang yang memiliki stok lebih rendah daripada stok minimalnya
    """
    stok_rendah = []
    for item in inventaris:
        if item["jumlah_stok"] < item["stok_minimal"]:
            stok_rendah.append(item)
    return stok_rendah


def input_hanya_angka(angka):
    """
    Memvalidasi agar input hanya berupa angka
    """
    while True:
        nilai = input(angka)
        if nilai.isdigit():
            return int(nilai)
        else:
            print("Input tidak valid. Mohon isi dengan angka")


def input_tidak_kosong(huruf):
    """Memastikan input tidak kosong"""
    while True:
        nilai = input(huruf).strip()
        if nilai:
            return nilai
        else:
            print("Input tidak boleh kosong!")
     
            
def generate_id_mutasi(jenis):
    """Menghasilkan ID mutasi secara otomatis berdasarkan jenis mutasi dan jumlah mutasi sebelumnya
    
    ID mutasi akan berformat 4 digit dengan prefix "IN" atau "OUT"
    """
    jumlah = 0
    for r in riwayat_mutasi:
        if r["jenis_mutasi"].lower() == jenis.lower():
            jumlah += 1
    return f"{jenis.upper()}-{jumlah + 1:04d}" 

main_menu()