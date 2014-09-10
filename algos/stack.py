class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, e):
		self.items.append(e)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def size(self):
		return len(self.items)
	def __str__(self):
		return '[' + ' '.join(self.items) + ']' 

def revString(inString):
	temp = Stack()
	for e in inString:
		temp.push(e)
	newStr = ''
	while not temp.isEmpty():
		newStr += temp.pop()
	return newStr

def parChecker(theString):
	s = Stack()
	leftB 	= ['[', '{', '(']
	rightB 	= [']', '}', ')']

	for e in theString:
		if (not e in leftB) and (not e in rightB):
			continue
		if e in leftB:
			s.push(e)
		if e in rightB:
			if s.isEmpty():
				return False
			lB = s.pop()
			if leftB.index(lB) != rightB.index(e):
				return False
	if s.isEmpty():
		return True
	else:
		return False

def in2post(expression):
	lB 	= ['[', '{', '(']
	rB 	= [']', '}', ')']
	prec = {}
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	opStack = Stack()
	post = []

	for e in expression.split():
		if e in lB:
			opStack.push(e)
		elif e in rB:
			if opStack.isEmpty():
				raise RuntimeError("Invalid Expression")
			while opStack.peek() not in lB:
				post.append(opStack.pop())
			opStack.pop()
		elif e in prec.keys():
			if not opStack.isEmpty():
				top = opStack.peek()
				while top in prec.keys() and prec[top] >= prec[e] and not opStack.isEmpty():
					post.append(opStack.pop())
			opStack.push(e)
		else:
			post.append(e)
		# print ''.join(post), opStack

	while not opStack.isEmpty():
		post.append(opStack.pop())

	return ''.join(post)

def in2pre(expression):
	lB 	= ['[', '{', '(']
	rB 	= [']', '}', ')']
	prec = {}
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	opStack = Stack()
	post = []

	for e in expression.split():
		if e in lB:
			opStack.push(e)
		elif e in rB:
			if opStack.isEmpty():
				raise RuntimeError("Invalid Expression")
			while opStack.peek() not in lB:
				post.append(opStack.pop())
			opStack.pop()
		elif e in prec.keys():
			if not opStack.isEmpty():
				top = opStack.peek()
				while top in prec.keys() and prec[top] >= prec[e] and not opStack.isEmpty():
					post.append(opStack.pop())
			opStack.push(e)
		else:
			post.append(e)
		# print ''.join(post), opStack

	while not opStack.isEmpty():
		post.append(opStack.pop())

	return ''.join(post)

if __name__ == "__main__":
	# s=Stack()

	# print(s.isEmpty())
	# s.push(4)
	# s.push('dog')
	# print(s.peek())
	# s.push(True)
	# print(s.size())
	# print(s.isEmpty())
	# s.push(8.4)
	# print(s.pop())
	# print(s.pop())
	# print(s.size())

	# print revString("Python Stack")

	# print(parChecker('((()))'))
	# print(parChecker('(()'))
	# print(parChecker('(2  4))'))

	print in2post("A * B + C * D")
	print in2post("( A + B ) * C - ( D - E ) * ( F + G )")
