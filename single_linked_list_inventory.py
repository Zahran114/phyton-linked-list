class Produk:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None


class InventoryManagement:
    def __init__(self):
        self.head = None

    def menambahkan_produk(self, name, code, stock):
        new_product = Produk(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def hapus_produk(self, code):
        if self.head is None:
            return

        if self.head.code == code:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.code == code:
                current.next = current.next.next
                return
            current = current.next

    def print_penyimpanan(self):
        if self.head is None:
            print("Inventaris kosong.")
            return

        print("Daftar produk dalam inventaris:")
        current = self.head
        while current is not None:
            print("Nama:", current.name, "| Kode:",
                  current.code, "| Jumlah Stok:", current.stock)
            current = current.next


# Contoh penggunaan

penyimpanan = InventoryManagement()

# Menambahkan produk ke dalam inventaris
penyimpanan.menambahkan_produk("Buku", "BB001", 10)
penyimpanan.menambahkan_produk("map", "MM001", 30)
penyimpanan.menambahkan_produk("kertas", "KK001", 25)

# Mencetak daftar produk dalam inventaris
penyimpanan.print_penyimpanan()

# Menghapus produk dari inventaris
penyimpanan.hapus_produk("BB001")

# Mencetak daftar produk setelah menghapus
penyimpanan.print_penyimpanan()
