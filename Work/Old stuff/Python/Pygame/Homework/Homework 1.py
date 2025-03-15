import pygame as pg
import pygamebg
(width,height) = (200,200)
window = pygamebg.open_window(width,height,"Switzerland")
window.fill((255, 0, 0))
pg.draw.rect(window, pg.Color("White"), (80,30,40,140))
pg.draw.rect(window, pg.Color("White"), (30,80,140,40))

pygamebg.wait_loop()
