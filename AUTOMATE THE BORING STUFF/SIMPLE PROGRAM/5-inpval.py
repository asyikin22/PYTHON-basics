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
