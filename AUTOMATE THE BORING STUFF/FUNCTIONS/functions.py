
# #basic function
def hi():
    print("hola")
    print("Ciao")
    print("konnichiwa")

hi()
hi()
hi()

#def statement with parameters
def greeting(nama):
    print("Selamat pagi, " + nama)

greeting ("Asyikin")
greeting ("Liam")
greeting ("Austin")

#return values + return statement
print("random module")
import random

def jawapan(nombor):
    if nombor == 1:
        return 'Ia adalah pasti'
    elif nombor == 2:
        return 'Ia telah ditentukan'
    elif nombor == 3:
        return 'ya'
    elif nombor == 4: 
        return 'Jawapan kelihatan samar, cuba lagi'
    elif nombor == 5:
        return 'Tanya lagi sebentar lagi'
    elif nombor == 6:
        return 'tumpukan perhatian dan tanya lagi'
    elif nombor == 7:
        return 'jawapan saya adalah tidak'
    elif nombor == 8:
        return 'ia kelihatan tidak bagus'
    elif nombor == 9:
        return 'sangat meragukan'

rawak = random.randint(1, 9)      # 1 to 9 inclusive
fortune = jawapan(rawak)
print(fortune)

#optional parameters - end
print("end parameter will disable the newline at the end of of function call")
print("hello", end=" ")
print('asyikin')

#optional parameters - sep
print("sep parameter will separate values with a single space")
print("anjing", "lembu", "kucing", "ayam", "kambing")
print("anjing", "lembu", "kucing", "ayam", "kambing", sep=", ")

#call stack 

def a():
    print('a() mula')
    
    b()
    d()
    print('a() balik')

def b():
    print('b() mula')
    
    c()
    print('b() balik')

def c():
    print('c() mula')
    print('c() balik')

def d():
    print('d() mula')
    print('d() balik')

a()

#local scopes cannot use variales in other local scope
def spam():
    telur = 100
    bacon()
    print(telur)

def bacon():
    ham = 50
    telur = 0

spam()

#global variables can be read from a local scope
def kucing():
    print(oyen)

oyen = 99
kucing()
print(oyen)

#try and except 
def kira (bahagi):
    try: 
        return 50 / bahagi
    except ZeroDivisionError:
        print("Error: Invalid argument")

print(kira(3))
print(kira(10))
print(kira(19))
print(kira(0))


