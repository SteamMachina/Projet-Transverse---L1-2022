import pygame
from game import Game
import time

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
move_right = False
move_left = False
# Allow us to know at which walking frame the player is
stepIndex = 0
background = pygame.image.load('assets/Levels/Level 1/level1 - first.png')

# Load images of the characters
player_stationary = pygame.image.load('assets/player_walking_frames/right/walk1.png')

right = [pygame.image.load('assets/player_walking_frames/right/walk1.png'),
         pygame.image.load('assets/player_walking_frames/right/walk2.png'),
         pygame.image.load('assets/player_walking_frames/right/walk3.png'),
         pygame.image.load('assets/player_walking_frames/right/walk4.png'),
         pygame.image.load('assets/player_walking_frames/right/walk5.png'),
         pygame.image.load('assets/player_walking_frames/right/walk6.png'),
         pygame.image.load('assets/player_walking_frames/right/walk7.png'),
         pygame.image.load('assets/player_walking_frames/right/walk8.png')]

left = [pygame.image.load('assets/player_walking_frames/left/walk1.png'),
        pygame.image.load('assets/player_walking_frames/left/walk2.png'),
        pygame.image.load('assets/player_walking_frames/left/walk3.png'),
        pygame.image.load('assets/player_walking_frames/left/walk4.png'),
        pygame.image.load('assets/player_walking_frames/left/walk5.png'),
        pygame.image.load('assets/player_walking_frames/left/walk6.png'),
        pygame.image.load('assets/player_walking_frames/left/walk7.png'),
        pygame.image.load('assets/player_walking_frames/left/walk8.png')]

# Blit allows us to draw the png pictures onto the player's assigned ppsition
def draw_game():
    global stepIndex
    screen.blit(background, (0,0))
    # If the player already went through all 8 walking frames, we reset it to 0
    if stepIndex >= 8:
        stepIndex = 0
    # If player goes right, we go through the right list walking frames
    elif move_right:
        screen.blit(right[stepIndex], (game.player.rect.x, game.player.rect.y))
        time.sleep(0.06)
        stepIndex += 1
    # If player goes right, we go through the left list walking frames
    elif move_left:
        screen.blit(left[stepIndex], (game.player.rect.x, game.player.rect.y))
        time.sleep(0.06)
        stepIndex += 1
    # If the player neither goes left or right, we just apply the stationary frame to it
    else:
        screen.blit(player_stationary, (game.player.rect.x, game.player.rect.y))


# load our game
game = Game()

running = True
while running:
    draw_game()

    # verify if the player wants to go left or right
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 900:
        game.player.move_right()
        move_right = True
        move_left = False
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        move_right = False
        move_left = True
    else:
        move_right = False
        move_left = False
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