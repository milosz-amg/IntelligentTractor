from cmath import sqrt
import pygame
from settings import screen_height, screen_width, SIZE, SPECIES, block_size, tile, road_coords, fields_amount, field_size, field_height, field_width
from src.Plant import Plant
import random
from src.Field import Field
from src.Road import Road
import csv


def get_type_by_position(fields, x, y):
    for field in fields:
        if field.x == x and field.y == y:
            return field.plant_type
    return None

def get_cost_by_type(plant_type):
    #plant_type == None, when field is empty.
    if plant_type == None: 
        return 200
    elif plant_type == 'carrot':
        return 300
    elif plant_type == 'potato':
        return 500
    elif plant_type == 'beetroot':
        return 500
    elif plant_type == 'wheat':
        return 1000
    #else, means that field is type of road.
    else:
        return 100

fields = pygame.sprite.Group()

 
world_matrix = [[0 for _ in range(fields_amount+1)] for _ in range(fields_amount+1)]

def drawRoads(screen):
    #drawing roads:
    road = pygame.image.load("assets/road.jpeg")
    road = pygame.transform.scale(road, tile)
    for x in road_coords:
        for block in range(int(fields_amount)+1):
            screen.blit(road, (x*block_size, block * 36))
            tmp_field=Field('road', x*block_size, block * 36, None, get_cost_by_type('road'), None, None, None, None, 'road', None, None)
            fields.add(tmp_field)
            world_matrix[x][block]=Road(x,block)
    for y in road_coords:
        for block in range(int(fields_amount)+1):
            screen.blit(road, (block * block_size, y*block_size))
            tmp_field=Field('road', block * block_size, y*block_size, None, get_cost_by_type('road'), None, None, None, None, 'road', None, None)
            fields.add(tmp_field)
            world_matrix[block][y]=Road(block,y)


    barn_img = pygame.image.load('assets/barn.png')
    barn = pygame.transform.scale(barn_img, tile)
    screen.blit(barn, (0, 900))
        
    return screen

def seedForFirstTime():
    plant_group = pygame.sprite.Group()
    for field in range(fields_amount):
        plant_name = random.choice(SPECIES)
        blocks_seeded_in_field = 0
        while (blocks_seeded_in_field < field_size):

            x = (((field%5)*((block_size*(field_width+1)))) + ((blocks_seeded_in_field % field_width)*block_size) + ((3/2)*block_size))
            y = ((int(field/5)*((block_size*(field_width+1)))) + ((int(blocks_seeded_in_field/field_height))*block_size) + ((3/2)*block_size))
            
            new_plant = Plant(plant_name,0, x, y)
            blocks_seeded_in_field = blocks_seeded_in_field + 1
            plant_group.add(new_plant)
            tmp_field_plant = Field('field', x-18, y-18, None, get_cost_by_type(plant_name), None, None, None, None, plant_name, None, None)
            fields.add(tmp_field_plant)

            mx = int((x-18)/36)
            my = int((y-18)/36)
            world_matrix[mx][my]=tmp_field_plant

            # for i in range(1,4):
            #     world_matrix[mx][my+i]=tmp_field_plant
    #debug
    print(world_matrix)
    #end of debug

    return plant_group

def put_to_matrix():
    return 0

def return_fields_list():
    return fields


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
