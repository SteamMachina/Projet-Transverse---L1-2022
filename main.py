import pygame
from game import Game
import settings as settings
# We import the mixer module of pygame which allows to have sounds
from pygame import mixer

from menu import Button
import random
# We import the lists that contains the animations of the game
from animations import *
import time


'''INIT -------------------------------------------- '''
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Super Plush Rescue')

import functions as functions

'''VARIABLES -------------------------------------------- '''
running = True
stepIndex = 0
last_side_that_the_user_went = "right"

'''SOUNDS -------------------------------------------- '''

'''We load the sounds in the game'''
# game_over_fx = pygame.mixer.Sound('')
# game_over_fx.set_volume(0.5)
pygame.mixer.music.load('assets/Music/Game_menu_music.mp3')
# 5000 : nbr of ms per delay
pygame.mixer.music.play(-1, 0.0, 5000)



# load our game
game = Game()
paused = False

# This is the part which allows us to handle the animations
def draw_game(difficulty, level_number,surface):
    global last_side_that_the_user_went
    global stepIndex

    if difficulty == 'Hard':
        surface.blit(background_hard[level_number], (0, 0))

    if difficulty == 'Easy':
        surface.blit(background_easy[level_number], (0, 0))

    # If the player already went through all 8 walking frames, we reset it to 0
    if stepIndex >= 16:
        stepIndex = 0

    # If player goes right, we go through the right list walking frames
    elif game.joueur.IsmovingRight:
        surface.blit(right[stepIndex], (game.joueur.yoke_rect.x, game.joueur.yoke_rect.y ))
        stepIndex += 1
        last_side_that_the_user_went = "right"
        time.sleep(0.01)

    # If player goes right, we go through the left list walking frames
    elif game.joueur.IsmovingLeft:
        surface.blit(left[stepIndex], (game.joueur.yoke_rect.x, game.joueur.yoke_rect.y ))
        stepIndex += 1
        last_side_that_the_user_went = "left"
        time.sleep(0.01)

    # If the player neither goes left or right, we just apply the stationary frame to it
    else:

        if last_side_that_the_user_went == "right":
            surface.blit(right_rest[stepIndex], (game.joueur.yoke_rect.x,game.joueur.yoke_rect.y ))
            stepIndex += 1
            time.sleep(0.08)
        else:
            surface.blit(right_rest[stepIndex], (game.joueur.yoke_rect.x, game.joueur.yoke_rect.y ))



def game_loop(main_menu):
    # verify if the player wants to go left or right
    if game.pressed.get(pygame.K_RIGHT) and game.joueur.yoke_rect.x <= settings.screen_width:

        game.joueur.move_right(game.joueur.yoke_velocity)
        game.joueur.IsmovingRight = True
        game.joueur.IsmovingLeft = False

    elif game.pressed.get(pygame.K_LEFT) and game.joueur.yoke_rect.x >= 0:
        game.joueur.move_left(game.joueur.yoke_velocity)
        game.joueur.IsmovingRight = False
        game.joueur.IsmovingLeft = True

    else:
        game.joueur.IsmovingRight = False
        game.joueur.IsmovingLeft = False
        stepIndex = 0

    return main_menu

while running:

    screen.blit(settings.side_left_bg_starter_menu, (0, 0))
    # We will load the button and main menu thingy when main menu is true, else we load the game
    if game.menu.main_menu:
        # We apply the background image of the starter menu
        screen.blit(settings.side_right_bg_starter_menu, (500, 0))
        screen.blit(settings.game_logo, (340, 50))

        if settings.start_button.draw(screen) and game.menu.credits_menu == False and game.menu.exit_menu == False and game.menu.rules_menu == False:
            game.menu.difficulty_menu = True
            game.menu.should_starter_menu_appear = False

        if settings.rules_button.draw(screen) and game.menu.should_starter_menu_appear == True and game.menu.credits_menu == False and game.menu.exit_menu == False:
            game.menu.rules_menu = True
            game.menu.main_menu = True

        if settings.credits_button.draw(screen) and game.menu.should_starter_menu_appear == True and game.menu.rules_menu == False and game.menu.exit_menu == False:
            game.menu.credits_menu = True
            game.menu.main_menu = True

        if settings.exit_button.draw(screen) and game.menu.should_starter_menu_appear == True and game.menu.credits_menu == False and game.menu.rules_menu == False:
            game.menu.exit_menu = True

    if game.menu.difficulty_menu:
        screen.blit(settings.side_left_bg_starter_menu, (0, 0))
        screen.blit(settings.side_right_bg_starter_menu, (500, 0))
        settings.return_button.draw(screen)
        if settings.hard_game_difficulty_button.draw(screen):
            game.menu.level_difficulty = "Hard"
            level_choice_number = random.randint(0, 2)
            game.menu.main_menu = False
        if settings.easy_game_difficulty_button.draw(screen):
            level_choice_number = random.randint(0, 2)
            game.menu.level_difficulty = 'Easy'
            game.menu.main_menu = False
        if settings.return_button.draw(screen):
            game.menu.difficulty_menu = False
            game.menu.main_menu = True
            game.menu.should_starter_menu_appear = True

    if game.menu.rules_menu:
        screen.blit(settings.rules_menu_image, (0, 0))
        settings.return_button.draw(screen)
        if settings.return_button.draw(screen):
            game.menu.rules_menu = False
            game.menu.main_menu = True
            game.menu.should_starter_menu_appear = True

    if game.menu.credits_menu:
        screen.blit(settings.rules_menu_image, (0, 0))
        settings.return_button.draw(screen)
        if settings.return_button.draw(screen):
            game.menu.credits_menu = False
            game.menu.main_menu = True
            game.menu.should_starter_menu_appear = True

    if game.menu.exit_menu:
        quit()

    if not game.menu.main_menu:
        pygame.mixer.music.stop()
        level_data = game.carte.load_tmx_data()
        delta_time = pygame.time.Clock().tick(60) * 0.001 * 60

        draw_game(game.menu.level_difficulty, level_choice_number,screen)
        game.menu.main_menu = game_loop(game.menu.main_menu)

        # update our screen
    pygame.display.flip()

    for event in pygame.event.get():
        # event is closing of window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if (
                event.key == pygame.K_p
                and game.menu.main_menu == False
                and not paused
            ):
                paused = True
                paused = functions.pause_function(paused)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

pygame.quit()