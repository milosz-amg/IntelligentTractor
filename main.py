import pygame
import sys
import random
from settings import screen_height, screen_width, SIZE, SPECIES, block_size, tile, road_coords, directions
from src.map import drawRoads, seedForFirstTime, return_fields_list, WORLD_MATRIX
from src.Tractor import Tractor
from src.bfs import Astar
from src.Plant import Plant
from src.Field import Field
import pickle
import os
from src.ID3 import make_decision
import torch
import neural_networks

def recognize_plants(plants_array):
    checkpoint = torch.load(f'plants.model')
    model = neural_networks.Net(num_classes=3)
    model.load_state_dict(checkpoint)
    model.eval()
    img = ''
    b=0
    j=0
    field_array_small = []
    field_array_big = []
    for i in range(11):
        field_array_small = []
        if b == 0:
            for j in range(11):
                if plants_array[j][i] == 'carrot':
                    img = 'assets/learning/test/carrot/' + str(random.randint(1, 200)) + '.jpg'
                    pred = neural_networks.prediction(img, model)
                    #show_plant_img(img)
                elif plants_array[j][i] == 'potato':
                    img = 'assets/learning/test/potato/' + str(random.randint(1, 200)) + '.jpg'
                    pred = neural_networks.prediction(img, model)
                    # show_plant_img(img)
                elif plants_array[j][i] == 'wheat':
                    img = 'assets/learning/test/wheat/' + str(random.randint(1, 200)) + '.jpg'
                    pred = neural_networks.prediction(img, model)
                    # show_plant_img(img)
                else:
                    pred = 'none'
                field_array_small.append(pred)
                print(i,',', j,'-',pred)
                # agent_movement(['f'], agent, fields_for_movement, fields_for_astar)
            # agent_movement(['r','f','r'], agent, fields_for_movement, fields_for_astar)
            field_array_big.append(field_array_small)
        else:
            for j in range(10,-1,-1):
                if plants_array[j][i] == 'carrot':
                    img = 'assets/learning/test/carrot/' + str(random.randint(1, 200)) + '.jpg'
                    pred = neural_networks.prediction(img, model)
                    # show_plant_img(img)
                elif plants_array[j][i] == 'potato':
                    img = 'assets/learning/test/potato/' + str(random.randint(1, 200)) + '.jpg'
                    pred = neural_networks.prediction(img, model)
                    # show_plant_img(img)
                elif plants_array[j][i] == 'wheat':
                    img = 'assets/learning/test/wheat/' + str(random.randint(1, 200)) + '.jpg'
                    pred = neural_networks.prediction(img, model)
                    # show_plant_img(img)
                else:
                    pred = 'none'
                field_array_small.append(pred)
                print(i,',', j,'-',pred)
                # agent_movement(['f'], agent, fields_for_movement, fields_for_astar)
            field_array_small = field_array_small[::-1]
            field_array_big.append(field_array_small)
            # agent_movement(['l','f','l'], agent, fields_for_movement, fields_for_astar)
        if b==0:
            b=1
        else:
            b=0
    correct = 0
    incorrect = 0
    for i in range(11):
        for j in range(11):
            if plants_array[i][j]=='none':
                continue
            else:
                if plants_array[i][j]==field_array_big[j][i]:
                    correct+=1
                else:
                    incorrect+=1
    print("Accuracy: ",correct/(correct+incorrect)*100,'%')



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

tractor.setCapacity(90)
tractor.setFuel(100)

#PLANTS
plant_group = pygame.sprite.Group()
plant_group = seedForFirstTime()
fields = return_fields_list()



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

#ID3 TREE LOADING
dtree = pickle.load(open(os.path.join('src','tree.plk'),'rb'))
     
# pobierz dane o polu field i czy ma na sobie roslinke, zadecyduj czy zebrac
this_field = WORLD_MATRIX[mx][my]
this_contain = Field.getContain(this_field)
def action(this_contain):
    if isinstance(this_contain, Plant): 
        this_plant = this_contain
        params=Plant.getParameters(this_plant)
        #ID3 decision
        decision=make_decision(params[0],params[1],params[2],params[3],params[4],tractor.fuel,tractor.capacity,params[5],dtree)
        print('wzorst',params[0],'wilgotnosc',params[1],'dni_od_nawiezienia',params[2],'pogoda',params[3],'zdrowa',params[4],'paliwo',tractor.fuel,'pojemnosc eq',tractor.capacity,'cena sprzedazy',params[5])
        print(decision)
        if decision == 1:
            print('Gotowe do zbioru')
            return 1
        else:
            print('nie zbieramy')
            return 0
    else:
        print('Road, no plant growing')
        return 0


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
                    if (tractor.rect.x, tractor.rect.y) == destination and action == 1:
                        tractor.collect(plant_group)
                    
                    

        Tractor.movement_using_keys(tractor)
        screen.blit(background,(0,0))
        plant_group.draw(screen)
        tractor_group.draw((screen))
        tractor_group.update()
        pygame.display.flip()
        clock.tick(60)