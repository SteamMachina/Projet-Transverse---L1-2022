import pygame

##############
# parameters #
##############
screen_width = 1080
screen_heigh = 720


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 13
        self.image = pygame.image.load('assets/player_walking_frames/walk1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 362

    def move_right(self):
        # vitesse du joueur
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def init_next(self):
        self.rect.x = 0

    def init_previous(self):
        self.rect.x = screen_width