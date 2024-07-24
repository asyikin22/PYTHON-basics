print("dictionaries")

#basic syntax
myKucing = {'saiz': 'gemuk', 'warna': 'oren', 'sifat': 'garang'}
print('kucing saya', myKucing['sifat'], 'dan', myKucing['saiz'])

#unordered
print('\nItems in dictionaries are unordered')
myLauk = {'kuah': 'sambal', 'protein': 'ayam', 'karbo': 'nasi'}
myMakanan = {'protein': 'ayam', 'karbo': 'nasi', 'kuah': 'sambal'}
isTrue = myLauk == myMakanan
print('myLauk dan myMakanan adalah sama:', isTrue)

print('\nItems in lists are unordered')
myNasi = ['goreng', 'lemak', 'kerabu', 'paprik']
myNasi2 = [ 'lemak','goreng', 'kerabu', 'paprik']
isTrue = myNasi == myNasi2
print(isTrue)

#birthday
hariLahir = {'asyikin': 'Jan 1', 'Lily': 'Feb 2', 'Austin':'Mar 3'}

while True:
    print('\n')
    print("Masukkan nama: ")
    nama = input()
    if nama == "":
        break

    if nama in hariLahir:
        print(hariLahir[nama] + ' ialah hari lahir ' + nama)

    else:
        print("saya tiada informasi tarikh lahir untuk " + nama)
        birthday = input("Bilakah mereka lahir? ---> ")
        hariLahir[nama] = birthday
        print("Hari lahir baru telah dikemaskini")

#keys(), values(), items()
print('\nmethods: keys(), values(), items()')
buku = {
    'tajuk':"To Kill a Mockingbird",
    'penulis': 'Harper Lee',
    'tarikh terbit': 1960,
    'genre': 'Fiction',
    'isbn': "978-0-06-112008-4"
}

for keys in buku.keys():
    print(keys)

print("\n")
for values in buku.values():
    print(values)

print("\n")
for items in buku.items():
    print(items)

#multiple assignments
print("\nmultiple assignments")

cuaca = {
    "city": 'Kuala Lumpur',
    'tarikh': "24-7-2024",
    'suhu': '34°C', 
    'humidity': '55%', 
    'condition': 'panas terik'
}

for a, b in cuaca.items():
    print('key: ' + a + ", Value: " + b)

#checking if value or key exists in a dict - in + not in = boolean
print("\nCheck if a value or key exists using 'not' and 'not in'")
myCat = {'saiz': 'gemuk', 'warna': 'oren', 'sifat': 'garang'}
isTrue = 'sifat' in myCat.keys()
isTrue1 = 'gemuk' not in myCat.values()
isTrue2 = 'blablabla' in myCat.keys()
print ("key: nama is in the dictionary:", isTrue)
print("Value gemuk is not in the dictionary:", isTrue1 )
print("Key Blablabla is in the dictionary:", isTrue2)

#get method
print("\nGet() method")
furniture = {'table':5, 'chair': 10, 'Desk': 1}
print("I need to buy " + str(furniture.get('table', 0))+ ' tables.')
print("My friend will give me " + str(furniture.get('Desk', 0)) + " study desk.")
print("I have " + str(furniture.get("Ottoman", 0)) + " Ottoman though.")

#nested dictionaries and lists
tetamu = { 'Asyikin': {"oren": 15, "pasta": 10},
          'Austin': {"karipap": 20, "oren": 10},
          'Lily': {'pasta': 20, 'croissant': 10, 'karipap': 5}}

def buahTangan(tetamu, item):
    nomBawa = 0
    for key, values in tetamu.items():
        nomBawa = nomBawa + values.get(item, 0)
    return nomBawa

print('\nBilangan buah tangan: ')
print( "* Oren: " + str(buahTangan(tetamu, 'oren')))
print( "* Strawberry: " + str(buahTangan(tetamu, 'strawberry')))
print( "* Karipap: " + str(buahTangan(tetamu, 'karipap')))
print( "* Pasta: " + str(buahTangan(tetamu, 'pasta')))
print( "* Croissant: " + str(buahTangan(tetamu, 'croissant')))

#Practice questions
print('\nPractice Questions')
print('Q1 - empty dict')
kucing = {}

print('\nQ2')
dictionary = {'foo': 42}
print(dictionary)

# print('\nQ4')
# contoh = {'bar': 100}
# print(contoh['foo'])            # key error

#Fantasy Game Inventory
print("Fantasy Game Inventory\n")

inventory = {'arrow': 12, 'torch': 6, 
             'gold coin': 42, 'dagger': 1, 
             'rope': 1}

print('Inventory: ')
for k, v in inventory.items():
    print(" *", k, v)

#calculate total number of items in inventory
total = 0
for key, value in inventory.items():
    total = total + value

print("Total number of items: ", total)



