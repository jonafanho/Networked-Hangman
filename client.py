# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:16:01 2019

@author: JongHyuk
"""

from socket import *

from _thread import *


serverName = 'localhost'
serverPort = 43500
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print( "You have successfully connected!!")

#this function will be called using thread. Simple receiving function
def recv(socket):
    while True:
        msg = clientSocket.recv(1024)
        print(msg.decode())

name = input("Please enter your name:")

while 1:
    print("Please enter your guess")
    start_new_thread(recv,(clientSocket,))
    msg = input()

    msgOut = name +": "+msg
    clientSocket.send(msg.encode())
    


 
    