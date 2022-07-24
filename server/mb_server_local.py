#!/usr/bin/python3

import socket
import threading
import time

mb_server_sock = None
list_connected = {}

players = []

def init_socket():
    global mb_server_sock

    mb_server_sock = socket.socket()
    mb_server_sock.bind(('0.0.0.0',9091))
    mb_server_sock.listen(0)



def accept_connection():
    while True:
        conn_sock,addr = mb_server_sock.accept()
        print(f'Connected {addr}')
        list_connected[addr] = conn_sock
        conn_sock.send(b'01')
        start_data_transfer(conn_sock,addr)


def data_transfer(sock):
    while True:
        data = sock.recv(1024)
        print(data)

        if data == b'ready'



        if not data:
            sock.close()


def start_data_transfer(socket, addr):
    print(f'Starting data transfer {addr}')
    thread = threading.Thread(target=data_transfer,name='accept_connection',args=(socket,))
    thread.start()
    

def thread_accept_connect():
    thread = threading.Thread(target=accept_connection,name='accept_connection')
    thread.start()




init_socket()
thread_accept_connect()
print('Accepting connections')

while True:
    time.sleep(5)
    print(list_connected)

