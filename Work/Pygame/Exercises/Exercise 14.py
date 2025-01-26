import pygame as pg
import pygamebg
(sirina, visina) = (600, 600)
prozor = pygamebg.open_window(sirina, visina, "OOU Lazo Angelovski")
OOU = pg.image.load("../Images/OOU.jpg")
Book_image = pg.image.load("../Images/Book.jpg")
Background = pg.image.load("../Images/Background1.png")
School = pg.transform.scale(OOU, (600, 400))
Book = pg.transform.scale(Book_image, (80, 80))
Bookr = pg.transform.rotate(Book, 270)
Background = pg.transform.scale(Background,(600,600))
prozor.fill(pg.Color("White"))
prozor.blit(Background,(0,0))
prozor.blit(School, (0, 100))
prozor.blit(Book, (50, 520))
prozor.blit(Bookr, (265, 520))
prozor.blit(Book, (470, 520))
text = "OOU Lazo Angelovski"
font = pg.font.SysFont("Times New Roman", 60, True, False)
textadded = font.render(text, True, pg.Color("Black"))
wt, ht = textadded.get_width(), textadded.get_height()
x = (sirina - wt) // 2
y = 30
prozor.blit(textadded, (x,y))
pygamebg.wait_loop()

