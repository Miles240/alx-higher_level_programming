#!/usr/bin/python3

"""prints the State object with the name passed as 
    argument from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    result = session.query(State).filter(State.name.like(sys.argv[4])).all()

    for state in result:
        print(state.id)

    session.close()
