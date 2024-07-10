print("Hello bitches")

x = 30
if x < 100:
    print("kecil")
if x > 200:
    print("besar")

print("whatever")

#comparison operators

a = 15
if a == 15:
    print("sama dengan 15")

if a > 10:
    print("lebih besar dari 10")

if a >= 15:
    print("lebih besar ATAU sama dengan 15")

if a < 20:
    print("lebih kecil dari 20")

if a <= 15:
    print("lebih kecil ATAU sama dengan 15") 

if a !=10:
    print("tak sama dengan 10")

# one way decision
# python will skip if statements in a block if it's not true.
# note that when b == 4, python skips the block because it's false.
b = 3
print("sebelum 3")

if b == 3:
    print("ialah 3")
    print("masih 3")
    print("3 yang ketiga")

print("Selepeas 3")
print("Sebelum 4")
if b == 4:
    print("ialah 4")
    print("masih 4")
    print("4 yang ketiga")

print("selepas 4")

# nested decisions - 2 indentatations in a block
c = 99
if c > 5:
    print("lebih daripada 5")
    if c < 200:
        print("kurang daripada 200")

print("dah siap!")

# 2-way decisions - either or
# do one thing if a logical expressions is true
# do something else if the expression is false

d = 7
if d > 0:
    print("lebih besar")
else:
    print("lebih kecil")
print("dah siap!")

# try-except
# except block is triggered when something goes wrong in the code

test = "hello asyikin"
try:
    tukar = int(test)
except:
    tukar = 0
print("pertama", tukar)  # note that this code is not logical, except was triggered

test2 = "789"
try:
    tukar2 = int(test2)
except:
    tukar2 = 1
print("kedua", tukar2)   # note that 789 is succesfully converted into integer, except was ignored

#exercise - try except (input number)

abcde = input("masukkan nombor anda: ")
try:
    ival = int(abcde)
except:
    ival = -5

if ival > 0:
    print("good job, it's a nice number!")
else:
    print("Awas, itu bukan nombor!")

# compute gross pay for overtime and regular hours. 
# over time is x1.5 the regular rate
# incorporate try except block in case where input number is not integer

masa = input("masukkan masa bekerja: ")
rate = input("masukkan bayaran untuk sejam: ")
try:
    fm = float(masa)
    fr = float(rate)
except:
    print("sila masukkan nombor!")
    quit()

if fm > 40:
    print("lebih masa")
    regular = 40 * fr
    bayaranLebihMasa = (fr * 1.5) * (fm - 40)
    print( regular, bayaranLebihMasa)
    xy = regular + bayaranLebihMasa

else:
    print("masa biasa")
    xy = fm * fr

print("Bayaran anda adalah RM ", xy)