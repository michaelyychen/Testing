import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]

port = int(port)

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((host,port))
sentence = raw_input('Please Enter Your User Name (ex: login <username>):')
clientSocket.send(sentence)


loginreceived = clientSocket.recv(1024)
print (loginreceived)
if loginreceived =="login success":
    while 1 :
        cmd = raw_input('>>> ')
        clientSocket.send(cmd)
        received = clientSocket.recv(1024)
        print (received)
        if received =="logout success":
        	break


