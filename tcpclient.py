
import socket 

target_host = "127.0.0.1"
target_port = 9999

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to client
client.connect((target_host,target_port))

#send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve data
response = client.recv(4096)

print response

