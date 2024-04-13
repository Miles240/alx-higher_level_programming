#!/usr/bin/python3

"""Contains the list_states Module"""
import MySQLdb
import sys


def list_states(username, password, name):
    """Function that lists all the states from the database"""

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=name
    )

    cursor = conn.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    list_states(username, password, name)
