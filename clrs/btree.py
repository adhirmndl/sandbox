class Node:
    data  = None
    left  = None
    right = None
    def __init__(self, data):
        data = data

def lookup(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    if node.data < target:
        return lookup(node.right, target)
    else:
        return lookup(node.left, target)

def insert(node, value):
    return
