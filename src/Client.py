import socket

clientSocket = socket.socket()

clientSocket.connect(('localhost', 9999))

print(clientSocket.recv(1024).decode())


def printMenu():
    print("\nPython DB Menu\n")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit\n")
    print("Select:")

    return int(input())


def findCustomer():
    print("\nFIND CUSTOMER\n")
    name = input("Enter Name of Customer: ")
    return name


def addCustomer():
    print("\nADD CUSTOMER\n")
    name = input("Enter Name of Customer: ")
    age = input("Enter Age of Customer: ")
    address = input("Enter Address of Customer: ")
    phone = input("Enter Phone Number of Customer: ")
    return name + "|" + age + "|" + address + "|" + phone


def deleteCustomer():
    print("\nDELETE CUSTOMER\n")
    name = input("Enter Name of Customer")
    return name


def updateAge():
    print("\nUPDATE AGE\n")
    name = input("Enter Name of Customer")
    age = input("Enter Age of Customer")
    return name + "|" + age


def updateAddress():
    print("\nUPDATE ADDRESS\n")
    name = input("Enter Name of Customer")
    address = input("Enter Address of customer")
    return name + "|" + address


def updatePhone():
    print("\nUPDATE PHONE\n")
    name = input("Enter Name of Customer")
    phone = input("Enter Phone Number of Customer")
    return name + "|" + phone


def printReport():
    return "print"


def switchMenu(argument):
    switcher = {
        1: findCustomer,
        2: addCustomer,
        3: deleteCustomer,
        4: updateAge,
        5: updateAddress,
        6: updatePhone,
        7: printReport
    }
    function = switcher.get(argument, lambda : 'invalid')
    return function()


option = printMenu()

while 0 < option < 8:
    data = switchMenu(option)
    clientSocket.send(bytes(str(option) + "|" + data, 'utf-8'))
    print(clientSocket.recv(4096).decode())
    option = printMenu()
