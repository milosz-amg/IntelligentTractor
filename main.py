import pygame
import tractor

#pygame initialization
pygame.init()

#set screen
SCREEN = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Traktor_interaktor")

myTractor = tractor.Tractor

#screen background
def set_screen():
        SCREEN.fill((0,100,0))
        TRACTOR = SCREEN.blit(myTractor.ROTATION_IMG, (myTractor.x, myTractor.y))
        pygame.display.update()

if __name__ == "__main__":
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and myTractor.x>0:
                 myTractor.ROTATION_IMG = myTractor.LEFT
                 myTractor.x -= myTractor.speed
            if keys[pygame.K_RIGHT] and myTractor.x<1000-myTractor.width:
                 myTractor.ROTATION_IMG = myTractor.RIGHT
                 myTractor.x += myTractor.speed
            if keys[pygame.K_UP] and myTractor.y>0:
                 myTractor.ROTATION_IMG = myTractor.UP
                 myTractor.y -= myTractor.speed
            if keys[pygame.K_DOWN] and myTractor.y<1000-myTractor.height:
                 myTractor.ROTATION_IMG = myTractor.DOWN
                 myTractor.y += myTractor.speed
        set_screen()
        
    pygame.quit()