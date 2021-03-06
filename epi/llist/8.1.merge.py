class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def __str__(self):
		return str(self.val) + str(self.next and (',' + str(self.next)) or ' *')

def mergeTwoLists(left, right):
	if left is None:
		return right
	if right is None:
		return left

	merged = None
	mptr   = None
	while left is not None and right is not None:
		val = 0
		if left.val <= right.val:
			val = left.val
			left = left.next
		else:
			val = right.val
			right = right.next
		node = ListNode(val)
		if merged is None:
			merged = node
			mptr   = node
		else:
			mptr.next = node
			mptr = node
	while left is not None:
		node = ListNode(left.val)
		if merged is None:
			merged = node
			mptr   = node
		else:
			mptr.next = node
			mptr = node
		left = left.next
	while right is not None:
		node = ListNode(right.val)
		if merged is None:
			merged = node
			mptr   = node
		else:
			mptr.next = node
			mptr = node
		right = right.next
	return merged

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

def merge(left, right):
	currL = left
	currR = right
	merged = None

left  = build123(range(2,10,3))
right = build123(range(3,10,2))
print left
print right
print mergeTwoLists(left, right)
print mergeTwoLists(None, right)
print mergeTwoLists(left, ListNode(1))
