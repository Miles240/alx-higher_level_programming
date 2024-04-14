#!/usr/bin/python3

"""contains the class definition of a State """

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

myMetadata = MetaData()
Base = declarative_base(metadata=myMetadata)


class State(Base):
    """Class representation of States"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
