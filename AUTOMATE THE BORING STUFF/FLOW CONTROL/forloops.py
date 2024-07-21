# for loop
print ("Nama saya")
for nama in range(5):
    print(f"Asyikin ({nama})")

#calculate sum of number 
jumlah = 0
for nombor in range(901):
    jumlah = jumlah + nombor
print(jumlah)                       #405450

#range() function

for item in range (8, 15):
    print(item)

for item in range (0, 18, 2):
    print(item)

for item in range (5, -5, -3):
    print(item)

#importing modules
import random
for i in range (5):
    print(random.randint(1, 1000))

########################################################################

#Practice questions 1
a = 2 == 2
print(a)

b = 3 != 3
print(b)

#Practice questions 4
print("Q4")
aa = (5 > 4) and (3 == 5)
print(aa)

bb = not (5 > 4)
print (bb)

cc = (5 > 4) or ( 3 == 5)
print(cc)

dd = (True and True) and (True == False)
print(dd)

ee = (not False) or (not True)
print(ee)

#Practice questions 7 - condition

# basic - to make decision
nombor = input("Masukkan nombor: ")
if int(nombor) % 2 == 0:
    print(f"{nombor} adalah nombor genap.")
else:
    print(f"{nombor} adalah nombor ganjil.")

#form validation
namaPengguna = input("Masukkan nama anda: ")
if len(namaPengguna) < 5: 
    print("Nama pengguna mesti melebihi 5 karakter")
else:
    print("Nama pengguna anda diterima")

#game logic
markah = input("masukkan markah awak: ")
if int(markah) >= 80:
    print("You scored an A!")
elif int(markah) >= 60:
    print("You scored a B!")
else:
    print("study harder you stup!d b@tch 😄")

#practice question 9 
ucapan = int(input("masukkan nilai untuk bahasa: "))

if ucapan == 1:
    print("Bahasa Inggeris")

elif ucapan == 2:
    print("Bahasa Mandarin")

else:
    print("Apa-apa bahasa")

#Practice questions 14 - import module
# import spam   # type: ignore

# spam.bacon    # type: ignore

#practice question 13
# for loop
print("for loop")
for item in range (1,11):
    print(item)

#while loop
print("while loop")
count = 1
while count < 11:
    print(count)
    count = count + 1

#pracice question 12
#range() - for loop
print("range() - for loop")
for item in range(10):
    print(item)

print("0, 10, 1")
for item in range(0, 10, 1):
    print(item)
