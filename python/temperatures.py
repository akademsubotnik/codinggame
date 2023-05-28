#Write a program that prints the temperature closest to 0 among input data. 
#If two numbers are equally close to zero, positive integer has to be considered closest to zero 
#(for instance, if the temperatures are -5 and 5, then display 5).

#Passes 5/5 test cases 
#Translated from previous bash correct answer by AI you.com

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
    exit()
else:
    closestToZero=myList[0]

for i in myList:
    # Handle i == -i
    if i == closestToZero * -1:
        if i < 0:
            continue
        else:
            closestToZero = i

    # Handle i < 0
    if i < 0:
        if closestToZero < 0:
            if closestToZero > i:
                continue
            else:
                closestToZero = i
        else:
            i = i * -1
            if i > closestToZero:
                continue
            else:
                closestToZero = i * -1
    #Handle i greater than 0
    if i  < closestToZero:
        closestToZero=i

print(closestToZero)
#print("result")
