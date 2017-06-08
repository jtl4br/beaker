from flask import Flask, Response, json, send_file, render_template, request, jsonify, make_response, session, redirect, url_for
from flask_restful import Resource, Api, reqparse
# from sqlalchemy i  mport create_engine
import sqlalchemy
from sqlalchemy import *
from kafka import KafkaProducer
import datetime
import json
from apscheduler.schedulers.background import BackgroundScheduler
import uuid

app = Flask(__name__)
api = Api(app)

sched = BackgroundScheduler()
sched.start()

def connect(db, host='localhost', port=5432):
	# We connect with the help of the PostgreSQL URL
	# postgresql://user:passlocalhost:5432/database
	print 'Connecting...'
	url = 'postgresql://{}:{}/{}'
	url = url.format(host, port, db)
	print url

	con = sqlalchemy.create_engine(url, client_encoding='utf8')
	meta = sqlalchemy.MetaData(bind=con, reflect=True)
	return con, meta, db

# TODO
def startupSavedExperiments():
	# Spin up experiments saved in DB Experiment Table
	return 0


con, meta, db = connect('beaker')
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
	# Get all query strings
	expToQueryString = dict()
	expTable = Table('experiment', meta, autoload=True)
	s = select([expTable])
	result = conn.execute(s)
	for row in result:
		print row
		expToQueryString[row[]] = row[]
	
	for exp in expToQueryString:
		query_string = expToQueryString[exp]

		from sqlalchemy import text
		sql = text(query_string)
		result = db.engine.execute(sql)

		for row in result:
			print row
			producer = KafkaProducer()
			producer.send(exp, str(row))



def updateExperiment(experiment):
	consumer = KafkaConsumer(experiment['id'])
	data = []
	for msg in consumer:
		data.add(msg)
	for metric in experiment['metrics']
		if metric == 'RatioAmountToBalance':
			m = RatioAmountToBalance(data)
			ratios = m.calculate()
			stat = m.stat(args={'ratios':ratios})
			print ratio
			print stat 
		elif metric == :
			m = NumCustomersPastXMonths(data)
			ans = m.calculate(args={'numMonths':3})
			stat = m.stat()
			print ratio
			print stat 
		else:
			print 'Error'

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
        obj = obj.strftime("%Y/%m/%d")
    raise TypeError('Not sure how to serialize %s' % (obj,))

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

		_expMetrics = args['metric'] # Returns a list of predefined metrics codenames

		# Spin up a new experiment job
		populationData = {'ageGroup': _expAgeGroup, 'geo': _expGeoGroup, 'incomeLevel': _expIncomeLevel}
		experiment = {'id': _expId,
					  'name': _expName, 
					  'target': _expTarget, 
					  'startDate': _expStartDate, 
					  'endDate': _expEndDate, 
					  'active': _expActive, 
					  'population': populationData, 
					  'metrics':expMetrics
					  }
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
		try:
			print 'doing al exp'
			parser = reqparse.RequestParser()
			parser.add_argument('experimentId', type=str, required=True, help='experiment id')
			args = parser.parse_args()
			_id = args['experimentId']
			print 'one experiment got'
			# Query DB for specified experiment
			return 0
		except Exception as e:
			print 'getting all experiments'
			# Query DB for all experiments
			experiments = Table('experiments', meta, autoload=True)
			s = select([experiments])
			result = con.execute(s)
			print 'all experiments got'
			for row in result:
				print row
 			return json.dumps([dict(r) for r in result],default=default)

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


sched.add_job(filter)
api.add_resource(AuthenticateUser, '/api/AuthenticateUser')
api.add_resource(Experiment, '/api/Experiment')

if __name__ == "__main__":
	app.run()
