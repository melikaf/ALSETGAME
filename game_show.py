import pygame
cell_dict = dict()
red = (255, 0, 0)
light_red = (150,0,0)
light_blue = (0,0,150)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128,128,128)

view_red = (255, 213, 150)
view_blue = (200,231,255)
m = 10
n = 10

cells = []


class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.visit = []


def init_board():
    import random
    for i in range(m):
        for j in range(n):
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
            p = Cell(i, j, c)
            cell_dict[(i,j)] = []
            cell_dict[(i, j)] = p
            cells.append(p)


def update_light():
    for i in range(m):
            for j in range(n):
                c = cell_dict.get((i,j))

                nei1 = cell_dict.get((i-1, j))
                nei2 = cell_dict.get((i+1, j))
                nei3 = cell_dict.get((i, j-1))
                nei4 = cell_dict.get((i, j+1))

                if c:
                    c.visit = []
                    if nei1:
                        if nei1.val == 'B':
                            c.visit.append('B')
                        if nei1.val == 'R':
                            c.visit.append('R')
                    if nei2:
                        if nei2.val == 'B':
                            c.visit.append('B')
                        if nei2.val == 'R':
                            c.visit.append('R')

                    if nei3:
                        if nei3.val == 'B':
                            c.visit.append('B')
                        if nei3.val == 'R':
                            c.visit.append('R')

                    if nei4:
                        if nei4.val == 'B':
                            c.visit.append('B')
                        if nei4.val == 'R':
                            c.visit.append('R')
                    cell_dict[(i,j)] = c


def show_game():

    #init_board()
    #print('behamdellah')
    gameDisplay = pygame.display.set_mode((600,600))
    #print(':DDDDDD')
    pygame.display.set_caption("GAME!")
    gameExit = False
    #while not gameExit:
    for p in range(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        gameDisplay.fill(gray)


        update_light()



        for i in range(0, 600, 60):

            pygame.draw.line(gameDisplay, black, (0, i), (600, i))
            pygame.draw.line(gameDisplay, black, (i, 0), (i, 600))

        x = 0
        y = 0
        for i in range(0, 600, 60):
            x += 1
            y = 0
            for j in range(0, 600, 60):
                y += 1
                cel = cell_dict.get((x,y))
                # if cel and len(cel.visit) > 0:
                #     if 'B' in cel.visit and 'R' in cel.visit:
                #         pygame.draw.rect(gameDisplay,white, [i, j, 60, 60])
                #     elif 'B' in cel.visit:
                #         pygame.draw.rect(gameDisplay,view_blue, [i, j, 60, 60])
                #     elif 'R' in cel.visit:
                #         pygame.draw.rect(gameDisplay,view_red, [i, j, 60, 60])

                if cel and cel.val == '#':
                    pygame.draw.rect(gameDisplay,black, [i, j, 60, 60])
                if cel and cel.val == 'B':
                    pygame.draw.circle(gameDisplay, blue, [i+30,j+30], 25)
                if cel and cel.val == 'R':
                    pygame.draw.circle(gameDisplay, red, [i+30, j+30], 25)
                if cel and cel.val == 'r':
                    pygame.draw.polygon(gameDisplay, light_red, [[i+30, j+10], [i+50, j+30], [i+30, j+50], [i+10,j+30]], 0)

                if cel and cel.val == 'b':
                    pygame.draw.polygon(gameDisplay, light_blue, [[i+30, j+10], [i+50, j+30], [i+30, j+50], [i+10,j+30]], 0)
                if cel and cel.val == 'g':
                    pygame.draw.polygon(gameDisplay, green, [[i+30, j+10], [i+50, j+30], [i+30, j+50], [i+10,j+30]], 0)
        pygame.display.update()
        #circle(Surface, color, pos, radius, width=0)


