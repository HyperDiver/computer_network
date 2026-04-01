from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    s = sentence
    if(s=='exit'):
        break
    a, b = map(int, s.split(','))
    c=str(a*b)
    connectionSocket.send(c.
    encode())
    connectionSocket.close()