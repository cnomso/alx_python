"""script that lists all states from the database hbtn_0e_0_usa
    """

import MySQLdb
import sys
from sys import argv


# def usa_states(username, password, database):
#     db = MySQLdb.connect(
#         host="localhost", port="3306", username=username, passwrd=password, db=database
#     )

#     cursor = db.cursor()

#     cursor.execute("SELECT * FROM states ORDER BY id ASC")

#     results = cursor.fetchall()

#     for row in results:
#         print(row)
#     cursor.close()
#     db.close()


# if __name__ == "__main__":
#     username = sys.argv[1]
#     password = sys.argv[2]
#     database = sys.argv[3]

#     list_states(username, password, database)

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", username=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
