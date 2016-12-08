from socket import *

activeUser =[]
class Post :
    def __init__(self):
        self.postID = -1
        self.groupname =""
        self.subject =""
        self.author = ""
        self.date = ""
        self.data= ""

class Group :
    def __init__(self):
        self.groupID = -1
        self.name = ""
        self.postArray =[]




serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive, the port number is '+ str(serverPort))
while 1:
    connectionSocket, addr = serverSocket.accept()

    commandsAll = connectionSocket.recv(1024).split(" ")
    firstcommand = commandsAll[0]
    if(firstcommand=="login"):
        userID = commandsAll[1]
        if not userID in activeUser:
            activeUser.append(userID)
            #Send protocol back to client
        else:
            # send protocol to tell client enter another id
            pass

    elif firstcommand=="ag":
        while 1:
            subcommand = connectionSocket.recv(1024)
            if subcommand == 's':
                pass
            elif subcommand =='u':
                pass
            elif subcommand == 'n':
                pass
            elif subcommand == 'q':
                break


    elif firstcommand == "sg":
        while 1:
            subcommand = connectionSocket.recv(1024)

            if subcommand =='u':
                pass
            elif subcommand == 'n':
                pass
            elif subcommand == 'q':
                break

    elif firstcommand == "rg":
        pass

    elif firstcommand == "logout":
        pass


