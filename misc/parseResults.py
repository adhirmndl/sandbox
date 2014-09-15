import csv
import numpy as np 
import itertools

def main(fname):
	with open(fname, 'rb') as statfile:
		statfile = statfile.read().splitlines()
		stats = csv.reader(statfile, delimiter=',')
		stats.next() 
		header = stats.next()
		stats.next()
		data = stats.next()
		# print data 
		nList = isplit(data, ('Link Up',))
		i = 1
		for l in nList[1:-1]:
			print '\nPort' + str(i) 
			print 'Frames Sent: ', l[1]
			print 'Valid Frames Received: ', l[3]
			print 'Bytes Sent: ', l[5]
			print 'Bytes Received: ', l[7]
			print 'Transmit Duration: ', l[38]
			print 'Scheduled Frames Sent: ', l[42]

			i +=1

def isplit(iterable,spliters):
    return [list(g) for k,g in itertools.groupby(iterable,lambda x:x in spliters) if not k]


if __name__ == "__main__":
	main('abc.csv')