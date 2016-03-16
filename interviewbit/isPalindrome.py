# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self is None:
            return []
        return str(self.val) + ',' + str(self.next)

from sets import Set
class Solution:
    # @param A : head node of linked list
    # @return True/False
    def isPalindrome(self, A):
        length = self.length(A)
        count = 1
        head = A

        curr = A
        while count != length/2:
            curr = curr.next
            count += 1
        tail = curr.next
        if length % 2 != 0:
            tail = tail.next
        curr.next = None
        return self.list_equal(head, self.reverseList(tail))

    def reverseList(self, A):
        curr = A
        nxt  = None
        prev = None
        while curr:
            nxt      = curr.next
            curr.next = prev
            prev     = curr
            curr     = nxt
        A = prev
        return A         

    def length(self, A):
        count = 0
        curr = A
        while curr:
            count += 1
            curr = curr.next
        return count

    def list_equal(self, listA, listB):
        currA = listA
        currB = listB
        while(currA and currB):
            if currA.val != currB.val:
                return False
            currA = currA.next
            currB = currB.next
        if currA or currB:
            return False
        return True

def build123():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    return head

def build123456():
    head = build123()
    head.next.next.next = build123()
    return head

if __name__=="__main__":
    list1 = build123()
    s = Solution()
    print s.isPalindrome(build123())