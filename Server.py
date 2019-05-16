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
PORT = 20002 # Port to listen on (non-privileged ports are > 1023)

lock1 = threading.Lock()


def communicate_with_clients(con1, con2):
    #while True:
        try:
            data1 = pickle.loads(con1.recv(1024))
            header1 = data1.get("header")
            data2 = pickle.loads(con2.recv(1024))
            header2 = data2.get("header")
            if header1 == 'INFO':
                check_and_send_info(data1, con2)
            if header2 == 'INFO':
                check_and_send_info(data2, con1)
            if header1 == 'MOVES':
                get_player_move(data1, 'B')
            if header2 == 'MOVES':
                get_player_move(data2, 'R')
            send_player_state(con1, 'B')
            send_player_state(con2, 'R')
            send_player_vision(con1, 'B')
            send_player_vision(con2, 'R')
        except Exception:
            import traceback
            print(traceback.format_exc())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    con1, addr = s.accept()
    con2, addr2 = s.accept()

    init_board()
    #show_game()

    with con1 and con2:
        try:
            while True:
                time.sleep(5)
                print( 'inja'
                )
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
