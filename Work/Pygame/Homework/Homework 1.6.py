import pygame as pg
import pygamebg
(width,height) = (300,300)
window = pygamebg.open_window(width,height,"Bear")
window.fill((255, 255, 255))
pg.draw.circle(window,pg.Color("Yellow"),(100,80),50)
pg.draw.circle(window,pg.Color("Yellow"),(200,80),50)
pg.draw.circle(window,pg.Color("Black"),(100,80),55,5)
pg.draw.circle(window,pg.Color("Black"),(200,80),55,5)
pg.draw.circle(window,pg.Color("Yellow"),(150,150),100)
pg.draw.circle(window,pg.Color("Black"),(150,150),105,5)
pg.draw.circle(window,pg.Color("Black"),(110,120),25)
pg.draw.circle(window,pg.Color("Black"),(190,120),25)
pg.draw.circle(window,pg.Color("Black"),(150,200),48,4)
pg.draw.circle(window,pg.Color("Brown"),(150,200),45)
pg.draw.circle(window,pg.Color("Black"),(150,180),20)

pygamebg.wait_loop()
