print("Phone number and email address extractor\n")

#read the whole file
fhand = open('4-regex.txt')
read = fhand.read()
print("Content of text in 4-regex.txt file:")
print(read)
print('-end of text-'.center(55))
print("Word counter: ", len(read.split()))

#create a regex for phone numbers
import re

nomTelRegex = re.compile(r''' 

(\d{3})                             # mobile carrier code (group 0)
(\s|-|\.)?                          # separator  (group 1)
(\d{7})                             # 7 digits   (group 2)
 (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension  (group 3)        
''', re.VERBOSE)

#create a regex for email addresses
emailRegex = re.compile(r''' 
[a-zA-Z0-9._%+-]+                   # username
@                                   # @ symbol
[a-zA-Z0-9._%+-]+                   # domain name
\.[a-zA-Z]{2,4}                     # dot something                    
''', re.VERBOSE)

#Find all matches in the text
matches = []
for group in nomTelRegex.findall(read):
    nomTel = f"{group[0]}-{group[2]}"
    if group[3]:
        nomTel += f" {group[3]}"
    matches.append(nomTel)

for email in emailRegex.findall(read):
    matches.append(email)

# print results
if len(matches) > 0:
    print("Matches found: ")
    print("\n".join(matches))
else:
    print('No phone numbers or email addresses found')