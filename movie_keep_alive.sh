#!/bin/bash
count=0
limit=12

while true ; do
    count=$(( count + 1 ));
    random_x=$(( ( RANDOM % 1000 )  + 1 ));
    random_y=$(( ( RANDOM % 1000 )  + 1 ));
    echo "moved the mouse to $random_x and $random_y"
    xdotool mousemove $(( $random_x )) $(( $random_y ));
    sleep $(( 5 * 60 ));
    if [ $count -eq $limit ]; then
        break;
    fi
done
