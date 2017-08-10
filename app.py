from flask import Flask
from flask import Flask, jsonify, abort, request, make_response, url_for,render_template


import psycopg2
import psycopg2.extras
import sys
import os


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__, static_url_path = "")



#engine = create_engine('postgres:///jive', echo=True)
engine = create_engine(os.environ['DATABASE_URL'], echo=True)
connection = engine.connect()

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/test')
def test():

	arr =[]
	for row in engine.execute('select * from nodes'):
		arr.append(dict(row))
		print(row)
	return jsonify(arr); 


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/nodes',methods = ['GET','POST'])
def getNodes():
	arr =[]
	for row in engine.execute('select id,txt from nodes'):
		arr.append(dict(row))

	return jsonify(arr); 




	
if __name__ == "__main__":
    app.run(debug = True)