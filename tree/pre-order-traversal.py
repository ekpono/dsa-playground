def preOrderTraversal(node):
    if node == None:
        return
    
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)