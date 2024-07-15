print("hello")

#loops
n = 3
while n > 0:
    print(n)
    n = n-1
print("Hooray!")
print(n)

#Definite Loop

for i in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] :
    print(i)
print("Off you go!")

#Definite loop with strings
friends = ["Asyikin", "Liam", "Austin", "Lily"]
for friend in friends:
    print("Selamat Hari Raya,", friend)
print("Ok dah siap")

# Loop Idioms

#Looping through a set
print("Sebelum")
for benda in [99, 56, 43, 18, 72, 402]:
    print(benda)
print("Selepas")

#largest number
largest_so_far = -2
print("Sebelum", largest_so_far)
for nombor in [99, 56, 43, 18, 72, 402]:
    if nombor > largest_so_far:
        largest_so_far = nombor
    print(largest_so_far, nombor)
print("Selepas", largest_so_far)

#Counting in a loop


