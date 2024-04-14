#!/usr/bin/python3

""" lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    db_host = "localhost"
    db_port = 3306
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_URL = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(db_URL, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print(state.id, state.name, sep=": ")

    session.close()
