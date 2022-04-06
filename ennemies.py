import pygame


# The class of the Continuous boomerang in the third frame
# The boomerang can't be caught, nor destroy
class Boomerang(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.attack = 5
        self.image = pygame.image.load('assets/boomerang_rotation/boomerang - a0.png')
        self.image_scale = pygame.transform.scale(pygame.image.load('assets/boomerang_rotation/boomerang - a0.png'), (55, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 380
        self.velocity = 10

    def moves_right(self):
        self.rect.x += self.velocity

    def moves_left(self):
        self.rect.x -= self.velocity


