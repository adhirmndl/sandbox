# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
    	return '[' + str(self.start) + ', ' + str(self.end) + ']'

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
    	o_intervals = []
    	self.clean(intervals)
    	self.clean([new_interval])
    	for i in intervals:
    		if self.isOverlap(i, new_interval):
    			o_intervals.append(i)
    	m_interval = self.mergeIntervals(o_intervals, new_interval)

    	if len(o_intervals) == 0:
    		pos = 0
	    	for i in intervals:
	    		if i.start < m_interval.start:
	    			pos += 1
	    	intervals.insert(pos, m_interval)
	    	return intervals

    	res = []
    	appended = False
    	for i in intervals:
    		if i.start < m_interval.start or i.end > m_interval.end:
    			res.append(i)
    		elif not appended:
    			res.append(m_interval)
    			appended = True
    	return res

    def isOverlap(self, i1, i2):
    	return not (max(i1.start, i2.start) > min(i1.end, i2.end))

    def mergeIntervals(self, overlaps, new):
    	for interval in overlaps:
    		new.start = min(interval.start, new.start)
    		new.end   = max(interval.end, new.end)
    	return new    	

    def clean(self, intervals):
    	for i in intervals:
    		if i.start > i.end:
    			tmp = i.start
    			i.start = i.end
    			i.end = tmp

    def merge(self, intervals):
    	res = []
    	for i in intervals:
    		res = self.insert(res, i)
    	return res

s = Solution()
# res = s.insert([Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(16,12)], Interval(4,9))
# res = s.insert([Interval(1,2), Interval(3,6)], Interval(8,10))
res = s.merge([Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)])
print res
