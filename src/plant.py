from pygame.sprite import Sprite

class Plant(Sprite):
    def __init__(self,species,location,is_ill,pic_path):
        super.__init__()
        self.species=species
        self.location=location
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

        if species=="wheat":
            self.growth_time=250
            self.weight=75
            self.fertilizer="wheat_fertilizer"
            self.pic_path="assets/Wheat.png"
        
    