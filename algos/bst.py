class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.p = None
	def __str__(self):
		return 'node: ' + str(self.data)

class BST:
	def __init__(self):
		self.root = None
	def addNode(self, newNode):
		if not self.root:
			self.root = newNode
		else:
			curr = self.root
			insPoint = None
			while curr:
				insPoint = curr
				if newNode.data < curr.data:
					curr = curr.left
				else:
					curr = curr.right
			if insPoint.data > newNode.data:
				insPoint.left = newNode
				# print 'adding to left', newNode.data
			else:
				insPoint.right = newNode
				# print 'adding to right', newNode.data
			newNode.p = insPoint
	def __str__(self):
		return self.inOrder(self.root)

	def inOrder(self, nodePtr):
		if not nodePtr:
			return ''
		tree = '[ '
		tree += self.inOrder(nodePtr.left)
		tree += str(nodePtr.data)
		tree += self.inOrder(nodePtr.right) + ' ]'
		return tree

	def search(self, x, data):
		if not x:
			return None 
		if x.data == data:
			return x 
		if data < x.data:
			return self.search(x.left, data)
		else:
			return self.search(x.right, data)

	def tmin(self, x):
		if not x:
			return None
		if not x.left:
			return x.data 
		return self.tmin(x.left)

	def tmax(self, x):
		if not x:
			return None
		if not x.left:
			return x.data 
		return self.tmax(x.right)

	def successor(self, x):
		if x.right:
			return self.tmin(x.right)
		y = x.p
		while y != None and x == y.right:
			x = y
			y = y.p
		return y

if __name__ == "__main__":
	bTree = BST()
	# construct tree
	bTree.addNode(Node(50))
	bTree.addNode(Node(10))
	bTree.addNode(Node(0))
	bTree.addNode(Node(-10))
	bTree.addNode(Node(5))
	bTree.addNode(Node(20))
	bTree.addNode(Node(30))
	bTree.addNode(Node(70))
	bTree.addNode(Node(60))
	bTree.addNode(Node(90))
	print bTree

	# search	
	print bTree.search(bTree.root, 90)
	print bTree.search(bTree.root, 34)

	# minimum
	print bTree.tmin(bTree.root)

	#maximum
	print bTree.tmax(bTree.root)
	
	#successor
	print bTree.successor(bTree.search(bTree.root, 30))