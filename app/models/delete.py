# coding=utf-8

from app.models.base import Session
from app.models.game import Game
from app.models.user import User
from app.models.league import League

session = Session()

users = session.query(User).delete()
leagues = session.query(League).delete()

session.commit()