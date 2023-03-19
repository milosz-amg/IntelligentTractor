import pygame
import sys
import tractor
import src.screen as screen
import src.plant as plant

class Tractor2(pygame.sprite.Sprite):
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

# pygame initialization
pygame.init()
pygame.mouse.set_visible(False)


myTractor = tractor.Tractor
        
if __name__ == "__main__":
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # defines agent movement
            tractor.movement(myTractor)
        # screen visualisation
        screen.set_screen(myTractor)
        
