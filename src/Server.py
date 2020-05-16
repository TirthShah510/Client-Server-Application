import socket

serverSocket = socket.socket()
print("Server Socket created")

serverSocket.bind(('localhost', 9999))

serverSocket.listen()
print("Waiting for Client Connection")

readFile = open('data.txt', 'r')
Lines = readFile.readlines()
print("Database Loading Completed")


def customerExists():
    for line in Lines:
        listLine = line.split('|')
        if listLine[0].strip() == listData[1].strip():
            return True
    return False


def findCustomer():
    for line in Lines:
        if line.startswith(listData[1]):
            clientSocket.send(bytes(line, 'utf-8'))
            break
    clientSocket.send(bytes("Customer not found", 'utf-8'))


def addCustomer():
    appendFile = open('data.txt', 'a+')

    if customerExists():
        clientSocket.send(bytes("Customer already exists", 'utf-8'))
    else:
        record = ""
        i = 1
        while i < len(listData) - 1:
            record = record + listData[i] + "|"
            i += 1
        record += listData[len(listData) - 1]
        record = "\n" + record
        appendFile.write(record)
        clientSocket.send(bytes("Customer has been added", 'utf-8'))


def deleteCustomer():
    lineToBeDeleted = ""

    if customerExists():
        f = open("data.txt", "w")
        for line in Lines:
            if line.strip("\n") != lineToBeDeleted:
                f.write(line)
        clientSocket.send(bytes("Customer has been deleted", 'utf-8'))
    else:
        clientSocket.send(bytes("Customer already exists", 'utf-8'))


def updateAge():
    if customerExists():
        f = open('data.txt', 'w')
        for line in Lines:
            listLine = line.split('|')
            if listLine[0].strip() == listData[1].strip() and listData[2] != "":
                listLine[1] = listData[2]
                record = ""
                i = 0
                while i < len(listLine) - 1:
                    record = record + listLine[i] + "|"
                    i += 1
                record += listLine[len(listLine) - 1]
                f.write(record)
            else:
                f.write(line)
        clientSocket.send(bytes("Customer has been updated", 'utf-8'))
    else:
        clientSocket.send(bytes("Customer not found", 'utf-8'))


def updateAddress():
    if customerExists():

        f = open('data.txt', 'w')
        for line in Lines:
            listLine = line.split('|')
            if listLine[0].strip() == listData[1].strip() and listData[2] != "":
                listLine[2] = listData[2]
                record = ""
                i = 0
                while i < len(listLine) - 1:
                    record = record + listLine[i] + "|"
                    i += 1
                record += listLine[len(listLine) - 1]
                f.write(record)
            else:
                f.write(line)
        clientSocket.send(bytes("Customer has been updated", 'utf-8'))
    else:
        clientSocket.send(bytes("Customer not found", 'utf-8'))


def updatePhone():
    if customerExists():

        f = open('data.txt', 'w')
        for line in Lines:
            listLine = line.split('|')
            if listLine[0].strip() == listData[1].strip() and listData[2] != "":
                listLine[3] = listData[2]
                record = ""
                i = 0
                while i < len(listLine) - 1:
                    record = record + listLine[i] + "|"
                    i += 1
                record += listLine[len(listLine) - 1]
                f.write(record)
            else:
                f.write(line)

        clientSocket.send(bytes("Customer has been updated", 'utf-8'))
    else:
        clientSocket.send(bytes("Customer not found", 'utf-8'))


def printReport():
    return "print"


def serverSwitchMenu(argument):
    switcher = {
        1: findCustomer,
        2: addCustomer,
        3: deleteCustomer,
        4: updateAge,
        5: updateAddress,
        6: updatePhone,
        7: printReport
    }
    function = switcher.get(argument, lambda: 'invalid')
    function()


while True:
    clientSocket, clientAddress = serverSocket.accept()
    print("Connected with ", clientAddress)
    clientSocket.send(bytes("Hello Client", 'utf-8'))
    data = clientSocket.recv(4096).decode()
    while data:
        listData = data.split('|')
        serverSwitchMenu(int(listData[0]))
        data = clientSocket.recv(4096).decode()
