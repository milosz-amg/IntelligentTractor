import pygame

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
        