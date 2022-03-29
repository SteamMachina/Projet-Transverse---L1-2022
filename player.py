import pygame

##############
# parameters #
##############
screen_width = 1080
screen_heigh = 720


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.velocity_fast = 20
        self.image = pygame.image.load('assets/player_walking_frames/right/walk1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 362

        '''PLAYER MOVEMENT'''
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 362

        '''BOOLEAN '''
        # Boolean that will indicate if the player is currently moving right or left
        self.IsmovingRight = False
        self.IsmovingLeft = False

    def move_right(self,velocity):
        # vitesse du joueur
        self.rect.x += velocity

    def move_left(self,velocity):
        self.rect.x -= velocity

    def init_next(self):
        self.rect.x = 0

    def init_previous(self):
        self.rect.x = screen_width