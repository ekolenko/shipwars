#!/usr/bin/python3


import random
import socket
import time

mb_client_sock = None
player = None
my_field = set()
enemy_field = set()


def connect_to_host():

    global mb_client_sock
    global player
    mb_client_sock = socket.socket()
    mb_client_sock.connect(('localhost',9091))

    # тут сервер возращает строку каким подключился "1" или "2" сразу после подключения
    data = mb_client_sock.recv(1024)
    player = bytes.decode(data,'utf-8') 

    # тут сервер ждет пока подключится второй и возращает "ок" когда второй подключился
    
    # < тут меняем кнопку на ожидание второго игрока> 
    data = mb_client_sock.recv(1024) 

    if bytes.decode(data,'utf-8') == 'ok':

        # меняем на подключено
        return True

def send_field(str_in):
    mb_client_sock.send(bytes(str_in,'utf-8'))

    data = mb_client_sock.recv(1024) 
    if bytes.decode(data,'utf-8') == 'ok':

        # меняем на отправлено
        return True



def send_fire(str_in: str) -> str:
    mb_client_sock.send(bytes(str_in,'utf-8'))

    data = mb_client_sock.recv(1024) 
    return bytes.decode(data,'utf-8') 



def recv_fire() -> str:
    data = mb_client_sock.recv(1024) 
    return bytes.decode(data,'utf-8')


def check_my_field(fire):
    if fire in my_field:
        my_field.remove(fire) 
        print('Hit')
    if len(my_field) == 0:
        return True
    return False



def start_game():
    global enemy_field
    if player == '1':
        while True:
            fire = str(random.randint(0,99))
            while fire in enemy_field:
                fire = str(random.randint(0,99))
            enemy_field.add(fire)
            if send_fire(fire) == 'w':
                print('i win')
                return
            print('Fire to',fire)
            # time.sleep()
            fire = recv_fire()
            if check_my_field(fire):
                print('i lose')
                return
    else:
        while True:
            fire = recv_fire()
            if check_my_field(fire):
                print('i lose')
                return
            # time.sleep(1)
            fire = str(random.randint(0,99))
            while fire in enemy_field:
                fire = str(random.randint(0,99))
            enemy_field.add(fire)
            time.sleep(2)
            send_fire(fire)
            print('Fire to',fire)
            
            
def random_field():
    global my_field
    while len(my_field) < 10:
        my_field.add(str(random.randint(0,99)))
    return my_field


connect_to_host()
print(player)
send_field(' '.join(random_field()))
start_game()