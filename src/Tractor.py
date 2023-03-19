from pygame.sprite import Sprite
import pygame

class Tractor(pygame.sprite.Sprite):
    def __init__(self,engine,transmission,pos_x,pos_y):
        super.__init__()
        self.image=pygame.image.load("../assets/tractor/tractor.png")
        self.image=pygame.transform.scale(self,(36,36))
        self.rect = self.image.get_rect()

        self.engine=engine
        self.transmission=transmission
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.fuel=100

    def update(self):
        self.rect.center=pygame.mouse.get_pos()
        # self.pos_x=pos_x
        # self.pos_y=pos_y

    def movement(self):
        print("todo")

        
    def rotation(self,direction):
        print("todo")



