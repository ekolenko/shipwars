
import socket


def send_field(sock: socket, str_in: str) -> bool:

    sock.send(bytes('02,' + str_in,'utf-8'))

    data = sock.recv(1024) 
    if bytes.decode(data,'utf-8') == '02,ok':
        return True
    else:
        return False


def send_fire(sock: socket, str_in: str) -> str:

    sock.send(bytes('03,' + str_in,'utf-8'))

    data = sock.recv(1024) 
    data_str_lst = bytes.decode(data,'utf-8').split(',')
    
    if data_str_lst[0] == '03':
        return (data_str_lst[1])


def connect_to_host(addr: str, port: int) -> socket:

    sb_client_sock = socket.socket()
    sb_client_sock.connect((addr,port))

    return sb_client_sock


def check_connection(sock: socket) -> bool:

    sock.send(b'01')

    data = sock.recv(1024) 
    if bytes.decode(data,'utf-8') == '01,ok':
        return True
    else:
        return False


def disconnect_sock(sock: socket) -> bool:
    
    sock.send(b'05')

    data = sock.recv(1024) 
    if bytes.decode(data,'utf-8') == '05,ok':
        sock.close()
        return True
    else:
        return False