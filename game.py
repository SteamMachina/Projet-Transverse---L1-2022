from player import Player
#from ennemies import Boomerang


# we create the class of the game
class Game:

    def __init__(self):
        # we generate our player
        self.player = Player()
        #self.boomerang = Boomerang()
        self.pressed = {}


