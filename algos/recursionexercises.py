def factorial(n):
	if n == 1 or n == 0:
		return 1
	return n * factorial(n - 1)

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LList:
	def __init__(self, data):
		self.head = Node(data)
		self.head.next = None	
	def insert(self, data):
		temp = Node(data)
		temp.data = data
		temp.next = self.head
		self.head = temp
	def insertNode(self, node):
		node.next = self.head
		self.head = node

	def __str__(self):
		cur = self.head
		lStr = ''
		while cur != None:
			lStr += str(cur.data) + ', '
			cur = cur.next
		return lStr[:-2]

	def reverse(self):
		prev = None
		cur = self.head
		next = None
		while cur:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		self.head = prev

if __name__ == "__main__":
	l = LList(10)
	for i in range(5):
		l.insert(i)
	print l
	l.reverse()
	print l 
