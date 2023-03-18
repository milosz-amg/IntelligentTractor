import pygame

class Tractor:
    # this is where tractor spawns when program starts (center)
    x=432
    y=432
    # it's speed -> pixels it moves after pressing arrow
    speed = 36
    # tractor image
    tractor_img = pygame.image.load('assets/tractor/tractor.png')
    IMG = pygame.transform.scale(tractor_img, (36, 36))
    # tractor image rotation
    UP = pygame.transform.rotate(IMG, 0)
    DOWN = pygame.transform.rotate(IMG, 180)
    LEFT = pygame.transform.rotate(IMG, 90)
    RIGHT = pygame.transform.rotate(IMG, -90)


def movement(myTractor):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and myTractor.x>0:
            myTractor.IMG = myTractor.LEFT
            myTractor.x -= myTractor.speed
    if keys[pygame.K_RIGHT] and myTractor.x<900-myTractor.speed:
            myTractor.IMG = myTractor.RIGHT
            myTractor.x += myTractor.speed
    if keys[pygame.K_UP] and myTractor.y>0:
            myTractor.IMG = myTractor.UP
            myTractor.y -= myTractor.speed
    if keys[pygame.K_DOWN] and myTractor.y<900-myTractor.speed:
            myTractor.IMG = myTractor.DOWN
            myTractor.y += myTractor.speed
