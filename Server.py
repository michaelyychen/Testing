from socket import *

activeUser =[]
activeGroup = []


class Post:
    def __init__(self):
        self.postID = -1
        self.groupname =""
        self.subject =""
        self.author = ""
        self.date = ""
        self.data= ""


class Group:
    def __init__(self):
        self.groupID = -1
        self.name = ""
        self.postArray =[]
        self.subscribedUsers=[]




serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive, the port number is '+ str(serverPort))
while 1:
    connectionSocket, addr = serverSocket.accept()

    commandsAll = connectionSocket.recv(1024).split(" ")
    firstcommand = commandsAll[0]
    if firstcommand=="login":
        userID = commandsAll[1]
        if userID not in activeUser:
            activeUser.append(userID)
            #Send protocol back to client
        else:
            # send protocol to tell client enter another id
            pass

    elif firstcommand=="ag":
        index = 0               # index in the activeGroup Array
        optionalcommand = commandsAll[1]
        if optionalcommand == None:
            optionalcommand = 5
            #here uses the default value for N -> showing N items at a time

        while index<optionalcommand:
            # list all the group up to N
            index += 1
            pass



        while 1:
            subcommand = connectionSocket.recv(1024).split(" ")
            if subcommand[0] == 's':
                temp = 0
                while subcommand[temp+1]!=None:
                    ##subscribe to index + argument group
                    groupToSubscribe = index + subcommand[temp+1]
                   # activeGroup[groupToSubscribe].getUserArray.AddtoGroup
                    temp+=1


            elif subcommand[0] =='u':
                temp = 0
                while subcommand[temp + 1] != None:
                    ##subscribe to index + argument group
                    groupToSubscribe = index + subcommand[temp + 1]
                    # activeGroup[groupToSubscribe].getUserArray.Remove
                    temp +=1


            elif subcommand[0] == 'n':
                # list next set of group
                temp =0
                while temp<optionalcommand :
                    if index>len(activeGroup):
                        ##### QUIT if no more active groups to show
                        break
                    index +=1
                    temp +=1
            elif subcommand[0] == 'q':
                temp = 0

                while index > len(activeGroup):
                    ##### print all group before finishing

                    temp += 1
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
        #remove user from activeUser array
        pass


