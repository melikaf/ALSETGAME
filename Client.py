import json
from client_utils import send_info, get_info
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65431       # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    import pickle

    while(True):

        out_info = send_info()
        s.sendall(pickle.dumps(out_info))
        print("ferestadam")
        data = pickle.loads(s.recv(1024))
        info = get_info(data)
        print(data)
