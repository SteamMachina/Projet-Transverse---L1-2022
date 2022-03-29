import pygame
from player import Player
from ennemies import Boomerang


# we create the class of the game
class Game:

    def __init__(self):
        # we generate our player
        self.player = Player()
        self.boomerang = Boomerang()
        #self.all_enemies = pygame.sprite.Group()
        self.pressed = {}
        #self.spawn_enemies()

    #def spawn_enemies(self):
        #boomerang_enemy = Boomerang()
        #self.all_enemies.add(boomerang_enemy)

