print("hello")

#loops
n = 3
while n > 0:
    print(n)
    n = n-1
print("Hooray!")
print(n)

#Definite Loop

for i in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] :
    print(i)
print("Off you go!")

#Definite loop with strings
friends = ["Asyikin", "Liam", "Austin", "Lily"]
for friend in friends:
    print("Selamat Hari Raya,", friend)
print("Ok dah siap")

# Loop Idioms

#Looping through a set
print("Sebelum")
for benda in [99, 56, 43, 18, 72, 402]:
    print(benda)
print("Selepas")

#largest number
largest_so_far = -2
print("Sebelum", largest_so_far)
for nombor in [99, 56, 43, 18, 72, 402]:
    if nombor > largest_so_far:
        largest_so_far = nombor
    print(largest_so_far, nombor)
print("Selepas", largest_so_far)

#Counting in a loop
kosong = 0
print("Sebelum", kosong)
for benda in[99, 56, 43, 18, 72, 402]:
    kosong = kosong + 2
    print (kosong, benda)
print("Selepas", kosong)

#summing in a loop
dua = 2
print("sebelum", dua)
for nombor in [1, 2, 3, 4, 5]:
    dua = dua + nombor
    print(dua, nombor)
print("selepas", dua)

#finding average in a loop
kira = 0
jumlah = 0
print("sebelum", kira, jumlah)
for nilai in [3, 6, 9, 12, 15]:
    kira = kira + 1
    jumlah = jumlah + nilai
    print(kira, jumlah, nilai)
print('selepas', kira, jumlah, jumlah/kira)

#filtering in a loop
print('sebelum')
for nilai in [99, 56, 43, 18, 72, 402]:
    if nilai > 95:
        print("Nombor besar:", nilai)
print("selepas")

#search using a boolean variable
found = False
print('sebelum', found)
for nilai in [56, 43, 18, 72, 99, 402]:
    if nilai == 99:
        found = True
    print(found, nilai)
print('Selepas', found)

#finding the largest value
nombor_terbesar = 0
print('sebelum', nombor_terbesar)
for nombor in [56, 43, 18, 72, 99, 402]:
    if nombor > nombor_terbesar:
        nombor_terbesar = nombor
    print(nombor_terbesar, nombor)
print('selepas', nombor_terbesar)

#finding the smallest value
nombor_terkecil = 20
print('sebelum', nombor_terkecil)
for nombor in [56, 43, 18, 72, 99, 402]:
    if nombor < nombor_terkecil:
        nombor_terkecil = nombor
    print(nombor_terkecil, nombor)
print('selepas', nombor_terkecil)