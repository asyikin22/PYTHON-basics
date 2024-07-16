print ("hellowww")

sayur = 'sawi'
huruf = sayur[3]
print(huruf)

z = 2
y = sayur[z-1]
print(y)

#Len function
buah = 'durian'
nama = 'Asyikin'
x = len(buah)
w = len(nama)
print(x)
print(w)

#looping thorugh strings - while loop
nama = 'asyikin'
index = 0
while index < len(nama):
    huruf = nama[index]
    print(index, huruf)
    index = index + 1

#looping thorugh strings - for loop
nama = 'asyikin'
for huruf in nama:
    print(huruf)

#Slicing strings
full_name = 'Nur Asyikin'
print(full_name[0:3])
print(full_name[4:5])
print(full_name[4:20])

#string concatenation
m = 'hello'
n = m + "world"
print(n)
o = m + " " + 'World'
print(o)

#using in as a logical operator
negara = 'Switzerland'
print(negara)
result = 'z' in negara
print(result)
result2 = 'y' in negara
print(result2)
result3 = 'land' in negara
print(result3)

if 'e' in negara:
    print('Jumpa! There is an e in the word Switzerland')

#string library - built in string functions
greet = "Hello Asyikin"
blergh = greet.lower()
print(blergh)
print(greet)
print('HI THERE!'.lower())

# search a string using find()
negeri = 'Terengganu'
pos = negeri.find('gg')
print(negeri)
print(pos)

t = negeri.find('y')
print(t)

# search and replace
greet = 'Hello, Asyikin'
tukar = greet.replace('Asyikin', 'Liam')
print(greet)
print(tukar)

tukar_huruf = greet.replace("i", "3")
print(tukar_huruf)

# stripping whitespace
greet = '   Konnichiwa    '
print(greet)
kiri = greet.lstrip()
print(kiri)
kanan = greet.rstrip()
print(kanan)
kirikanan = greet.strip()
print(kirikanan)

#prefixes
line = "Please stop being annoying"
result = line.startswith("Please")
print(result)
result2 = line.startswith('r')
print(result2)