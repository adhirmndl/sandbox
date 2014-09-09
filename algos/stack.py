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

def revString(inString):
	temp = Stack()
	for e in inString:
		temp.push(e)
	newStr = ''
	while not temp.isEmpty():
		newStr += temp.pop()
	return newStr


if __name__ == "__main__":
	s=Stack()

	print(s.isEmpty())
	s.push(4)
	s.push('dog')
	print(s.peek())
	s.push(True)
	print(s.size())
	print(s.isEmpty())
	s.push(8.4)
	print(s.pop())
	print(s.pop())
	print(s.size())

	print revString("Python Stack")