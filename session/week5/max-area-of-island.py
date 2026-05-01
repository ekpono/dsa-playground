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
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])

        def direction(x, y):

            if x is None or y is None:
                return 0

            if x >= number_of_rows or x < 0 or y >= number_of_columns or y < 0:
                return 0

            if grid[x][y] == 0:
                return 0

            grid[x][y] = 0
            top = direction(x + 1, y) # top
            bottom = direction(x - 1, y) # bottom
            right = direction(x, y + 1) # right
            left = direction(x, y - 1) # left

            return 1 + sum([top, bottom, right, left])

        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if grid[x][y] == 1:
                    result = max(direction(x, y), result)

        return result
