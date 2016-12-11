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
<<<<<<< HEAD
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

=======
# self.subscribedUsers = []


# initialize some groups and posts
group1 = Group(0, "comp.programming")
group2 = Group(1, "comp.os.threads")
group3 = Group(2, "comp.lang.c")
group4 = Group(3, "comp.lang.python")
group5 = Group(4, "comp.lang.javascript")
group6 = Group(5, "comp.stonybrook")
group7 = Group(6, "comp.nyu")
group8 = Group(7, "comp.c++")
group9 = Group(8, "comp.ruby")
group10 = Group(9, "comp.java")
group11 = Group(10, "comp.object")
group12 = Group(11, "comp.algorithm")
group13 = Group(12, "comp.recursion")
group14 = Group(13, "comp.os")
group15 = Group(14, "comp.lang.assembly")
>>>>>>> a47466daf7de638b24d9db271b70425e89589a1f

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
<<<<<<< HEAD
    groupToAdd = getattr(activeGroup[num % 15], 'postArray')
    groupToAdd.append(newPost)
=======
                   groupToAdd = getattr(activeGroup[num % 15], 'postArray')
                   groupToAdd.append(newPost)
>>>>>>> a47466daf7de638b24d9db271b70425e89589a1f

serverPort = 12003
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print ('The server is ready to receive, the port number is ' + str(serverPort))
while 1:
    (connectionSocket, addr) = serverSocket.accept()
    
    commandsAll = connectionSocket.recv(1024).split(" ")
    firstcommand = commandsAll[0]
    if firstcommand == "login":
        userID = commandsAll[1]
<<<<<<< HEAD
        print (userID)
=======
        print userID
>>>>>>> a47466daf7de638b24d9db271b70425e89589a1f
        if userID not in activeUser:
            activeUser.append(userID)
            currentUser = userID
            authenticated = True
<<<<<<< HEAD
            #Send protocol back to client
            connectionSocket.send("login success\r\n")


        else:
            # send protocol to tell client enter another id
            connectionSocket.send("login failed\r\n")


    #############ONLY IF LOGIN SUCCESSFULLY
    while authenticated == True:
        print ('Authenticated')
        commandsAll = connectionSocket.recv(1024).split()
        firstcommand = commandsAll[0]
        if firstcommand=="ag":
            print ('AG')
            index = 0               # index in the activeGroup Array
            buffer=""

            if len(commandsAll) == 1:
                optionalcommand = 5
                #here uses the default value for N -> showing N items at a time
            else:
                optionalcommand = commandsAll[1]

            while index<optionalcommand:
                # list all the group up to N
                if currentUser not in getattr(activeGroup[index],'subscribedUsers'):
                    buffer += str(index)+'. ( )     '+getattr(activeGroup[index], 'name')  +'\n'
                else:
                    buffer += str(index)+'. (s)     '+getattr(activeGroup[index], 'name') +'\n'
                index += 1
            print(buffer)
            connectionSocket.send(buffer)


            while 1:
                buffer = "'"
                subcommand = connectionSocket.recv(1024).split()
=======
            # Send protocol back to client
            connectionSocket.send("login success")
        else:
            # send protocol to tell client enter another id
            connectionSocket.send("login failed")

#############ONLY IF LOGIN SUCCESSFULLY
while authenticated == True:
    firstcommand =""
        commandsAll = connectionSocket.recv(1024).split(" ")
        print type(commandsAll)
        firstcommand = commandsAll[0]
        if firstcommand == "ag":
            # index = 0  # index in the activeGroup Array
            #
            # optionalcommand = 5
            #
            # if len(commandsAll) > 1:
            #     optionalcommand = commandsAll[1]
            # here uses the default value for N -> showing N items at a time
            
            connectionSocket.send("you are in ag option")
            
            while 1:
                buffer = "'"
                subcommand = connectionSocket.recv(1024).split(" ")
>>>>>>> a47466daf7de638b24d9db271b70425e89589a1f
                if subcommand[0] == 's':
                    temp = 0
                    while subcommand[temp + 1] != None:
                        ##subscribe to index + argument group
                        groupToSubscribe = getattr(activeGroup[index + int(subcommand[temp + 1])], 'subscribedUsers')
                        # activeGroup[groupToSubscribe].getUserArray.AddtoGroup
                        groupToSubscribe.append(currentUser)
                        temp += 1
            
            
                elif subcommand[0] == 'u':
                    temp = 0
                    while subcommand[temp + 1] != None:
                        ##subscribe to index + argument group
                        groupToUnsubscribe = getattr(activeGroup[index + int(subcommand[temp + 1])], 'subscribedUsers')
                        # activeGroup[groupToSubscribe].getUserArray.Remove
                        groupToUnsubscribe.remove(currentUser)
                        temp += 1
                
                elif subcommand[0] == 'n':
                    # list next set of group
                    temp = 0
                    while temp < optionalcommand:
                        if index > len(activeGroup):
                            buffer += "------All Group Has Been Shown------"
                            break
                        if currentUser not in getattr(activeGroup[index], 'subscribedUsers'):
                            buffer += index + '. ( )     ' + getattr(activeGroup[index], 'name') + '\n'
                        else:
                            buffer += index + '. (s)     ' + getattr(activeGroup[index], 'name') + '\n'
                        index += 1
                        temp += 1
                    connectionSocket.send(buffer)
