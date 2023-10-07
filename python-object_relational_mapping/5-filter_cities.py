"""
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(
        """SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id"""
    )
    print(", ".join([city[2] for city in c.fetchall() if city[4] == sys.argv[4]]))
