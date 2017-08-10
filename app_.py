from flask import Flask


import psycopg2
import psycopg2.extras
import sys


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)


@app.route('/')
def index():
	engine = create_engine(os.environ['DATABASE_URL'], echo=True)
	connection = engine.connect()
	return 'rrr'


if __name__ == "__main__":
	app.run(debug = True)