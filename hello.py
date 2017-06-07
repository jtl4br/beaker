from flask import Flask, Response, json, send_file
from flask_restful import Resource, Api, reqparse
import datetime


app = Flask(__name__)

@app.route("/")
def hello():
    return "Login Page"

if __name__ == "__main__":
    app.run()

class Experiment(Resource):
	# Adds a new experiment
	def post(self):
		parser = reqparse.RequestParser()
	    parser.add_argument('name', type=str, help='Exp Name')
        parser.add_argument('target', type=str, help='product or feature we are collecting from')
		args = parser.parse_args()

        _courseNum = args['name']
        _courseName = args['target']
        _courseInstructor = args['instructor']

	# Gets the configuration of an experiment
	def get(self):

	# Deletes an experiment from the database
	def delete(self):

class AddMetricToExperiment(Resource):
	# Adds a new metric to an existing experiment
	def put(self):

class StartExperiment(Resource):
	# Triggers it to start collecting data
	def put(self):

class PauseExperiment(Resource):
	# Temporarily stops data collection
	def put(self):
