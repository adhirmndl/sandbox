class BinaryTree:
	def __init__(self, root):
		self.key   = root
		self.left  = None
		self.right = None

	def insertLeft(self, newNode):
		if self.left is None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp

	def insertRight(self, newNode):
		if self.right is None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp

	def getRightChild(self):
		return self.right

	def getLeftChild(self):
		return self.left

	def getRootVal(self):
		return self.key

	def setRootVal(key):
		self.key = key

