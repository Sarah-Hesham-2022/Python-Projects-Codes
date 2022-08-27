from socket import *

#This library is for python to take arguments
import sys
serverIP = '127.0.0.1'
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.bind( ('', int(sys.argv[1])) ) #modification to extract port
message = sys.argv[2]                       #modification to extract message
serverPort = 12000
clientSocket.sendto(message.encode(),(serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()


