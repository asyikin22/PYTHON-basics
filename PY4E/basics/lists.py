print("Yellooowww")

# a list
flowers = ['rose', 'tulips', 'sunflower', 'orchid', 'daisy']
trees = ['oak', 'maple', 'palm', 'willow', 'pine']

print(flowers)
print(trees)

#list using for loops
for x in [5, 4, 3, 2, 1]:
    print(x)
print("Hooray!")

# definite loops + list
flowers = ['rose', 'tulips', 'sunflower', 'orchid', 'daisy']
for flower in flowers:
    print('My favorite flower is', flower)
print("ok dah siap!")

a = ['oak', 'maple', 'palm', 'willow', 'pine']
for a in a:
    print("I just chopped a", a, "tree")

#position in a list
cats = ['persian', 'siamese', 'bengal']
print(cats[1])

# lists are immutable - we can change it
lucky_number = [1, 2, 3, 4, 5]
print(lucky_number)
lucky_number[2] = 6
print(lucky_number)
print(len(lucky_number))

#concatenate list
a = [10, 11, 12, 13, 14, 15]
b = [16, 17, 18, 19, 20, 21]
c = a + b
print(a)
print(b)
print(c)

# slice list
number = [2, 4, 6, 8, 10]
print(number)
print(number[0:2])
print(number[1:4])
print(number[2:4])

#append() method
warna = []
warna.append("blue")
warna.append("pink")
print(warna)
warna.append("green")
print(warna)

#is something in a list?
number = [2, 4, 6, 8, 10]
result = 11 in number
print(result)
result2 = 6 in number
print(result2)

#lists in order
flowers = ['rose', 'tulips', 'sunflower', 'orchid', 'daisy']
print(flowers)
flowers.sort()
print(flowers)

#built in functions
num = [56, 987, 43, 29, 5, 201]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))

# strings and lists
# we can access the word using loops
xyz = 'My name is Asyikin'
pecah = xyz.split()
print(xyz)
print(pecah)
print(len(xyz))
print(len(pecah))

for i in pecah:
    print(i)

#double split pattern
fhand = open('email.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print (words)

    email = words[1]
    pieces = email.split('@')
    print(pieces[0])
    print(pieces[1])
