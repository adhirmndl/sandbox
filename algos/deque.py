class Deque:
	def __init__(self ):
		self.items = []
	def addFront(self, item):
		self.items.insert(0, item)
	def addRear(self, item):
		self.items.append(item)
	def removeFront(self):
		if not self.isEmpty():
			return self.items.pop(0)
		else:
			raise RuntimeError("Q Empty")
	def removeRear(self):
		if not self.isEmpty():
			return self.items.pop()
		else:
			raise RuntimeError("Q Empty")
	def isEmpty(self):
		return len(self.items) == 0
	def size(self):
		return len(self.items)
	def __str__(self):
		return ' '.join(self.items)

def palchecker(pal):

	d = Deque()
	for e in pal:
		d.addRear(e)
	while d.size() > 1:
		if d.removeRear() != d.removeFront():
			return False
	return True

if __name__ == "__main__":
	d = Deque()
	d.addFront("Yoo")
	print d

	print palchecker("radar")
	print palchecker("test")