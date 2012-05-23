import time

class Throttler(object) :
	def __init__(self, thr_set) :
		if not thr_set :
			self.thr_count = 0
			self.thr_period = 0
		else :
			self.thr_count, self.thr_period = thr_set
			self.tsset = list()
	def check(self) :
		if not self.thr_count :
			return True

		# expire timestamps
		self.tsset = [ts for ts in self.tsset if ts >= time.time() - self.thr_period]

		if len(self.tsset) > self.thr_count :
			return False
		else :
			self.tsset.append(time.time())
			return True
