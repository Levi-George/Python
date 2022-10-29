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
        message = connectionSocket.recv(1024).decode() #you had the server socket set to receive
        filename = message.split()[1]
        f = open(filename[1:], 'r')

        outputdata = f.read() #you need to set the file to read

        #Send one HTTP header line to socket

        httpHeader = 'HTTP/1.0 200 OK\r\n'

        connectionSocket.send(httpHeader.encode('iso-8859-1'))

        httpHeader = 'Content-Type: text/html\n\r\n'

        connectionSocket.send(httpHeader.encode('iso-8859-1'))


        #send content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            print(outputdata[i])
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
    #   Send 404 response
    #   Fill In
        
        outputdata = open("Hello404.html", 'r').read()

        httpHeader = "HTTP/1.1 404 Page Not Found\r\n"
        connectionSocket.send(httpHeader.encode('iso-8859-1'))

        httpHeader = 'Content-Type: text/html\n\r\n'
        connectionSocket.send(httpHeader.encode('iso-8859-1'))

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        print(httpHeader)

        #Close Socket
        serverSocket.close()

    serverSocket.close()

    sys.exit()