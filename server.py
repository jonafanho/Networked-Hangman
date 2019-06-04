from socket import *
from random import *
from select import *
import sys


serverPort = 43500
serverSoc = socket(AF_INET,SOCK_STREAM)
serverSoc.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serverSoc.bind (('',serverPort))
serverSoc.listen(5)
serverSoc.setblocking(0)
clients = [serverSoc]
usr = []
hangman = [" ------------\n|           \n|           \n|         \n|        \n|            \n-------------\n"
           ," ------------\n|      |     \n|           \n|         \n|         \n|            \n-------------\n"
           ," ------------\n|      |     \n|      O     \n|         \n|         \n|            \n-------------\n"
           ," ------------\n|      |     \n|      O     \n|      |     \n|         \n|            \n-------------\n"
           ," ------------\n|      |     \n|      O     \n|     /|    \n|         \n|            \n-------------\n"
           ," ------------\n|      |     \n|      O     \n|     /|\    \n|         \n|            \n-------------\n"
           ," ------------\n|      |     \n|      O     \n|     /|\    \n|     /      \n|            \n-------------\n"
           ," ------------\n|      |     \n|      O     \n|     /|\    \n|     / \    \n|            \n-------------\n"]
wrd = "hello"
word = list(wrd)
msgSend = ''
print("Server Started")
i = 0
letters = len(word)*"_"
letters = list(letters)
"""Select method to connect multiple clients, send, and receive msgs to, from clients"""
while True:
    readable,writable, exception = select(clients,clients,[])
    for s in readable:
        if s == serverSoc:
            conn,addr = s.accept()
            #when each client connects, the server prints address
            print(addr,"has Connected")
            clients.append(conn)
        else:
            """Use try method to avoid abortion of server when each client disconnects"""
            try:
                data = s.recv(1024).decode()
                
                try:
                    
                    if data:
                        if data not in word:
                            print(data)
                            print(letters)
                            i+=1
                            if i > 7:
                                i=0
                                msgsend = "Game over!"
                            else:
                                let = str(letters)
                                msgsend = hangman[i] + let
                        else:
                            if len(data) is 1:
                                corr = wrd.find(data)
                                letters[corr] = data
                            letter = str(letters)
                            msgsend = hangman[i]+"Correct!\n" +letter
                        for ss in writable:
                            ss.send(msgsend.encode())
                except:
                    continue
            
            except:
                continue
        
                
       