# if statement
name = "Asyikin"

if name == 'Asyikin':
    print('Hi, Asyikin')

# else statement
inpName = input("Insert a name: ")

if inpName == 'Austin':
    print('Hi, Austin')

else:
    print('Hello Stranger')

#elif statement
name = 'Anna'
age = input("Insert your age here: ")

if age == '35':
    print('Hi, Lily')

elif int(age) < 12:
    print('You are not Anna, child')

elif int(age) > 50:
    print('You are not Anna, Grandma')

elif int(age) > 18:
    print('Unlike you, Anna is more mature and experienced!')

#elseif - else
name = "Kucing"
umur = input("Berapa umur awak? - ")

if int(umur) == 10:
    print("Hi, Kucing, meows 🐾")
elif int(umur) < 10:
    print("You are a baby, you're not Kucing!")
else:
    print("You're not Kucing either!")

#While statement 1
kira = 0
while kira < 5:
    print("Konnichiwa", (kira))

    kira = kira + 1

#break statement
while True:
    print("Please type your name.")
    name = input()
    if name == 'Spongebob':
        break

print('Terima kasih')

#While statement 2
counter = 0
while counter < 10:
    if counter == 5:
        break
    print(counter)
    counter += 1

#While statement 3 - For loop
print("For loop - break statement")
for item in range(10):
    if item == 4:
        break
    print(item)

#continue statement
print("Continue statement")

while True:
    print("Siapa awak?")
    name = input("Nama saya: ")

    if name != "asyikin":
        continue
    print("Hi Asyikin, sila masukkan password") 

    password = input()
    if password == "abcde":
        break

print("Access granted")