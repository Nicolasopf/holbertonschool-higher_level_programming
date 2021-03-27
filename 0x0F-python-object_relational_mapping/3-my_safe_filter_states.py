#!/usr/bin/python3
""" lists all states with a name starting with N """

from sys import argv
import MySQLdb as mysql

if __name__ == '__main__':
    state = argv[4]

    connection = mysql.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = connection.cursor()

    syntax = 'SELECT states.id, states.name FROM states WHERE\
    states.name = %s ORDER BY states.id'
    cursor.execute(syntax, (state, ))

    for column in cursor:
        print(column)
