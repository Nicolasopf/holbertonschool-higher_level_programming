#!/usr/bin/python3
""" lists all states with a name starting with N """

from sys import argv
import MySQLdb as mysql

if __name__ != '__main__':
    exit

connection = mysql.connect(
    host='localhost',
    port=3307,
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)

cursor = connection.cursor()
cursor.execute(
    'SELECT states.id, states.name FROM states WHERE\
 ASCII(states.name) = 78 ORDER BY states.id')

for column in cursor:
    print(column)
