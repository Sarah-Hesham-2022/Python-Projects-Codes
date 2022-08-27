from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Listening at: "+str(serverSocket.getsockname()))
flag=1
while True:
     connectionSocket, addr = serverSocket.accept()
     if(flag):
         print("The server is now connceted to : "+str(addr))
         print("Socket conncets between : "+str(connectionSocket.getsockname())+" and "+str(addr))
         flag=0
     sentence = connectionSocket.recv(1024).decode()
     capitalizedSentence = sentence.upper()
     print("Recieved Message from Client : "+sentence)
     connectionSocket.send(capitalizedSentence.encode())
     connectionSocket.close()
     if(sentence=="Exit"):
          print("Reply Sent, Server Socket Closed.")
          print("Listening at: "+str(serverSocket.getsockname()))