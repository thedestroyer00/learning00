#To create a server 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket , address = s.accept()
	print(f"connected to {address} client")
	clientsocket.send(bytes("Welcome to the server!", "utf-8"))
	
#To create a client

import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv()
print(msg.decode("utf-8")
