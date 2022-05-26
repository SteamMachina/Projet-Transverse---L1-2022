import pygame
from menu import Button
pygame.font.init()

##############
# parameters #
##############
screen_width = 1080
screen_height = 720

##############
# colors #
##############
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

'''FONTS -------------------------------------------- '''
small_font = pygame.font.Font("freesansbold.ttf", 25)
medium_font = pygame.font.Font("freesansbold.ttf", 50)
big_font = pygame.font.Font("freesansbold.ttf", 80)

'''IMAGES -------------------------------------------- '''

game_logo = pygame.image.load('assets/menu/logo.png')
side_left_bg_starter_menu = pygame.image.load('old_assets/Levels/niv1_1.png')
side_right_bg_starter_menu = pygame.image.load('old_assets/Levels/niv2_2.png')
rules_menu_image = pygame.image.load('assets/menu/Rules.png')
in_game_rules_image = pygame.image.load('assets/menu/InGame_Rules.png')
in_game_rules_image = pygame.transform.scale(in_game_rules_image, (800, 500))
game_over_image = pygame.image.load('assets/menu/Game_Over_Menu.png')

'''We declare the various buttons use in the game (in starter menu)'''
start_image_button = pygame.image.load('assets/menu/Play_Button.png')
start_image_button = pygame.transform.scale(start_image_button, (305, 100))
rules_image_button = pygame.image.load('assets/menu/Rules_button.png')
rules_image_button = pygame.transform.scale(rules_image_button, (305, 100))
exit_image_button = pygame.image.load('assets/menu/Quit_Button.png')
exit_image_button = pygame.transform.scale(exit_image_button, (305, 100))
return_back_button = pygame.image.load('assets/menu/Return_button.png')
return_back_button = pygame.transform.scale(return_back_button, (150, 80))
credits_image_button = pygame.image.load('assets/menu/Credit_Button.png')
credits_image_button = pygame.transform.scale(credits_image_button, (305, 100))

hard_difficulty_button = pygame.image.load('assets/menu/Hard_Difficulty_Button.png')
hard_difficulty_button = pygame.transform.scale(hard_difficulty_button, (305, 100))
easy_difficulty_button = pygame.image.load('assets/menu/Easy_Difficulty_Button.png')
easy_difficulty_button = pygame.transform.scale(easy_difficulty_button, (305, 100))

'''BUTTONS --------------------------------------------
'WE THEN CREATE THOSE BUTTONS WITH OUR PREVIOUS CLASS'''

start_button = Button(400, 278, start_image_button)
rules_button = Button(400, 378, rules_image_button)
credits_button = Button(400, 478, credits_image_button)
exit_button = Button(400, 578, exit_image_button)
return_button = Button(878, 600, return_back_button)

hard_game_difficulty_button = Button(650, 278, hard_difficulty_button)
easy_game_difficulty_button = Button(50, 278, easy_difficulty_button)


# We define a position where to hide ennemies after they're killed
hidden_object_space = 1090

# Allow us to know at which walking frame the player is
stepIndex = 0


# Allow us to know at which frame the background of Level 1 of the boomerang is
background_index = 0
max_background_index = 4