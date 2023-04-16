#!/usr/bin/env python3
"""
     script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


# Connect to MySQL server running on localhost at port 3306
db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=argv[1],
                     passwd=argv[2],
                     db=argv[3])

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

data = cursor.fetchall()
for row in data:
    print(row)
cursor.close()
db.close()
