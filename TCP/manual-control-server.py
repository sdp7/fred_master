#!/usr/bin/env python3

'''
Example usage of the TCPServer class from the TCPCOM library
'''

from tcpcom import TCPServer

# connection configuration settings
tcp_ip = "192.168.1.103"
tcp_port = 5008
tcp_reply = "Manual control message"

wheelbase_x = 0
wheelbase_y = 0
turret_x = 0
turret_y = 0

def handleMessage(msg):
    global wheelbase_x
    global wheelbase_y
    global turret_x
    global turret_y
    message = msg.split(";")
    if(message[0] == "Wheelbase"):
        wheelbase_x = float(message[1])
        wheelbase_y = float(message[2])
    elif(message[0] == "Turret"):
        turret_x = float(message[1])
        turret_y = float(message[2])

def onStateChanged(state, msg):
    global isConnected

    if state == "LISTENING":
        print("Server:-- Listening...")
    elif state == "CONNECTED":
        isConnected = True
        print("Server:-- Connected to" + msg)
    elif state == "MESSAGE":
        print("Server:-- Message received:", msg)
        handleMessage(msg)
        server.sendMessage(tcp_reply)


def main():
    global server
    server = TCPServer(tcp_port, stateChanged=onStateChanged)


if __name__ == '__main__':
    main()
