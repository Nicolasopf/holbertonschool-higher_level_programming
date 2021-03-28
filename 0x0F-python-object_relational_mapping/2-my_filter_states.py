#!/usr/bin/python3
""" lists all states with a name starting with N """

from sys import argv
import MySQLdb as mysql

if __name__ != '__main__':
    exit

connection = mysql.connect(
    host='localhost',
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)

cursor = connection.cursor()

syntax = 'SELECT states.id, states.name FROM states WHERE\
 states.name = \'{}\' ORDER BY states.id'.format(argv[4])
cursor.execute(syntax)

for column in cursor:
    if (column[1] == argv[4]):
        print(column)
