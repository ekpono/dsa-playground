# https://leetcode.com/problems/number-of-islands/
"""
Move through all directions (island) you can find and sink them
then count the occurance in result and return
"""
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

class Solution(object):
    def numIslands(self, grid):
        result = 0

        if not grid:
            return result

        rows, cols = len(grid), len(grid[0])

        def dfs(x, y):
            print(x, y)
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != "1":
                return

            grid[x][y] = "0"

            for dx, dy in dirs:
                dfs(x + dx, y + dy)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    result += 1
                    dfs(x, y)


        return result
