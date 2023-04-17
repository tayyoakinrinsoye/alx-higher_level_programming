#!/usr/bin/python3


'''
 script that takes in the name of a state as an argument
 and lists all cities of that state, using the database hbtn_0e_4_usa
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    state_name = argv[4]
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(state_name)
    cursor.execute(query)

    cities = cursor.fetchall()
    print(", ".join([city[1] for city in cities]))
