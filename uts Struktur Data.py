class InventarisProduk:

    def __init__(self):
        self.data_produk = {}

    def tambah_produk(self, id_produk, nama, kategori, harga, stok):

        if id_produk in self.data_produk:
            print("\n[!] ID produk sudah terdaftar!")
            return

        self.data_produk[id_produk] = {
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": stok
        }

        print("\n[BERHASIL] Produk berhasil ditambahkan!")

    def cari_produk(self, id_produk):

        produk = self.data_produk.get(id_produk)

        if produk is not None:
            print("\n========== DETAIL PRODUK ==========")
            print("ID Produk :", id_produk)
            print("Nama      :", produk["nama"])
            print("Kategori  :", produk["kategori"])
            print("Harga     : Rp", format(produk["harga"], ",.2f"))
            print("Stok      :", produk["stok"])
            print("===================================")

        else:
            print("\n[!] Produk tidak ditemukan!")

    def hapus_produk(self, id_produk):

        if id_produk in self.data_produk:
            del self.data_produk[id_produk]

            print("\n[BERHASIL] Produk berhasil dihapus!")

        else:
            print("\n[!] Produk tidak ditemukan!")

    def tampilkan_semua(self):

        if len(self.data_produk) == 0:
            print("\n[!] Inventaris masih kosong!")
            return

        print("\n========== DAFTAR INVENTARIS ==========")

        for id_produk, produk in self.data_produk.items():

            print("---------------------------------------")
            print("ID Produk :", id_produk)
            print("Nama      :", produk["nama"])
            print("Kategori  :", produk["kategori"])
            print("Harga     : Rp", format(produk["harga"], ",.2f"))
            print("Stok      :", produk["stok"])

        print("---------------------------------------")
        print("Total produk:", len(self.data_produk))
        print("=======================================")

    def jumlah_produk(self):

        return len(self.data_produk)

def tampilkan_menu():

    print("\n")
    print("=" * 45)
    print("       SISTEM MANAJEMEN INVENTARIS")
    print("          BERBASIS HASH TABLE")
    print("=" * 45)
    print("1. Tambah Produk")
    print("2. Cari Produk")
    print("3. Hapus Produk")
    print("4. Tampilkan Semua Produk")
    print("5. Jumlah Produk")
    print("6. Keluar")
    print("=" * 45)

def main():

    inventaris = InventarisProduk()

    while True:

        tampilkan_menu()

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":

            print("\n========== TAMBAH PRODUK ==========")

            id_produk = input("Masukkan ID Produk: ").strip()
            nama = input("Masukkan Nama Produk: ").strip()
            kategori = input("Masukkan Kategori: ").strip()

            if not id_produk or not nama or not kategori:
                print("\n[!] Semua data harus diisi!")
                continue

            try:

                harga = float(input("Masukkan Harga Produk: Rp "))
                stok = int(input("Masukkan Jumlah Stok: "))

                if harga < 0 or stok < 0:
                    print("\n[!] Harga dan stok tidak boleh negatif!")
                    continue

                inventaris.tambah_produk(
                    id_produk,
                    nama,
                    kategori,
                    harga,
                    stok
                )

            except ValueError:

                print("\n[!] Harga harus berupa angka dan stok harus berupa bilangan bulat!")

        elif pilihan == "2":

            print("\n========== CARI PRODUK ==========")

            id_produk = input("Masukkan ID Produk: ").strip()

            inventaris.cari_produk(id_produk)

        elif pilihan == "3":

            print("\n========== HAPUS PRODUK ==========")

            id_produk = input("Masukkan ID Produk: ").strip()

            inventaris.hapus_produk(id_produk)

        elif pilihan == "4":

            inventaris.tampilkan_semua()

        elif pilihan == "5":

            total = inventaris.jumlah_produk()

            print("\nJumlah produk dalam inventaris:", total)

        elif pilihan == "6":

            print("\n===================================")
            print("Terima kasih telah menggunakan")
            print("Sistem Manajemen Inventaris Produk!")
            print("===================================")

            break

        else:

            print("\n[!] Pilihan tidak valid!")
            print("Silakan pilih menu 1 sampai 6.")

if __name__ == "__main__":

    main()
