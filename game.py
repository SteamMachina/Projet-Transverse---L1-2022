import pygame
from player import Player


# we create the class of the game
class Game:

    def __init__(self):
        # we generate our player
        self.player = Player()
        self.pressed = {}
