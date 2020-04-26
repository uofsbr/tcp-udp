from socket import *

serverName = "servername" # server name or server  ip
serverPort = 12000

# socket(IPv4, TCP)
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = input("Input lowercase sentence:\n")
clientSocket.send(bytes(sentence, "utf-8"))

modifiedSentence = clientSocket.recv(1024)
print ("From Server:", modifiedSentence.decode("utf-8"))

clientSocket.close()
