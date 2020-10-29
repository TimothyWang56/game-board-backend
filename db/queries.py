# coding=utf-8

from db.base import Session
from db.user import User
from db.game import Game
from db.league import League

session = Session()

# print leagues
leagues = session.query(League).all()

print('\n### All leagues:')
for league in leagues:
    print(f'{league.id}, {league.league_name}, {league.game_name}')
    for game in league.games:
        print(f'\t{game.date}')
    for user in league.members:
        print(f'\t{user.username}')
print('')

# print games
games = session.query(Game).all()

print('\n### All games:')
for game in games:
    print(f'{game.date}, {game.winner}')
print('')

# print users
users = session.query(User).all()

print('\n### All users:')
for user in users:
    print(f'{user.id}, {user.username}')
    for league in user.leagues:
        print(f'\t{league.league_name}')
    print(user.check_password('password1'))
print('')