#!/usr/bin/bash 

case $RULES in 
	8_balls)
		echo "Type of game chosen: 8 balls"
		;;
	9_balls)
		echo "Type of game chosen: 9 balls"
		;;
	pool)
		echo "Type of game chosen: pool"
		;;
	snooker)
		echo "Type of game chosen: snooker"
		;;

	*) 
	echo"Incorrect game mode choice! Please choose between: 8_balls, 9_balls, pool, snooker"

esac
