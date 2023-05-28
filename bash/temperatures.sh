#Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, 
#positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the number of temperatures to analyse
read -r n
read -r -a myArray
for (( i=0; i<$n; i++ )); do
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t=${myArray[$((i))]}
done

# Write an answer using echo
# To debug: echo "Debug messages..." >&2
negativeFlag="false"
closestToZero=0

#Handle Empty Array
if [ ${#myArray[@]} -eq 0 ]; then
    echo $closestToZero
    exit
else
    closestToZero=${myArray[0]}
fi


for i in ${myArray[@]}; do
    echo >&2 "Debug:  $i"

    #Handle i -eq --i
    if [ $i -eq $((closestToZero * -1)) ]; then
        if [ $i -lt 0 ]; then
            continue
        else
            closestToZero=$i
        fi
    fi

    #Handle i -lt 0
    if [ $i -lt 0 ]; then
        #i=$((i*-1))
        #echo >&2 "Debug:  $i"
        if [ $closestToZero -lt 0 ]; then
            if [ $closestToZero -gt $i ]; then
                continue
            else
                closestToZero=$i
            fi
        else
            i=$((i*-1))
            if [ $i -gt $closestToZero ]; then
                continue
            else
                closestToZero=$((i*-1))
            fi
        fi
        #if [ $((i*-1)) -gt $closestToZero ]; then
        #    continue
        #else
        #    closestToZero=$i
        #fi

    fi


    #Handle i greater than 0
    if [ $i  -lt $closestToZero ]; then
        closestToZero=$i
    fi
    
done

echo $closestToZero
