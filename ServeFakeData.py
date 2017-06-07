import numpy as np
import json

import string
import random
from apscheduler.schedulers.blocking import BlockingScheduler

import time

import sqlalchemy
from sqlalchemy import *
from faker import Factory
fake = Factory.create()


def connect(db, host='localhost', port=5432):
	# We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}/{}'
    url = url.format(host, port, db)

    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta


def generateNewCustomerSignUpData(): 
    _id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    cardType = random.randint(0,2)
    _name = fake.name()
    _region = random.randint(0,4) # SE, NE, NW, MW, SW
    _income = max(0, np.random.normal(51000,15000, 1)[0])
    _age = max(0, int(np.random.normal(37,15, 1)[0]))
    previousNumCreditCards = random.randint(0,10)

    con, meta = connect('beaker')
    beaker = Table('customer', meta, autoload=True)
    i = beaker.insert()
    i.execute(name=_name,card_type=cardType,region=_region,income=_income,age=_age,prev_num_card=previousNumCreditCards)
    print _id, cardType, _name, _region, _income, _age, previousNumCreditCards

def generateNewTransactionData():
    _id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    cardType = random.randint(0,2)
    transactionType = random.randint(0,6)
    _name = fake.name()
    _amount = max(0, np.random.normal(150,50, 1)[0])
    _balance = max(0, np.random.normal(2000,750, 1)[0])
    _limit = random.choice([500, 1000, 1500, 2000, 5000, 10000])
    _region = random.randint(0,4) # SE, NE, NW, MW, SW
    _income = max(0, np.random.normal(51000,15000, 1)[0])
    _age = max(0, int(np.random.normal(37,15, 1)[0]))
    previousNumCreditCards = random.randint(0,10)

    con, meta = connect('beaker')
    beaker = Table('transactions', meta, autoload=True)
    i = beaker.insert()
    i.execute(name=_name,card_type=cardType,transaction_type=transactionType,income=_income,region=_region,age=_age,prev_num_card=previousNumCreditCards,balance=_balance,max_limit=_limit,amount=_amount)
    print _id, cardType, transactionType, _name, _amount, _balance, _limit, _region, _income, _age, previousNumCreditCards


import logging
logging.basicConfig()

sched = BlockingScheduler()
sched.add_job(generateNewCustomerSignUpData, 'interval', seconds=10)
sched.add_job(generateNewTransactionData, 'interval', seconds=10)
sched.start()