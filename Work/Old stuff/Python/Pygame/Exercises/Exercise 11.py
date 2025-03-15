import pygame as pg
import pygamebg
(width,height) = (800,200)
window = pygamebg.open_window(width,height,"Circles")
window.fill(pg.Color("Beige"))
x=255
y=5
for index in range(8):
    pg.draw.rect(window,(0,x,0), (y,50,90,90),0,30)
    y += 100
    x -= 31.875
pygamebg.wait_loop()