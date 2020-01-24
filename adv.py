from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# print("room graph", room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

class Transversal_Graph:
    def __init__(self):
        self.prev_room_id = 0
        self.rooms = {}
    
    def add_room(self, room_id):
        """
        Add a room to graph
        """

        if room_id not in self.rooms:
            valid_exit = {}
            for exit in player.current_room.get_exits():
                valid_exit[exit] = '?'
            self.rooms[room_id] = valid_exit
        else:
            print(f"{room_id} already exists.")
    
    def add_door(self, room_id, prev_room_id, direction):
        if room_id == prev_room_id:
            print("Cannot add a door to same room")
        else:
            #keep track of which direction traveled from prev room id?
            #if 's', then prev_room_id will be 'n' of current_room id
            if direction == 'n':
                graph.rooms[prev_room_id][direction] = room_id
                graph.rooms[room_id]['s'] = prev_room_id
            if direction == 's':
                graph.rooms[prev_room_id][direction] = room_id
                graph.rooms[room_id]['n'] = prev_room_id
            if direction == 'e':
                graph.rooms[prev_room_id][direction] = room_id
                graph.rooms[room_id]['w'] = prev_room_id
            if direction == 'w':
                graph.rooms[prev_room_id][direction] = room_id
                graph.rooms[room_id]['e'] = prev_room_id
        
    def create_graph(self):
        prev_room_id = self.prev_room_id
        #create first room
        self.add_room(player.current_room.id)
        #get possible directions of the current room?
        while '?' in self.rooms[player.current_room.id].values():
            possible_dir = []
            for k,v in self.rooms[player.current_room.id].items():
                if v is '?':
                    possible_dir.append(k) 

        #pick one with '?' at random
            direction = random.choice(possible_dir)
        #go to that room, keeping track of direction.
            player.travel(direction)
        #add room, then add door
            self.add_room(player.current_room.id)
            self.add_door(player.current_room.id, prev_room_id, direction)
            #set prev room id to current
            prev_room_id = player.current_room.id
            print("prev room id", prev_room_id)
            

graph = Transversal_Graph()
graph.create_graph()
print("graph dict", graph.rooms)
# graph.add_room(player.current_room.id)
# direction = 'w'
# print("graph at current room", graph.rooms[player.current_room.id][direction])
# player.travel(direction)
# print("current room ID", player.current_room.id)
# graph.add_room(player.current_room.id)
# print("graph at current room", graph.rooms[player.current_room.id])
# graph.add_door(player.current_room.id, graph.prev_room_id, direction)
# print("graph at current room", graph.rooms[player.current_room.id])
# print("graph at prev room", graph.rooms[graph.prev_room_id])

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
