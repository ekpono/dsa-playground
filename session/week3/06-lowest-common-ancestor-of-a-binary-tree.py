# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root

        if node is None:
            return None

        if node == p or node == q:
            return node

        left = self.lowestCommonAncestor(node.left, p, q)
        right =  self.lowestCommonAncestor(node.right, p, q)

        if left and right:
            return node

        return left or right
