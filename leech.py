import socket,sys

HOST = sys.argv[1] # The remote host
PORT = 1414       # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
FILE_NAME=s.recv(1024)
writer = open(FILE_NAME,"wb")
data = s.recv(1024)
while data:
    writer.write(data)
    data=s.recv(1024)
writer.close()
s.close()
print "[+]Successfully Donwload [%s]"%FILE_NAME
