#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
if __name__ == "__main__":	
	db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
	cur = db.cursor()
	cur.execute("SELECT * FROM  states ORDER BY id ASC;")
	states = cur.fetchall()
	for state in states:
		print(state)
	cur.close()
	db.close()
