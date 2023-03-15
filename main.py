import pygame
import tractor
import screen

# pygame initialization
pygame.init()

# creating agent
myTractor = tractor.Tractor
        
if __name__ == "__main__":
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # defines agent movement
            tractor.movement(myTractor)
        # screen visualisation
        screen.set_screen(myTractor)
        
    pygame.quit()