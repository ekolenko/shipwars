#!/usr/bin/python3


import socket
import threading
import time


# class myThread

mp_serv_sock  = None

player_id = 0
play_order = 0

list_connected = []
players_fields = {}
players = {}
game = []

def init_socket():
    global mb_server_sock

    mb_server_sock = socket.socket()
    mb_server_sock.bind(('0.0.0.0',9091))
    mb_server_sock.listen(0)


def accept_connection():
    while True:
        conn_sock,addr = mb_server_sock.accept()
        print(f'Connected {addr}')
        list_connected.append(conn_sock)
        start_data_transfer(conn_sock,addr)


def data_transfer(sock):
    while sock.fileno() != -1:
        data = sock.recv(1024)
        print(data)

        if not data:
            sock.close()

        else:
            decode_data(sock, data)


def start_data_transfer(socket, addr):
    print(f'Starting data transfer {addr}')
    thread = threading.Thread(target=data_transfer,name='accept_connection',args=(socket,))
    thread.start()
    

def thread_accept_connect():
    thread = threading.Thread(target=accept_connection,name='accept_connection')
    thread.start()


def get_field(sock, str):
    
    sock_name = sock.getpeername()    
    if sock_name not in players_fields.keys():

        gen_field(sock_name, str)
        sock.send(b'02,ok')
    else:
        sock.send(b'02,er')

def get_fire(sock, str_in):
    global players_fields
    global game_orde

    sock_name = sock.getpeername()

    if play_order == game.index(sock_name):

        check_fire()

    else:
        sock.send(b'03,er')
    #  pass

    # sock.send(b'03,' + check_fire(sock_name, str_in))


def check_fire(sock_name, str_in):

    global play_order

    pass

    play_order = abs(play_order - 1)

def gen_field(sock_name, str_in):

    global players_fields

    res_list =  [step.split(':') for step in str_in.split(' ')]

    players_fields[sock_name] = res_list


def gen_game():
    global game
    
    game = list(players.keys())


def add_to_players(sock):
    global players
    global player_id
    sock_name = sock.getpeername()
    player_id += 1
    players[sock_name] = player_id


def decode_data(sock, data):
    command_data = bytes.decode(data,'utf-8').split(',')
    sock_name = sock.getpeername()
    match command_data[0]:
        case '01':
            sock.send(b'01,ok')
        case '02':
            get_field(sock, command_data[1]) 
        case '03':
            get_fire(sock, command_data[1])
        case '04':
            add_to_players(sock)
            sock.send(b'04,ok')
        case '05':
            sock.send(b'05,ok')
            if sock_name in players.keys():
                del players[sock_name]
            sock.close()
        case '06':
            if len(players) == 2:
                gen_game()
                sock.send(bytes('06,ok,' + str(game.index(sock_name)) ,'utf-8'))
            else:
                sock.send(b'06,er')                


def check_fire(i):
    enemy_i = abs(i - 1)
    data = list_connected[i].recv(1024)
    fire_point = bytes.decode(data,'utf-8')
    list_connected[enemy_i].send(data)
    if fire_point in players_fields[enemy_i]:        
        players_fields[enemy_i].remove(fire_point)
        if len(players_fields[enemy_i]) == 0:
            list_connected[i].send(b'w')
        else:
            list_connected[i].send(b'+')
    else:
        list_connected[i].send(b'-')

    print(i,fire_point)

    return False

init_socket()
thread_accept_connect()
print('Accepting connections')

while True:
    time.sleep(5)
    # print(list_connected)
    # print()
    print(players_fields)
    print()
    print(players)
    print()
    print(game)
