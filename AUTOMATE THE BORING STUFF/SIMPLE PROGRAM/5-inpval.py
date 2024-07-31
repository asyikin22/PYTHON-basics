#1st mini program
print('How to keep an idiot busy for hours')

import pyinputplus as pyip

while True:
    prompt = "Nak tahu tak macam mana orang bodoh sibukkan dirinya?\n"
    jawapan = pyip.inputYesNo(prompt)
    if jawapan == "no":
        break

print('Terima kasih, have a nice day 😊')

#2nd mini program
print('Multiplication quiz')
import pyinputplus as pyip
import random, time

bilSoalan = 10
jawapanBetul = 0
for nomSoalan in range (1, bilSoalan+1):

    nom1 = random.randint(0,9)
    nom2 = random.randint(0,9)

    prompt = f"Soalan {nomSoalan}: {nom1} x {nom2} = " 

    try:
        pyip.inputStr(prompt, allowRegexes = [f"^{nom1 * nom2}$"],
                              blockRegexes = [('.*', 'Jawapan salah!')],
                              timeout=5, limit=1)
    except pyip.TimeoutException:
        print("Masa tamat!")
    except pyip.RetryLimitException:
        print("Peluang mencuba sudah habis")
    
    else:
        print('Jawapan anda betul!')
        jawapanBetul += 1
    
    time.sleep(2)

print(f'Markah Keseluruhan: {jawapanBetul} / {bilSoalan}')


#3rd mini program 
print('Nasi Lemak maker')
print('Hello, welcome to my Nasi Lemak shop 😊')
import pyinputplus as pyip

#define harga 
harga_NL = {
    "Nasi Lemak Kukus": 8, 
    'Nasi Lemak Daun Pisang': 5, 
    'Nasi Lemak vegetarian': 5
}

harga_protein = {
    'ayam': 10, 'daging': 15, 'kambing': 20, 'vegetarian':5
    }

harga_telur = {'goreng': 3, 'dadar': 3, 'rebus':2}

options = [
    "Nasi Lemak Kukus", 
    'Nasi Lemak Daun Pisang', 
    'Nasi Lemak vegetarian']
pilihJenis = pyip.inputMenu(
    options,
    prompt="Sila pilih jenis nasi lemak\n", 
    numbered=True)
print(f'Anda memilih {pilihJenis}')

protein = ['ayam', 'daging', 'kambing', 'vegetarian']
pilihProtein = pyip.inputMenu(
    protein,
    prompt="Sila pilih jenis lauk\n",
    lettered=True)
print(f'Anda memilih {pilihJenis} berlauk {pilihProtein}')

telur = pyip.inputYesNo(prompt='Nak telur tak? (yes/no)\n')
if telur == 'yes':
    telurOption=['goreng', 'dadar', 'rebus']
    pilihTelur=pyip.inputMenu(
        telurOption,
        prompt='Awak nak telur yang mana?\n')
    print(f"Anda mahu telur {pilihTelur} dengan nasi lemak anda")
else:
    pilihTelur = None
    print('Kami tidak akan masukkan telur dalam nasi lemak anda')

accompaniment = ['kacang', 'ikan bilis', 'timun']
responses = {}
for item in accompaniment:
    responses[item]=pyip.inputYesNo(prompt=f'Awak nak {item} tak?\n')
print('Awak mahu: ')
for item, response in responses.items():
    print(f'* {item.capitalize()}: {'Ya' if response == 'yes' else 'Tak'}')

bilNasi = pyip.inputNum(prompt='berapa bungkus awak nak beli?\n')

jumlah = harga_NL[pilihJenis] + harga_protein[pilihProtein]
if pilihTelur:
    jumlah += harga_telur[pilihTelur]

print(f'Terima kasih, kami akan siapkan {bilNasi} bungkus nasi lemak')
print(f'Jumlah yang anda perlu bayar ialah RM{jumlah * bilNasi}')
print('Sila tunggu di depan kaunter')
print('kami akan panggil nombor bila dah siap 😊')
