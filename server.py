# server.py
# This is the server file for the chat program.
# Includes socket sending and receiving as well as a couple of bots.

from socket import *
import sys
import random
import time
import math
import urllib.request

# set up socket to wait for connections
serverSocket = socket(AF_INET, SOCK_STREAM) # TCP (reliable)
# check for command line arguments
if len(sys.argv) >= 2:
	# if at least two arguments, grab the second argument to use as server port
	serverPort = int(sys.argv[1])
else:
	# if no second argument
	serverPort = 43500
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # make port reusable
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
serverSocket.setblocking(0) # make socket non-blocking
print("Server ready on port " + str(serverPort))

clients = [] # list of connected clients

stop = 0 # flag to exit the loop

# omitting while loop means the server will run once!
while 1:
	# accept connection from client
	try:
		connectionSocket, addr = serverSocket.accept()
		clients.append((connectionSocket, addr)) # add new client to the master list
		if len(greeting) > 0:
			connectionSocket.send(greeting.encode("utf-8"))
		print(str(len(clients)) + " client(s) connected")
	except:
		i=0 # do nothing
	# loop through all connected clients
	for client in clients:
		# try to receive data from each client
		try:
			sentence = client[0].recv(1024)
		except:
			sentence = ""
		if len(sentence) > 0:
			print(sentence.decode("utf-8"))
	if stop == 1:
		# loop through all clients and close connection
		for client in clients:
			client[0].close()
		exit() # exit python program