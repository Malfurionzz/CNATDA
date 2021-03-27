from socket import *
serverName='192.168.133.134'
serverPort=12000

clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')  # raw_input was integrated into input()
clientSocket.send(sentence)
modifiedMessage = clientSocket.recv(2048)
print 'From Server:', modifiedMessage
clientSocket.close()
