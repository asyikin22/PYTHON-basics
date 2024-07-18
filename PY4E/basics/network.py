print('make an HTTP request')

#make HTTP request 
import socket

#create a socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Define the server and port to connect to
host = 'data.pr4e.org'
port = 80

#connect to the server
socket.connect((host, port))

#send an HTTP GET request
request = "GET /romeo.txt HTTP/1.1\r\nHost: {}\r\n\r\n".format(host)
socket.send(request.encode())

#receive the response
response = socket.recv(4096)
print(response.decode())

#close the socket
socket.close()

#unicode and UTF-8

#Representing simple strings
print(ord('X'))   #88
print(ord('z'))   #122
print(ord('%'))   #37
print(ord('!'))   #33

#python3 and unicode
q = b'abc'
print(type(q))      #bytes

r = 'こんにちは'
print(type(r))      #str

#urllib

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


#reading web pages
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in fhand:
    print(line.decode().rstrip())