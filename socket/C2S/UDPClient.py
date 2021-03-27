from socket import *
serverName='192.168.133.134'
serverPort=12000

clientSocket=socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')  # raw_input was integrated into input()
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, ServerAddress= clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()