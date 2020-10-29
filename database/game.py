# coding=utf-8

from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id', ondelete="CASCADE"))
    league = relationship("League", back_populates="games")
    date = Column(DateTime)
    
    # will add later when user data is figured out
    # winner = Column(String)

    def __init__(self, date):
        self.date = date