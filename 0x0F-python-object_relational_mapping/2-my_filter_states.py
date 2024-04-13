#!/usr/bin/python3

"""Contains the list_state Module"""

import MySQLdb
import sys


def list_states(username, password, name, state_name):
    """list the states in the table
    Args:
        username(str): user
        password(str): db password
        name(str): db name
        state_name(str): Required state
    """
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=name
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        sys.exit(1)

    cursor = conn.cursor()
    query = """
    SELECT * FROM states
    WHERE name = '{}'
    ORDER BY states.id ASC""".format(state_name)

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            """Usage: python script.py
            <username>
            <password>
            <name>
            <state_name>"""
             )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state_name = sys.argv[4]

    list_states(username, password, name, state_name)
