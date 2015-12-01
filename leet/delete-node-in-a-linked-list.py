"""
Write a function to delete a node (except the tail)
in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4
and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next != None:
            node.val = node.next.val
            node.next = node.next.next 

if __name__ == '__main__':
    llist = ListNode(1)
    delNode = ListNode(3)
    llist.next = ListNode(2)
    llist.next.next = delNode
    llist.next.next.next = ListNode(4)

    sol = Solution()
    sol.deleteNode(delNode)