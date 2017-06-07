from apscheduler.schedulers.blocking import BlockingScheduler
from kafka import KafkaConsumer
import datetime


sched = BlockingScheduler()
consumer = KafkaConsumer('beaker_topic', bootstrap_servers='localhost:1234')

while True:
	for msg in consumer:
		print msg