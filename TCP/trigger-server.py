#!/usr/bin/env python3

'''
Example usage of the TCPServer class from the TCPCOM library
'''

from tcpcom import TCPServer
import socket

# connection configuration settings

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

tcp_ip = get_ip_address()  # '192.168.0.110'

# tcp_ip = '127.0.0.1'
tcp_port = 34000
tcp_reply = "TRIGGGERED"

def handleMessage(msg):
    global response
    msg = int(msg)
    if msg == 0: 
        response = "OFF"
    elif msg == 1: 
        response = "FIRE"
    else: 
        response = "Something wrong"
    
    
def onStateChanged(state, msg):
    global isConnected

    if state == "LISTENING":
        print("Server:-- Listening...")

    elif state == "CONNECTED":
        isConnected = True
        print("Server:-- Connected to" + msg)
        # got_state = handleMessage(msg)
        # print(f"we have recievd this {got_state}")
    
    elif state == "MESSAGE":
        print("Server:-- Message received:", msg)
        handleMessage(msg)
        #print(f"we have recievd this {got_state}")
        server.sendMessage(tcp_reply)


def main():
    global server
    print(f"got this ip add for this server; {get_ip_address()} port is: {tcp_port}")
    server = TCPServer(tcp_port, stateChanged=onStateChanged)

    

if __name__ == '__main__':
    main()
