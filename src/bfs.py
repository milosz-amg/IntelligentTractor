import heapq
from settings import block_size, screen_width, directions
import copy
from src.map import get_cost_by_type, get_type_by_position, return_fields_list

fields = return_fields_list()

class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h
    
    def f(self):
        return self.g + self.h
    
    def __lt__(self, other):
        return self.f() < other.f()

class Astar:
    def __init__(self):
        self.fringe = [] 
        self.explored = [] 
    
    def successor(self, state):
        pos_x, pos_y, rotation = state
        options = []
        cost = get_cost_by_type(get_type_by_position(fields, pos_x, pos_y))
        
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
                options.append((a, s, cost))
        
        return options
    
    def valid_state(self, state):
        pos_x, pos_y, rotation = state
        if pos_x < 0 or pos_x >= screen_width or pos_y < 0 or pos_y >= screen_width:
            return False
        return True
    
    def heuristic(self, state, goal):
        return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
        
    def goal_path(self, elem):
        path = []
                
        while elem.parent: 
            path.append([elem.action, elem.state[0], elem.state[1]])
            elem = elem.parent

        return path

    def search(self, istate, goaltest):
        x, y, rotation = istate
        start_node = Node((x, y, rotation), None, None, 0, self.heuristic(istate, goaltest))

        heapq.heappush(self.fringe, (start_node.f(), start_node))

        while True:
            if len(self.fringe) == 0:
                return False

            _, elem = heapq.heappop(self.fringe)

            if elem.state[0] == goaltest[0] and elem.state[1] == goaltest[1]:
                return self.goal_path(elem)

            self.explored.append(elem.state)

            for (action, state, cost) in self.successor(elem.state):
                if state not in self.explored:
                    g = elem.g + cost  # cost to move from parent node to current node is based on the field type.
                    h = self.heuristic(state, goaltest) # manhattan distance cost
                    x = Node(state, elem, action, g, h) #creating the node and pushing it into fringe
                    heapq.heappush(self.fringe, (x.f(), x))


