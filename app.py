from flask import Flask, Response, json, send_file, render_template, request, jsonify, make_response, session, redirect, url_for
from flask_restful import Resource, Api, reqparse
from sqlalchemy import *
from kafka import KafkaProducer
import datetime


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

            conn = mysql.connect()
            cursor = conn.cursor()
            #Could try string formatting for statement execute
            #Check for username AND password match in user table
            stmt = "SELECT * FROM user WHERE Username='{}' AND Password='{}'".format(_userUsername,_userPassword)
            cursor.execute(stmt)
            data = cursor.fetchall()

            if(len(data)>0):
                if(data):
                    #Format return into JSON object
                    userData = {'username': data[0][0], 'userType': data[0][2]}
                    js = json.dumps(userData)
                    resp = Response(js, status=200, mimetype='application/json')
                    return resp
                else:
                    return {'status':100,'message':'Authentication failure'}

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
    return render_template('login.html')

#@app.route("/")
#def hello():
#    return "Login Page"

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
