import pygame as pg
import pygamebg
text = "Jakov"
text2 = "Nestorovski"
(width,height) = (500,500)
window = pygamebg.open_window(width,height,"Name and surname")
window.fill((0,0,0))
font = pg.font.SysFont("Times New Roman", 50, True, False)
textadded = font.render(text, True, pg.Color("Green"))
textadded2 = font.render(text2, True, pg.Color("Red"))
wt, ht = textadded.get_width(), textadded.get_height()
wt1, ht1 = textadded2.get_width(), textadded2.get_height()
x = (width - wt) // 2
y = (height // 2) - 50
x1 = (width - wt1) // 2
y1 = (height // 2)
window.blit(textadded, (x,y))
window.blit(textadded2, (x1,y1))
pygamebg.wait_loop()