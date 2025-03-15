import pygame as pg
import pygamebg
(width,height) = (600,100)
window = pygamebg.open_window(width,height,"Circles")
window.fill(pg.Color("White"))
radius = 30
distance = 2*radius
colors = [pg.Color("Red"),pg.Color("Orange"),pg.Color("Yellow"),pg.Color("Lime"),pg.Color("Green"),pg.Color("Blue"),pg.Color("Indigo"),pg.Color("Violet"),pg.Color("Brown"),pg.Color("Black")]
for index in range(10):
    x = radius + index * distance

    pg.draw.circle(window, pg.Color(colors[index]), (x,50),radius)

pygamebg.wait_loop()