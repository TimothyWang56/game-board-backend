# coding=utf-8

from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from db.base import Base

league_member_association = Table('league_members', Base.metadata,
    Column('league_id', Integer, ForeignKey('leagues.id', ondelete="CASCADE")),
    Column('user_id', Integer, ForeignKey('users.id', ondelete="CASCADE"))
)

class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    league_name = Column(String)
    game_name = Column(String)

    games = relationship(
        "Game", back_populates="league",
        cascade="all, delete",
        passive_deletes=True
    )

    members = relationship(
        "User",
        secondary=league_member_association,
        back_populates="leagues",
        passive_deletes=True
    )

    def __init__(self, league_name, game_name):
        self.league_name = league_name
        self.game_name = game_name