import pygame


class Tractor(pygame.sprite.Sprite):
    def __init__(self,engine,transmission):
        super().__init__()
        self.image=pygame.image.load("assets/tractor/tractor.png")
        self.image=pygame.transform.scale(self.image,(36,36))
        self.rect = self.image.get_rect()

        self.engine=engine
        self.transmission=transmission
        self.fuel=100
    
    def collect(self,plant_group):
         self.plant_group=plant_group
         print("collected plant")
         pygame.sprite.spritecollide(self,self.plant_group,True)
        #  collected=collected+1
        #  print("plants in trunk "+collected)

    def update(self):
        self.rect.center=pygame.mouse.get_pos()
