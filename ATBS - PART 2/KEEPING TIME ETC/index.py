print('Keeping Time, Scheduling Tasks and Launching Programs')

# import time
# masa = time.time()
# print(masa)
# print(round(masa, 2))
# print(round(masa, 3))
# print(round(masa))

# #use time.time() to profile code
# import time, sys

# def calcProd(n):
#     product = 1
#     for i in range (1, n+1):
#         product = product * i
#     return product

# n = 100000

# # Set the maximum number of digits for integer string conversion
# sys.set_int_max_str_digits(2000000)  # Increase as needed

# startMasa = time.time()
# prod = calcProd(n)
# tamatMasa = time.time()

# print(f'The result is {len(str(prod))} digits long')
# print(f'Took {tamatMasa-startMasa:.2f} seconds to calculate')

# #time.ctime() - human readable version

# import time
# masaManusia = time.ctime()
# print(f"Epoch time: {masaManusia}")

# print('\nEpoch time converted to human readable time:')

# masaSekarang = time.time()
# print(time.ctime(masaSekarang))

# #use time.sleep() Funtion - to pause a program
# import time 
# for i in range(3):
#     print("Meow")
#     time.sleep(2)
#     print("Mooooooo")
#     time.sleep(2)

# time.sleep(5)

# #datetime() moudle
# import datetime
# print(datetime.datetime.now())

#timedelta data type
from datetime import timedelta

delta = timedelta(days=20, hours=5, minutes =2, seconds=7)
hari = delta.days
saat = delta.seconds
microSaat = delta.microseconds
print({hari, saat, microSaat})