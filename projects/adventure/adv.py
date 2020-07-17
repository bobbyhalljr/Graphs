from room import Room
from player import Player
from world import World
from graph import Graph

from queue import SimpleQueue
import random
from ast import literal_eval


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
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

# ******************* THE PLAN **********************

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

# ************************ start of code *********************************

# *********** trying for faster solution *********************

traversal_path = []
reversed_path = []
rooms = {}

# for backtracking
opposite_Directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# get exits in first room
rooms[0] = player.current_room.get_exits()

# while length of rooms is less than graph
while len(rooms) < len(room_graph) - 1:
    print("rooms: ", rooms, "\n\n", " room_graph: ", room_graph, "\n\n")
    # if current room.id not in rooms
    if player.current_room.id not in rooms:
        # get exits of room
        rooms[player.current_room.id] = player.current_room.get_exits()
        # get last item in list
        lastRoom = reversed_path[-1]
        rooms[player.current_room.id].remove(lastRoom)

    # while room is empty
    while len(rooms[player.current_room.id]) < 1:
        # pop off room from reverse list
        reverse = reversed_path.pop()
        # add to traversal list
        traversal_path.append(reverse)
        # travel through list
        player.travel(reverse)

    # get exits of room
    exit_dir = rooms[player.current_room.id].pop(0)
    # add exit to traversal_path
    traversal_path.append(exit_dir)
    # backtrack in opposite direction
    reversed_path.append(opposite_Directions[exit_dir])
    # travel in that direction
    player.travel(exit_dir)
    

# ************** brute force solution *******************

# traversal_path = []
# visited = []
# paths = ['n', 's', 'e', 'w']

# def explore_all(starting_point):
#     s = Stack()
#     s.push(starting_point)
#     while s.size() > 0:
#         v = s.pop()
#         if v not in visited:
#             visited.append(v)
#             for path in world.rooms:
#                 print(path)
#                 traversal_path.append(random.choice(paths))
#                 if player.current_room not in visited:
#                     s.push(path)
    
#     return traversal_path

# explore_all('n')
# print(traversal_path)
        


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
