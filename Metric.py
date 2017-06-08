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

class NumTransactionsPastXMonths(Metric):
	def monthdelta(date, delta):
	    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
	    if not m: m = 12
	    d = min(date.day, [31,
	        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
	    return date.replace(day=d,month=m, year=y)

	def calculate(self, args={'numMonths': -1}):
		numMonths = args['numMonths']
		ans = 0
		if numMonths == -1:
			ans = len(data)
			self.numTransactionsList.append(ans)
		else:
			num = 0
			XMonthsDateTime = monthdelta(datetime.now(), -1*numMonths)
			for d in self.data:
				if d[] < XMonthsDateTime:
					num += 1
			self.numTransactionsList.append(num)
			ans = num
		return ans

	def stat(self, args=None):
		mean = np.mean(self.numTransactionsList)
		median = np.median(self.numTransactionsList)
		stdDev = np.std(self.numTransactionsList)
		var = np.var(self.numTransactionsList)
		percentChanges = []
		
		for i in range(0, len(self.numTransactionsList) - 1):
			x1 = args['ratios'][i]
			x2 = args['ratios'][i + 1]
			pChange = (x2 - x1)/x1
			percentChanges.append(pChange)

		return (mean, median, stdDev, var, percentChanges)
