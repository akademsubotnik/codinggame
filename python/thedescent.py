import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

mh = {}
smh = {}
listL = []

def add_element(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)

def sort(dict):
    #print(dict)
    smh = sorted(dict.items(),reverse=True)
    print(smh)

def fire(dict):
    for values in smh.values():
        print(values)

# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        add_element(mh,mountain_h,i)
    sort(mh)
    #print(smh)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    
    print("4")
