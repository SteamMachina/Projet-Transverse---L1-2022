import pygame
from pygame.time import Clock
from animations import *
import settings as settings
import time
from game import Game

clock = Clock()

# Allow us to know at which walking frame the player is
stepIndex = 0
last_side_that_the_user_went = "right"
game = Game()



def Add_text_to_screen(msg, color, x, y, size,surface):
    font = settings.small_font
    if size == "small":
        font = settings.small_font
    elif size == "medium":
        font = settings.medium_font
    elif size == "big":
        font = settings.big_font

    text = font.render(msg, True, color)
    surface.blit(text, (x, y))


def pause_function(paused,surface):
    while paused:
        for event in pygame.event.get():
            # event is closing of window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        surface.fill(settings.white)
        Add_text_to_screen("Paused", settings.black, 400, 200, "big")
        Add_text_to_screen("Press C to continue or Q to quit.", settings.blue, 200, 400, "medium")
        pygame.display.update()
        clock.tick(5)
    return paused

