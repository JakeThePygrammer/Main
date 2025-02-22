import pygame as pg
import time

pg.init()
SIRINA, VISINA = 800, 600
ekran = pg.display.set_mode((SIRINA, VISINA))
pg.display.set_caption("Контрола на квадрат")

kvadrat = pg.Rect(375, 275, 50, 50)
boja = (0, 0, 255)

brzina = 2
skok_sila = 15
skoka = False

sizedown = pg.mixer.Sound("../Audio/mixkit-arrow-whoosh-1491.wav")
sizeup = pg.mixer.Sound("../Audio/mixkit-retro-game-notification-212.wav")

posledna_promena = time.time()
color_change_time = 0
square_x, square_y = 200, 200
square_size = 60
Color = "Blue"

running = True
while running:
    ekran.fill((255, 255, 255))

    for nastan in pg.event.get():
        if nastan.type == pg.QUIT:
            running = False
        elif nastan.type == pg.KEYDOWN:
            if nastan.key == pg.K_ESCAPE:
                running = False

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
        sizeup.play()
        Color = "Green"
        color_change_time = time.time()
    if keys[pg.K_MINUS] or keys[pg.K_UNDERSCORE]:
        square_size -= 10
        sizedown.play()
        Color = "Red"
        color_change_time = time.time()

    if time.time() - color_change_time > 3:
        Color = "Blue"

    square_x = max(0, min(SIRINA - square_size, square_x))
    square_y = max(0, min(VISINA - square_size, square_y))

    pg.draw.rect(ekran, pg.Color(Color), (square_x, square_y, square_size, square_size))
    pg.display.flip()
    pg.time.delay(5)

pg.quit()
