class Barang:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None


class Penyimpanan:
    def __init__(self):
        self.head = None

    def menambah_barang(self, name, importance):
        new_item = Barang(name, importance)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_item

    def menghapus_barang(self, name):
        if self.head is None:
            return

        if self.head.name == name:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    def print_barang_terpenting(self):
        if self.head is None:
            print("Tas kosong.")
            return

        sorted_items = self._sort_items_by_importance()
        print("Daftar item dalam tas berdasarkan tingkat kepentingan:")
        for item in sorted_items:
            print("Nama:", item.name, "| Tingkat Kepentingan:", item.importance)

    def _sort_items_by_importance(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current)
            current = current.next
        items.sort(key=lambda x: x.importance, reverse=True)
        return items


# Contoh penggunaan

penyimpanan = Penyimpanan()

# Menambahkan item ke dalam tas
penyimpanan.menambah_barang("Pedang", 6)
penyimpanan.menambah_barang("qm", 1)
penyimpanan.menambah_barang("sepatu perang", 4)

# Mencetak daftar item dalam tas
penyimpanan.print_barang_terpenting()

# Menghapus item dari hatiku(tas)
penyimpanan.menghapus_barang("qm")

# Mencetak daftar item setelah menghapus
penyimpanan.print_barang_terpenting()
