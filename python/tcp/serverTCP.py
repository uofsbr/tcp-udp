from socket import *

serverPort = 12000

# socket(IPv4, TCP)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))

serverSocket.listen(1)

print ("The server is ready to receive\n")
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.decode("utf-8").upper()
    connectionSocket.send(byte(capitalizedSentence, "utf-8"))
    connectionSocket.close()
