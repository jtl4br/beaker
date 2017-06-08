import numpy as np
import json
import string
import random
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import datetime
import sqlalchemy
from sqlalchemy import *
from faker import Factory
import logging
fake = Factory.create()
from kafka import KafkaProducer

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def connect(db, host='localhost', port=5432):
    # We connect with the help of the PostgreSQL URL
    # postgresql://user:passlocalhost:5432/database
    print 'Connecting...'
    url = 'postgresql://{}:{}/{}'
    url = url.format(host, port, db)
    print url

    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con, meta

con, meta = connect('beaker')

def generateNewCustomerSignUpData(): 
    _id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    _cardType = random.randint(0,2)
    _name = fake.name()
    _region = random.randint(0,4) # SE, NE, NW, MW, SW
    _income = random.randint(0,4)
    _age = max(0, int(np.random.normal(37,15, 1)[0]))
    _previousNumCreditCards = random.randint(0,10)
    _date = str(datetime.datetime.now())

    # data = {'id':_id, 'cardType':_cardType, 'date':_date, 'name': _name, 'region': _region, 'income': _income, 'age': '_age', 'previousNumCreditCards': _previousNumCreditCards}
    # producer.send('main', data)

    beaker = Table('customer', meta, autoload=True)
    i = beaker.insert()
    i.execute(name=_name,card_type=_cardType,region=_region,income=_income,age=_age,prev_num_card=_previousNumCreditCards)
    
    print _id, _cardType, _name, _region, _income, _age, _previousNumCreditCards

def generateNewTransactionData():
    _id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    _cardType = random.choice(['silver', 'gold', 'platinum'])
    _transactionType = random.randint(0,6)
    _name = fake.name()
    _amount = max(0, np.random.normal(150,50, 1)[0])
    _balance = max(0, np.random.normal(2000,750, 1)[0])
    _limit = random.choice([500, 1000, 1500, 2000, 5000, 10000])
    _region = random.randint(0,2) # SE, NE, NW, MW, SW
    _income = random.randint(0,2)
    _age = max(0, int(np.random.normal(37,15, 1)[0]))
    _previousNumCreditCards = random.randint(0,10)
    _date = str(datetime.datetime.now())

    # data = {'id':_id, 'date':_date, 'cardType':_cardType, 'transactionType':_transactionType, 'name': _name, 'amount': _amount, 'balance':_balance, 'limit':_limit, 'region': _region, 'income': _income, 'age': _age, 'previousNumCreditCards': _previousNumCreditCards}
    # producer.send('main', data)

    table = Table('transactions', meta, autoload=True)
    i = table.insert()
    i.execute(name=_name,card_type=_cardType,transaction_type=_transactionType,income=_income,region=_region,age=_age,prev_num_card=_previousNumCreditCards,balance=_balance,max_limit=_limit,amount=_amount)
    
    print _id, _cardType, _transactionType, _name, _amount, _balance, _limit, _region, _income, _age, _previousNumCreditCards


logging.basicConfig()
sched = BlockingScheduler()
sched.add_job(generateNewCustomerSignUpData, 'interval', seconds=5)
sched.add_job(generateNewTransactionData, 'interval', seconds=5)
sched.start()