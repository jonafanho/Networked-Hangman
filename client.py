from socket import *
from _thread import *
import sys

# set up socket to connect to server
clientSocket = socket(AF_INET, SOCK_STREAM) # TCP socket
# check for command line arguments
if len(sys.argv) >= 2:
	# if at least two arguments, grab the second argument to use as server name
	serverName = sys.argv[1]
else:
	# if no second argument
	serverName = "localhost"
if len(sys.argv) >= 3:
	# if at least three arguments, grab the third argument to use as server port
	serverPort = int(sys.argv[2])
else:
	# if no third argument
	serverPort = 43500
try:
	# try connecting to custom server name and port
	clientSocket.connect((serverName, serverPort))
	print("Connected to " + serverName + ":" + str(serverPort))
except:
	# if that doesn't work, try localhost port 43500
	clientSocket.connect(("localhost", 43500))
	print("Connected to localhost:43500")

print("You have successfully connected!")

# this function will be called using a thread
# it is a receiving function to read messages from the server.
def recv(socket):
	while True:
		msg = clientSocket.recv(1024).decode()
		if msg.startswith("/"): # show message if it starts with /<myname>
			if msg.startswith("/" + name + " "):
				print(msg.replace("/" + name + " ", ""))
		elif msg.startswith("~"): # don't show message if it starts with ~<myname>
			if not msg.startswith("~" + name + " "):
				print(msg[msg.find(" ") + 1:])
		else: # print all other messages
			print(msg)

# ask for name first, then send the "join" message to the server
name = input("Please enter your name: ").replace(" ", "_").upper()
clientSocket.send(("join " + name).encode())
# separate thread for receiving messages
start_new_thread(recv,(clientSocket,))

while 1:
	msg = input()
	clientSocket.send((name + ": " + msg).encode())