print('beautiful soup')

#retrieve anchor tag
#url example: http://www.dr-chuck.com/page1.htm
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# # retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

#beautiful soup and requests
#url example: http://data.pr4e.org/romeo.txt
from bs4 import BeautifulSoup
import requests

url = 'http://data.pr4e.org/romeo.txt'

response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')