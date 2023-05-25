import pygame
import sys
import random
from settings import screen_height, screen_width, SIZE, SPECIES, block_size, tile, road_coords, directions
from src.map import drawRoads, seedForFirstTime, return_fields_list, WORLD_MATRIX
from src.Tractor import Tractor
from src.Plant import Plant
from src.bfs import Astar
from src.Field import Field
import pickle
import os


# pygame initialization
pygame.init()
clock = pygame.time.Clock()
#pygame.mouse.set_visible(False)

#GAME SCREEN
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Traktor_interaktor")
background = pygame.image.load("assets/farmland.jpg")
background = pygame.transform.scale(background,SIZE)
screen.fill((90,50,20))
background.fill((90,50,20))
background = drawRoads(background)

for line in range(26):
            pygame.draw.line(background, (0, 0, 0), (0, line * block_size), (screen_width, line * block_size))
            pygame.draw.line(background, (0, 0, 0), (line * block_size, 0), (line * block_size, screen_height))

#TRACTOR
tractor = Tractor('oil','manual', 'fuel', 'fertilizer1', 20)
tractor_group = pygame.sprite.Group()
tractor_group.add(tractor)

#PLANTS
plant_group = pygame.sprite.Group()
plant_group = seedForFirstTime()
fields = return_fields_list()

#ID3 TREE
tree = pickle.load(open(os.path.join('src','tree.plk'),'rb'))

#
tractor_move = pygame.USEREVENT + 1
pygame.time.set_timer(tractor_move, 800)
moves = []
goal_astar = Astar()
mx=random.randrange(0, 936, 36)
my=random.randrange(0, 936, 36)
destination = (mx, my)
print("Destination: ", destination)
mx=int((mx+18)/36)
my=int((my+18)/36)
print("Destination: ", mx,my)
tmp = WORLD_MATRIX[mx][my]
print(tmp)

moves = goal_astar.search(
    [tractor.rect.x, tractor.rect.y, directions[tractor.rotation]], destination)



if __name__ == "__main__":
    running = True  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    tractor.collect(plant_group)
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == tractor_move:
                if len(moves) != 0:
                    moves_list = list(moves)  # convert to list
                    step = moves_list.pop()  # pop the last element
                    moves = tuple(moves_list)  # convert back to tuple
                    tractor.movement(step[0])
                    

        Tractor.movement_using_keys(tractor)
        screen.blit(background,(0,0))
        plant_group.draw(screen)
        tractor_group.draw((screen))
        tractor_group.update()
        pygame.display.flip()
        clock.tick(60)