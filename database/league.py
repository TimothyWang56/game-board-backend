# coding=utf-8

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref

from base import Base

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

    def __init__(self, league_name, game_name):
        self.league_name = league_name
        self.game_name = game_name