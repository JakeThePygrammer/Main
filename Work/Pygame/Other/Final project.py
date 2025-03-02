import pygame as pg, pygamebg, random
import tkinter as tk
import math

shoporgame = input("Внеси што сакаш да правиш :\n1 - игра \n2 - продавница\n: ")
def screenres():
    root = tk.Tk()
    (sirina, visina) = (root.winfo_screenwidth(),root.winfo_screenheight())
    root.destroy()
    return sirina, visina

sirina, visina = screenres()
try:
    f = open("CoinsStore.txt", "x")
except FileExistsError:
    pass
else:
    f = open("CoinsStore.txt", "w")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.close()

if shoporgame == "1":
    print("Добродојде!")
    prozor = pygamebg.open_window(sirina, visina, "Dino Game")

    boja_igrac = (0, 255, 0)
    igrac = pg.Rect(math.floor(sirina / 30), math.floor(sirina / 30), math.floor(sirina / 30), math.floor(sirina / 30))

    boja_prepreka = (255, 0, 0)
    prepreki = []
    prepreka_sirina = math.floor(sirina / 30)
    prepreka_visina = 100
    brzina_prepreki = -5

    brzina_y = 0
    skok_sila = -15

    points = 0
    coins = 0
    win_threshold = 4
    level_threshold = 2
    levels = 1
    gamestart = False

    def start(event):
        global gamestart
        if event.type == pg.MOUSEBUTTONDOWN:
            gamestart = True


    def dodadi_prepreka():
        global prepreka_visina
        x_pocetok = sirina + random.randint(50, 200)
        prepreka_visina = random.randint(math.floor(visina / 4.5), math.floor(visina / 2))
        prepreka_visina1 = random.randint(math.floor(visina / 3), math.floor(visina / 2))
        rand_choice = random.randint(1, 2)
        if rand_choice == 1:
            prepreki.append(pg.Rect(x_pocetok, visina - prepreka_visina1, prepreka_sirina, prepreka_visina1))
            prepreki.append(pg.Rect(x_pocetok, 0, prepreka_sirina, prepreka_visina))
        elif rand_choice == 2:
            prepreki.append(pg.Rect(x_pocetok, visina - prepreka_visina, prepreka_sirina, prepreka_visina))
            prepreki.append(pg.Rect(x_pocetok, 0, prepreka_sirina, prepreka_visina1))


    def crtanje():
        prozor.fill((0, 0, 0))
        pg.draw.rect(prozor, boja_igrac, igrac)
        for prepreka in prepreki:
            pg.draw.rect(prozor, boja_prepreka, prepreka)
        f = open("CoinsStore.txt", "r")
        lines1 = f.readlines()
        value = int(lines1[1]) + int(levels)
        value2 = float(lines1[2]) + float(points)
        size = sirina / 25
        sized = math.floor(size)
        font = pg.font.SysFont("Arial", sized)
        tekst = font.render("Пројдени: " + str(value2), True, (255, 255, 255))
        prozor.blit(tekst, (10, 10))
        tekst2 = font.render("Левел: " + str(value), True, (255, 255, 255))
        prozor.blit(tekst2, (10, size + 10))

    stuck = False
    f = open("CoinsStore.txt", "r")

    def nov_frejm():
        global brzina_y, points, stuck, coins, level_threshold, lines, f, levels, value
        pritisnato = pg.key.get_pressed()
        if pritisnato[pg.K_DOWN]:
            brzina_y += 1
        if pritisnato[pg.K_UP] and stuck == False:
            brzina_y -= 1
        if not pritisnato[pg.K_DOWN]:
            brzina_y += 0.3

        igrac.y += brzina_y

        if igrac.y + igrac.height >= visina:
            igrac.y = visina - igrac.height
            brzina_y = 0
        if igrac.y <= 0:
            brzina_y = 0
            stuck = True
        if igrac.y >= 0:
            stuck = False

        for prepreka in prepreki:
            prepreka.x += brzina_prepreki

        nova_lista = []
        for prepreka in prepreki:
            if prepreka.x + prepreka.width > 0:
                nova_lista.append(prepreka)
            else:
                points += 0.5
        prepreki[:] = nova_lista

        if not prepreki or prepreki[-1].x < sirina - random.randint(100, 200):
            dodadi_prepreka()

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
                f.write(f"{str(currenthighscore)}\n")
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
                f.write(f"{str(currenthighscore)}\n")
                print(f"Бројот на најмногу поминати препреки е {currenthighscore}, ти не го достигна.")
            f.close()
            exit()

        crtanje()

    pygamebg.frame_loop(30, nov_frejm)

if shoporgame == "2":
    exit()