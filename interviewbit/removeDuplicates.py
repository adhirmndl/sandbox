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
    def __init__(self):
        self.tail = None
        self.head = None
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        dups = []
        curr = A
        prev = None
        while curr:
            if prev and prev.val == curr.val:
                dups.append(curr.val)
            prev = curr
            curr = curr.next
        dups = list(set(dups))
        curr = A
        while curr:
            if curr.val not in dups:
                self.insertAtEnd(curr.val)
            elif dups[0] < curr.val:
                dups = dups[1:]
            curr = curr.next

        return self.head

    def insertAtEnd(self, val):
        if self.tail is None:
            self.tail = ListNode(val)
            self.head = self.tail
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

def build123():
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)
    return head
s = Solution()
testL = build123()
print testL
print s.deleteDuplicates(testL)
