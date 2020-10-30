# coding=utf-8

from app.models.base import Session, engine, Base
from app.models.game import Game
from app.models.league import League
from app.models.user import User

Base.metadata.create_all(engine)

def register_user(username, password):
    if (len(username) < 3):
        return False
    if (len(password) < 8):
        return False

    session = Session()
    users = session.query(User).filter(User.username == username).all()
    
    unique_name = len(users) == 0

    if unique_name:
        new_user = User(username, password)
        session.add(new_user)
        session.commit()
    
    session.close()
    return unique_name

def login_user(username, password):
    session = Session()
    users = session.query(User).filter(User.username == username).all()
    token = ''
    if len(users) != 0:
        user = users[0]
        if (user.check_password(password)):
            token = user.encode_auth_token()

    session.close()
    return token

def authenticate_user(token):
    return User.decode_auth_token(token)
