# Create a tree - done
# Link a tree - done
# Traversal ( in order, pre order and post order) done
# Search for a value
# Insert a node
# Find the lowest value
# Delete a node

class TreeNode():
        def __init__(self, node):
                self.data = node
                self.left = None
                self.right = None

root = TreeNode(20)

node18 = TreeNode(18)
node50 = TreeNode(50)

node17 = TreeNode(17)
node19 = TreeNode(19)

node47 = TreeNode(47)
node51 = TreeNode(51)

root.left = node18
root.right = node50

node18.left = node17
node18.right = node19

node50.left = node47
node50.right = node51

def inOrderTraversal(node):
        if node is None:
                return
        inOrderTraversal(node.left)
        print(node.data, ', ')
        inOrderTraversal(node.right)


# inOrderTraversal(root)

def preOrderTraversal(node):
        if node is None:
                return
        
        print(node.data, ', ')
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

def postOrderTraversal(node):
        if node is None:
                return
        
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node.data, ', ')

# print('\n')

# preOrderTraversal(root)

# print('\n')

# postOrderTraversal(root)

def search(node, data):
        if node is None:
                return
        
        if data < node.data:
                return search(node.left, data)
        elif data > node.data:
                return search(node.right, data)
        else:
                return node


# result = search(root, 50)
# print(result.data)

def insert(node, data) :
        if node is None:
                return TreeNode(data)
        else:
                if data < node.data:
                        node.left = insert(node.left, data)
                elif data > node.data:
                        node.right = insert(node.right, data)
        return node

def minValue(node):
        currentValue = node
        while currentValue.left is not None:
                currentValue = currentValue.left
        
        return currentValue

# value = minValue(root)
# print(value.data)

def delete(node, data):
        if node is None:
                return
        elif data < node.data:
                node.left = delete(node.left, data)
        elif node.data > data:
                node.right = delete(node.right, data)
        else:
                if node.left is None:
                        temp = node.right
                        node = None
                        return temp
                elif node.right is None:
                        temp = node.left
                        node = None
                        return temp
                else:
                        node.data = minValue(node.right).data
                        node.right = delete(node, node.data)
        return node

# inOrderTraversal(root)
print("------")
delete(root, 17)
inOrderTraversal(root)