# Traversal
# Search for a value
# Insert a node
# Find the lowest value
# Delete a node


# TRAVERSAL

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, 
# followed by a recursive pre-order traversal of the right subtree. It's used for creating a copy of the tree, prefix 
# notation of an expression tree, etc.
# This traversal is "pre" order because the node is visited "before" the recursive pre-order traversal of the left and right subtrees.
def preOrderTraversal(node):
    # base
    if node is None:
        return
    
    # pre
    print(node.data, ', ')
    
    # recurse
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


# In-order Traversal
# In-order Traversal is a type of Depth First Search, where each node is visited in a certain order.
# In-order Traversal is mainly used for Binary Search Trees where it returns values in ascending order.
# In-order Traversal does a recursive In-order Traversal of the left subtree, 
# visits the root node, and finally, does a recursive In-order Traversal of the
#  right subtree. This traversal is mainly used for Binary Search Trees where 
# it returns values in ascending order.


def inOrderTraversal(node):
    # base
    if node is None:
        return
    # pre
    inOrderTraversal(node.left)

    print(node.data, end=', ')
    # post
    inOrderTraversal(node.right)



# Post-order Traversal is a type of Depth First Search, where each node is visited in a certain order
# Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the 
# right subtree, followed by a visit to the root node. 
# It is used for deleting a tree, post-fix notation of an expression tree, etc.
# What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.l
def postOrderTraversal(node):
    if node is None:
        return

    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, ', ')

root = TreeNode(13)
node7 = TreeNode(7)
node2 = TreeNode(2)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)
node20 = TreeNode(20)
node21 = TreeNode(21)

root = root

root.left = node7
root.right = node20

node7.left = node3
node7.right = node8

node20.left = node18


# Execute
# inOrderTraversal(root)


# SEARCH A NODE in Binary search tree

def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

# result = search(root, 7)

# if result:
#     print(f"\n Found the node with value: {result.data}")
# else:
#     print("\n Value not found in the BST")

def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

# insert(root, 51)
# preOrderTraversal(root)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    
    return current

min = minValueNode(root)

# print(min)

# value = minValueNode(root)
# print(value.data)
def delete(node, data):
    if node is None:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            print('here is triggered')
            temp = node.left
            node = None
            return temp
        else:
            print('here is triggered 7')

            node.data = minValueNode(node.right).data
            node.right = delete(node.right, node.data)
    return node

    
inOrderTraversal(root)
print('\n')
delete(root,7)

inOrderTraversal(root)

# def balancedHeight(root):
#     currentRight = root
#     currentLeft = root
#     leftNum = 0
#     rightNum = 0
#     while currentLeft.left is not None:
#         currentLeft = currentLeft.left
#         leftNum += 1
    
#     while currentRight.right is not None:
#         currentRight = currentRight.right
#         rightNum += 1
    
#     print(leftNum, rightNum)
#     if (leftNum - rightNum) > 1:
#         return True
#     return False



# def isBalance(root):
#     res = [1]
    
#     def maxDepth(root):
#         if root is None:
#             return 0
#         left = maxDepth(root.left)
#         right = maxDepth(root.right)

#         if abs(left - right) > 1:
#             res[0] = 0
#         return 1 + max(left, right)
#     maxDepth(root)
#     return True if res[0] == 1 else False



# solu = isBalance(root)
# print(solu)

# # print(res)