import random

import pygame as pg, pygamebg


sirina, visina = 400, 400
prozor = pygamebg.open_window(sirina, visina, "Зголемување и намалување на квадрат со клик")

kvadrat_golemina = 200
kvadrat_crvena_boja = 0
kvadrat_sina_boja = 0
kvadrat_zelena_boja = 0
def nov_frejm():
    global kvadrat_golemina,kvadrat_sina_boja, kvadrat_crvena_boja, kvadrat_zelena_boja


    pritisnat_taster = pg.mouse.get_pressed()
    xm, ym = pg.mouse.get_pos()

    kvadrat_x = (sirina - kvadrat_golemina) // 2
    kvadrat_y = (visina - kvadrat_golemina) // 2

    if kvadrat_x < xm < kvadrat_x + kvadrat_golemina and kvadrat_y < ym < kvadrat_y + kvadrat_golemina:
        if pritisnat_taster[2]:
            kvadrat_crvena_boja = random.randint(0,255)
            kvadrat_zelena_boja = 0
            kvadrat_sina_boja = 0
        elif pritisnat_taster[1]:
            kvadrat_crvena_boja = 0
            kvadrat_zelena_boja = random.randint(0, 255)
            kvadrat_sina_boja = 0
        elif pritisnat_taster[0]:
            kvadrat_crvena_boja = 0
            kvadrat_zelena_boja = 0
            kvadrat_sina_boja = random.randint(0, 255)
    prozor.fill(pg.Color("white"))
    pg.draw.rect(prozor, (kvadrat_crvena_boja, kvadrat_zelena_boja, kvadrat_sina_boja), (kvadrat_x, kvadrat_y, kvadrat_golemina, kvadrat_golemina))

pygamebg.frame_loop(50, nov_frejm)