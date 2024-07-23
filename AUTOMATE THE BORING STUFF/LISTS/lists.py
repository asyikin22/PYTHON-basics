print("Lists")

#List data type
nombor = [1, 2, 3, 4, 5]
print (nombor)
print(nombor[2])
print(nombor[1:3])                  #slice
# print(nombor[10]) - this is out of range - index error
print(f"Jumlah item: {len(nombor)}")

binatang = ["ayam", "kucing", "lembu", "anjing", "ikan", "capybara"]
print(binatang)
print(binatang[0])
print(f"Jumlah binatang: {len(binatang)}")
binatang[0] = "biri-biri"
print("List baru: ", binatang)

#negaitve indexes
print(binatang[-2])                 # second to the last

#concatenation
gabung = nombor + binatang 
print(gabung)

#delete valus
del gabung[8]
print(gabung)                   #anjing deleted

random = ['selamat pagi', '3.1415', None, True, 42]
print(random)
print(random[3])
print(f"{random[0]}, Asyikin")
print(f"jumlah item: {len(random)}")

pi = random[1]
print('Nilai pi bersamaan dengan ' + pi)

#multiple list values
blergh = [ ['biru', 'merah', 'kuning'] , [2, 4, 6, 8, 10] ]
print(blergh[1])
print(blergh[0][2])                 #first list, third item     
print(blergh[1][3])                 #second item, fourth item
print(f"Kita ada {len(blergh)} list")

#range(len(someList)) - iterate over the indexes of a list
alphabet = ["aa", "bb", "cc", "dd", "ee"]
for i in range(len(alphabet)):
    print("Indeks " + str(i) + " in alphabet is: " + alphabet[i])

#The 'in' and 'not in' operators - example 1
(print('**not and not in operators - ex 1**'))
x = 'saya' in ["nama", 'saya', 'asyikin']
y = 'anna' in ["nama", 'saya', 'asyikin']
z = 'anna' not in ["nama", 'saya', 'asyikin']
print(x)
print(y)
print(z)

(print('**not and not in operators - ex 2**'))
negaraSaya = ['Malaysia', "Indonesia", "Thailand"]
print("Anda berasal dari mana?")
negara = input()
if negara not in negaraSaya:
    print("Maaf, negara anda tiada dalam senarai 😔")
else:
    print(f"Anda berasal dari {negara}")

#random.choice() + random.shuffle()
print("random.choice() + random.shuffle()")
import random
bunga = ["tulip", "daisy", "orchid", "daffodil", "marigold"]
print(random.choice(bunga))
random.shuffle(bunga)
print(bunga)

#augmented assignment statement + concatenation

greeting = "Selamat malam, "
greeting += 'Asyikin!'
print(greeting)

#method - index() - find values in a list
angka = [1, 2, 3, 4, 5]
print(angka.index(4))
# print(angka(9))           #not callable - type error

#method - append() insert() - add values to list
angka1 = [1, 2, 3, 4, 5]
angka1.append(6)
print(angka1)
angka1.insert(0, 0)
print(angka1)

#method - remove() 
angka2 = [6, 7, 8, 9, 10, 11, 12]
angka2.remove(11)
print(angka2)

#method - sort()
bunga1 =  ["tulip", "daisy", "orchid", "daffodil", "marigold"]
bunga1.sort()
print("Susunan asal: ", bunga)
print(bunga1)
bunga1.sort(reverse=True)
print("Susunan terbalik", bunga1)

#method - reverse()
bunga1 = ["tulip", "daisy", "orchid", "daffodil", "marigold"]
bunga1.reverse()
print(bunga1)

#Sequence data types
print('Sequence data type')
namaSaya = 'Asyikin'
print(namaSaya[5])
print(namaSaya[-7])
print(namaSaya[1:8])
isTrue = "ki" in namaSaya
print(isTrue)
isTrue = "n" not in namaSaya
print(isTrue)

for i in namaSaya:
    print(f"🌸🐤🌳 {i} 🌳🐤🌸")

#tuple
telur = "hello", 42, 9.99
print(telur[2])
# telur[0] = "hi"
#print(telur)            #this will give error

#list() + tuple()
print("tuple() + list()")

list1 = [1, 2, 3, 4, 5]
print(list1, "list ---> tuple", tuple(list1))

tuple1 = (5, 6, 7, 8, 9)
print(tuple1,'tuple ---> list', list(tuple1))

print("list on a tuple: ", list("Asyikin"))

#identity id() function
print("Id() function")
identifier = id("Asyikin")
print("ID Asyikin is: ", identifier)

sarapan = 'nasi'
print("ID sarapan asal: ", id(sarapan))

sarapan += 'lemak'
print("ID selepas diubah: ", id(sarapan))

print("_______________________________________________________")

#Practice Questions
print('\n practice questions \n')

#Q2
nombor = [2, 4, 6, 8, 10]
nombor[2] = 'hello'
print(nombor)

#Q3, 4, 5
kucing = ['k', 'l', 'm', 'n', 'o']
print(kucing[int(int('3' * 2) // 11)])
print(kucing[-1])
print(kucing[:2])

#Q6, 7, 8
ayam = [3.14, 'car', 11, 'car', True]
print("list asal: ", ayam)
print(ayam.index('car'))
ayam.append(99)
print("appended list: ", ayam)
ayam.remove('car')
print("removed item from list: ", ayam)




