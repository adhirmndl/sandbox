from __future__ import division
import unittest

class GreedyScheduler:
	def schedule(self, joblist, func):
		joblist.sort(key = func, reverse = True)
		elapsedlength = 0
		weightedsum   = 0
		for job in joblist:
			# print 'job', job, 'diff', job[0] - job[1], 'div', job[0] / job[1]
			weightedsum   += (job[1] + elapsedlength) * job[0]
			elapsedlength += job[1]
		return weightedsum

	def diff(self, job):
		return (job[0] - job[1], job[0])

	def div(self, job):
		return (job[0] / job[1], job[0])

class GreedyScheduleTester(unittest.TestCase):
	def testSimpleDiv(self):
		gs = GreedyScheduler()
		weight = gs.schedule([(1,2), (3, 5)], gs.div)
		self.assertEquals(weight, 22)

	def testSimpleDiff(self):
		gs = GreedyScheduler()
		weight = gs.schedule([(1,2), (3, 5)], gs.diff)
		self.assertEquals(weight, 23)

	def testInputDiv(self):
		data = file2list('jobs_input.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.div)
		self.assertEquals(weight, 67311454237)

	def testDiff6(self):
		data = file2list('jobs_6.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.diff)
		self.assertEquals(weight, 31814)

	def testDiv6(self):
		data = file2list('jobs_6.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.div)
		self.assertEquals(weight, 31814)

	def testDiff10(self):
		data = file2list('jobs_10.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.diff)
		self.assertEquals(weight, 61545)

	def testDiv10(self):
		data = file2list('jobs_10.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.div)
		self.assertEquals(weight, 60213)

	def testDiff32(self):
		data = file2list('jobs_32.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.diff)
		self.assertEquals(weight, 688647)

	def testDiv32(self):
		data = file2list('jobs_32.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.div)
		self.assertEquals(weight, 674634)

	def testInputDiff(self):
		data = file2list('jobs_input.txt')
		gs = GreedyScheduler()
		weight = gs.schedule(data, gs.diff)
		self.assertEquals(weight, 69119377652)

	def testfile2list(self):
		tuple_list = file2list('jobs_input.txt')
		self.assertEquals(len(tuple_list), 10000)

def file2list(filename):
	f = open(filename)
	content = f.readlines()
	n = int(content[0])
	data = content[1:]
	tuple_list = []
	for l in data:
		line = l.split()
		tuple_list.append((int(line[0]), int(line[1])))
	return tuple_list

if __name__ == "__main__":
	unittest.main()