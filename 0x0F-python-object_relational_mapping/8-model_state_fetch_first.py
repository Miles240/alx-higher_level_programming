#!/usr/bin/python3

"""prints the first State object from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    db_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".fomat(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    engine = create_engine(db_URL, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).first()
    if result is None:
        print("Nothing")
    print(result.id, result.name, sep=": ")

    session.close()
