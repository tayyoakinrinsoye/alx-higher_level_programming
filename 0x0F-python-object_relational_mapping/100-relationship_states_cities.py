#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == '__main__':
    # Get MySQL credentials from command line arguments
    user_name = argv[1]
    mysql_passwd = argv[2]
    db_name = argv[3]

    # Create SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, mysql_passwd, db_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)

    # Add objects to session
    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()
