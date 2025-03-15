import pygame as pg
import random

# Иницијализација на pygame
pg.init()

# Поставување на прозорецот
sirina, visina = 700, 500
prozor = pg.display.set_mode((sirina, visina))
pg.display.set_caption("Ден - ноќ")

den = True  # дали е ден или ноќ

# Функција за цртање
def crtaj():
    if den:  # ако е ден
        prozor.fill(pg.Color("skyblue"))                           # сино небо
        pg.draw.circle(prozor, pg.Color("yellow"), (350, 100), 70)  # сонце
    else:    # ако е ноќ
        prozor.fill(pg.Color("black"))                            # црно небо
        broj_zvezda = 150                                         # ѕвезди
        for i in range(broj_zvezda):
            x = random.randint(0, sirina)
            y = random.randint(0, visina)
            pg.draw.circle(prozor, pg.Color("white"), (x, y), 2)  # мали ѕвезди
    pg.display.flip()  # Освежување на екранот

# Функција за обработка на настани
def obraboti_nastan(nastan):
    global den
    if nastan.type == pg.MOUSEBUTTONDOWN: # ако е притиснато копчето на глувчето
        if nastan.button == 1:
            print("Kliknato e levoto kopche")
            den = not den  # ако било ден, сега ќе биде ноќ и обратно
            crtaj()  # веднаш повторно цртај
            return True
    return False

# ⚡ ПОЧЕТНО ЦРТАЊЕ за да не биде празен екран
crtaj()

# Главен циклус за обработка на настани
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        obraboti_nastan(event)  # Веќе вклучува crtaj()

pg.quit()
