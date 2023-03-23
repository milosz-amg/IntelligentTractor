import pygame
from settings import screen_height, screen_width, SIZE, SPECIES, block_size, tile, road_coords_x, road_coords_y


def drawRoads(screen):
    #drawing roads:
    road = pygame.image.load("assets/road.jpeg")
    road = pygame.transform.scale(road, tile)
    for x in road_coords_x:
        for block in range(25):
            screen.blit(road, (x*block_size, block * 36))
    for y in road_coords_y:
        for block in range(25):
            screen.blit(road, (block * 36, y*block_size))

    barn_img = pygame.image.load('assets/barn.png')
    barn = pygame.transform.scale(barn_img, tile)
    screen.blit(barn, (0, 864))
        
    return screen


# to-be-done with minecraft farmland graphic xD
# maybe this function should be in drawRoads (ofc with changed name), not separated

#def drawFields(background):
    #field = pygame.image.load()
    #field = pygame.transform.scale(field, tile)
    #for x in range(25):
        #if block not in road_coords_x:
            #screen.blit(field, (x*block_size, block * 36))
    #for y in range(25):
        #if block not in road_coords_y:
            #screen.blit(field, (block*36, y*block_size))

    #return screen
