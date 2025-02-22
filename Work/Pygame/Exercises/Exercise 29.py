import random
import pygame as pg
import pygamebg

# Иницијализација на Pygame
pg.init()

# Димензии на прозорецот
(sirina, visina) = (500, 300)
prozor = pygamebg.open_window(sirina, visina, "Игра-Собирање јаболки")

# Поставување на повторување на настани од тастатурата
pg.key.set_repeat(10, 10)

# Вчитување на слики
korpa = pg.image.load("../Images/korpa.png")
jabuka = pg.image.load("../Images/jabolko.png")
zivot = pg.image.load("../Images/img.png")
rasipanajabolka = pg.transform.scale(pg.image.load(("../Images/img_1.png")), (50, 50))

# Иницијализација на променливи
MAKS_JABOLKA = 5  # Максимален број на јаболка на екранот
jabolka = []  # Листа на јаболка на екранот
rasipanajabolkalista = []  # Листа на расипани јаболка на екранот
poeni = 0  # Број на поени
zivoti = 3  # Број на животи
(korpa_x, korpa_y) = (0, visina - korpa.get_height())  # Почетна позиција на корпата
igra_zavrsena = False

# Функција за додавање на ново расипано јаболко
def dodadi_rasipanojabolka():
    x = random.randint(0, sirina - rasipanajabolka.get_width())
    rasipanajabolkalista.append([x, 5])

# Функција за додавање на ново јаболко
def dodadi_jabolko():
    x = random.randint(0, sirina - jabuka.get_width())
    jabolka.append([x, 5])

# Функција за случајно додавање на јаболка и расипани јаболка
def dodadi_jabolka_i_rasipanajabolka():
    if len(jabolka) == 0 or (len(jabolka) < MAKS_JABOLKA - len(rasipanajabolkalista) and random.randint(1, 100) == 1):
        dodadi_jabolko()
    if len(rasipanajabolkalista) == 0 or (len(rasipanajabolkalista) < MAKS_JABOLKA - len(jabolka) and random.randint(1, 100) == 1):
        dodadi_rasipanojabolka()

# Функција за поместување на јаболката и расипаните јаболка надолу
def pomesti_jabolka_i_rasipanajabolka():
    for jabolko in jabolka:
        jabolko[1] += 2  # Зголемена брзина на паѓање
    for rasipano in rasipanajabolkalista:
        rasipano[1] += 2  # Зголемена брзина на паѓање

# Функција за собирање на јаболката и ажурирање на поени и животи
def soberi_jabolka_i_rasipanajabolka():
    global jabolka, rasipanajabolkalista, poeni, zivoti
    novi_jabolka = []
    novi_rasipanajabolka = []
    for [x, y] in jabolka:
        if (y > visina - korpa.get_height() and korpa_x <= x and x <= korpa_x + korpa.get_width()):
            poeni += 1
        elif y > visina:
            zivoti -= 1
        else:
            novi_jabolka.append([x, y])
    for [x, y] in rasipanajabolkalista:
        if (y > visina - korpa.get_height() and korpa_x <= x and x <= korpa_x + korpa.get_width()):
            poeni -= 1  # Одзема поен ако е собрана расипана јаболка
        else:
            novi_rasipanajabolka.append([x, y])
    jabolka = novi_jabolka
    rasipanajabolkalista = novi_rasipanajabolka

# Функција за прикажување на содржината на прозорецот
def crtaj():
    prozor.fill(pg.Color("white"))
    font = pg.font.SysFont("Arial", 20)
    tekst = font.render("Поени: " + str(poeni), True, pg.Color("black"))
    prozor.blit(tekst, (5, 5))
    for i in range(1, zivoti + 1):
        prozor.blit(zivot, (sirina - 5 - i * zivot.get_width(), 5))
    for [x, y] in jabolka:
        prozor.blit(jabuka, (x, y))
    for [x, y] in rasipanajabolkalista:
        prozor.blit(rasipanajabolka, (x, y))
    prozor.blit(korpa, (korpa_x, korpa_y))

# Функција за прикажување на пораката "Изгубивте"
def prikazi_poraka_izgubivte():
    prozor.fill(pg.Color("white"))
    font = pg.font.SysFont("Arial", 50)
    tekst = font.render("Изгубивте", True, pg.Color("red"))
    tekst_rect = tekst.get_rect(center=(sirina / 2, visina / 2))
    prozor.blit(tekst, tekst_rect)
    pg.display.flip()

# Функција за обработка на настани од тастатурата
def obraboti_nastan(nastan):
    global korpa_x
    if nastan.type == pg.KEYDOWN:
        if nastan.key == pg.K_LEFT or nastan.key == pg.K_a:
            korpa_x -= 10
        elif nastan.key == pg.K_RIGHT or nastan.key == pg.K_d:
            korpa_x += 10
        crtaj()

# Функција за ажурирање на состојбата на играта
def nov_frejm():
    global igra_zavrsena
    if not igra_zavrsena:
        dodadi_jabolka_i_rasipanajabolka()
        pomesti_jabolka_i_rasipanajabolka()
        soberi_jabolka_i_rasipanajabolka()
        if zivoti <= 0:
            igra_zavrsena = True
        crtaj()
    else:
        prikazi_poraka_izgubivte()

pygamebg.frame_loop(25, nov_frejm, obraboti_nastan)
