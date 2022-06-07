import socket
import sys
import time

s = socket.socket()
host = input(str("Please enter the hostname of the server :"))
s.connect((host.port))
print("connecter to chat server")
