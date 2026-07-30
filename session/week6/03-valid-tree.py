# https://neetcode.io/problems/valid-tree/history?submissionIndex=8

"""
There are two conditions that must be true for a graph to be a valid tree
1. It must not be cyclic
2. Every node must be reached

To solve this problem, first you use the edges to create adjacency list
Since it is undirected tree (A points to B, and B points to A), you pass a parent so it won't count parent as cyclic
It recurses through the entire tree, if it has found a node it has already visited, then cylic is detected
After the dfs has finished, it check to see if all the node are visited to detect if the tree is connected
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n - 1 != len(edges):
            return False

        graph = {}

        for a, b in edges:
            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)

        visited = [0] * n

        def dfs(i, parent):
            if visited[i] == 1:
                return False

            visited[i] = 1

            if i in graph:
                for neighbor in graph[i]:
                    if neighbor == parent:
                        continue
                    if not dfs(neighbor, i):
                        return False

            return True

        if not dfs(0, -1):
            return False

        if 0 in visited:
            return False

        return True





