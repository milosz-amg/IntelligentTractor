import pygame
import sys
import random
from settings import SIZE, directions, draw_lines_on_window, matrix_plants_type
from src.map import drawRoads, seedForFirstTime, return_fields_list, WORLD_MATRIX, get_type_by_position
from src.Tractor import Tractor
from src.bfs import Astar
from src.Plant import Plant
from src.Field import Field
import pickle
import os
from src.ID3 import action
import torch
import src.neural_networks as neural_networks

def show_plant_img(img):
    image = pygame.image.load(img)
    image = pygame.transform.scale(image, (360, 360))
    screen.blit(image, (972, 288))
    pygame.display.update()
    pygame.time.delay(1000)

# neural_networks.learn()

def recognize_plants(fields, destination):
    checkpoint = torch.load(f'plants2.model')
    model = neural_networks.Net(num_classes=3)
    model.load_state_dict(checkpoint)
    model.eval()
    img = ''
    if get_type_by_position(fields, destination[0], destination[1]) == 'carrot':
        img = 'assets/learning/test/carrot/' + str(random.randint(1, 200)) + '.jpg'
        pred = neural_networks.predict(img, model)
        show_plant_img(img)
    elif get_type_by_position(fields, destination[0], destination[1]) == 'potato':
        img = 'assets/learning/test/potato/' + str(random.randint(1, 200)) + '.jpg'
        pred = neural_networks.predict(img, model)
        show_plant_img(img)
    elif get_type_by_position(fields, destination[0], destination[1]) == 'wheat':
        img = 'assets/learning/test/wheat/' + str(random.randint(1, 200)) + '.jpg'
        pred = neural_networks.predict(img, model)
        show_plant_img(img)
    else:
        pred = 'none'
    print(pred)
    return pred


# pygame initialization
pygame.init()
clock = pygame.time.Clock()

# GAME SCREEN
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Traktor_interaktor")
background = pygame.image.load("assets/farmland.jpg")
background = pygame.transform.scale(background,SIZE)
screen.fill((90,50,20))
background.fill((90,50,20))
background = drawRoads(background)

draw_lines_on_window(background)

#TRACTOR
tractor = Tractor('oil','manual', 'fuel', 'fertilizer1', 20)
tractor_group = pygame.sprite.Group()
tractor_group.add(tractor)

tractor.setCapacity(90)
tractor.setFuel(100)

#PLANTS
plant_group = pygame.sprite.Group()
plant_group = seedForFirstTime()
fields = return_fields_list()

#
tractor_move = pygame.USEREVENT + 1
pygame.time.set_timer(tractor_move, 200)
moves = []
goal_astar = Astar()
mx = random.randrange(0, 936, 36)
my = random.randrange(0, 936, 36)
destination = (mx, my)
print("Destination: ", destination)
mx = int((mx+18)/36)
my = int((my+18)/36)
print("Destination: ", mx, my)

#ID3 TREE LOADING
dtree = pickle.load(open(os.path.join('src','tree.plk'),'rb'))
     
# pobierz dane o polu field i czy ma na sobie roslinke, zadecyduj czy zebrac
this_field = WORLD_MATRIX[mx][my]
this_contain = Field.getContain(this_field)


moves = goal_astar.search(
    [tractor.rect.x, tractor.rect.y, directions[tractor.rotation]], destination)

expected_plant = get_type_by_position(fields, destination[0], destination[1])


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
                    # recognize_plants(fields, destination)
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == tractor_move:
                if len(moves) != 0:
                    moves_list = list(moves)  # convert to list
                    step = moves_list.pop()  # pop the last element
                    moves = tuple(moves_list)  # convert back to tuple
                    tractor.movement(step[0])
                    # checks if tractor is in destiantion field and make decision if it's ready to collect
                    if tractor.rect.x == destination[0] and tractor.rect.y == destination[1] and action(this_contain, Plant, tractor, dtree) == 1:
                        # show what should be in this field
                        print('expected:', expected_plant)
                        # check if program correctly recognize plant
                        if recognize_plants(fields, destination) == expected_plant:
                            # if correctly  recognized than plant can be collected
                            tractor.collect(plant_group)
                        else:
                            print('wrong recognition')
                    

        Tractor.movement_using_keys(tractor)
        screen.blit(background,(0,0))
        plant_group.draw(screen)
        tractor_group.draw((screen))
        tractor_group.update()
        pygame.display.flip()
        clock.tick(60)