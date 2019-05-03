import json
import pickle

n = 10
m = 10
cell_dict = dict()
cells = []


class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val


def init_board():
    for i in range(m):
        for j in range(n):
            p = Cell(i, j, '.')
            cell_dict[(i,j)] = []
            cell_dict[(i, j)] = p


def check_and_send_info(data, con):
    x = data['X']
    y = data['Y']
    vals = data['VAL']

    print(x, type(x))
    try:
        for i in x:
            int(i)
        for j in y:
            int(j)
        good_val = True
        for v in vals:
            if len(v) > 1:
                good_val = False
        if good_val:
            con.sendall(pickle.dumps(data))
    except:
        # TODO: send some empty data to opponent
        print("message is unvalid")


def send_player_vision(col):
    data = dict()
    data['header'] = 'VISION'
    data['X'] = []
    data['Y'] = []
    data['VAL'] = []
    for cell in cells:
        if cell.val == col:
            x = cell.x
            y = cell.y
            nei1 = cell_dict.get((x-1,y))
            nei2 = cell_dict.get((x+1,y))
            nei3 = cell_dict.get((x, y-1))
            nei4 = cell_dict.get((x, y+1))
            if nei1:
                data['X'].append(nei1.x)
                data['Y'].append(nei1.y)
                data['VAL'].append(nei1.val)

            if nei2:
                data['X'].append(nei2.x)
                data['Y'].append(nei2.y)
                data['VAL'].append(nei2.val)

            if nei3:
                data['X'].append(nei3.x)
                data['Y'].append(nei3.y)
                data['VAL'].append(nei3.val)
            if nei4:
                data['X'].append(nei4.x)
                data['Y'].append(nei4.y)
                data['VAL'].append(nei4.val)

    return data


def send_player_state(con, turn):
    states = dict()
    states['header'] = 'STATE'
    states['X'] = []
    states['Y'] = []
    states['VAL'] = []
    for cell in cells:
        if cell.val == turn:
            states['X'].append(cell.x)
            states['Y'].append(cell.y)
            states['VAL'].append(cell.val)
    con.sendall(pickle.dumps(states))


def get_player_move(data, col):
    X = data.get('X')
    Y = data.get('Y')
    val = data.get('VAL')

    #TODO : Healer check
    for i in range(len(X)):
        if val[i] == 'D':
            x = X[i]
            y = Y[i]
            c = cell_dict.get((x+1, y))
            if c and c.val == '.':
                cell_dict[(x+1, y)].val = col
        if val[i] == 'U':
            x = X[i]
            y = Y[i]
            c = cell_dict.get((x-1, y))
            if c and c.val == '.':
                cell_dict[(x-1, y)].val = col
        if val[i] == 'R':
            x = X[i]
            y = Y[i]
            c = cell_dict.get((x, y+1))
            if c and c.val == '.':
                cell_dict[(x, y+1)].val = col
        if val[i] == 'L':
            x = X[i]
            y = Y[i]
            c = cell_dict.get((x, y-1))
            if c and c.val == '.':
                cell_dict[(x, y-1)].val = col