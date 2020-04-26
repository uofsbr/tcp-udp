from socket import *

# serverName = "hostname" # server name or server  ip
serverName = "127.0.0.1" # server name or server  ip
serverPort = 12000

# socket(IPv4, UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input lowercase sentence:\n")
clientSocket.sendto(bytes(message, "utf-8"),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode("utf-8")) 

clientSocket.close()
