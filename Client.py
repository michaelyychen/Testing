import sys, time, os
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
ut = '\n'
ut=ut + 'Usage statements:\n\n'
ut=ut + 'login <username>:\tlogin with your user ID\n'
ut=ut + 'help:\tprints a list of supported commands and sub-commands\n'
ut=ut + 'logout:\tIt logs out the current user, and terminate the client program after all proper updates are completed\n'
ut=ut + 'ag N:\tIt takes an optional argument, N, and lists the names of all existing discussion groups, N groups at a time, numbered 1 to N. If N is not specified, a default value is used.\n'
ut=ut + 'sub-commands for ag N:\n'
ut=ut + 's - subscribe to groups. It takes one or more numbers between 1 and N as arguments.\n'
ut=ut + 'u - unsubscribe. It has the same syntax as the s command, except that it is used to unsubscribe from one or more groups.\n'
ut=ut + 'n - lists the next N discussion groups. If all groups are displayed, the program exits from the ag command mode\n'
ut=ut + 'q - exits from the ag command, before finishing displaying all groups\n'
ut=ut + 'sg N:\tIt takes an optional argument, N, and lists the names of all subscribed groups, N groups at a time, numbered 1 to N.  If N is not specified, a default value is used.\n'
ut=ut + 'rg <gname> N:\tdisplays the (status - new or not, time stamp, subject line) of all posts in the group gname, N posts at a time. If N is not specified, a default value is used. gname must be a subscribed group.\n'
ut=ut + 'sub-commands for rg <gname> N:\n'
ut=ut + '[id] - a number between 1 and N denoting the post within the list of N posts to display. The content of the specified post is shown.\n'
ut=ut + '\tsub-commands for [id]:\n'
ut=ut + '\tn - would display at most N more lines of the post content. \n'
ut=ut + '\tq - would quit displaying the post content. The list of posts before opening the post is shown again with the post just opened marked as read. \n'
ut=ut + 'r - marks a post as read. It takes a number or range of number as input.\n'
ut=ut + 'n - lists the next N posts. If all posts are displayed, the program exits from the rg command mode\n'
ut=ut + 'p - post to the group. This sub-command allows a user to compose and submit a new post to the group. \n'
ut=ut + 'q - exits from the rg command\n'
usage_statement=ut
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
			sentence = sentence + ' ' + history

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
