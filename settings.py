import pygame

##############
# parameters #
##############
screen_width = 1080
screen_height = 720
white = (255, 255, 255)
black = (0, 0, 0)

'''FONTS -------------------------------------------- '''
font = pygame.font.SysFont(None,25)

'''IMAGES -------------------------------------------- '''

game_logo = pygame.image.load('assets/menu/logo.png')
side_left_bg_starter_menu = pygame.image.load('old_assets/Levels/niv1_1.png')
side_right_bg_starter_menu = pygame.image.load('old_assets/Levels/niv2_2.png')
rules_menu_image = pygame.image.load('assets/menu/Rules.png')


'''We declare the various buttons use in the game (in starter menu)'''
start_image_button = pygame.image.load('assets/menu/Play_Button.png')
start_image_button = pygame.transform.scale(start_image_button, (305, 100))
rules_image_button = pygame.image.load('assets/menu/Rules_button.png')
rules_image_button = pygame.transform.scale(rules_image_button, (305, 100))
exit_image_button = pygame.image.load('assets/menu/Quit_Button.png')
exit_image_button = pygame.transform.scale(exit_image_button, (305, 100))
return_back_button = pygame.image.load('assets/menu/Return_button.png')
return_back_button = pygame.transform.scale(return_back_button, (305, 100))
credits_image_button = pygame.image.load('assets/menu/Credit_Button.png')
credits_image_button = pygame.transform.scale(credits_image_button, (305, 100))

hard_difficulty_button = pygame.image.load('assets/menu/Hard_Difficulty_Button.png')
hard_difficulty_button = pygame.transform.scale(hard_difficulty_button, (305, 100))
easy_difficulty_button = pygame.image.load('assets/menu/Easy_Difficulty_Button.png')
easy_difficulty_button = pygame.transform.scale(easy_difficulty_button, (305, 100))


# We define a position where to hide ennemies after they're killed
hidden_object_space = 1090

# Allow us to know at which walking frame the player is
stepIndex = 0


# Allow us to know at which frame the background of Level 1 of the boomerang is
background_index = 0
max_background_index = 4