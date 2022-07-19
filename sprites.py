import pygame
from pygame import gfxdraw


def bigPixel(surf: pygame.surface, cords: tuple, color: tuple):
    x, y = cords
    limits_x = (x * 5, (x + 1) * 5)
    limits_y = (y * 5, (y + 1) * 5)
    for x in range(*limits_x):
        for y in range(*limits_y):
            gfxdraw.pixel(surf, x, y, color)


class Dinosaur:
    def __init__(self, rect):
        self.rect = rect
        self.pixels = list()
        for x_i in range(240):
            self.pixels.append([])
            for y_i in range(80):
                self.pixels[x_i].append('')

    def head(self, c):
        x_s, y_s = [i // 5 for i in self.rect[:2]]
        x_eye, y_eye = x_s + 17, y_s + 1
        for x in range(x_eye - 2, x_eye + 10):
            for y in range(y_eye - 1, y_eye + 5):
                self.pixels[x][y] = c
        self.pixels[x_eye][y_eye] = ''
        self.pixels[x_eye - 2][y_eye - 1] = ''
        self.pixels[x_eye + 9][y_eye - 1] = ''
        for x in range(x_eye - 2, x_eye + 4):
            self.pixels[x][y_eye + 5] = c
        for x in range(x_eye - 2, x_eye + 8):
            self.pixels[x][y_eye + 6] = c

    def body(self, c):
        x_s, y_s = [i // 5 for i in self.rect[:2]]
        x_eye, y_eye = x_s + 17, y_s + 1
        for x in range(x_eye - 3, x_eye + 3):
            self.pixels[x][y_eye + 7] = c
        for x in range(x_eye - 5, x_eye + 3):
            self.pixels[x][y_eye + 8] = c
        for x in range(x_eye - 7, x_eye + 6):
            self.pixels[x][y_eye + 9] = c
        self.pixels[x_eye + 5][y_eye + 10] = c
        for x in range(x_eye - 8, x_eye + 3):
            self.pixels[x][y_eye + 10] = c
        for x in range(x_eye - 13, x_eye + 3):
            for y in range(y_eye + 11, y_eye + 13):
                self.pixels[x][y] = c
        for x in range(x_eye - 12, x_eye + 2):
            self.pixels[x][y_eye + 13] = c
        for x in range(x_eye - 11, x_eye + 2):
            self.pixels[x][y_eye + 14] = c
        for x in range(x_eye - 10, x_eye + 1):
            self.pixels[x][y_eye + 15] = c

    def tail(self, c):
        x_s, y_s = [i // 5 for i in self.rect[:2]]
        x_eye, y_eye = x_s + 17, y_s + 1
        for x in range(x_eye - 13, x_eye - 10):
            self.pixels[x][y_eye + 10] = c
        for x in range(x_eye - 13, x_eye - 11):
            self.pixels[x][y_eye + 9] = c
        for y in range(y_eye + 7, y_eye + 9):
            self.pixels[x_eye - 13][y] = c

    def leftLeg(self, c):
        x_s, y_s = [i // 5 for i in self.rect[:2]]
        x_eye, y_eye = x_s + 17, y_s + 1
        for x in range(x_eye - 9, x_eye - 6):
            self.pixels[x][y_eye + 16] = c
        for x in range(x_eye - 9, x_eye - 7):
            self.pixels[x][y_eye + 17] = c
        self.pixels[x_eye - 9][y_eye + 18] = c
        for x in range(x_eye - 9, x_eye - 7):
            self.pixels[x][y_eye + 19] = c

    def rightLeg(self, c):
        x_s, y_s = [i // 5 for i in self.rect[:2]]
        x_eye, y_eye = x_s + 17, y_s + 1
        for x in range(x_eye - 1, x_eye + 1):
            self.pixels[x][y_eye + 16] = c
        self.pixels[x_eye][y_eye + 17] = c
        self.pixels[x_eye][y_eye + 18] = c
        for x in range(x_eye, x_eye + 2):
            self.pixels[x][y_eye + 19] = c

    def idle(self):
        self.head('d')
        self.body('d')
        self.tail('d')
        self.head('d')
        self.rightLeg('d')
        self.leftLeg('d')

    def draw(self, scr):
        for x in range(240):
            for y in range(80):
                if self.pixels[x][y] == 'd':
                    bigPixel(scr, (x, y), (100, 100, 100))

    def run(self, is_right_leg_up):
        x_s, y_s = [i // 5 for i in self.rect[:2]]
        x_eye, y_eye = x_s + 17, y_s + 1
        if is_right_leg_up:
            self.rightLeg('')
            for x in range(x_eye - 1, x_eye + 1):
                self.pixels[x][y_eye + 14] = 'd'
            self.pixels[x_eye][y_eye + 15] = 'd'
            self.pixels[x_eye][y_eye + 16] = 'd'
            for x in range(x_eye, x_eye + 2):
                self.pixels[x][y_eye + 17] = 'd'
        else:
            self.leftLeg('')
            for x in range(x_eye - 9, x_eye - 6):
                self.pixels[x][y_eye + 14] = 'd'
            for x in range(x_eye - 9, x_eye - 7):
                self.pixels[x][y_eye + 15] = 'd'
            self.pixels[x_eye - 9][y_eye + 16] = 'd'
            for x in range(x_eye - 9, x_eye - 7):
                self.pixels[x][y_eye + 17] = 'd'

    def lay(self):
        self.head('')
        self.body('')
        self.tail('')

        x_s, y_s = [i // 5 for i in self.rect[:2]]
        x_eye, y_eye = x_s + 17, y_s + 1

        # body
        for x in range(x_eye - 10, x_eye + 1):
            self.pixels[x][y_eye + 15] = 'd'
        for x in range(x_eye - 10, x_eye + 6):
            self.pixels[x][y_eye + 14] = 'd'
        for x in range(x_eye - 11, x_eye + 6):
            self.pixels[x][y_eye + 13] = 'd'
        for x in range(x_eye - 12, x_eye + 9):
            self.pixels[x][y_eye + 12] = 'd'
        for x in range(x_eye - 13, x_eye + 9):
            self.pixels[x][y_eye + 11] = 'd'
        for x in range(x_eye - 14, x_eye + 9):
            self.pixels[x][y_eye + 10] = 'd'
        for x in range(x_eye - 15, x_eye + 9):
            self.pixels[x][y_eye + 9] = 'd'
        for x in range(x_eye - 16, x_eye + 9):
            self.pixels[x][y_eye + 8] = 'd'
        for x in range(x_eye - 9, x_eye + 5):
            self.pixels[x][y_eye + 7] = 'd'

        # tail
        for x in range(x_eye - 17, x_eye - 14):
            self.pixels[x][y_eye + 7] = 'd'
        self.pixels[x_eye - 17][y_eye + 6] = 'd'

        # head
        for x in range(x_eye + 9, x_eye + 19):
            self.pixels[x][y_eye + 6] = 'd'
        for x in range(x_eye + 8, x_eye + 20):
            for y in range(y_eye + 7, y_eye + 12):
                self.pixels[x][y] = 'd'
        for x in range(x_eye + 8, x_eye + 14):
            self.pixels[x][y_eye + 12] = 'd'
        for x in range(x_eye + 8, x_eye + 18):
            self.pixels[x][y_eye + 13] = 'd'
        self.pixels[x_eye + 10][y_eye + 7] = ''

    def jump(self, direction):
        if direction == 'up':
            self.rect[1] -= 8
        else:
            self.rect[1] += 8


class Cactus:
    def __init__(self, num, types):
        self.num = num
        self.types = types
        self.width = num * 11
        self.height = 17 if 2 in self.types else 13
        self.y = 43
        self.x = 241
        self.pixels = list()
        for x_i in range(280):
            self.pixels.append([])
            for y_i in range(80):
                self.pixels[x_i].append('')

    def matrix(self, c):
        count = 0
        for t in self.types:
            if t == 1:
                for x in range(self.x + count * 11 + 3, self.x + count * 11 + 7):
                    for y in range(self.y + 4, self.y + 17):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11, self.x + count * 11 + 2):
                    for y in range(self.y + 6, self.y + 10):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11, self.x + count * 11 + 3):
                    for y in range(self.y + 10, self.y + 12):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11 + 8, self.x + count * 11 + 10):
                    for y in range(self.y + 7, self.y + 12):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11 + 7, self.x + count * 11 + 10):
                    for y in range(self.y + 12, self.y + 14):
                        self.pixels[x][y] = c
            if t == 2:
                for x in range(self.x + count * 11 + 3, self.x + count * 11 + 7):
                    for y in range(self.y, self.y + 17):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11, self.x + count * 11 + 2):
                    for y in range(self.y + 3, self.y + 10):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11, self.x + count * 11 + 3):
                    for y in range(self.y + 10, self.y + 12):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11 + 8, self.x + count * 11 + 10):
                    for y in range(self.y + 2, self.y + 10):
                        self.pixels[x][y] = c
                for x in range(self.x + count * 11 + 7, self.x + count * 11 + 10):
                    for y in range(self.y + 8, self.y + 10):
                        self.pixels[x][y] = c
            count += 1

    def clear(self):
        self.matrix('')

    def draw(self, scr):
        self.matrix('c')
        for x in range(270):
            for y in range(80):
                if self.pixels[x][y] == 'c':
                    bigPixel(scr, (x, y), (100, 100, 100))


