from socket import *
from _thread import *

serverName = "localhost"
serverPort = 43500
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print("You have successfully connected!")

# this function will be called using thread. Simple receiving function
def recv(socket):
	while True:
		msg = clientSocket.recv(1024)
		print(msg.decode())

name = input("Please enter your name: ").replace(" ", "_")
clientSocket.send(b"join")
start_new_thread(recv,(clientSocket,))

while 1:
	msg = input()
	clientSocket.send((name + ": " + msg).encode())