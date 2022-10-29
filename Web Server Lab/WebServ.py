#Name: LG
#Date: 10-29-22
#Purpose: Basic web server

from socket import *
import sys #termination of prog

#responses the server may send
ServerResp = {  "200": """HTTP/1.0 200 OK
                    Content-Type: text/html\n\r\n""",
                "404": """HTTP/1.0 404 FILE NOT FOUND
                    Content-Type: text/html\n\r\n"""                    
            }

#names of files to be used
ResponseFiles = {
                "200": """DO NOT USE, If our response was successful we don't need to send this""",
                "404": """Hello404.html"""
}

#takes file and outputs each chunk through socket
def sendConnectionData(outputdata):

    for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            #print(outputdata[i]) #debug code
    connectionSocket.send("\r\n".encode())

#get and print server response
def sendHTTP_Resp(Code):

    httpHeader = ServerResp[Code]
    connectionSocket.send(httpHeader.encode('iso-8859-1'))

#MAIN
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare server socket
port = 6789

#Bind and listen to the port
serverSocket.bind(('', port))
serverSocket.listen(1)


while True:
    #Establish Connection
    print('Ready to serve...')

    #accept socket connection
    connectionSocket, addr = serverSocket.accept()

    try:
        #get data from connection
        message = connectionSocket.recv(1024).decode() #you had the server socket set to receive
        
        #open file using message sent
        filename = message.split()[1]
        f = open(filename[1:], 'r')

        #output file to be read
        outputdata = f.read()

        #header text and delivery
        sendHTTP_Resp("200")

        #send content of the requested file to the client
        sendConnectionData(outputdata)

        #close socket after message has been sent in entirety
        connectionSocket.close()
        
    except IOError:
    #   Send 404 response
        
        #get error response file and send it
        outputdata = open(ResponseFiles['404'], 'r').read()

        #header text and delivery of 404 message
        sendHTTP_Resp("404")  

        #send content of file to the client
        sendConnectionData(outputdata)

        #Close Socket
        connectionSocket.close()

    serverSocket.close()

    sys.exit()