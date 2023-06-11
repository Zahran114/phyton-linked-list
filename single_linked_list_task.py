class Tugas:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next_task = None


class ListTugas:
    def __init__(self):
        self.head = None

    def add_tugas(self, description, priority):
        new_task = Tugas(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current_task = self.head
            while current_task.next_task is not None:
                current_task = current_task.next_task
            current_task.next_task = new_task

    def hapus_tugas(self, description):
        if self.head is None:
            return

        if self.head.description == description:
            self.head = self.head.next_task
            return

        current_task = self.head
        while current_task.next_task is not None:
            if current_task.next_task.description == description:
                current_task.next_task = current_task.next_task.next_task
                return
            current_task = current_task.next_task

    def print_tugas_terpenting(self):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        sorted_tasks = self._sort_tasks_by_priority()
        print("Daftar tugas berdasarkan prioritas:")
        for task in sorted_tasks:
            print("Deskripsi:", task.description,
                  "| Prioritas:", task.priority)

    def _sort_tasks_by_priority(self):
        tasks = []
        current_task = self.head
        while current_task is not None:
            tasks.append(current_task)
            current_task = current_task.next_task
        tasks.sort(key=lambda x: x.priority, reverse=True)
        return tasks


# Contoh penggunaan

list_tugas = ListTugas()

# Menambahkan tugas
list_tugas.add_tugas("Mengerjakan tugas matematika", 2)
list_tugas.add_tugas("Menulis laporan proyek", 1)
list_tugas.add_tugas("Membaca buku", 3)

# Mencetak daftar tugas
list_tugas.print_tugas_terpenting()

# Menghapus tugas
list_tugas.hapus_tugas("Menulis laporan proyek")

# Mencetak daftar tugas setelah menghapus
list_tugas.print_tugas_terpenting()
