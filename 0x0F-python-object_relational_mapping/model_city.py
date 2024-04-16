#!/usr/bin/python3

"""Module that contains the class definition of a City"""

from model_state import Base, State
from sqlalchemy import Column, String, Integer, MetaData, ForeignKey


class City(Base):
    """Class representation of City"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
