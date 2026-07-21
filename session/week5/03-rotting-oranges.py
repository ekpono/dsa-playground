# https://leetcode.com/problems/rotting-oranges/
"""
how to solve this problem
Count of row and column of the 2D matrix
Get all rotten x, y in queue and count all fresh
perform what is called Multi-source BFS on everything by looping through
everything in the queue and going on every 4 bidirection (left, right, top, bottom)
if it is not valid e.g out of bounds, mark the grid as rotten, decrement totalFresh and add it to queue
and lastly return -1 if totalFresh still exists, or minutes - 1 if minute is more than 0, else 0
"""
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1

        rows, columns = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        queue = deque()

        # fill up queue
        for x in range(rows):
            for y in range(columns):
                if grid[x][y] == 2:
                    queue.append((x, y))
                if grid[x][y] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < columns and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))

            minutes += 1

        print(minutes, fresh)
        return minutes if fresh == 0 else -1