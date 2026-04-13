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



        # if node.val == p.val or node.val == q.val:
        #     if node.right:
        #         if node.right.val == p.val or node.right.val == q.val:
        #             return node
        #     if node.left:
        #         if node.left.val == p.val or node.left.val == q.val:
        #             return node
        #     if self.finder(node.left, p.val) or self.finder(node.left, q.val):
        #         return node
        #     if self.finder(node.right, p.val) or self.finder(node.right, q.val):
        #         return node

        # if node.left and node.right:
        #     if (node.left.val == q.val or node.left.val == p.val) and (node.right.val == q.val or node.right.val == p.val):
        #         return node

        # if node.left:
        #     if node.left.val == q.val or node.left.val == p.val:
        #         result1 = self.finder(node.right, p.val)
        #         result2 = self.finder(node.right, q.val)
        #         if result1 is True or result2 is True:
        #             return node
        #         elif self.finder(node.left, p.val) or self.finder(node.left, q.val):
        #             return node.left


        # if node.right:
        #     if node.right.val == q.val or node.right.val == p.val:
        #         result1 = self.finder(node.left, p.val)
        #         result2 = self.finder(node.left, q.val)
        #         if result1 is True or result2 is True:
        #             return node
        #         elif self.finder(node.right, p.val) or self.finder(node.right, q.val):
        #             return node.right

        # if node.val == p.val or node.val == q.val:
        #     if node.right:
        #         if node.right.val == p.val or node.right.val == q.val:
        #             return node
        #     if node.left:
        #         if node.left.val == p.val or node.right.val == q.val:
        #             return node

        # return self.lowestCommonAncestor(node.left, p, q) or self.lowestCommonAncestor(node.right, p, q)







        # left = self.finder(node.left, p.val)

        # if left:
        #     right = self.finder(node.right, q.val)
        #     if right:
        #         return node
        #     left = self.finder(node.left, q.val)
        #     if left:
        #         return node.left

        # right = self.finder(node.right, p.val)
        # if right:
        #     print(node.right)
        #     right = self.finder(node.left, q.val)
        #     if right:
        #         return node
        #     left = self.finder(node.right, q.val)
        #     if left:
        #         print(left)
        #         print('pwee')
        #         return node.right

        # left = self.finder(node.left, q.val)

        # if left:
        #     right = self.finder(node.right, p.val)
        #     if right:
        #         return node
        #     left = self.finder(node.left, p.val)
        #     if left:
        #         return node.left

        # right = self.finder(node.right, q.val)
        # if right:
        #     right = self.finder(node.left, p.val)
        #     if right:
        #         return node
        #     left = self.finder(node.right, p.val)
        #     if left:
        #         return node.right

        # # current node
        # if node.val == q.val or p.val:
        #     return node













        # if node is None:
        #     return None

        # if node.left and node.left.val == p.val:
        #     if self.finder(node.left, q.val):
        #         print('found 1', node.left.val)
        #         return node.left
        #     elif self.finder(node.right, q.val):
        #         print('found 2', node.right.val)
        #         return node

        # if node.right and node.right.val == q.val:
        #     if self.finder(node.right, q.val):
        #         print('found 3', node.right.val)
        #         return node.right
        #     elif self.finder(node.left, q.val):
        #         print('found 4', node.right.val)
        #         return node

        # return self.lowestCommonAncestor(node.left, p, q) or self.lowestCommonAncestor(node.right, p, q)



        # node = root

        # if node is None:
        #     return None

        # if node.val == p.val or node.val == q.val:
        #     return node

        # if node.left and node.left.val == p.val or q.val:
        #     return node

        # if node.right and node.right.val == p.val or q.val:
        #     return node

        # self.lowestCommonAncestor(node.left, p, q)
        # self.lowestCommonAncestor(node.right, p, q)
