import pygame as pg, pygamebg
import random
import tkinter as tk
import math

pg.init()

shoporgame = input("Внеси што сакаш да правиш :\n1 - игра \n2 - продавница\n: ")
def screenres():
    root = tk.Tk()
    (sirina, visina) = (root.winfo_screenwidth(),root.winfo_screenheight())
    root.destroy()
    return sirina, visina
try:
    f = open("CoinsStore.txt", "x")
    f.close()
except FileExistsError:
    pass
else:
    f = open("CoinsStore.txt", "w")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.write(f"{str(0)}\n")
    f.write(f"{str("White")}\n")
    f.write(f"{str(6)}\n")
    f.write(f"{str(6)}\n")
    f.close()

f = open("CoinsStore.txt", "r")
lines = f.readlines()
boja_igrac = lines[4]
level_thresholds = lines[6]
sirina, visina = screenres()


if shoporgame == "1":
    print("Добродојде!")
    prozor = pygamebg.open_window(sirina, visina, "Jakov's game")
    igrac = pg.Rect(math.floor(sirina / 30), math.floor(sirina / 30), math.floor(sirina / 30), math.floor(sirina / 30))
    f.close()
    boja_prepreka = (255, 0, 0)
    prepreki = []
    prepreka_sirina = math.floor(sirina / 30)
    prepreka_visina = 100
    brzina_prepreki = -5

    brzina_y = 0
    skok_sila = -15

    points = 0
    coins = 0
    level_threshold = int(level_thresholds)
    levels = 1

    def dodadi_prepreka():
        global prepreka_visina
        x_pocetok = sirina + random.randint(50, 200)
        prepreka_visina = random.randint(math.floor(visina / 4.5 - 30), math.floor(visina / 2 - 30))
        prepreka_visina1 = random.randint(math.floor(visina / 3 - 30), math.floor(visina / 2 - 30))
        rand_choice = random.randint(1, 2)
        if rand_choice == 1:
            prepreki.append(pg.Rect(x_pocetok, visina - prepreka_visina1, prepreka_sirina, prepreka_visina1))
            prepreki.append(pg.Rect(x_pocetok, 0, prepreka_sirina, prepreka_visina))
        elif rand_choice == 2:
            prepreki.append(pg.Rect(x_pocetok, visina - prepreka_visina, prepreka_sirina, prepreka_visina))
            prepreki.append(pg.Rect(x_pocetok, 0, prepreka_sirina, prepreka_visina1))


    def crtanje():
        prozor.fill((0, 0, 0))
        try:
            player_color = pg.Color(str(boja_igrac.strip()))
        except ValueError:
            player_color = (255, 255, 255)
        pg.draw.rect(prozor, player_color, igrac)
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
        keys = pg.key.get_pressed()
        if keys[pg.K_e]:
            exit()
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
                print("Судир! Играта заврши.")
                exit()
        if points >= level_threshold:
            f = open("CoinsStore.txt", "r")
            lines1 = f.readlines()
            value = int(lines1[1]) + int(levels)
            f.close()
            print(f"Го поминавте левел {value}, отвори пак за следен левел. Добивте 10 парички.")
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
            f.write(f"{str(boja_igrac)}\n")
            f.write(f"{str(level_threshold)}\n")
            f.close()
            exit()

        crtanje()

    pygamebg.frame_loop(30, nov_frejm)

