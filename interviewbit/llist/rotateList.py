class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def __str__(self):
		return str(self.val) + str(self.next and (',' + str(self.next)) or ' *')

class Solution:
	def rotateRight(self, llist, n):
		if llist is None:
			return None
		head = llist
		tail = llist
		size = 1
		while (tail.next):
			tail = tail.next
			size += 1
		if size == 1:
			return llist
		n = n % size
		n = size - n
		for i in range(n):
			temp = head
			head = head.next
			temp.next = None
			tail.next = temp
			tail = temp
		return head

def build123(numR):
	head = None
	numR = numR[::-1]
	for i in numR:
		curr = ListNode(i)
		if head is None:
			head = curr
		else:
			curr.next = head
			head = curr
	return head

s = Solution()
# for i in range(11):
# 	print i, ':', s.rotateRight(build123(range(10)), i)

print s.rotateRight(build123([1, 2]), 2)