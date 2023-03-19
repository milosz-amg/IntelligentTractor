from pygame.sprite import Sprite

class Plant(Sprite):
    def __init__(self,engine,transmission,pos_x,pos_y):
        super.__init__()
        self.engine=engine
        self.transmission=transmission
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.fuel=100
        

