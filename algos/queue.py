#!/bin/python
#queue.py

class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self):
		return self.items.pop(0)
	def isEmpty(self):
		return len(self.items) == 0
	def size(self):
		return len(self.items)

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

if __name__ == "__main__":
	# q = Queue()
	# q.enqueue(4)
	# q.enqueue('dog')
	# q.enqueue(True)
	# print q.size()
	# print q.isEmpty()
	# q.enqueue(8.4)
	# print q.dequeue()
	# print q.dequeue()
	# print q.size()

	print hotPotato(['C0', 'C1', 'C2', 'C3', 'C4', 'C5'], 7)
