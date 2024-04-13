#!/usr/bin/python3
"""Contains the list_states Module"""

import MySQLdb
import sys


def list_states(username, password, name):
    """Function that lists all the states from the database"""
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
            WHERE name LIKE BINARY 'N%'
            ORDER BY states.id ASC"""

        cursor.execute(query)
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    list_states(username, password, name)
