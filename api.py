from flask import Flask, Response, json, send_file, render_template, request, jsonify, make_response, session, redirect, url_for
from flask_restful import Resource, Api, reqparse
import sqlalchemy
from sqlalchemy import *
import random

app = Flask(__name__)
api = Api(app)

def connect(db, host='localhost', port=5432):
	# We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}/{}'
    url = url.format(host, port, db)

    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('beaker')
beaker = Table('', meta, autoload=True)

i = beaker.insert()
for x in range(6, 20):
	y = random.randint(0,2)
	if (y == 0):
		card = 'gold'
	elif (y == 1):
		card = 'silver'
	elif (y == 2):
		card = 'platinum'
	i.execute(name='0' + str(x),product=card,start_date='2017-06-04',end_date='2017-06-05', active=str(y>0))
