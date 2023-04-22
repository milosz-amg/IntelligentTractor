from settings import block_size, screen_width, directions


class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

class BFS:
    def __init__(self):
        self.fringe = [] 
        self.explored = [] 
    
    def successor(self, state):
        pos_x, pos_y, rotation = state
        options = []
        
        if rotation == directions[0]:
            states = [(pos_x, pos_y - block_size, directions[0]), (pos_x, pos_y, directions[270]), (pos_x, pos_y, directions[90])]
            actions = ['F', 'L', 'R']
        elif rotation == directions[90]:
            states = [(pos_x + block_size, pos_y, directions[90]), (pos_x, pos_y, directions[0]), (pos_x, pos_y, directions[180])]
            actions = ['F', 'L', 'R']
        elif rotation == directions[180]:
            states = [(pos_x, pos_y + block_size, directions[180]), (pos_x, pos_y, directions[90]), (pos_x, pos_y, directions[270])]
            actions = ['F', 'L', 'R']
        elif rotation == directions[270]:
            states = [(pos_x - block_size, pos_y, directions[270]), (pos_x, pos_y, directions[0]), (pos_x, pos_y, directions[180])]
            actions = ['F', 'L', 'R']
            
        for s, a in zip(states, actions):
            if self.valid_state(s):
                options.append((a, s))
        
        return options
    
    def valid_state(self, state):
        pos_x, pos_y, rotation = state
        if pos_x < 0 or pos_x >= screen_width or pos_y < 0 or pos_y >= screen_width:
            return False
        return True
        
    def search(self):
        pass
