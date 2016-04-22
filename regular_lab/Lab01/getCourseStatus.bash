#! /bin/bash
#
#$Author: ee364f04 $ Yiyi Chen
#$Date: 2016-01-25 15:40:43 -0500 (Mon, 25 Jan 2016) $
#$Revision: 86749 $ 
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364f04/Lab01/getCourseStatus.bash $ 
#$Id: getCourseStatus.bash 86749 2016-01-25 20:40:43Z ee364f04 $ A combination of the above keywords

Num_Of_Param=$#
Param_Values=$@

sum=0
max=0
num=0
avg=0
grade=0
stu=0


if (( $#!=1 ))
then
    echo "Usage : ./getCourseStatus.bash <filename>"
    exit 1
fi

if [[ $1 != "ece364" && $1 != "ece337" && $1 != "ece468" ]]
then
    echo "course $1 is not a valid option"
    exit 5
fi

for temp in $(ls gradebooks/$1*)
do
    getFinalScores.bash $temp
    if (( $? != 0 ))
    then
	echo "Erro while running getFinalScores.bash"
	exit 3
    fi
    output=$(echo $temp | cut -d '.' -f1)
    output+=".out"
    while read student
    do 
	((num=$num+1))
	((grade=$(echo $student | cut -d ',' -f2)))
	((sum=$sum+$grade))
	((avg=$sum/$num))
	if (($grade>$max))
	then
	    max=$grade
	    stu=$(echo $student | cut -d ',' -f1)
	fi
    done<$output
done
echo "Total students: $num"
echo "Average score: $avg"
echo "$stu had the highest score of $max"

exit 0
