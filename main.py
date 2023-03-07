import pygame

#pygame initialization
pygame.init()

#set screen
SCREEN = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Traktor_interaktor")

#screen background
def set_screen():
        SCREEN.fill((0,100,0))
        pygame.display.update()
    


if __name__ == "__main__":
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        set_screen()
        
    pygame.quit()