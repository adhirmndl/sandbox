# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from sets import Set
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
    	bSet = Set()
    	currB = B
    	while currB:
    		bSet.add(currB)
    		currB = currB.next

    	currA = A
    	while currA:
    		if currA in bSet:
    			return currA
    		currA = currA.next
    	return currA

if __name__=="__main__":
