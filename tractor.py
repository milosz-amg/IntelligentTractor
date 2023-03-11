import pygame

class Tractor:
    #this is where tractor spawns when program starts (center)
    x=500
    y=500
    #it's speed -> pixels it moves after pressing arrow
    speed = 10
    #it's size
    width = 20
    height = 20
    
    #tractor image rotation
    ROTATION_IMG = pygame.image.load('assets/tractor/tractor_UP.png')
    UP = pygame.image.load('assets/tractor/tractor_UP.png')
    DOWN = pygame.image.load('assets/tractor/tractor_DOWN.png')
    LEFT = pygame.image.load('assets/tractor/tractor_LEFT.png')
    RIGHT = pygame.image.load('assets/tractor/tractor_RIGHT.png')
    
