#Write a program that prints the temperature closest to 0 among input data. 
#If two numbers are equally close to zero, positive integer has to be considered closest to zero 
#(for instance, if the temperatures are -5 and 5, then display 5).

#Passes 1/4 test cases - checking if no temperature is passed

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

negativeFlag="false"
closestToZero=0
myList = []

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    myList.append(t)

    #print(myList)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#Handle Empty Array
if len(myList) == 0 :
    print(closestToZero)
else:
    closestToZero=myList[0]

#print("result")
