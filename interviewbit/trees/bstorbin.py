'''
BST or Bin

Given a tree, determine if its BST or a regular Binary Tree

algo:
- perform in-order traversal and create list from values
- if list is sorted : BST
- else              : Binary Tree
'''

class Node:
  def __init__(self, val):
    self.val   = val;
    self.left  = None
    self.right = None

  def __str__(self):
    return '[' + str(self.left) + ']| ' + str(self.val) + ' |[' + str(self.right) + ']'

def createBST():
  root = Node(4)
  root.left = Node(2)
  root.left.left  = Node(1)
  root.left.right = Node(3)
  root.right = Node(7)
  root.right.right = Node(9)
  root.right.right.left = Node(8)
  root.right.right.right = Node(12)
  return root

def inorder_tail(root, acc):
  if root.left:
    inorder_tail(root.left, acc)
  acc.append(root.val)
  if root.right:
    inorder_tail(root.right, acc)

def inorder(node):
  temp = []
  if node.left:
    temp = temp + inorder(node.left)
  temp.append(node.val)
  if node.right:
    temp = temp + inorder(node.right)
  return temp

import unittest

class Tester(unittest.TestCase):

  def testBSTtail(self):
    tree = createBST()
    treelist = []
    inorder_tail(tree, treelist)
    self.assertEqual(treelist, sorted(treelist))

  def testBST(self):
    tree = createBST()
    treelist = inorder(tree)
    self.assertEqual(treelist, sorted(treelist))

  def testNotBST(self):
    tree = createBST()
    tree.val = 40 # violate BST property
    treelist = inorder(tree)
    self.assertNotEqual(treelist, sorted(treelist))

if __name__ == '__main__':
  unittest.main()