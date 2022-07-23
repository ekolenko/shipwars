#!/usr/bin/python3


import socket
import time
import random

player = None

mb_client_sock = socket.socket()
mb_client_sock.connect(('glt.ekolenko.ru',9091))


def connect_to_host():
    data = mb_client_sock.recv(1024)
    bytes.decode(data,'utf-8') 
    data = mb_client_sock.recv(1024)
    print(str(data))


def send_field(str_in):
    mb_client_sock.send(bytes(str_in,'utf-8'))

    data = mb_client_sock.recv(1024) 
    if bytes.decode(data,'utf-8') == 'ok':

        # меняем на отправлено
        return True

connect_to_host()
print(player)
send_field('11 12 13 14 15')
