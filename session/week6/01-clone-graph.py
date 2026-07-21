# https://leetcode.com/problems/clone-graph/

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        cloned_nodes = {}

        def dfs(currNode):
            if currNode in cloned_nodes:
                return cloned_nodes[currNode]


            copy = Node(currNode.val)
            cloned_nodes[currNode] = copy

            for neighbor in currNode.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)




