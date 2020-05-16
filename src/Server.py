import socket

serverSocket = socket.socket()
print("Server Socket created")

serverSocket.bind(('localhost', 9999))

serverSocket.listen()
print("Waiting for Client Connection")

while True:
    clientSocket, clientAddress = serverSocket.accept()
    print("Connected with ", clientAddress)
    clientSocket.send(bytes("Hello Client", 'utf-8'))
    data = clientSocket.recv(4096).decode()
    while not data:
        print(data)
