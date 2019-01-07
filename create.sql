CREATE TABLE firstCl1415 (
	gid int,
	country1 varchar(40),
	team1 text,
	score1 int,
	country2 varchar(40),
	team2 varchar(40),
	score2 int
);

CREATE TABLE countries (
	abbrev varchar(40),
	country text
);

CREATE TABLE teams (
	country varchar(40),
	name text,
	points int
);

CREATE TABLE rankings (
	abbrev varchar(40),
	country text,
	num int,
	points int
);

CREATE TABLE final (
	abbrev varchar(40),
	country text,
	score float
);