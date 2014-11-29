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
	def __str__(self):
		cur = self.head
		temp = []
		while cur:
			temp.append(cur.data)
			cur = cur.next
		return str(temp)

def mergeLists(lone, ltwo):
	return
	
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

	listOne = UnList()
	for i in range(5):
		listOne.add(i)

	for i in range(10,15):
		listOne.add(i)

	print listOne

	listTwo = UnList()
	for i in range(5,10):
		listTwo.add(i)

	for i in range(15,20):
		listTwo.add(i)

	print listTwo

	mergeLists(listOne, listTwo)
