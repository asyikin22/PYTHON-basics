#dictionaries
cars = dict()
cars ['Ford Mustang'] = 1964
cars ['Toyota Camry'] = 1982
cars ['Honda Civic'] = 1972
print(cars)
print(cars['Honda Civic'])
cars['Ford Mustang'] = cars['Ford Mustang'] + 10
print(cars)

#dictionary literals (constants)
abcd = {'biru':1, 'hijau': 8, 'merah': 3}
print(abcd)

#empty dictionaries
efgh = {}
print(efgh)

#counting with get()
kira = dict()
nama = ['kucing', 'lembu', 'ayam','kucing', 'ayam', 'kucing', 'lembu', 'ayam']
for nama in nama:
    kira[nama] = kira.get(nama, 0) + 1
print(kira)

#counting words with text
kira = dict()
print('Enter aline of text:')
line = input('')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
    kira[word] = kira.get(word, 0) + 1
print('Kira', kira)

#retrieving lists of keys ad values
abcd = {'asyikin' : 1, 'austin': 10, 'Liam': 99}
print(list(abcd))
print(list(abcd.keys()))
print(list(abcd.values()))
print(list(abcd.items()))

#two iteration variables
abcd = {'asyikin' : 1, 'austin': 10, 'Liam': 99}
for x,y in abcd.items():
    print(x, y)

#count big text
name = input('Enter a file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print('Word count:', counts)
