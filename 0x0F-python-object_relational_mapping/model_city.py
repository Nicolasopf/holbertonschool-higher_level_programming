#!/usr/bin/python3
""" class definition of a State and an instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from model_state import Base


class City(Base):
    """ Link to mysql table states """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
