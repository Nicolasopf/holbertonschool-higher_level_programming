#!/usr/bin/python3
""" Lists all cities from a DB """

from sys import argv
import MySQLdb as mysql

if __name__ == "__main__":
    connection = mysql.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = connection.cursor()

    syntax = 'SELECT cities.id, cities.name, states.name FROM cities JOIN\
    states ON cities.state_id = states.id ORDER BY cities.id'
    cursor.execute(syntax)
    for column in cursor:
        print(column)
