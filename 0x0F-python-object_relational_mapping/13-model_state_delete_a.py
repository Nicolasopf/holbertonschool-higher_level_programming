#!/usr/bin/python3
""" deletes all State objects with a name containing the letter  """
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import delete

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    query = session.query(State).filter(State.name.like("%a%"))
    for item in query:
        session.delete(item)
    session.commit()
