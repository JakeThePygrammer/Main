import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)
prozor = pygamebg.open_window(sirina, visina, "Пеперутка што  го следи покажувачот")

broj_frejmovi = 0
butterfly = pg.image.load("../Images/Butterfly.png")
slika = butterfly

def crtaj():
    global butterfly, slika
    prozor.fill(pg.Color("white"))
    (mouse_x, mouse_y) = pg.mouse.get_pos()
    slika_sirina = slika.get_width()
    slika_visina = slika.get_height()
    x = mouse_x - slika_sirina // 2
    y = mouse_y - slika_visina // 2
    prozor.blit(slika, (x, y))

def nov_frejm():
    global broj_frejmovi
    broj_frejmovi += 1
    crtaj()

pygamebg.frame_loop(50, nov_frejm)

