import pygame as pg
import sys

class Rec:
    def __init__(self, x=0, y=0, w=0, h=0, r=0, g=0, b=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.g = g
        self.b = b

    def draw(self, screen):
        pg.draw.rect(screen,(self.r, self.g, self.b),(self.x, self.y, self.w, self.h))

class Button(Rec):
    def __init__(self, x=0, y=0, w=0, h=0,r=0,g=0,b=0):
        Rec.__init__(self, x, y, w, h,r,g,b)
    def ismouseon(self):
        # m = pg.mouse.get_pos()
        if (20, 20) <= pg.mouse.get_pos() and pg.mouse.get_pos() <= (120, 120):
            return True
        else:
            return False


pg.init()
cr = True
win_x = 800
win_y = 480
color_w = (255, 255, 255)
m = pg.mouse.get_pos()
screen = pg.display.set_mode((win_x,win_y))

px,py=20,20

################################
while(cr):
    b = Button(20, 20, 100, 100,255,0,0)
    rb = Rec(px, py, 100, 100,255,0,0)
    gb = Rec(px, py, 100, 100,170,170,170)
    pb = Rec(px, py, 100, 100,120,20,220)

    screen.fill((255, 255, 255))


    if b.ismouseon()==True:
        gb.draw(screen)
        if pg.mouse.get_pressed()[0] and b.ismouseon()==True:
            pb.draw(screen)


    else:
        b.draw(screen)


    pg.display.update()
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            cr =False





