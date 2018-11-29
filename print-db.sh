#!/bin/bash

sqlite3 $1 "
select Items.text, Credits.Credit, Credits.Credit1
from Items
    inner join Credits on Items.ItemID=Credits.ItemID
"
#sqlite3 $1 "select * from Items" | sed -e "s/|/;/g"
