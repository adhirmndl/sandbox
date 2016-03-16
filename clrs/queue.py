class Node():
	value = None
	nxt   = None
	def __init__(self, value):
		self.value = value

class Queue():
	head = None
	tail = None

	def empty(self):
		return (self.head == None and self.tail == None)

	def enqueue(self, element):
		newNode = Node(element)
		if (self.head == None):
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.nxt = newNode
			self.tail = newNode

	def dequeue(self):
		if not self.empty():
			val = self.head.value
			self.head = self.head.nxt
			if self.head == None:
				self.head = None
				self.tail = None
			return val
		else:
			print 'we are empty'
			return None

	def printQueue(self):
		tempHead = self.head
		while(tempHead):
			print tempHead.value
			tempHead = tempHead.nxt

if __name__ == '__main__':
	q = Queue()
	q.enqueue(15)
	q.enqueue(6)
	q.enqueue(2)
	q.enqueue(9)
	q.printQueue()
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()
