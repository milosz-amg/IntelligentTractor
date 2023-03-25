from cmath import sqrt
import pygame
from settings import screen_height, screen_width, SIZE, SPECIES, block_size, tile, road_coords, fields_amount, field_size, field_height, field_width
from src.Plant import Plant
import random


def drawRoads(screen):
    #drawing roads:
    road = pygame.image.load("assets/road.jpeg")
    road = pygame.transform.scale(road, tile)
    for x in road_coords:
        for block in range(26):
            screen.blit(road, (x*block_size, block * 36))
    for y in road_coords:
        for block in range(26):
            screen.blit(road, (block * 36, y*block_size))

    barn_img = pygame.image.load('assets/barn.png')
    barn = pygame.transform.scale(barn_img, tile)
    screen.blit(barn, (0, 900))
        
    return screen

def seedForFirstTime():
    plant_group = pygame.sprite.Group()
    for field in range(fields_amount):
        plant = random.choice(SPECIES)
        blocks_seeded_in_field = 0
        while (blocks_seeded_in_field < field_size):
            x = (((field%5)*((block_size*(field_width+1)))) + ((blocks_seeded_in_field % field_width)*block_size) + ((3/2)*block_size))
            y = ((int(field/5)*((block_size*(field_width+1)))) + ((int(blocks_seeded_in_field/field_height))*block_size) + ((3/2)*block_size))
            new_plant = Plant(plant,0, x, y)
            blocks_seeded_in_field = blocks_seeded_in_field + 1
            plant_group.add(new_plant)
    return plant_group


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
