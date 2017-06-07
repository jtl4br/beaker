from flask import Flask, Response, json, send_file, render_template, request, jsonify, make_response, session, redirect, url_for
from flask_restful import Resource, Api, reqparse
import datetime


app = Flask(__name__)

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
    return render_template('login.html')

#@app.route("/")
#def hello():
#    return "Login Page"

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
