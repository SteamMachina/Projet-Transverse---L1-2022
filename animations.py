import pygame

background = [pygame.image.load('assets/Levels/Level 1/level1 - first.png'),
              pygame.image.load('assets/Levels/Level 1/level1 - second.png'),
              pygame.image.load('assets/Levels/Level 1/level1 - third.png'),
              pygame.image.load('assets/Levels/Level 1/level1 - fourth.png')]

right = [pygame.image.load('assets/player_walking_frames/right/walk1.png'),
         pygame.image.load('assets/player_walking_frames/right/walk1.png'),
         pygame.image.load('assets/player_walking_frames/right/walk2.png'),
         pygame.image.load('assets/player_walking_frames/right/walk2.png'),
         pygame.image.load('assets/player_walking_frames/right/walk3.png'),
         pygame.image.load('assets/player_walking_frames/right/walk3.png'),
         pygame.image.load('assets/player_walking_frames/right/walk4.png'),
         pygame.image.load('assets/player_walking_frames/right/walk4.png'),
         pygame.image.load('assets/player_walking_frames/right/walk5.png'),
         pygame.image.load('assets/player_walking_frames/right/walk5.png'),
         pygame.image.load('assets/player_walking_frames/right/walk6.png'),
         pygame.image.load('assets/player_walking_frames/right/walk6.png'),
         pygame.image.load('assets/player_walking_frames/right/walk7.png'),
         pygame.image.load('assets/player_walking_frames/right/walk7.png'),
         pygame.image.load('assets/player_walking_frames/right/walk8.png'),
         pygame.image.load('assets/player_walking_frames/right/walk8.png')]

left = [pygame.image.load('assets/player_walking_frames/left/walk1.png'),
        pygame.image.load('assets/player_walking_frames/left/walk1.png'),
        pygame.image.load('assets/player_walking_frames/left/walk2.png'),
        pygame.image.load('assets/player_walking_frames/left/walk2.png'),
        pygame.image.load('assets/player_walking_frames/left/walk3.png'),
        pygame.image.load('assets/player_walking_frames/left/walk3.png'),
        pygame.image.load('assets/player_walking_frames/left/walk4.png'),
        pygame.image.load('assets/player_walking_frames/left/walk4.png'),
        pygame.image.load('assets/player_walking_frames/left/walk5.png'),
        pygame.image.load('assets/player_walking_frames/left/walk5.png'),
        pygame.image.load('assets/player_walking_frames/left/walk6.png'),
        pygame.image.load('assets/player_walking_frames/left/walk6.png'),
        pygame.image.load('assets/player_walking_frames/left/walk7.png'),
        pygame.image.load('assets/player_walking_frames/left/walk7.png'),
        pygame.image.load('assets/player_walking_frames/left/walk8.png'),
        pygame.image.load('assets/player_walking_frames/left/walk8.png')]

boomerang_rotation = [
    pygame.transform.scale(pygame.image.load('assets/boomerang_rotation/boomerang - a0.png'), (55, 55)),
    pygame.transform.scale(pygame.image.load('assets/boomerang_rotation/boomerang - r1.png'), (55, 55)),
    pygame.transform.scale(pygame.image.load('assets/boomerang_rotation/boomerang - a2.png'), (55, 55)),
    pygame.transform.scale(pygame.image.load('assets/boomerang_rotation/boomerang - a3.png'), (55, 55)),
    pygame.transform.scale(pygame.image.load('assets/boomerang_rotation/boomerang a4.png'), (55, 55))]