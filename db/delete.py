# coding=utf-8

from db.base import Session
from db.game import Game
from db.user import User
from db.league import League

session = Session()

users = session.query(User).delete()
leagues = session.query(League).delete()

session.commit()