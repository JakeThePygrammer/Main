import pygame as pg
import pygamebg
(width,height) = (300,300)
window = pygamebg.open_window(width,height,"Ladder")
window.fill(pg.Color("Beige"))
pg.draw.line(window, pg.Color("Brown"),(100,10),(100, height-10),  10)
pg.draw.line(window, pg.Color("Brown"),(200,10),(200, height-10),  10)

for index in range(40,251,50):
    pg.draw.line(window, pg.Color("Brown"), (100, index), (200, index), 10)

pygamebg.wait_loop()