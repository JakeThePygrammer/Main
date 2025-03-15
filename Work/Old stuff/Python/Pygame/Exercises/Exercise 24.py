import pygame
import pygamebg
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Движечки круг и квадрат")

WHITE = (255, 255, 255)
RED = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
BLUE = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

circle_x, circle_y = 400, 300
circle_radius = 30
circle_speed = 5

square_x, square_y = 200, 200
square_size = 60
square_speed = 5

def newframe():
    global circle_x, circle_y, square_x, square_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    if keys[pygame.K_a]:
        square_x -= square_speed
    if keys[pygame.K_d]:
        square_x += square_speed
    if keys[pygame.K_w]:
        square_y -= square_speed
    if keys[pygame.K_s]:
        square_y += square_speed

    circle_x = max(circle_radius, min(width - circle_radius, circle_x))
    circle_y = max(circle_radius, min(height - circle_radius, circle_y))
    square_x = max(0, min(width - square_size, square_x))
    square_y = max(0, min(height - square_size, square_y))

def draw():
    newframe()
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(circle_x), int(circle_y)), circle_radius)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))

pygamebg.frame_loop(60, draw)
