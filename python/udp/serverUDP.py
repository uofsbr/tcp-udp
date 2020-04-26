from socket import *

serverPort = 12000

# socket(IPv4, UDP)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print ("The server is ready to receive...")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode("utf-8").upper()
    serverSocket.sendto(bytes(modifiedMessage, "utf-8"), clientAddress)
