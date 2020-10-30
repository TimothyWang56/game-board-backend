# coding=utf-8

# 1 - imports
from datetime import datetime

from app.models.base import Session, engine, Base
from app.models.game import Game
from app.models.league import League
from app.models.user import User

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create leagues
league1 = League("Catan with the Boys", "Catan")
league2 = League("Bigger Catan Group!", "Catan")
league3 = League("Pokemasters", "Pokemon")

#5 - create games
game1 = Game(datetime(2020, 10, 1, 20, 0))
game2 = Game(datetime(2020, 10, 1, 22, 0))
game3 = Game(datetime(2020, 10, 2, 10, 0))
game4 = Game(datetime(2020, 10, 3, 20, 0))
game5 = Game(datetime(2020, 10, 4, 8, 0))
game6 = Game(datetime(2020, 10, 4, 15, 0))
game7 = Game(datetime(2020, 10, 5, 21, 0))
game8 = Game(datetime(2020, 10, 8, 21, 0))
game9 = Game(datetime(2020, 10, 10, 13, 0))
game10 = Game(datetime(2020, 10, 12, 17, 0))
game11 = Game(datetime(2020, 10, 14, 20, 0))
game12 = Game(datetime(2020, 10, 15, 18, 0))

#6 - create users
user1 = User("GyozaCrumb", "password1")
user2 = User("socho", "password2")
user3 = User("corgo", "password3")
user4 = User("gabin", "password4")

league1.games = [game1, game2, game3, game4]
league2.games = [game5, game6, game7, game8]
league3.games = [game9, game10, game11, game12]

league1.members = [user1, user2, user3]
league2.members = [user1, user2, user3, user4]
league3.members = [user1, user3]

session.add(league1)
session.add(league2)
session.add(league3)

session.commit()
session.flush()
game1.winner = user1.id
game2.winner = user2.id
game3.winner = user1.id
session.commit()
session.close()