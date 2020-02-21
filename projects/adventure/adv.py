from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    
# def get_neighbors(exit):
#     """
#     Get all neighbors (edges) of a vertex.
#     """
#     p = {}
#     return p['exit']

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# -------------------------------------

# player is the Node 
# rooms are the Edges
# (0 - 500)

traversal_path = []
visited = []
paths = ['n', 's', 'e', 'w']
# paths = ['n', 's', 'e', 'w']

# room = Room()

def explore_all(starting_point):
    s = Stack()
    s.push(starting_point)
    if s.size() > 0:
        v = s.pop()
        if v not in visited:
            visited.append(v)
            for path in world.rooms:
                # traversal_path.append(paths[0])
                # visited.append(starting_point)
                traversal_path.append(random.choice(paths))
                # if room.get_exits() == None:
                #     s.pop()
                if world.rooms.values() != '?':
                    s.push((random.choice(paths)))
    
    return traversal_path

explore_all('e')
print(traversal_path)
# print(world.rooms.keys())
        
        

# use DST to pick a unvisted direction from players room
# for path in traval_path
    # pick unvisted direction (n/s/e/w)
    # player.travel into room 
    # add it to visted
    # if unvisted direction is none
        # player.travel to nearest unvisted room

# use BFS to search for the shortest unvisted room
# searching for an exit with a `'?'` as the value
#  if exit is in visted
    # add exit to the queue  

# convert dict of rooms to a list of n/s/e/w
# add to traversal_list
# if all paths explored, done


# -------------------------------------
        
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
