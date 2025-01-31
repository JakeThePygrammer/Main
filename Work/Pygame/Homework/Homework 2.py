import pygame as pg
import pygamebg
text = "Tomb Adventure"
text2 = "Start level"
(width,height) = (960,540)
window = pygamebg.open_window(width,height,"Name and surname")
window.fill((0,0,0))
Background = pg.image.load("../Images/TombBackground.jpg")
Protagonist = pg.image.load("../Images/Protagonist.png")
Mummy = pg.image.load("../Images/Mummy.png")
Money = pg.image.load("../Images/Money.png")
PaperScroll = pg.image.load("../Images/PaperScroll.png")
font = pg.font.SysFont("Papyrus", 50, True, False)
textadded = font.render(text, True, pg.Color("Black"))
font = pg.font.SysFont("Papyrus", 50, True, False)
textadded2 = font.render(text2, True, pg.Color("Black"))
wt, ht = textadded.get_width(), textadded.get_height()
wt1, ht1 = textadded2.get_width(), textadded2.get_height()
Background = pg.transform.scale(Background, (960, 540))
window.blit(Background, (0, 0))
x = (width - wt) // 2
y = (height // 2) - 50
x1 = (width - wt1) // 2
y1 = (height // 2)
window.blit(textadded, (x,y - 20))
window.blit(textadded2, (x1,y1))
pygamebg.wait_loop()