#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base


if __name__ == '__main__':
    # Get MySQL credentials from command line arguments
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, passwd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()
    # Query database and print results
    query = session.query(State).order_by(State.id)
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("f\t{city.id}: {city.name}")
    session.close()
