# conditional statements + input validation
name = input("Insert your name: ") 

password = input("Insert your password: ")

#check if the name is correct
if name == 'Asyikin':               # first block of code
    print('Hello Asyikin')

    #check if the password is correct
    if password == "cats":
        print('Access Granted')     # second block of code

    else:
        print('Wrong Password')     # third block of codea

else:
    print('Unauthorized User')

#comparison operators
x = 99 == 99
print(x)

y = 99 == 0
print(y)

z = 1 != 2
print(z)

print("strings comparison")

nama = 'asyikin' == "Asyikin"
print(nama)

nama2 = 'asyikin' != "Asyikin"
print(nama2)



