#!/usr/bin/python3
"""
This script takes in state name as arguemnt from the database and list all
the cities by state
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cities = []
    cursor.execute('Select cities.name from cities join states on '
                   'cities.state_id = states.id where states.name = '
                   '"{}" order by cities.id asc'.format(sys.argv[4]))
    values = []
    counter = 1
    for a in cursor.fetchall():
        for i in a:
            values.append(i)

    for a in values:
        if(counter < len(values)):
            print(a, end=", ")
        else:
            print(a, end="")
        counter += 1
    print()
    cursor.close()
    db.close()
