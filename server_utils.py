import json
import pickle
from score_class import Score
from game_show import Cell, cell_dict, true_info, false_info
n = 10
m = 10


'''

The server side logic of the game can be found here.

'''


def check_and_send_info(data, con, col):
    x = data['X']
    y = data['Y']
    del true_info[0 : len(true_info)-1]
    del false_info[0 : len(false_info)-1]

    vals = data['VAL']

    #print(x, type(x))
    try:
        for i in x:
            int(i)
        for j in y:
            int(j)
        good_val = True
        for v in vals:
            if len(v) > 1:
                good_val = False
                #print('v', v)
        #print('helllo', x, y)
        for i in range(len(x)):
            X = x[i]
            Y = y[i]
            V = vals[i]
            #print('INFO', (X,Y,V))
            if V == cell_dict[(X,Y)].val:
                true_info.append((X,Y,col))
            else:
                false_info.append((X,Y,col))
            #print('TRUE!!', true_info)
            #print('FALSE!!', false_info)
        if good_val:
            #print('inje')
            con.sendall(pickle.dumps(data))
            #print('unja')
    except:
        # TODO: send some empty data to opponent
        print("message is unvalid")


def send_player_vision(con, col):
    data = dict()
    data['header'] = 'VISION'
    data['X'] = []
    data['Y'] = []
    data['VAL'] = []
    for p in cell_dict:
        cell = cell_dict[p]
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
    for p in cell_dict:
        cell = cell_dict[p]
        if cell.val == col:
            #print("STATE", col, cell.x, cell.y)
            states['X'].append(cell.x)
            states['Y'].append(cell.y)
            states['VAL'].append(cell.val)
    con.sendall(pickle.dumps(states))


def get_player_move(data, col):
    X = data.get('X')
    Y = data.get('Y')
    val = data.get('VAL')

    for i in range(len(X)):

        x = X[i]
        y = Y[i]
        here = cell_dict.get((x, y))
        moved = False

        if here and here.val == col:
            if val[i] == 'D':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x+1, y))

                if c and c.val == '.':
                    moved = True
                    cell_dict[(x+1, y)] = Cell(x+1, y, col)
                if c and c.val == 'b' and col == 'B':
                    moved = True
                    Score.scoreB += 10
                    cell_dict[(x+1, y)] = Cell(x+1, y, col)

                if c and c.val == 'r' and col == 'R':
                    moved = True
                    Score.scoreR += 10
                    cell_dict[(x+1, y)] = Cell(x+1, y, col)
                if c and c.val == 'g':
                    moved = True
                    cell_dict[(x+1, y)] = Cell(x+1, y, col)
                    if col == 'R':
                        Score.scoreR += 20
                    if col == 'B':
                        Score.scoreB += 20
            elif val[i] == 'U':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x-1, y))
                if c and c.val == '.':
                    moved = True
                    cell_dict[(x-1, y)] = Cell(x-1, y, col)

                if c and c.val == 'b' and col == 'B':
                    moved = True
                    Score.scoreB += 10
                    cell_dict[(x-1, y)] = Cell(x-1, y, col)

                if c and c.val == 'r' and col == 'R':
                    Score.scoreR += 10
                    cell_dict[(x-1, y)] = Cell(x-1, y, col)
                    moved = True
                if c and c.val == 'g':
                    moved = True
                    cell_dict[(x-1, y)] = Cell(x-1, y, col)
                    if col == 'R':
                        Score.scoreR += 20
                    if col == 'B':
                        Score.scoreB += 20
            elif val[i] == 'R':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x, y+1))
                if c and c.val == '.':
                    moved = True
                    cell_dict[(x, y+1)] = Cell(x, y+1, col)
                if c and c.val == 'b' and col == 'B':
                    moved = True
                    Score.scoreB += 10
                    cell_dict[(x, y+1)] = Cell(x, y+1, col)

                if c and c.val == 'r' and col == 'R':
                    Score.scoreR += 10
                    cell_dict[(x, y+1)] = Cell(x, y+1, col)
                    moved = True
                if c and c.val == 'g':
                    moved = True
                    cell_dict[(x, y+1)] = Cell(x, y+1, col)
                    if col == 'R':
                        Score.scoreR += 20
                    if col == 'B':
                        Score.scoreB += 20
            elif val[i] == 'L':
                x = X[i]
                y = Y[i]
                c = cell_dict.get((x, y-1))
                if c and c.val == '.':
                    cell_dict[(x, y-1)] = Cell(x, y-1, col)
                    moved = True

                if c and c.val == 'b' and col == 'B':
                    Score.scoreB += 10
                    cell_dict[(x, y-1)] = Cell(x, y-1, col)
                    moved = True

                if c and c.val == 'r' and col == 'R':
                    Score.scoreR += 10
                    cell_dict[(x, y-1)] = Cell(x, y-1, col)
                    moved = True
                if c and c.val == 'g':
                    moved = True
                    cell_dict[(x, y-1)] = Cell(x, y-1, col)
                    if col == 'R':
                        Score.scoreR += 20
                    if col == 'B':
                        Score.scoreB += 20
            if moved:
                cell_dict[(x, y)] = Cell(x, y, '.')