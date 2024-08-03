print("input validation")

#input validation without pyinputplus module
while True:
    print("Masukkan umur awak: ")
    umur = input()
    try:
        umur = int(umur)
    except:
        print("Sila masukkan nombor")
        continue

    if umur < 1:
        print("Masukkan nombor positif!")
        continue
    break

print(f"Umur awak ialah {umur} tahun")

#pyinputplus
import pyinputplus as pyip
response = pyip.inputNum(prompt = 'Masukkan nombor: ')
print("Nombor yang anda pilih ialah: ", response)

#max, min, less than, greater than
print('\nmin, max, lessThan, greaterThan')
import pyinputplus as pyip
nombor1 = pyip.inputNum("Masukkan nombor minimum 5: ", min=5)
print("Nombor ini lebih dari 5:", nombor1)

import pyinputplus as pyip
nombor2 = pyip.inputNum("Masukkan nombor lebih besar dari 5: ", greaterThan=5)
print(f"Nombor ini lebih dari 5: {nombor2}")

import pyinputplus as pyip
nombor3 = pyip.inputNum("Masukkan nombor: min 5, kurang dari 7 ---> ", min=5, lessThan=7)
print(f"The correct number: {nombor3}")

#blank keyword argument
print("blank keyword argument")
import pyinputplus as pyip
jawapan = pyip.inputNum('Enter a digit: ')
print(jawapan)

jawapanKosong = pyip.inputNum("Masukkan nombor: ", blank=True)
print(jawapanKosong)

#limit, timeout and default
print("limit and timeout")
import pyinputplus as pyip
respon = pyip.inputNum("Masukkan satu nombor: ", limit=3)
print(respon)

import pyinputplus as pyip
try:
    respon1 = pyip.inputNum("Masukkan digit: ", timeout=10)
    print(respon1)
except pyip.inputTimeoutException:
    print("Tiada jawapan diterima selepas 10 saat")

#inputMenu()
import pyinputplus as pyip
pilihan = ['A', 'B', 'C']
menuPilihan = pyip.inputMenu(
    pilihan, 
    prompt="Sila pilih satu\n", 
    caseSensitive=False)
print(f'Awak telah memilih: {menuPilihan}')

#inputYesNo()
import pyinputplus as pyip
response = pyip.inputYesNo(
prompt='Adakah anda ingin ke langkah seterusnya?:\n')
print(f'Jawapan anda: {response}')

#inputChoice()
import pyinputplus as pyip
pilihan = ['kucing', 'ayam', 'semut']
response = pyip.inputMenu(
    pilihan, 
    prompt="Pilih antara 3, (1, 2, 3)\n",
    numbered=True
)
print('Anda telah memilih', response)

#inputStr()
import pyinputplus as pyip
response = pyip.inputStr(prompt="Masukkan suatu perkataan: \n",
allowRegexes=[r'^[a-zA-Z]+$'],
blockRegexes=[('.*', 'Ini bukan perkataan!')])
print(f'perkataan yang anda masukkan: {response}')

#inputDateTime()
import pyinputplus as pyip
tarikhMasa = pyip.inputDatetime(
    prompt = 'Apa tarikh hari ini dan sekarang pukul berapa?: \n',
    formats=['%d/%m/%Y %H:%M'])
print(f'Masa + tarikh sekarang: {tarikhMasa}')

#inputBool()
import pyinputplus as pyip
isTrue = pyip.inputBool(prompt='I am beautiful?\n')
if isTrue:
    print('Aw thanks 😊')
else:
    print('You\'re not very nice, are you 😢')


