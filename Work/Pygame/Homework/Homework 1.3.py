import pygame as pg
import pygamebg
(width,height) = (200,200)
window = pygamebg.open_window(width,height,"Hospital")
window.fill((0, 0, 255))
pg.draw.rect(window, pg.Color("White"), (40,30,40,140))
pg.draw.rect(window, pg.Color("White"), (120,30,40,140))
pg.draw.rect(window, pg.Color("White"), (40,90,120,20))
pygamebg.wait_loop()
