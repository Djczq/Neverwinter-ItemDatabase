#!/bin/bash
set -e

sqlite3 $1 "drop table images"
sqlite3 $1 "create table images(iblob blob)"
echo "insert into  images (iblob) values(x'$(hexdump -v -e '1/1 "%02x"' $2)')" | sqlite3 $1

sqlite3 $1 ".dump"


sqlite3 $1 "select * from images"
