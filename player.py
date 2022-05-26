import pygame


class Player():

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('old_assets/player_walking_frames/right/walk1.png')

        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.yoke_velocity = 19
        self.yoke_rect = self.image.get_rect()
        self.yoke_rect.x = 100
        self.yoke_rect.y = 370
        self.position = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0.4)

        '''BOOLEAN '''
        # Boolean that will indicate if the player is currently moving right or left
        self.IsmovingRight = False
        self.IsmovingLeft = False

        self.jump = False
        self.on_ground = False

        #self.stepIndex = 0

    def move_right(self, velocity):
        # vitesse du joueur
        self.yoke_rect.x += velocity

    def move_left(self, velocity):
        self.yoke_rect.x -= velocity

    # main function that calls the others
    def movements(self, game, delta_time):
        self.mov_x(game, delta_time)
        self.colli_x(game.carte.tiles_ground)
        self.mov_y(delta_time)
        self.colli_y(game.carte.tiles_ground)

    # function that calculates the x & y coordinates of the player

    def mov_x(self, game, delta_time):
        self.acceleration.x = 0
        if (pygame.key.get_pressed()[pygame.K_RIGHT]) and (self.acceleration.x < 8):
            self.acceleration.x += 0.6
            self.IsmovingRight = True
            self.IsmovingLeft = False

        elif (pygame.key.get_pressed()[pygame.K_LEFT]) and (self.acceleration.x > -8):
            self.acceleration.x -= 0.6
            self.IsmovingRight = False
            self.IsmovingLeft = True
        else:
            self.IsmovingRight = False
            self.IsmovingLeft = False
            self.stepIndex = 0

        self.acceleration.x += self.velocity.x * game.friction
        self.velocity.x += self.acceleration.x * delta_time

        if (self.velocity.x < 0.1) and (self.velocity.x > -0.1):
            self.velocity.x = 0

        self.position.x += self.acceleration.x * 0.5 * delta_time ** 2 + self.velocity.x * delta_time
        self.rect.x = self.position.x

    def mov_y(self, delta_time):
        if (pygame.key.get_pressed()[pygame.K_UP]) and (self.on_ground is True):
            self.velocity.y -= 8
            self.on_ground = False
            self.jump = True
        self.velocity.y += self.acceleration.y * delta_time

        if self.velocity.y > 6:
            self.velocity.y = 6

        self.position.y += self.velocity.y * delta_time + self.acceleration.y / 2 * delta_time ** 2
        self.rect.bottom = self.position.y

    # functions that rectfies the position in case of a collision

    def colli_x(self, obj_list):
        collision = self.get_hit(obj_list)
        for obj in collision:
            if self.velocity.x > 0:  # hits the box from the left
                self.position.x = obj.x - self.rect.width
                self.rect.x = self.position.x

            elif self.velocity.x < 0:  # hits the box from the right
                self.position.x = obj.right
                self.rect.x = self.position.x

    def colli_y(self, obj_list):
        self.on_ground = False
        self.rect.bottom += 1

        collision = self.get_hit(obj_list)
        for obj in collision:
            if self.velocity.y > 0:  # hits the box from the top
                self.on_ground = True
                self.jump = False
                self.velocity.y = 0

                self.position.y = obj.top
                self.rect.bottom = self.position.y

            elif self.velocity.y < 0:  # hits the box from the bottom
                self.velocity.y = 0
                self.position.y = obj.bottom + self.rect.h
                self.rect.bottom = self.position.y

    def get_hit(self, obj_list):
        hit_list = []
        for element in obj_list:
            if self.rect.colliderect(element):
                hit_list.append(element)

        return hit_list
