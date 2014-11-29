#banktree.py
class Node:
	def __init__(self, parent, n, prob):
		self.n = n
		self.prob = prob
		self.parent = parent 
		self.children = []
	def __str__(self):
		return '[ node: ' + str(self.n) + ' | parent: ' + str(self.parent) + ' | prob: ' + str(self.prob) + ' ] '

class BankTree:
	def __init__(self):
		self.root = Node(None, 1, 1)
		self.nodeTable = {1:self.root}
	def addBranch(self, parent, current, prob):
		parentNode = self.nodeTable[parent]
		newNode = Node(parentNode, current, prob)
		parentNode.children.append(newNode)
		self.nodeTable[current] = newNode
		#print newNode
	def findPathProbability(self, fromBranch, toBranch):
		fromBranch = self.nodeTable[fromBranch]
		toBranch = self.nodeTable[toBranch]

		for cBranch in fromBranch.children:
			findPathProbability(cBranch)
		#if the parent is the node you are seeking
		if fromBranch.parent == toBranch:
			return fromBranch.prob
		else:
			return

	def pathToRoot(self, branch):
		if branch.parent == None:
			return [(branch.n, branch.prob)];
		path = [(branch.n, branch.prob)]
		path.extend(self.pathToRoot(branch.parent))
		return path

if __name__ == "__main__":
	n = input()
	bTree = BankTree()
	for _ in range(n - 1):
		parent, current, prob = map(int, raw_input().strip().split(' '))
		bTree.addBranch(parent, current, prob/100.00)
	nTests = input()
	for _ in range(nTests):
		fromBranch, toBranch, prob = map(float, raw_input().strip().split(' '))
		fromBranch = int(fromBranch)
		toBranch = int(toBranch)
		fromPath = bTree.pathToRoot(bTree.nodeTable[fromBranch])
		toPath = bTree.pathToRoot(bTree.nodeTable[toBranch])	

		path = list(set(fromPath)^set(toPath))
		commonpath = list(set(fromPath)&set(toPath))
		# print "pathB : " + str(path)
		if commonpath[0] not in path and commonpath[0][0] != fromBranch and commonpath[0][0] != toBranch:
			path.append(commonpath[0])

		# print "path: " + str(path)
		# print "common: " + str(commonpath)

		pathProb = 1
		for (n, p) in path:
			pathProb *= p
		# print pathProb

		targetProb = pow(10, prob)

		# print "pathProb: " + str(pathProb)
		# print "targetProb: " + str(targetProb)
		if pathProb >= targetProb:
			print "YES"
		else:
			print "NO"