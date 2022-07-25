#!/usr/bin/python3


import net_func
import time
import random


sb_sock = net_func.connect_to_host('localhost',9090)

if net_func.check_connection(sb_sock):
    print('OK')
else:
    print('ERROR')

if net_func.send_field(sb_sock,'12:12 13 1 4:43 45:23 45 56 67:23 21:56 78 94'):
    print('Field send')
else:
    print('Field error')

if net_func.send_field(sb_sock,'12:12 13 1 4:43 45:23 45 56 67:23 21:56 78 94'):
    print('Field send')
else:
    print('Field error')

time.sleep(random.randint(1,5))
net_func.disconnect_sock(sb_sock)