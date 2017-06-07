from flask import Flask, Response, json, send_file, render_template, request, jsonify, make_response, session, redirect, url_for
from flask_restful import Resource, Api, reqparse
from sqlalchemy import *
from kafka import KafkaProducer
import datetime
import json

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

class AuthenticateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            con, meta = connect('beaker')
            
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Username for Authentication')
            parser.add_argument('password', type=str, help='Password for Authentication')
            args = parser.parse_args()

            _userUsername = args['username']
            _userPassword = args['password']

            print _userUsername
            print _userPassword

            users = Table('users', meta, autoload=True)
            data = users.select(and_(users.username == _userUsername, users.password == _userPassword)).execute()

            if(len(data)>0):
                if(data):
                    #Format return into JSON object
                    resp = Response(js, status=200, mimetype='application/json')
                    return resp
                else:
                    return {'status':100,'message':'Authentication failure'}

        except Exception as e:
            return {'error': str(e)}



producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
KAFKA_TOPIC = 'beakertopic'

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

#@app.route("/")
#def hello():
#    return "Login Page"

class Experiment(Resource):
	def post(self):
		parser = reqparse.RequestParser()

		parser.add_argument('name', type=str, required=True, help='experiment name')
		parser.add_argument('target', type=str, required=True, help='product or feature we are collecting from')
		parser.add_argument('startDate', type=str, required=True, help='start date')
		parser.add_argument('endDate', type=str, required=True, help='end date - when to stop the data collection')

		# Population Category (default should be all)
		parser.add_argument('ageGroup', type=int, required=True, help='')
		parser.add_argument('geo', type=int, required=True, help='geographic area')
		parser.add_argument('incomeLevel', type=int)

		# Metrics
		parser.add_argument('metric', action='append', required=True, help='all metrics')

		args = parser.parse_args()

		_expName= args['name']
		_expTarget = args['target']
		_expStartDate = args['startDate']
		_expEndDate = args['endDate']
		_expShouldCollect = True # State for whether the experiment should be collecting or not (pause)

		_expAgeGroup = args['ageGroup']
		_expGeoGroup = args['geo']
		_expIncomeLevel = args['incomeLevel']

		_expMetrics = args['metric'] # Returns a lisr of predefined metrics codenames

		# Persist to the local database

		# Persist to Kafka Producer
		populationData = {'ageGroup': _expAgeGroup, 'geo': _expGeoGroup, 'incomeLevel': _expIncomeLevel}
		data = {'type': 'AddExperiment', 'name': _expName, 'target': _expTarget, 'startDate': _expStartDate, 'endDate': _expEndDate, 'status': _expShouldCollect, 'population': populationData, 'metrics':expMetrics}
		producer.send(KAFKA_TOPIC, data)

		return data

	# Gets the configuration of an experiment
	def get(self):
		producer.send(KAFKA_TOPIC, {'type' : 'this is a test of the GT emergency system'})

	# Update an 'experiment'
	def put(self):
		return 0

	# Deletes an experiment from the database
	def delete(self):
		return 0

#api.add_resource(AuthenticateUser, '/api/AuthenticateUser')
api.add_resource(Experiment, '/api/Experiment')
# api.add_resource(AddExperiment, '/api/AddExperiment')


if __name__ == "__main__":
    app.run()
