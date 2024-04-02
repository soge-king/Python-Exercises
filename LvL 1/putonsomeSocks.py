# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:48:50 2024

@author: User
"""

import socket 

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80)) #web server and port number
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #set up request
mysocket.send(cmd) #set request to command line


while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysocket.close()
    
