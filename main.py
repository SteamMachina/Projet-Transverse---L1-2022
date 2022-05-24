import pygame
from game import Game
import settings as set
# We import the mixer module of pygame which allows to have sounds
from pygame import mixer

# We import the lists that contains the animations of the game
from animations import *
import time

pygame.mixer.pre_init(44100,-16,2,512)
mixer.init()
pygame.init()

screen = pygame.display.set_mode((set.screen_width, set.screen_height))
pygame.display.set_caption('Super Plush Rescue')
game_logo = pygame.image.load('assets/menu/logo.png')

'''We declare the variables '''

# Allow us to know at which walking frame the player is
stepIndex = 0
main_menu = True
rules_menu = False
credits_menu = False
running = True
starter_menu_bg_image = pygame.image.load('old_assets/Levels/niv2_2.png')
rules_menu_image = pygame.image.load('assets/menu/Rules.png')

'''We load the sounds in the game'''
#game_over_fx = pygame.mixer.Sound('')
#game_over_fx.set_volume(0.5)
pygame.mixer.music.load('assets/Music/Game_menu_music.mp3')
# 5000 : nbr of ms per delay
pygame.mixer.music.play(-1, 0.0, 5000)

'''We declare the various buttons use in the game (in starter menu)'''
start_image_button = pygame.image.load('assets/menu/Play_Button.png')
start_image_button = pygame. transform. scale(start_image_button, (305, 100))
rules_image_button = pygame.image.load('assets/menu/Rules_button.png')
rules_image_button = pygame. transform. scale(rules_image_button, (305, 100))
exit_image_button = pygame.image.load('assets/menu/Quit_Button.png')
exit_image_button = pygame. transform. scale(exit_image_button, (305, 100))
return_back_button = pygame.image.load('assets/menu/Return_button.png')
return_back_button = pygame. transform. scale(return_back_button, (305, 100))
credits_image_button = pygame.image.load('assets/menu/Credit_Button.png')
credits_image_button = pygame. transform. scale(credits_image_button, (305, 100))

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

        if pygame.mouse.get_pressed()[0] == 1 :
            self.is_the_button_pressed = False

        screen.blit(self.image, self.rect)

        return has_user_clicked



'''WE THEN CREATE THOSE BUTTONS WITH OUR PREVIOUS CLASS'''

start_button = Button(400, 278, start_image_button)
rules_button = Button(400, 378, rules_image_button)
credits_button = Button(400, 478, credits_image_button)
exit_button = Button(400, 578, exit_image_button)
return_button = Button(778, 600, return_back_button)


# Blit allows us to draw the png pictures onto the player's assigned ppsition
def draw_game():
    global stepIndex

    # We apply the image of the current background that the character is on the screen
    screen.blit(background[set.background_index], (0, 0))

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

bg = pygame.image.load('old_assets/Levels/niv1_1.png')

while running:
    screen.blit(bg, (0, 0))
    # We will load the button and main menu thingy when main menu is true, else we load the game
    if main_menu:
        # We apply the background image of the starter menu
        screen.blit(starter_menu_bg_image, (500, 0))
        screen.blit(game_logo, (340, 50))

        if start_button.draw():
            main_menu = False

        if rules_button.draw():
            rules_menu = True
            main_menu = True

        if credits_button.draw():
            credits_menu = True
            main_menu = True

        if exit_button.draw() :
            running = False

    if rules_menu:
        screen.blit(rules_menu_image, (0, 0))
        return_button.draw()
        if return_button.draw():
            rules_menu = False
            main_menu = True

    if credits_menu:
        screen.blit(rules_menu_image, (0, 0))
        return_button.draw()
        if return_button.draw():
            credits_menu = False
            main_menu = True


    if not main_menu:
        pygame.mixer.music.fadeout(10)
        draw_game()
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

        elif (game.pressed.get(pygame.K_RIGHT)) and (game.player.rect.x > set.screen_width) and (
                set.background_index < set.max_background_index):
            game.player.init_next()
            game.player.IsmovingRight = True
            game.player.IsmovingLeft = False
            set.background_index += 1
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