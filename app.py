from flask import Flask, Response, json, send_file, render_template, request, jsonify, make_response, session, redirect, url_for
from flask_restful import Resource, Api, reqparse
# from sqlalchemy i  mport create_engine
import sqlalchemy
from sqlalchemy import *
#from kafka import KafkaProducer
import datetime
import json
from apscheduler.schedulers.background import BackgroundScheduler
import uuid

app = Flask(__name__)
api = Api(app)
sched = BackgroundScheduler()
sched.start()
startupSavedExperiments()

# TODO
def startupSavedExperiments():
	# Spin up experiments saved in DB Experiment Table
	return 0

def connect(db, host='localhost', port=5432):
	# We connect with the help of the PostgreSQL URL
	# postgresql://user:passlocalhost:5432/database
	print 'Connecting...'
	url = 'postgresql://{}:{}/{}'
	url = url.format(host, port, db)
	print url

	con = sqlalchemy.create_engine(url, client_encoding='utf8')
	meta = sqlalchemy.MetaData(bind=con, reflect=True)
	return con, meta

con, meta = connect('beaker')

class AuthenticateUser(Resource):
	def post(self):
		print 'authenticating...'
		try:
			# Parse the arguments
			parser = reqparse.RequestParser()
			parser.add_argument('username', type=str, help='Username for Authentication')
			parser.add_argument('password', type=str, help='Password for Authentication')
			args = parser.parse_args()

			_userUsername = args['username']
			_userPassword = args['password']

			print _userUsername
			print _userPassword

			if _userUsername is None or _userPassword is None:
				raise Exception('Username and password required')
			users = Table('users', meta, autoload=True)

			s = sqlalchemy.select([users]).where(users.c.username == _userUsername).where(users.c.password == _userPassword)

			data = con.execute(s)
			row = data.fetchone()
			print row

			if (row is not None):
				print 'GOOD'
				resp = Response(js, status=200, mimetype='application/json')
				return resp
			else:
				print 'BAD'
				return Response(js, status=100, mimetype='application/json')

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

def filter(experiment):
	return []

def calcMetrics(messages, metrics):
	for metric in metrics:
	return []

def updateExperiment(experiment):
	print experiment
	filtered = filter(experiment)
	calcMetrics(filtered, experiment['metrics'])

class Experiment(Resource):
	def post(self):
		parser = reqparse.RequestParser()

		# Experiment Metadata
		parser.add_argument('name', type=str, required=True, help='experiment name')
		parser.add_argument('product', type=str, required=True, help='product we are collecting from')
		parser.add_argument('target', type=str, required=True, help='feature we are collecting from')
		parser.add_argument('startDate', type=str, required=True, help='start date')
		parser.add_argument('endDate', type=str, required=True, help='end date - when to stop the data collection')
		parser.add_argument('active', type=bool, required=True, help='')
		
		# Population Category (default should be 'all')
		parser.add_argument('ageGroup', type=int, required=True, help='age category')
		parser.add_argument('geo', type=int, required=True, help='geographic category')
		parser.add_argument('incomeLevel', type=int, required=True, help='income category')
		
		# Metrics
		parser.add_argument('metric', action='append', required=True, help='all metrics')
		args = parser.parse_args()

		_expId = str(uuid.uuid4())
		_expName= args['name']
		_expProduct = args['product']
		_expTarget = args['target']
		_expStartDate = '{} 00:00:00'.format(args['startDate'])
		_expEndDate = '{} 00:00:00'.format(args['endDate'])
		_expActive = args['active'] # State for whether the experiment should be collecting or not (pause)

		_expAgeGroup = args['ageGroup']
		_expGeoGroup = args['geo']
		_expIncomeLevel = args['incomeLevel']

		_expMetrics = args['metric'] # Returns a lisr of predefined metrics codenames

		# Spin up a new experiment job
		populationData = {'ageGroup': _expAgeGroup, 'geo': _expGeoGroup, 'incomeLevel': _expIncomeLevel}
		experiment = {'id': _expId,
					  'name': _expName, 
					  'target': _expTarget, 
					  'startDate': _expStartDate, 
					  'endDate': _expEndDate, 
					  'active': _expActive, 
					  'population': populationData, 
					  'metrics':expMetrics}
		sched.add_job(updateExperiment, 
					  'interval', 
					  kwargs={'experiment':experiment}, 
					  id=_expId, seconds=30, 
					  start_date=_expStartDate, 
					  end_date=_expEndDate)
		print experiment
		print job

		# Persist to the local database
		expTable = Table('experiment', meta, autoload=True)
		i = expTable.insert()
		i.execute(id=_expId, name=_expName, 
				  product=_expProduct, target=_expTarget, 
				  active=_expShouldCollect, start_date=_expEndDate, 
				  end_date=_expEndDate, agegroup=_expAgeGroup,
				  geogroup=_expGeoGroup, incomegroup = _expIncomeLevel)
		
		return experiment

	# Gets the configuration of an experiment
	def get(self):
		parser.add_argument('experimentId', type=str, required=True, help='experiment id')
		id = args['experimentId']
		if args['experimentId'] == None: 
			# Query DB for all experiments
		else:
			# Query DB for specified experiment

		return 0


	# Update an 'experiment'
	def put(self):
		parser.add_argument('experimentId', type=str, required=True, help='experiment id')
		parser.add_argument('newName', type=str, required=True, help='new name')
		parser.add_argument('active', type=bool, required=True, help='new active state')
		
		job_id = args['experimentId']
		name = args['newName']
		active = args['active']

		if active == True:
			sched.resume_job(job_id)
		else:
			sched.pause_job(job_id)
		
		# Update DB

	# Deletes an experiment from the database
	def delete(self):
		parser.add_argument('experimentId', type=str, required=True, help='experiment id')
		job_id = args['experimentId']

		sched.remove_job(job_id)

api.add_resource(AuthenticateUser, '/api/v1/AuthenticateUser')
api.add_resource(Experiment, '/api/v1/Experiment')

if __name__ == "__main__":
	app.run()
