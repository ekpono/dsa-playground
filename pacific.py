# This is the hardest problem of both weeks. Multi-source DFS from two different boundaries simultaneously. Don't rush into it.
# Tonight — just read the problem statement. Draw the grid. Think about what "Pacific" and "Atlantic" mean in terms of which edges of the grid they touch.

# pacific
# top
# left

# atlantic 
# bottom
# right
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        results = []
        height = len(heights)
        width = len(heights[0])

        visited = [ [0] * width for i in range(height) ]

        height = len(heights)
        width = len(heights[0])

        def right (island, row, col):
            for i in range(col + 1, width):
                if heights[row][i] > island:
                    return False

            return True
        
        def top (island, row, col):

            for i in range(row):
                print(heights[i][col], 'top')
                if heights[i][col] > island:
                    return False

            return True
        
        results = []

        level = 0

        for row in range(width):
            for col in range(height):
                island = heights[row][col]

                # rightx = right(island, row, col)

                topx = top(island, 3, 0)
                # print(topx, row, col)

                # print(topx)
                break
                # if rightx:
                #     results.append([row, col])
            level += 1

            if level == 1:
                break
        
        return results



heights = [ [1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4] ]

req = Solution()
pipeline = req.pacificAtlantic(heights)

expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4, 0]]

# print('RESPONSE', pipeline)
# print('EXPECTED', expected)

# assert pipeline == expected

# print(True)








