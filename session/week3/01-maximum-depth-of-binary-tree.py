# https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
Use recursion to walk through the tree. At each node, return 1 + the maximum depth of the left and right subtrees. If you reach a null node, return 0.


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
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