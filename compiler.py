import psycopg2 as pg2

con = pg2.connect(database='rankings', user='isdb')
con.autocommit = True
cur = con.cursor()

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    for row in rows:
        print(row)


populate = cur.mogrify('''

		INSERT INTO teams (country, name, points)
		   SELECT country1, team1, 0
		     FROM firstCL1415
		    WHERE NOT EXISTS (SELECT name
		                        FROM teams
		                       WHERE name = team1)
		    GROUP by country1, team1;
		
		INSERT INTO teams (country, name, points)
		   SELECT country2, team2, 0
		     FROM firstCL1415
		    WHERE NOT EXISTS (SELECT name
		                        FROM teams
		                       WHERE name = team2)
		    GROUP by country2, team2;




	''')

cur.execute(populate)

#cmd = cur.mogrify('''
#		SELECT *
#		  FROM firstCL1415;
#	''')
#print_cmd(cmd)
#cur.execute(cmd)
#rows = cur.fetchall()
#print_rows(rows)

points = cur.mogrify('''
		UPDATE teams
		   SET points = points + 1
		 WHERE name IN (SELECT team1 FROM firstCL1415 WHERE score1 > score2);

		UPDATE teams
		   SET points = points + 1
		 WHERE name IN (SELECT team2 FROM firstCL1415 WHERE score2 > score1);
	''')

cur.execute(points)

pop2 = cur.mogrify('''
		INSERT INTO rankings (abbrev, country, num, points)
			SELECT c.abbrev, c.country, count(t.country), sum(t.points)
			  FROM countries as c
			  	JOIN teams as t on c.abbrev = t.country
			 WHERE NOT EXISTS (SELECT abbrev, country
			 					 FROM rankings
			 					WHERE abbrev = c.abbrev and country = c.country)
			 GROUP by c.abbrev, c.country;
	''')

cur.execute(pop2)

change = cur.mogrify('''
	UPDATE rankings
	   SET points = 
	 WHERE abbrev = (SELECT r.country FROM teams as t JOIN rankings as r ON r.abbrev = t.country WHERE )
	''')

display = cur.mogrify('''
    SELECT *
      FROM teams
	''')

#cur.execute(display)
#rows1 = cur.fetchall()
#print_rows(rows1)

display2 = cur.mogrify('''
	SELECT *
	  FROM rankings;
	''')

cur.execute(display2)
rows2 = cur.fetchall()
print_rows(rows2)