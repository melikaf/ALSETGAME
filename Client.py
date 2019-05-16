import json
from client_utils import send_info, get_info, get_player_state, get_vision, set_player_move
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 20002  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    import pickle

    while(True):

        out_info = send_info()
        s.sendall(pickle.dumps(out_info))
        print("sent")
        data = pickle.loads(s.recv(1024))
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
