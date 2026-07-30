# https://leetcode.com/problems/count-the-number-of-complete-components/


class Solution(object):
    def countCompleteComponents(self, n, edges):
        visited = [0] * n
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(node):
            if visited[node]:
                return

            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        counter = 0
        for visit in range(n):

            if visited[visit] == 1:
                continue
            component = []
            dfs(visit)

            k = len(component)

            if sum(len(graph[v])  for v in component) == k * (k - 1):
                counter += 1

        return counter