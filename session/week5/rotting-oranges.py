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
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1

        row = len(grid)
        column = len(grid[0])

        queue = deque()
        totalFresh = 0

        # scan and add all 2s into queue
        for x in range(row):
            for y in range(column):
                if grid[x][y] == 2:
                    queue.append((x,y))
                if grid[x][y] == 1:
                    totalFresh += 1

        def isValid(x, y):
            if x < 0 or y < 0:
                return False

            if x >= row or y >= column:
                return False

            if grid[x][y] != 1:
                return False

            return x, y
            # return 0 <= x < row and 0 <= y < column and grid[x][y] == 1

        minutes = 0

        # while queue:
        #     isIncremented = False
        #     for i in range(len(queue)):
        #         current_node = queue.popleft()
        #         x, y = current_node

        #         left = isValid(x - 1, y)
        #         right = isValid(x + 1, y)
        #         top = isValid(x, y + 1)
        #         bottom = isValid(x, y - 1)

        #         if left is not False:
        #             totalFresh -= 1
        #             grid[x - 1][y] = 2
        #             isIncremented = True
        #             queue.append((x - 1, y))

        #         if right is not False:
        #             totalFresh -= 1
        #             grid[x + 1][y] = 2
        #             isIncremented = True
        #             queue.append((x + 1, y))

        #         if top is not False:
        #             totalFresh -= 1
        #             grid[x][y + 1] = 2
        #             isIncremented = True
        #             queue.append((x, y + 1))

        #         if bottom is not False:
        #             totalFresh -= 1
        #             grid[x][y - 1] = 2
        #             isIncremented = True
        #             queue.append((x, y - 1))

        #     if isIncremented:
        #         minutes += 1
        # return -1 if totalFresh > 0 else minutes

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < column and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        totalFresh -= 1
                        queue.append((nx, ny))
            minutes += 1

        return -1 if totalFresh > 0 else minutes - 1 if minutes > 0 else 0