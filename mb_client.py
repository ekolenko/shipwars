#!/usr/bin/python3


import socket

mb_client_sock = None
player = None


def connect_to_host():

    global mb_client_sock
    global player
    mb_client_sock = socket.socket()
    mb_client_sock.connect(('glt.ekolenko.ru',9091))

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

connect_to_host()
print(player)
send_field('1 2 3 4 5')
