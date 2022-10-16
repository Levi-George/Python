#import socket module

from socket import *
import platform
import sys #termination of prog

serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare server socket
port = 6789

#Start Here
serverSocket.bind(('', port))
serverSocket.listen(1)
#End Here

while True:
    #Establish Connection
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()

    try:
        message = serverSocket.recv(2048).decode()
        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f

        #Send one HTTP header line to socket

        httpHeader = 'HTTP/1.0 200 OK\r\n'

        connectionSocket.send(httpHeader.encode(), addr)


        #send content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send 404 response
        #Fill In
        httpHeader = 'HTTP/1.0 404 Page Not Found\r\n'

        connectionSocket.send(httpHeader.encode(), addr)
        
        #Close Socket
        serverSocket.close()

    serverSocket.close()

    sys.exit()