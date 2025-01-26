text = input("Enter a message : ")
import pygame as pg
import pygamebg
(width,height) = (300,300)
window = pygamebg.open_window(width,height,"Text")
window.fill(pg.Color("Blue"))
font = pg.font.SysFont("Calibri", 30, True, True)
textadded = font.render(text, True, pg.Color("White"))
wt, ht = textadded.get_width(), textadded.get_height()
x = (width - wt) // 2
y = (height // 2)
window.blit(textadded, (x,y))
pygamebg.wait_loop()