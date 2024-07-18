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