from socket import *


serverName = 'localhost'
serverPort = 7037
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence")
clientSocket.sendto(bytes(message, 'utf-8'), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()
