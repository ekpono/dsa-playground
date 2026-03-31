# https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
Use recursion to walk through the tree. At each node, return 1 + the maximum depth of the left and right subtrees. If you reach a null node, return 0.
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        return self.walker(root)

    def walker(self, node):
        if node is None:
            return 0

        return 1 + max(self.walker(node.left), self.walker(node.right))