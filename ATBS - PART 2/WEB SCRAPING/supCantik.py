#creating BS Object from HTML
from bs4 import BeautifulSoup

pathHTML = r'C:\Users\ASYIKIN\OneDrive\Desktop\PYTHON\ATBS - PART 2\WEB SCRAPING\index.html'

#open and read the local HTML file
with open(pathHTML, 'r', encoding='utf-8') as file:
    kandunganHTML = file.read()

#create a BS object and parse the HTML content
contohSup = BeautifulSoup(kandunganHTML, 'html.parser')

#print the type of the BS object
print(f'Type of BS object: {type(contohSup)}')

#select() method
element = contohSup.select('#author')
print(f'Type of #author element: {type(element)}')
print(len(element))
print(type(element[0]))
print(str(element[0]))
print(element[0].getText())
print(element[0].attrs)

#getting data from an Element's attribute
ElemSpan = contohSup.select('span')[0]
print(f'HTLM representation of span tag: {str(ElemSpan)}')
print(f'The "id": {ElemSpan.get('id')}')
print(f'The attribute of tag span {ElemSpan.attrs}')


# Find element with select() method - URL

# #creating BS Object from URL
# import requests, bs4
# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# supAyam = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(supAyam))

