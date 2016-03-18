# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
    	if self is None:
    		return '[]'
    	return str(self.val) + ', ' + str(self.next)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list

    def __init__(self):
    	self.head = None
    def deleteDuplicates(self, A):
    	self.head = A
    	prev = None
    	curr = A
    	dups = []
    	while curr:
    		if prev and curr.val == prev.val:
    			prev.next = curr.next
    			if curr.val not in dups:
    			    dups.append(curr.val)
    		else:
    			prev = curr
    		curr = curr.next
    	curr = self.head
    	while curr:
    		if curr.val in dups:
    			self.delete(curr.val)
    		curr = curr.next
    	return self.head

    def delete(self, val):
    	prev = None
    	curr = self.head
    	found = False
    	while curr and found is False:
    		if curr.val == val:
    			found = True
    		else:
    			prev = curr
    			curr = curr.next
    	if prev is None:
    		self.head = curr.next
    	else:
    		prev.next = curr.next
    	print 'a', self.head

def build123():
	head = ListNode(1)
	head.next = ListNode(1)
	head.next.next = ListNode(2)
	head.next.next.next = ListNode(2)
	head.next.next.next.next = ListNode(3)
	return head

s = Solution()
testL = build123()
print testL
print s.deleteDuplicates(testL)
print testL
