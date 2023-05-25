import pygame
from settings import block_size

class Plant(pygame.sprite.Sprite):
    def __init__(self,wzrost,
                    wilgotnosc,
                    dni_od_nawiezienia,
                    aktualna_pogoda,
                    czy_robaczywa,
                    cena_sprzedarzy,
                    species,
                    pos_x,
                    pos_y):
        
        super().__init__()
        self.species=species
        self.wzrost=wzrost
        self.wilgotnosc=wilgotnosc
        self.dni_od_nawiezienia=dni_od_nawiezienia
        self.aktualna_pogoda=aktualna_pogoda
        self.czy_robaczywa=czy_robaczywa
        self.cena_sprzedarzy=cena_sprzedarzy
        if species=="carrot":
            self.growth_time=100
            self.weight=50
            self.min_hydration = 30
            self.max_hydration = 60
            self.soil_type = "torf"
            self.fertilizer="carrot_fertilizer"
            self.pic_path="assets/Carrot.png"
        
        elif species=="beetroot":
            self.growth_time=200
            self.weight=200
            self.min_hydration = 20
            self.max_hydration = 60
            self.soil_type = "piaszczyste"
            self.fertilizer="beetroot_fertilizer"
            self.pic_path="assets/Beetroot.png"

        elif species=="potato":
            self.growth_time=100
            self.weight=100
            self.min_hydration = 10
            self.max_hydration = 30
            self.soil_type = "ilaste"
            self.fertilizer="potatoe_fertilizer"
            self.pic_path="assets/Potato.png"

        else:
            self.growth_time=250
            self.weight=75
            self.min_hydration = 10
            self.max_hydration = 65
            self.soil_type = "gliniaste"
            self.fertilizer="wheat_fertilizer"
            self.pic_path="assets/Wheat.png"

        self.image = pygame.image.load(self.pic_path) #zmienic
        self.image = pygame.transform.scale(self.image,(block_size, block_size))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

def getParameters(self):
    return [self.species, self.wzrost, self.wilgotnosc, self.dni_od_nawiezienia,self.aktualna_pogoda,self.czy_robaczywa,self.cena_sprzedarzy]