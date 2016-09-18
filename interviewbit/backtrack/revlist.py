# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
		curr = A
		newhead = None
		while curr:
			temp = curr.next
			curr.next = newhead
			newhead = curr
			curr = temp
		return newhead
