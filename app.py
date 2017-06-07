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

	# Gets the configuration of an experiment
	def get(self):


	def delete(self):


class StartExperiment(Resource):
	def put(self):

class PauseExperiment(Resource):
	def put(self):
