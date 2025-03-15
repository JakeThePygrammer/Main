import pygame as pg
import pygamebg
(width,height) = (500,500)
window = pygamebg.open_window(width,height,"Circles")
window.fill(pg.Color("orange"))
pg.draw.circle(window,(255,0,0),(250,250),225)
pg.draw.circle(window,(0,0,255),(250,250),175)
pg.draw.circle(window,(0,255,0),(250,250),125)
pg.draw.circle(window,(255,0,255),(250,250),75)
pg.draw.circle(window,(255,255,255),(250,250),25)

pygamebg.wait_loop()
