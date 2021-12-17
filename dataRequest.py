def sortByDate_game(cur):
    cur.execute('''
        select
            g.title,
            g.metacritic,
            date_part('year', g."release") as release_year
        from game g
        where
            g.metacritic = (
                select max(metacritic)
                from game
                where date_part('year', "release") = date_part('year', g."release")
            )
        order by release_year;''')

    return cur.fetchall()

def bad_game(cur):

    cur.execute('''
        select title, metacritic, date_part('year', "release") as year from game where metacritic < 60 order by "release" ;''')

    return cur.fetchall()

def avg_game(cur):
    cur.execute('''
        select g.first_name, count(*) as nbre_jeux, avg(g.metacritic) as moyenne_score from (
            select * from game g
            inner join "user" u on u.id = addedby  
        ) as g
        group by g.first_name;''')

    return cur.fetchall()

def sort_genre(cur):
    cur.execute('''
        select b.name, count(*) from (select * from games_genres gg 
        inner join game g on g.id = game_id 
        inner join genre g2 on g2.id = genre_id ) as b
        group by b.name;''')

    return cur.fetchall()
        