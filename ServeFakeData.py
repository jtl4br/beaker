import pandas as pd
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
    # do your stuff
    id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    cardType = random.randint(0,2)
    transactionType = random.randint(0,6)
    name = fake.name()
    region = random.randint(0,4) # SE, NE, NW, MW, SW
    income = np.random.normal(51000,15000, 1)[0]
    age = int(np.random.normal(37,15, 1)[0])
    previousNumCreditCards = random.randint(0,10)

    print id, cardType, transactionType, name, region, income, age, previousNumCreditCards

    if cardType == 0:
    	return 0
    elif cardType == 1:
    	return 1
    else:
    	return 2

def generateNewTransactionData():
    id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    cardType = random.randint(0,2)
    name = fake.name()
    region = random.randint(0,4) # SE, NE, NW, MW, SW
    income = max(0, np.random.normal(51000,15000, 1)[0])
    age = max(0, int(np.random.normal(37,15, 1)[0]))
    previousNumCreditCards = random.randint(0,10)
    print id, cardType, name, region, income, age, previousNumCreditCards


def generateNewTransactionData():
    id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    cardType = random.randint(0,2)
    transactionType = random.randint(0,6)
    name = fake.name()
    amount = max(0, np.random.normal(150,50, 1)[0])
    balance = max(0, np.random.normal(2000,750, 1)[0])
    limit = random.choice([500, 1000, 1500, 2000, 5000, 10000])
    region = random.randint(0,4) # SE, NE, NW, MW, SW
    income = max(0, np.random.normal(51000,15000, 1)[0])
    age = max(0, int(np.random.normal(37,15, 1)[0]))
    previousNumCreditCards = random.randint(0,10)
    print id, cardType, transactionType, name, amount, balance, limit, region, income, age, previousNumCreditCards


import logging
logging.basicConfig()

sched = BlockingScheduler()
sched.add_job(generateNewCustomerSignUpData, 'interval', seconds=30)
sched.add_job(generateNewTransactionData, 'interval', seconds=30)
sched.start()