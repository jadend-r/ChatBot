# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:18:16 2022

@author: Jaden Reid
"""
import socket

server = True
serv_addr = "127.0.0.1"
serv_port = 7888

def respond(connection, clientmsg):
    response = None
    if clientmsg.find("hello") != -1:
        response = "Hello!"
    elif clientmsg.find("wentworth") != -1:
        response = "Go leopards!"
    elif clientmsg.find("homework") != -1:
        response = "Homework sucks!"
    else:
        response = "Beep boop!" 
    print(">" + response) 
    connection.sendall(response.encode())
   
if server:
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.bind(('', serv_port))
    serversock.listen(5)
    while True:
        clientconn, addr = serversock.accept()
        while True:
            msg = clientconn.recv(50).decode().lower()
            print("Client: " + msg)
            if msg.find("goodbye") != -1:
                clientconn.sendall(b'Goodbye!')
                clientconn.close()
                break
            else:
                respond(clientconn, msg)
        break
else:
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsock.connect((serv_addr, serv_port))
   
    while True:
        sendToServ = input(">")
        chatEnding = False
        if sendToServ.lower().find("goodbye") != -1:
            chatEnding = True
        sendToServ = sendToServ.encode()
        clientsock.sendall(sendToServ)
        servResponse = clientsock.recv(50).decode()
        print("Server: " + servResponse)
        if chatEnding:
            exit()