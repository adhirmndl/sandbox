class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

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
				print 'adding to left', newNode.data
			else:
				insPoint.right = newNode
				print 'adding to right', newNode.data
	def __str__(self):
		return self.printTree(self.root)

	def printTree(self, nodePtr):
		if not nodePtr:
			return ''
		tree = '[ '
		tree += self.printTree(nodePtr.left) + ','
		tree += str(nodePtr.data) + ','
		tree += self.printTree(nodePtr.right) + ' ]'
		return tree

if __name__ == "__main__":
	bTree = BST()
	bTree.addNode(Node(50))

	bTree.addNode(Node(10))
	bTree.addNode(Node(0))
	bTree.addNode(Node(20))

	bTree.addNode(Node(30))
	bTree.addNode(Node(70))
	bTree.addNode(Node(60))
	bTree.addNode(Node(90))
	print bTree