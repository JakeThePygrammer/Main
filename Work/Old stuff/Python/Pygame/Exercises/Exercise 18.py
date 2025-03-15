import pygame as pg
import pygamebg
flip = False

(width,height) = (1000,210)
window = pygamebg.open_window(width,height,"Fish")
window.fill(pg.Color("Cyan"))

fish = pg.image.load("../Images/fish.png")
a = 0
fishwidth = fish.get_width()


def new_frame():
    global fish, a, flip
    window.fill(pg.Color("Cyan"))
    window.blit(fish, (a, 50))

    if not flip:
        a += 5
        if a >= 1000 - fishwidth:
            fish = pg.transform.flip(fish, True, False)
            flip = True
    else:
        a -= 5
        if a <= 0:
            fish = pg.transform.flip(fish, True, False)
            flip = False


pygamebg.frame_loop(10,new_frame)
