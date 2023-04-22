from cmath import sqrt


screen_width=936
screen_height=936
SIZE = (screen_width, screen_height)
SPECIES=["carrot","potato","beetroot","wheat"]
# size in pixels of one tile = 36px/36px
tile = (36, 36)
block_size = 36
road_coords = [0, 5, 10, 15, 20, 25]
field_width = 4
field_height = 4
field_size = field_width*field_height
fields_amount = 26

directions = {0: 'UP', 90: 'RIGHT', 180: 'DOWN', 270: 'LEFT'}