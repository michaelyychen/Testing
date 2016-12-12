import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
usage_statement = 'help statement!!!!!'
port = int(port)

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((host,port))

while 1:
	print ('1. Enter Your User Name (ex: login <username>)')
	print ('2. Print usage statements (ex: help)')
	print ('3. Exit the client program (ex: exit)')
	sentence = raw_input('$ ')
	clientSocket.send(sentence)


	loginreceived = clientSocket.recv(1024)
	print (loginreceived)
	if loginreceived =="client exit":
		break
	if loginreceived =="print usage":
		print(usage_statement)
	if loginreceived =="invalid command":
		print(usage_statement)
	if loginreceived =="login success":
	    while 1 :
	        cmd = raw_input('>>> ')
	        if cmd =="help":
	        	print(usage_statement)
	        	continue
	        clientSocket.send(cmd)
	        received = clientSocket.recv(1024)
	        print (received)
	        if received =="logout success":
	        	break
	        elif received =="invalid command":
	        	print(usage_statement)

