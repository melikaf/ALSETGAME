import json
import pickle

my_cells = []


class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val


def get_vision(data):
    x = data['X']
    y = data['Y']
    vals = data['VAL']


def get_player_state(data):
    x = data['X']
    y = data['Y']
    vals = data['VAL']

    try:
        for i in range(len(x)):
            my_cells.append(Cell(x[i],y[i],vals[i]))
    except:
        print("states are unvalid")
    return my_cells


def set_player_move():
    data = dict()
    data['header'] = 'MOVES'
    data['X'] = []
    data['Y'] = []
    data['VAL'] = [] # U/D/R/L
    for cell in my_cells:
        data['X'].append(cell.X)
        data['Y'].append(cell.Y)
        data['VAL'].append('D')
    return data


def get_info(data):
    x = data['X']
    y = data['Y']
    vals = data['VAL']

    try:
        for i in x:
            i
            #print(int(i))
        for j in y:
            j
            #print(int(j))
        for v in vals:
            v
            #print(v)
    except:
        print("message is unvalid")


def send_info():
    info = dict()
    info['header'] = 'INFO'
    info['X'] = [1,2,3,4,5]
    info['Y'] = [1,2,3,4,5]
    info['VAL'] = ['.', '.', '.', '.', '.']
    return info