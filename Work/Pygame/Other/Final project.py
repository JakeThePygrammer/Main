import pygame as pg, pygamebg, random

# Дефинирање на големината на прозорецот
(sirina, visina) = (500, 300)
prozor = pygamebg.open_window(sirina, visina, "Dino Game")

# Параметри за играчот
boja_igrac = (0, 255, 0)
igrac = pg.Rect(50, visina - 50, 30, 30)

# Параметри за препреките
boja_prepreka = (255, 0, 0)
prepreki = []
prepreka_sirina = 20
prepreka_visina = 40
brzina_prepreki = -5

# Физички параметри
brzina_y = 0
gravitacija = 1
skok_sila = -15

# Променливи за следење на избегнати препреки и победен услов
pominati = 0
win_threshold = 10  # Ако се избегнат 10 препреки, играчот победува


# Функција за додавање нова препрека
def dodadi_prepreka():
    x_pocetok = sirina + random.randint(50, 200)
    prepreki.append(pg.Rect(x_pocetok, visina - prepreka_visina, prepreka_sirina, prepreka_visina))


# Функција за цртање
def crtanje():
    prozor.fill((0, 0, 0))
    pg.draw.rect(prozor, boja_igrac, igrac)
    for prepreka in prepreki:
        pg.draw.rect(prozor, boja_prepreka, prepreka)
    # Прикажување на бројот на избегнати препреки
    font = pg.font.SysFont("Arial", 20)
    tekst = font.render("Избегнати: " + str(pominati), True, (255, 255, 255))
    prozor.blit(tekst, (10, 10))


# Функција за нов кадар
def nov_frejm():
    global brzina_y, pominati
    # Контрола со тастатурата (само за скок)
    pritisnato = pg.key.get_pressed()
    if pritisnato[pg.K_SPACE] and igrac.y + igrac.height >= visina:
        brzina_y = skok_sila

    # Ажурирање на позицијата на играчот
    brzina_y += gravitacija
    igrac.y += brzina_y

    # Ограничување на подот
    if igrac.y + igrac.height >= visina:
        igrac.y = visina - igrac.height
        brzina_y = 0

    # Движење на препреките
    for prepreka in prepreki:
        prepreka.x += brzina_prepreki

    # Отстранување на препреките што излегле од екран и зголемување на бројачот за избегнати препреки
    nova_lista = []
    for prepreka in prepreki:
        if prepreka.x + prepreka.width > 0:
            nova_lista.append(prepreka)
        else:
            pominati += 1
    prepreki[:] = nova_lista

    # Додавање нови препреки
    if not prepreki or prepreki[-1].x < sirina - random.randint(100, 200):
        dodadi_prepreka()

    # Проверка за судир со препрека
    for prepreka in prepreki:
        if igrac.colliderect(prepreka):
            print("Судир! Играта заврши. Губење.")
            exit()

    # Проверка за победа
    if pominati >= win_threshold:
        print("Победа! Ги избегнавте сите препреки.")
        exit()

    crtanje()


# Започнување на анимацијата
pygamebg.frame_loop(30, nov_frejm)