#!/bin/bash
set -e
rm -f $1

sqlite3 $1 "
CREATE TABLE languages(
	code varchar(5) not null primary key,
	name varchar(20)
);"

sqlite3 $1 "
CREATE TABLE professions(
	id integer not null primary key
);"

sqlite3 $1 "
CREATE TABLE professions_translation(
	id integer not null primary key,
	profession integer,
	name varchar(100),
	lang varchar(5),
	foreign key (lang) references languages(code),
	foreign key (profession) references professions(id)
);"

sqlite3 $1 "
CREATE TABLE items(
	id integer not null primary key,
	requiredLevel integer,
	sellPrice integer,
	buyPrice integer
);"

sqlite3 $1 "
CREATE TABLE production(
	id integer not null primary key,
	item integer,
	profession integer,
	commission integer,
	morale integer,
	time integer,
	foreign key (item) references items(id),
	foreign key (profession) references professions(id)
);"

sqlite3 $1 "
CREATE TABLE items_translation(
	id integer not null primary key,
	item integer,
	lang varchar(5),
	name varchar(100),
	desc varchar(1),
	foreign key (lang) references languages(code),
	foreign key (item) references items(id)
);"

sqlite3 $1 "
CREATE TABLE credits(
	id integer not null primary key,
	item integer,
	credit integer,
	credit1 integer,
	foreign key (item) references items(id)
);"

sqlite3 $1 "
CREATE TABLE materials(
	id integer not null primary key,
	item integer,
	material integer,
	quantity integer,
	foreign key (item) references items(id),
	foreign key (material) references items(id)
);"

sqlite3 $1 "
CREATE TABLE appearance(
	id integer not null primary key,
	day date,
	Item integer,
	foreign key (Item) references items(id)
);"


sqlite3 $1 ".dump"
