from socket import *
import sys
serverName = '127.0.0.1' #servername
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input two numbers:')
clientSocket.send(sentence.encode())
if(sentence=='exit'):
    sys.exit()
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()