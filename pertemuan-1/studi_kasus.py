print("==== SISTEM PENENTUAN KELULUSAN MHS =====")

nama = str(input("Masukkan Nama : "))
nilai_akhir = int(input("Masukkan Nilai Lu : "))

print("Namamu :", nama)
print("Nilai Akhir :", nilai_akhir)

if nilai_akhir > 80:
    print("Selamat! Kamu Lulus")
    status = "Lulus"
    grade = "A"
else: 
    nilai_akhir < 80
    print("Kamu harus mengulang lagi")
    status = "Tidak lulus"
    grade = "B"
    
print("Lu dapet Grade", grade)
print("==== Sampai Jumpa Lagi Bro ====")

