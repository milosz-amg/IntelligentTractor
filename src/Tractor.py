import pygame
from settings import block_size, tile

mx=0
my=0

class Tractor(pygame.sprite.Sprite):
    def __init__(self, engine, transmission, fuel, fertilizer, capacity):
        super().__init__()
        self.image = pygame.image.load("assets/tractor/tractor.png")
        self.image = pygame.transform.scale(self.image, tile)
        self.rect = self.image.get_rect()  
        
        self.up = pygame.transform.rotate(self.image, 0)
        self.down = pygame.transform.rotate(self.image, 180)
        self.left = pygame.transform.rotate(self.image, 90)
        self.right = pygame.transform.rotate(self.image, -90)
        
        self.rect.x = 0
        self.rect.y = 0
        self.direction = 'F'
        self.rotation = 90

        self.collected = 0
        self.capacity = capacity
        self.engine = engine
        self.transmission = transmission
        self.fuel = fuel
        self.fertilizer = fertilizer
        
        

    def movement_using_keys(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.movement('L')
        if keys[pygame.K_RIGHT]:
            self.movement('R')
        if keys[pygame.K_UP]:
            self.movement('F')
        
        #waits between moves to avoid moving to fast
        pygame.time.wait(30) 
    
    def move_forward(self):
        if self.rect.y > 0 and self.rotation == 0:
            self.rect.y -= block_size
        if self.rect.x < 900 and self.rotation == 90:
            self.rect.x += block_size
        if self.rect.y < 900 and self.rotation == 180:
            self.rect.y += block_size
        if self.rect.x > 0 and self.rotation == 270:
            self.rect.x -= block_size
        
    
    def move_left(self):
        self.rotation -= 90
        if self.rotation < 0:
            self.rotation = 270
            
    def move_right(self):
        self.rotation += 90
        if self.rotation >= 360:
            self.rotation = 0
            
    def check_rotation(self):
        if self.rotation == 0:
            self.image = self.up
        elif self.rotation == 90:
            self.image = self.right
        elif self.rotation == 180:
            self.image = self.down
        elif self.rotation == 270:
            self.image = self.left
            
    def movement(self, direction):
        print(int((self.rect.x-18)/36),';',int((self.rect.y-18)/36))
        if direction == 'F':
            self.move_forward()
        elif direction == 'L':
            self.move_left()
        elif direction == 'R':
            self.move_right()
            
        self.check_rotation()
                
    def collect(self, plant_group):
        if self.collected <= self.capacity:
            self.plant_group=plant_group
            # print("collected plant")
            pygame.sprite.spritecollide(self, self.plant_group, True)
            self.collected += 1
             #  print("plants in trunk "+collected)
        
    def water_plant(self, plant_group):
        self.plant_group = plant_group
        print("watered plant")
    
    def fertilize(self, plant_group):
        self.plant_group = plant_group
        print("fertilize")
        
    def plant(self, plant_group):
        self.plant_group = plant_group
        print("new plant")
        
    def find_nearest_plant(self, plant_group):
        self.plant_group = plant_group
        