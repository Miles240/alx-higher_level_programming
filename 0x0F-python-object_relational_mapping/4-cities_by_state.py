#!/usr/bin/python3

"""Contains the list_cities Module"""

import MySQLdb
import sys


def list_cities(username, password, name):
    """lists all cities from the database
    Args:
        username(str): user
        password(str): user's password
        name(str): db name
    """

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
            SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN states ON cities.id = states.id
            ORDER BY cities.id ASC
        """

        cursor.execute(query)
        cities = cursor.fetchall()

        for city in cities:
            print(city)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to Database {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            """Usage:
                python script.py
                <username>
                <password>
                <database>
            """
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    list_cities(username, password, name)
