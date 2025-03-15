import pygame as pg
import pygamebg
(width,height) = (200,200)
window = pygamebg.open_window(width,height,"Letter A")
window.fill((0, 255, 255))
pg.draw.line(window,(255,0,0),(100, 50), (150, 150), 20)
pg.draw.line(window,(255,0,0),(100, 50), (50, 150), 20)
pg.draw.line(window,(255,0,0),(75, 100), (125, 100), 20)
pygamebg.wait_loop()
