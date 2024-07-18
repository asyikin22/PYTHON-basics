print('hello regex')

#using find()
print('using find()')
fhand = open('email.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('From: ') >=0:
        print(line)

#using re.search()
print('using re.search()')
import re

xhand = open ('email.txt')
for line in xhand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)


#matching and extractign data
import re
y = 'my 3 favorite numbers are 99, 19, 20'
z = re.findall('[0-9]+', y)
print(z)

#splitting strings
print('splitting strings using regex')
import re
ghand = open ('email.txt')
for line in ghand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)
        
        a = re.findall('@([^ ]*)', line)
        print(a)

#escape character
import re 
k = 'I just received $20 for nasi lemak'
l = re.findall('\$[0-9]+', k)
print(l)