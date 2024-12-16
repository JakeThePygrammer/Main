import pygame as pg
import pygamebg
(width,height) = (550,150)
window = pygamebg.open_window(width,height,"Squares")

window.fill(pg.Color("black"))

pg.draw.rect(window,(255,0,0),(50, 50, 50,50))
pg.draw.rect(window,(0,255,0),(150, 50, 50,50))
pg.draw.rect(window,(0,0,255),(250, 50, 50,50))
pg.draw.rect(window,(255,255,0),(350, 50, 50,50))
pg.draw.rect(window,(255,255,255),(450, 50, 50,50))

pygamebg.wait_loop()
