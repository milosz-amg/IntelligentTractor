from settings import block_size, screen_width, directions
import copy


class Node:
    def __init__(self, state, parent=None, action=None):
        # Initializes a Node object with a state, parent (default None), and action (default None)
        self.state = state
        self.parent = parent
        self.action = action

class BFS:
    def __init__(self):
        # Initializes a BFS object with an empty fringe and an empty explored list
        self.fringe = [] 
        self.explored = [] 
    
    def successor(self, state):
        # Given a state, generates a list of possible (action, state) pairs for the next step
        pos_x, pos_y, rotation = state
        options = []
        
        if rotation == directions[0]:
            # If the current rotation is north-facing, generate possible next states and actions for each:
            states = [(pos_x, pos_y - block_size, directions[0]), (pos_x, pos_y, directions[270]), (pos_x, pos_y, directions[90])]
            actions = ['F', 'L', 'R']
        elif rotation == directions[90]:
            # If the current rotation is east-facing, generate possible next states and actions for each:
            states = [(pos_x + block_size, pos_y, directions[90]), (pos_x, pos_y, directions[0]), (pos_x, pos_y, directions[180])]
            actions = ['F', 'L', 'R']
        elif rotation == directions[180]:
            # If the current rotation is south-facing, generate possible next states and actions for each:
            states = [(pos_x, pos_y + block_size, directions[180]), (pos_x, pos_y, directions[90]), (pos_x, pos_y, directions[270])]
            actions = ['F', 'L', 'R']
        elif rotation == directions[270]:
            # If the current rotation is west-facing, generate possible next states and actions for each:
            states = [(pos_x - block_size, pos_y, directions[270]), (pos_x, pos_y, directions[0]), (pos_x, pos_y, directions[180])]
            actions = ['F', 'L', 'R']
            
        for s, a in zip(states, actions):
            # If a given state is valid (i.e. within the bounds of the screen), add it to the list of options
            if self.valid_state(s):
                options.append((a, s))
        
        return options
    
    def valid_state(self, state):
        # Returns True if a given state is valid (i.e. within the bounds of the screen), False otherwise
        pos_x, pos_y, rotation = state
        if pos_x < 0 or pos_x >= screen_width or pos_y < 0 or pos_y >= screen_width:
            return False
        return True
        
    def goal_path(self, elem):
        # Given a Node object, generates a list of (action, x-coordinate, y-coordinate) tuples representing the path to that Node
        path = []
                
        while elem.parent: 
            path.append([elem.action, elem.state[0], elem.state[1]])
            elem = elem.parent

        path = path[::-1]
        return path
    
    def search(self, istate, goaltest):
        # Create a start node with the initial state
        x, y, rotation = istate
        start_node = Node((x, y, rotation))

        # Add the start node to the fringe
        self.fringe.append(start_node)

        while True:
            # If there are no nodes left to explore, the goal cannot be reached
            if len(self.fringe) == 0:
                return False

            # Get the first node from the fringe
            elem = self.fringe.pop(0)

            # If the current node's state matches the goal state, return the path
            if elem.state[0] == goaltest[0] and elem.state[1] == goaltest[1]:
                return self.goal_path(elem)

            # Add the current node's state to the explored set
            self.explored.append(elem.state)

            # Expand the current node's successors
            for (action, state) in self.successor(elem.state):
                # Check if the successor state has not been explored yet
                if state not in self.explored:
                    # Create a new node with the successor state, and add it to the fringe
                    x = Node(state, elem, action)
                    self.fringe.append(x)