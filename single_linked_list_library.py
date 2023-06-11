class Pengunjung:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = None

    def borrow_book(self, book_title):
        new_book = Buku(book_title)
        if self.borrowed_books is None:
            self.borrowed_books = new_book
        else:
            current_book = self.borrowed_books
            while current_book.next_book is not None:
                current_book = current_book.next_book
            current_book.next_book = new_book

    def print_borrowed_books(self):
        if self.borrowed_books is None:
            print("Pengunjung", self.name, "tidak memiliki buku yang dipinjam.")
        else:
            print("Daftar buku yang dipinjam oleh pengunjung", self.name + ":")
            current_book = self.borrowed_books
            while current_book is not None:
                print(current_book.title)
                current_book = current_book.next_book


class Buku:
    def __init__(self, title):
        self.title = title
        self.next_book = None


class Perpus:
    def __init__(self):
        self.visitors = []

    def add_pengunjung(self, name):
        new_visitor = Pengunjung(name)
        self.visitors.append(new_visitor)

    def cari_pengunjung(self, name):
        for visitor in self.visitors:
            if visitor.name == name:
                return visitor
        return None


# Contoh penggunaan

perpus = Perpus()

# Menambahkan pengunjung
perpus.add_pengunjung("wawa")
perpus.add_pengunjung("ujang")
perpus.add_pengunjung("Mamat")

# Menyimpan catatan peminjaman buku
wawa = perpus.find_visitor("wawa")
wawa.borrow_book("mencintai dia")
wawa.borrow_book("kapan kamu suka sama aku?")

ujang = perpus.cari_pengunjung("ujang")
ujang.borrow_book("jatuh cinta sendiri")

# Mencetak daftar buku yang dipinjam oleh pengunjung
wawa.print_borrowed_books()
ujang.print_borrowed_books()
