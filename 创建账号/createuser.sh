#!/bin/bash
if [ $# != 1 ];then
    echo "give a list"
elif [ -f $1 ];then
    cat $1 | while read -r name password
    do 
        echo -e "$name\t$password"
	useradd $name
        echo $password | passwd --stdin $name
    done
else
    echo "give a list"
fi
