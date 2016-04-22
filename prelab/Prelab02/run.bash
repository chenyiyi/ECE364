#! /bin/bash
#
#$Author: ee364f04 $ Yiyi Chen
#$Date: 
#$Revision:  
#$HeadURL: 
#$Id: 

Num_Of_Param=$#
Param_Values=$@
pro=(a i)
fastest=(0 0 0 5000)

if (( $#!=2 ))
then 
    echo "Usage: yards.bash <filename>"
    exit 2
elif [[ ! -e $1 ]]
then 
    echo "Error: $1 is not readable"
    exit 2
elif ! gcc $1 -o quick_sim
then 
    echo "Error: quick_sim could not be compiled!"
else
    if [[ -e $2 ]]
    then
	echo -n "$2 exitst. Would you like to delete it? " 
	read nu
	if [[ $nu = "y" || $nu = "yes" ]]
	then
	    exec 4> $2
	else
	    echo -n "Enter a new filename: "
	    read newfile
	    exec 4> $newfile
	fi	    
    fi

    for (( cache = 1; cache <33 ; cache=$cache*2 ))
    do 
	for (( issue = 1; issue < 17; issue=$issue*2 ))
	do 
	    for p in ${pro[*]}
	    do
		out=$(quick_sim $cache $issue $p)
		IFS=:
		set $out
		if [[ "$p" = "a" ]]
		then
		    echo "$2:$4:$6:$8:${10}" >&4
		else
		    echo "$2:$4:$6:$8:${10}" >&4 
		fi
		if (( ${fastest[3]} > ${10} ))
		then
		    fastest[0]=$2
		    fastest[1]=$4
		    fastest[2]=$6
		    fastest[3]=${10}
		fi		    
	    done
	done
    done
    echo "Fastest run time achived by ${fastest[0]} with cache size ${fastest[1]} and issue width ${fastest[2]} was ${fastest[3]} "
fi