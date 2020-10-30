# coding=utf-8

from sqlalchemy import Column, String, Integer, Table, Binary
from sqlalchemy.orm import relationship, backref
from datetime import datetime, timedelta
import bcrypt
import jwt

from db.base import Base

from db.config import SECRET_KEY

from db.league import league_member_association

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    passhash = Column(Binary(60))

    leagues = relationship(
        "League",
        secondary=league_member_association,
        back_populates="members",
        passive_deletes=True
    )

    def __init__(self, username, password):
        self.username = username
        password_as_bytes = password.encode('utf-8')
        self.set_password(password_as_bytes)

    def set_password(self, password):
        self.passhash = bcrypt.hashpw(password, bcrypt.gensalt())

    def check_password(self, password):
        password_as_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_as_bytes, self.passhash)

    def encode_auth_token(self):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1, seconds=0),
                'iat': datetime.utcnow(),
                'sub': self.id
            }

            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            ).decode('utf-8')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'