import psycopg2

def reset_database(cur):
        cur.execute('''
            DROP SCHEMA public CASCADE;
            ''')
        cur.execute('''
            CREATE SCHEMA public;
            ''')
        cur.execute('''
            create table IF NOT EXISTS "user" (
                id serial primary key,
                first_name text not null,
                last_name text,
                created_at timestamp default current_timestamp
            );''')
        cur.execute('''
            create table IF NOT EXISTS "game" (
                id serial primary key,
                title text not null,
                metacritic int,
                pegi int,
                release timestamp,
                added_at timestamp,
                addedBy integer references public.user(id)
            );''')
        cur.execute('''
            create table IF NOT EXISTS "genre" (
                id serial primary key,
                name text not null   
            );''')
        cur.execute('''
            create table IF NOT EXISTS "games_genres" (
                game_id integer references game(id),
                genre_id integer references genre(id)
            );''')
        

        # On ajoute l'autorisation à l'utilisateur sur toutes les tables et les séquences une fois créées
        cur.execute('grant all privileges on all tables in schema public to python;')
        cur.execute('grant all privileges on all sequences in schema public to python;')