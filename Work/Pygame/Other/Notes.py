import pygame as pg
import pygamebg
(width,height) = (500,500)
window = pygamebg.open_window(width,height,"Testing")

window.fill(pg.Color("red"))
window.fill((0, 255, 255))
pg.draw.line(window,(255,0,0),(200, 200), (200, 300), 30)
pygamebg.wait_loop()

#Ова создава прозорец во сина боја преку RGB кодот. Може да се додаваат линии со drawiline.

import pygame as pg
import pygamebg
(width,height) = (200,200)
window = pygamebg.open_window(width,height,"Letter A")
window.fill((0, 255, 255))
pg.draw.rect(window,(0,0,0),(25, 50, 150,100), 2)
pg.draw.rect(window,pg.Color("White"),(50, 75, 100,50),)
pygamebg.wait_loop()

#Ова става правоаголник во правоаголник.
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

#Ова става круг во круг.