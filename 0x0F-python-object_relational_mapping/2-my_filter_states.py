#!/usr/bin/python3


'''
 script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    state_name = argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id ASC".format(
        (state_name))
    cursor.execute(query)

    data = cursor.fetchall()
    for state in data:
        print(state)
    cursor.close()
    db.close()
