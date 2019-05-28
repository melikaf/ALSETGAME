import json
from client_utils import send_info, get_info, get_player_state, get_vision, set_player_move
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 20007  # The port used by the server

'''
This file is only for communication with Server.py and get message about
STATE, INFO, Vision and send message about INFO and MOVE to the server.

Each message is a json that has a header that shows what kind of information that cantains:

INFO: The information that has been sent by other opponent.
SSTATE: Our players locations in the current round.
VISION: The status of cells that are neighbour to our players and we are aware of them.
MOVE: our decision for moving our players in this round. it could be U or D or L or R for each or our players.
'''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    import pickle

    while True:

        out_info = send_info()
        s.sendall(pickle.dumps(out_info))
        print("sent")
        data = pickle.loads(s.recv(4194304))
        header = data.get("header")
        if header == 'INFO':
            info = get_info(data)
        if header == 'STATE':
            get_player_state(data)
        if header == 'VISION':
            get_vision(data)
        out_data = set_player_move()
        s.sendall(pickle.dumps(out_data))
        print('data', data)
        #print(data)
