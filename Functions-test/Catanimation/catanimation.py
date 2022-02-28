import pygame, sys
from pygame.locals import *
import time

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((1000, 300))
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 0
caty = 150
direction = 'right'


def display_update():
    screen.fill(WHITE)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (1000, 200), 4)

running = True
while running: # the main game loop

    display_update()

    for event in pygame.event.get():  # event handling loop
        if event.type == KEYUP:
            if ((event.key in (K_RIGHT, K_d)) and (catx <= 1000)):
                display_update()
                catx += 100

            elif ((event.key in (K_LEFT, K_a)) and (catx != 0)):
                display_update()
                catx -= 100


    '''if direction == 'right':
        catx += 5
        if catx == 220:
            direction = 'left'

    elif direction == 'left':
        catx -= 5
        if catx == 20:
            direction = 'right'''


    screen.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        # event is closing of window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.update()
    fpsClock.tick(FPS)