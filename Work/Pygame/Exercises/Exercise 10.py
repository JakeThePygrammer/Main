import pygame as pg
import pygamebg
pg.init()
(width, height) = (400, 400)
window = pygamebg.open_window(width, height, "Chessboard")
window.fill(pg.Color("White"))
white = pg.Color("White")
black = pg.Color("Black")
square_size = width // 8
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = white
        else:
            color = black
        pg.draw.rect(window, color, (col * square_size, row * square_size, square_size, square_size))
pygamebg.wait_loop()
