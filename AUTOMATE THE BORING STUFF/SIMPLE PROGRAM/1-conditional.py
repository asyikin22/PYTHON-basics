# Guess the number

import random
luckyNum = random.randint(1, 15)
print("I am thinking of a number between 1 and 15")

#ask the player to guess 5 times
for tekaNombor in range (1, 6):
    print("Teka nombor saya")
    teka = int(input())
    
    if teka < luckyNum:
        print("Tekaan anda terlalu rendah")
    
    elif teka > luckyNum:
        print("Tekaan anda terlalu tinggi")
    
    else:
        break

if teka == luckyNum:
    print(f"Congrats, you got it right! My number is {luckyNum}")

else: 
    print(f"I am sorry, you are wrong, my chosen number is {luckyNum}")


