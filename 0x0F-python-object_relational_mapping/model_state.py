#!/usr/bin/python3

"""contains the class definition of a State """

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    """Class representation of States"""

    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


engine = create_engine(
    "mysql://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
