import pygame

class Player():

    def __init__(self):
        main_menu = True
        rules_menu = False
        credits_menu = False
        paused = False

class Button():
    # We put an image so that we can change the purpose of buttons at once and not re-create function per buttons
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_the_button_pressed = False

        self.small_font = pygame.font.Font("freesansbold.ttf", 25)
        self.medium_font = pygame.font.Font("freesansbold.ttf", 50)
        self.big_font = pygame.font.Font("freesansbold.ttf", 80)

    def draw(self):

        # We define a variable which will tell us if the user pressed the button

        has_user_clicked = False

        # we get the mouse position
        pos = pygame.mouse.get_pos()
        # Since rect acts like a rectangle, we can use a collision function to see if clicked

        # First we confirm that the mouse is on the button
        if self.rect.collidepoint(pos):
            # Now we checked if the mouse clicked, [0] means the left mouse button
            if pygame.mouse.get_pressed()[0] == 1 and self.is_the_button_pressed == False:
                has_user_clicked = True
                self.is_the_button_pressed = True

        if pygame.mouse.get_pressed()[0] == 1:
            self.is_the_button_pressed = False

        screen.blit(self.image, self.rect)

        return has_user_clicked