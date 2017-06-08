from apscheduler.schedulers.background import BackgroundScheduler
from kafka import KafkaConsumer
from kafka import KafkaProducer
import datetime
import json


producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
sched = BackgroundScheduler()
sched.start()


customerConsumer = KafkaConsumer('NewCustomerData')
transactionConsumer = KafkaConsumer('NewTransactionData')


def filter():


def runExperiment(exp):
	if exp['target'] == 'Gold-NewCustomer':
		for msg in c1
		# persist newly available data to DB's Customer Table
		filter()

	elif exp['target'] == 'Silver-NewCustomer':
		# persist newly available data to DB's Customer Table
		filter()

	elif exp['target'] == 'Platinum-NewCustomer':
		# persist newly available data to DB's Customer Table
		filter()

	elif exp['target'] == 'Gold-NewTransaction':
		# persist newly available data to DB's Transaction Table
		filter()

	elif exp['target'] == 'Silver-NewTransaction':
		# persist newly available data to DB's Transaction Table
		filter()

	elif exp['target'] == 'Platinum-NewTransaction':
		# persist newly available data to DB's Transaction Table
		filter()

	else:
		print 'Unknown target'
	# Filters the dataset based on exp['ageGroup'], exp[], exp[]
	# Exp is a dictionary
	# After filtering, pull data from NewCustomerData kafka topic, NewTransactionData kafka topic

c1 = KafkaConsumer('AddNewExperiment')
def manageAddNewExperiment():
	for msg in c1:
		sched.add_job(runExperiment, 'interval', seconds=5, start_date='', end_date='')

c2 = KafkaConsumer('ResumeExperiment')
def manageResumeExperiment():
	for msg in c2:
		print msg.value

c3 = KafkaConsumer('PauseExperiment')
def managePauseExperiment():
	for msg in c3:
		print msg.value


sched.add_job(manageAddNewExperiment, 'interval', seconds=5)
sched.add_job(manageResumeExperiment, 'interval', seconds=5)
sched.add_job(managePauseExperiment, 'interval', seconds=5)
sched.add_job(manageDeleteExperiment, 'interval', seconds=5)
sched.add_job(manageUpdateExperiment, 'interval', seconds=5)


