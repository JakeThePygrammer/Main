
import pygame as pg
import pygamebg

(sirina, visina) = (600, 600)
prozor = pygamebg.open_window(sirina, visina, "Happy New Year!")


ognomet = pg.image.load("../Images/ognomet.jpg")
elka = pg.image.load("../Images/elka.jpg")
podarok = pg.image.load("../Images/podarok.jpg")


ognomet = pg.transform.scale(ognomet, (200, 200))
elka = pg.transform.scale(elka, (350, 350))
podarok = pg.transform.scale(podarok, (80, 80))


prozor.fill(pg.Color("white"))

prozor.blit(ognomet, (50, 10))
prozor.blit(ognomet, (250, 10))
prozor.blit(elka, (50, 190))
prozor.blit(podarok, (400, 250))
prozor.blit(podarok, (500, 350))
prozor.blit(podarok, (380, 450))


font = pg.font.SysFont("Comic Sans MS", 50)
tekst = font.render("Happy New Year!", True, pg.Color("magenta"))
tekst_x = (sirina - tekst.get_width()) // 2
tekst_y = (visina - tekst.get_height()) // 4
prozor.blit(tekst, (tekst_x, tekst_y))


pygamebg.wait_loop()