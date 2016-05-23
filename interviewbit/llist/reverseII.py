class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def __str__(self):
		return str(self.val) + str(self.next and (',' + str(self.next)) or ' *')

class Solution:
	def reverseBetween(self, A, m, N):
		head = A
		if head == None or head.next == None:
			return head
		dummy = ListNode (0)
		dummy.next = head
		head1 = dummy
		for i in range (m - 1 ):
			head1 = head1.next
		p = head1.next
		for i in range (N - m):
			tmp = head1.next
			head1.next = p.next
			p.next = p.next.next
			head1.next.next = tmp
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
# print s.reverseBetween(build123([1,2,3]), 1, 2)
print s.reverseBetween(build123(range(1,8)), 1, 3)
# print s.reverseBetween(build123([97, 63, 89, 34, 82, 95, 4, 70, 14, 41, 38, 83, 49, 32, 68, 56, 99, 52, 33, 54]), 13, 15)
# print s.reverseBetween(build123([97, 63, 89, 34, 82, 95, 4, 70, 14, 41, 38, 83, 49, 32, 68, 56, 99, 52, 33, 54]), 13, 15)
