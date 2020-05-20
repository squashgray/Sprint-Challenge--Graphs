from room import Room
from player import Player
from world import World

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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
 

s = Stack()
s.push(player.current_room.id) 



visited = dict() 
path = [] 
reverse = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}



visited[player.current_room.id] = player.current_room.get_exits()  



while len(visited) < len(room_graph):
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()
        current_move = path[-1]
        visited[player.current_room.id].remove(current_move)
    if len(visited[player.current_room.id]) == 0:
        current_move = path[-1]
        path.pop()
        traversal_path.append(current_move)
        player.travel(current_move)
    else:
        next_travel = visited[player.current_room.id][-1]
        visited[player.current_room.id].pop() 
        player.travel(next_travel) 
        path.append(reverse[next_travel])
        traversal_path.append(next_travel)




# while len(visited) < len(room_graph) - 1: 
#     v = s.pop()
#     print("stack",s.stack)
#     print("v", visited)
#     if v not in visited:
#         print("ghgh",v)
#         visited.add(v) 
#         for direction in player.current_room.get_exits(): 
#             player.travel(direction)
#             traversal_path.append(direction)
#             direction = player.current_room.id
#             visited.add(direction) 
#             print("d", direction)
#             s.push(direction) 


# entries[player.current_room.id] = room_graph[player.current_room.id][1]
# entries[player.current_room.id] = { i: '?' for i in player.current_room.get_exits() }

# while len(entries) <  2:
#     new_stack = stack.pop()
#     prev_room = player.current_room.id
#     if new_stack not in entries:
#         entries[new_stack] = { i: '?' for i in player.current_room.get_exits() }
#         for direction in player.current_room.get_exits():
#             print('s', stack)
#             print('d', direction)
#             player.travel(direction)
#             print(f'this is where im at {player.current_room.id}')
#             traversal_path.append(direction)
#             entries[new_stack][direction] = player.current_room.id
#             # print(entries[new_stack])
#             stack.append(player.current_room.id)
#             # print(entries)
#             print(traversal_path)
        


# TRAVERSAL TEST - DO NOT MODIFY
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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
