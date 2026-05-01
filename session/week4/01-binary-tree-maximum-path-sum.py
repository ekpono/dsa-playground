# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        def crawler(node):
            if node is None:
                return 0

            left_gain = max(crawler(node.left), 0)
            right_gain = max(crawler(node.right), 0)

            self.max_sum = max(node.val + left_gain + right_gain, self.max_sum)

            return node.val + max(left_gain, right_gain)

        crawler(root)

        return self.max_sum
