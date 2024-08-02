#How to use webbrowser
import webbrowser
webbrowser.open("https://www.python.org")

#Launch map in the web browser
import webbrowser
import urllib.parse

alamat = 'Muzium Negara, Jalan Damansara, 50566 Kuala Lumpur, Malaysia'

#URL-encode the address
encoded_address = urllib.parse.quote(alamat)

#construct the goole maps URL
url = f'https://www.google.com/maps/search/?api=1&query={encoded_address}'

#open the URL in the default web browser
webbrowser.open(url)

#open all links on a page in a separate browser tabs
import webbrowser

urls = [
    'https://automatetheboringstuff.com/',
    'https://www.py4e.com/',
    'https://en.wikipedia.org/wiki/SpongeBob_SquarePants'
]

for url in urls:
    webbrowser.open_new_tab(url)

#open the browser to the URL for my local weather
import webbrowser

urlCuaca = 'https://weather.com/weather/today/l/4730af035e999b2a2e62d06178d18fb3cd2b036ee65eb6b2b876fbac27075920'
webbrowser.open(urlCuaca)



