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
    query = "SELECT cities.name FROM cities INNER JOIN \
        states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id"
    cursor.execute(query, (state_name),)

    cities = cursor.fetchall()
    if not cities:
        print(f'No city found for {state_name} state')
    else:
        print(', '.join(city[0] for city in cities))
    cursor.close()
    db.close()
