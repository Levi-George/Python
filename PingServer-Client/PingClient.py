from socket import *
import datetime
import time
from timeit import default_timer
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
sendSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
sendSocket.connect(('127.0.0.1', 12000))

while(True):

    #used to hold message from server
    msg = ""
    #time to track RTT
    start = default_timer()

    #send message
    sendSocket.send("Hello".encode('utf-8'))
    
    #receive message from socket
    msg = sendSocket.recv(1024).decode("utf-8")

    #only print an actual message
    if(msg):
        roundTripTime = default_timer() - start
        print(msg, str(roundTripTime), sep="::")   

    #Limit amount of packets being sent
    time.sleep(2)

