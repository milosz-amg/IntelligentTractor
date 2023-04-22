from settings import block_size, screen_width, directions
import copy


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
        
    def tempfunc(self, elem):
        path = []
                
        while elem.parent: 
            path.append([elem.action, elem.state[0], elem.state[1]])
            elem = elem.parent

        path = path[::-1]
        return path

    def search(self, istate, goaltest):
        node = Node([istate[0], istate[1], istate[2]])
        fringe = []
        fringe.append(node)
        fringe_states = [fringe[0].state]
        
        #fringe_state = [fringe[0].state]
        #visited = []
        explored_states = []
        
        while True:
            if not fringe:
                return False

            elem = fringe.pop(0)
            temp = copy.copy(elem)
            fringe_states.pop(0)
            
            # DESTINATION
            if elem.state[0] == goaltest[0] and elem.state[1] == goaltest[1]:
                return self.tempfunc(elem)

            explored_states.append(elem.state) #elem.state(?)

            for (action, state) in self.successor(temp):
                print
                if (state not in fringe_states) and (state not in explored_states):
                    x = Node([state[0][0], state[1], state[2]])
                    x.parent = elem
                    x.action = action
                    fringe.append(x)
                    fringe_states.append(x.state)