class Bird:
    def __init__(self, type):
        self.type = type
        self.x = 241
        if type == 1:
            self.y = 16
        elif type == 2:
            self.y = 27
        else:
            self.y = 30
        self.width = 23
        self.height = 22
        self.pixels = list()
        for x_i in range(270):
            self.pixels.append([])
            for y_i in range(80):
                self.pixels[x_i].append('')

    def head(self, c):
        for x in range(self.x, self.x + 7):
            self.pixels[x][self.y + self.height // 2] = c
        for x in range(self.x + 1, self.x + 7):
            self.pixels[x][self.y + self.height // 2 - 1] = c
        for x in range(self.x + 2, self.x + 7):
            self.pixels[x][self.y + self.height // 2 - 2] = c
        for x in range(self.x + 3, self.x + 6):
            self.pixels[x][self.y + self.height // 2 - 3] = c
        for x in range(self.x + 4, self.x + 6):
            self.pixels[x][self.y + self.height // 2 - 4] = c

    def body_up(self, c):
        for x in range(self.x + 7, self.x + 21):
            self.pixels[x][self.y + self.height // 2] = c
        for x in range(self.x + 5, self.x + 18):
            self.pixels[x][self.y + self.height // 2 + 1] = c
        for x in range(self.x + 7, self.x + 20):
            self.pixels[x][self.y + self.height // 2 + 2] = c
        for x in range(self.x + 9, self.x + 17):
            self.pixels[x][self.y + self.height // 2 + 3] = c

    def wing_up(self, c):
        for x in range(self.x + 8, self.x + 16):
            self.pixels[x][self.y + self.height // 2 - 1] = c
        for x in range(self.x + 8, self.x + 15):
            self.pixels[x][self.y + self.height // 2 - 2] = c
        for x in range(self.x + 8, self.x + 14):
            self.pixels[x][self.y + self.height // 2 - 3] = c
        for x in range(self.x + 8, self.x + 13):
            self.pixels[x][self.y + self.height // 2 - 4] = c
        for x in range(self.x + 8, self.x + 12):
            for y in range(self.y + self.height // 2 - 5, self.y + self.height // 2 - 7, -1):
                self.pixels[x][y] = c
        for x in range(self.x + 8, self.x + 11):
            self.pixels[x][self.y + self.height // 2 - 7] = c
        for x in range(self.x + 8, self.x + 10):
            self.pixels[x][self.y + self.height // 2 - 8] = c
        self.pixels[self.x + 8][self.y + self.height // 2 - 9] = c

    def body_down(self, c):
        for x in range(self.x + 7, self.x + 16):
            self.pixels[x][self.y + self.height // 2] = c
        for x in range(self.x + 7, self.x + 17):
            self.pixels[x][self.y + self.height // 2+1] = c
        for x in range(self.x + 8, self.x + 22):
            self.pixels[x][self.y + self.height // 2+2] = c
        for x in range(self.x + 8, self.x + 19):
            self.pixels[x][self.y + self.height // 2+3] = c
        for x in range(self.x + 8, self.x + 21):
            self.pixels[x][self.y + self.height // 2+4] = c
        for x in range(self.x + 8, self.x + 18):
            self.pixels[x][self.y + self.height // 2+5] = c

    def wing_down(self, c):
        for x in range(self.x + 8, self.x + 12):
            self.pixels[x][self.y + self.height // 2+6] = c
        for x in range(self.x + 8, self.x + 11):
            self.pixels[x][self.y + self.height // 2+7] = c
        for x in range(self.x + 8, self.x + 10):
            self.pixels[x][self.y + self.height // 2+8] = c
        for x in range(self.x + 8, self.x + 10):
            self.pixels[x][self.y + self.height // 2+9] = c
        self.pixels[self.x + 8][self.y + self.height // 2 + 10] = c

    def clear(self):
        self.head('')
        self.wing_down('')
        self.wing_up('')
        self.body_up('')
        self.body_down('')

    def up(self):
        self.head('')
        self.body_down('')
        self.wing_down('')
        if self.y % 2 == 0:
            self.y += 5
        self.body_up('b')
        self.wing_up('b')
        self.head('b')

    def down(self):
        self.head('')
        self.body_up('')
        self.wing_up('')
        if self.y % 2 != 0:
            self.y -= 5
        self.body_down('b')
        self.wing_down('b')
        self.head('b')

    def draw(self, scr, is_up):
        # self.clear()
        if is_up:
            self.up()
        else:
            self.down()
        for x in range(270):
            for y in range(80):
                if self.pixels[x][y] == 'b':
                    bigPixel(scr, (x, y), (100, 100, 100))
