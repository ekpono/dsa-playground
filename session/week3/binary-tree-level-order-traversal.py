from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def getChildren(self, parent):
    #     children = []
    #     newParent = deque()

    #     while parent:
    #         child = parent.popleft()
    #         left = child.left
    #         right = child.right
    #         if left:
    #             children.append(left.val)
    #             newParent.append(left)
    #         if right:
    #             children.append(right.val)
    #             newParent.append(right)

    #     return (newParent, children)

    # def levelOrder(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[List[int]]
    #     """

    #     if not root:
    #         return []


    #     queue = deque([root])
    #     stack = [[root.val]]

    #     while queue:
    #         newparent, children = self.getChildren(queue)
    #         queue = newparent
    #         if len(children) > 0:
    #             stack.append(children)

    #     return stack
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result