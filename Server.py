#!/usr/bin/env python3
import json
import socket
import pickle
from server_utils import init_board, check_and_send_info

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    con1, addr = s.accept()
    con2, addr2 = s.accept()

    init_board()
    with con1 and con2:
        print('First Connected by', addr)
        print('Second Connected by', addr2)

        while True:
            data1 = pickle.loads(con1.recv(1024))
            header1 = data1.get("header")

            data2 = pickle.loads(con2.recv(1024))
            header2 = data2.get("header")

            if header1 == 'INFO':
                check_and_send_info(data1, con2)
            if header2 == 'INFO':
                check_and_send_info(data2, con1)



            #if data1:
            #    print("good")
            #    con1.sendall(pickle.dumps((data1)))
            #if data2:
            #    print("hey")
            #    con2.sendall(pickle.dumps((data2)))