if shoporgame == "2":
    print("Добродојде!")
    colors = ["Red", "Blue", "Purple"]
    prozor = pygamebg.open_window(sirina, visina, "Jakov's shop")
    button_color = pg.Color("Red")
    button_color2 = pg.Color("Blue")
    button_color3 = pg.Color("Purple")
    button_rect = pg.Rect(math.floor(sirina / 8), math.floor(visina / 5), math.floor(sirina / 5),math.floor(visina / 8))
    button_rect2 = pg.Rect(math.floor(sirina / 2.5), math.floor(visina / 5), math.floor(sirina / 5),math.floor(visina / 8))
    button_rect3 = pg.Rect(math.floor(sirina / 1.4), math.floor(visina / 5), math.floor(sirina / 3.7),math.floor(visina / 8))
    font = pg.font.SysFont("Arial", 60)
    button_text = font.render("Црвена коцка", True, pg.Color("White"))
    button_text2 = font.render("Сина коцка", True, pg.Color("White"))
    button_text3 = font.render("Виолетова коцка", True, pg.Color("White"))



    def crtanje2():
        prozor.fill((0, 0, 0))
        pg.draw.rect(prozor, button_color, button_rect)
        pg.draw.rect(prozor, button_color2, button_rect2)
        pg.draw.rect(prozor, button_color3, button_rect3)
        text_width, text_height = button_text.get_size()
        text_x = button_rect.x + (button_rect.width - text_width) // 2
        text_y = button_rect.y + (button_rect.height - text_height) // 2
        prozor.blit(button_text, (text_x, text_y))
        text_width, text_height = button_text.get_size()
        text_x2 = button_rect2.x + (button_rect2.width - text_width) // 2
        text_y2 = button_rect2.y + (button_rect2.height - text_height) // 2
        prozor.blit(button_text, (text_x, text_y))
        text_width, text_height = button_text.get_size()
        text_x3 = button_rect3.x + (button_rect3.width - text_width) // 4
        text_y3 = button_rect3.y + (button_rect3.height - text_height) // 2
        prozor.blit(button_text, (text_x, text_y))
        prozor.blit(button_text2, (text_x2, text_y2))
        prozor.blit(button_text3, (text_x3, text_y3))
        size = sirina / 25
        sized = math.floor(size)
        font = pg.font.SysFont("Arial", sized)
        tekst = font.render("Цената е 10 пари за промена", True, pg.Color("White"))
        rect_x = (sirina - size) // 3
        rect_y = (visina - size) // 1.5

        prozor.blit(tekst, (rect_x, rect_y))

    def nov_frejm2():
        global i
        keys = pg.key.get_pressed()
        if keys[pg.K_e]:
            exit()
        press = False
        mouse_pos = pg.mouse.get_pos()
        crtanje2()
        if button_rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] and not press:
                press = True
                i = 0
            elif pg.mouse.get_pressed()[0] and press:
                press = False
        if button_rect2.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] and not press:
                press = True
                i = 1
            elif pg.mouse.get_pressed()[0] and press:
                press = False
        if button_rect3.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] and not press:
                press = True
                i = 2
            elif pg.mouse.get_pressed()[0] and press:
                press = False

        f = open("CoinsStore.txt", "r")
        lines = f.readlines()
        money = int(lines[0])

        size = sirina / 25
        sized = math.floor(size)
        font = pg.font.SysFont("Arial", sized)
        tekst = font.render("Пари: " + str(money), True, pg.Color("White"))
        prozor.blit(tekst, (10, 10))

        if money < 10 and press:
            text = font.render("Немаш доволно пари!", True, pg.Color("White"))
            text_width, text_height = text.get_size()
            text_x = sirina / 2 - text_width
            text_y = visina // 2 - text_height
            prozor.blit(text, (text_x, text_y))
        x = 10
        if money >= x and press:
            money -= x
            f = open("CoinsStore.txt", "r+")
            lines = f.readlines()
            if lines:
                lines[0] = f"{money}\n"
            else:
                lines.append(f"{money}\n")
            f.seek(0)
            f.writelines(lines)
            f.close()
            f = open("CoinsStore.txt", "r+")
            lines = f.readlines()
            if lines:
                lines[4] = f"{colors[i]}\n"
            else:
                lines.append(f"{colors[i]}\n")
            f.seek(0)
            f.writelines(lines)
            f.close()
            pg.time.delay(5)

    pygamebg.frame_loop(30, nov_frejm2)