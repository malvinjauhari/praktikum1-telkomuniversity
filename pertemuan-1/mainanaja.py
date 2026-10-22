kopi_sachet =  2000
kopi_satuan = 3

total_kopi = kopi_sachet * kopi_satuan

print("Total kopi", total_kopi)


nama = "Aljau Hari"
nim = 19823
ipk = 3.75
aktif = True

print("Nama :", nama)
print("Nim :", nim)
print("ipk :", ipk)
print("Status mahasiswa :", aktif)

print(type(nama))

#if else elif

total_belanja = 350000

if total_belanja >= 300000:
    diskon = 0.12
elif total_belanja <= 350000:
    diskon = 0.05
else:
    diskon = 0.01
bayar = total_belanja *(-1, + diskon)
print(diskon * 100, "%")
print("Total bayar", bayar)


#Indentasi
# Kondisi -> ==, !=, >, <. >=, <=

partai = int(input("Pilih siapa hayo?"))
if partai == 1:
    print("Antek antek asing")
elif partai == 2:
    print("Salut, anak abah")
elif partai == 3:
    print("03 mas, nggak asik")
else:
    print("Jangan golputlah, anjir")




