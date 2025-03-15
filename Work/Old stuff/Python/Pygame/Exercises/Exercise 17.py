import pygame as pg
import pygamebg


(width,height) = (225,225)
window = pygamebg.open_window(width,height,"Sun")
window.fill(pg.Color("White"))

Sunshine = pg.image.load("../Images/Sun.png")
a = 0

def new_frame():
    global Sunshine, a
    window.fill(pg.Color("White"))
    Sun = pg.transform.rotate(Sunshine, a)
    x = Sun.get_rect(center = (112, 112))
    window.blit(Sun,x)
    a += 5
    if a >= 360:
        a = 0

pygamebg.frame_loop(10,new_frame)
