from socket import *
serverIP = '127.0.0.1'
serverPort = 12000
sentence=""
while(sentence!="Exit"):
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((serverIP,serverPort))
   sentence = input('Enter message to send or type Exit to disconnect: ')
   clientSocket.send(sentence.encode())
   modifiedSentence = clientSocket.recv(1024)
   print ('From Server:', modifiedSentence.decode())
   if(sentence!="Exit"):
       print("Recieved message from server : Your data was "+str(len(modifiedSentence))+ " bytes ")
   else:
       print("Recieved message from server : Disconncet")
   clientSocket.close()
print("Now you are disconnected from the server")
