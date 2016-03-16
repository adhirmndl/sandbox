class Node():
	value = None
	nxt   = None
	def __init__(self, value):
		self.value = value

class Stack():
	head = None
	def empty(self):
		return self.head == None

	def push(self, element):
		newNode = Node(element)
		if self.head == None:
			self.head = newNode
		else:
			newNode.nxt = self.head
			self.head = newNode

	def pop(self):
		if not self.empty():
			val = self.head.value
			self.head = self.head.nxt
			return val
		else:
			print '-- we are empty'
			return None

	def top(self):
		return self.head.value

	def printStack(self):
		tempHead = self.head
		while(tempHead):
			print tempHead.value
			tempHead = tempHead.nxt

if __name__ == '__main__':
	st = Stack()
	st.push(15)
	st.push(6)
	st.push(2)
	st.push(9)
	st.printStack()
	print st.pop()
	print st.pop()
	print st.pop()
	print st.pop()
	print st.pop()
