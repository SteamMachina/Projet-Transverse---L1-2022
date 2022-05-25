import pygame
from game import Game
import settings as set
# We import the mixer module of pygame which allows to have sounds
from pygame import mixer
import random
# We import the lists that contains the animations of the game
from animations import *
import time

'''INIT -------------------------------------------- '''
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()


screen = pygame.display.set_mode((set.screen_width, set.screen_height))
pygame.display.set_caption('Super Plush Rescue')

'''VARIABLES -------------------------------------------- '''

# Allow us to know at which walking frame the player is
stepIndex = 0
main_menu = True
rules_menu = False
credits_menu = False
running = True
difficulty_menu = False
level_difficulty = "Nothing"


'''SOUNDS -------------------------------------------- '''

'''We load the sounds in the game'''
# game_over_fx = pygame.mixer.Sound('')
# game_over_fx.set_volume(0.5)
pygame.mixer.music.load('assets/Music/Game_menu_music.mp3')
# 5000 : nbr of ms per delay
pygame.mixer.music.play(-1, 0.0, 5000)

'''CLASSES -------------------------------------------- '''

'''A class for the buttons of the game in the starter menu'''


class Button():
    # We put an image so that we can change the purpose of buttons at once and not re-create function per buttons
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_the_button_pressed = False

    def draw(self):

        # We define a variable which will tell us if the user pressed the button

        has_user_clicked = False

        # we get the mouse position
        pos = pygame.mouse.get_pos()
        # Since rect acts like a rectangle, we can use a collision function to see if clicked

        # First we confirm that the mouse is on the button
        if self.rect.collidepoint(pos):
            # Now we checked if the mouse clicked, [0] means the left mouse button
            if pygame.mouse.get_pressed()[0] == 1 and self.is_the_button_pressed == False:
                has_user_clicked = True
                self.is_the_button_pressed = True

        if pygame.mouse.get_pressed()[0] == 1:
            self.is_the_button_pressed = False

        screen.blit(self.image, self.rect)

        return has_user_clicked


'''BUTTONS --------------------------------------------
'WE THEN CREATE THOSE BUTTONS WITH OUR PREVIOUS CLASS'''

start_button = Button(400, 278, set.start_image_button)
rules_button = Button(400, 378, set.rules_image_button)
credits_button = Button(400, 478, set.credits_image_button)
exit_button = Button(400, 578, set.exit_image_button)
return_button = Button(778, 600, set.return_back_button)

hard_game_difficulty_button = Button(650, 278, set.hard_difficulty_button)
easy_game_difficulty_button = Button(50, 278, set.easy_difficulty_button)

'''FUNCTIONS -------------------------------------------- '''

def Add_text_to_screen(text,color):
    screen_text = set.font.render(text,True,color)
    screen.blit(screen_text,[set.screen_width/2, set.screen_height/2])

def pause_function():
    paused = True
    while paused:
        for event in pygame.event.get():
            # event is closing of window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill(set.white)
        # -100 pixels up
        Add_text_to_screen("Paused",set.black,-100,size="large")
        Add_text_to_screen("Press P to continue or Q to quit.",black,25)
        pygame.display.updaate()
        clock.tick(5)
# Blit allows us to draw the png pictures onto the player's assigned position
def draw_game(difficulty, level_number):
    global stepIndex

    if difficulty == 'Hard':
        screen.blit(background_hard[level_number], (0, 0))
        pygame.mixer.music.load('assets/Music/Hard_Levels_Music.mp3')
    if difficulty == 'Easy':
        screen.blit(background_easy[level_number], (0, 0))

    # If the player already went through all 8 walking frames, we reset it to 0
    if stepIndex >= 16:
        stepIndex = 0
    # If player goes right, we go through the right list walking frames
    elif game.player.IsmovingRight:
        screen.blit(right[stepIndex], (game.player.rect.x, game.player.rect.y))
        stepIndex += 1
        time.sleep(0.01)
    # If player goes right, we go through the left list walking frames
    elif game.player.IsmovingLeft:
        screen.blit(left[stepIndex], (game.player.rect.x, game.player.rect.y))
        stepIndex += 1
        time.sleep(0.01)
    # If the player neither goes left or right, we just apply the stationary frame to it
    else:
        screen.blit(game.player.image, (game.player.rect.x, game.player.rect.y))


# load our game
game = Game()

while running:
    screen.blit(set.side_left_bg_starter_menu, (0, 0))
    # We will load the button and main menu thingy when main menu is true, else we load the game
    if main_menu:
        # We apply the background image of the starter menu
        screen.blit(set.side_right_bg_starter_menu, (500, 0))
        screen.blit(set.game_logo, (340, 50))

        if start_button.draw():
            difficulty_menu = True

        if rules_button.draw():
            rules_menu = True
            main_menu = True

        if credits_button.draw():
            credits_menu = True
            main_menu = True

        if exit_button.draw():
            running = False

    if difficulty_menu:
        screen.blit(set.side_left_bg_starter_menu, (0, 0))
        screen.blit(set.side_right_bg_starter_menu, (500, 0))
        return_button.draw()
        if hard_game_difficulty_button.draw():
            level_difficulty = "Hard"
            level_choice_number = random.randint(0, 2)
            main_menu = False
        if easy_game_difficulty_button.draw():
            level_choice_number = random.randint(0, 2)
            level_difficulty = 'Easy'
            main_menu = False
        if return_button.draw():
            difficulty_menu = False
            main_menu = True

    if rules_menu:
        screen.blit(set.rules_menu_image, (0, 0))
        return_button.draw()
        if return_button.draw():
            rules_menu = False
            main_menu = True

    if credits_menu:
        screen.blit(set.rules_menu_image, (0, 0))
        return_button.draw()
        if return_button.draw():
            credits_menu = False
            main_menu = True

    if not main_menu:
        draw_game(level_difficulty, level_choice_number)
        # verify if the player wants to go left or right
        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <= set.screen_width:

            # Control the moment that if the player presses shift, he can run
            if game.pressed.get(pygame.K_LSHIFT):
                game.player.move_right(game.player.velocity_fast)
            else:
                game.player.move_right(game.player.velocity)
            game.player.IsmovingRight = True
            game.player.IsmovingLeft = False

        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:

            # Control the moment that if the player presses shift, he can run
            if game.pressed.get(pygame.K_LSHIFT):
                game.player.move_left(game.player.velocity_fast)
            else:
                game.player.move_left(game.player.velocity)

            game.player.IsmovingRight = False
            game.player.IsmovingLeft = True

        elif (game.pressed.get(pygame.K_RIGHT)) and (game.player.rect.x > set.screen_width):
            game.player.init_next()
            game.player.IsmovingRight = True
            game.player.IsmovingLeft = False
        else:
            game.player.IsmovingRight = False
            game.player.IsmovingLeft = False
            stepIndex = 0
        # update our screen
    pygame.display.flip()

    for event in pygame.event.get():
        # event is closing of window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

pygame.quit()
