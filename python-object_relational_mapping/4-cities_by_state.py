#!/usr/bin/python3
"""module for gettin states that start with letter n"""
import MySQLdb
import sys


if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=u, passwd=p, db=d,
                         charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT cities.id, states.name"
    "FROM states JOIN states ON cities.states_id = states.id"
    )
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
