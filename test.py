#!/usr/bin/python3

import threading
import time

my_str=''

def qwerty():
    global my_str
    print(threading.current_thread().__getattribute__('name') + ' started')
    time.sleep(1)
    my_str += threading.current_thread().__getattribute__('name')


for i in range (10):
    my_thread = threading.Thread(None,qwerty,str(i))
    my_thread.start()





print(threading.active_count())
print(threading.current_thread())

time.sleep(5)

print(my_str)