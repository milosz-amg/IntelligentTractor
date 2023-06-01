from pygame.sprite import Sprite   
from src.Plant import Plant

class Field(Sprite):    
    def __init__(self, type, x, y, image, cost, hydration_level , soil,
                 fertilizer_degree, development_degree, plant_type, fertilizer_type, to_water, contain):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.position = (x, y)
        self.image = image
        self.cost = cost

        self.hydration_level = hydration_level 
        self.soil = soil
        self.fertilizer_degree = fertilizer_degree
        self.development_degree = development_degree
        self.plant_type = plant_type
        self.fertilizer_type = fertilizer_type
        self.to_water = to_water
        self.contain = contain

    def getContain(self):
        return self.contain

    def setContain(self,newPlant):
        self.contain=newPlant


