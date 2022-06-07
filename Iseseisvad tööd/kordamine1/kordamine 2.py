import socket
import sys
import time

s = socket.socket() #loob uue pistiku
host = input(str("Please enter the hostname of the server :")) #võtab kasutaja inputi
port = 8080 #port on 8080
s.connect((host,port)) #ühendab pistikupesa aadressile
print("connected to chat server") #prindib et connected to chat
while 1: #while loop
    incoming_message = s.recv(1024) #võtab infot
    incoming_message = incoming_message.decode()
    print("Server: ", incoming_message) #prindib "server:" ja serverist kirjutatud sõnumi
    print("") #prindib tühiku
    message = input(str(">> ")) #prindib nooled ja võtab kasutaja sisestatud sõnumi
    message = message.encode() #kodeerib sõnumi
    s.send(message) #
    print("message has been sent...") #prindib teksti sulgude sees
    print("") #prindib tühiku