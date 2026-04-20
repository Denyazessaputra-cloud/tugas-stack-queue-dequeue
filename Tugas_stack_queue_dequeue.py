from collections import deque

# =========================================
# STRUKTUR DATA
# =========================================

class StrukturData:
    def __init__(self):
        self.data = deque()

    def tambah_normal(self, item):
        self.data.append(item)

    def tambah_vip(self, item):
        self.data.appendleft(item)

    def ambil(self):
        if self.kosong():
            return None
        return self.data.popleft()

    def hapus_item(self, item):
        try:
            self.data.remove(item)
            return True
        except ValueError:
            return False

    def kosong(self):
        return len(self.data) == 0

    def tampil(self):
        return list(self.data)


# =========================================
# SISTEM RESTORAN
# =========================================

class SistemRestoran:
    def __init__(self):
        self.antrian = StrukturData()
        self.riwayat = []  # stack

    def tambah_pelanggan(self, nama, tipe):
        if tipe.lower() == "vip":
            self.antrian.tambah_vip(nama)
        else:
            self.antrian.tambah_normal(nama)

        self.riwayat.append(nama)
        print(f"{nama} masuk sebagai {tipe}")

    def batalkan_pesanan(self):
        if not self.riwayat:
            print("Tidak ada pesanan untuk di-undo")
            return

        terakhir = self.riwayat.pop()

        if self.antrian.hapus_item(terakhir):
            print(f"Pesanan {terakhir} berhasil dibatalkan")
        else:
            print("Pesanan tidak ditemukan")

    def proses_dapur(self):
        pelanggan = self.antrian.ambil()

        if pelanggan:
            print(f"Pesanan diproses: {pelanggan}")
        else:
            print("Antrian kosong")

    def tampilkan_antrian(self):
        data = self.antrian.tampil()

        if not data:
            print("Antrian kosong")
        else:
            print("\n=== ANTRIAN ===")
            for i, nama in enumerate(data, 1):
                print(f"{i}. {nama}")


# =========================================
# MENU
# =========================================

def menu():
    sistem = SistemRestoran()

    while True:
        print("\n=== SISTEM RESTORAN ===")
        print("1. Tambah Pelanggan")
        print("2. Proses Pesanan")
        print("3. Batalkan Pesanan (Undo)")
        print("4. Lihat Antrian")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama: ")
            tipe = input("Tipe (normal/vip): ")
            sistem.tambah_pelanggan(nama, tipe)

        elif pilihan == "2":
            sistem.proses_dapur()

        elif pilihan == "3":
            sistem.batalkan_pesanan()

        elif pilihan == "4":
            sistem.tampilkan_antrian()

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


# =========================================
# MAIN
# =========================================

if __name__ == "__main__":
    menu()
