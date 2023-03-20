import pygame
import sys
import random
from src.Tractor import Tractor
from src.Plant import Plant

#SETTINGS
screen_width=900
screen_height=900
SIZE = (screen_width, screen_height)
SPECIES=["carrot","potatoe","beetroot","wheat"]
# size in pixels of one tile = 36px/36px
tile = (36, 36)

# pygame initialization
pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#GAME SCREEN
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Traktor_interaktor")
background = pygame.image.load("assets/farmland.jpg")
background = pygame.transform.scale(background,SIZE)
background.fill((90,50,20))

for line in range(25):
            pygame.draw.line(background, (0, 0, 0), (0, line * 36), (SIZE[0], line * 36))
            pygame.draw.line(background, (0, 0, 0), (line * 36, 0), (line * 36, SIZE[1]))


#later move it to another class "barn"?
barn_img = pygame.image.load('assets/barn.png')
barn = pygame.transform.scale(barn_img, tile) 

#TRACTOR
tractor = Tractor('oil','manual')
tractor_group = pygame.sprite.Group()
tractor_group.add(tractor)

#PLANTS
plant_group = pygame.sprite.Group()
for plant in range(30):
     new_plant = Plant(random.choice(SPECIES),0,random.randrange(0,screen_width),random.randrange(0,screen_height))
     plant_group.add(new_plant)

if __name__ == "__main__":
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 tractor.collect(plant_group)
            
        pygame.display.flip()
        screen.blit(background,(0,0))
        plant_group.draw(screen)
        tractor_group.draw(screen)
        tractor_group.update()
        clock.tick(60)
        
