from socket import *

activeUser = []
activeGroup = []
currentUser = ""
authenticated = False


class Post:
    def __init__(self, postID, subject, author, date, data):
        self.postID = postID
        # self.groupname =groupname
        self.subject = subject
        self.author = author
        self.date = date
        self.data = data


class Group:
    def __init__(self, groupID, name):
        self.groupID = groupID
        self.name = name
        self.postArray = []
        self.subscribedUsers = []


#initialize some groups and posts
group1 = Group(0,"comp.programming")
group2 = Group(1,"comp.os.threads")
group3 = Group(2,"comp.lang.c")
group4 = Group(3,"comp.lang.python")
group5 = Group(4,"comp.lang.javascript")
group6 = Group(5,"comp.stonybrook")
group7 = Group(6,"comp.nyu")
group8 = Group(7,"comp.c++")
group9 = Group(8,"comp.ruby")
group10 = Group(9,"comp.java")
group11 = Group(10,"comp.object")
group12 = Group(11,"comp.algorithm")
group13 = Group(12,"comp.recursion")
group14 = Group(13,"comp.os")
group15 = Group(14,"comp.lang.assembly")


# self.subscribedUsers = []


# initialize some groups and posts


activeGroup.append(group1)
activeGroup.append(group2)
activeGroup.append(group3)
activeGroup.append(group4)
activeGroup.append(group5)
activeGroup.append(group6)
activeGroup.append(group7)
activeGroup.append(group8)
activeGroup.append(group9)
activeGroup.append(group10)
activeGroup.append(group11)
activeGroup.append(group12)
activeGroup.append(group13)
activeGroup.append(group14)
activeGroup.append(group15)

