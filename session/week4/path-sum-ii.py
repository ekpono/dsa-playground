# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        current_path = []
        result = []

        def crawler(node, remainder, paths):
            if node is None:
                return node

            remainder = remainder - node.val
            paths.append(node.val)

            if node.left is None and node.right is None:
                if remainder == 0:
                    result.append(paths[:])

            crawler(node.left, remainder, paths)
            crawler(node.right, remainder, paths)

            paths.pop()

            return node


        crawler(root, targetSum, current_path)

        return result