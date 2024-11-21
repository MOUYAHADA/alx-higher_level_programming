#!/usr/bin/env python3
"""SELECT all states"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    [username, password, db_name] = sys.argv[1:]

    db = MySQLdb.connect(
        host='localhost',
        username=username,
        password=password,
        database=db_name,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
                ORDER BY states.id""")
    data = cursor.fetchall()
    for d in data:
        print(d)
