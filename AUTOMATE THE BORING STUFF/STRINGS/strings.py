print ("Manipulating strings")

#escape character
blergh = 'Say hi to Asyikin\'s cat'
isTrue = 'cat' not in blergh
isTrue1 = 'Asyikin' in blergh
print(blergh)
print(blergh[10])
print(blergh[10:17])
print(isTrue)
print(isTrue1)


#Multiline strings
print("\nMultiline Strings\n")
print('''Dear Asyikin,
      
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
      
Sincerely, Bob''')

#String interpolation
print("\nString Interpolation\n")
nama = 'Asyikin'
umur = 3500
#with str()
print("Hello, my name is " + nama + ". I am " + str(umur) + ' years old')
#with interpolation
print("Hello, my name is %s. I am %s years old." %(nama, umur))
#with string literal
print(f"Hello, my name is {nama}. I am {umur} years old.")

#upper(), lower()
kucing = 'My cat, Leo is so playful.'
print('original', kucing)
print("Upper case: ", kucing.upper())
print("Lower case: ", kucing.lower())

#case-insensitive comparison
print("\nCase-insensitive comparison")
print("How are you feeling today?")
perasaan = input("---> " )
if perasaan.lower() == 'sedih':
    print('Aw, I hope you feel better soon 🥺')
else:
    print("I feel great too!")

#isupper(), islower()
ayam = 'SELAMAT PAGI, dunia'
isTrue = 'SELAMAT PAGI'.isupper()
isTrue1 = ayam.islower()
isTrue2 = 'dunia'.islower()
tukarKecil = 'SELAMAT PAGI'.upper().lower()
tukarBesar = 'dunia'.lower().upper()
print(isTrue)
print(isTrue1)
print(isTrue2)
print(tukarKecil)
print(tukarBesar)

#isX() method
print("\nisX() method")
lembu = 'My password is abc12345'
aa = 'password'.isalpha()
bb = 'abc12345'.isalpha()
cc = 'abc12345'.isalnum()
dd = '12345'.isdecimal()
ee = lembu.istitle()
print(aa, bb, cc, dd, ee, sep=(", "))

#user input validation
print("\nUser input validation")

while True:
    print('Masukkan umur anda: ')
    umur = input()
    if umur.isdecimal():
        break
    print('Tolong masukkan nombor untuk umur anda.')

while True:
    print("Sila masukkan kata laluan (nombor dan huruf sahaja)")
    kataLaluan = input()

    if kataLaluan.isdecimal():
        print("Kata laluan perlu mengandungi huruf")

    elif kataLaluan.isalpha():
        print("Kata laluan perlu mengandungi nombor")
    
    elif kataLaluan.isalnum():
        break

if kataLaluan.isalnum():
    print(f"Kata laluan anda adalah {kataLaluan}")

#startswith(), endswith()
greeting = 'Hello, world'
kk = greeting.startswith("Hello")
mm = greeting.endswith("world")
pisah = greeting.partition(",")
print(kk)
print(mm)
print(pisah)

#justifying text
print(greeting.rjust(20, "-"))
print(greeting.ljust(20, "*"))
print('Hello'.center(20, "+"))

#whitespace
print('\nWhitespace')
greeting1 = '     Selamat Pagi     '
print(greeting1)
print(greeting1.strip())
print(greeting1.lstrip())
print(greeting1.rstrip())

#ord() and chr()
print('\nord() and chr()')
print('Code point for each character in Asyikin')
print('A: ', ord("A"))
print('S: ', ord("S"))
print('Y: ', ord("Y"))
print('I: ', ord("I"))
print('K: ', ord("K"))
print('I: ', ord("I"))
print('N: \n', ord("N"))

print("Character string of integer 12345: ", chr(12345))
print("Character string of integer 9999: ", chr(77))
print("Character string of integer 9: ", chr(902))

#practice questions
print('Q6:')
print('hello, world!'[1])    #e
print('hello, world!'[0:5])  #hello
print('hello, world!'[:5])   #hello
print('hello, world!'[3:])   #lo, world   

print('\nQ7:')
print('hello'.upper())
print('hello'.upper().isupper())
print('hello'.upper().lower())

print('\nQ8:')
abc = 'Remember, remember, the first of November.'
print(abc.split())

fgh = " - "
print(fgh.join('There can be only one.'.split()))