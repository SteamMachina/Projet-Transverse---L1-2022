import pygame
from objects import Objects


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 10
        self.attack = 10
        self.projectiles_everything = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player_walking_frames/right/walk1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 435
        self.jumpHeight = 10
        self.isJumping = False

    def move_right(self):
        # vitesse du joueur
        self.rect.x += self.velocityp

    def move_left(self):
        self.rect.x -= self.velocity


