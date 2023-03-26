import pygame



class Tractor(pygame.sprite.Sprite):
    def __init__(self,engine,transmission,fuel,fertilizer):
        super().__init__()
        self.image=pygame.image.load("assets/tractor/tractor.png")
        self.image=pygame.transform.scale(self.image,(36,36))
        self.UP = pygame.transform.rotate(self.image, 0)
        self.DOWN = pygame.transform.rotate(self.image, 180)
        self.LEFT = pygame.transform.rotate(self.image, 90)
        self.RIGHT = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()

        self.engine=engine
        self.transmission=transmission
        self.fuel=fuel
        self.fertilizer=fertilizer

    def movement(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.x>0:
                self.image = self.LEFT
                self.rect.x -= 36 
        if keys[pygame.K_RIGHT] and self.rect.x<900:
                self.image = self.RIGHT
                self.rect.x += 36
        if keys[pygame.K_UP] and self.rect.y>0:
                self.image = self.UP
                self.rect.y -= 36
        if keys[pygame.K_DOWN] and self.rect.y<900:
                self.image = self.DOWN
                self.rect.y += 36
                
    def collect(self,plant_group):
        self.plant_group=plant_group
        print("collected plant")
        pygame.sprite.spritecollide(self,self.plant_group,True)
        #  collected=collected+1
        #  print("plants in trunk "+collected)
        
    def water_plant(self,plant_group):
        self.plant_group=plant_group
        print("watered plant")
    # def update(self):
    #     self.rect.center=pygame.mouse.get_pos()
    
    def fertilize(self, plant_group):
        self.plant_group=plant_group
        print("fertilize")
        
    def plant(self, plant_group):
        self.plant_group=plant_group
        print("new plant")
        
    def find_nearest_plant(self,plant_group):
        self.plant_group=plant_group
        