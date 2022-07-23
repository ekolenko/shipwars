#!/usr/bin/python3


import socket


# class myThread

mp_serv_sock = socket.socket()
mp_serv_sock.bind(('0.0.0.0',9091))
mp_serv_sock.listen(0)

list_connected = []
players_fields = {}

def wait_for_connect():

    conn_sock,addr = mp_serv_sock.accept()
    print(f'Connected {addr}')
    return conn_sock

def receive_data(conn_sock):
    data_lst =[]
    while True:
        data = conn_sock.recv(1024)
        print(data)
        if not data:
            print('Disconnected')
            break
        else:
            data_lst.append(data)

    return data_lst


def recv_player_fields() -> bool:

    for i in range(2):
        data = list_connected[i].recv(1024)
        players_fields[i] = bytes.decode(data,'utf-8').split()
        list_connected[i].send(b'ok')

def check_fire(i):
    
    data = list_connected[i].recv(1024)
    fire_point = bytes.decode(data,'utf-8')
    if fire_point in players_fields[abs(i - 1)]:
        list_connected[i].send(b'+')
    else:
        list_connected[i].send(b'-')

    print(i,fire_point,list_connected[i].ladr)



    return True

def connect_players():

    list_connected.append(wait_for_connect())
    print(list_connected)
    list_connected[0].send(b'1')
    list_connected.append(wait_for_connect())
    print(list_connected)
    list_connected[1].send(b'2')
    list_connected[0].send(b'ok')
    list_connected[1].send(b'ok')

    print('Players connected')


connect_players()

recv_player_fields()

print(players_fields)

while True:
    for i in range(2):
        check_fire(i)
