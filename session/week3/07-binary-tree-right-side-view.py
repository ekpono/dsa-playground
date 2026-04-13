# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def crawler(self, node, result):
    #     if node is None:
    #         return None


    #     right = self.crawler(node.right, result)
    #     left = self.crawler(node.left, result)

    #     if right:
    #         result.append(node.val)
    #     else:
    #         result.append(node.val)
    #     return node
    # def crawler(self, left, right):


    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)


        return result













        # result = [root.val]
        # self.crawler(root.right, result)

        # node = root.left

        # newArray = []
        # self.crawler(root.left, newArray)

        # final = newArray[len(result) - 1:]

        # return sorted(result + final)















        # queue = deque([root])
        # result = []

        # while queue:

        #     for _ in range(len(queue)):
        #         print(len(queue))
        #         node = queue.popleft()

        #         if node.right:
        #             queue.append(node.right)
        #             result.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #             result.append(node.val)


        # return result

















        # result = [root.val]

        # queue = deque([root])


        # while queue:
        #     for _ in range(len(queue)):
        #         print(len(queue))
        #         node = queue.popleft()

        #         if node.right:
        #             result.append(node.right.val)
        #             queue.append(node.right)

        #         if node.left:
        #             queue.append(node.left)

        # return result






