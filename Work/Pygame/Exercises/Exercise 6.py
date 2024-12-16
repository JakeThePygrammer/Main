import pygame as pg
import pygamebg
(width,height) = (200,200)
window = pygamebg.open_window(width,height,"Circles")
window.fill(pg.Color("cyan"))
pg.draw.circle(window,(255,0,0),(75,75),50)
pg.draw.circle(window,(255,0,0),(125,75),50)
pg.draw.polygon(window,(255,0,0),[(30,95),(100,50),(170,95),(100,175)])
pygamebg.wait_loop()
