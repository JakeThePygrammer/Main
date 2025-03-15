import pygame as pg
import pygamebg

level = 0
text = "Tomb Adventure"
text2 = f"Level {level}"
text3 = "Quit"

(width,height) = (960,540)
window = pygamebg.open_window(width,height,"Game screen")
window.fill((0,0,0))

Background = pg.image.load("../Images/TombBackground.jpg")
Protagonist = pg.image.load("../Images/Protagonist.png")
Mummy = pg.image.load("../Images/Mummy.png")
Money = pg.image.load("../Images/Money.png")
PaperScroll = pg.image.load("../Images/PaperScroll.png")

font = pg.font.SysFont("Papyrus", 50, True, False)
textadded = font.render(text, True, pg.Color("Black"))
font = pg.font.SysFont("Papyrus", 50, False, False)
textadded2 = font.render(text2, True, pg.Color("Black"))
textadded3 = font.render(text3, True, pg.Color("Black"))

wt, ht = textadded.get_width(), textadded.get_height()
wt1, ht1 = textadded2.get_width(), textadded2.get_height()
wt2 = textadded2.get_width()

x = (width - wt) // 2
y = (height // 2) - 50
x1 = (width - wt1) // 2
y1 = (height // 2)
x2 = 435

Background = pg.transform.scale(Background, (960, 540))
Papyrus = pg.transform.rotate(PaperScroll, 270)
window.blit(Background, (0, 0))
Papyrus = pg.transform.scale(Papyrus, (460, 95))
window.blit(Papyrus, (x - 40, y-30))
Papyrus = pg.transform.scale(Papyrus, (300, 95))
window.blit(Papyrus, (350 , y1 - 10))
Papyrus = pg.transform.scale(Papyrus, (300, 95))
window.blit(Papyrus, (350 , y1 + 70))
Protagonist = pg.transform.scale(Protagonist, (250, 300))
window.blit(Protagonist, (600,250))
Mummy = pg.transform.scale(Mummy, (200, 250))
window.blit(Mummy, (50,300))
Coins = pg.transform.scale(Money, (100, 100))
window.blit(Coins, (300,440))

window.blit(textadded2, (435,y1 - 2))
window.blit(textadded, (x,y - 20))
window.blit(textadded3, (x2 ,y1 + 75))
pygamebg.wait_loop()