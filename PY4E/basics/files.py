print('Yellow')

#newline character

baru = "Hello\nAsyikin"
print(baru)

baru2 = "1\n2\n3\n4\n5"
print(baru2)

print(len(baru))

# file handle as a sequence
# 'cheese' is a placeholder, it can be anything really.
# it includes a newline character, you will see spaces between lines when you print it out
xfile = open('abcd.txt')
for cheese in xfile:
    print(cheese)

#counting lines in a file
fhand = open ('abcd.txt')
kira = 0
for baris in fhand:
    kira = kira + 1
print("Kiraan barisan:", kira)

# #reading the whole file
# fhand = open('long.txt')
# baca = fhand.read()
# print('kiraan bacaan: ', len(baca))

#searching through a file
# fhand = open('long.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("Duis"):
#         print(line)

#prompt for a file name 
fname = input("Masukkan nama fail: ")
fhand = open(fname)
kira = 0
for line in fhand:
    if line.startswith('Excepteur'):
        kira = kira + 1
print('There were', kira, 'perkataan yang dicari dalam', fname)

