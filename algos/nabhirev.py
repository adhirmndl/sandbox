class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def __str__(self):
		listStr = ''
		cur = self
		while cur:
			listStr += str(cur.data) + ', '
			cur = cur.next
		return listStr[:-2]+']'

class LList:
	def __init__(self):
		self.head = None
	def insert(self, data):
		temp = Node(data)
		temp.next = self.head
		self.head = temp
	def __str__(self):
		cur = self.head
		listStr = ''
		while cur:
			listStr += str(cur.data) + ', '
			cur = cur.next
		return '['+listStr[:-2]+']'
	# tweaked nabhi's algo
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
# nabhi's algo
def nabhirev(a, b, c):
	a.next = None
	while b:
		b.next = a
		a = b
		b = c
		if c.next:
			c = c.next
		else:
			b = None
			c.next = a
			a = c
		# print a
		# print b
		# print c
	print a

# recursive reverse
def revRecursive(node):
	if node == None:
		return None
	if node.next == None:
		return node
	b = node.next
	node.next = None
	tempNode = revRecursive(b)
	b.next = node 
	return tempNode

if __name__ == "__main__":
	l = LList()
	for i in range(10):
		l.insert(i)
	# print l
	# print l.head
	l.reverse()
	print l

	node = revRecursive(l.head)
	print node

	a = node
	b = node.next
	c = node.next.next
	nabhirev(a, b, c)
