from socket import *
serverPort = 12010
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('192.168.0.105',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    print "Client connected",addr
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    print "Closing connection"
    connectionSocket.close()
    print "Connection closed"
