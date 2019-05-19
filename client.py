# client.py
# This is the client file for the chat program.
# Includes socket sending and receiving.

from socket import *
import threading
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

name = input("Username: ") # ask for user's name, will be used in chat messages
stop = 0 # flag to stop the input thread

# this function repeatedly gets the terminal input and sends it to the server
def getInput():
	send = input()
	global room # make the room variable readable on a separate thread
	if len(send) > 0:
		try:
			clientSocket.send(send.encode("utf-8")) # encode and send the message
		except:
			print("Error sending message!")
	global stop
	if stop == 0:
		getInput() # loop function back to itself

# start a thread to get user input so that it doesn't block the receiving program
threading.Thread(target=getInput).start()

# loop client forever
while 1:
	try:
		data = clientSocket.recv(1024).decode("utf-8") # read messages from server
		if len(data) > 0:
			print(data)
	except:
		# if there's an error receiving messages, assume something bad happened and exit
		break

stop = 1 # tell the input thread to stop
# close the connection
clientSocket.close()