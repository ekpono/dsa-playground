class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F') 
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# print("root.right.left.data:", root.right.right.left.data)

def preOrderTraversal(node):
    if node == None:
        return
    
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node == None:
        return
    
    inOrderTraversal(node.left)
    print(node.data, end=', ')
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node == None:
        return
    
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=', ')

# preOrderTraversal(root)
# print('\n')
# inOrderTraversal(root)
# print('\n')
# postOrderTraversal(root)
# print('\n')
# postOrderTraversal(nodeA)

# def divide(number):
#     # base case
#     if number < 1:
#         return
    
#     # pre
#     # print(number)
    
#     # recurse
#     divide(number / 2)
#     print('><<>')
#     print(number)

# 10*10=100
# def multiple(incrementor):
#     if incrementor == 11 or incrementor == 12:
#         return
    
#     print(10 * incrementor)

    
#     multiple(incrementor + 1)

#     print('>>>>>><<<<<<', incrementor)

#     multiple(incrementor + 2)

#     print('{{{}}}}}', incrementor)


# multiple(1)

def fibonacci(number):
    if number == 1:
        return 1
    
    print(number)

    
    return number + fibonacci(number - 1)




fibonacci(20)





    

    # post



# divide(8)

