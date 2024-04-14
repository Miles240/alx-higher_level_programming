#!/usr/bin/python3

"""contains the class definition of a State """

from sqlalchemy import Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

myMetadata = MetaData()
Base = declarative_base(metadata=myMetadata)


class State(Base):
    """Class representation of States"""

    __tablename__ = "people"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    age = Column(Integer, nullable=False)


engine = create_engine("mysql+mysqlconnector://root:Scombone240@localhost:3306/test_db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = State(name="Miles", age=20)

# session.add(person)
# session.commit()
session.close()


result = session.query(State).all()

for person in result:
	print(f'{person.name}, {person.age}')