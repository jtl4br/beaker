from flask import Flask, Response, json, send_file, render_template, request, jsonify, make_response, session, redirect, url_for
from flask_restful import Resource, Api, reqparse
# from sqlalchemy i  mport create_engine
import sqlalchemy
from sqlalchemy import *
from kafka import KafkaProducer, KafkaConsumer
import datetime
import json
from apscheduler.schedulers.background import BackgroundScheduler
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)
api = Api(app)

sched = BackgroundScheduler()
experimentToMetrics = dict()
sched.start()

def connect(db, host='localhost', port=5432):
	# We connect with the help of the PostgreSQL URL
	# postgresql://user:passlocalhost:5432/database
	url = 'postgresql://{}:{}/{}'
	url = url.format(host, port, db)

	con = sqlalchemy.create_engine(url, client_encoding='utf8')
	meta = sqlalchemy.MetaData(bind=con, reflect=True)
	return con, meta, db


# TODO
def startupSavedExperiments():
	# Spin up experiments saved in DB Experiment Table
	return 0

#startupSavedExperiments()

class AuthenticateUser(Resource):
	def post(self):
		print "Authenticating..."
		try:
			# Parse the arguments
			parser = reqparse.RequestParser()
			parser.add_argument('username', type=str, help='Username for Authentication')
			parser.add_argument('password', type=str, help='Password for Authentication')
			args = parser.parse_args()

			_userUsername = args['username']
			_userPassword = args['password']

			if _userUsername is None or _userPassword is None:
				return False;
			users = Table('users', meta, autoload=True)

			s = sqlalchemy.select([users]).where(users.c.username == _userUsername).where(users.c.password == _userPassword)

			data = con.execute(s)
			row = data.fetchone()

			if (row is not None):
				return True;
			return False;

		except Exception as e:
			return {'error': str(e)}

