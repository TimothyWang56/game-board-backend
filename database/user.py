# coding=utf-8

from sqlalchemy import Column, String, Integer, Table, Binary
from sqlalchemy.orm import relationship, backref
import bcrypt

from base import Base

from league import league_member_association

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