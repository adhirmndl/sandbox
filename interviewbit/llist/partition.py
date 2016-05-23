class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def __str__(self):
		return str(self.val) + str(self.next and (',' + str(self.next)) or ' *')

class Solution:
	def partition(self, head, x):
		if head == None or head.next == None:
			return head
		dummy = ListNode(0)
		dummy.next = head
		ip = dummy
		curr  = head.next
		prev  = head
		while prev.val < x and curr:
			ip = ip.next
			curr  = curr.next
			prev  = prev.next
		while curr:
			if curr.val < x:
				prev.next = curr.next
				curr.next = ip.next
				ip.next   = curr
				ip = ip.next
				curr = prev.next
			else:
				curr = curr.next
				prev = prev.next
		return dummy.next

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
# print s.partition(build123([1,4,3,2,5,2]), 3)
print s.partition(build123([1,2,3,4,5]), 5)
print s.partition(build123([1]), 1)
print s.partition(build123([1,2]), 1)
print s.partition(build123([3,1,2]), 3)
# print s.partition(build123(range(1,8)), 1, 3)
# print s.partition(build123([97, 63, 89, 34, 82, 95, 4, 70, 14, 41, 38, 83, 49, 32, 68, 56, 99, 52, 33, 54]), 13, 15)
# print s.partition(build123([97, 63, 89, 34, 82, 95, 4, 70, 14, 41, 38, 83, 49, 32, 68, 56, 99, 52, 33, 54]), 13, 15)
