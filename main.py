import psycopg2
import matplotlib.pyplot as plt
username = 'postgres'
password = '3220'
database = 'test_DB'
host = 'localhost'
port = '5432'

a = """select player_height from players;"""



b = """Select TRIM(team_name), count(*) from (Select  * from players
                                join teams
                                using(team_id)) as joined_table
group by team_name;"""


c = "select age, pts from players;"

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

#first part of plotting

print("first query")
with con:
    cur = con.cursor()
    cur.execute(a)
    for row in cur:
        print(row)

with con:
    cur = con.cursor()
    cur.execute(b)
    for row in cur:
        print(row)

with con:
    cur = con.cursor()
    cur.execute(c)
    for row in cur:
        print(row)
