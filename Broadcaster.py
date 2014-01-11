import socket,sys
PORT = 1414 #defult port
HOST = ''
if len(sys.argv)==1:
   print "%s.py filename [port]\ndefult port is 1414"%sys.argv[0]
   sys.exit(1)
if len(sys.argv)==3:
      PORT = int(sys.argv[2])
FILE_NAME = sys.argv[1]

print "\t\t\t***\n"
print "[#] FILE:%s\n"%FILE_NAME
print "[#] PORT:%d\n"%PORT
print "\t\t\t***\n"
print "[+]Listening ... "

Server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Server.bind((HOST,PORT))
Server.listen(1)
Connection,address = Server.accept()
print "[+]Connected by:",address[0]

Connection.sendall(FILE_NAME)
with open(FILE_NAME, 'rb') as f:
     Connection.sendall(f.read())

print 'DONE'