<<<<<<< HEAD
                elif subcommand[0] == 'q':
=======
                        elif subcommand[0] == 'q':
>>>>>>> a47466daf7de638b24d9db271b70425e89589a1f
                    temp = 0
                    
                    while temp < len(activeGroup):
                        ##### print all group before finishing
                        if currentUser not in getattr(activeGroup[temp], 'subscribedUsers'):
                            buffer += temp + '. ( )     ' + getattr(activeGroup[temp], 'name') + '\n'
                        else:
                            buffer += temp + '. (s)     ' + getattr(activeGroup[temp], 'name') + '\n'
                        
                        temp += 1
                    connectionSocket.send(buffer)
<<<<<<< HEAD
                    break


=======
                        break
>>>>>>> a47466daf7de638b24d9db271b70425e89589a1f

        elif firstcommand == "sg":
            while 1:
                subcommand = connectionSocket.recv(1024)
                index = 0  # index in the activeGroup Array
                buffer = ""
                quit = False
                optionalcommand = commandsAll[1]
                if optionalcommand == None:
                        optionalcommand = 5
                # here uses the default value for N -> showing N items at a time

<<<<<<< HEAD
                while index < optionalcommand:
                    # list all the group up to N
                    if currentUser in getattr(activeGroup[index], 'subscribedUsers'):
                        buffer += index + '. POST### ' + getattr(activeGroup[index], 'name') + '\n'
                        index += 1
                    connectionSocket.send(buffer)
                    while 1:
                        buffer = "'"
                        subcommand = connectionSocket.recv(1024).split(" ")
                        if subcommand == 'u':
                            temp = 0
                            while subcommand[temp + 1] != None:
                                ##subscribe to index + argument group
                                groupToUnsubscribe = getattr(activeGroup[index + int(subcommand[temp + 1])],
                                                             'subscribedUsers')
                                # activeGroup[groupToSubscribe].getUserArray.Remove
                                groupToUnsubscribe.remove(currentUser)
                                temp += 1
                        elif subcommand == 'n':
                            temp = 0
                            while temp < optionalcommand:
                                if index > len(activeGroup):
                                    buffer += "------All Group Has Been Shown------"
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
                            break



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
                    print( 'you are not in the group')

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
                pass
        
        
        
        elif firstcommand == "logout":
            # remove user from activeUser array

=======
    elif firstcommand == "sg":
        while 1:
            subcommand = connectionSocket.recv(1024)
                index = 0  # index in the activeGroup Array
                buffer = ""
                quit = False
                optionalcommand = commandsAll[1]
                if optionalcommand == None:
                    optionalcommand = 5
            # here uses the default value for N -> showing N items at a time
            
            while index < optionalcommand:
                # list all the group up to N
                if currentUser in getattr(activeGroup[index], 'subscribedUsers'):
                    buffer += index + '. POST### ' + getattr(activeGroup[index], 'name') + '\n'
                    index += 1
                connectionSocket.send(buffer)
                while 1:
                    buffer = "'"
                    subcommand = connectionSocket.recv(1024).split(" ")
                    if subcommand == 'u':
                        temp = 0
                        while subcommand[temp + 1] != None:
                            ##subscribe to index + argument group
                            groupToUnsubscribe = getattr(activeGroup[index + int(subcommand[temp + 1])],
                                                         'subscribedUsers')
                                                         # activeGroup[groupToSubscribe].getUserArray.Remove
                                                         groupToUnsubscribe.remove(currentUser)
                                                         temp += 1
                    elif subcommand == 'n':
                        temp = 0
                        while temp < optionalcommand:
                            if index > len(activeGroup):
                                buffer += "------All Group Has Been Shown------"
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
                        break


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
                print 'you are not in the group'
            
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
>>>>>>> a47466daf7de638b24d9db271b70425e89589a1f
            authenticated = False
            connectionSocket.send("logout success")
            break


