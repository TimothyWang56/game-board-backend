# coding=utf-8

from base import Session
from game import Game
from user import User
from league import League

session = Session()

users = session.query(User).delete()
leagues = session.query(League).delete()

session.commit()