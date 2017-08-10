from flask import Flask
from flask import render_template

import psycopg2
import psycopg2.extras
import sys


app = Flask(__name__)
@app.route('/')
def index():

	a = 'aaa'
	return 'a'
"""	
		#Define our connection string
	conn_string = "host='localhost' dbname='jive' user='q' password='w'"

	# print the connection string we will use to connect
	print ("Connecting to database") #+ str(conn_string)

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
	# tell postgres to use more work memory
	work_mem = 2048
 
	# by passing a tuple as the 2nd argument to the execution function our
	# %s string variable will get replaced with the order of variables in
	# the list. In this case there is only 1 variable.
	# Note that in python you specify a tuple with one item in it by placing
	# a comma after the first variable and surrounding it in parentheses.
	cursor.execute('SET work_mem TO %s', (work_mem,))
 
	# Then we get the work memory we just set -> we know we only want the
	# first ROW so we call fetchone.
	# then we use bracket access to get the FIRST value.
	# Note that even though we've returned the columns by name we can still
	# access columns by numeric index as well - which is really nice.
	cursor.execute('SHOW work_mem')
 
	# Call fetchone - which will fetch the first row returned from the
	# database.
	memory = cursor.fetchall()
 
	# access the column by numeric index:
	# even though we enabled columns by name I'm showing you this to
	# show that you can still access columns by index and iterate over them.
	#print ("Value: ", memory[0])
 
	# print the entire row 
	#print ("Row:	", memory)

	print(memory)


	return  str(memory)"""
	

	
if __name__ == "__main__":
    app.run(debug = True)