#!/usr/bin/python3
"""Prints the first State object from the database
"""

import MySQLdb
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                sys.argv[2],
                                                sys.argv[3]),
    pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
state = session.query(State).first()
print("{}: {}".format(state.id, state.name))

session.close()
