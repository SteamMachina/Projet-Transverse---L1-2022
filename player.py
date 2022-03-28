import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 4
        self.image = pygame.image.load('assets/player_walking_frames/walk1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 362

    def move_right(self):
        # vitesse du joueur
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity