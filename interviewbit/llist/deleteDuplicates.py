class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def __str__(self):
		return str(self.val) + str(self.next and (',' + str(self.next)) or ' *')

class Solution:
	def deleteDuplicates(self, llist):
		if llist is None:
			return None
		prev = llist
		curr = llist.next
		while curr is not None:
			if curr.val == prev.val:
				prev.next = curr.next
				curr = curr.next
			else:
				prev = curr
				curr = curr.next
		return llist

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

llist  = build123([1]*2 + range(2,10))
s = Solution()
print s.removeDups(llist)
print s.removeDups(None)
print s.removeDups(ListNode(1))
print s.removeDups(build123([1]*2))
print s.removeDups(build123(range(5) + [6]*3 + range(7,10)))
