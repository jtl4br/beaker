from flask import Flask, Response, json, send_file
from flask_restful import Resource, Api, reqparse
from kafka import KafkaProducer
import datetime


app = Flask(__name__)
api = Api(app)
producer = KafkaProducer(bootstrap_servers='localhost:1234')


@app.route("/")
def hello():
    return "Login Page"

class Experiment(Resource):
	# Update an 'experiment'
	def put(self):

	# Gets the configuration of an experiment
	def get(self):
		producer.send('beaker_topic', b'this is a test of the GT emergency system')
		#api.add_resource(AddExperiment, '/api/AddExperiment')

	# Deletes an experiment from the database
	def delete(self):

class AddExperiment(Resource):
	def get(self):
		return 'hello'

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

#api.add_resource(AuthenticateUser, '/api/AuthenticateUser')
api.add_resource(Experiment, '/api/Experiment')




if __name__ == "__main__":
    app.run()
