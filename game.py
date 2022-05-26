from level import Level
from menu import Menu
from player import Player
from settings import *


class Game:
    def __init__(self):
        super().__init__()
        self.carte = Level()
        self.joueur = Player()
        self.menu = Menu()
        self.pressed = {}
        self.ecran = pygame.display.set_mode((screen_width, screen_height))

        self.gravity = -0.4
        self.friction = -0.15

    def affichage(self):

        # printing stuff
        self.ecran.fill((255, 255, 255))

        for i in range(len(self.carte.image_ground["images"])):
            self.ecran.blit(self.carte.image_ground["images"][i],
                       (self.carte.image_ground["coordinates"][i][0] * 30, self.carte.image_ground["coordinates"][i][1] * 30))

        self.ecran.blit(self.joueur.image, (self.joueur.rect.x, self.joueur.rect.y))

        for i in range(len(self.carte.tiles_liquid["images"])):
            self.ecran.blit(self.carte.tiles_liquid["images"][i],
                       (self.carte.tiles_liquid["coordinates"][i][0] * 30, self.carte.tiles_liquid["coordinates"][i][1] * 30))

        for i in range(len(self.carte.tiles_other["images"])):
            self.ecran.blit(self.carte.tiles_other["images"][i],
                       (self.carte.tiles_other["coordinates"][i][0] * 30, self.carte.tiles_other["coordinates"][i][1] * 30))


