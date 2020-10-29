# coding=utf-8

from base import Session
from user import User
from game import Game
from league import League

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
    print(f'{game.date}')
print('')

# print users
users = session.query(User).all()

print('\n### All users:')
for user in users:
    print(f'{user.id}, {user.username}')
    for league in user.leagues:
        print(f'\t{league.league_name}')
print('')