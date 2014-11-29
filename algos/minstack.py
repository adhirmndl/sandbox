class MinStack:
	def __init__(self):
		self.stack = []
		self.minStack = []
	def size(self):
		return len(self.stack)		
	def push(self, e):
		self.stack.append(e)
		if self.empty():
			raise Exception("stack empty")	
		if len(self.minStack) == 0 or e <= self.minStack[-1]:
			self.minStack.append(e)
	def pop(self):
		if self.empty():
			raise Exception("stack empty")	
		top = self.stack[-1]
		self.stack = self.stack[:-1]
		if self.minStack[-1] == top:
			self.minStack = self.minStack[:-1]
		return top
	def min(self):
		return self.mine
	def empty(self):
		return len(self.stack) <= 0

	def __str__(self):
		return "contents: " + str(self.stack) + "\nmin: " + str(self.minStack)

if __name__ == "__main__":
	ms = MinStack()
	for i in range(10):
		ms.push(i)
		print ms 
	ms.push(0)
	print ms 
	for i in range(10):
		ms.pop()
		print ms


