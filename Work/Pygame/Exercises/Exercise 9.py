import pygame as pg
import pygamebg
(width,height) = (200,600)
window = pygamebg.open_window(width,height,"Circles")
window.fill(pg.Color("White"))
radius = 10
distance = 2*radius+10
colors = [pg.Color("Red"),pg.Color("Orange"),pg.Color("Yellow"),pg.Color("Lime"),pg.Color("Green"),pg.Color("Blue"),pg.Color("Indigo"),pg.Color("Violet"),pg.Color("Brown"),pg.Color("Black"),pg.Color("Red"),pg.Color("Orange"),pg.Color("Yellow"),pg.Color("Lime"),pg.Color("Green"),pg.Color("Blue"),pg.Color("Indigo"),pg.Color("Violet"),pg.Color("Brown"),pg.Color("Black")]
for index in range(20):
    x = radius + index * distance

    pg.draw.circle(window, pg.Color(colors[index]), (100,x),radius)

pygamebg.wait_loop()