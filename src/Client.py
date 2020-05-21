import socket

clientSocket = socket.socket()

try:
    clientSocket.connect(('localhost', 5555))

    print(clientSocket.recv(1024).decode())
except socket.error:
    print("Server is not active. No request will be forwarded to server.")


def printMenu():
    print("----------------------------------------------------------------------------------------------------")
    print("\nPython DB Menu\n")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit\n")

    while True:
        print("Select:")
        choosenOption = input().strip()
        if choosenOption.isdigit() and 0 < int(choosenOption) < 9:
            return int(choosenOption)
        else:
            print("ERROR: PLEASE ENTER VALID OPTION BETWEEN 1 TO 8.")


def inputName():
    while True:
        name = input("Enter Name of Customer: ")
        if name == "":
            print("ERROR: NAME FIELD IS MANDATORY. PLEASE GO TO MAIN MENU.")
            return "invalid"
        else:
            return name


def findCustomer():
    print("\nFIND CUSTOMER\n")

    while True:
        name = input("Enter Name of Customer: ")
        if name != "":
            return name.strip()
        else:
            print("ERROR: NAME IS MANDATORY FIELD. PLEASE GO TO MAIN MENU.")
            return "invalid"


def addCustomer():
    print("\nADD CUSTOMER\n")

    name = inputName()
    if name == "invalid":
        return name
    while True:
        age = input("Enter Age of Customer: ")
        if age == "":
            break
        else:
            if age.isdigit():
                break
            else:
                print("ERROR: PLEASE ENTER VALID AGE.\n")
    address = input("Enter Address of Customer: ")
    phone = input("Enter Phone Number of Customer: ")
    return name.strip() + "|" + str(age) + "|" + address.strip() + "|" + phone.strip()


def deleteCustomer():
    print("\nDELETE CUSTOMER\n")

    while True:
        name = input("Enter Name of Customer: ")
        if name != "":
            return name.strip()
        else:
            print("ERROR: NAME FIELD IS MANDATORY. PLEASE GO TO MAIN MENU.")
            return "invalid"


def updateAge():
    print("\nUPDATE AGE\n")

    name = inputName()
    if name == "invalid":
        return name
    while True:
        age = input("Enter Age of Customer: ")
        if age == "":
            break
        else:
            if age.isdigit():
                break
            else:
                print("ERROR: PLEASE ENTER VALID AGE.\n")
    return name.strip() + "|" + str(age)


def updateAddress():
    print("\nUPDATE ADDRESS\n")
    name = inputName()
    if name == "invalid":
        return name
    address = input("Enter Address of customer: ")
    return name.strip() + "|" + address.strip()


def updatePhone():
    print("\nUPDATE PHONE\n")
    name = inputName()
    if name == "invalid":
        return name
    phone = input("Enter Phone Number of Customer: ")
    return name.strip() + "|" + phone.strip()


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
    function = switcher.get(argument, lambda: 'invalid')
    return function()


option = printMenu()

while 0 < option < 8:
    try:
        data = switchMenu(option)
        if data != "invalid":
            clientSocket.send(bytes(str(option) + "|" + data, 'utf-8'))
            if option == 7:
                print("-----------------------------------------------------------------------------------------------")
                print("                                         REPORT                                                ")
                print("-----------------------------------------------------------------------------------------------")
                data = clientSocket.recv(4096).decode()
                listOfRecords = data.split(',')
                for record in listOfRecords:
                    if record:
                        individualRecord = record.split('|')
                        print("NAME: ", individualRecord[0].strip(), "|", "AGE: ", individualRecord[1].strip(), "|",
                              "ADDRESS: ", individualRecord[2].strip(), "|", "PHONE: ", individualRecord[3].strip())
            elif option == 1:
                data = clientSocket.recv(4096).decode()
                if data == "Customer not found":
                    print(data)
                else:
                    listRecord = data.split('|')
                    print("NAME: ", listRecord[0].strip(), "|", "AGE: ", listRecord[1].strip(), "|",
                          "ADDRESS: ", listRecord[2].strip(), "|", "PHONE: ", listRecord[3].strip())
            else:
                print(clientSocket.recv(4096).decode())
        option = printMenu()
    except socket.error:
        print("An existing connection was forcibly closed by the server.")
        break

print("THANK YOU..... GOOD BYE.....")
