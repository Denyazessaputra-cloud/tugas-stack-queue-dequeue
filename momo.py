# Daftar makanan (LIST)
makanan = ["Nasi Goreng", "Es Teh", "Mie Ayam"]

# Harga makanan (TUPLE) – urutan harus sama dengan list makanan
harga = (35000, 5000, 12000)

# Status pembayaran (DICTIONARY)
status_pembayaran = {
    "Nasi Goreng": "sudah dibayar",
    "Es Teh": "belum dibayar",
    "Mie Ayam": "sudah dibayar"
}

# Fungsi untuk menghitung total & mengecek status pembayaran
def cek_jajan(makanan, harga, status_pembayaran):
    total = 0
    print("=== RINCIAN JAJAAN DIKA ===")
    
    for i in range(len(makanan)):
        print(f"{makanan[i]} - Rp{harga[i]} - {status_pembayaran[makanan[i]]}")
        total += harga[i]   # perulangan menghitung total harga
    
    print("\nTotal uang yang dihabiskan:", total)

    # Cek status pembayaran (perulangan)
    print("\n=== STATUS PEMBAYARAN ===")
    for item, status in status_pembayaran.items():
        print(f"{item} -> {status}")

# Panggil fungsi
cek_jajan(makanan, harga, status_pembayaran)