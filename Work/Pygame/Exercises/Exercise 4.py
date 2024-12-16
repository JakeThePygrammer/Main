import pygame as pg
import pygamebg
(width,height) = (600,400)
window = pygamebg.open_window(width,height,"German flag")

window.fill(pg.Color("yellow"))

pg.draw.rect(window,(0,0,0),(0, 0, 600,133))
pg.draw.rect(window,(255,0,0),(0, 133, 600,133))
pg.draw.rect(window,(255,255,0),(0, 266, 600,133))


pygamebg.wait_loop()
