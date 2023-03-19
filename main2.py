import pygame
import sys
import random
#import tractor
#import src.screen as screen
import src.plant as plant

screen_width=900
screen_height=900
SIZE = (screen_width, screen_height)
SPECIES=["carrot","potatoe","beetroot","wheat"]
# collected=0


#agent class
class Tractor(pygame.sprite.Sprite):
    def __init__(self,engine,transmission):
        super().__init__()
        self.image=pygame.image.load("assets/tractor/tractor.png")
        self.image=pygame.transform.scale(self.image,(36,36))
        self.rect = self.image.get_rect()

        self.engine=engine
        self.transmission=transmission
        self.fuel=100
    
    def collect(self):
         print("collected plant")
         pygame.sprite.spritecollide(tractor,plant_grup,True)
        #  collected=collected+1
        #  print("plants in trunk "+collected)

    def update(self):
        self.rect.center=pygame.mouse.get_pos()

#plant class
class Plant(pygame.sprite.Sprite):
    def __init__(self,species,is_ill,pos_x,pos_y):
        super().__init__()
        self.species=species
        self.is_ill=is_ill

        if species=="carrot":
            self.growth_time=100
            self.weight=50
            self.fertilizer="carrot_fertilizer"
            self.pic_path="assets/Carrot.png"
        
        if species=="beetroot":
            self.growth_time=200
            self.weight=200
            self.fertilizer="beetroot_fertilizer"
            self.pic_path="assets/Beetroot.png"

        if species=="potato":
            self.growth_time=100
            self.weight=100
            self.fertilizer="potatoe_fertilizer"
            self.pic_path="assets/Potato.png"

        else:
            self.growth_time=250
            self.weight=75
            self.fertilizer="wheat_fertilizer"
            self.pic_path="assets/Wheat.png"

        self.image = pygame.image.load(self.pic_path) #zmienic
        self.image = pygame.transform.scale(self.image,(36,36))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        



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

for line in range(25):
            pygame.draw.line(background, (0, 0, 0), (0, line * 36), (SIZE[0], line * 36))
            pygame.draw.line(background, (0, 0, 0), (line * 36, 0), (line * 36, SIZE[1]))

# size in pixels of one tile = 36px/36px
tile = (36, 36)

# later move it to another class "barn"?
barn_img = pygame.image.load('assets/barn.png')
barn = pygame.transform.scale(barn_img, tile) 

#Tractor
tractor = Tractor('oil','manual')
tractor_group = pygame.sprite.Group()
tractor_group.add(tractor)

#PLANTS
plant_grup = pygame.sprite.Group()
for plant in range(30):
     new_plant = Plant(random.choice(SPECIES),0,random.randrange(0,screen_width),random.randrange(0,screen_height))
     plant_grup.add(new_plant)

if __name__ == "__main__":
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 tractor.collect()
            
        pygame.display.flip()
        screen.blit(background,(0,0))
        plant_grup.draw(screen)
        tractor_group.draw(screen)
        tractor_group.update()
        clock.tick(60)
        
