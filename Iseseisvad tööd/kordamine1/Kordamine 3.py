import socket

s = socket.socket()#loob socketi objekti
host = socket.gethostname() #saad hosti nime
port = 8080 #port 8080
s.bind((host,port)) #saab serveri aadressi ja pordi
s.listen(1) #kuulab kasutajad
print(host) #prindib hostinime
print("waiting for any incoming connections ...") #prindib jutumärkides oleva teksti
conn, addr = s.accept() #kuulab kasutajad
print(addr, "has connected to the server") ##kontrollib kas kasutaja on ühendatud

filename = input(str("Please enter the filename of the file : ")) #prindib jutumärkides oleva teksti ja laseb sinan taha kirjutada failinime
file = open(filename , 'rb') #avab faili
file_data = file.read(1024) #loeb faili
conn.send(file_data) #saadab faili
print("data has been transmitted successfully") #prindib et fail on sadetud