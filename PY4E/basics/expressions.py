#numeric expressions
xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy/1000
print(zz)

jj = 23
kk=jj % 5
print (kk)

print (4 ** 3)

#types
aaa = 5 + 3
print(aaa)

bbb = "Hello" + " Asyikin"
print(bbb)

cc = 1
print(type(cc))

temp = 30.5
print(type(temp))

print(type(1))

print(type(1.0))

#integer division
print(10/2)
print(9/2)
print(99/100)
print(10.0/2.0)
print(99.0/100.0)

#string conversion
perkataan = "123"
tukar = int(perkataan)
print(type(perkataan))
print(tukar + 1)         #124

#user input
name=input("What is your name? ")
print("Welcome", name)

#converting user input
tambah = input("Sila pilih nombor anda ")
hasil=int(tambah) + 1
print("tambah 1 sama dengan: ", hasil)

#compute gross pay
masa = input("masukkan jam bekerja: ")
rate = input("masukkan bayaran untuk sejam: ")
bayaran = float(masa) * float(rate)
print("Gaji anda adalah: RM", bayaran)