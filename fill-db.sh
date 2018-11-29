#!/bin/bash
set -e

sqlite3 $1 ".import Professions-$lang.list Professions"
sqlite3 $1 "select * from Professions"

sqlite3 $1 ".import Items-$lang.list Items"
sqlite3 $1 "select * from Items"

sqlite3 $1 ".import Credits.list Credits"
