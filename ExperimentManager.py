from apscheduler.schedulers.background import BackgroundScheduler
from kafka import KafkaConsumer
from kafka import KafkaProducer
import datetime
import json


producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
KAFKA_TOPIC = 'beakertopic'

def executeExperimentJob(a):




sched = BackgroundScheduler()
sched.start()
print 'b'

consumer = KafkaConsumer('beakertopic')
while True:
	for msg in consumer:
		data = json.loads(msg.value)
		if data['type'] == 'AddExperiment':
			sched.add_job(executeExperimentJob, 'interval', )
		elif data['type'] == 'foo':
			print 'B'
		else:
			print 'C'

