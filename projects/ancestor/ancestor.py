# use DFT
# find nearest known ancestor
# if there is more than 1 ancestor tied for earliest, 
# return lowest numeric ID
# if no parents return -1

import sys
sys.path.append('../graph/')
from util import Stack

def get_neighbors(start_node):
    neighbors = []
    

def earliest_ancestor(ancestors, starting_node):
    ancestors = []
    
    # make a stack
    s = Stack()
    # push starting node onto stack
    s.push(starting_node)
    # make a set to track visited
    visited = set()
    # while stack is not empty
    while s.size() > 0:
        # pop off current node
        current_node = s.pop()
        # if we have not visted that vertex
        if current_node not in visited:
            # mark as visted
            visited.add(current_node)
            # get the neighbors
            neighbors = ancestors[current_node]
            # for each neightbor
            for neighbor in ancestors:
                # add to the stack
                s.push(neighbor)
        return 