@app.after_request
def add_header(r):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the rendered page for 10 minutes.
	"""
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r

@app.route('/')
def login():
	#if 'username' in session:
		#return redirect('/dashboard')
	return app.send_static_file('index.html')


def filter():
	con, meta, db = connect('beaker')
	expToQueryString = dict()
	con, meta, db = connect('beaker')
	expTable = Table('experiments', meta, autoload=True)
	s = select([expTable])
	result = con.execute(s)

	for row in result:
		expToQueryString[row[0]] = row[10]
	
	for exp in expToQueryString:
		_expQueryString = expToQueryString[exp]
		result = con.execute(_expQueryString)

		for row in result.fetchall():
			producer = KafkaProducer()
			print 'Sending to topic={} with data={}'.format(exp, row)
			producer.send(exp, str(row))
	return 0


def updateExperiment(experiment):
	con, meta, db = connect('beaker')
	job_id = experiment['id']
	consumer = KafkaConsumer(job_id)
	
	data = []
	maxDate = experiment['startDate']
	for msg in consumer:
		data.append(tuple(msg.value))

	data2=[]
	for entry in data:
		if entry[10] >= maxDate:
			data2.append(entry)
			print 'New Entry: ', entry
	
	for metric in experiment['metrics']:
		if metric == 'RatioAmountToBalance':
			m = RatioAmountToBalance(data2)
			ratios = m.calculate()
			stat = m.stat(args={'ratios':ratios})
			experimentToMetrics[job_id] = {'value': ratios,
										   'stat': stat}
			print ratios
			print stat
		elif metric == 'NumCustomers':
			m = NumCustomers(data2)
			m.calculate()
			stat = m.stat()
			experimentToMetrics[job_id] = {'value': m.numCustomersList,
										   'stat': stat}
			print ratios
			print stat 
		else:
			print 'Error'
	
	for d in data:
		maxDate = max(maxDate, d[10])
		print 'MaxDate: ', maxDate

def default(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        # if obj.utcoffset() is not None:
        #     obj = obj - obj.utcoffset()
        # millis = int(
        #     calendar.timegm(obj.timetuple()) * 1000 +
        #     obj.microsecond / 1000
        # )
        # return millis
        obj = obj.strftime("%Y-%m-%d")
    raise TypeError('Not sure how to serialize %s' % (obj,))

class Experiment(Resource):
	def post(self):

		con, meta, db = connect('beaker')
		# parser = reqparse.RequestParser()
		# # Experiment Metadata
		# parser.add_argument('name', type=str, required=True, help='experiment name')
		# parser.add_argument('product', type=str, required=True, help='product we are collecting from')
		# parser.add_argument('target', type=str, required=True, help='feature we are collecting from')
		# parser.add_argument('startDate', type=str, required=True, help='start date')
		# parser.add_argument('endDate', type=str, required=True, help='end date - when to stop the data collection')
		# parser.add_argument('active', type=bool, required=True, help='')
		
		# # Population Category (default should be 'all')
		# parser.add_argument('ageLower', type=int, required=True, help='age category')
		# parser.add_argument('ageUpper', type=int, required=True, help='age category')

		# parser.add_argument('geo', type=int, required=True, help='geographic category')
		# parser.add_argument('incomeLevel', type=int, required=True, help='income category')
		
		# # Metrics
		# parser.add_argument('metric', action='append', required=True, help='all metrics')
		# args = parser.parse_args()

		_expId = str(uuid.uuid4())
		_expName= request.form['name']
		_expProduct = request.form['product']
		_expTarget = int(request.form['target'])
		
		_expStartDate = datetime.strptime(request.form['startDate'] , '%Y-%m-%d')
		_expEndDate = datetime.strptime(request.form['endDate'] , '%Y-%m-%d')
		_expActive = bool(request.form['active']) # State for whether the experiment should be collecting or not (pause)


		_expAgeLower = int(request.form['ageLower'])
		_expAgeUpper = int(request.form['ageUpper'])

		_expGeoGroup = int(request.form['geo'])
		_expIncomeLevel = int(request.form['incomeLevel'])

		_expMetrics1 = bool(request.form['metric1']) # Returns a list of predefined metrics codenames
		_expMetrics2 = bool(request.form['metric2']) # Returns a list of predefined metrics codenames

		# insert experiment into experiments
		# _expInsertString = []
		# _expInsertString.append('INSERT INTO EXPERIMENTS (NAME,PRODUCT,START_DATE,END_DATE,ACTIVE,TARGET,AGE_L,AGE_U,GEOGROUP,INCOMEGROUP) VALUES (')
		# _expInsertString.append(str(_expName))
		# _expInsertString.append(',')
		# _expInsertString.append(str(_expActive))
		# _expInsertString.append(',')
		# _expInsertString.append(str(_expTarget))
		# _expInsertString.append(',')
		# _expInsertString.append(str(_expAgeLower))
		# _expInsertString.append(',')
		# _expInsertString.append(str(_expAgeUpper))
		# _expInsertString.append(',')
		# _expInsertString.append(');')
		# _expInsertString = ''.join(_expInsertString)
		# con.execute(_expInsertString)

		#build table for data
		# if _expTarget == 0:
		# 	dataTable = Table(_expName+'_data', meta,
		# 		Column('id', Integer, Sequence(_expName + '_id_seq'), primary_key=True),
		# 		Column('name', String(30)),
		# 		Column('card_type', String(20)),
		# 		Column('region', Integer),
		# 		Column('age',Integer),
		# 		Column('prev_num_card', Integer),
		# 		Column('date', timestamp)
		# 	)
		# elif _expTarget == 1:
		# 	dataTable = Table(_expName+'_data', meta,
		# 		Column('id', Integer, Sequence(_expName + '_id_seq'), primary_key=True),
		# 		Column('name', String(30)),
		# 		Column('card_type', String(20)),
		# 		Column('transaction_type', String(20)),
		# 		Column('amount', Integer),
		# 		Column('balance', Integer),
		# 		Column('max_limit', Integer),
		# 		Column('region', Integer),
		# 		Column('age',Integer),
		# 		Column('income', Integer),
		# 		Column('date', timestamp)
		# 	)

		# meta.create_all()

		### TODO - build query string

		whichTable = None
		if (_expTarget == 0):
			whichTable = 'transactions'
		else:
			whichTable = 'customer'

		q1 = 'SELECT * from {} WHERE card_type = {} AND date '.format(whichTable, _expProduct)
		q2 = 'BETWEEN \'{}\' AND \'{}\' AND age BETWEEN {} AND {} '.format(_expStartDate, _expEndDate,_expAgeLower, _expAgeUpper)
		q3 = 'AND region = \'{}\' AND income = {};'.format(_expGeoGroup, _expIncomeLevel)
		_expQueryString = q1 + q2 + q3

		result = con.execute(_expQueryString)
		toReturn = result.fetchall()

		# Spin up a new experiment job
		populationData = {'ageLower': _expAgeLower, 'ageUpper': _expAgeUpper, 'geo': _expGeoGroup, 'incomeLevel': _expIncomeLevel}
		experiment = {'id': _expId,
					  'name': _expName, 
					  'target': _expTarget, 
					  'startDate': _expStartDate, 
					  'endDate': _expEndDate, 
					  'active': _expActive, 
					  'population': populationData, 
					  'metric1':_expMetrics1,
					  'metric2':_expMetrics2,
					  'queryString':_expQueryString # <---TODO: Add column to database
					  }
		
		sched.add_job(updateExperiment, 'interval',
					  kwargs={'experiment':experiment}, 
					  id=_expId,
					  start_date=_expStartDate, 
					  end_date=_expEndDate)

		# Persist to the local database
		expTable = Table('experiments', meta, autoload=True)
		i = expTable.insert()
		i.execute(id=_expId, name=_expName, 
				  product=_expProduct, target=_expTarget, 
				  active=_expActive, start_date=_expEndDate, 
				  end_date=_expEndDate, agelower=_expAgeLower, ageupper=_expAgeUpper,
				  geogroup=_expGeoGroup, incomegroup = _expIncomeLevel, 
				  querystring=_expQueryString, metric1=_expMetrics1, metric2=_expMetrics2)

	# Gets the configuration of an experiment
	def get(self):
		con, meta, db = connect('beaker')
		try:
			_id = request.args['experimentId']
			return 0
		except Exception as e:
			experiments = Table('experiments', meta, autoload=True)
			s = select([experiments])
			result = con.execute(s)
			return jsonify([dict(r) for r in result])


	# Update an 'experiment'
	def put(self):
		parser.add_argument('experimentId', type=str, required=True, help='experiment id')
		parser.add_argument('active', type=bool, required=True, help='new active state')
		
		job_id = args['experimentId']
		active = args['active']

		if active == True:
			sched.resume_job(job_id)
		else:
			sched.pause_job(job_id)
		
		# TODO: Update DB entry

	# Deletes an experiment from the database
	def delete(self):
		parser.add_argument('experimentId', type=str, required=True, help='experiment id')
		job_id = args['experimentId']

		sched.remove_job(job_id)

class BasicStat(Resource):
	def get(self):
		id = request.args['experimentId']
		print id

		stat = experimentToMetrics[id]['stat']
		data = {'mean': stat['mean'], 'median': stat['median'], 'stdDev': stat['stdDev'], 'var': stat['var']}
		return jsonify(data)

class PChange(Resource):
	def get(self):
		import random
		id = request.args['experimentId']
		print id

		if id == 'test':
			data = []
			for x in range(0, 5):
				data.append({'date': datetime.now()+timedelta(minutes=x*2), 'val': 20 + random.random() * 100})
			return jsonify(data)
		else:
			data = []
			pChanges = experimentToMetrics[id]['stat'][4]
			for x in pChanges:
				date = x[0]
				pChange = x[1]
				data.append({'date':date, 'val':pChange})
			return Response(jsonify(data), )

class Values(Resource):
	def get(self):
		id = request.args['experimentId']
		print id

		data = []
		values = experimentToMetrics[id]['value']
		for x in values:
			date = x[0]
			val = x[1]
			data.append({'date':date, 'val':val})
		return 'a'

import logging
logging.basicConfig()
sched.add_job(filter, 'interval', seconds=1)
api.add_resource(AuthenticateUser, '/api/AuthenticateUser')
api.add_resource(Experiment, '/api/Experiment')
api.add_resource(PChange, '/api/data/pChange')
api.add_resource(Values, '/api/data/values')
api.add_resource(BasicStat, '/api/data/basic')

if __name__ == "__main__":
	app.run()
