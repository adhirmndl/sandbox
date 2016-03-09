class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createDummyTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    return root

def inorder(root):
    if (root is None):
        return '|'
    return inorder(root.left) + ' ' + str(root.data) + ' ' + inorder(root.right)

if __name__ == "__main__":
    root = createDummyTree()
    print inorder(root)