for num in range(0, 44):
    postid = (num // 15) + 1
    newPost = Post(postid, "This is post" + str(postid), "Author " + str(postid), "Sat, Nov 12 19:34:03 EST 2016",
                   "Testestsetestset" + str(postid))

    groupToAdd = getattr(activeGroup[num % 15], 'postArray')
    groupToAdd.append(newPost)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print ('The server is ready to receive, the port number is ' + str(serverPort))
while 1:
    (connectionSocket, addr) = serverSocket.accept()
    
    commandsAll = connectionSocket.recv(1024).split()
    firstcommand = commandsAll[0]
    if firstcommand == "login":
        userID = commandsAll[1]

        print (userID)

        if userID not in activeUser:
            activeUser.append(userID)
            currentUser = userID
            authenticated = True

            #Send protocol back to client
            connectionSocket.send("login success")



        else:
            # send protocol to tell client enter another id
            connectionSocket.send("login failed")


    while authenticated == True:
        firstcommand =""
        buffer = ""
        commandsAll = connectionSocket.recv(1024).split()

        firstcommand = commandsAll[0]
        if firstcommand == "ag":
            index = 0  # index in the activeGroup Array
            quit = False
            optionalcommand = 5

            if len(commandsAll) > 1:
                optionalcommand = commandsAll[1]
                #here uses the default value for N -> showing N items at a time


            while index < optionalcommand:
                if currentUser not in getattr(activeGroup[index], 'subscribedUsers'):
                    buffer += str(index) + '. ( )     ' + getattr(activeGroup[index], 'name') + '\n'
                else:
                    buffer += str(index) + '. (s)     ' + getattr(activeGroup[index], 'name') + '\n'
                index += 1
            connectionSocket.send(buffer)

            while quit==False:
                
                buffer = "'"

                subcommand = connectionSocket.recv(1024).split()

                if subcommand[0] == 's':
                    temp = 1
                    while temp<len(subcommand):
                        ##subscribe to index + argument group
                        groupToSubscribe = getattr(activeGroup[int(subcommand[temp])], 'subscribedUsers')
                        print ("Subscribing group " + getattr(activeGroup[int(subcommand[temp])],'name'))
                        # activeGroup[groupToSubscribe].getUserArray.AddtoGroup
                        groupToSubscribe.append(currentUser)
                        temp += 1

                elif subcommand[0] == 'u':
                     temp = 1
                     while temp<len(subcommand):
                        ##subscribe to index + argument group
                        groupToUnsubscribe = getattr(activeGroup[int(subcommand[temp ])], 'subscribedUsers')
                        print ("UNSubscribing group " + getattr(activeGroup[int(subcommand[temp])],'name'))
                        # activeGroup[groupToSubscribe].getUserArray.Remove
                        groupToUnsubscribe.remove(currentUser)
                        temp += 1

                elif subcommand[0] == 'n':
                    # list next set of group
                    temp = 0

                    while temp < optionalcommand:
                        if index > len(activeGroup)-1:
                            buffer += "------All Group Has Been Shown------"+'\n'
                            quit = True
                            break
                        elif currentUser not in getattr(activeGroup[index], 'subscribedUsers'):
                            buffer += str(index) + '. ( )     ' + getattr(activeGroup[index], 'name') + '\n'
                        elif currentUser  in getattr(activeGroup[index], 'subscribedUsers'):
                            buffer += str(index) + '. (s)     ' + getattr(activeGroup[index], 'name') + '\n'
                        index += 1
                        temp += 1
                    connectionSocket.send(buffer)

                elif subcommand[0] == 'q':

                    temp = 0

                    while temp < len(activeGroup):
                        ##### print all group before finishing
                        if currentUser not in getattr(activeGroup[temp], 'subscribedUsers'):
                            buffer += str(temp) + '. ( )     ' + getattr(activeGroup[temp], 'name') + '\n'
                        else:
                            buffer += str(temp) + '. (s)     ' + getattr(activeGroup[temp], 'name') + '\n'
                        temp += 1
                    connectionSocket.send(buffer)
                    quit == True

        elif firstcommand == "sg":
            index = 0  # index in the activeGroup Array
            buffer = ""
            quit = False
            optionalcommand = 5
            if len(commandsAll) > 1:
                optionalcommand = commandsAll[1]
            # here uses the default value for N -> showing N items at a time

            while index < optionalcommand:
                # list all the group up to N
                if currentUser in getattr(activeGroup[index], 'subscribedUsers'):
                    buffer += index + '. POST### ' + getattr(activeGroup[index], 'name') + '\n'
                    index += 1
                connectionSocket.send(buffer)

            while quit == False:

                buffer = "'"
                subcommand = connectionSocket.recv(1024).split()
                if subcommand == 'u':
                    temp = 1
                    while temp < len(subcommand):
                        ##subscribe to index + argument group
                        groupToUnsubscribe = getattr(activeGroup[int(subcommand[temp + 1])], 'subscribedUsers')
                        # activeGroup[groupToSubscribe].getUserArray.Remove
                        groupToUnsubscribe.remove(currentUser)
                        temp += 1
                elif subcommand == 'n':
                    temp = 0
                    while temp < optionalcommand:
                        if index > len(activeGroup):
                            buffer += "------All Group Has Been Shown------"
                            quit = True
                            break
                        if currentUser in getattr(activeGroup[index], 'subscribedUsers'):
                            buffer += index + '. POST###' + getattr(activeGroup[index], 'name') + '\n'

                        index += 1
                        temp += 1
                    connectionSocket.send(buffer)

                elif subcommand == 'q':
                    temp = 0

                    while temp < len(activeGroup):
                        ##### print all group before finishing
                        if currentUser in getattr(activeGroup[temp], 'subscribedUsers'):
                            buffer += temp + '. POST###  ' + getattr(activeGroup[temp], 'name') + '\n'

                        temp += 1
                    connectionSocket.send(buffer)
                    quit == True


        elif firstcommand == "rg":
            if commandsAll[1] in activeGroup:
                defaultN = 5
                if len(commandsAll) > 2:
                    defaultN = commandsAll[2]
                    index = activeGroup.index(commandsAll[1])
                    if (defaultN > len(activeGroup[index].postArray)):
                        defaultN = len(activeGroup[index].postArray)
                for i in range(0,defaultN):
                    connectionSocket.send(activeGroup[index].postArray[i])


                else:
                    print ('you are not in the group')

                while 1:
                    subcommand = connectionSocket.recv(1024)

                    if subcommand[0] in range(0,defaultN):
                        while 1:
                            subsubcommand = connectionSocket.recv(1024)
                            if subsubcommand[0] == 'n':
                                pass
                            elif subsubcommand[0] == 'q':
                                break
                    elif subcommand[0] == 'r':
                        pass
                    elif subcommand[0] == 'n':
                        pass
            elif subcommand[0] == 'p':
                pass
            elif subcommand[0] == 'q':
                break

        elif firstcommand == "logout":
            # remove user from activeUser array
            activeUser.remove(currentUser)
            authenticated = False
            connectionSocket.send("logout success")



