import pygame


class Menu:

    def __init__(self):
        self.main_menu = True
        self.rules_menu = False
        self.credits_menu = False
        self.difficulty_menu = False
        self.exit_menu = False
        self.return_menu = False
        self.should_starter_menu_appear = True
        self.level_difficulty = "Nothing"


'''A class for the buttons of the game in the starter menu'''


class Button:
    # We put an image so that we can change the purpose of buttons at once and not re-create function per buttons
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_the_button_pressed = False


    def draw(self, surface):

        # We define a variable which will tell us if the user pressed the button

        has_user_clicked = False

        # we get the mouse position
        pos = pygame.mouse.get_pos()
        # Since rect acts like a rectangle, we can use a collision function to see if clicked

        '''First we confirm that the mouse is on the button 
        and we check if the mouse clicked, [0] means the left mouse button'''
        if (
                self.rect.collidepoint(pos)
                and pygame.mouse.get_pressed()[0] == 1
                and self.is_the_button_pressed == False
        ):
            has_user_clicked = True
            self.is_the_button_pressed = True

        if pygame.mouse.get_pressed()[0] == 1:
            self.is_the_button_pressed = False

        surface.blit(self.image, self.rect)

        return has_user_clicked
