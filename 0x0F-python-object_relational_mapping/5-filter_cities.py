#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities of that
 state, free of SQL injections """

from sys import argv
import MySQLdb as mysql

if __name__ == "__main__":
    state = argv[4]
    connection = mysql.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = connection.cursor()

    query = 'SELECT cities.name FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id'
    cursor.execute(query, (state, ))

    result = [i[0] for i in cursor]
    print(', '.join(result))
