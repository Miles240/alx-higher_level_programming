#!/usr/bin/python3

"""List all states in the database"""

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
        SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC""".format(
        sys.argv[4]
    )

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
