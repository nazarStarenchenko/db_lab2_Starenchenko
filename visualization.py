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
number_lst = []
with con:
    cur = con.cursor()
    cur.execute(a)
    for row in cur:
        print(row)
        number_lst.append(row[0])


plt.hist(number_lst, width = 2)
plt.title("height of players in cm")
plt.grid()
plt.show()

#second part of plotting
print("\nsecond query")
team_lst = []
number_lst = []
with con:
    cur = con.cursor()
    cur.execute(b)
    for row in cur:
        print(row)
        team_lst.append(row[0])
        number_lst.append(row[1])

plt.pie(number_lst, labels=team_lst)
plt.title("number of players in different teams")
plt.show()


#third part of plotting
print("\nthird query")
x_lst = []
y_lst = []
with con:
    cur = con.cursor()
    cur.execute(c)
    for row in cur:
        print(row)
        x_lst.append(row[0])
        y_lst.append(row[1])

plt.plot(sorted(x_lst), sorted(y_lst))
plt.grid()
plt.title("realtion between age and points of players")
plt.xlabel("age")
plt.ylabel("points")
plt.show()


