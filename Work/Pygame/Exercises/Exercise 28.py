import pygame as pg
import time

# Иницијализација на Pygame
pg.init()

# Поставување на екран
SIRINA, VISINA = 800, 600
ekran = pg.display.set_mode((SIRINA, VISINA))
pg.display.set_caption("Контрола на  квадрат")

# Почетна позиција, големина и боја на квадратот
kvadrat = pg.Rect(375, 275, 50, 50)
boja = (0, 0, 255)  # Почетна боја: сина

# Брзина на движење
brzina = 2
skok_sila = 15
skoka = False

# Време на последна промена на боја
posledna_promena = time.time()
square_x, square_y = 200, 200
square_size = 60
# Главна програма
running = True
while running:
    ekran.fill((255, 255, 255))  # Позадина

    for nastan in pg.event.get():
        if nastan.type == pg.QUIT:
            running = False

        elif nastan.type == pg.KEYDOWN:
            if nastan.key == pg.K_ESCAPE:
                running = False

    # Движење со WASD
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        square_x -= brzina
    if keys[pg.K_d]:
        square_x += brzina
    if keys[pg.K_w]:
        square_y -= brzina
    if keys[pg.K_s]:
        square_y += brzina
    if keys[pg.K_PLUS] or keys[pg.K_EQUALS]:
        square_size += 10
    if keys[pg.K_MINUS] or keys[pg.K_UNDERSCORE]:
        square_size -= 10
    square_x = max(0, min(SIRINA - square_size, square_x))
    square_y = max(0, min(VISINA - square_size, square_y))
    # Цртање на квадратот
    pg.draw.rect(ekran,(pg.Color("Blue")), (square_x, square_y, square_size, square_size))
    pg.display.flip()
    pg.time.delay(5)

pg.quit()
