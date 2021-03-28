#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    query = session.query(State, City).join(City, State.id == City.state_id)\
        .order_by(City.id)

    for item in query:
        print("{}: ({}) {}".format(item.State.name, item.City.id,
                                   item.City.name))
