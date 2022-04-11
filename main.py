import pygame
from game import Game
import settings as set
from animations import *
import time

pygame.init()

screen = pygame.display.set_mode((set.screen_width, set.screen_height))
pygame.display.set_caption('Super Plush Rescue')

'''Allow us to know if the boomerang is on the left. If it is, the game know 
that the boomerang needs to rebounce to the right'''
boomerang_on_left = False

# Allow us to know at which  frame the rotation of the boomerang is
boomerang_rotation_index = 0

# Allow us to know at which walking frame the player is
stepIndex = 0

# Blit allows us to draw the png pictures onto the player's assigned ppsition
def draw_game():
    global stepIndex
    global boomerang_on_left
    global boomerang_rotation_index

    # We apply the image of the current background that the character is on the screen
    screen.blit(background[set.background_index], (0, 0))

    # We configure how each sub-level 1 of level 1 is going to be
    if set.background_index == 0:

        if (not game.pressed.get(pygame.K_t)) and (
                game.boomerang.rect.x > 0) and game.boomerang.rect.x != set.hidden_object_space and boomerang_on_left == False:
            game.boomerang.moves_left()

            if game.boomerang.rect.x == 0:
                boomerang_on_left = True

        elif (not game.pressed.get(pygame.K_t)) and (game.boomerang.rect.x != set.hidden_object_space) and (
                boomerang_on_left == True) and game.boomerang.rect.x <= set.screen_width:
            game.boomerang.moves_right()

            if game.boomerang.rect.x == set.screen_width:
                boomerang_on_left = False
        else:
            game.boomerang.rect.x = set.hidden_object_space

        # If the player already went through all 8 walking frames, we reset it to 0
        if boomerang_rotation_index >= 5:
            boomerang_rotation_index = 0
        # If player goes right, we go through the right list walking frames
        elif boomerang_on_left == False:
            screen.blit(boomerang_rotation[boomerang_rotation_index],
                        (game.boomerang.rect.x, game.boomerang.rect.y))
            boomerang_rotation_index += 1
        elif boomerang_on_left == True:
            screen.blit(boomerang_rotation[boomerang_rotation_index],
                        (game.boomerang.rect.x, game.boomerang.rect.y))
            boomerang_rotation_index += 1

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

running = True
while running:
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

    elif (game.pressed.get(pygame.K_RIGHT)) and (game.player.rect.x > set.screen_width) and (set.background_index < set.max_background_index):
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
