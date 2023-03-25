import pygame
import sys
import random
from settings import screen_height, screen_width, SIZE, SPECIES, block_size, tile, road_coords_y, road_coords_x
from src.map import drawRoads
from src.Tractor import Tractor
from src.Plant import Plant

# pygame initialization
pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#GAME SCREEN
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Traktor_interaktor")
background = pygame.image.load("assets/farmland.jpg")
background = pygame.transform.scale(background,SIZE)
screen.fill((90,50,20))
background.fill((90,50,20))
background = drawRoads(background)

for line in range(25):
            pygame.draw.line(background, (0, 0, 0), (0, line * 36), (SIZE[0], line * 36))
            pygame.draw.line(background, (0, 0, 0), (line * 36, 0), (line * 36, SIZE[1]))


#TRACTOR
tractor = Tractor('oil','manual')
tractor_group = pygame.sprite.Group()
tractor_group.add(tractor)

#PLANTS
plant_group = pygame.sprite.Group()
for plant in range(30):
     new_plant = Plant(random.choice(SPECIES),0,random.randrange(0,25)*36+18,random.randrange(0,25)*36+18)
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
        
