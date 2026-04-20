def hitung_nilai_akhir (tugas, uts, uas):
    nilai_akhir = (tugas * 0.30 ) + (uts * 0.30) + (uas + 0.40)
    return nilai_akhir
def tentukan_grade(nilai):
    if nilai >= 85:
        print ("A")
    elif nilai >= 70:
        print ("B")
    else:
        print ("E")
    
tugas = float(input ("masukan nilai tugas: "))
uts = float (input("masukan nilai: "))
uas = float (input("masukan nilai: "))

hitung_nilai_akhir (tugas, uts, uas)
grade = tentukan_grade(tentukan_grade)

print(f"nilai_akhir : {hitung_nilai_akhir}")
print(f" grade :{grade}")