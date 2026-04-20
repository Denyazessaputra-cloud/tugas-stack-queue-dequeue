
nama=["dede","dodo","mama"]
pilihan=0
print("\n=== WELCOME DENYYYYY GANTENG PROGRAM ===")
print("\nsilahkan memilih")
print("1,menambahkan nama yang ingin di masukan ")
print("2,untuk menghapus dodo")
print("3,mengganti dede dengan didi")
print("4,selesai")
pilihan=str(input("silahkan masukan pilihan anda 1/2/3/4: "))
if pilihan == "1":
    nama.append("saleh")
    print(nama)
elif pilihan == "2":
    nama.remove("dodo")
    print(nama)
elif pilihan == "3":
    nama[0]="didi"
    print(nama)
else:
    print("program selesai bro")
