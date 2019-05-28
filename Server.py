#!/usr/bin/env python3
import json
import socket
import pickle
import threading

import _thread
import time
from server_utils import check_and_send_info, get_player_move, send_player_vision, send_player_state
from game_show import show_game, init_board
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 20007  # Port to listen on (non-privileged ports are > 1023)

lock1 = threading.Lock()


'''

In this file the communication between server and client will be handled.

'''


def communicate_with_clients(con1, con2):
    #while True:
        num = 0
        try:
            print('hi')

            data1 = con1.recv(4194304)
            data2 = con2.recv(4194304)

            header1 = ""
            header2 = ""
            if data1:

                data1 = pickle.loads(data1)
                print('data', data1)

                header1 = data1.get("header")
            if data2:
                data2 = pickle.loads(data2)
                print('data2', data2)
                header2 = data2.get("header")

            print('data1', data1)
            print('data2', data2)
            if header1 == 'INFO':
                print('info came')
                check_and_send_info(data1, con2, 'B')
            if header1 == 'MOVES':
                get_player_move(data1, 'B')
            print(':D :D :D')


            if header2 == 'INFO':
                check_and_send_info(data2, con1, 'R')

            if header2 == 'MOVES':
                get_player_move(data2, 'R')

            print('inja')
            send_player_state(con1, 'B')
            send_player_state(con2, 'R')
            print('-------------')
            print(num)
            num += 1
            send_player_vision(con1, 'B')
            send_player_vision(con2, 'R')
        except Exception:
            import traceback
            print('heey')
            print(traceback.format_exc())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    con1, addr = s.accept()
    con2, addr2 = s.accept()

    init_board('map1.txt')

    with con1 and con2:
        try:
            while True:
                time.sleep(0.7)
                communicate_with_clients(con1, con2)
                show_game()
            ##_thread.start_new_thread(communicate_with_clients, (con1, con2))
            ##_thread.start_new_thread(show_game, (1,))
        except Exception:

            import traceback
            print (traceback.format_exc())
            #if data1:
            #    print("good")
            #    con1.sendall(pickle.dumps((data1)))
            #if data2:
            #    print("hey")
            #    con2.sendall(pickle.dumps((data2)))
