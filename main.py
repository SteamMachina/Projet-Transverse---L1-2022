import pygame
from game import Game

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)


def display_update():
    screen.fill(WHITE)
    #
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (1080, 600), 5)


# load our game
game = Game()

running = True
while running:

    display_update()

    # apply image of player
    screen.blit(game.player.image, game.player.rect)
    # verify if the player wants to go left or right
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 900:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
