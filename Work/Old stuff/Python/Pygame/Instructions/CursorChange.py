import pygame as pg
import pygamebg

(width, height) = (400, 400)
window = pygamebg.open_window(width, height, "Picture as Cursor")

mouse_image = (pg.image.load("../Images/ChekanGore.png"), pg.image.load("../Images/ChekanDole.png"))
i_image = 0

(mouse_x, mouse_y) = (width // 2, height // 2)
pg.mouse.set_pos((mouse_x, mouse_y))
pg.mouse.set_visible(False)

def draw():
    window.fill(pg.Color("skyblue"))

    image = mouse_image[i_image]
    image_width = image.get_width()
    image_height = image.get_height()

    top_left = (mouse_x - image_width // 2, mouse_y - image_height // 2)
    window.blit(image, top_left)

def handle_event(event):
    global mouse_x, mouse_y, i_image

    if event.type == pg.MOUSEBUTTONDOWN:
        i_image = 1
        return True
    elif event.type == pg.MOUSEBUTTONUP:
        i_image = 0
        return True
    elif event.type == pg.MOUSEMOTION:
        mouse_x, mouse_y = event.pos
        return True
    return False

pygamebg.event_loop(draw, handle_event)

