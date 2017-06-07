from apscheduler.schedulers.background import BackgroundScheduler
from kafka import KafkaConsumer
from kafka import KafkaProducer
import datetime
import json


producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
sched = BackgroundScheduler()
sched.start()

def runExperiment(experiment):
	

customerConsumer = KafkaConsumer('AddExperiment')
def manageAddExperiment():
	for msg in consumer:
		print msg.value

customerConsumer = KafkaConsumer('ResumeExperiment')
def manageDeleteExperiment():
	for msg in consumer:
		print msg.value

customerConsumer = KafkaConsumer('PauseExperiment')
def manageDeleteExperiment():
	for msg in consumer:
		print msg.value

customerConsumer = KafkaConsumer('DeleteExperiment')
def manageDeleteExperiment():
	for msg in consumer:
		print msg.value

customerConsumer = KafkaConsumer('UpdateExperiment')
def manageUpdateExperiment():
	for msg in consumer:
		print msg.value

customerConsumer = KafkaConsumer('NewCustomerData')
def manageNewCustomerData():
	for msg in consumer:
		print msg.value
	    con, meta = connect('beaker')
	    beaker = Table('customer', meta, autoload=True)
	    i = beaker.insert()
	    i.execute(name=_name,card_type=cardType,region=_region,income=_income,age=_age,prev_num_card=previousNumCreditCards)

transactionConsumer = KafkaConsumer('NewTransactionData') 
def manageNewTransactionData():
	for msg in consumer:
		print msg.value
		con, meta = connect('beaker')
	    beaker = Table('transactions', meta, autoload=True)
	    i = beaker.insert()
	    i.execute(name=_name,card_type=cardType,transaction_type=transactionType,income=_income,region=_region,age=_age,prev_num_card=previousNumCreditCards,balance=_balance,max_limit=_limit,amount=_amount)

sched.add_job(manageNewCustomerData, 'interval', seconds=5)
sched.add_job(manageNewTransactionData, 'interval', seconds=5)
sched.add_job(manageNewTransactionData, 'interval', seconds=5)
sched.add_job(manageNewTransactionData, 'interval', seconds=5)


