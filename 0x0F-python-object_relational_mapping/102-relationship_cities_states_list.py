#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base


if __name__ == '__main__':
    # Get MySQL credentials from command line arguments
    user_name = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    # Create SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, passwd, db_name))

    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database and print results
    query = session.query(City).order_by(City.id)
    for city in query.all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()
