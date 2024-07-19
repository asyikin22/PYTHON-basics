print('Object Oriented Programming')

#how to model a program?
# input - process - output
tambah2 = input('Masukkan nombor: ')
result = int(tambah2) + 2
print('Nombor anda ditambah 2 sama dengan:', result)

#Object oriented programming - PY4E example
class kiranombor:
    def __init__(self):
        self.x = 0
    
    def kira(self):
        self.x = self.x + 1
        print("So far", self.x)

blergh = kiranombor()

blergh.kira()
blergh.kira()
blergh.kira()

#0bject oriented programming - my example
class buku:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_details(self):
        print(f"title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
    
    def is_long_book(self):
        return self.pages > 350
    
#ceating an isntance of the book class
my_buku = buku("Metamorphosis", "Franz Kafka", 68)

#displaying the book details
my_buku.display_details()

#checking if the book is long
if my_buku.is_long_book():
    print("This is a thick book.")
else:
    print("This is a thin book.")

# dir()
class kiranombor:
    def __init__(self):
        self.x = 0
    
    def kira(self):
        self.x = self.x + 1
        print("So far", self.x)

blergh = kiranombor()

print("Type", type(blergh))
print("Type", type(blergh.x))
print("Type", type(blergh.kira))
print("Dir", dir(blergh))

#constructor vs destructor
class kucing:
    def __init__(self):
        self.z = 0
        print("I am constructed")
    
    def orange(self):
        self.z = self.z + 2
        print("So far", self.z)
    
    def __del__(self):
        print("I am destructed", self.z)

cat = kucing()

cat.orange()
cat.orange()

cat = 42
print("cat contains", cat)

#inheritance
print('inheritance')

#base class
class Binatang:
    def __init__ (self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes a sound.")

#derived class: cat
class Kucing(Binatang):
    def __init__ (self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print(f"{self.name}, the {self.breed}, meows")


#using the class
#create an instance of binatang
generic_animal = Binatang("Generic Animal")
generic_animal.sound()

# create an instance of cat
my_kucing = Kucing("Black", "Persian")
my_kucing.sound()