#!/usr/bin/python3
""" Connect to database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ != '__main__':
    exit

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}').format(argv[1],
                                                                    argv[2],
                                                                    argv[3])
Base.metadata.create_all(engine)
