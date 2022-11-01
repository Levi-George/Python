from socket import *
import time
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
sendSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
sendSocket.connect(('127.0.0.1', 12000))

while(True):

    sendSocket.send("Hello".encode('utf-8'))

    time.sleep(2)

