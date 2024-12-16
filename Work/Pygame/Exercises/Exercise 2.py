import pygame as pg
import pygamebg
pg.init()
(width,height) = (300,300)
window = pygamebg.open_window(width,height,"Antenna")
window.fill((0, 255, 255))
pg.draw.line(window,(0,0,0),(150, 10), (150, 290), 20)
pg.draw.line(window,(0,0,0),(50, 240), (240, 240), 20)
pg.draw.line(window,(0,0,0),(60, 200), (230, 200), 18)
pg.draw.line(window,(0,0,0),(70, 160), (220, 160), 16)
pg.draw.line(window,(0,0,0),(80, 117), (210, 117), 14)
pg.draw.line(window,(0,0,0),(90, 80), (200, 80), 12)
pg.draw.line(window,(0,0,0),(105, 45), (190, 45), 10)

pygamebg.wait_loop()
