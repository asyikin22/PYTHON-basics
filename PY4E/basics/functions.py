print ("good morning!")

#max + min function
besar = max("Selamat pagi")
print(besar)

kecil = min("Selamat pagi")
print(kecil)                    # it returns space character (empty)

blergh = min("Selamatpagi")
print(blergh)                   # it returns character with smallest unicode value - 's'

#functions - invoked vs not invoked
x = 5
print("hello")

def print_ayat():                   # this is NOT calling, it's storing & remembering things = zero output
    print("saya suka makan nasi")
    print("happy birthday to you!")

print("I run out of milk")
x = x + 10
print(x)

print_ayat()        # this is how we invoke a function, output in terminal

#parameters

def salutation(bahasa):             #salutation is a placeholder
    if bahasa == 'malay':
        print("selamat siang")
    elif bahasa == "italian":
        print("ciao")
    else:
        print("konnichiwa")

salutation("en")
salutation("malay")
salutation("italian")

# return value
def apa_khabar():
    return("How are you doing,")

print(apa_khabar(), "Asyikin","?")
print(apa_khabar(), "Austin", "?")
print(apa_khabar(), "Liam", "?")

def greeting(language):
    if language == "mandarin":
        return "Ni hao"
    elif language == "hindi":
        return "Namaste"
    else:
        return "Sawasdee"

print(greeting("hindi"), "Asyikin")
print(greeting('es'), "Liam")
print(greeting("mandarin"), "Austin")

#multiple parameters/ arguments
def tambahdua(a, b):
    added = a + b
    return added

x = tambahdua(23, 79)
print(x)