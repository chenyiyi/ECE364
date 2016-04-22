#! /bin/bash
#
#$Author: ee364f04 $ Yiyi Chen
#$Date: 2016-01-25 15:40:43 -0500 (Mon, 25 Jan 2016) $
#$Revision: 86749 $ 
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f04/Lab01/getFinalScores.bash $ 
#$Id: getFinalScores.bash 86749 2016-01-25 20:40:43Z ee364f04 $ A combination of the above keywords

Num_Of_Param=$#
Param_Values=$@

sum=0

file=$(echo $1 | cut -d '.' -f1)
file+=".out"

if (( $#!=1 ))
then
    echo "Usage : ./getStudentData.bash <filename>"
    exit 1
elif [[ -e $file ]]
then
    echo "Ouput file $file already exits"
    exit 3
elif [[ ! -e $1 ]]
then 
    echo "Error reading input file: $1"
    exit 2
else 
    exec 4> $file
    cat $1 | while read student
    do 
     	((sum=$sum+15*$(echo $student | cut -d ',' -f2)/100))
	((sum=$sum+30*$(echo $student | cut -d ',' -f3)/100))
	((sum=$sum+30*$(echo $student | cut -d ',' -f4)/100))
	((sum=$sum+25*$(echo $student | cut -d ',' -f5)/100))
	name=$(echo $student | cut -d ',' -f1)
	echo "$name,$sum" >&4
	sum=0
    done
fi

exit 0
