#! /bin/bash
#
#$Author: ee364f04 $ Yiyi Chen
#$Date: 
#$Revision:  
#$HeadURL: 
#$Id: 

Num_Of_Param=$#
Param_Values=$@
avg=0

if (( $#!=1 ))
then 
    echo "Usage: process_temps.bash <filename>"
    exit 1
elif [[ ! -e $1 || ! -r $1 ]]
then 
    echo "Error: $1 is not readable"
    exit 2
else
    while read line
    do
	time=($line)
	if [[ ${time[0]} != "time" ]]
	then
	    for (( i = 1; i < ${#time[*]}; i++ ))
	    do
		(( avg=$avg+${time[i]} ))	    
	    done
	    (( avg=$avg/(${#time[*]}-1) ))
	    echo "Average temperature for time ${time[0]} was $avg C."
	    avg=0
	fi
	done<$1
fi
