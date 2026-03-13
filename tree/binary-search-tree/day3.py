# Create a tree - done
# Link a tree - done
# Traversal ( in order, pre order and post order) done
# Search for a value
# Insert a node
# Find the lowest value
# Delete a node

class TreeNode:
        def __init__(self, data):
                self.left = None
                self.right = None
                self.data = data


root = TreeNode(13)

node7 = TreeNode(7)
node15 = TreeNode(15)

node3 = TreeNode(3)
node8 = TreeNode(8)

node14 = TreeNode(14)
node19 = TreeNode(19)

node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

def preOrderTraversal(node):
        if node is None:
                return None
        
        print(node.data, ', ')
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

def inOrderTraversal(node):
        if node is None:
                return
        
        inOrderTraversal(node.left)
        print(node.data, end=', ')
        inOrderTraversal(node.right)

def postOrderTraversal(node):
        if node is None:
                return None
        
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node.data, ', ')


# preOrderTraversal(root)
# inOrderTraversal(root)
# postOrderTraversal(root)