import operator

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

	def setRootVal(self, key):
		self.key = key

	def __str__(self):
		return str(self.key) + ' [ ' + str(self.getLeftChild()) + ' ' + str(self.getRightChild()) + ' ]'

def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = []
	root   = BinaryTree('')
	pStack.append(root)
	curr   = root

	for i in fplist:
		if i == '(':
			curr.insertLeft('')
			pStack.append(curr)
			curr = curr.getLeftChild()
		elif i not in ['+', '-', '*', '/', ')']:
			curr.setRootVal(int(i))
			curr = pStack.pop()
		elif i in ['+' , '-', '*', '/']:
			curr.setRootVal(i)
			curr.insertRight('')
			pStack.append(curr)
			curr = curr.getRightChild()
		elif i == ')':
			curr = pStack.pop()
		else:
			raise ValueError
	return root

def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def evaluate(ptree):
	oper = { '+' : operator.add
				 , '-' : operator.sub
				 , '*' : operator.mul
				 , '/' : operator.truediv
				 }
	left  = ptree.getLeftChild()
	right = ptree.getRightChild()
	if left and right:
		fn = oper[ptree.getRootVal()]
		return fn(evaluate(left), evaluate(right))
	else:
		return ptree.getRootVal()

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print pt
print evaluate(pt)
