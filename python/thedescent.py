#This code passes tests 2/5, it assumes that the mountains will fall after being shot 1x.  The other 3/5 cases a mountain requires 
#multiple shots to fall
#Bubblesort written by AI you.com

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

def bubble_sort_dict(my_dict):
    # Convert dictionary to list of tuples
    my_list = list(my_dict.items())

    # Sort list using bubble sort
    n = len(my_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j][1] < my_list[j+1][1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    # Convert sorted list back to dictionary
    sorted_dict = {}
    for item in my_list:
        sorted_dict[item[0]] = item[1]

    #print(sorted_dict)

    for k in sorted_dict:
        print(k)
    #return sorted_dict


# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        add_element(mh,i,mountain_h)
    bubble_sort_dict(mh)
    #print(smh)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    
    print("4")
