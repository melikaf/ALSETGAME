import json
import pickle
from game_show import Cell, cell_dict, cells
n = 10
m = 10


class Score:
    scoreB = 0
    scoreR = 0


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


def send_player_vision(con, col):
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

    con.sendall((pickle.dumps(data)))


def send_player_state(con, col):
    states = dict()
    states['header'] = 'STATE'
    states['X'] = []
    states['Y'] = []
    states['VAL'] = []
    for cell in cells:
        if cell.val == col:
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

        x = X[i]
        y = Y[i]
        here = cell_dict.get((x, y))
        moved = False
        if here:
            if val[i] == 'D':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x+1, y))

                if c and c.val == '.':
                    moved = True
                    cell_dict[(x+1, y)].val = col
                if c and c.val == 'b' and col == 'B':
                    moved = True
                    Score.scoreB += 10
                    cell_dict[(x+1, y)].val = col

                if c and c.val == 'r' and col == 'R':
                    moved = True
                    Score.scoreR += 10
                    cell_dict[(x+1, y)].val = col


            if val[i] == 'U':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x-1, y))
                if c and c.val == '.':
                    moved = True
                    cell_dict[(x-1, y)].val = col

                if c and c.val == 'b' and col == 'B':
                    moved = True
                    Score.scoreB += 10
                    cell_dict[(x-1, y)].val = col

                if c and c.val == 'r' and col == 'R':
                    Score.scoreR += 10
                    cell_dict[(x-1, y)].val = col
                    moved = True


            if val[i] == 'R':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x, y+1))
                if c and c.val == '.':
                    moved = True
                    cell_dict[(x, y+1)].val = col
                if c and c.val == 'b' and col == 'B':
                    moved = True
                    Score.scoreB += 10
                    cell_dict[(x, y+1)].val = col

                if c and c.val == 'r' and col == 'R':
                    Score.scoreR += 10
                    cell_dict[(x, y+1)].val = col
                    moved = True

            if val[i] == 'L':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x, y-1))
                if c and c.val == '.':
                    cell_dict[(x, y-1)].val = col
                    moved = True

                if c and c.val == 'b' and col == 'B':
                    Score.scoreB += 10
                    cell_dict[(x, y-1)].val = col
                    moved = True

                if c and c.val == 'r' and col == 'R':
                    Score.scoreR += 10
                    cell_dict[(x, y-1)].val = col
                    moved = True

            if moved:
                cell_dict[(x, y)] = Cell(x,y, '.')