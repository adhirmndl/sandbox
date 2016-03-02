"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wronte (Homebrew),
but you can't invert a binary tree on a whiteboard, so fuck off.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
    	return str(self.val) + ' [' + str(self.left) + ',' + str(self.right) + '] '

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
        	return
        tmpNode    = root.left
        root.left  = root.right
        root.right = tmpNode
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == '__main__':

    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)

    tree.right = TreeNode(7)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)

    rtree = TreeNode(10)
    rtree.right = TreeNode(35)
    rtree.right.right = TreeNode(35)
    rtree.right.right.left = TreeNode(35)
    rtree.left = TreeNode(32)
    

    print tree
    sol = Solution()
    print sol.invertTree(tree)
