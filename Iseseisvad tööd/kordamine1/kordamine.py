import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("Server will start on host: ", host)
port = 8080
s.bind((host.port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connection")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, "has connected to the server and is now onlline ...")
print("")
