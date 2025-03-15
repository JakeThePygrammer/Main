import pygame as pg
import pygamebg

(width, height) = (400, 400)
window = pygamebg.open_window(width, height, "Топче што бега")

ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_color = pg.Color('red')

def new_frame():
    global ball_x, ball_y
    mouse_x, mouse_y = pg.mouse.get_pos()
    dx = ball_x - mouse_x
    dy = ball_y - mouse_y
    ball_x += dx // 10
    ball_y += dy // 10
    if ball_x < ball_radius:
        ball_x = ball_radius
    elif ball_x > width - ball_radius:
        ball_x = width - ball_radius
    if ball_y < ball_radius:
        ball_y = ball_radius
    elif ball_y > height - ball_radius:
        ball_y = height - ball_radius
    window.fill(pg.Color('white'))
    pg.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)

pygamebg.frame_loop(30, new_frame)
