# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket

class Connect():   
    def SocketClient(self):
        print("start connect")
        host="127.0.0.1"
        port=5000
        
        SocketCli=socket.socket()
        SocketCli.connect((host,port))
        #送
        SocketCli.send('test'.encode())
        
        #收
        data=SocketCli.recv(1024)
        print("get str "+str(data)+"\n")

test=Connect()
test.SocketClient()