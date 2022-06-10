import socket #import socketib
s = socket.socket() #loob socket objekti
host = input(str("Please enter the host address of the sender : ")) #saab sisestada hosti aadressi
port = 8080 #port 8080
s.connect((host,port)) #saab serveri aadressi ja pordi
print("Connected ...") #prindib connected

filename = input(str("Please enter a filename for the incoming file : ")) #saab sisestada failinime
file  =open(filename, 'wb') #avab faili
file_data = s.recv(1024) #saadab faili
file.write(file_data) #kirjutab faili
file.close() #sulgeb faili
print("file has been received successfully.") #prindib et fail on edukalt saadetud