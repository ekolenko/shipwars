
import socket
import threading


def send_field(sock: socket, str_in: str) -> bool:

    sock.send(bytes('02,' + str_in,'utf-8'))

    data = sock.recv(1024) 
    print(data)
    if bytes.decode(data,'utf-8') == '02,ok':
        return True
    else:
        return False


def send_fire(sock: socket, str_in: str) -> str: # возвращает 0 - мимо, 1 - попал, 2 - потопил, 3 - победил

    sock.send(bytes('03,' + str_in,'utf-8'))

    data = sock.recv(1024) 
    print(data)
    data_str_lst = bytes.decode(data,'utf-8').split(',')
    
    if data_str_lst[0] == '03':
        if data_str_lst[1] == 'ok':
            return data_str_lst[2]
        else: 
            return False
        


def start_game(sock) -> bool:
    
    sock.send(b'04')

    data = sock.recv(1024) 
    print(data)
    if bytes.decode(data,'utf-8') == '04,ok':
        return True
    else:
        return False


def find_player(sock) -> str:

    sock.send(b'06')

    data = sock.recv(1024) 
    print(data)
    data_str_lst = bytes.decode(data,'utf-8').split(',')
   
    if data_str_lst[0] == '06':
        if (data_str_lst[1]) == 'ok':
            return data_str_lst[2]
        return False
    else:
        return False




def connect_to_host(addr: str, port: int) -> socket:

    sb_client_sock = socket.socket()
    sb_client_sock.connect((addr,port))

    return sb_client_sock


def check_connection(sock: socket) -> bool:

    sock.send(b'01')

    data = sock.recv(1024) 
    print(data)
    if bytes.decode(data,'utf-8') == '01,ok':
        return True
    else:
        return False


def disconnect_sock(sock: socket) -> bool:
    
    if sock != None:
        sock.send(b'05')

    data = sock.recv(1024) 
    print(data)
    if bytes.decode(data,'utf-8') == '05,ok':
        sock.close()
        return True
    else:
        return False

def start_bot(sock: socket) -> bool:

    sock.send(b'07')

    data = sock.recv(1024) 
    print(data)
    if bytes.decode(data,'utf-8') == '07,ok':
        return True
    else:
        return False
        

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
   