# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:54:06 2019

@author: shu
"""

import socket

def main():
    count=1
    while(1):
        host="127.0.0.1"
        port=5000
    
        socketser=socket.socket()
        socketser.bind((host,port))
        print("Turn on server "+ str(count))
        
        socketser.listen(9)
        
        c_socket,addr=socketser.accept()#int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
        print("client from"+str(addr)+"\nok")
        #收
        data=c_socket.recv(1024)
        
        #回
        print("From client user"+str(data)+"\n")
        c_socket.send('I have got your msf'.encode())
        c_socket.close
        count+=1
    
main()