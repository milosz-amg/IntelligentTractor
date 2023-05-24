from pygame.sprite import Sprite   

class Road(Sprite):    
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.type='Road'
        self.cost=200