class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def setData(self, newData):
		self.data = newData
	def getData(self):
		return self.data
	def setNext(self, node):
		self.next = node
	def getNext(self):
		return self.next

class UnList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None
	def add(self, item):
		n = Node(item)
		n.setNext(self.head)
		self.head = n
	def size(self):
		count = 0
		tempH = self.head
		while tempH != None:
			count += 1
			tempH = tempH.getNext()
		return count
	def search(self, item):
		cur = self.head
		while cur != None:
			if cur.getData() == item:
				return True
			cur = cur.getNext()
		return False
	def remove(self, item):
		cur = self.head
		while cur != None:
			if cur.getData() == item:
				temp = cur.getNext()
				cur.data = temp.getData()
				cur.setNext(temp.getNext())
				return True
			cur = cur.getNext()
		return False

if __name__ == "__main__":
	testList = UnList()
	testList.add(32)
	testList.add("fad")
	testList.add(23.32)

	print testList.size()
	print testList.search("fad")
	print testList.remove("fad")
	print testList.search("fad")
	print testList.size()