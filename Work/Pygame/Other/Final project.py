import pygame as pg, pygamebg, random

try:
    f = open("CoinsStore.txt", "x")
except FileExistsError:
    pass
else:
    f = open("CoinsStore.txt", "a")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.close()

# Дефинирање на големината на прозорецот
(sirina, visina) = (500, 300)
prozor = pygamebg.open_window(sirina, visina, "Dino Game")

# Параметри за играчот
boja_igrac = (0, 255, 0)
igrac = pg.Rect(50, visina - 50, 30, 30)

# Параметри за препреките
boja_prepreka = (255, 0, 0)
prepreki = []
prepreka_sirina = 30
prepreka_visina = 100
brzina_prepreki = -5

# Физички параметри
brzina_y = 0
skok_sila = -15

# Променливи за следење на избегнати препреки и победен услов
points = 0
coins = 0
win_threshold = 4  # Ако се избегнат 10 препреки, играчот победува
level_threshold = 2
levels = 1
gamestart = False
def start(event):
    global gamestart
    if event.type == pg.MOUSEBUTTONDOWN:
        gamestart = True

# Функција за додавање нова препрека
def dodadi_prepreka():
    global prepreka_visina
    prepreka_visina = random.randint(65,150)
    x_pocetok = sirina + random.randint(50, 200)
    prepreki.append(pg.Rect(x_pocetok, visina - prepreka_visina, prepreka_sirina, prepreka_visina))
    prepreki.append(pg.Rect(x_pocetok, 0, prepreka_sirina, random.randint(70,120)))

# Функција за цртање
def crtanje():
    prozor.fill((0, 0, 0))
    pg.draw.rect(prozor, boja_igrac, igrac)
    for prepreka in prepreki:
        pg.draw.rect(prozor, boja_prepreka, prepreka)
    # Прикажување на бројот на избегнати препреки
    f = open("CoinsStore.txt", "r")
    lines1 = f.readlines()
    value = int(lines1[1]) + int(levels)
    value2 = float(lines1[2]) + float(points)
    font = pg.font.SysFont("Arial", 20)
    tekst = font.render("Пројдени: " + str(value2), True, (255, 255, 255))
    prozor.blit(tekst, (10, 10))
    tekst2 = font.render("Левел: " + str(value), True, (255, 255, 255))
    prozor.blit(tekst2, (10, 30))


stuck = False
f = open("CoinsStore.txt", "r")
# Функција за нов кадар
def nov_frejm():
    global brzina_y, points, stuck, coins, level_threshold, lines, f, levels, value
    # Контрола со тастатурата (само за скок)
    pritisnato = pg.key.get_pressed()
    if pritisnato[pg.K_DOWN]:
        brzina_y += 1
    if pritisnato[pg.K_UP] and stuck == False:
        brzina_y -= 1
    if not pritisnato[pg.K_DOWN]:
        brzina_y += 0.3


    # Ажурирање на позицијата на играчот
    igrac.y += brzina_y

    # Ограничување на подот
    if igrac.y + igrac.height >= visina:
        igrac.y = visina - igrac.height
        brzina_y = 0
    if igrac.y <= 0:
        brzina_y = 0
        stuck = True
    if igrac.y >= 0:
        stuck = False



    # Движење на препреките
    for prepreka in prepreki:
        prepreka.x += brzina_prepreki

    # Отстранување на препреките што излегле од екран и зголемување на бројачот за избегнати препреки
    nova_lista = []
    for prepreka in prepreki:
        if prepreka.x + prepreka.width > 0:
            nova_lista.append(prepreka)
        else:
            points += 0.5
    prepreki[:] = nova_lista

    # Додавање нови препреки
    if not prepreki or prepreki[-1].x < sirina - random.randint(100, 200):
        dodadi_prepreka()

    # Проверка за судир со препрека
    for prepreka in prepreki:
        if igrac.colliderect(prepreka):
            print("Судир! Играта заврши. Губење.")
            exit()
    f = open("CoinsStore.txt", "r")
    lines2 = f.readlines()
    value3 = float(lines2[2]) + float(points)
    if value3 >= win_threshold:
        print("Победа! Ги избегнавте сите препреки. Оди во вториот свет при отварање.")
        coins += 100
        f.seek(0)
        lines = f.readlines()
        coins += int(lines[0])
        currenthighscore = float(lines[3])
        newhighscore = points + float(lines[2])
        f = open("CoinsStore.txt", "w")
        f.write(f"{str(coins)}\n")
        f.write(f"{str(0)}\n")
        f.write(f"{str(0)}\n")
        if newhighscore > currenthighscore:
            f.write(f"{str(newhighscore)}\n")
            print(f"Новиот број на најмогу поминати препреки е {newhighscore}!")
        else:
            print(f"Бројот на најмногу поминати препреки е {currenthighscore}, ти не го достигна.")
        f.close()
        exit()
    if points >= level_threshold:
        f = open("CoinsStore.txt", "r")
        lines1 = f.readlines()
        value = int(lines1[1]) + int(levels)
        f.close()
        print(f"Го поминавте левел {value}, отвори пак за следен левел. Доби 10 парички.")
        f = open("CoinsStore.txt", "r")
        coins += 10
        levels += 1
        lines = f.readlines()
        coins += int(lines[0])
        levels += int(lines[1])
        points += float(lines[2])
        currenthighscore = float(lines[3])
        newhighscore = points + float(lines[2])
        level_threshold += 1
        f.close()
        f = open("CoinsStore.txt", "w")
        f.write(f"{str(coins)}\n")
        f.write(f"{str(levels-1)}\n")
        f.write(f"{str(points)}\n")
        if newhighscore > currenthighscore:
            f.write(f"{str(newhighscore)}\n")
            print(f"Новиот број на најмогу поминати препреки е {newhighscore}!")
        else:
            print(f"Бројот на најмногу поминати препреки е {currenthighscore}, ти не го достигна.")
        f.close()
        exit()


    crtanje()


# Започнување на анимацијата
pygamebg.frame_loop(30, nov_frejm)