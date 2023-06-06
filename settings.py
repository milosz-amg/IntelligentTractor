from cmath import sqrt
import pygame


screen_width = 1368
screen_height = 936

SIZE = (screen_width, screen_height)

SPECIES=["carrot","potato","wheat"]
WEATHER=['slonce','wiatr','snieg','deszcz']

# size in pixels of one tile = 36px/36px
tile = (36, 36)
block_size = 36
road_coords = [0, 5, 10, 15, 20, 25]
field_width = 4
field_height = 4
field_size = field_width*field_height
fields_amount = 25

directions = {0: 'UP', 90: 'RIGHT', 180: 'DOWN', 270: 'LEFT'}

def draw_lines_on_window(background):
    for line in range(26):
        pygame.draw.line(background, (0, 0, 0), (0, line * block_size), (936, line * block_size))
        pygame.draw.line(background, (0, 0, 0), (line * block_size, 0), (line * block_size, screen_height))
        
    pygame.draw.line(background, (0, 0, 0), (968, 285), (1336 , 285))
    pygame.draw.line(background, (0, 0, 0), (968, 649), (1336 , 649))
    pygame.draw.line(background, (0, 0, 0), (968, 285), (968, 649))
    pygame.draw.line(background, (0, 0, 0), (1336, 285), (1336, 649))