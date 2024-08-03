print('request module\n')

#basic use case
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

print(f'Status code: {requests.codes.ok}')
print(f'\nNumber of characters in this text: {len(res.text)}')
print('\nThe following shows the first 200 characters of the text\n')
print(res.text[:200])

#Checking for error - raise for status methodd
print('\nraise_for_status method\n')
import requests
res = requests.get("https://inventwithpython.com/page_ini_tak_wujud")
res.raise_for_status()

#Checking for error - try and except statement
import requests
res = requests.get("https://inventwithpython.com/page_ini_tak_wujud")
try:
    res.raise_for_status()
except Exception as exc:
    print(f'Uh oh, there\'s a problem: {exc}')

#save downlaoded files to the hard drive
import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
print(f"Status code of the request is: {res.status_code}")
pathRomJul = r'C:\Users\ASYIKIN\OneDrive\Desktop\PYTHON\ATBS - PART 2\WEB SCRAPING\romjul.txt'
handleFile = open(pathRomJul, 'wb')
for chunk in res.iter_content(100000):
    handleFile.write(chunk)
    
handleFile.close()
