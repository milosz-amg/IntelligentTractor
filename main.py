import pygame
import sys
import tractor
import src.screen as screen
import src.plant as plant
from src.Tractor import Tractor as ractor2
#import src.tractor as tractor2

# pygame initialization
pygame.init()
pygame.mouse.set_visible(False)

# #new tractor sprite - todo
# tr=tractor2('oil','manual',36,36)
# tr_group = pygame.sprite.Group()
# tr_group.add()

# creating agent
myTractor = tractor.Tractor
        
#if __name__ == "__main__":
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
    
#pygame.quit()