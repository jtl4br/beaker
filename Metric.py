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
			ans.append((d[], ratio)) #(date, value)
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
			percentChanges.append((self.data[], pChange)) #(date, value)

		return (mean, median, stdDev, var, percentChanges)

class NumCustomers(Metric):
	def calculate(self, args):
		ans = (self.data[-1][ ], len(self.data)) #(date, value)
		self.numCustomersList.append(ans)
		return ans

	def stat(self, args=None):
		dates = [a[0] for a in self.numCustomersList]
		x = [a[1] for a in self.numCustomersList]

		mean = np.mean(x)
		median = np.median(x)
		stdDev = np.std(x)
		var = np.var(x)
		percentChanges = []
		
		for i in range(0, len(x) - 1):
			x1 = x[i]
			x2 = x[i + 1]
			pChange = (x2 - x1)/x1
			percentChanges.append((dates[i+1], pChange)) #(date, value)

		return (mean, median, stdDev, var, percentChanges)
