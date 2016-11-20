'''
BTree to List

Given a tree, return an in-order linked list

algo:
'''

class Node:
  def __init__(self, val):
    self.val   = val;
    self.left  = None
    self.right = None

  def __str__(self):
    return '[' + str(self.left) + ']| ' + str(self.val) + ' |[' + str(self.right) + ']'

def createBTree():
  root = Node(4)
  root.left = Node(2)
  root.left.left  = Node(1)
  root.left.right = Node(3)
  root.right = Node(7)
  root.right.right = Node(9)
  root.right.right.left = Node(8)
  root.right.right.right = Node(12)
  return root

def btree2list(root):
  if root.left:
    btree2list(root.left)
  temp = root.right
  root.right = root.left
  if temp:
    btree2list(temp)
    curr = temp.left
    if curr:
      while curr.right:
        curr = curr.right
      curr.right = root
      root = temp.left
  return root



import unittest

class Tester(unittest.TestCase):

  def testbtree2list(self):
    tree = createBTree()
    treelist = btree2list(tree)
    print treelist

if __name__ == '__main__':
  unittest.main()