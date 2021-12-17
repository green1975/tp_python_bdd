from faker import Faker
from datetime import date

faker = Faker()

def user_last_name():
    return faker.last_name()

def user_first_name():
    return faker.last_name()

def user():
    return (user_first_name(), user_last_name())

def game_name():
    return ' '.join(faker.words())

def game_metacritic():
    return faker.random_int(min=0, max=100)

def game_release():
    return faker.date()

def game_pegi():
    return faker.random_int(min=3, max=18)

def game_addedBy():
    return faker.random_int(min=1, max=10)

def game():
    return (game_name(), game_metacritic(),  game_pegi(), game_release(), game_addedBy(), date.today())

def genre():
    return [faker.word()]

def game_genre():
    return (faker.random_int(min=1, max=100), faker.random_int(min=1, max=10))