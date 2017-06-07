from apscheduler.schedulers.background import BackgroundScheduler
from kafka import KafkaConsumer
from kafka import KafkaProducer
import datetime
import json


producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
KAFKA_TOPIC = 'beakertopic'

def executeExperimentJob():
	print 'AAAA'


sched = BackgroundScheduler()
sched.start()
print 'b'

consumer = KafkaConsumer('experiments')
while True:
	for msg in consumer:
		data = json.loads(msg.value)
		if data['type'] == 'AddExperiment':
			# Adds a new job to the scheduler
			# sched.add_job(executeExperimentJob, 'interval', seconds=3, start_date=data['startDate'], end_date=data['endDate'])
			print 'A'	
		elif data['type'] == 'DeleteExperiment':
			# Removes job from scheduler
			print 'B'
		elif data['type'] == 'UpdateExperiment':
			# Deletes the experiment and adds in a new one with the same id 
			print 'C'
		else:
			print 'ERROR'
			sched.add_job(executeExperimentJob, 'interval', seconds=3)

def manageExperiment

consume = KafkaConsumer('newData')
def manageData():
	for msg in consumer
		data = json.loads(msg.value)
		if data['target'] == '':
		