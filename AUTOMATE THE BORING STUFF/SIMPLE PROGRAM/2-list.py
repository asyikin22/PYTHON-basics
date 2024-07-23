#bad way to write list
print("bad way to write a list:")
warna1 = "hitam"
warna2 = "kuning"
warna3 = "biru"
warna4 = "merah"
warna5 = "hijau"

print(warna1)
print(warna2)
print(warna3)
print(warna4)
print(warna5)

#"better" way to write a list
print("better way to write a list")
kucing1 = input("Masukkan nama kucing pertama: ")
kucing2 = input("Masukkan nama kucing kedua: ")
kucing3 = input("Masukkan nama kucing ketiga: ")
kucing4 = input("Masukkan nama kucing keempat: ")
kucing5 = input("Masukkan nama kucing kelima: ")
print("Kucing kepunyaan anda bernama " 
      + kucing1, kucing2, kucing3, kucing4, kucing5, sep=", ")

#improved version using while loop
namaKucing = []                       
while True:
    print("Masukkan nama kucing awak yang nombor " 
          + str(len(namaKucing) + 1) 
          + " (tekan space jika tiada lagi)")
            
    nama = input()
    if nama == "":                   #this has to be empty string, NOT space
        break
    namaKucing = namaKucing + [nama]

print("Nama kucing awak adalah: ")
for nama in namaKucing:
    print(" ", nama)
