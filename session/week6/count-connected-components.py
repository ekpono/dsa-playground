# https://neetcode.io/problems/count-connected-components/question

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i: [] for i in range(n)}
        visits = [False] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(node):
            if visits[node]:
                return

            visits[node] = True
            for neigbor in graph[node]:
                dfs(neigbor)

        count = 0

        for i in range(len(visits)):
            if visits[i]:
                continue

            count += 1
            dfs(i)


        return count





