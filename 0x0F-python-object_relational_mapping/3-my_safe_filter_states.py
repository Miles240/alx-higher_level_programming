#!/usr/bin/python3

"""Contains the list_states Module"""

import MySQLdb
import sys


def list_states(username, password, name, state_name):
    """list the states in the table"""
    conn = MySQLdb.connect(
        host="localhost",
        port="3306",
        user=username,
        password=password,
        db=name
    )

    cursor = conn.cursor()
    query = """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY states.id ASC
    """

    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state_name = sys.agrv[4]

    list_states(username, password, name, state_name)
