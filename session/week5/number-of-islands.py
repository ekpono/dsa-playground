# https://leetcode.com/problems/number-of-islands/
"""
Move through all directions (island) you can find and sink them
then count the occurance in result and return
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        result = 0
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])

        def direction(x, y):
            if x >= number_of_rows or x < 0 or y >= number_of_columns or y < 0:
                return
            if grid[x][y] == "0":
                return
            grid[x][y] = "0"
            direction(x + 1, y) # top
            direction(x - 1, y) # bottom
            direction(x, y + 1) # right
            direction(x, y - 1) # left

        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if grid[x][y] == "1":
                    result += 1
                    direction(x, y)

        return result
