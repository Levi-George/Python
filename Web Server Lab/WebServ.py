#import socket module

from socket import *
import sys #termination of prog

serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare server socket

#Start Here

#End Here

while True:
    #Establish Connection
    print('Ready to serve...')

    connectionSocket, addr = ""#"Fill In"

    try:
        message = "Fill In"
        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = "Fill In"

        #Send one HTTP header to socket

        #send content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send 404 response
        #Fill In

        #Close Socket
        #Fill in
        print("Does this appease the error")#Temp line, while figuring code out.

    serverSocket.close()

    sys.exit()