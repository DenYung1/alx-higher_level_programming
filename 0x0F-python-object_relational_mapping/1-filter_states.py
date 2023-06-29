#!/usr/bin/python3
import MySQLdb
import sys
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
if __name__ == " __main__":	
	db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
	cur = db.cursor()
	cur.execute("SELECT * FROM  states WHERE BINARY name LIKE "%N" ORDER BY id ASC;")
	states = cur.fetchall()
	for state in states:
		print(states)
	cur.close()
	db.close()
