import random, math
import pygame as pg
import pygamebg

(sirina, visina) = (500, 500)
prozor = pygamebg.open_window(sirina, visina, "Топче што го следи покажувачот")

# растојание меѓу две точки (зададени со парови координати)
def rastojanie(A, B):
    (xa, ya) = A
    (xb, yb) = B
    return math.sqrt((xb - xa)**2 + (yb - ya)**2)

(x, y) = (sirina // 2, visina // 2)  # позиција на топче- иницијално во центарот на прозорецот

def crtaj():
    prozor.fill(pg.Color("white"))
    pg.draw.circle(prozor, pg.Color((random.randint(0,255),random.randint(0,255),random.randint(0,255))), (x, y), 20)

def nov_frejm():
    global x, y
    (xm, ym) = pg.mouse.get_pos()  # координати на покажувачот
    d = rastojanie((x, y), (xm, ym))  # растојание меѓу топчето до покажувачот
    v = 15 # брзина на движење на топчето
    if d < v:  # ако топчето е доволно блиску до покажувачот
        (x, y) = (xm, ym)  # се поместува точно на позицијата на глувчето
    else:  # во спротивно
        x = x + v * (xm - x) / d  # се поместува малку во насока кон покажувачот
        y = y + v * (ym - y) / d  # се поместува и во y-насока кон покажувачот
    crtaj()

pygamebg.frame_loop(50, nov_frejm)