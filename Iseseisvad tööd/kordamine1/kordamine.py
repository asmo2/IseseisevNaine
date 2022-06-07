import socket
import sys
import time

s = socket.socket() #loob uue pistikupesa
host = socket.gethostname() #loob uue pistikupesa
print("Server will start on host: ", host) #prindib
port = 8080 #port 8080
s.bind((host, port)) #
print("") #prindib tühiku
print("Server done binding to host and port successfully") #prindib et serveril sai cliendiga ühendamine valmis
print("") #prindib tühiku
print("Server is waiting for incoming connection")#prindib et server ootab sissetulevad connectioni
print("") #prindib tühiku
s.listen(1)
conn, addr = s.accept()#seab muutujad ühenduse loomiseks
print(addr, "has connected to the server and is now onlline ...") #prindib et server on nüüd online
print("") #prindib tühiku
while 1: #while loop
    message = input(str(">>")) #prindib nooled
    message = message.encode() #kodeerib sõnumi
    conn.send(message) #saadab sõnumi
    print("message has been sent...") #prindib et sõnum saadeti välja
    print("") #prindib tühiku
    incoming_message = conn.recv(1024) #võtab infot
    incoming_message = incoming_message.decode() #dekodeerib sõnumi
    print("Client: ", incoming_message) #prindib client ja sissetulnud sõnumi
    print("") #prindib tühiku
