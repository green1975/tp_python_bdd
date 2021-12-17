import json
import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)

def parse_game(gametuple):
    (id, title, added_at, metacritic, pegi, release, addedby, genre) = gametuple
    return {
        '_id': id,
        'title': title,
        'added_at': added_at,
        'added_by': addedby,
        'infos': {
            'metacritic': metacritic,
            'pegi': pegi,
            'release': release,
            'genres': genre
        }
    }
def parse_user(usertuple):
    (id, first_name, last_name, created_at) = usertuple
    return {
        'id': id,
        'firstname': first_name,
        'last_name': last_name,
        'created_at': created_at
    }

def game_table(cur):
    cur.execute('''SELECT 
    game.id,
    title, 
    added_at, 
    metacritic, 
    pegi, 
    release, 
    addedby,
    ARRAY_AGG (g."name" ) genre
    FROM game
    left JOIN games_genres gg on id = gg.game_id 
    left JOIN genre g on g.id = gg.genre_id 
    GROUP BY
        title, game.id, added_at, metacritic, pegi, release, addedby 
    ORDER BY
        title;''')
    res = cur.fetchall()

    games = list(map(parse_game, res))

    with open(f'./migrations/games.json', 'w') as file:
        file.write(json.dumps(games, cls=DateTimeEncoder))

def user_table(cur):
    cur.execute('select * from "user" u ')
    res = cur.fetchall()
    print(res)

    users = list(map(parse_user, res))

    with open(f'./migrations/users.json', 'w') as file:
        file.write(json.dumps(users, cls=DateTimeEncoder))