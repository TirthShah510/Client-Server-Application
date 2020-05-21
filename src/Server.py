import socket

serverSocket = socket.socket()
print("Server Socket created")

serverSocket.bind(('localhost', 5555))

serverSocket.listen()
print("Waiting for Client Connection")

readFile = open('data.txt', 'r')
Lines = readFile.readlines()
dictRecord = {}
for line in Lines:
    listLine = line.split('|')
    if listLine[0]:
        dictRecord[listLine[0]] = line[(len(listLine[0]) + 1):].strip()


def customerExists():
    if listData[1] in dictRecord:
        return True
    return False


def findCustomer(argument):

    if listData[1] in dictRecord:
        record = listData[1] + "|" + dictRecord[listData[1]]
        clientSocket.send(bytes(record, 'utf-8'))
    else:
        clientSocket.send(bytes("Customer not found", 'utf-8'))


def addCustomer(argument):

    if customerExists():
        clientSocket.send(bytes("Customer already exists", 'utf-8'))
    else:
        record = ""
        i = 2
        while i < len(listData) - 1:
            record = record + listData[i] + "|"
            i += 1
        record += listData[len(listData) - 1]
        dictRecord[listData[1]] = record
        clientSocket.send(bytes("Customer has been added", 'utf-8'))


def deleteCustomer(argument):

    if customerExists():
        del dictRecord[listData[1]]
        clientSocket.send(bytes("Customer has been deleted", 'utf-8'))
    else:
        clientSocket.send(bytes("Customer Not Found", 'utf-8'))


def update(argument):

    tempDict = {}
    if customerExists():
        data = dictRecord[listData[1]]
        tempList = data.split('|')
        if argument == 4:
            tempList[0] = listData[2]
        elif argument == 5:
            tempList[1] = listData[2]
        elif argument == 6:
            tempList[2] = listData[2]
        record = ""
        i = 0
        while i < len(tempList) - 1:
            record = record + tempList[i] + "|"
            i += 1
        record += tempList[len(tempList) - 1]
        tempDict[listData[1]] = record
        dictRecord.update(tempDict)
        clientSocket.send(bytes("Customer has been updated", 'utf-8'))
    else:
        clientSocket.send(bytes("Customer not found", 'utf-8'))


def printReport(argument):

    record = ""
    for key in sorted(dictRecord.keys()):
        record += key + "|" + dictRecord[key] + ","

    clientSocket.sendall(bytes(record, 'utf-8'))


def serverSwitchMenu(argument):
    switcher = {
        1: findCustomer,
        2: addCustomer,
        3: deleteCustomer,
        4: update,
        5: update,
        6: update,
        7: printReport
    }
    function = switcher.get(argument, lambda: 'invalid')
    function(argument)


while True:
    try:
        clientSocket, clientAddress = serverSocket.accept()
        print("Connected with ", clientAddress)
        clientSocket.send(bytes("Hello Client", 'utf-8'))
        data = clientSocket.recv(4096).decode()
        while data:
            listData = data.split('|')
            serverSwitchMenu(int(listData[0]))
            data = clientSocket.recv(4096).decode()
    except socket.error:
        print("An existing connection was forcibly closed by the client.")

