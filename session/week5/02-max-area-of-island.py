# https://leetcode.com/problems/max-area-of-island/

"""
Move through all directions (island) you can find and sink them
then count the occurance in result and return
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        result = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def direction(x, y):

            if x >= rows or x < 0 or y >= cols or y < 0:
                return 0

            if grid[x][y] == 0:
                return 0

            grid[x][y] = 0
            area = 1
            for dx, dy in directions:
                area += direction(x + dx, y + dy)

            return area

        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if grid[x][y] == 1:
                    result = max(direction(x, y), result)

        return result