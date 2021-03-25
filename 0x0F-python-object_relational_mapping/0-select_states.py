#!/usr/bin/python3
""" """
from sys import argv
import MySQLdb as mysql

if __name__ != '_B_main__':
    exit

connection = mysql.connect(
    host='localhost',
    port=3307,
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)

cursor = connection.cursor()  # get the cursor

cursor.execute("SELECT states.id, states.name FROM states ORDER BY states.id")
for column_name in cursor:
    print(column_name)
