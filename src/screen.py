import pygame

# size in pixels of one tile = 36px/36px
tile = (36, 36)

# later move it to another class "barn"?
barn_img = pygame.image.load('assets/barn.png')
barn = pygame.transform.scale(barn_img, tile) 

# screen settings
SIZE = (900, 900)
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Traktor_interaktor")

# screen dispaly
def set_screen(myTractor):
        # setting background color
        SCREEN.fill((90,50,20))
        
        # dispaly agent icon
        TRACTOR = SCREEN.blit(myTractor.IMG, (myTractor.x, myTractor.y))
        # display barn
        SCREEN.blit(barn, (0, 863))
        # draw lines(horizontal, vertical) on the screen
        for line in range(25):
            pygame.draw.line(SCREEN, (0, 0, 0), (0, line * 36), (SIZE[0], line * 36))
            pygame.draw.line(SCREEN, (0, 0, 0), (line * 36, 0), (line * 36, SIZE[1]))
            
        pygame.display.update()