# https://leetcode.com/problems/number-of-provinces/
"""
This is an adjecency matrix problem, meaning each row points to rows that are connected to it
e.g [1,0,1] means row one points to itself and row three, but not row two
so we can perform DFS on each row and mark all the rows that are connected to it as visited, and count the number of times we have to perform DFS, which is the number of provinces
"""
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        provinces = 0
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            visited[i] = True
            for y in range(n):
                if isConnected[i][y] == 1 and not visited[y]:
                    dfs(y)


        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1


        return provinces
