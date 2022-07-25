#!/usr/bin/python3


import net_func
import time
import random


sb_sock = net_func.connect_to_host('glt.ekolenko.ru',9091)

if net_func.check_connection(sb_sock):
    print('OK')
else:
    print('ERROR')

    [[4], [17, 27], [19, 29], [21, 22, 23, 24], [51], [53, 63, 73], [55, 65, 75], [58, 59], [78], [81]]

if net_func.send_field(sb_sock,'4:17 27:19 29:21 22 23 24:51:53 63 73:55 65 75:58 59:78:81'):
    print('Field send')
else:
    print('Field error')


while True:
    str_in = input()
    # net_func.start_game(sb_sock)
    # print(net_func.find_player(sb_sock))
    # time.sleep(15)
    # net_func.disconnect_sock(sb_sock)
    sb_sock.send(bytes(str_in, 'utf-8'))
    data_in = sb_sock.recv(1024)
    print(data_in)
    data_lst = bytes(data_in,'utf-8')
    if data_lst[0] == '03' and data_lst[1] != 'er' and data_lst[2] == '0':
        while net_func.receive_fire()[1] != '0':
            pass
