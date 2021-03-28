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

    syntax = session.query(State)
    for item in syntax:
        if 'a' in item.name:
            query = session.query(State).filter_by(name=item.name)
            query.delete()
            session.commit()
    session.close()
