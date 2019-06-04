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
word = "hello"

jokelist =["Today at the bank, an old lady asked me to help check her balance. So I pushed her over","I bought some shoes from a drug dealer. I don't know what he laced them with, but I've been tripping all day.","My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.", "I'm so good at sleeping. I can do it with my eyes closed","H2O is water and H2O2 is hydrogen peroxide. What is H2O4?\n drinking"]

msgSend = ''
print("Server Started")
i = 0
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
                data = s.recv(1024)
                
                try:
                    # if there is data coming, then decode to print, and send the msgs out to all users
                    if data:
                        guess = data.decode()
                        if guess not in word:
                            i+=1
                            if i > 7:
                                i=0
                                msgsend = "Game over!"
                            else:
                                msgsend = hangman[i]
                            
                        else:
                            msgsend = "correct"
                        for ss in writable:
                            ss.send(msgsend.encode())
                except:
                    continue
            
            except:
                continue
        
                
       