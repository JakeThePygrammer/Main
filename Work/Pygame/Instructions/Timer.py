import pygame as pg

# Inicijalizacija na pygame
pg.init()

# Postavuvanje na prozorecot
sirina, visina = 400, 200
prozor = pg.display.set_mode((sirina, visina))
pg.display.set_caption("Штоперица")

# Font za prikaz na tekst
font = pg.font.SysFont("Arial", 40)

# Početni vrednosti
vreme = 0  # Vreme vo sekundi
tajmer_aktiven = False  # Dali tajmerot e aktiviran?

# Tajmer koj se aktivira na sekoja sekunda
TIMER_EVENT = pg.USEREVENT + 1
pg.time.set_timer(TIMER_EVENT, 1000)


# Funkcija za crtanje
def crtaj():
    prozor.fill(pg.Color("white"))
    tekst = font.render(f"Време: {vreme} секунди", True, pg.Color("black"))
    prozor.blit(tekst, (50, 80))
    pg.display.flip()  # Osvežuvanje na ekranot


# Funkcija za obrabotka na nastani
def obraboti_nastan(nastan):
    global vreme, tajmer_aktiven

    if nastan.type == pg.QUIT:
        return False
    elif nastan.type == pg.KEYDOWN:
        if nastan.key == pg.K_s:  # Start
            tajmer_aktiven = True
        elif nastan.key == pg.K_p:  # Pauza
            tajmer_aktiven = False
        elif nastan.key == pg.K_r:  # Reset
            vreme = 0
            tajmer_aktiven = False
    elif nastan.type == TIMER_EVENT and tajmer_aktiven:
        vreme += 1
    return True


# Osnoven kod
running = True
while running:
    for event in pg.event.get():
        running = obraboti_nastan(event)

    crtaj()

pg.quit()
