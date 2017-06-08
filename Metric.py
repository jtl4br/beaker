from scipy import stats
import numpy as np
import datetime

class Metric():
	def __init__(self, _data):
		self.data = _data

	def calculate(self, args=None):
		return 0

	def stat(self, args=None):
		return 0


class RatioAmountToBalance(Metric):
	def calculate(self, args=None):
		ans = []
		for d in self.data:
			ratio = float(d[0])/d[1]
			ans.append(ratio)
		return ans

	def stat(self, args=None):
		mean = np.mean(args['ratios'])
		median = np.median(args['ratios'])
		stdDev = np.std(args['ratios'])
		var = np.var(args['ratios'])
		percentChanges = []
		
		for i in range(0, len(args['ratios']) - 1):
			x1 = args['ratios'][i]
			x2 = args['ratios'][i + 1]
			pChange = (x2 - x1)/x1
			percentChanges.append(pChange)

		return (mean, median, stdDev, var, percentChanges)

class NumCustomers(Metric):
	def calculate(self, args):
		numMonths = args['numMonths']
		ans = len(self.data)
		return ans

	def stat(self, args=None):
		mean = np.mean(self.numCustomersList)
		median = np.median(self.numCustomersList)
		stdDev = np.std(self.numCustomersList)
		var = np.var(self.numCustomersList)
		percentChanges = []
		
		for i in range(0, len(self.numCustomersList) - 1):
			x1 = self.numCustomersList[i]
			x2 = self.numCustomersList[i + 1]
			pChange = (x2 - x1)/x1
			percentChanges.append(pChange)

		return (mean, median, stdDev, var, percentChanges)
