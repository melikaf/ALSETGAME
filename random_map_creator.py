import random
import json
m = 10
n = 10
cells = []
for i in range(1, m+1):
    for j in range(1, n+1):
        c = '.'
        r = random.random()
        if r < 0.04:
            c = 'B'
        elif r > 0.96:
            c = 'R'
        elif r > 0.90:
            c = 'r'
        elif r < 0.10:
            c = 'b'
        elif r < 0.30:
            c = '#'
        elif r > 0.85:
            c = 'g'
        cells.append(c)


d = {'map1': cells}
json.dump(d, open('map1.txt','w'))