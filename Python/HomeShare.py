import sys,socket,re

def Server(FILE_NAME,PORT=1416,HOST=''):
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

def Client(SERVER_IP,PORT=1416):
    CONNECTOR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CONNECTOR.connect((SERVER_IP, PORT))
    print '\n[+]Connected to the distributor [ %s ]'%SERVER_IP
    FILE_NAME=CONNECTOR.recv(1024)
    writer = open(FILE_NAME,"wb")
    print '[+]Downloading %s'%FILE_NAME
    data = CONNECTOR.recv(1024)
    while data:
        writer.write(data)
        data=CONNECTOR.recv(1024)
    writer.close()
    CONNECTOR.close()
    print "[+]Successfully Donwload [%s]"%FILE_NAME



if __name__ == '__main__':

    
    if len(sys.argv)<2:
        for i in range(0,100):
            sys.stdout.write("\b\b\b"+str(i))
        print "HomeShare\n"+"="*9
        print "Usage:\n"
        print "%s [FILE_NAME]\n\n"%sys.argv[0]
        print "FILE_NAME : mean server or Distributor"
        print "\t | %s FILE_NAME"%sys.argv[0]
        print '\n'
        print "without argument means Downloader"
        print "="*33
        print "\n\n[+]Searching for Distributor ...",
        IP=re.findall('\d+\.\d+\.\d+\.',socket.gethostbyname(socket.gethostname()))[0]
        for ip in range(0,256):
            pers = int((ip/256.0)*100) 
            sys.stdout.write("\b\b\b"+str(pers)+"%")
            sys.stdout.flush()

            try:
                Client(IP+str(ip))
                break
            except Exception, e:
               
                
                pass
            else:
                print '[-]Server or Distributor not found '
        sys.exit(0)


