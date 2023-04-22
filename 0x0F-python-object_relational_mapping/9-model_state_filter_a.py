#!/usr/bin/python3
""" lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_data = session.query(State).order_by(State.id)\
        .filter(State.name.like("%a%")).all()

    for items in new_data:
        print(f'{items.id}: {items.name}')
    session.close()
