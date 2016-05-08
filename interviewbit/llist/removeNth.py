class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def __str__(self):
		return str(self.val) + str(self.next and (',' + str(self.next)) or ' *')

class Solution:
	def removeNthFromEnd(self, llist, n):
		n += 1
		if llist is None:
			return None
		curr = llist
		nth  = llist
		while n > 0:
			if nth is None:
				llist = llist.next
				return llist
			nth = nth.next
			n -= 1
		while nth is not None:
			nth  = nth.next
			curr = curr.next
		# print 'curr: ' , curr
		if curr.next is not None:
			curr.next = curr.next.next
		else:
			curr.next = None
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

s = Solution()
for i in range(11):
	print i, ':', s.removeNthFromEnd(build123(range(10)), i)
print s.removeNthFromEnd(build123([1]), 0)
print s.removeNthFromEnd(build123([1]), 1)
print s.removeNthFromEnd(build123([1]), 2)
print s.removeNthFromEnd(build123([1,2]), 0)
print s.removeNthFromEnd(build123([1,2]), 1)
print s.removeNthFromEnd(build123([1,2]), 2)
print s.removeNthFromEnd(build123([1,2,3]), 0)
print s.removeNthFromEnd(build123([1,2,3]), 1)
print s.removeNthFromEnd(build123([1,2,3]), 2)
print s.removeNthFromEnd(build123([1,2,3,4,5]), 0)
print s.removeNthFromEnd(build123([1,2,3,4,5]), 1)
print s.removeNthFromEnd(build123([1,2,3,4,5]), 2)
# print s.removeNthFromEnd(None, 2)
# print s.removeNthFromEnd(ListNode(1),1)
