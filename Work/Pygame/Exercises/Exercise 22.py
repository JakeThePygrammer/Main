import pygame as pg
import pygamebg

(width, height) = (400, 400)
window = pygamebg.open_window(width, height, "Color Changing Circle")

circle_radius = 20
circle_x = width // 2
circle_y = height // 2
circle_color = pg.Color('red')


def new_frame():
    global circle_color

    mouse_x, mouse_y = pg.mouse.get_pos()

    dx = mouse_x - circle_x
    dy = mouse_y - circle_y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance <= circle_radius:
        circle_color = pg.Color('yellow')
    elif mouse_y > circle_y:
        circle_color = pg.Color('blue')
    elif mouse_y < circle_y:
        circle_color = pg.Color('green')
    else:
        circle_color = pg.Color('red')

    window.fill(pg.Color('white'))
    pg.draw.circle(window, circle_color, (circle_x, circle_y), circle_radius)


pygamebg.frame_loop(30, new_frame)
