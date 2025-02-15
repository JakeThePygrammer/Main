import random
import pygame as pg
pg.init()
width, height = 400, 400
window = pg.display.set_mode((width, height))
pg.display.set_caption("Every half second color change")
time = 0
timer_paused = False
current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
TIMER_EVENT = pg.USEREVENT + 1
pg.time.set_timer(TIMER_EVENT, 500)

def draw():
    window.fill(pg.Color("white"))
    pg.draw.circle(window, current_color, (200, 200), 100)
    pg.display.flip()

def handle_event(events):
    global time, timer_paused, current_color
    if events.type == pg.QUIT:
        return False
    elif events.type == TIMER_EVENT and not timer_paused:
        time += 1
        current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif events.type == pg.MOUSEBUTTONDOWN:
        if events.button == 3 and timer_paused:
            print("Timer continued")
            timer_paused = False
        if events.button == 1 and not timer_paused:
            print("Timer paused")
            timer_paused = True
    return True

running = True
while running:
    for event in pg.event.get():
        running = handle_event(event)
    draw()
pg.quit()
