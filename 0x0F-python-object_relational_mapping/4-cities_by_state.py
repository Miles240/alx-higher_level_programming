#!/usr/bin/python3

"""List all cities and states in the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
