import psycopg2
import generate
from helpers import reset_database
from dataRequest import *
from createCsv import createCsv
from convertSQLtoNoSQL import game_table, user_table

with psycopg2.connect(dbname="library", user="postgres", password="didier", host="127.0.0.1", port="5432") as conn:
    with conn.cursor() as cur:

        # A chaque fois qu'on lance le script, on reset la base pour avoir les mêmes résultats
        reset_database(cur)

        # On ajoute 10 utilsateurs
        for i in range(10):
            cur.execute('insert into "user" (first_name, last_name) values (%s, %s);', generate.user())

        # On la joue safe et on recompte le nombre d'utilisateurs depuis la base pour plus tard
        cur.execute('select count(*) from "user";')
        # Ici on a un [0] car fetchone() renvoi toujours un tuple, même avec une seule valeur
        user_count = cur.fetchone()[0]

        # On ajoute 100 jeux
        for i in range(100):
            cur.execute('''
                insert into "game" (title, metacritic, pegi, release, addedby, added_at) values (%s, %s, %s, %s, %s, %s);''', generate.game())
        
        # on ajoute une dizaine de genres
        for i in range(10):
            cur.execute('insert into "genre" (name) values (%s);', generate.genre())

        # on lie les genres avec les jeux
        for i in range(160):
            cur.execute('insert into "games_genres" (game_id, genre_id) values (%s, %s);', generate.game_genre())
        # recuperation des requetes

        data1 = sortByDate_game(cur)
        createCsv(data1, 'stat', ['title','metacritic', 'date'])
        data2 = bad_game(cur)
        createCsv(data2, 'bad', ['title','metacritic', 'year'])
        data3 = avg_game(cur)
        createCsv(data3, 'avg', ['user','nbre_jeux', 'moyenne_jeux'])
        data4 = sort_genre(cur)
        createCsv(data4, 'genre', ['genre','nbre_jeux'])

        # conversion list en dictionnaire
        game_table(cur)
        user_table(cur)

        conn.commit()