select player_height from players;


Select TRIM(team_name), count(*) from (Select  * from players
                                join teams
                                using(team_id)) as joined_table
group by team_name;


select age, pts from players;