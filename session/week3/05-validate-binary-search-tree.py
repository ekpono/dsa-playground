# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def validate(self, node, min_val, max_val):
        if node is None:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (self.validate(node.left, min_val, node.val) and
                self.validate(node.right, node.val, max_val))

    def isValidBST(self, root):
        return self.validate(root, float('-inf'), float('inf'))



