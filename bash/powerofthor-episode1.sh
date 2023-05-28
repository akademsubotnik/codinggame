#Your program must allow Thor to reach the light of power.
# 	Rules
#Thor moves on a map which is 40 wide by 18 high. Note that the coordinates (X and Y) start at the top left! 
#This means the most top left cell has the coordinates "X=0,Y=0" and the most bottom right one has the coordinates "X=39,Y=17".

#Once the program starts you are given:
#the variable lightX: the X position of the light of power that Thor must reach.
#the variable lightY: the Y position of the light of power that Thor must reach.
#the variable initialTX: the starting X position of Thor.
#the variable initialTY: the starting Y position of Thor.
#At the end of the game turn, you must output the direction in which you want Thor to go among:

#Passes 5/5 tests

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# initialTX: Thor's starting X position
# initialTY: Thor's starting Y position
read -r lightX lightY initialTX initialTY

# game loop
while true; do
    # remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
    read -r remainingTurns

    # Write an action using echo
    # To debug: echo "Debug messages..." >&2
    #echo $initialTX $initialTY >&2
    directionX=""
    directionY=""

    if [ $initialTY -gt $lightY ]; then
        directionY="N"
        initialTY=$((initialTY - 1))
    elif [ $initialTY -lt $lightY ]; then
        directionY="S"
        initialTY=$((initialTY + 1))
    fi

    if [ $initialTX -gt $lightX ]; then
        directionX="W"
        initialTX=$((initialTX - 1))
    elif [ $initialTX -lt $lightX ]; then
        directionX="E"
        initialTX=$((initialTX + 1))
    fi

    echo $directionY$directionX



    # A single line providing the move to be made: N NE E SE S SW W or NW
    #echo "SE"
done
