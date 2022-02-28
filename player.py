import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 4
        self.image = pygame.image.load('assets/player - walking frames/walk1.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 350

    def move_right(self):
        # vitesse du joueur
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity