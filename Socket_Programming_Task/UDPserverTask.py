from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort=12000
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while True:
      message, clientAddress = serverSocket.recvfrom(2048)
      modifiedMessage = message.decode().upper()
      print("This message: "+modifiedMessage)
      print("is recieved from: "+str(clientAddress))
      serverSocket.sendto(modifiedMessage.encode(),clientAddress)