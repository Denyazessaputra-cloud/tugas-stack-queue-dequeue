pilihan = 0
while pilihan !=3:
    print("WELCOME DENY HANDSOME")
    print("1,tampilkan angka 1 - 5 menggunakan (ror)")
    print("2,hitung mundur 5 - 1 menggunakan (while)")
    print("3, keluar ya geng")
    
    pilihan = str(input("silahkan masukan pilihan antara 1/2/3 : "))
    if pilihan == "1":
        print("kasih dia tampilan 1 - 5")
        for i in range (1, 6):
            print(i)
    elif pilihan =="2":
        print("kasih dia hitung mundur brohhh")
        x=5
        while x >= 1:
            print(x)
            x -= 1
    elif pilihan =="3":
        print("program selesai masss")
    else:
        print("pilihanmu ngawurrrrr")
    break