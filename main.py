import pygame
from game import Game
import time
pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
move_right = False
move_left = False
stepIndex = 0

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


def draw_game():
    global stepIndex
    screen.fill(WHITE)
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (1080, 600), 5)
    if stepIndex >= 8:
        stepIndex = 0
    elif move_right :
        screen.blit(right[stepIndex], (game.player.rect.x,game.player.rect.y))
        time.sleep(0.06)
        stepIndex += 1
    elif move_left :
        screen.blit(left[stepIndex], (game.player.rect.x,game.player.rect.y))
        time.sleep(0.06)
        stepIndex += 1
    else:
        screen.blit(player_stationary, (game.player.rect.x,game.player.rect.y))


# load our game
game = Game()

running = True
while running:

    draw_game()

    # apply image of player
    # verify if the player wants to go left or right
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 900:
        game.player.move_right()
        move_right = True
        move_left = False
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        move_right = False
        move_left = True
    else :
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
