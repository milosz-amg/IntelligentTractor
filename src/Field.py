from pygame.sprite import Sprite   
from src.Plant import Plant

class Field(Sprite):    
    def __init__(self, type, x, y, image, cost, hydration_level , soil,
                 fertilizer_degree, development_degree, plant_type, fertilizer_type, to_water, plantObj):
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
        self.plantObj = plantObj

    def getPlantObj(self):
        return self.plantObj

    def setPlantObj(self,newPlant):
        self.plantObj=newPlant

