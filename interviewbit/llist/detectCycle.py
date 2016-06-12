# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self is None:
            return []
        return str(self.val) + ',' + str(self.next)

class Solution:
    # @param A : head node of linked list
    # @return True/False
    def detectCycle(self, head):
        slow = head
        fast = head
        loopy = None
        # detect loop
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loopy = slow
                break
        if not loopy:
            return None
        # compute length of loop = k
        curr = loopy
        k    = 1
        while curr.next != loopy:
            curr = curr.next
            k += 1
        curr = head
        while k > 0:
            curr = curr.next
            k -= 1
        loopStart = head
        while loopStart != curr:
            loopStart = loopStart.next
            curr = curr.next
        return loopStart.val



def build123():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    return head

def build123456():
    head = build123()
    head.next.next.next = build123()
    return head

if __name__=="__main__":
    list1 = build123()
    s = Solution()
    print s.detectCycle(list1)