#!/usr/bin/python3
"""
This script takes in threestates from the database
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('Select * from states where name = '
                   '%(name)s order by id asc', {'name': sys.argv[4]})
    for a in cursor.fetchall():
        print(a)
    cursor.close()
    db.close()
