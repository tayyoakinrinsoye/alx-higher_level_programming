#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py
 lists all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Get database credentials
    user1 = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user1, passwd, db_name))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and corresponding states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print results
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
