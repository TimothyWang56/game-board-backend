# coding=utf-8

from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey('leagues.id', ondelete="CASCADE"))
    league = relationship("League", back_populates="games")
    date = Column(DateTime)
    winner = Column(Integer, ForeignKey('users.id', ondelete="SET NULL"), nullable=True)

    def __init__(self, date, winner=None):
        self.date = date
        self.winner = winner
