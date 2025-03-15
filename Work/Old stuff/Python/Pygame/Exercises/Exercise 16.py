import pygame as pg
import pygamebg


(width,height) = (400,100)
window = pygamebg.open_window(width,height,"Lights")

def draw():
    window.fill(pg.Color("Black"))
    for index in range(20,400,40):
        pg.draw.circle(window,pg.Color("Gray"), (index, 50), 15)

a = 20

def new_frame():
    global a
    window.fill(pg.Color("Black"))
    draw()
    pg.draw.circle(window, pg.Color("Yellow"), (a, 50), 15)
    a += 40
    if a >= 380:
        a = 20

pygamebg.frame_loop(10,new_frame)
