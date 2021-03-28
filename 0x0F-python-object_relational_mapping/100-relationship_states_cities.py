#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    city_n = City(name="San Francisco")
    state_n = State(name="California", cities=[city_n])
    session.add(city_n)
    session.commit()
