import sys, time, os
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
usage_statement = 'Usage statements:\n'
usage_statement2 = 'login <username>:\tlogin with your user ID\n'
usage_statement3 = 'help:\tprints a list of supported commands and sub-commands\n'
usage_statement4 = 'help:\tprints a list of supported commands and sub-commands\n'
usage_statement5 = 'ag N:\tIt takes an optional argument, N, and lists the names of all existing discussion groups, N groups at a time, numbered 1 to N. If N is not specified, a default value is used.\n'
					

port = int(port)

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((host,port))
isRunning = True
while isRunning==True:
	print ('1. Enter Your User Name (ex: login <username>)')
	print ('2. Print usage statements (ex: help)')
	print ('3. Exit the client program (ex: exit)')
	sentence = raw_input('$ ')
	username = ''
	sentence_list=sentence.split()
	if sentence_list[0]=='login' and len(sentence_list)>=2:
		username = sentence_list[1]
		file_name = username+'.txt'
		if os.path.isfile(file_name):
			text_file = open(file_name, "r")
			history = text_file.read()
			text_file.close()
			print(history)
			print(sentence + ' ' + history)
			#sentence = sentence + ' ' + history


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
	        	clientSocket.send('send data')
	        	data = clientSocket.recv(1024)
	        	text_file2 = open(username+".txt", "w")
	        	text_file2.write(data)
	        	text_file2.close()
	        	isRunning=False
	        	break
	        elif received =="invalid command":
	        	print(usage_statement)

