#!/usr/bin/python3

"""Contains the list_state Module"""

import MySQLdb
import sys


def list_states(username, password, name, state_name):
    """list the states in the table"""
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
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

    except MySQLdb.Error as e:
        print(f"Error connecting to database {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            """Usage: Python Script.py
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
