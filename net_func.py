
import socket
import threading


def send_field(sock: socket, ships_data: list) -> bool:

    data_to_send = bytearray()
    data_to_send.append(2)

    for elem in ships_data:
        data_to_send += bytes(elem)

    data = sock.recv(1024) 
    print(data)
    if data == bytes((2,0)):
        return True
    else:
        return False


def send_fire(sock: socket, coords: tuple) -> str: # возвращает 0 - мимо, 1 - попал, 2 - потопил, 3 - победил

    sock.send(bytes((3,coords[0],coords[1])))

    data = sock.recv(1024) 
    print(data)
     
    if data[0] == 3:
        if data[1] == 0:
            return data[2]
        else: 
            return False
        


def start_game(sock) -> bool:
    
    sock.send(bytes((4,)))

    data = sock.recv(1024) 
    print(data)
    
    if data == bytearray((4,0)):
        return True
    else:
        return False


def find_player(sock) -> str:

    sock.send(bytes((6,)))

    data = sock.recv(1024) 
    print(data)
       
    if data[0] == 6:
        if (data[1]) == 0:
            return data[2]
        return False
    else:
        return False




def connect_to_host(addr: str, port: int) -> socket:

    sb_client_sock = socket.socket()
    sb_client_sock.connect((addr,port))

    return sb_client_sock


def check_connection(sock: socket) -> bool:

    sock.send(bytes((1,)))

    data = sock.recv(1024) 
    print(data)
    if data == bytearray((1,0)):
        return True
    else:
        return False


def disconnect_sock(sock: socket) -> bool:
    
    if sock != None:
        sock.send(bytes((5,)))

    data = sock.recv(1024) 
    print(data)
    if data == bytearray((5,0)):
        sock.close()
        return True
    else:
        return False

# def start_bot(sock: socket) -> bool:

#     sock.send(b'07')

#     data = sock.recv(1024) 
#     print(data)
#     if bytes.decode(data,'utf-8') == '07,ok':
#         return True
#     else:
#         return False
        

def receive_fire(sock, butnobj, gameobj):

    def listen_data(sock, butnobj,gameobj):
        print('im a thread')
        print(gameobj.enemy_round)
        print(gameobj.listen_sock)
        gameobj.listen_sock = True
        butnobj['text'] = 'Ход врага'
        data = sock.recv(1024)
        print(data)

        data_str_lst = bytes.decode(data,'utf-8').split(',')
        while data_str_lst[2] != '0':
            data = sock.recv(1024)
            print(data)
            data_str_lst = bytes.decode(data,'utf-8').split(',')
            gameobj.enemy_round = True
            butnobj['text'] = 'Ход врага'
        else:
            gameobj.listen_sock = False
            gameobj.enemy_round = False
        
        butnobj['text'] = 'Твой ход'
    if not gameobj.listen_sock:
        thread = threading.Thread(target=listen_data,name='listen_data',args=(sock,butnobj,gameobj))
        thread.start()
        print('thread started')
    else:
        print('Already listen')
        print(threading.active_count())
   