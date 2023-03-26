from pygame.sprite import Sprite   

class Field(Sprite):    
    def __init__(self, type, row_id, col_id, image, cost, hydration_level , soil,
                 fertilizer_degree, development_degree, plant_type, fertilizer_type, to_water):
    
        self.type = type
        self.row_id = row_id
        self.col_id = col_id
        self.position = (row_id, col_id)
        self.image = image
        self.cost = cost

        self.hydration_level = hydration_level 
        self.soil = soil
        self.fertilizer_degree = fertilizer_degree
        self.development_degree = development_degree
        self.plant_type = plant_type
        self.fertilizer_type = fertilizer_type
        self.to_water = to_water

