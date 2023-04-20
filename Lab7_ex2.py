import pygame as pg
import math

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height

    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))



pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
px, py = 20,20

# btn = Button(20,20,100,100)


while (run):
    firstObject = Rectangle(px, py, 100, 100)  # สร้าง Object จากคลาส Rectangle ขึ้นมา

    screen.fill((255, 255, 255))
    firstObject.draw(screen)
    pg.time.delay(30)
    pg.display.update()

    k = pg.key.get_pressed()
    if k[pg.K_w]:
        py -= 1
    if k[pg.K_s]:
        py += 1
    if k[pg.K_a]:
        px -= 1
    if k[pg.K_d]:
        px += 1







    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        # if event.type == pg.K_w:
        #     px += 1
        #     print('w')
        #     run = True
        # if event.type == pg.K_s:
        #     px -= 1
        # if event.type == pg.K_a:
        #     py -= 1
        # if event.type == pg.K_d:
        #     py += 1


        # if event.type == pg.KEYDOWN:
        #     pg.quit()
        #     run = False