#import socket module
from socket import *
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
# Prepare a sever socket
# Fill in start
# Fill in end
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr =serverSocket.accept() #Fill in start  #Fill in end
    try:
        message = connectionSocket.recv(1024)  #Fill in start  #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        # Fill in start
        outputdata = f.read()
        header='HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        header= ' HTTP/1.1 404 Found'
        connectionSocket.send(header.encode())

        connectionSocket.close()
        # Send response message for file not found
        # Close client socket

serverSocket.close()