print("regular expression")
print("Length of phone number: ", len("017-1234567")) #11

def isNomTel(text):
    if len(text) != 11:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != "-":
        return False
    
    for i in range(4,11):
        if not text[i].isdecimal():
            return False
        
    return True

print ('Is 017-1234567 a phone number?')
print(isNomTel("017-1234567"))
print("Is kucing a phone number?")
print(isNomTel('kucing'))

# nombor_pengguna = input('Sila masukkan nombor telefon anda: ')
# if isNomTel(nombor_pengguna):
#     print(f"Nombor telefon anda ialah {nombor_pengguna} ")
# else:
#     print(f"Maaf, format nombor telefon anda tidak dibenarkan")

#Finding patterns with larger strings
mesej = '''Hubungi saya di nombor 012-1234568 esok. 
        Nombor pejabat saya ialah 018-1234569 .'''
for i in range(len(mesej)):
    chunk = mesej[i:i+11]
    if isNomTel(chunk):
        print('Telefon number yang dijumpai: ' + chunk)
print('Done')

#Creating + matching regex Object
print("\nCreating Regex Object")
import re
nomborTelRegex = re.compile(r'\d\d\d\-\d\d\d\d\d\d\d')
matchObject = nomborTelRegex.search('Nombor saya ialah 019-7654321.')
print('Nombor telefon yang dijumpai: ' + matchObject.group())

#grouping with parentheses
print("\ngrouping with parentheses")
nomborTepon = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d)')
mo = nomborTepon.search("Nombor telefon saya ialah 010-1234567")
print("Mobile carrier code: " + mo.group(1))
print(f"Nombor utama: {mo.group(2)}" )
print("Nombor penuh: ", mo.group())
print("nombor dipecahkan ke dua group", mo.groups())

#matching multiple groups with Pipe
print("\nmatching multiple groups with Pipe (either one)")
bikiniBottomRegex = re.compile(r'Spongebob Squarepants|Patrick Star')
mo1 = bikiniBottomRegex.search("Spongebob Squarepants and Patrick Star")
mo2 = bikiniBottomRegex.search("Patrick Star and Spongebob Squarepants")
print(mo1.group())
print(mo2.group())

print("matching multiple groups with Pipe (one of several patterns)")
butterRegex = re.compile(r'\bbutter(?:flies|cream)?\b', re.IGNORECASE)
text = '''Butterflies fluttered around the butter dish, 
adding a touch of buttercream sweetness to the afternoon tea'''

matches = butterRegex.findall(text)
print("These are the words with prefix 'butter: ")
for match in matches:
    print(" * ", match)

#matching with question mark
print("\nMatching with question mark '?'")
mobileNum = re.compile(r'(\d\d\d-)?\d\d\d\d\d\d\d')
mo1 = mobileNum.search("Nombor saya ialah 123-4567890")
mo2 = mobileNum.search("Nombor saya ialah 1234567")
print(f"Nombor penuh: {mo1.group()}")
print("Nombor tanpa carrier code:", mo2.group())

#matching specific repetitions with braces
print("\nmatching specific repetitions with braces")
laughRegex = re.compile(r'(Ha){5}')
mo1 = laughRegex.search("HaHaHaHaHa")
mo2 = laughRegex.search("HaHa") 
isTrue = mo2 == None
print(mo1.group())
print(isTrue)

#greedy vs non-greedy matching
print("\ngreedy vs non-greedy matching")
text = "1abc2def2"
greedyRegex = re.compile(r'1.*2')
mo = greedyRegex.search(text)

nonGreedyRegex = re.compile(r'1.*?2')
mo1 = nonGreedyRegex.search(text)

print("Greedy Match captures everything from start to end: ", mo.group())
print(f"Non-greedy match only captures the shortest string possible: {mo1.group()}")

#Character classes using findall() method
print('\ncharacter classes:')
itemsRegex = re.compile(r'\d+\s\w+')
x = itemsRegex.findall('10 apples, 5 oranges, 12 bananas, 2 grapes')
print(x)

#making my own character classes 
print("making my own character classes ")
text = '''A Cat danced effortlessly, 
Finding great Joy in every Hidden Gem.'''
lettersRegex = re.compile(r'[abcdeFGHIJ]')
otherLettersRegex = re.compile(r'[^abcdeFGHIJ]')
y = lettersRegex.findall(text)
z = otherLettersRegex.findall(text)
print("1: ", y)
print("2:", z)

#wildcard character
print('\nWildcard character')
text = "The analysis is key to the crisis."
isRegex = re.compile(r'.is')
abc = isRegex.findall(text)
print(abc)

#matching everythign with dot-star
print("\nmatching everythign with dot-star")
namaRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = namaRegex.search('First Name: Nur Last Name: Asyikin')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

#substituting string with sub() method
print("\nsub() method")
secretText = 'Officer Asyikin gave the secret files to Officer Lily'
name = re.compile(r'Officer \w+')
secret = name.sub('CENSORED', secretText)
print(secretText)
print(secret)


