# coding=utf-8

from sqlalchemy import Column, String, Integer, Table
from sqlalchemy.orm import relationship, backref

from base import Base

from league import league_member_association

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

    leagues = relationship(
        "League",
        secondary=league_member_association,
        back_populates="members",
        passive_deletes=True
    )

    def __init__(self, username):
        self.username = username