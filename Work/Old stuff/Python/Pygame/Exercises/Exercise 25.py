import pygame as pg
import random

pg.init()

width, height = 700, 500
window = pg.display.set_mode((width, height))
pg.display.set_caption("Ден - ноќ")

nature = True
city = False
def draw():
    if nature:
        window.fill(pg.Color("skyblue"))
        pg.draw.circle(window, pg.Color("yellow"), (350, 100), 70)
        for index in range(75,631,100):
            pg.draw.rect(window,(pg.Color("Brown")),(index,350,50,100))
            pg.draw.rect(window,(pg.Color("Green")), (index - 20, 300,90, 50))
    if city:
        window.fill(pg.Color("Gray"))
        for index in range(75, 631, 75):
            pg.draw.rect(window, (pg.Color("Black")), (index, 350, 50, 100))
            pg.draw.rect(window, (pg.Color("Black")), (index - 50, 350 - 50, 50, 100))
            pg.draw.rect(window, (pg.Color("Brown")), (index, 350-100, 50, 100))
            pg.draw.rect(window, (pg.Color("Brown")), (index-50, 350- 150, 50, 100))
    pg.display.flip()

def workevent(events):
    global nature,city
    if events.type == pg.MOUSEBUTTONDOWN:
        if events.button == 1:
            nature = True
            city = False
            draw()
            return True
        if events.button == 3:
            nature = False
            city = True
            draw()
            return True
    return False

draw()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        workevent(event)

pg.quit()
