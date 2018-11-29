#!/bin/bash

if [ $# -ne 2 ]
then
	echo Error : wrong number of parameters !
	exit
fi


db=$1
file=$2

checkItemExist(){
	if [ $# -ne 2 ]
	then
		echo Error : checkItemExist : wrong number of parameters !
		exit
	fi
	db=$1
	name=$2
	res=$(sqlite3 $db "select * from Items where text = \"$name\"")
	if [ "$res" = "" ]
	then
		echo 0
	else
		echo 1
	fi
}

putItemDB(){
	if [ $# -ne 2 ]
	then
		echo Error : putItemDB : wrong number of parameters !
		exit
	fi
	db=$1
	name=$2
	sqlite3 $db "insert into Items(text) values (\"$name\")"
}


while read -r line || [[ -n "$line" ]]
do
	res=$(checkItemExist $db "$line")
	if [ $res -eq 0 ]
	then
		putItemDB $db "$line"
		echo $line
	fi
done < <(cat $file | tr -d "#+:[:digit:]" | sed -e 's/^\s*//g;s/\s*$//g' | sort -u)

sqlite3 $db "select * from Items"

